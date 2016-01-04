#ex31B.py
#range of numbers

print "enter a number: ",
x = int(raw_input())

#you can set a range of numbers like this
if (1 < x < 10 ):
	print "Your number is between 1 and 10"
#or this
elif (x in range(10, 50)):
	print "Your number is between 10 and 50"
else:
	print "Out of range"


