# ------------- Library ----------------

# def lib(ty):
#     if ty == "Fiction" or ty == "fiction":
#         genrefic(gen)
#     elif ty == "Non Fiction" or ty == "non fiction":
#         genrenonfic(gen)
#     else:
#         print("Invalid category entered")


def genrefic(ge):
            if ge == "Comedy".lower():
                return 'A'
            elif ge == "Comic".lower():
                return 'B'
            elif ge == "Sci Fi".lower():
                return 'C' 
            elif ge == "Fantasy".lower():
                return 'D'
            elif ge == "Historic Fiction".lower():
                return 'E'
            else:
                print("Invalid genre. Please check in the Non-Fiction area.")

def genrenonfic(ge):
            if ge == "History or Geography".lower():
                return 'F'
            elif ge == "Art".lower():
                return 'G' 
            elif ge == "Science and Technology".lower():
                return 'H'
            elif ge == "Other".lower():
                return 'I'
            else:
                print("Invalid genre. Please check in the Fiction area")


ch = input("Enter whether you want to search in Fiction or Non-Fiction:  ")

if ch == "fiction".lower():
    gen = input("Enter the genre you are looking from:  ")
    genrefic(gen)
    print(genrefic(gen))
elif ch == "nonfiction".lower():
    gen = input("Enter the genre you are looking from:  ")
    genrenonfic(gen)
    print(genrenonfic(gen))
else:
    print("Incorrect Category")