#rounding numbers
num1 = 54.0
num2 = 5.0
total = num1 / num2
#don't do this for somthing like that
#this does not give the right answer
#print "%d divided by %d = %d" % (num1, num2, num1 / num2)

print "if we divide", num1, "by", num2, "we get", total
print "if we round our answer we get ", round(total)
#don't do this either round(num1 / num2)
#also does give the right answer