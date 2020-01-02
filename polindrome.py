# ------------ Checking if polindrome is possible or not ----------

class possible_polindrome():
    def __init__(self,stri):
        self.stri = stri

    def checking_polindrome(self):
        re = self.stri[::-1]
        if re == self.stri:
            print("Polindrome is possible")
        else:
            print("Polindrome is not possible")

obj1 = possible_polindrome("acabbaa")
obj2 = possible_polindrome("aacbdb") 
obj3 = possible_polindrome("abacbb") 

obj1.checking_polindrome
obj2.checking_polindrome
obj3.checking_polindrome