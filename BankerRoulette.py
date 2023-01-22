import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

banana = random.randrange(len(names))

print("{} is going to buy the meal today!".format(names[banana]))

# si può utilizzare anche randint che parte da 0 fino a len().
# bisogna creare una variabile per la formula len e poi metterla nel codice
# minore di 1: random.randint(0, "variabile" - 1)