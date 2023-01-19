import os
SPACING = 60

def staffMenu():
    os.system('cls')
    print("#"*SPACING)
    print("\t\t\tSTAFF")
    print("#"*SPACING)
    print("1 - Car Entry")
    print("2 - Car Exit")
    print("3 - Logout")
    userInput = input("Enter input: ")
    return userInput
    pass