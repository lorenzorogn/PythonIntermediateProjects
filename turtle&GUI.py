import turtle
import random 

timmy = turtle.Turtle()

# drawing different shapes 
"""angoli = 3
def colormio():
    r = random.randrange(0, 255)
    b = random.randrange(0, 255)
    g = random.randrange(0, 255)
    turtle.colormode(255)
    timmy.color(r,g,b)

for _ in range(8):
    colormio()
    for _ in range(angoli):
        svolte = 360 / angoli 
        timmy.forward(100)
        timmy.right(svolte)
    angoli += 1"""

# draw a random walk

def colormio():
    r = random.randrange(0, 255)
    b = random.randrange(0, 255)
    g = random.randrange(0, 255)
    turtle.colormode(255)
    timmy.color(r,g,b)

timmy.speed(3)
timmy.pensize(3)


def movimento(direzione):
    timmy.direzione(50)

    
move = random.choice(["right", "back", "left"])


while timmy:
    colormio()
    movimento(move)
    timmy.forward(50)
    

my_screen = turtle.Screen()
my_screen.exitonclick()