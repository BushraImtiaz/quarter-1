       #number guessing Game
winning_number= 23
guess_number=(int(input("guess a number between 1 to 50:")))
if guess_number==winning_number:
    print("YOU WIN !!!!")
    
else:
    if guess_number < winning_number:
        print("Too Low")
    else:
        print("Too High")

    # and operator (1+1) true
name = "hufsa"
age= 24
if name=="afshan" and age==24:
    print("condition True")
else:
    print("condition False")


    # OR operator (1+0) true
if name=="hufsa" or age==40:
    print("condition True")
else:
    print("condition False")
