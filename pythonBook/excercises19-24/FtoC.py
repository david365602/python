#FtoC.py
#convertes degrees


def convert(fahrenheit):
	celsius = (fahrenheit - 32) * (5/float(9))
	return celsius


print "Enter the degrees you want to convert"
#must include int() or it will not work
fahrenheit = int(raw_input())
celsius = convert(fahrenheit)

print "%d degrees fahrenheit is %0.2f degrees celsius" % (fahrenheit, celsius)
