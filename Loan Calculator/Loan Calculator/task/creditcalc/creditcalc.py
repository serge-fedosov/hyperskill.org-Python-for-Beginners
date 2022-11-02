import argparse
import math

incorrect_parameters = "Incorrect parameters"
month_payment = "Month {}: payment is {}"
overpayment = "Overpayment = {}"
annuity_payment = "Your annuity payment = {}!"
loan_principal = "Your loan principal = {}!"
repay_loan = "It will take {}{}{} to repay this loan!"


def parse():
    parser = argparse.ArgumentParser(description="This program compute annuity and differentiated payments.")
    parser.add_argument("-t", "--type",
                        choices=["annuity", "diff"],
                        help="You need to choose type of payments.")

    parser.add_argument("-p", "--principal")
    parser.add_argument("-per", "--periods")
    parser.add_argument("-i", "--interest")
    parser.add_argument("-pay", "--payment")

    args = parser.parse_args()
    if args.type is None:
        print(incorrect_parameters)
    elif args.type == "annuity":
        if args.payment is None:
            if args.principal is None or args.periods is None or args.interest is None:
                print(incorrect_parameters)
                return

            p = int(args.principal)
            n = int(args.periods)
            i = float(args.interest) / 1200

            if p < 0 or n < 0 or i < 0:
                print(incorrect_parameters)
                return

            a = math.ceil(p * i * (1 + i) ** n / ((1 + i) ** n - 1))
            print(annuity_payment.format(a))
            over = n * a - p
            print(overpayment.format(over))

        elif args.principal is None:
            if args.payment is None or args.periods is None or args.interest is None:
                print(incorrect_parameters)
                return

            a = int(args.payment)
            n = int(args.periods)
            i = float(args.interest) / 1200

            if a < 0 or n < 0 or i < 0:
                print(incorrect_parameters)
                return

            p = math.floor(a / (i * (1 + i) ** n / ((1 + i) ** n - 1)))
            print(loan_principal.format(p))
            over = n * a - p
            print(overpayment.format(over))

        elif args.periods is None:
            if args.principal is None or args.payment is None or args.interest is None:
                print(incorrect_parameters)
                return

            p = int(args.principal)
            a = int(args.payment)
            i = float(args.interest) / 1200

            if p < 0 or a < 0 or i < 0:
                print(incorrect_parameters)
                return

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

            print(repay_loan.format(years, " and " if y != 0 and n != 0 else "", months))
            over = (n + y * 12) * a - p
            print(overpayment.format(over))

    elif args.type == "diff":
        if args.principal is None or args.periods is None or args.interest is None:
            print(incorrect_parameters)
            return

        p = int(args.principal)
        n = int(args.periods)
        i = float(args.interest) / 1200

        if p < 0 or n < 0 or i < 0:
            print(incorrect_parameters)
            return

        sum_d = 0
        for m in range(1, n + 1):
            d = math.ceil(p / n + i * (p - p * (m - 1) / n))
            print(month_payment.format(m, d))
            sum_d += d

        over = sum_d - p
        print()
        print(overpayment.format(over))


parse()
