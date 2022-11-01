import math

b = 35 * math.pi / 180
c = 105 * math.pi / 180
side_b = 7
side_c = side_b * math.sin(c) / math.sin(b)

print(round(side_c, 1))
