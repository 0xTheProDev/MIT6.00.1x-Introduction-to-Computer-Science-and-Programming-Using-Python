# Write a program that calculates the minimum fixed monthly payment needed
# in order pay off a credit card balance within 12 months. By a fixed monthly
# payment, we mean a single number which does not change each month, but
# instead is a constant amount that will be paid each month.

balance = 60
annualInterestRate = 0.2

rate = annualInterestRate/12.0
monthlyPayment = 10
while monthlyPayment < balance:
    bal = balance
    i = 1
    while i<=12 and bal>0:
        bal -= monthlyPayment
        bal += bal * rate
        i+=1
    if bal<=0:
        print monthlyPayment
        break
    monthlyPayment += 10
