from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def left_angle():
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)


def right_angle():
    current_heading = tim.heading()
    tim.setheading(current_heading - 10)


def clear_screen():
    tim.setheading(0)
    tim.setposition(0.0, 0.0)
    tim.clear()


screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(left_angle, "a")
screen.onkey(right_angle, "d")
screen.onkey(clear_screen, "c")

screen.listen()
screen.exitonclick()