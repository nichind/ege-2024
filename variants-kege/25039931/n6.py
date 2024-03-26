import turtle as t


t.color("black", "blue")
t.tracer(2)
k = 20


t.begin_fill()
x, y = 0, 0
for i in range(10):
    def ch():
        t.goto((x, y))
        print(t.pos())

    for n in [[0,2],[2,0],[0,10],[-2,0],[0,2],[6,0],[0,-2],[-2,0],[0,-10],[2,0],[0,-2],[-6,0]]:
        x += n[0] * k
        y += n[1] * k
        ch()


t.end_fill()

t.penup()
canvas = t.getcanvas()

c = 0
for x in range(-100 * k, 100 * k, k):
    for y in range(-100 * k, 100 * k, k):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item):
            c += 1

print(c)
t.update()

t.done()