chickens = int(input(" Enter the number of chickens in your farm: "))
pigs= int(input(" ENter the number of pigs in your farm :"))
cows = int(input(" Enter the number of cows in your farm:"))
chlegs = chickens * 2
chpigs = pigs * 4
chcows = cows * 4
total_animals = chickens + pigs + cows
total_legs = chlegs + chpigs + chcows
print(" You have total" , total_animals ,"animals in your farm,")
print(" So according to it,")
print(" The total animals legs are ", total_legs)