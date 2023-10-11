import turtle as tur

t = tur.Turtle()
t.speed(0)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

for i in range(10):
    for color in colors:
        t.color(color)
        t.circle(100)
        t.right(10)

t.screen.mainloop()
