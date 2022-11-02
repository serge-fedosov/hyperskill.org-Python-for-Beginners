import random

words = ["python", "java", "swift", "javascript"]
chosen_word = words[random.randint(0, len(words) - 1)]

arr = list(chosen_word)
for i in range(3, len(arr)):
    arr[i] = "-"

hidden_word = "".join(arr)

print("H A N G M A N")
word = input(f"Guess the word {hidden_word}: ")
if word == chosen_word:
    print("You survived!")
else:
    print("You lost!")
