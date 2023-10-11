# Draw a dotted line. (Any length, any thickness, any color, any direction)
# Learning objections: there is a hydraulic pen connected to the turtle's butt,
# it’s possible to turn it on and off with penup and pendown methods.

import turtle as tur

t = tur.Turtle()
t.penup()

for s in range(4):
    for d in range(10):
        t.dot(20, 'violet')
        t.forward(20)
    t.right(90)

t.screen.mainloop()
