try:
    filename=open('p.txt','r')
    for line in filename:
        if line.find('Python')>=0:
            print line
    filename.close()

except IOError as e:
    print e

raw_input()