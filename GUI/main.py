import random
import turtle
from turtle import Turtle, Screen

# Graphical User Interface

tim = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_rgb = (r, g, b)
    return color_rgb


# draw shape
def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for n in range(3, 11):
    tim.color(random_color())
    draw_shape(n)


# draw random walk
direction = [0, 90, 180, 270]


def random_walk():
    tim.pensize(10)
    tim.speed(10)
    tim.forward(30)
    tim.color(random_color())
    tim.setheading(random.choice(direction))


for n in range(200):
    random_walk()


# draw spirograph
def draw_spirograph(size_of_gap):
    tim.speed('fastest')
    tim.setheading(0)
    for _ in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


# draw hirst painting
dot_size = 20
step_size = 50
x_position = -225
y_position = -225

for _ in range(10):
    tim.penup()
    tim.hideturtle()
    tim.setposition(x_position, y_position)
    y_position += step_size
    for _ in range(10):
        tim.penup()
        tim.dot(dot_size, random_color())
        tim.forward(step_size)


screen = Screen()
screen.exitonclick()



















