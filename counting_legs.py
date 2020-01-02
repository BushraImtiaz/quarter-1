#  ---------- Counting legs ---------------

chick = int(input("Enter the number of chickens:   "))
cow = int(input("Enter the number of cows:  "))
pi = int(input("Enter the number of pigs:  "))

leg = (chick*2) + (cow*4) + (pi*4)

print("Animals ( ",chick," , ",cow," , ",pi,") = ", leg )