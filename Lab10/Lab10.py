#Kristina Keenan
#4/15/15
#The purpose of this program is to take a file of data and print information from that data
#and performing various mathematical analyses with the data, such as median and mode.


def importSheet():
    '''This function opens a spreadsheet and reads its lines for use later in the program'''
    readSpreadSheet = open("spreadSheet.csv", "r")
    spreadSheet = readSpreadSheet.readlines()

    return spreadSheet



def theHigh(numbers):
    '''This function finds the highest number in a list, or the maximum'''
    
    theHigh = 0
    for i in numbers:
        
        if int(i) > theHigh:
            theHigh = int(i)
        else:
            theHigh = theHigh

    return theHigh


def theLow(numbers):
    '''This function finds the lowest number in a list, or the minimum'''
    
    theLow = 10
    for i in numbers:
        
        if int(i) < theLow:
            theLow = int(i)
        else:
            theLow = theLow

    return theLow
        

def theMean(numbers):
    '''This function adds all of the numbers in a list and then divides them by the number
    of items in the list. The mean/average.'''
    addingTotal = 0
    for i in numbers:
        addingTotal = addingTotal + int(i)
    dividingTotal = addingTotal / 10
    return dividingTotal



def theMedian(numbers):
    '''The number that is in the middle of the list. In this case it's the average of the two
    values in the middle of the list.'''
    newList = []
    maximumNumber = 0
    for i in numbers:
        j = int(i)
        newList = newList + [j]
    
    newList.sort()
    theMedian = (newList[4] + newList[5]) / 2
    return theMedian


        
        
def theMode(numbers):
    '''The number that occurs the most in a list.'''
    newList = []
    maximumNumber = 0
    for i in numbers:
        j = int(i)
        newList = newList + [j]
    newList.sort()
    countingNumber = 0
    anotherList = []
    for j in newList:
        countingValue = newList.count(j)
        #If the number of times a number appears is higher than the ones before it, then it is
        #the mode
        if countingValue > countingNumber:
            countingNumber = countingValue
            answerNumber = [j]
    anotherList = anotherList + answerNumber

    return anotherList
    

        
    
    
            


def calculateSpreadSheet(spreadSheet):
    '''This function calls all of the number manipulation functions and then prints them out'''
    for i in spreadSheet:
        #removes \n occurrences
        person = i.replace("\n","")
        newperson = person.split(",")
        highestNumber = theHigh(newperson[1:])
        lowestNumber = theLow(newperson[1:])
        averageMean = theMean(newperson[1:])
        findMedian = theMedian(newperson[1:])
        findMode = theMode(newperson[1:])
        #prints out the table
        print(newperson[0],"\t","|",highestNumber,"\t","|",lowestNumber,"\t","|",averageMean,"\t","|",findMedian,"\t","|",findMode)




def main():
    '''This is the main function which imports the spreadsheet, sets up the header, and calls
    the calculateSpreadSheet function.'''
    spreadSheet = importSheet()

    print("Name","\t","\t","|Maximum","|Minimum","|Mean","|Median","|Mode")
    print("-------------------------------------------------------")

    calculateSpreadSheet(spreadSheet[1:])

main()
