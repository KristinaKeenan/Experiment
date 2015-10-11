import random
import turtle

def isInScreen(w,t,t2):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()
    turtleZ = t2.xcor()
    turtleA = t2.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        t.right(180)
    if turtleY > topBound or turtleY < bottomBound:
        t.right(180)
    if turtleZ > rightBound or turtleZ < leftBound:
        t2.right(180)
    if turtleA > topBound or turtleA < bottomBound:
        t2.right(180)
    if turtleA == turtleX and turtleZ == turtleY:
        t.right(180)
        t2.right(180)

    return stillIn




def main():
    t = turtle.Turtle()
    t2 = turtle.Turtle()
    wn = turtle.Screen()
    t.shape('turtle')
    t2.shape('turtle')
    
    while isInScreen(wn,t,t2):
        coin = random.randrange(0, 2)
        if coin == 0:
            t.left(random.randrange(0,360))
            t2.left(random.randrange(0,360))
        else:
            t.right(random.randrange(0,360))
            t2.left(random.randrange(0,360))

        t.forward(50)
        t2.forward(50)        

 


main()
wn.exitonclick()




