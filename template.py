import os
SPACING = 60

def invalidUserPrint():
    print("%"*SPACING)
    print("System Message: Invalid username and/or password!")
    print("%"*SPACING)

def errorPrinter():
    print("%"*SPACING)
    print("System Message: Error")
    print("%"*SPACING)

def invalidInput():
    print("%"*SPACING)
    print("System Message: Invalid User Input")
    print("%"*SPACING)


def printIntro():
    os.system('cls')
    print("="*SPACING)
    print("="*SPACING)
    print("\t\tParking Ticketing System")
    print("="*SPACING)

def printMenu():
    print("="*SPACING)
    print("1 - Login")
    print("2 - Exit")
    userInput = input("Enter input: ")
    return userInput

def logoutMessage():
    print("="*SPACING)
    print("\t\tLOGGED OUT SUCCESSFULLY")
    print("^"*SPACING)
    pass
