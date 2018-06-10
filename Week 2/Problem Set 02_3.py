# Write a program that calculates the minimum fixed monthly payment needed
# in order pay off a credit card balance within 12 months. By a fixed monthly
# payment, we mean a single number which does not change each month, but
# instead is a constant amount that will be paid each month.
# Use Bisection search to short the time

balance = 60
annualInterestRate = 0.2

rate = annualInterestRate/12.0
monthlyPayment = 0
upper = balance*1.00
lower = 0.00
bal = balance
while True :
    monthlyPayment = (upper + lower)/2
    bal = balance
    for i in range(0,12) :
        bal -= monthlyPayment
        bal += bal * rate
    if bal<-0.01 :
        upper = monthlyPayment
    elif bal>0.01 :
        lower = monthlyPayment
    else :
        break;
print round(monthlyPayment, 2)
