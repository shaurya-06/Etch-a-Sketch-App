from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def rotate_clockwise():
    tim.setheading(tim.heading() - 10)


def rotate_anti_clockwise():
    tim.setheading(tim.heading() + 10)


screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=rotate_clockwise, key="d")
screen.onkey(fun=rotate_anti_clockwise, key="a")
screen.onkey(fun=screen.resetscreen, key="c")
screen.exitonclick()
