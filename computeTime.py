timeOut = 36000
timeIn = 24000

# timeSpent = timeOut-timeIn
timeSpent = 9705
print(timeSpent)

#1 hour is 3600 secs
hours = str(timeSpent/60/60).split(".")[0]
minutes = str(timeSpent/60/10).split(".")[0]
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
amountToPay = 50
if(int(hours)>3):
    if(int(minutes)>30):
        amountToPay = 50 + (int(hours)-3)*10 + 10
    else:
        amountToPay = 50 + (int(hours)-3)*10

print(amountToPay)

