# Draw a square. (It may have any size or even shape).
# Learning objections: install dependencies and import module, create an object,
# explore methods forward(), right()/left(), and .screen.mainloop()
# How to change shape.

import turtle as tur

t = tur.Turtle()

for s in range(4):
    t.forward(100)
    t.right(90)

t.screen.mainloop()
