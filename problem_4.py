# Problem 4. Random walk.
# There is such thing as random walk https://en.wikipedia.org/wiki/Random_walk
# The model of random walk has a tons of applications in physics, math, and many other fields. Let's build this simulation. Rules:
# 1. Each step has the same length.
# 2. Each step has a different random color.
# Please, choose your favorite colors out of this table: https://cs111.wellesley.edu/labs/lab02/colors

import random
import turtle as tur

t = tur.Turtle()
t.pensize(5)
t.speed(0)

angles = [0, 90, 180, 270]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

while True:
    angle = random.choice(angles)
    color = random.choice(colors)

    t.setheading(angle)
    t.color(color)
    t.forward(20)

t.screen.mainloop()
