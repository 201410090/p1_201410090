myfile=open('output.txt','w')
line1='first line \n'
myfile.write(line1.upper())
line2='second line \n'
myfile.write(line2.upper())
line3='third'
myfile.write(line3.upper())
myfile.close()