def addPlusMinus(num,let):
    if num >=95:
        return let

    remainder = num % 10

    if remainder >= 7:
        let = let + "+"
    elif remainder <=3:
        let = let + "-"

    return let


def getLetterGrade(score):

    letGrade = ""

    if score >= 90:
        letGrade =addPlusMinus(score,"A")
    elif score >=80 and score <90:
        letGrade =addPlusMinus(score,"B")
    elif score >=70 and score <80:
        letGrade =addPlusMinus(score,"C")
    elif score >= 65and score < 70:
        letGrade =addPlusMinus(score,"D")
    else:
        letGrade = "F"

    return letGrade
        



def main():
    isRunning = True
    while isRunning:
        numberGrade = int(input("What is the grade?"))
        letterGrade=getLetterGrade(numberGrade)
        print(letterGrade)
        again = input("Do you want to enter another grade (Y/N)?")

        if again != "Y":
            isRunning = False
            print("Goodbye!")

 

main()
