#Kristina Keenan
#2/12/15
#The purpose of this program is to calculate the area of two houses


def calcRectArea(l, w):
    """Calculate the area of the rectangular sections of the house"""
    rectArea = l * w
    return(rectArea)

def calcTriangleArea(b, h):
    """Calculate the area of the triangular sections of the house"""
    triangleArea = (b * h)/2
    return(triangleArea)

def main():
    """The main function, collecting values and doing final calculations"""
    print("Painting footage calculator, please enter values to compute:")
    finalTotal = 0
    for i in range(1,3):
        #intial variables
        width = int(input("What is the width?"))
        length = int(input("What is the length?"))
        height = int(input("What is the height?"))
        gable = int(input("What is the gable length?"))

        #calculated variables
        front = calcRectArea(length, height)
        side = calcRectArea(width, height) 
        triangle = calcTriangleArea(width, gable)

        #final calculations
        total = (2 * triangle) + (2 * side) + (2 * front)           
        print("Total for house:", total)
        finalTotal = total + finalTotal

    print("Total for two houses:", finalTotal)
    

main()





    
