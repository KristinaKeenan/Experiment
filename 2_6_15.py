import turtle
wn = turtle.Screen()
shape = turtle.Turtle()

shape.pensize(5)
shape.speed(0)

shape.penup()
shape.left(180)
shape.forward(200)
shape.left(180)
shape.pendown()


for i in range(3,13):
    for j in range(i):
        shape.left(360/i)
        shape.forward(10)
    shape.penup()
    shape.forward(50)
    shape.pendown()

                
    
   
