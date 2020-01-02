li = ['taha', 'sana', 'zainab', 'tajdar', 'hassan', 'hamza', 'amir', 'saud']
def leng(lst):
    a = 0
    for i in lst:
        a = a + 1
    return a
print ("The Lenght of the list is :", end = " ")
print (leng(li))