#create_new_file.py

#asks for the name of the file
print "enter the name of the new file"
name = raw_input()

#opens the file and makes it read and writable
filename = open(name, 'a+')

#asks for text that is to be added
print "enter the text you want to give your file"
txt = raw_input()

#text is added to file
filename.write(txt)

#this part does not work just yet

print "All done now. \nYour file reads"
#broken after this point

filename.seek(0)
print (filename.read())


#closes file
filename.close()