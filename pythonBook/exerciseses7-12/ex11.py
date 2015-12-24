#ex11.py
#asking questions 

print "How are old you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do weight?",
weight = raw_input()

print "numbers to multiply? enter 2: "
x = int(raw_input())
y = int(raw_input())


print "So you are %r old, %r tall, and %r heavy" % (
	age, height, weight)
print ("%d multiplied by %d is equal to %d") % (x, y, x*y)