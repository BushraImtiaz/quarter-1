try:
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    division = num1/num2
    print(num1,"/",num2,"=",division)
    excepts:
        print("change the value of denominator , 0 is not allowed sss")
    finally:
        print("I am in the final block")