    
#Question num 1:

''' FIND A LEAP YEAR '''

def get_year():
   print("Please input year:")
   year = int(input())
   return year
  
def if_else(year):
   if year % 4 == 0 and year % 100 != 0:
    print("It's a leap year")
   elif year % 400 == 0 and year % 100 != 0:
    print("It's a leap year")
   elif (year % 100 == 0):
    print("It's not a leap year")
   else:
    print("There is an error")
  
def main():
    years = get_year()
    if_else(years)
    
main()
