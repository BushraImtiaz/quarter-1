#  ----------- Check whether leap year or not --------------

def is_leap(year):
    leap = False

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap
       


year = int(input("Enter an year:  "))
print(is_leap(year))