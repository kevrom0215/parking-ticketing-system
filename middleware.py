import os,json

CONFIG_PATH = "users.json"


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

    try:
        f = open(CONFIG_PATH)
        data = json.load(f)
        for i in data:
            if(credentials[0]==i["username"] and credentials[1]==i["password"]):
                if i["type"]=="admin":
                    return 1
                elif i["type"] == "staff":
                    return 2
                else:
                    return 3
    except:
        print("Error loading json object")
    return 3
    pass
