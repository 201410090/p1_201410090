allData=[
    ["Coffee","Water","Milk","Icecream"], 
    ["Espresso","No","No","No"],
    ["Long Black","Yes","No","No"],
    [ "Flat White","No","Yes","No"],
    ["Cappuccino","No","Yes","No"],
    ["Affogato","No","No","Yes"]
]

data = allData[1:]
print data
print "coffe count =", len(data)


for i in range(0,len(data)):
    print data[i][0], data[i][2]


for i in data:
    if i[2].upper()=="YES":
        print "milk coffe =", i[0]

print "milk coffe count =", len(i[2])

print (float(len(i[2]))/float(len(data)))

raw_input()