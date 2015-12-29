#create_new_file.py
#creates a new file and adds words to the document

#asks for the name of the file
print "enter the name of the new file"
name = raw_input()

#opens the file and makes it read and writable
filename = open(name, 'w+')

#asks for text that is to be added
print "enter the text you want to give your file"
txt = raw_input()

#text is added to file
filename.write(txt)

print "All done now. \nYour file reads"

filename.seek(0)
print (filename.read())

#closes file
filename.close()