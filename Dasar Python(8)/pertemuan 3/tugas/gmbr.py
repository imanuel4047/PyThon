import turtle
frank =turtle.Turtle()

frank.speed(500)
for x in range(1000):
    canvas=turtle.Screen()
    frank.pencolor("red")
    frank.forward(x)
    frank.left(30)
    frank.circle(100)