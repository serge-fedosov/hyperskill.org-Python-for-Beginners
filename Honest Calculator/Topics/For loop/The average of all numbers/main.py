a = int(input())
b = int(input())

sum_ = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        sum_ += i
        count += 1

print(sum_ / count)
