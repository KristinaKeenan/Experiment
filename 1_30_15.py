#compute the average of odds from 1 - 100

average = 0 #computed average

total = 0 #computed sum

steps = 0 #number of times through loop


for i in range(1,100,2):

    steps = steps + 1

    total = total + i

    average = total / steps
    
    print("The current total is:", total)
    print("The current average is:", average)
