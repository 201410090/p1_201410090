p1=raw_input("input p1")
p2=raw_input("input p2")

if p1=="r" :
    if p2=="r":
        print "draw"
    elif p2=="s":
        print "p1 win"
    elif p2=="p":
        print "p2 win"
    else:
        print "p2 error"
        
elif p1=="s":
    if p2=="r":
        print "p2 win"
    elif p2=="s":
        print "draw"
    elif p2=="p":
        print "p1 win"
    else:
        print "p2 error"
        
elif p1=="p":
    if p2=="r":
        print "p1 win"
    elif p2=="s":
        print "p2 win"
    elif p2=="p":
        print "draw"
    else:
        print "p2 error"
        
else:
    print "p1 error"
    
raw_input()