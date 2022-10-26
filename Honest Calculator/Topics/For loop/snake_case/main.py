string = input()

result = ""
for s in string:
    if s.islower():
        result += s
    else:
        result += "_" + s.lower()

print(result)
