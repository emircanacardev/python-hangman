import random

try_Again = "yes"

while try_Again == "yes":
    hangmanList = open("./hangman_list.txt", "r")
    my_list1 = (hangmanList.read()).lower().split()
    secret_word = random.choice(my_list1)
    live = int((len(secret_word))*2-len(secret_word)/2-2)
    guess_string = ""
    character_list = list(secret_word)
    print("Welcome to the Hangman!")
    print("You have", live, "chances to guess.")
    print("The word has", len(secret_word), "letters.")

    while live > 0:
        character_left = 0
        for character in secret_word:
            if character in guess_string:
                print(character.upper(), end=" ")
            else:
                print("_", end=" ")
                character_left += 1

        if character_left > 0:
            guess = (input("\nGuess a letter: ")).lower()
            if len(guess) > 1 and guess != secret_word:
                print(" Please enter only one letter or the whole word.")
                continue
            elif guess == secret_word:
                print("\nYOU WON!")
                break
            elif guess == "":
                print(" Please enter a letter.")
                continue
            elif not guess.isalpha():
                print(" Please enter a valid letter.")
                continue
            elif len(guess) == 1 and guess in guess_string:
                print(" You've already used this letter.")
            elif len(guess) == 1 and guess not in secret_word and guess in guess_string:
                live -= 1
                print(" Wrong guess! You have", live, "chances for left.")
            elif len(guess) == 1 and guess not in secret_word and guess not in guess_string:
                live -= 1
                print(" Wrong guess! You have", live, "chances for left.")
            elif len(guess) != 1 and guess != secret_word and guess in guess_string:
                live -= 1
                print(" Wrong guess! You have", live, "chances for left.")

        if character_left == 0:
            print("\nYOU WON!")
            break
        if live == 0:
            print("YOU LOST!")
            print("The word was:", secret_word.upper())
            break

        guess_string += guess

    try_Again = input("Do you want to try again? yes/no ")
