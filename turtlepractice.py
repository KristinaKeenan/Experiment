#Program to write parallel lines that start black and progressively get redder

#basic info
import turtle
wn = turtle.Screen()
molly = turtle.Turtle()

#establish variables
lineNumber = int(input("How many lines?"))

lineSpace = int(input("How far away are the lines from each other?"))

molly.speed(0)

red = 0

blue = 1

molly.pensize(10)

#preposition
molly.penup()

molly.forward(-200)

molly.pendown()

#sequence drawing
for i in range(lineNumber):

    #color
    print(red)
    red = (1/lineNumber) + red
    blue = blue - (1/lineNumber)
    molly.color(red,0,blue)

    #drawing
    molly.left(90)
    molly.forward(100)
    molly.penup()
    molly.forward(-100)
    molly.right(90)
    molly.forward(lineSpace)
    molly.pendown()
 
