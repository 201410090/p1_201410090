def findLeapyear():
    sel = int(raw_input("pressed year: "))
    if (sel%4==0) and (sel%100!=0 or sel%400==0):
        print "This is leapyear"
    else:
        print "This is not leapyear"
        
findLeapyear()