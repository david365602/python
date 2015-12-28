#ex15D.py
#write words to a file
#not working yet

print "enter the name of the file you want to write to:",
txt = raw_input()

#this line gives the file a variable
#the w is important as it tells python that it will be used 
#for appending
filename = open(txt, 'a')

print "enter the words you want to add to the file"
words = raw_input()

filename.write(words)
filename.close()