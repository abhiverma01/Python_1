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

#***************DRAW RANDOM WALK :( Final Code )***************#
# import turtle as t
# import random

# tim = t.Turtle()
# tim.pensize(5)
# tim.speed("fastest")

# directions = [0, 90, 180, 270]

# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# t.mainloop()

#******************** Turtle Challenge : DRAW a Spirograph ***************#
import turtle as t
import random

# Setup turtle and speed
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)

# Generate a random RGB color tuple
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    # Calculate the exact number of circles needed to complete a 360-degree rotation

    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100) 
        
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()


