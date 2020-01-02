def is_leap (year):
    # print(year)
    if (year %4 == 0 or year % 400== 0):
        print(" true, the year is evenly divided by 4, 400")
    elif (year % 100 == 0):
        print(" false, the year is divided by 100 is not a leap year")
    # return year


years = int(input("enter the year :"))
is_leap(years)