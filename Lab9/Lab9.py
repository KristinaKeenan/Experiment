#Kristina Keenan
#4/8/15
#The purpose of this program is to take an inputed phrase and check to see if it spelled correctly.




def wordIndex():
    '''This function reads a file and creates a list of words from it.'''
    wordIndex1 = open("words1.txt", "r")
    #wordIndex2 = open("words2.txt","r")

    words1 = wordIndex1.readlines()
    #words2 = wordIndex2.readlines()
    return words1


def listMaker(wordsCheck):
    '''This function takes the inputed phrases and creates a list out of the words.'''
    wordsList = wordsCheck.split(" ")
    return wordsList


def suggestions(mispelledWord):
    '''This function sees if an iterance of a mispelled word is erroneous because it is two correct words without a space in between them.
    If so, then the function prints a suggested way to fix the problem.'''

    words = wordIndex()

    #This sees splits the misspelled word into two words that are spelled correctly
    for i in range(len(mispelledWord)):
        if mispelledWord[:i] + "\n" in words and mispelledWord[i:] in words:
            print("Here's a suggestion: \n",mispelledWord[:i],mispelledWord[i:])
    


def spellCheck(wordsCheck):
    '''This function checks to see if the words in the phrase are in the word list or are mispelled, and then
    calls functions or prints phrases accordingly.'''
    wordsList = listMaker(wordsCheck)
    
    words1 = wordIndex()
    
    check = 0

    #These see if all the words are correct, or if there are some correct/incorrect
    for i in wordsList:
        if i + "\n" in words1:
            check = check + 1

    if check == len(wordsList):
        print("This entire phrase is correct.")
    else:
        for i in wordsList:
            if i + "\n" in words1:
                print(i,"is spelled correctly.")
                check = check + 1
            else:
                print(i,"may be mispelled.")
                #this checks to see if the misspelled words are two words without a space inbetween them.
                suggestions(i + "\n")
        


    tryAgain = input("Enter more words or 'quit' to quit:")

    if tryAgain != "quit":
        spellCheck(tryAgain)
    
        


def main():
    '''This is the main function, which accepts an inputed phrase and calls the spellCheck function.'''
    wordsCheck = input("Words to spellcheck:")


    spellCheck(wordsCheck)

 


main()



