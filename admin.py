import template

SPACING = 60

def adminMenu():
    print("^"*SPACING)
    print("\t\t\tADMIN")
    print("^"*SPACING)
    print("1 - View Vehicles in Parking")
    print("2 - View All Recorded Vehicles")
    print("3 - View Sales Today")
    print("4 - View Lifetime Sales")
    print("5 - Logout")
    userInput = input("Enter input: ")
    return userInput
    pass

def viewVehiclesHere():
    pass

def viewAllVehicles():
    pass

def viewSalesToday():
    pass

def viewLifetimeSales():
    pass

def logoutMessage():
    pass

def main(userInput):
    if userInput == "1":
        pass
    elif userInput == "2":
        pass
    elif userInput == "3":
        pass
    elif userInput == "4":
        pass
    elif userInput == "5":
        pass
    else:
        print("System Message: User Input Invalid")
