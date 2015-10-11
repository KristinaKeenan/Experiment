def vowelCheck(englishString):
    vowels = "AEIOUaeiou"
    if englishString[0] in vowels:
        return True
    else:
        return False

def vowelGet(englishString):
        pigLatin = englishString + "way"
        return pigLatin

def consonantGet(englishString):
    newWord = ""
    vowels = "AEIOUaeiou"
    charend = False
    for aChar in englishString:
        if aChar not in vowels and charend == False:
            newWord = newWord + aChar
    else:
        charend = True
    sliceOff = len(newWord)
    pigLatin = englishString[sliceOff:len(englishString)] + newWord + "ay"
    return pigLatin
    

def main():
    englishString = input("What do you want to translate?")
    if vowelCheck(englishString):
        newphrase = vowelGet(englishString)
    else:
        newphrase = consonantGet(englishString)
        
    print("Your word:","\n",englishString)
    print("Translated word:","\n",newphrase)

main()



#algorithm:
#first you create a function that calls for input of a string, then call a function that translates that
#function into pig latin. This function first determines if the string begins with a vowel or a
#consonant. There is an if statement that prints the string from the second letter to the last using a slice,
#then concates the first letter to the end of that using a string and then adds the string "ay".
#If it begins with a vowel, then the string "way" is concated to the end of the string.


#myString = "This class is awesome"
#stringList = "myString.split(" ")
#stringList is now: ["This","class","is","awesome"]
