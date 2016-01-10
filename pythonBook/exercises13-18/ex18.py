#ex18.py
#Names, Variable, Code, Functions

#this one is like scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)


#we can also do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this one only takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
	print "I got nothing this time."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First")
print_none()