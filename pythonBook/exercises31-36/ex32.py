#ex32.py
#loops and lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']



#this type of for loop goes through a list
for number in the_count:
	print "This count %d" % number

#same as above
for fruit in fruits:
	print "A fruit of type %s" % fruit

#mixed lists
#notice the %r
for i in change:
	print "I got %r" % i

#we can build lists, first initilize it
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	#append is a function that lists understand
	elements.append(i)

#now we can print them out too
for i in elements:
	print "Elements was: %d" % i

#me practicing
#this is an atempt to add numbers choosen by the user
user_input = []
for i in range(0, 5):
	print "Enter the number you want to assign to element %d: " % i,
	numbers = int(raw_input())
	user_input.append(numbers)

#prints user input	
count = 0
for i in user_input:
	print "The user input for element %d is %d" % (count, i)
	count += 1

