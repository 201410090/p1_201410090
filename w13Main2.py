class Dog(object): 
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "my dog name is", self.name
    def talk(self):
        print self.name, "is mung mung"
        
class ShihTzudog(object): 
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "my dog name is", self.name
    def talk(self):
        print self.name, "is si si"
        
class Maltese(object): 
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "my dog name is", self.name
    def talk(self):
        print self.name, "is mal mal"

mydogname='poppy'
mydog=Dog(mydogname)
mydog.getName()
mydog.talk()

mydogname='poppy'
mydog=ShihTzudog(mydogname)
mydog.getName()
mydog.talk()

mydogname='poppy'
mydog=Maltese(mydogname)
mydog.getName()
mydog.talk()
