#Kristina Keenan
#January 29, 2015
#The purpose of this program is to help the user understand counting.

#Enter a name
userName = input("Please enter your name:")


#Enter number to count by
numberCount = input("Please enter a number to count by:")


#Change number to count by into a float
numberCount = float(numberCount)


#Round number to count by to two decimals
numberCount = round(numberCount, 2)

#Enter number of steps
numberSteps = input("Please enter the number of steps:")

#Change number of steps to an integer
numberSteps = int(numberSteps)

#Print Let's begin message
print("Let's begin counting", userName)

#set the count total to 0
countTotal = 0

#Start Loop
for step in range(numberSteps):

    countTotal = countTotal + numberCount
    
    print("Step", step + 1, ": count is", round(countTotal, 2))

#Print goodbye message
print("The counting is complete! Come back if you want to count some more!")
    
