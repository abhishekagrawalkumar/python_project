import json
import difflib
x = json.load(open("dictionary.json"))
#difining the function to check the value exist or not!!
def meaning(word):
    word = word.lower()
    if word in x:
        return x[word]
    elif word.title() in x:
        return x[word.title()]
    elif word.upper() in x:
        return x[word.upper()]
    else:
        next = difflib.get_close_matches(word,x.keys(),1)
        print("Do u mean ", next[0],"?")
        ans = input("press 'Y' for yes and 'N' for no : ")
        if (ans=="y" or ans =="Y"):
            return x[next[0]]
        else:
            print(word,"-- Invalid word !!")


word = input("Enter the word:- ")
s = meaning(word)
print()
#print diffrent meaning in different line
if (type(s)==list):
    for item in s:
        print(item)
