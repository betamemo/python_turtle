import turtle as tur

t = tur.Turtle()

t.speed(0)

for i in range(10):
    for color in ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'):
        t.color(color)
        t.circle(100)
        t.left(10)

t.screen.mainloop()
