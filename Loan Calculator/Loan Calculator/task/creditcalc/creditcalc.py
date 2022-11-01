import math

loan_principal = 'Enter the loan principal:'
what_calculate = '''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:'''
monthly_payment = "Enter the monthly payment:"
repay_loan = "It will take {} month{} to repay the loan"
number_months = "Enter the number of months:"
your_monthly_payment = "Your monthly payment = {}"
last_payment = "Your monthly payment = {} and the last payment = {}."

print(loan_principal)
principal = int(input())
print(what_calculate)
command = input()
if command == "m":
    print(monthly_payment)
    payment = int(input())
    months = math.ceil(principal / payment)
    print()
    if months == 1:
        print(repay_loan.format(months, ""))
    else:
        print(repay_loan.format(months, "s"))
elif command == "p":
    print(number_months)
    months = int(input())
    payment = math.ceil(principal / months)
    print()
    if payment * months == principal:
        print(your_monthly_payment.format(payment))
    else:
        last_payment_ = principal - (months - 1) * payment
        print(last_payment.format(payment, last_payment_))
