import os
from datetime import datetime
import template
SPACING = 60

def staffMenu():
    print("#"*SPACING)
    print("\t\t\tSTAFF")
    print("#"*SPACING)
    print("1 - Car Entry")
    print("2 - Car Exit")
    print("3 - Logout")
    userInput = input("Enter input: ")
    return userInput
    pass

def carEntry(plateNumber, vehicleType):
    try:
        f = open("parking.txt", "a")
        formattedTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        f.write(f"{plateNumber} - {vehicleType} - {formattedTime}\n")
        pass
    except:
        print("System Message: Something went wrong!")
    finally:
        f.close()  

        
    pass

def carExit():
    pass

def computeHours(timeIn, timeOut):
    """
        Computes hours spent inside the parking space.
        First three hours is 50 pesos.
        Rate for exceeding hours is 10 pesos per hour
    """
    hoursSpent = timeOut - timeIn
    print(hoursSpent)

    pass


def main(userInput):
    if userInput == "1":
        plateNumber = input("Enter car plate number: ")
        print("\nVehicle Type:")
        print("1 - Motorcycle")
        print("2 - Car\n")
        vehicleType = input("Enter vehicle type: ")
        carEntry(plateNumber, vehicleType)
    elif userInput == "2":
        tempTimeIn = "3:0:0"
        tempTimeOut = datetime.now().strftime("%H:%M:%S")
        #formattedTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(computeHours(tempTimeIn,tempTimeOut))
        pass
    elif userInput == "3":
        template.logoutMessage()
    else:
        template.invalidInput()
