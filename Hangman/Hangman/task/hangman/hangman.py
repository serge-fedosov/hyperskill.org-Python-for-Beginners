import random

hangman = "H A N G M A N"
input_letter = "Input a letter: "
no_letter = "That letter doesn't appear in the word."
thanks = "Thanks for playing!"

words = ["python", "java", "swift", "javascript"]
chosen_word = words[random.randint(0, len(words) - 1)]
letters = set()

print(hangman)
print()
print("-" * len(chosen_word))

for _ in range(8):
    letter = input(input_letter)
    letters.add(letter)
    if letter not in chosen_word:
        print(no_letter)

    hidden_word = ""
    for i in range(len(chosen_word)):
        letter_i = chosen_word[i]
        hidden_word += letter_i if letter_i in letters else "-"

    print()
    print(hidden_word)

print()
print(thanks)
