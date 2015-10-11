
import turtle
import random
import math

def dl(a,b,c,d, e, f, g):
    bob = turtle.Turtle()
    bob.shape("blank")
    bob.speed(0)
    bob.color(e, f, g)
    
    bob.up()
    bob.goto(a,b)
    bob.down()
    bob.goto(c,d)

def dd():
    num=random.randrange(2,5)
    num2=random.randrange(0,2)
    if num2==0:
        num = -1 * num
    return num


def dls():
    """draws random lines on the screen that bounce around"""
    w=340
    h=320
    f=0
    j=0
    k=0
    m=0
    finc=dd()
    jinc=dd()
    kinc=dd()
    minc=dd()

    s1=random.random()
    s2=random.random()
    s3=random.random()
    e1=random.random()
    e2=random.random()
    e3=random.random()

    inc1=(e1-s1)/100
    inc2=(e2-s2)/100
    inc3=(e3-s3)/100

    a=0
    while(True):
        
        s1 = s1 + inc1
        s2 = s2 + inc2
        s3 = s3 + inc3

        a = a + 1
        
        if a >= 100 or s1 >= 1 or s1 <= 0 or s2 >= 1 or s2 <= 0 or s3 >= 1 or s3 <= 0:
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
        if f>w:
            finc = finc * -1
        j = j + jinc
        if j>h:
            jinc = jinc * -1
        k = k + kinc
        if k>w:
            kinc = kinc * -1
        m = m + minc
        if m>h:
            minc = minc * -1
            
        dl(f,j,k,m, s1, s2, s3)
    
def main():
    dls()

main()
