ldict={
    'hello':'otai',
    'hi':'oty',
    'hey':'oai',
    'meet':'reask',
    'whatsup':'imitzio',
    'good':'saiie',
    'how':'roke',
    'you':'oka',
    'do':'irru',
    'next':'iep',
    'first':'oa',
    'second':'ob',
    'bye':'sotai',
    'tell':'sapi',
    'end':'rdn',
    'and':'iu',
    'see':'ryz',
    'sea':'oli',
    'water':'rias',
    'building':'rumpa',
    'attack':'shar',
    'kill':'oiep',
    'destory':'iros',
    'capture':'suz',
    'save':'imma',
    'survive':'rive',
    'hold':'oos',
    'fly':'sakoz',
    'to':'ot',
}
new_key = input("Enter a word Translate form Englist to Alien or Alien to English: ")
output = 0
for key_word, value_word in ldict.items():
    if (key_word == new_key):
        output = value_word
    elif (value_word == new_key):
        output = key_word
print(output)
if output == 0:
    for key_word, value_word in ldict.items():
        if not(key_word == output):
            new_value = input("Enter the meaning of the word: ")
            ldict[new_key] = new_value
            print("new word:", new_key,"\nmeaing: ", new_value)
            break
        elif not(value_word == output):
            new_value = input("Enter the meaning of the word: ")
            ldict[new_key] = new_value
            print("new word:", new_key,"\nmeaing: ", new_value)
            break