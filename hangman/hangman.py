import json


def initial():
    data = getterData()
    keys = list(data.keys())  # get keys (types)
    selectedText = displaySelectCategory(keys[0], keys[1], keys[2])
    return selectedText


def randomWord():
    print('hello')


def getterData():
    with open('./datamodel/words.json') as file:
        return json.load(file)
        # return json.load(file)[selectedText]


def startGame(selected):
    print('hello')
    #     print(f"Hint : {hintWord}")


def displaySelectCategory(category_one_name='', category_two_name='', category_three_name=''):
    if(category_one_name != "" or category_two_name != "" or category_three_name != ""):
        print("Select Category")
        print(f"PRESS 1 ) {category_one_name}")
        print(f"PRESS 2 ) {category_two_name}")
        print(f"PRESS 3 ) {category_three_name}")
        try:
            select_category = int(input("Select Category : "))
            if(select_category <= 3 and select_category >= 1):
                if(select_category == 1):
                    return category_one_name
                elif(select_category == 2):
                    return category_two_name
                elif(select_category == 3):
                    return category_three_name
            else:
                print("ValueError : Input only 1, 2, 3")

        except ValueError:
            print("ValueError : Input only number")

    else:
        print("log : some category's null string")


def main():
    selected = initial()
    startGame(selected)


main()


# Docs for read data from csv format (https://docs.python.org/3/library/csv.html)
