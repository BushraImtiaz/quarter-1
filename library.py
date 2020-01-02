#Question num 3:

''' MY LIBRARY '''

bookType = input("Are you looking for a fiction (type F) or a non-fiction book (type NF)?")
bookGenre = ''
if bookType =="F":
   bookGenre = int(input("What genre are you looking for: comedy (1), graphic novel (2), science fiction (3), fantasy (4), historial fiction (5)?"))
if bookType =="NF":
    bookGenre = int(input('What genre are you looking for: history (6), art (7), science (8), other(9)'))

if bookGenre == "F":
    print("You are looking for a comedy fiction book.")
    print("You will find it in bookshelf A.")
elif bookGenre == "NF":
    print("You are looking for a comic/graphic novel.")
    print("You will find it in bookshelf B.")