#ex15.py
#This program will read a file that is given by the user
#use file "ex15_example.txt"

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()