li = [1, 2, 3, 85, 95, 65, 12]
def leng(lst):
    a = 0
    for i in lst:
        a = a + i
    return a
print ("The sum of the list is :", end = " ")
print (leng(li))