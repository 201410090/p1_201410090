import time
fin=open('output.txt','r')
fout=open('outputUpper.txt','w')

for line in fin:
    sentense = ""
    words=line.split()
    for word in words:
        if word=='line':
            word=word.upper()
            sentense =  "[{0} edited {1}]".format(editor, timeEdited) + " " + sentense
        sentense = sentense + " " + word
    fout.write(sentense)
fin.close()
fout.close()

%outputUpper.txt