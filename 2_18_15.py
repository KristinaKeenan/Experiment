#isRunning = True
#x = 0

#while isRunning:
 #   print("I should only see this once")

 #   if x > 5:
        #isRunning = False
#

 #   x = x + 1



def runStory(isEnded):
    while not isEnded:
        choice = input("Your Choice:")

        if choice == "funkadelic":
            story = "fkasl;fkld"
            instructions = "s;fkjdskfsdk"
        elif choice == "slow ride":
            story ="asdfsadf"
            instructions = "adfsd"
        else:
            story = ""
            instructions = ""
            isEnded = True




def main():
    print(input("enter thing here"))
    isOver = False
    runStory(isOver)


main()
