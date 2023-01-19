import os
import json
import time

import admin, staff, template


SALES_FILENAME = "sales.txt"

def startup():
    # try:
    #     open(SALES_FILENAME, "x")
    # except:
    #     print("File already exists")
    pass


def getUserCreds():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username,password

def authenticator(credentials):
    """
    This function authenticates with a return value depending
    on the user level.
        - returns 1 if admin
        - returns 2 if staff
        - returns 3 if not authenticated
    """
    #open user jsons
    #compare username
    #compare password
    #return authenticate
    return 1
    pass



##############################################################
template.printIntro()
startup()
exiter = "1"
while exiter!="2":
    exiter = template.printMenu()
    if exiter == "1":
        creds = getUserCreds()
        userInput = 1
        authenticator = authenticator(creds)
        if authenticator == 1:
            os.system('cls')
            while userInput!="5":
                userInput = admin.adminMenu()
                admin.main(userInput)
                
            pass
        elif authenticator == 2:
            os.system('cls')
            userInput = staff.staffMenu()
            while userInput!=3:
                pass
            pass
        elif authenticator == 3:
            template.invalidUserPrint()
        else:
            template.errorPrinter()
