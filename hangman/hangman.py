import json
import os
import random
import math


def initial():
    data = getterData()
    # get keys (types) from file
    keys = list(data.keys())
    # select category
    selectedText = displaySelectCategory(keys[0], keys[1])
    # get word and hint from category (random)
    word, hint = randomWord(data[selectedText])
    return word, hint


def randomWord(data):
    index_sample = random.randint(0, len(data)-1)
    # return word's random in file
    return data[index_sample]['word'].lower(), data[index_sample]['hint']


def getterData():
    pathFile = './datamodel/words.json'
    if os.path.exists(pathFile):
        with open(pathFile) as file:
            try:
                return json.load(file)
            except:
                print("Error : Cant open file")
    else:
        print("Not Found: directory this file")
        exit()
        #
        # return json.load(file)[selectedText]


def startGame(word, hint):
    score = 0
    remaining_wrong_guess = len(word)
    played = getHangman(word)
    wrong_guessed = []
    difference = math.floor(100/remaining_wrong_guess)
    print("Hint: ", hint)
    display(played, score, remaining_wrong_guess, wrong_guessed)
    while(True):
        my_turn = input("> ").lower()
        if (my_turn in word):
            # assign char
            if(my_turn not in played):
                for i in range(len(word)):
                    if my_turn == word[i]:
                        played[i] = my_turn
                        score += difference
            else:
                print("Selected, Enter again.")

        else:
            remaining_wrong_guess -= 1
            wrong_guessed.append(my_turn)

        if((score < (difference * len(word)) and score >= 0) and remaining_wrong_guess != 0):
            display(played, score, remaining_wrong_guess, wrong_guessed)
        elif(remaining_wrong_guess == 0):
            print("Game Over !!!")
            exit()
        else:
            display(played, 100, remaining_wrong_guess, wrong_guessed)
            print("You Won !!!")
            exit()


def display(played, score, remaining_wrong_guess, wrong_guessed):
    for i in played:
        print(i, end=' ')
    print("   score", score, end=",")
    print(" remaining wrong guess", remaining_wrong_guess, end=",")
    if(wrong_guessed != []):
        print(" wrong guessed: ", end="")
        for i in wrong_guessed:
            print(i, end=" ")
    print('')


def getHangman(word):
    listForGame = []
    for i in word:
        listForGame.append('_')
    return listForGame


def displaySelectCategory(category_one_name='', category_two_name=''):
    if(category_one_name != "" or category_two_name != ""):
        print("Select Category")
        print(f"PRESS 1 ) {category_one_name}")
        print(f"PRESS 2 ) {category_two_name}")
        try:
            select_category = int(input("Select Category : "))
            if(select_category <= 2 and select_category >= 1):
                if(select_category == 1):
                    return category_one_name
                elif(select_category == 2):
                    return category_two_name
            else:
                print("ValueError : Input only 1, 2")

        except ValueError:
            print("ValueError : Input only number")

    else:
        print("log : some category's null string")


def main():
    word_selected, hint_selected = initial()
    startGame(word_selected, hint_selected)


# call main function
main()
