operations = ["+", "-", "*", "/"]
error = True

while error:
    print("Enter an equation")
    calc = input()
    try:
        x, oper, y = calc.split()
        x = float(x)
        y = float(y)
    except Exception:
        print("Do you even know what numbers are? Stay focused!")
        continue

    if oper not in operations:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue

    if oper == "/" and y == 0:
        print("Yeah... division by zero. Smart move...")
        continue

    error = False

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
