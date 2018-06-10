# Write a program to calculate the credit card balance after one year if
# a person only pays the minimum monthly payment required by the credit card
# company each month.

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
i = 1
rate = annualInterestRate/12.0
totalPayment = 0
while i<=12:
    print "Month: " + str(i)
    monthlyPayment = balance * monthlyPaymentRate
    totalPayment += monthlyPayment
    print "Minimum monthly payment: " + str(round(monthlyPayment,2))
    balance -= monthlyPayment
    balance += balance * rate
    print "Remaining balance: " + str(round(balance,2))
    i+=1
print "Total paid: " + str(round(totalPayment,2))
print "Remaining balance: " + str(round(balance,2))
