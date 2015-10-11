def maximum(myList):
    x = 0
    for i in range(len(myList)):
        if myList[i] > x:
            x = myList[i]
    return(x)


def main():
    print("What's the maximum?")
    myList = [int(input("First Number:")),int(input("Second Number:")),int(input("Third Number:"))]
    print("Maximum:",maximum(myList))


main()
