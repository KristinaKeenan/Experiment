#Kristina Keenan
#4/1/15
#The purpose of this program is to take user input and check it to see if a) one word is a
#palindrome, and b) if two words are anagrams of each other.


def removePunctuation(inputString):

    """ This function removes all punctuation and spaces from the inputed string so that
    it can be accurately tested in later functions. """
    
    justLetters = ""

    #removes all characters other than lowercase letters
    for i in inputString:
        if ord(i) >= 97 and ord(i) <=122:
            justLetters = justLetters + i
    return justLetters



def palindrome(string):

    """ This function takes one piece of user input and reverses its order. If the order of the
    input matches the order of the reversed string, then the function returns True, else False."""

    reversed1 = ""
    
    #makes a new string thats the reverse of the input
    for achar in string:
        reversed1 = achar + reversed1

    #if the order of the new string is the same as the old one, it's a palindrome
    if reversed1 == string:
        return True
    else:
        return False


def anagram(word1,word2):

    """ This function takes two pieces of user input and tests them to see if they share the
    same number and kind of letters. If they are anagrams, True is returned, else False."""

    theNumber = 0

    #Tests if both words share the same letters, if they do and the accumulator value equals
    #the length of the string, then the two words are anagrams of each other
    for i in word1:
        for j in word2:
            if i == j:
                theNumber = 1 + theNumber

                #goes to next i value
                break
            
            else:
                theNumber = theNumber
    if theNumber == len(word1):
         return True
    else:
         return False

      
            




def main():

    """ This function collects three pieces of user input and formats the input to be used
    in later functions. """
    
    print("Is this a palindrome?")
    palindromeInput = input("Word to test:")

    #This makes all the letters in the input lowercase and removes punctuation and spaces
    string = removePunctuation(palindromeInput.lower())

    #Tests if input is a palindrome
    pTrueFalse = palindrome(string)

    if pTrueFalse:
        print(palindromeInput,"IS a palindrome!")
    else:
        print(palindromeInput,"is NOT a palindrome!")

    print("Are these anagrams of each other?")
    
    anagramInput1 = input("First word to test:")
    anagramInput2 = input("Second word to test:")

    #This makes all the letters in the input lowercase and removes punctuation and spaces
    word1 = removePunctuation(anagramInput1.lower())
    word2 = removePunctuation(anagramInput2.lower())

    #Tests if inputs are anagrams
    aTrueFalse = anagram(word1,word2)

    if aTrueFalse:
        print(anagramInput1, "and", anagramInput2, "ARE anagrams of each other!")
    else:
        print(anagramInput1, "and", anagramInput2, "are NOT anagrams of each other!")


    #asks user if they want to repeat process, calls main if yes, ends program if no
    repeatProgram = input("Do you want to test more words? Type Yes or No:")

    if repeatProgram == "yes" or repeatProgram == "Yes":
        main()
    


main()
