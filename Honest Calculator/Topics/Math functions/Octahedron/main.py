import math

a = int(input())

area = 2 * math.sqrt(3) * a * a

volume = 1 / 3 * math.sqrt(2) * a * a * a

print(round(area, 2), round(volume, 2))
