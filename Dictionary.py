import json
from difflib import get_close_matches

data = json.load(open("data.json"))

print("\nWelcome to the python dictionary\n")

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Did you mean %s instead" %get_close_matches(word, data.keys()) [0])
        decide = input("press y for yes or n for no ")
        if decide =="y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            print("You have entered a word that is not in this dictionary, please try again")
        else:
            return("Please enter just y or n")
    else:
        print("You have entered a word that is not in this dictionary, please try again")


def start():
    word = input("Enter the word you would like to search for ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
        else:
            print(output)
    decide = input("Would you like to search again?\nPress y for yes or n for no\n")
    if decide == "y":
        start()
    elif decide == "n":
        print("Thank you for using the python dictionary")

start()

