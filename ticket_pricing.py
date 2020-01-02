print("Water Park Ticket Pricing")
age=int(input("Enter your age:"))
if age==0 or age<0:
    print("Sorry you can't Allow !!")
elif 0<age<=3:
    print("Ticket Price: Free !")
elif 3<age<=12:
    print("Ticket Price: 150 Rs")
elif 12<age<=17:
    print("Ticket Price: 250 Rs")
elif 18<=age<=25:
    print("Ticket Price: 300 RS")
elif 25<age<=40:
    print("Ticket Price: 500 Rs")
elif 40<age<=60:
    print("Ticket Price: 400 Rs")
else:
    print("Sorry you also can't Allow")