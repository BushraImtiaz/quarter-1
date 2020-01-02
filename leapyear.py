# year=int(input("Enter year to be checked:"))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("The year is a leap year!")
# else:
#     print("The year isn't a leap year!")
year=int(input("enter the year"))
def LeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
print (LeapYear(year))