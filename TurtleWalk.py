#from turtle import Turtle ,screen


# timmy_the_turtle=Turtle()
# timmy_the_turtle.shpae("turtle")
# timmy_the_turtle.color("Red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(100)
#     timmy_the_turtle.up(100)
#     timmy_the_turtle.down(100)

#**************************************#
#tim =turtle.Turtle()
# from turtle import Turtle

# tim=Turtle()
# tom=Turtle()
# terry=Turtle()

# from turtle import *
# from random import *


#choice([1,2,3,4])

#*******************TURTLE CHALLENGE 2 DRAW A DASHED LINE************#
# import random
# import turtle as t

# tim = t.Turtle()
# for _ in range(15):

#  tim.forward(10)
# tim.penup()
# tim.forward(10)
# tim.pendown()

# #import turtle as t
# #tim = t.Turtle()
# colours=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
# num_sides =5
# for  _ in range(num_sides):
#    Abhishek =360/ num_sides

# tim.forward(100)
# tim.right(Abhishek)

# def draw_shape(num_sides):
#     angel=360/num_sides
#     for  _ in range(num_sides):
#         tim.forward(100)
#         tim.right(Abhishek)
    
# for shape_size_n in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_size_n)

#***************DRAW RANDOM WALK ***************#
import turtle as t
import random

# Setup the turtle
tim = t.Turtle()
tim.pensize(5)
tim.speed("fastest")

# Define directions (0=East, 90=North, 180=West, 270=South)

directions = [0, 90, 180, 270]

# Generate random RGB colors directly 

t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Random Walk Loop

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

# Keep window open
t.mainloop()

