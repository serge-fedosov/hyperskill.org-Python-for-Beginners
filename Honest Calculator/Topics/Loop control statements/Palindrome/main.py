string = input()

for i in range(len(string) // 2):
    if string[i] != string[len(string) - i - 1]:
        print("Not palindrome")
        break
else:
    print("Palindrome")
