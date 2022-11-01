import math

what_calculate = '''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:'''
loan_principal = 'Enter the loan principal:'
monthly_payment = "Enter the monthly payment:"
loan_interest = "Enter the loan interest:"
repay_loan = "It will take {}{}{} to repay this loan!"
# repay_loan = "It will take 8 years and 2 months to repay this loan!"
number_periods = "Enter the number of periods:"
your_monthly_payment = "Your monthly payment = {}!"
annuity_payment = "Enter the annuity payment:"
your_loan_principal = "Your loan principal = {}!"


print(what_calculate)
command = input()

if command == "n":
    print(loan_principal)
    p = int(input())

    print(monthly_payment)
    a = int(input())

    print(loan_interest)
    i = float(input()) / 1200

    n = math.ceil(math.log(a / (a - i * p), 1 + i))
    y = n // 12
    n = n - y * 12

    years = ""
    months = ""
    if y != 0:
        if y == 1:
            years = "1 year"
        else:
            years = str(y) + " years"

    if n != 0:
        if n == 1:
            months = "1 month"
        else:
            months = str(n) + " months"

    print(repay_loan.format(years, " and " if y != 0 and n != 0 else "",months))

elif command == "a":
    print(loan_principal)
    p = int(input())

    print(number_periods)
    n = int(input())

    print(loan_interest)
    i = float(input()) / 1200

    a = math.ceil(p * i * (1 + i) ** n / ((1 + i) ** n - 1))
    print(your_monthly_payment.format(a))

elif command == "p":
    print(annuity_payment)
    a = float(input())

    print(number_periods)
    n = int(input())

    print(loan_interest)
    i = float(input()) / 1200

    p = round(a / (i * (1 + i) ** n / ((1 + i) ** n - 1)))
    print(your_loan_principal.format(p))
