# -------------- Removing duplicate from a list -------------

import collections

st = ["Namjoon","Jungguk","Namjoon","Jimin","Jin","Taehyung","Jungguk","Yoongi","Jimin"]

def removedups(st):
    st = collections.Counter(st)

    for i,j in st.items():
        if j == 2:
            j = j - 1
        else:
            j = j
    
    st = list(st)
    print(st)

removedups(st)