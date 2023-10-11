# Problem 3. From the Triangle to the Decagon.
# Draw a sequence of n-angles figures. Each figure has the same length of the side.
# Use different colors for each figure.
# Learning objections: how to change the color of the drawing (check docs).
# Can you speed up a turtle?

import random
import turtle as tur

t = tur.Turtle()

t.speed(0)
t.pensize(5)
t.forward(100)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

for n in range(3, 11):
    t.color(random.choice(colors))

    for s in range(n):
        t.right(360 / n)
        t.forward(100)

t.screen.mainloop()
