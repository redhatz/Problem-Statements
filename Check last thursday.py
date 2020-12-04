import calendar 
from time import strptime

def getLastThursday(year, month):
    cal = calendar.monthcalendar(year, month)
    last_thurs_date = cal[4][3]
    if month < 10:
        thurday_date = str(year)+'-0'+ str(month)+'-' + str(last_thurs_date)
    else:
        thurday_date = str(year) + '-' + str(month) + '-' + str(last_thurs_date)
    return thurday_date
    
    
def isLastThursday(input_date,lastThursday):
    if (input_date == lastThursday):
        return True
    else:
        return False
    
    

if __name__ == "__main__":
    argument=int(input("1) Checking Last Thursday of a Month\n2) Checking if the date is last Thursday of a Month\n"))
    if(argument == 1):
        month=input("Enter the month name: ")
        newMonth = month [0].upper() + month [1:3].lower()
        month_number=strptime(newMonth,'%b').tm_mon
        last_thursday= getLastThursday(2020, month_number)
        lastThursday=str(last_thursday)
        print("Last Thursday: "+lastThursday)
    else:
        month=input("Enter the month\n")
        newMonth = month [0].upper() + month [1:3].lower()
        month_number=strptime(newMonth,'%b').tm_mon
        last_thursday= getLastThursday(2020, month_number)
        lastThursday=str(last_thursday)
        check=str(input("Enter the date in yyyy-mm-dd format: "))
        print(isLastThursday(check,lastThursday))
    
    
    
    
    