from turtle import Turtle, Screen
from pprint import pprint

timmy = Turtle()
timmy.speed(0)
timmy.penup()
timmy.setposition(-250, -250)
timmy.pendown()
screen = Screen()
screen.listen()


def forward():
    timmy.forward(15)


def backward():
    timmy.back(15)


def turn_clockwise():
    current_heading = timmy.heading()
    timmy.setheading(current_heading-5)


def turn_anticlockwise():
    current_heading = timmy.heading()
    timmy.setheading(current_heading+5)


def clear_drawing():
    screen.resetscreen()


screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(turn_anticlockwise, "a")
screen.onkey(turn_clockwise, "d")
screen.onkey(clear_drawing, "c")


screen.exitonclick()
