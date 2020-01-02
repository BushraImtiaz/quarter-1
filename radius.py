"""1.	Write a Python program which accepts the radius of a circle from the user 
and compute the area"""

print("****AREA OF CIRCLE****")

import math
radius=int(input("Enter radius of a circle : "))
area=math.pi*((radius)**2)
print("Area of a circle is : ", area)