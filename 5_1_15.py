def checkWord(wordList,newWordIndex):
    wordBefore = wordList[newWordIndex - 1]
    wordAfter = wordList[newWordIndex]
    revWordBefore = ""

    for i in wordBefore:
        revWordBefore = i + revWordBefore

    if revWordBefore[0] == wordAfter[0]:
        return True
    else:
        return False


def main():
    wordList = []
    startWord = input("Enter a word:")
    wordList.append(startWord)
    i = 0
    correctAnswer = True

    while correctAnswer == True:
        nextAnswer = input("Okay, enter the next word:")
        wordList.append(nextAnswer)
        correctAnswer = checkWord(wordList,i+1)
        i = i + 1

    if correctAnswer == False:
        print("Too bad, game over! Word list:",wordList)


main()
