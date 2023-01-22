import template
import json
from user import user
from datetime import datetime
SPACING = 60
fileName = "parking"
fileDay = datetime.now().strftime("%d-%m-%Y")
file = f"{fileName}_{fileDay}.json"
saleFile = "sales.json"

def adminMenu():
    print("^"*SPACING)
    print("\t\t\tADMIN")
    print("^"*SPACING)
    print("1 - View Vehicles Parked")
    print("2 - View All Recorded Vehicles")
    print("3 - View Sales Today")
    print("4 - View Lifetime Sales")
    print("5 - Add staff")
    print("6 - Logout")
    userInput = input("Enter input: ")
    return userInput
    pass
    
def viewParked():
    print("="*SPACING)
    print("All Vehicles Parked here: ")
    try:
        carList = []
        with open(file,'r') as fs:
            carList = json.load(fs)
        for i in carList:
            if i["time_out"] == "0":
                print(i)
    except:
        print(e)
        print("System Message: Something went wrong!")
    finally:
        fs.close()

def viewAllVehicles():
    print("="*SPACING)
    print("All Recorded Vehicles: ")
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


def createUser():
    print("\n\nCreate a user: ")
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    username = input("Enter username: ")
    age = input("Enter age: ")
    password = input("Enter password: ")

    obj = user(firstName,lastName,username,age,password)
    print(obj.writeToFile())
    

def main(userInput):
    if userInput == "1":
        viewParked()
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
        createUser()
        pass
    elif userInput == "6":
        template.logoutMessage()
        
    else:
        template.invalidInput()
