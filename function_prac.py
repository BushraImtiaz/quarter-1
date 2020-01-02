#def add(num1, num2):
#    return num1 + num2
#def divide(num1, num2):
#    return num1/num2

#print(add(1,2))
#print(add(2, num2=3))
#print(divide(num2=4, num1=2))

#def add(*numbers):
#    total =0
#    for num in numbers:
#    total += num
#   return total

#print(add(1 ,2 ,3, 4, 5))
#print(add(4,5))

def add(num1, num2=5, num3=):
    total=num1 +num2
    for num in numbers
    total = num1 + num2 + num3
    return total

print(add(2, num3=4))

lst= [1, 2, 4, 6, 31, 11]
even_numbers = [i for i in lst if i%2==0]
print(even_numbers)

def even(lst, fn):
    evens=[]
    for num in lst:
        if fn(num):
            evens.append(num)
            return evens

print(even(lst, lambda x:x %2==0))