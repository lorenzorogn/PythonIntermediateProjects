import turtle
import random 

timmy = turtle.Turtle()
turtle.colormode(255)

# drawing different shapes 
"""angoli = 3
def random_color():
    r = random.randrange(0, 255)
    b = random.randrange(0, 255)
    g = random.randrange(0, 255)
    random_color = (r,g,b)
    return random_color

for _ in range(8):
    timmy.color(random_color())
    for _ in range(angoli):
        svolte = 360 / angoli 
        timmy.forward(100)
        timmy.right(svolte)
    angoli += 1"""

# draw a random walk

"""def random_color():
    r = random.randrange(0, 255)
    b = random.randrange(0, 255)
    g = random.randrange(0, 255)
    random_color = (r,g,b)
    return random_color

timmy.speed(0)
timmy.pensize(10)

direction = [0, 90, 180, 270]  

while timmy:
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))"""
    


# draw a spirograph

def random_color():
    r = random.randrange(0, 255)
    b = random.randrange(0, 255)
    g = random.randrange(0, 255)
    random_color = (r,g,b)
    return random_color

timmy.speed(0)

def draw_spirograph(size_of_gap):
    for _ in range(int((360 / size_of_gap))):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)

my_screen = turtle.Screen()
my_screen.exitonclick()