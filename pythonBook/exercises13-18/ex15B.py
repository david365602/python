#ex15B.py
#This program will only input the file for which 
#the name is entered in the argument variable
#use file "ex15_example.txt"

from sys import argv

Script, filename = argv

txt = open(filename)

print txt.read() 