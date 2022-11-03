import random

hangman = "H A N G M A N"
input_letter = "Input a letter: "
no_letter = "That letter doesn't appear in the word."
no_improvements = "No improvements."
lost = "You lost!"
guessed_word = "You guessed the word!"
survived = "You survived!"

words = ["python", "java", "swift", "javascript"]
chosen_word = words[random.randint(0, len(words) - 1)]
letters_true = set()
letters_false = set()

print(hangman)
print()
print("-" * len(chosen_word))

attempts = 8

while True:
    letter = input(input_letter)
    if letter in letters_true:
        print(no_improvements)
        attempts -= 1
    elif letter in letters_false:
        print(no_letter)
        attempts -= 1
    else:
        if letter in chosen_word:
            letters_true.add(letter)
        else:
            print(no_letter)
            letters_false.add(letter)
            attempts -= 1

    hidden_word = ""
    for i in range(len(chosen_word)):
        letter_i = chosen_word[i]
        if letter_i in letters_true:
            hidden_word += letter_i
        else:
            hidden_word += "-"

    print()
    print(hidden_word)

    if attempts == 0 or hidden_word.count("-") == 0:
        break

if hidden_word.count("-") == 0:
    print(guessed_word)
    print(survived)
else:
    print()
    print(lost)
