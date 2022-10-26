sum_ = 0
sum2 = 0
while True:
    n = int(input())
    sum_ += n
    sum2 += n ** 2
    if sum_ == 0:
        break

print(sum2)
