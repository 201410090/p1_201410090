def upanddown():
    target = input("pressed target: ")
    count = 0
    while(1):
        number = input("pressed number: ")
        count = count+1
        if(target == number):
            print "number"
            print count
            break
        else:
            if(target>number):
                print "up"
            else:
                print "down"

upanddown()

raw_input()