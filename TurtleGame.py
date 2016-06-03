import turtle
import random
wn=turtle.Screen()
t1=turtle.Turtle()

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(1000000000000000000000)
t1.shape("turtle")
t1.color("Red")
t1.pencolor("Red")

score_cursor = turtle.Turtle()
score_cursor.hideturtle()
score_cursor.penup()
score_cursor.goto(255,280)

score=0

end = turtle.Turtle()
end.hideturtle()
end.pencolor("Red")
end.penup()
end.goto(-100,0)

track_list=[]

def drawSquareAtSave(size,pos):
    tracks1=list()
    drawer.penup()
    drawer.setpos(pos)
    for i in range(0,4):
            drawer.fd(size)
            drawer.left(90)
            tracks1.append(drawer.pos())
    return tracks1
        
def drawSqareFront_list(tracks1):
    drawer.penup()
    drawer.goto(tracks1[3])
    drawer.pendown()
    for i in range(0,4):
        drawer.goto(tracks1[i])
    
    
def makeSquare():
    pos=(random.randrange(-300,300),random.randrange(-300,300))
    track_list.append(drawSquareAtSave(40,pos))
    
            
for i in range(5):
    makeSquare()
    
def drawAll():
    for i in track_list:
        drawSqareFront_list(i)
drawAll()

def InSqaure():
    global score
    pos = t1.pos()
    for i in track_list:
        if i[3][0]<=pos[0] and pos[0]<=i[1][0]:
            if i[3][1]<=pos[1] and pos[1]<=i[1][1]:
                t1.clear()
                t1.write('+1')
                track_list.remove(i)
                drawer.clear()
                makeSquare()
                score = score +1
                score_cursor.clear()
                score_cursor.write("score"+str(score),font=('Arial','30','normal'))
                drawAll()
        if score==10:
            end.write("CLEAR!",font=('Arial','60','normal'))
            break

    
t1.penup()
t1.home()

def movefd():
    if score!=10:
        t1.fd(30)
        InSqaure()
    
def movebac():
    if score!=10:
        t1.back(30)
        InSqaure()
    
def movel():
    if score!=10:
        t1.left(45)
def mover():
    if score!=10:
        t1.right(45)
    
wn.onkey(movefd,"Up")
wn.onkey(movebac,"Down")
wn.onkey(movel,"Left")
wn.onkey(mover,"Right")
wn.listen()
t1.penup()
turtle.mainloop()
