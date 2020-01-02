    
#1 Calculate Area Of Circle
pi= 3.14159
radius = float(input("Enter value of radius: "))
area = pi * (radius*radius)
print("Area of circle is: ",area)

#2 Check Number either positive, negative or zero
number = float(input("Enter number:"))
if number>0:
    print("Positive Number Entered")
elif number==0:
    print("Zero Entered")
else:
    print("Negative Number Entered")

#3 Divisibility Check of two numbers
numenator = int(input("Enter Numenator: "))
denominator = int(input("Enter Denomenator: "))
if numenator%denominator==0:
    print("Number",numenator, "is Completely divided by",denominator)
else:
        print("Number",numenator, "is not Completely divided by",denominator)

#4 Days Calculator

from datetime import datetime

startDate = input("Enter a date in (dd/mm/yy) format: ")
endDate = input("Enter a date in (dd/mm/yy) format: ")

finalstartDate = datetime.strptime(startDate,"%d/%m/%Y").date()
finalendDate = datetime.strptime(endDate,"%d/%m/%Y").date()

remainingDays = finalendDate - finalstartDate

print ("There are ", remainingDays.days, "days between ", finalstartDate," and ",finalendDate)


#5 Calculate Volume Of Sphere
pi= 3.14159
radius = float(input("Enter value of radius: "))
volume = 4.0/3.0*pi*radius**3
print("Volume of the Sphere with Radius is: ",volume)

#6 Copy String n times
a = str(input("Enter String: "))
result = ""
b = int(input("How many copies of String you need: "))
print(b*a)

#7 Check If number is Even Or Odd
num = int(input("Enter Number: "))
mod = num % 2
if mod > 0:
    print(num,"is Odd")
else:
    print(num,"is Even")

#8 Vowel Tester

vowels = ['A','E','I','O','U','a','e','i','o','u']

userInput = input("Enter A Character")

if userInput in vowels:
    print(userInput, " is Vowel")
else:
    print(userInput," is not Vowel")

#9 Triangle Area
magBase = float(input("Enter magnitude of Triangle base: "))
magHeight = float(input("Enter Magnitude of Triangle Height: "))
area = magBase*magHeight/2
print("Area of a Triangle with Height ",magHeight, " and Base ",magBase," is: ",area)

#10 Calculate Interest
p = float(input("Please enter principal amount: "))
r = float(input("Please Enter Rate of interest in %: "))
t = float(input("Enter number of years for investment: "))
#a = p* (1 + r/100)**2
a = p* (pow((1 + r*100 / 100), t))
print(a)

#11 Euclidean distcance
import math

x1 = int(input("Enter Co-Ordinate For x1 :"))
x2 = int(input("Enter Co-Ordinate For x2 :"))
y1 = int(input("Enter Co-Ordinate For y1 :"))
y2 = int(input("Enter Co-Ordinate For y2 :"))

distance = math.sqrt( ((x1-y1)**2)+((x2-y2)**2) )

print(distance)


#12 Feet to centimeter Converter

userHeight = float(input("Enter Height in feet"))

totalCm = userInput * 30.48

print("There are ",totalCm , " cm in ",userInput," ft")


#13 BMI Calculator

userHeight = float(input("Enter Your Height in Cm"))
userWeight = float(input("Enter Your Weight in kg"))

heightInMeters = userHeight * 0.01


totalBmi = userWeight / (heightInMeters * heightInMeters)



print(totalBmi)


#14 Sum of n Positive Number

sumNumber = 0

userNumber =int(input("Enter Number Of n"))
if userNumber >=0:
    total = int(userNumber * (userNumber + 1)/2)
    print(total)
else:
    print(userNumber," is not positive Number")


#15 Digit sum of a Number

number =int(input("Enter a Number"))

sumnum = str(number)

lst = list(sumnum)


totalDigits = ' + '.join(sumnum)

print(totalDigits)

total = 0
while number>0:
    digit = number%10
    total = total+digit
    number = number//10
print("Sum Of ", totalDigits, " is ", total)



#16 Decimal To Binary Converter

decimalNumber = int(input("Enter a decimal number "))
finalDecimalNumber = decimalNumber

# to store binary numbers in list
array=[]

while(decimalNumber>0):
    digit=decimalNumber%2
    array.append(digit)
    decimalNumber=decimalNumber//2
    
    # Converting integer list to string list
    s = [str(i) for i in array] 
      
    # Join list items using join() 
    res = int("".join(s))     
array.reverse()

print("Binary Representation of ", finalDecimalNumber," is ",res,end=" ")



#17 Binary To Decimal Converter

binaryNumber = input("Enter a Binary number ")
binaryNumberList = list(binaryNumber)
defaultValue = 0
actualNumber = str(binaryNumber)



for d in range(len(binaryNumberList)):
    numbers = binaryNumberList.pop()
    if numbers == '1':
        defaultValue = defaultValue + pow(2, d)
print("Decimal Representation of ", actualNumber," is " ,defaultValue)



#18 Vowel and Consonants Counter 

userInput = input("Enter Text ")
vowels = 0
consonants = 0
for i in userInput:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print("Vowels : ",vowels)
print("Consonants : ",consonants)


#19 Palindrome tester 

userInput = input("Enter Text :")
palindrome = userInput[::-1]
if userInput == palindrome:
    print("Text " , userInput," is Palindrome")
else:
    print("Text " , userInput," is not Palindrome")


#20 Count Alphabets, Numbers and Special Characters  

userInput = input("Please Enter your Own String : ")
alphabets = digits = special = 0
spaces = userInput.count(' ')
for i in range(len(userInput)):
    if(userInput[i].isalpha()):
        alphabets = alphabets + 1
    elif(userInput[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1

specialCharacter = special - spaces
print("\nTotal Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", specialCharacter) 
print("Total Number of Spaces in this String :  ", spaces)



#21 Pattern 1

number=5;
for i in range(number):
    for j in range(i):
        print ('* ', end="")
        
    print('')

for i in range(number,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


#22  Pattern 2 

number=5
random = 1
for i in range(number):
    for j in range(i):
        print (j+1, end="")
    
    print('')

for i in range(5,0,-1):
    for j in range(i):
        print(j+1, end="")
    print('')


#23 Pattern 3

for i in range(10):
    print(str(i) * i)