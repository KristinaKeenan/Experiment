import cImage as image



def main():
    win = image.ImageWin()
    img = image.Image("spacetacocat.gif")
    w = img.getWidth()
    h = img.getHeight()
    newImage = image.EmptyImage(w,h)

    for row in range(h):
        for col in range(w):
            p = img.getPixel(col,row)
            newImage.setPixel(col,row,p)


    

    
    newImage.draw(win)
    win.exitonclick()


main()
