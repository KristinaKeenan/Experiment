
myList = ["This","is","a","set","of","strings"]

item = "wednesday"

myList = myList + [item]

myList.append([item])

print(myList)


myFile = open("strings.txt", "r")
myLines = myFile.readlines()
print(myLines)
