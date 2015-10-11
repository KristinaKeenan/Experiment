#Kristina Keenan
#3/11/15
#The purpose of this program is to take an image and change it so it it only appears in four colors.

#First, cImage is imported. Next, the window is set up, and the original picture is imported, and its height and width are defined.
#Then, a new image is created in an empty image, using the same height and width as the original image. Each pixel of the old image
#are then put through a for loop and have their red, green, and blue color values averaged. These values are then divided into four
#groups and assigned new values. The new image is then drawn in the window using the newly colored pixels and displays an image that
#is similar to the original image except now showing in only four colors. The image then is closed on click.



import cImage as image


def drawImage(w,h,img,win):

'''This function takes the information from the old image, creates a space for a new image, and
creates that image by averaging the RGB values for each pixel of the old image and dividing those
values into four groups, each group given a separate color. The new image is then made with these colors.'''
    
    #space for new image
    newImage = image.EmptyImage(w,h)

    #nested loop to get each pixel
    for row in range(h):
        for col in range(w):

            #gets pixel information from old image
            p = img.getPixel(col,row)


            #gets old image color values
            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()

            #determines values to group pixels by for new colors
            brightness = (red + blue + green)/3.0

            #separates brightness values into color groups
            if brightness <= 64:
                newred = 217
                newgreen = 48
                newblue = 98
                
            elif brightness > 64 and brightness <=127.5:
                newred = 152
                newgreen = 129
                newblue = 245

            elif brightness > 127.5 and brightness <=191.25:
                newred = 249
                newgreen = 125
                newblue = 129
                
            else:
                newred = 249
                newgreen = 208
                newblue = 139


    
            #sets up new pixels
            newpixel = image.Pixel(newred, newgreen, newblue)

            #sets up new image
            newImage.setPixel(col, row, newpixel)


    

    #draws new image
    newImage.draw(win)

    #closes window on click
    win.exitonclick()


def main():

'''This function defines the window, the original image, and its width and height.'''

    #old image values
    window = image.ImageWin()
    oldimg = image.Image("spacetacocat.gif")
    width = oldimg.getWidth()
    height = oldimg.getHeight()
    
    #calls drawImage function
    drawImage(width,height,oldimg,window)
    




main()
