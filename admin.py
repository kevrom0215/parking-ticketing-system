import template
import json

from datetime import datetime
SPACING = 60
SPACING = 60
fileName = "parking"
fileDay = datetime.now().strftime("%d-%m-%Y")
file = f"{fileName}_{fileDay}.json"
saleFile = "sales.json"

def adminMenu():
    print("^"*SPACING)
    print("\t\t\tADMIN")
    print("^"*SPACING)
    print("1 - View All Recorded Vehicles")
    print("2 - View Sales Today")
    print("3 - View Lifetime Sales")
    print("4 - Logout")
    userInput = input("Enter input: ")
    return userInput
    pass
    
    

def viewAllVehicles():
    print("="*SPACING)
    print("All Vehicles Parked here: ")
    try:
        carList = []
        with open(file,'r') as fs:
            carList = json.load(fs)
        for i in carList:
            print(i)
    except Exception as e:
        print(e)
        print("System Message: Something went wrong!")
    finally:
        fs.close()

def viewSalesToday():
    print("="*SPACING)
    print("Sales today")
    totalSaleToday = 0
    try:
        carList = []
        with open(saleFile,'r') as fs:
            carList = json.load(fs)
        for i in carList:
            if i["date"] == fileDay:
                totalSaleToday += int(i["sale"])
        print(f"\nTotal Sales Today: {totalSaleToday}")
    except Exception as e:
        print(e)
        print("System Message: Something went wrong!")
    finally:
        fs.close()
    

def viewLifetimeSales():
    print("="*SPACING)
    print("Lifetime Sales")
    totalSales = 0
    try:
        carList = []
        with open(saleFile,'r') as fs:
            carList = json.load(fs)
        for i in carList:
            totalSales += int(i["sale"])
        print(f"\nLifetime Sales Today: {totalSales}")
    except Exception as e:
        print(e)
        print("System Message: Something went wrong!")
    finally:
        fs.close()

def main(userInput):
    if userInput == "1":
        viewAllVehicles()
        pass
    elif userInput == "2":
        viewSalesToday()
        pass
    elif userInput == "3":
        viewLifetimeSales()
        pass
    elif userInput == "4":
        template.logoutMessage()
        pass
    else:
        template.invalidInput()
