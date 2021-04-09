import random
import time
import sys

def hangman():
    #the word list is opened and then defined.
    with open("word_list.txt") as word_file:
        words = word_file.read().split()
    random_word = random.choice(words)
    #list of valid letters
    valid_letters = 'abcdefghijklmnopqurstvwxyz'
    #number of turns is determined
    turns = 7
    guessmade = ''

    while len(random_word)>0:
        main = ""
        missed = 0

        for letter in random_word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == random_word:
            print(main)
            print("Congratulations, You win!")
            print("Would you like to play again?")
            decide = input("Press y for yes or n for no ")
            if decide == "y":
                hangman()
            elif decide == "n":
                sys.exit()
            break

        print("Please guess a letter ", main)
        guess = input()

        if guess in valid_letters:
            guessmade = guessmade + guess
        else:
            print("Please choose a letter")
            guess = input()
        if guess not in random_word:
            turns = turns -1
            if turns == 6:
                print("You have 6 turns left.")
                print("----------")
            if turns == 5:
                print("You have 5 turns left")
                print("----------")
                print("         |")
                print("         |")
                print("         |")
                print("         |")
                print("         |")
            if turns == 4:
                print("You have 4 turns left")
                print("----------")
                print("      |  |")
                print("      |  |")
                print("         |")
                print("         |")
                print("         |")
            if turns == 3:
                print("You have 3 turns left")
                print("----------")
                print("      |  |")
                print("     O|  |")
                print("         |")
                print("         |")
                print("         |")
            if turns == 2:
                print("You have 2 turns left")
                print("----------")
                print("      |  |")
                print("     O|  |")
                print("     |   |")
                print("    / \  |")
                print("         |")
            if turns == 1:
                print("You have 1 turn left")
                print("----------")
                print("----------")
                print("      |  |")
                print("     O|  |")
                print("    /|   |")
                print("    / \  |")
                print("         |")
            if turns == 0:
                print("Sorry, but you failed to save an innocent man.")
                print("----------")
                print("----------")
                print("      |  |")
                print("     O|  |")
                print("    /|\  |")
                print("    / \  |")
                print("         |")

                print("Would you like to play again? ")
                decide = input("Press y for yes or n for no ")
                if decide == "y":
                    hangman()
                elif decide == "n":
                    sys.exit()
                break

name = input("Please enter your name ")
time.sleep(1)
print("Welcome to hangman ",name)
time.sleep(1)
print("--------------------")
time.sleep(1)
print("You have 7 attempts to guess the hidden word and save the innocent man.")
time.sleep(1)
hangman()

print()




