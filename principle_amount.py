"""15.	Write a Python program to compute the future value of a 
specified principal amount, rate of interest, and a number of years."""

print("**** COMPUTING FUTURE VALUE ****")

principal_amount = float(input("Enter Principal amount : "))
rate_of_interest = float(input("Enter Rate of Interest per year : "))
number_of_years = float(input("Enter number of years : "))
future_value = principal_amount * ( 1 + ((rate_of_interest/100) * number_of_years))
print(" Future value is " , future_value)