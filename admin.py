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
    print("="*SPACING)
    print("Vehicles here")
    pass

def viewAllVehicles():
    print("="*SPACING)
    print("All Vehicles Parked here")
    pass

def viewSalesToday():
    print("="*SPACING)
    print("Sales today")
    pass

def viewLifetimeSales():
    print("="*SPACING)
    print("Lifetime Sales")
    pass

def main(userInput):
    if userInput == "1":
        viewVehiclesHere()
        pass
    elif userInput == "2":
        viewAllVehicles()
        pass
    elif userInput == "3":
        viewSalesToday()
        pass
    elif userInput == "4":
        viewLifetimeSales()
        pass
    elif userInput == "5":
        template.logoutMessage()
        pass
    else:
        template.invalidInput()
