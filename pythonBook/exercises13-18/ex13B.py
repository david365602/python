#ex13B
#Parameters, Unpacking, Variables and practice

from sys import argv

script, first, second = argv

name = raw_input("Whats you name: ")
#print "the scrpt name is:", script
print "the first varible is:", first
print "the last varible is:", second
print "and your name is %s" % name