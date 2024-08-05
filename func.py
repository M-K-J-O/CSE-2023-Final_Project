# func.py
"""
Title
Author
Date
"""


def checkInt(NUMBER):
    """
    Verifies the number is an integer
    :param NUMBER: (String)
    :return: (int)
    """
    if NUMBER.isnumeric():
        return int(NUMBER)
    else:
        print("That is not a number!")
        NEW_NUM = input("Please enter a valid number: ")
        return checkInt(NEW_NUM)


def checkFloat(NUMBER):
    """
    Verifies that if the string is a floating point number
    :param NUMBER: (string)
    :return: (float)
    """
    try:
        NUMBER = float(NUMBER)
        return NUMBER
    except ValueError:
        print("You did not enter a number! ")
        NEW_NUM = input("Please enter a number: ")
        return checkFloat(NEW_NUM)


def askContinue():
    """
    Asks the user if they want to continue the program
    :return: (bool)
    """
    AGAIN = input("Do you wish to Continue? (Y/n): ").upper()
    if AGAIN == "n" or AGAIN == "N" or AGAIN == "No" or AGAIN == "no":
        exit()
    else:
        return True
