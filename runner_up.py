#  ----------- Runner up score ------------ 

list = [
]

n = int(input("Enter the number of students:  "))

for i in range(n):
    ch = int(input("Enter the score: "))
    list.append(ch)

for i in range(n):
    if list[i] < list[i+1]:
        temp = list[i]
        list[i] = list[i+1]
        list[i] = temp

max = list.pop
runn = list.pop

if max > runn:
    print("The runner up score is:  ", runn)
elif max == runn:
    secrun = list.pop
    print("The runner up score is:  ", secrun)