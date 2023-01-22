import json
file = "users.json"

class user():
    def __init__(self, firstName, lastName, username, age, password):
        self.first_name = firstName
        self.last_name = lastName
        self.user_name = username
        self.age = age
        self.password = password

    def printUserName(self):
        print("Hello user " + self.user_name)

    def _getPassword(self):
        return self.password
    
    def writeToFile(self):
        userDict = {
            "first_name" : f"{self.first_name}",
            "last_name" : f"{self.last_name}",
            "username" : f"{self.user_name}",
            "age" : f"{self.age}",
            "password" : f"{self.password}",
            "type" : "staff"
        }
        fp = open(file, 'r')
        listObj = json.load(fp)

        for i in listObj:
            if self.user_name == i["username"]:
                return "System Message: User already exists"
            
        listObj.append(userDict)
        with open(file,"w") as json_file:
            json.dump(listObj, json_file,
                                indent=4,  
                                separators=(',',': '))
        return "System Message: User creation success"
        