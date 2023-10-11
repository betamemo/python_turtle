import turtle as t

bob = t.Turtle()
screen = t.Screen()
screen.listen()


def go_up():
    bob.setheading(90)
    bob.forward(10)


def go_down():
    bob.setheading(270)
    bob.forward(10)


def go_left():
    bob.setheading(180)
    bob.forward(10)


def go_right():
    bob.setheading(0)
    bob.forward(10)


screen.onkeypress(fun=go_up, key='Up')
screen.onkeypress(fun=go_down, key='Down')
screen.onkeypress(fun=go_left, key='Left')
screen.onkeypress(fun=go_right, key='Right')
bob.screen.mainloop()
