import os
import json
from datetime import datetime
import template
SPACING = 60
fileName = "parking"
fileDay = datetime.now().strftime("%d-%m-%Y")
file = f"{fileName}_{fileDay}.json"

def initialize():
    path = f"/{file}"
    isExist = os.path.exists(path)
    if isExist == False:
        try:
            f = open(file, 'x')
        except Exception as e:
            print(e)
            print("Error creating file")

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
        f = open(f"{file}", "a")
        formattedTime = datetime.now().strftime("%H:%M:%S")
        carDict = {
            "plate_number": f"{plateNumber}",
            "vehicle_type": f"{vehicleType}",
            "time_in": f"{formattedTime}",
        }
        json_object = json.dumps(carDict, indent=4)
        with open(file, "a") as outfile:
            outfile.write(json_object + ",")
        pass
    except Exception as e:
        print(e)
        print("System Message: Something went wrong!")
    finally:
        f.close()  

        
    pass

def getTimeIn(userInput):
    with open(file, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        
    for i in json_object["cars"]:
        if userInput == i["plate_number"]:
            print("Plate match!")
            return i["time_in"]
    pass

def computeHours(timeIn, timeOut):
    """
        Computes hours spent inside the parking space.
        First three hours is 50 pesos.
        Rate for exceeding hours is 10 pesos per hour
        Grace period is 5 mins
    """
    timeOut = datetime.now().strftime("%H:%M:%S")
    t1 = datetime.strptime(timeIn, "%H:%M:%S")
    t2 = datetime.strptime(timeOut, "%H:%M:%S")
    hoursSpent = t2 - t1
    timeInSecs = hoursSpent.total_seconds()
    hours = int(str(hoursSpent).split(":")[0])
    minutes = int(str(hoursSpent).split(":")[1])
    print(f"\n\nTotal Hours: {hoursSpent}\n\n")
    
    if hours < 3:
        if minutes<15:
            return 0
        else:
            return 50
    else:
          amountToPay = 50 + (hours-3)*10
          if minutes > 30:
              amountToPay += 10
              return amountToPay
          return amountToPay
    

def carExit():
    userInput = input("Enter car plate: ")
    timeIn = getTimeIn(userInput)
    timeOut = datetime.now().strftime("%H:%M:%S")
    amountToPay = computeHours(timeIn, timeOut)
    print(f"Amount to pay is: {amountToPay}")
    amountInput = int(input("Enter amount: "))
    while amountInput < amountToPay:
        print("Enter amount > parking fee")
    #TODO: delete from json
    #TODO: add to sale
    print("System Message: PRINTING RECIEPT")
    print("\n\n\n")
    print("-"*SPACING)
    printReciept(userInput, timeIn, timeOut, amountInput, amountToPay)
    print("-"*SPACING)
    print("\n\n\n")
    print("$"*SPACING)
    print("System Message: End of Transaction")
    print("$"*SPACING)
    print("\n\n\n")

def printReciept(carPlate, timeIn,timeOut, amountInput, amountToPay):
    print("&"*SPACING)
    print("&"*SPACING)
    print("\t\t\tReciept")
    print(f"\n\nPlate Number: {carPlate}")
    print(f"\nTime in: {timeIn}")
    print(f"Time out: {timeOut}")
    print(f"\nAmount to Pay: {amountToPay}")
    print(f"Paid: {amountInput}")
    print(f"Change: {amountInput - amountToPay}")
    print("\n\n\t\t\tThank you")
    print("&"*SPACING)
    print("&"*SPACING)

def main(userInput):
    initialize()
    if userInput == "1":
        plateNumber = input("Enter car plate number: ")
        print("\nVehicle Type:")
        print("1 - Motorcycle")
        print("2 - Car\n")
        vehicleType = input("Enter vehicle type: ")
        carEntry(plateNumber, vehicleType)
    elif userInput == "2":
        carExit()
        pass
    elif userInput == "3":
        template.logoutMessage()
    else:
        template.invalidInput()
