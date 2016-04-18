import turtle
import random
wn=turtle.Screen()
t1=turtle.Turtle()

t1.shape("turtle")
t1.pencolor("Red")

def drawSquareAtSave(size,pos):
    tracks1=list()
    t1.penup()
    t1.setpos(pos)
    for i in range(0,4):
            t1.fd(size)
            t1.left(90)
            tracks1.append(t1.pos())
    return tracks1
        
def drawSqareFront_list(tracks1):
    t1.penup()
    t1.goto(tracks1[3])
    t1.pendown()
    for i in range(0,4):
        t1.goto(tracks1[i])

for i in range(6):
    t1.speed(10)
    pos=(random.randrange(-300,300),random.randrange(-300,300))
    drawSqareFront_list(drawSquareAtSave(40,pos))

def drawTriaangleAtSave(size,pos):
    tracks2=list()
    t1.penup()
    t1.setpos(pos)
    for i in range(0,3):
            t1.fd(size)
            t1.left(120)
            tracks2.append(t1.pos())
    return tracks2

def drawTriangleFront_list(tracks2):
    t1.penup()
    t1.goto(tracks2[2])
    t1.pendown()
    for i in range(0,3):
        t1.goto(tracks2[i])
        
for i in range(4):
    t1.speed(10)
    pos=(random.randrange(-300,300),random.randrange(-300,300))
    drawTriangleFront_list(drawTriaangleAtSave(60,pos))
    
t1.penup()
t1.home()

def movefd():
    t1.fd(30)
    
def movebac():
    t1.back(30)
    
def movel():
    t1.left(45)
def mover():
    t1.right(45)
    
wn.onkey(movefd,"Up")
wn.onkey(movebac,"Down")
wn.onkey(movel,"Left")
wn.onkey(mover,"Right")
wn.listen()
t1.penup()
turtle.mainloop()