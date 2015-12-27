#ex15C.py
#this program will open a file given by the user

print "Hello whats your name"
name = raw_input()

print "Hello %s" % name

print "enter the name of the file you want to open:",
txt = raw_input()

filename = open(txt)

print filename.read()