wordsCheck = input("Words to spellcheck:")

wordIndex1 = open("words1.txt", "r")
wordIndex2 = open("words2.txt","r")

words1 = wordIndex1.readlines()
words2 = wordIndex2.readlines()


for i in wordsCheck:
    if i not in words1 or i not in words2:
        print("this is mispelled")
    else:
        print("this is spelled correctly!")


