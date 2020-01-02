def addi(a,b,*c,**d):
    sum1 = 0
    sum2 = 0
    for i in (c):
        sum1 = i +sum1
    for j in (d):
        sum2 = i + sum2
    return a + b + (sum1) + (sum2)

print (addi(1,2,3,4,6,7))