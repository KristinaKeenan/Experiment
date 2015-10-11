import turtle

def reposition(reBob,reSize):
    reBob.penup()
    reBob.forward(reSize * 1.3)
    reBob.pendown()

def preposition(preBob,preSize):
    preBob.penup()
    preBob.backward(preSize * 4)
    preBob.pendown()

def drawShape(drawBob,drawEdgelength,drawNumedges):
    for j in range(drawNumedges):
        drawBob.forward(drawEdgelength)
        drawBob.left(360/drawNumedges)

def createArt(artBob,artNumshapes,artSize,artNumedges,artEdgelength):
    for i in range(artNumshapes):
        drawShape(artBob,artEdgelength,artNumedges)

        artNumedges = artNumedges + 1
        artEdgelength = (3.14 * artSize)/artNumedges

        reposition(artBob,artSize)

def main():
    import turtle
    wn = turtle.Screen()
    bob = turtle.Turtle()

    numshapes = 10
    size = 50
    numedges = 3
    edgelength = (3.14 * size)/numedges


    preposition(bob,size)

    createArt(bob,numshapes,size,numedges,edgelength)
    


main()
