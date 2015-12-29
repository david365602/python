#staticIP.py
#this program will set a static IP for a Ubuntu machine

from sys import argv

script, original = argv

backup = open("interfaces.bak", 'w+')
original = open(original, 'r+')

original_text = original.read()

backup.write(original_text)


#deletes contents of the orginal file
original.truncate(0)

#close opened files
backup.close()
original.close()
