"""
import random

def my_generator():

    for x in range(10):
        yield random.randint(1,5)

for val in my_generator():
    print(val) 
"""


def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 100:
            break


# in many cases, you really don't need to actually write a generator over just writing a generator
# expression. it's also more Pythonic to go ahead and just write the generator expression since it's simpler.
# that said, you should still know how to write a generator, since it will give you a bit more 
# insight into how generators work, and what iterable object really are, since, despite looking
# a lot like list comprehension, generators are very unique in how they act. also, you will want 
# to be able to know a generator when you see it.

# generators don't return things, they yield things, in a stream. this can be done on iterables, 
# which has been already illustrated, but also can be based purely in logic, whatever you want.
# for example:

"""
def simple_gen():
    yield "oh"
    yield "hello"
    yield "there"
"""

# there's our generator, super basic. now we can actually iterate over it:

"""
for i in simple_gen():
    print(i)
"""

# you can add logic to the yield statements, whatever you want. let's consider a scenario where
# we want to find the combination to a lock, one of the ones where you spin the dials, and each
# dial has 0-9 on it, and we need to get the perfect combination to unlock the lock. how might a 
# beginner approach this problem? i know how i would have started:

"""
correct_combo = (3, 6, 1)

for c1 in range(10):
    for c2 in range(10):
        for c3 in range(10):
            if (c1, c2, c3) == correct_combo:
                print("found the combo:{}".format((c1, c2, c3)))
"""

# sure enough, we do get the right answer: found the combo:(3, 6, 1)

# so what's the problem? well, even after we've found the combo, we continue to iterate through
# "all" of the combinations. luckily for us, the calculation is super cheap, but this code doesn't
# scale at all. even as beginners though, we know about the break statement. can't we just call it like:

"""
correct_combo = (3, 6, 1)

for c1 in range(10):
    for c2 in range(10):
        for c3 in range(10):
            if (c1, c2, c3) == correct_combo:
                print("found the combo:{}".format((c1, c2, c3)))
                break
"""

# you can but you're saving yourself the processing of less than 10 out of a thousand operations.
# hmm. okay, we might be beginners, but we're still crafty. we'll have breaking logic for all of the lines.
# to do this, we're going to introduce a new var: found_combo, which we'll set to False to start, 
# but then update to True if we find the combo. then, we'll have an if statement to see if we
# found the combo at each step, and then break if that's the case!

"""
found_combo = False
correct_combo = (3, 6, 1)

for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            print(c1, c2, c3)
            if (c1, c2, c3) == correct_combo:
                print("found the combo:{}".format((c1, c2, c3)))
                found_combo = True
                break
"""

#great, we've done it! is this pythonic though? it meets PEP 8 standards... but this is one 
# of the reasons why you need to take PEP 8 with a grain of salt, or, better put, think about 
# PEP 8 only as you're writing code, but, after that, we need to assess whether or not it's 
# "pythonic". there's a better way. since this is a generator tutorial, i suppose you might already
# know the answer is going to be a generator.

# for the generator, we really need to just iterate through the combinations, the logic is nothing
# new or surprising:

"""
correct_combo = (3, 6, 1)

def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

# then, to actually make use of it:

for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == correct_combo:
        print("found the combo:{}".format((c1, c2, c3)))
        break
"""

# once we beak, the generator stream stops, and we're done.

# this code is only 2 lines of actual code shorter( 1 if we count while space), but it's easier
# to read and understand, and is certainly more beautiful.


