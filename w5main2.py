"""

@author lgr
@since160404
"""

def computeBMI(height,weight):
	
	bmi=weight/(height*height)
	print bmi
	if bmi>=18.5 and bmi<25.0:
    		print "namal weight"
	elif bmi>=25.0 and bmi<30.0:
    		print "over weight"
	else: 
    		print "error"

def lab5():
	computeBMI
	height=1.8
	weight=75
	computeBMI(height,weight)

def main():
	lab5()

if__name__=="__main__"
	main()

raw_input()