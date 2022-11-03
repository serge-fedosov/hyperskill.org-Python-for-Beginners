import random
import string

hangman = "H A N G M A N"
input_letter = "Input a letter: "
input_single_letter = "Please, input a single letter."
input_lowercase_letter = "Please, enter a lowercase letter from the English alphabet."
no_letter = "That letter doesn't appear in the word."
already_guessed = "You've already guessed this letter."
lost = "You lost!"
guessed_word = "You guessed the word {}!"
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
    if len(letter) != 1:
        print(input_single_letter)
    elif letter not in string.ascii_lowercase:
        print(input_lowercase_letter)
    else:
        if letter in letters_true or letter in letters_false:
            print(already_guessed)
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
        hidden_word += letter_i if letter_i in letters_true else "-"

    print()
    print(hidden_word)

    if attempts == 0 or hidden_word.count("-") == 0:
        break

if hidden_word.count("-") == 0:
    print(guessed_word.format(hidden_word))
    print(survived)
else:
    print()
    print(lost)
