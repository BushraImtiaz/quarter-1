"""11.	Write a Python program to test whether a passed letter is a vowel or not"""

print("**** VOWEL OR NOT ****")

letter=input("Enter a letter : ")
vowels="a","e","i","o","u"
if letter in vowels:
        print("Letter is VOWEL")
else:
        print("Letter is not VOWEL")