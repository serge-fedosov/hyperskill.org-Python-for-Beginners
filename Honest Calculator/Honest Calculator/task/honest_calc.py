operations = ["+", "-", "*", "/"]

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

def check(v1, v2, v3):
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6

    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7

    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8

    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


memory = 0
repeat = True
while repeat:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()

    if x == "M":
        x = memory

    if y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)
    except Exception:
        print(msg_1)
        continue

    if oper not in operations:
        print(msg_2)
        continue

    check(x, y, oper)

    if oper == "/" and y == 0:
        print(msg_3)
        continue

    repeat = False

    result = 0.0
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/":
        result = x / y

    print(result)

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_4)
        answer = input()
        if answer == "y":
            if is_one_digit(result):
                msg_index = 10
                save = True
                while msg_index < 13:
                    if msg_index == 10:
                        print(msg_10)
                    elif msg_index == 11:
                        print(msg_11)
                    elif msg_index == 12:
                        print(msg_12)

                    msg_index += 1
                    answer3 = input()
                    if answer3 == "y":
                        continue
                    elif answer3 == "n":
                        save = False
                        break
                if save:
                    memory = result
            else:
                memory = result
        elif answer != "n":
            continue

        answer2 = ""
        while answer2 != "y" and answer2 != "n":
            print(msg_5)
            answer2 = input()
            if answer2 == "y":
                repeat = True
                break
            elif answer2 != "n":
                continue

            repeat = False
