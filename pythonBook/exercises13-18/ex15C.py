#ex15C.py
#this program will open a file given by the user
#use file "ex15_example.txt"

print "Hello whats your name"
name = raw_input()

print "Hello %s" % name

print "enter the name of the file you want to open:",
txt = raw_input()

#this line gives the file a variable
filename = open(txt)

#this line prints the the file by 
#giving the varible of the file to the command read
print filename.read()

print ""

print "prints it again"
#we need to seek 0 because the read command reads
#the entire file and leaves the cruzor at the end
#of the file. esentially we are just resetting.
filename.seek(0)
print filename.read()

print ""

print "Should not open the file after it is closed"
filename.seek(0)
filename.close()
print filename.read()