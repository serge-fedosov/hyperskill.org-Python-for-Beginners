v = input()
sum_ = 0
count = 0
while v != ".":
    sum_ += int(v)
    count += 1
    v = input()

print(sum_ / count)
