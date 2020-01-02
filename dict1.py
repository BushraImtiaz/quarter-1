#Object: Create a dictionary for Alien language to english and vise versa.Using filling and Exception handling

import json
list_alien=["ha","ary","yaa","dodo","ee","woe","da","reve","far","hake","tu"]
list_human=["hi","are","you","destroying ","earth","what","do","revenge","from","take","to"]

# save in file
with open("dic.json","w") as f:
        json.dump(list_alien,f)
with open("dic1.json","w") as f:        
       json.dump(list_human,f)

#retrive list form file
with open("dic.json") as f:
        list_alien_lang=json.load(f)
with open("dic1.json") as f:
        list_human_lang=json.load(f)
        
st =input("Enter a word: ")
try:
                
                     
        for c in range(len(list_alien_lang)):
                if list_alien_lang[c] == st.lower():
                        i = c
                        st1 = "human language"
                        word = list_human_lang[i]
                        break

        for c in range(len(list_human_lang)):
                if list_human_lang[c] == st.lower():
                        i = c
                        word = list_alien_lang[i]
                        st1 = "alien language"
                        break
                                         
        print(st + " meaning in " + st1 +" is: " + word)

except:
        print("This word dose not exist in our dictionary")
