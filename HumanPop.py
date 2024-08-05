"""
TITLE
DATE
AUTHOR
"""

# IMPORTS
from func import *


# inputs

def openFileRead(FILENAME):
    '''
    opens the file and does basic formatting
    :param FILENAME: string
    :return: CONTENT_LIST list
    '''
    FILE = open(FILENAME, newline="")
    CONTENT_LIST = FILE.readlines()
    FILE.close()
    for i in range(len(CONTENT_LIST)):  # gets rid of empty lines
        CONTENT_LIST[i] = CONTENT_LIST[i][:-1]
        CONTENT_LIST[i] = CONTENT_LIST[i].split(",")
    return CONTENT_LIST


def file():
    """
    gets the file name the user wants the data from
    :return: str
    """
    print("")
    print("Please Type in File name to access data from: ")
    print("HumanPop.csv, MalePop.csv, FemalePop.csv")
    FILE = input("> ")
    return FILE


def menu():
    '''
    Starting Menu Directs user where to go
    :return: OPTION (int)
    '''
    print(f"Accessing Data from: {FILE}")
    print("Please choose an option:")
    print(" 1. Country List")
    print(" 2. Change File")
    print(" 3. Table ")
    print(" 4. Search Population Growth ")
    print(" 5. Exit ")
    OPTION = input("> ")
    try:
        OPTION = int(OPTION)
        if 5 >= OPTION >= 1:
            return OPTION
    except ValueError:
        return menu()


def getYearRange():
    """
    gets year range
    :return: int
    """
    print(f"Note: Data stored from 1950 - {HUMANS[len(HUMANS) - 1][1]} currently")
    print("")
    print("Enter Years Range:")
    YEAR1 = input(" Start Year > ")
    YEAR2 = input(" End Year > ")
    try:
        YEAR3 = int(YEAR1)
        YEAR4 = int(YEAR2)
        if YEAR3 <= YEAR4 and YEAR3 >= 1950 and YEAR4 <= int(HUMANS[len(HUMANS) - 1][1]):
            return (YEAR1, YEAR2)
        else:
            return getYearRange()
    except ValueError:
        return getYearRange()


def getCountry():
    """
    gets Country/Countries
    :return:
    """
    COUNTRY = []
    print("Type Country Name/s: ")
    COUNTRY = input("> ")
    COUNTRY = COUNTRY.split()
    for C in range(len(COUNTRY)):
        STATE = COUNTRY[C] in COUNTRYL
        if STATE == False:
            print(COUNTRY[C], "Does not exist in this File")
            return getCountry()
    return COUNTRY


def getAgeRange():
    """
    gets range of population age you want
    :return:
    """
    print("Type A number from 1-22")
    for i in range(len(HUMANS[0]) - 2):
        j = i + 2
        print(f"{i + 1}, {HUMANS[0][j]}")
    AGE = int(input("> "))
    if 1 <= AGE <= 22:
        return AGE + 1
    else:
        return getAgeRange()


# Outputs

def getPopulationGrowth():
    GROWTHRATE = []
    STARTPOP = 0
    ENDPOP = 0
    for C in range(len(COUNTRY)):
        for i in range(len(HUMANS)):
            if HUMANS[i][0] == COUNTRY[C] and HUMANS[i][1] == YEARARRAY[0]:
                STARTPOP = HUMANS[i][AGE]
            if HUMANS[i][0] == COUNTRY[C] and HUMANS[i][1] == YEARARRAY[1]:
                ENDPOP = HUMANS[i][AGE]
        YEARS = int(YEARARRAY[1]) - int(YEARARRAY[0])
        GROWTH = (int(ENDPOP) - int(STARTPOP)) // int(YEARS)
        GROWTHRATE.append(GROWTH)
    return GROWTHRATE


def dataOutput():
    print("")
    for C in range(len(COUNTRY)):
        print(
            f"{HUMANS[0][AGE]}, Growth Rate of {GROWTH[C]} Humans per year\nfrom {YEARARRAY[0]} to {YEARARRAY[1]} in {COUNTRY[C]}")
    print("")


def countryList():
    global COUNTRYL
    COUNT = "Country name"
    COUNTRYL = []
    for i in range(len(HUMANS)):
        if COUNT != HUMANS[i][0]:
            COUNT = HUMANS[i][0]
            COUNTRYL.append(COUNT)


def dataTable():
    """
    prints the file in a table format
    :return:
    """
    print("{:<40} {:<15} {:<15} {:<20}".format("COUNTRY", YEARARRAY[0], YEARARRAY[1], "ABOSOLUTE CHANGE", "RELATIVE CHANGE"))
    STARTPOP = 0
    ENDPOP = 0
    for C in range(len(COUNTRYL)):
        for i in range(len(HUMANS)):
            if HUMANS[i][0] == COUNTRYL[C] and HUMANS[i][1] == YEARARRAY[0]:
                STARTPOP = HUMANS[i][AGE]
            if HUMANS[i][0] == COUNTRYL[C] and HUMANS[i][1] == YEARARRAY[1]:
                ENDPOP = HUMANS[i][AGE]
        YEARS = int(YEARARRAY[1]) - int(YEARARRAY[0])
        GROWTH = (int(ENDPOP) - int(STARTPOP))
        print("{:<40} {:<15} {:<15} {:<20}".format(COUNTRYL[C], STARTPOP, ENDPOP, GROWTH))

# main
if __name__ == "__main__":
    while FileNotFoundError:
        FILE = file()
        try:
            HUMANS = openFileRead(FILE)
        except FileNotFoundError:
            print("File Not Found")
            pass
        else:
            break
    countryList()
    print("===============================================================")
    print("Welcome to Human Population Database!")
    print("Link to Files: https://ourworldindata.org/")
    print("===============================================================")
    while True:
        OPTION = menu()
        if OPTION == 4:
            print("===============================================================")
            YEARARRAY = getYearRange()
            print("===============================================================")
            COUNTRY = getCountry()
            print("===============================================================")
            AGE = getAgeRange()
            print("===============================================================")
            GROWTH = getPopulationGrowth()
            print("===============================================================")
            dataOutput()
        if OPTION == 2:
            while FileNotFoundError:
                FILE = file()
                try:
                    HUMANS = openFileRead(FILE)
                except FileNotFoundError:
                    print("File Not Found")
                    pass
                else:
                    break
            print("===============================================================")
        if OPTION == 5:
            exit()
        if OPTION == 3:
            print("===============================================================")
            YEARARRAY = getYearRange()
            print("===============================================================")
            AGE = getAgeRange()
            print("=================================================================================================")
            dataTable()
            print("=================================================================================================")
        if OPTION == 1:
            print("===============================================================")
            for i in range(len(COUNTRYL)):
                print(COUNTRYL[i])
            print("===============================================================")
