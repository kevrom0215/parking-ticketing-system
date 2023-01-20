import os
import json
import time

import admin, staff, template, middleware


SALES_FILENAME = "sales.txt"

def startup():
    # try:
    #     open(SALES_FILENAME, "x")
    # except:
    #     print("File already exists")
    pass

##############################################################
template.printIntro()
startup()
exiter = "1"
while exiter!="2":
    exiter = template.printMenu()
    if exiter == "1":
        creds = ""
        creds = middleware.getUserCreds()
        userInput = 1
        auth = middleware.authenticator(creds)
        if auth == 1:
            #os.system('cls')
            while userInput!="5":
                userInput = admin.adminMenu()
                admin.main(userInput)
                
            pass
        elif auth == 2:
            #os.system('cls')
            while userInput!="3":
                userInput = staff.staffMenu()
                staff.main(userInput)
            pass
        elif auth == 3:
            template.invalidUserPrint()
        else:
            template.errorPrinter()
