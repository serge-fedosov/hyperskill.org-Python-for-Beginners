operations = ["+", "-", "*", "/"]
error = True

while error:
    print("Enter an equation")
    calc = input()
    try:
        x, oper, y = calc.split()
        if x.find(".") == -1:
            x = int(x)
        else:
            x = float(x)

        if y.find(".") == -1:
            y = int(y)
        else:
            y = float(y)
    except Exception:
        print("Do you even know what numbers are? Stay focused!")
        continue

    if oper not in operations:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue

    error = False
