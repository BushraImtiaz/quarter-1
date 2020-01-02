#  ----------- Password approval ------------ 

sp = ["!","@","#","$","%","^","&","*","_","(",")","=","+","{","}",":",";","'","?","<",".",",",">"]

def checking(s):
    while True:
        if len(s) >= 6 and len(s)<= 24:
            print("Invalid. Password should be more than 6 characters and less than 24 characters")
            continue
        elif not any (character.isupper() for character in n):
            print("Invalid. Password should contain atleast one uppercase letter")
            continue
        elif not any (character.islower() for character in n):
            print("Invalid. Password should contain atleast one lowercase letter")
            continue
        elif not any (character.isdigit() for character in n):
            print("Invalid. Password should contain atleast one digit")
            continue
        elif not any (character in sp for character in n):
            print("Invalid. Special characters found")
            continue
        else:
            print("Password Valid")
            break
                    

n = input("Enter your password:  ")
checking(n)
print(checking(n))
