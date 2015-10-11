#Kristina Keenan
#4/22/15
#The purpose of this lab is to take an inputed name and check to see if it is in a directory.
#If so, then the program tells the user where to find the name they typed in.

def importSheet():
    '''This function opens a spreadsheet and reads its lines for use later in the program'''
    readSpreadSheet = open("Lab11.csv", "r")
    spreadSheet = readSpreadSheet.readlines()

    return spreadSheet

def upperLower(nameCheck):
    newNameCheck = ""
    for i in range(len(nameCheck)):
        if i == 0 or nameCheck[i - 1] == " ":
            newNameCheck = newNameCheck + nameCheck[i].upper()
        else:
            newNameCheck = newNameCheck + nameCheck[i]
    return newNameCheck


def nickName(nameCheck,theDirectory):
    '''This function sees if the name typed in is a shortened version of one in the directory.'''
    for i in theDirectory.keys():
        if nameCheck in i:
            print(i)


def ourDirectory(nameCheck):
    '''This function sees if the name typed matches one in the directory.'''
    spreadSheet = importSheet()
    theDirectory = {}
    for i in spreadSheet:
        person = i.replace("\n","")
        newperson = person.split(",")
        theDirectory[newperson[0]] = newperson[1]
    if nameCheck in theDirectory:
        print(nameCheck,"can be found in:",theDirectory[nameCheck])
    else:
        print(nameCheck,"is not found in our directory.")
        print("Did you mean:")
        spellCheck = nickName(nameCheck,theDirectory)
        
        
    


def main():
    '''This is the main function which takes in a word and asks if one wants to check another
    name or quit the program'''
    
    print("Welcome to our directory!")
    nameCheck = input("Who do you want to find?")

    newNameCheck = upperLower(nameCheck)

    ourDirectory(newNameCheck)

    goAgain = input("Type 'quit' to quit or a new name to find someone else.")

    while goAgain != "quit":
        ourDirectory(goAgain)
        goAgain = input("Type 'quit' to quit or a new name to find someone else.")
    
    

main()
