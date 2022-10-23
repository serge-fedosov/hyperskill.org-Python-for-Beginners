initial_quantity = int(input())
final_quantity = int(input())

count = 0
while initial_quantity > final_quantity:
    initial_quantity //= 2
    count += 1

print(count * 12)
