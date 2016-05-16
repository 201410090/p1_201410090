import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

wn.bgpic("myMaze.gif")

t1.penup()
t1.goto(-400,350)
t1.right(90)
t1.pendown()

def move_fd():
    t1.fd(50)

def move_back():
    t1.back(50)

def move_left():
    t1.left(90)

def move_right():
    t1.right(90)

def mouse_goto(x,y):
    t1.setpos(x,y)


def add_keys():
    wn.onkey(move_fd,"Up")
    wn.onkey(move_back,"Down")
    wn.onkey(move_left,"Left")
    wn.onkey(move_right,"Right")
    wn.onkey(wn.bye,"q")

def add_mouse():
    wn.onclick(mouse_goto)

def lab11():
    add_keys()
    add_mouse()
    wn.listen()
    turtle.mainloop()

lab11()
