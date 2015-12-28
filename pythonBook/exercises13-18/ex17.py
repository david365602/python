#ex17.py
#copy files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()
#to do it in one line you can also do>>
#indata = in_file.read(open(from_file))

print "The input file is %d bytes long" % len(indata)

print "does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w+')
out_file.write(indata)

print "Alright, all done."

print out_file
out_file.close()
in_file.close()




