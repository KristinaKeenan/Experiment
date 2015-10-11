import turtle
import random
import math


def startDrawing(f,j,k,m, s1, s2, s3):
    '''Draws the turtle'''

    
    wn = turtle.Screen()
    
    
    bob = turtle.Turtle()
    bob.shape("blank")
    bob.speed(0)
    bob.color(s1, s2, s3)
    
    bob.up()
    bob.goto(f,j)
    bob.down()
    bob.goto(k,m)



    


def coordinateChange():
    '''Determines numbers to increment the turtle by'''
    num=random.randrange(2,5)
    num2=random.randrange(0,2)
    if num2==0:
        num = -1 * num
    return num


def drawLines():
    '''Sets and changes colors and positioning'''
    
    #width/height
    width=340
    height=320


    
    #starting coordinates
    f=0
    j=0
    k=0
    m=0
    #how much each coordinate changes each time
    finc=coordinateChange()
    jinc=coordinateChange()
    kinc=coordinateChange()
    minc=coordinateChange()


    #colors (red/blue/green)
    s1=random.random()
    s2=random.random()
    s3=random.random()

    #color increment numbers?
    e1=random.random()
    e2=random.random()
    e3=random.random()

    #color increments
    inc1=(e1-s1)/100
    inc2=(e2-s2)/100
    inc3=(e3-s3)/100

    a=0
    while(True):
        
        s1 = s1 + inc1
        s2 = s2 + inc2
        s3 = s3 + inc3

        a = a + 1

        #changes colors when a is greater than or equal to 100, or when s1, s2, or s3 goes out of the (0,1) bounds for color
        if a >= 100:
            a = 0
            s1=e1
            s2=e2
            s3=e3
            e1=random.random()
            e2=random.random()
            e3=random.random()
            inc1=(e1-s1)/100
            inc2=(e2-s2)/100
            inc3=(e3-s3)/100
        
 
        


        f = f + finc

        if f>width or f < -width:
            finc = finc * -1
        j = j + jinc
        if j>height or j<-height:
            jinc = jinc * -1
        k = k + kinc

        if k>width or k<-width:
            kinc = kinc * -1
        m = m + minc
        if m >height or m<-height:
            minc = minc * -1

            
        startDrawing(f,j,k,m, s1, s2, s3)
    
def main():
    '''The main function'''
    drawLines()

main()
