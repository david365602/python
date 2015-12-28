#create_new_file.py

print "enter the name of the new file"
filename = raw_input()

filename = open(filename, 'w+')

print "enter the text you want to give your file"
txt = raw_input()

filename.write(txt)

#broken after this point
print "All done now. \nYour file reads"
print filename.read()