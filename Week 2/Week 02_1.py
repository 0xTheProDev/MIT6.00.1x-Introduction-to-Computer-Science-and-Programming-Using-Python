# Program to convert Decimal to Binary

num = int(raw_input("Enter an integer: "))
result=""
while num!=0 :
    result = str(num%2) + result
    num/=2
if result!="" :
    print result
else :
    print "0"
