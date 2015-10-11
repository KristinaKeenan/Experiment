#print("Here is a loop thorugh a list of integers.")

#for i in range(40):
 #   i = i*2
    #print(i)

stringRepeat = input("Enter the number of times to repeat:")

integerRepeat = int(stringRepeat)

stringAdd = input ("What number do you want to add:")

integerAdd = int(stringAdd)

v = 0

for i in range(integerRepeat):

     v = v + i + integerAdd

     print(v)
     
    
print(v)
    

