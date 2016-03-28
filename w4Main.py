import turtle
wn= turtle.Screen()
t1=turtle.Turtle()

def makeSwirlSquare(size, bigger, sides, angle):
    for i in range(0, sides):
        if i%2:
            size=size+bigger
        t1.fd(size)
        t1.left(angle)
        

makeSwirlSquare(10,10,10,90)       

wn.exitonclick()