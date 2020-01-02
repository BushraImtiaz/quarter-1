"""10.	Write a Python program to find whether a given number (accept from the user) is even or odd, 
print out an appropriate message to the user."""


print("**** EVEN OR ODD ****")

user_input=int(input("Enter a number : "))
if user_input%2!=0:
    print("Number is odd")
else:
    print("Number is even")