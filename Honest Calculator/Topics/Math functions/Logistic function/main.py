import math

x = int(input())

d = math.exp(x) / (math.exp(x) + 1)

print(round(d, 2))
