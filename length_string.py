#  ------------- Equal length of string ------------- 

s1 = input("Enter the first string:   ")
s2 = input("Enter the second string:   ")

n1 = len(s1)
n2 = len(s2)

def checklen(len1,len2):
    if len1 == len2:
        return True
    else:
        return False

checklen(n1,n2)
print(checklen(n1,n2))