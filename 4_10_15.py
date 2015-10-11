def letterRepeat(theList):
    newList = theList
    
    for i in newList:
        newListLetters = i.split
        for j in range(len(newListLetters)):
            if newListLetters[j] == newListLetters[j-1]:
                newList[i] = i
            else:
                newList[i] = ""

    return newList


def main():
    theList = ["bob", "alligator","cannot","thee"]
    finalList = letterRepeat(theList)
    print(finalList)
    


main()
