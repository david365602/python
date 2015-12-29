# ex9.py
#more and more printing

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"
##\n creates a new line just as in java

print "Here are the months:", days
print "Here are the months:", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""


print "I am 5'2\" tall" #escape double-quote inside a string
print "I am 5\'2 tall" #escape single-quote inside a string

tabby_cat = "\t I'm tabbed in"
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat