import random


class robot:

    def __init__(self):

        """Our robot constructer."""

        self.moods = ["neutral","angry","happy","'kill all humans'"]
        self.eyecolors = ["off","red","green","electric crimson"]
        self.mood = ""
        self.eyecolor = ""


    def changemood(self):
        r = random.randint(0,3)
        self.mood = self.moods[r]
        self.eyecolor = self.eyecolors[r]


    def printmood(self):
        print("My mood has changed!")
        print("I am feeling very",self.mood,"right now!")
        print("My eyes are now",self.eyecolor)


def main():
    kristina = robot()
    kristina.changemood()
    kristina.printmood()

    kristina.changemood()
    kristina.printmood()


main()
