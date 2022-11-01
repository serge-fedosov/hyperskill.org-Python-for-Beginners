operations = ["+", "-", "*", "/"]

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

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














