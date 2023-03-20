# import colorgram 

# colors = colorgram.extract("Hirst.jpg", 30)
# rgb = []
# variabile = 0
# for _ in colors:
#     rgb.append(())
#     first_colors = colors[variabile]
#     mytuple = first_colors.rgb
#     rgb[variabile] = tuple(mytuple)
#     variabile += 1
# print(rgb)


# lei lo fa così 

"""
rgb_colors = []
colors = colorgram.extract("Hirst.jpg", 10)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)"""

import turtle as t
import random

color_list = [(202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244),
                (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), 
                (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), 
                (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), 
                (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174),
                (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), 
                (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.hideturtle()
tim.goto(-176.78,-176.78)


def move():
    for _ in range(10):    
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

position = -176.87        
for _ in range(10):
    tim.goto(-176.78, position)
    move()
    position += 50



my_screen = t.Screen()
my_screen.exitonclick()