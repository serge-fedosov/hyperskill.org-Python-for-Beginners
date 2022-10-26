guests = list()
name = input()
count = 0
while name != ".":
    guests.append(name)
    name = input()
    count += 1

print(guests)
print(count)
