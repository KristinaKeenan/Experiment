#Kristina Keenan
#2/5/15
#The purpose of this program is to drawn increasingly lighter and larger cocentric cirlces

#import and set up turtle
import turtle
wn = turtle.Screen()
square = turtle.Turtle()

#write a statement to determine how many squares
squareNumber = int(input("How many squares are you drawing?"))


#intialize the variables for the colors and length
red = 0

green = 0

blue = 0

length = 1

square.speed(0)

#create the loop
for i in range (squareNumber):

        #squares
        square.pendown()
        square.forward(length)
        square.left(90)
        square.forward(length)
        square.left(90)
        square.forward(length)
        square.left(90)

        #redefine the length
        length = (length + 1)
        

        #color
        square.color(red, green, blue)
        red = (red + 1/squareNumber)
        green = (green + 1/squareNumber)
        blue = (blue + 1/squareNumber)
