import math

degree = float(input())
radian = degree * math.pi / 180

print(round(math.cos(radian) / math.sin(radian), 10))
