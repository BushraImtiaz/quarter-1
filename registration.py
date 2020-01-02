name=input("enter the name")
gender=input("enter the gender")
age=int(input("enter the age"))
if(age<20 and gender=='male'):
    print(name,"please sit in the first two rows")
elif(age>=20 and gender=='male'):
    print(name,"please sit in the middle two rows")
elif(age<=20 and gender=='male'):
    print(name,"please sit in the middle forthss rows")
else:
    print("please sit in the last rows!")    
