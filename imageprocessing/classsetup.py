import cImage as image

def red(img):
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())

    for col in range(img.getHeight()):
        for row in range(img.getWidth()):
            p = img.getPixel(col, row)

            red = p.getRed()
            newBlue = 0
            newGreen = 0

            newpixel = img.Pixel(red, newGreen, newBlue)

            newimg.setPixel(col, row, newpixel)

            
    newimg.draw(win)
            

def main():
    win = image.ImageWin()
    img = image.Image("treeSmall.gif")
    w = img.getWidth()
    h = img.getHeight()
    newImage = image.EmptyImage(w,h)


    for row in range(h):
        for col in range(w):
            p = img.getPixel(col,row)
            newpixel = image.Pixel(p.getRed(),0,0)
            newImage.setPixel(col,row,newpixel)


    

    
    newImage.draw(win)
    win.exitonclick()



main()
