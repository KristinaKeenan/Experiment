word = "watermelon"



#double
for achar in word:
    
    if achar == "a" or achar == "e" or achar == "i" or achar == "o" or achar == "u" or achar == "A" or achar == "E" or achar == "I" or achar == "O" or achar == "U":
        achar = achar + achar
        print(achar, end = "")
    else:
        achar = achar
        print(achar, end = "")
print("\n")



#reverse
reversedword = ""
for achar in word:
    reversedword = achar + reversedword
print(reversedword)
print("\n")



#capitalize
capstring = ""
for i in range(len(word)):
    if i % 2 > 0:
        capstring = capstring + word[i].upper()
    else:
        capstring = capstring + word[i].lower()
print(capstring)
    


    
