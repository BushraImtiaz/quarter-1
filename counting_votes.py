#  -------------- Counting of votes ----------------- 

print("Following teams entered the competition: \nA\nB\nC\nD")

from collections import Counter

def majority_vote():
    votes = []

    for i in range(1,6):
        v = input("Enter your choice:  ")
        votes.append(v)
    print(votes)
    
    n = len(votes)

    votes = Counter(votes)
     
    for i,j in votes.items():
        if j > n/2:
            win = i
            print("Majority votes: ",win)
        else:
            print("None")

majority_vote()