def changeAges(myFamily):
    myFamily2016 = myFamily.copy()

    for j in myFamily2016:
        myFamily2016[j] = myFamily2016[j] + 1
        
    
    print(myFamily2016)


def createList(nameList, ageList):
    myFamily = {}
    j = 0
    for i in nameList:
        myFamily[i] = ageList[j]
        j = j + 1

    print(myFamily)

    changeAges(myFamily)


def main():
    nameList = ["Heather","Mike","Kristina","Tom"]
    ageList = [50,51,19,14]

    createList(nameList, ageList)




main()

        
