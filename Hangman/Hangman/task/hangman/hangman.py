import random

words = ["python", "java", "swift", "javascript"]
print("H A N G M A N")
word = input("Guess the word: ")
if word == words[random.randint(0, 3)]:
    print("You survived!")
else:
    print("You lost!")
