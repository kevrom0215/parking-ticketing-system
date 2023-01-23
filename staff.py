import os
import json
import re
from datetime import datetime
import template
SPACING = 60
fileName = "parking"
fileDay = datetime.now().strftime("%d-%m-%Y")
file = f"{fileName}_{fileDay}.json"
saleFile = "sales.json"

def initialize():
    path = f"/{file}"
    isExist = os.path.exists(file)
    isExist1 = os.path.exists(saleFile)
    if isExist == False:
        try:
            f = open(file, 'x')
            f.write("[]")
        except Exception as e:
            print(e)
            print("File already exists")
    if isExist1 == False:
        try:
            f = open(saleFile, 'x')
            f.write("[]")
        except Exception as e:
            print(e)
            print("File already exists")
        finally:
            f.close()

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

def carEntry(plateNumber):
    try:
        # f = open(f"{file}", "a")
        # listObj = json.load(f)
        listObj = []
        with open(file) as fp:
            listObj = json.load(fp)
        formattedTime = datetime.now().strftime("%H:%M:%S")
        carDict = {
            "plate_number": f"{plateNumber}",
            "time_in": f"{formattedTime}",
            "time_out": "0"
        }
        listObj.append(carDict)
        with open(file, 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))
        
    except Exception as e:
        print(e)
        print("System Message: Something went wrong!")
    finally:
        fp.close() 

        
    pass

def getTimeIn(userInput):
    try:
        with open(file, 'r') as openfile:
        # Reading from json file
            json_object = json.load(openfile)
        for i in json_object:
            if userInput == i["plate_number"] and i["time_out"]=="0":
                print("Plate match!")
                return i["time_in"]
    except:
        return None
    

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
        if minutes<5:
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
    regexPattern = "^[A-Z]{2,3} [0-9]{3,5}$"
    checker = re.search(regexPattern,userInput)
    if checker == None:
        print("System Message: Invalid Plate Format")
    timeIn = getTimeIn(userInput)
    if timeIn != None:
        timeOut = datetime.now().strftime("%H:%M:%S")
        amountToPay = computeHours(timeIn, timeOut)
        addTimeOut(userInput, timeIn, timeOut)
        print(f"Amount to pay is: {amountToPay}")
        if amountToPay != 0:
            amountInput = int(input("Enter amount: "))
            while amountInput < amountToPay:
                print("Enter amount > parking fee")
            addToSale(amountInput)
            print("System Message: PRINTING RECIEPT")
            print("\n\n\n")
            print("-"*SPACING)
            printReciept(userInput, timeIn, timeOut, amountInput, amountToPay)
            
            print("-"*SPACING)
            print("\n\n\n")
    else:
        print("System Message: Vehicle not found")
    print("$"*SPACING)
    print("System Message: End of Transaction")
    print("$"*SPACING)
    print("\n\n\n")

def printReciept(carPlate, timeIn,timeOut, amountInput, amountToPay):
    #write to file here
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

def addToSale(amount):
    try:
        # f = open(f"{file}", "a")
        # listObj = json.load(f)
        listObj = []
        with open(saleFile) as fp:
            listObj = json.load(fp)
        
        try:
            
            fileDateChecker()
            dateDict = {
                "date": f"{fileDay}",
                "sale": f"{amount}"
            }
            listObj.append(dateDict)
            with open(saleFile, 'w') as json_file:
                json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))
            print('System Message: Successfully written to the JSON file')
        except Exception as e:
            print("System Message: Something went wrong!")
    except Exception as e:
        print(e)
        print("System Message: Something went wrong!")
    finally:
        fp.close() 
    pass

def fileDateChecker():
    try:
        listObj = []
        with open(saleFile) as fp:
            listObj = json.load(fp)
        
        for i in listObj:
            if i["date"] == fileDay:
                return True
        #create key pair
        dateDict = {
            "date": f"{fileDay}",
            "sale": "0"
        }
        listObj.append(dateDict)
        with open(saleFile, 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))
        return True

    except Exception as e:
        print(e)
    finally:
        fp.close()

def addTimeOut(plateNumber, timeIn, timeOut):
    try:
        carList = []
        with open(file,'r') as fs:
            carList = json.load(fs)

        k = 0
        for i in carList:
            if i["plate_number"] == plateNumber:
                if i["time_out"] == "0":
                    carList[k] = {
                        "plate_number": f"{plateNumber}",
                        "time_in": f"{timeIn}",
                        "time_out":f"{timeOut}"
                    }
                    print(carList[k])
                    fs = open(file, 'w')
                    json.dump(carList,fs, indent=4,  
                                separators=(',',': '))
                else:
                    k+=1
            else:
                k+=1
        
    except Exception as e:
        print(e)
        print("System Message: Something went wrong!")
    finally:
        fs.close()
    pass


def main(userInput):
    initialize()
    if userInput == "1":
        plateNumber = input("Enter car plate number: ")
        regexPattern = "^[A-Z]{2,3} [0-9]{3,5}$"
        checker = re.search(regexPattern,plateNumber)
        if checker == None:
            print("System Message: Invalid Plate Format")
        else:
            carEntry(plateNumber)
    elif userInput == "2":
        carExit()
        pass
    elif userInput == "3":
        template.logoutMessage()
    else:
        template.invalidInput()



