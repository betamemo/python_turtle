import turtle as tur

import colorgram

cg = colorgram.extract('img/image.jpeg', 25)
colors = []
for color in cg:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    colors.append(rgb)

t = tur.Turtle()
t.penup()
t.screen.colormode(255)
t.goto(-250, 250)

for i in range(1, 26):
    t.dot(80, colors[i - 1])
    t.forward(120)
    if i % 5 == 0:
        t.setheading(270)
        t.forward(120)

        if i % 10 == 0:
            t.setheading(0)
        else:
            t.setheading(180)
        t.forward(120)

t.screen.mainloop()
