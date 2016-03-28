import turtle

wn=turtle.Screen()

t1=turtle.Turtle()

 

def draw(size, angle, sides):

    for s in range(sides):

        t1.forward(size)

        t1.left(angle)

 

sel=raw_input("Triangle or Square:")

if(sel=='T'):

    print "You entered T"

    draw(100, 120, 3)

else:

    print "You entered S"

    draw(100, 90, 4)

wn.exitonclick() 
