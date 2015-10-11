import random

class theDeck:
    def __init__(self):

        self.cardDictionary = {}
        theSuits = ["Spades","Hearts","Clubs","Diamonds"]
        for i in theSuits:
            for j in range(53):
                self.cardDictionary[j + ' of ' + i] = j
                self.cardDictionary = self.cardDictionary + {"2 of Spades": 2}




    def shuffleDeck():
        random.choice(d.keys())

    def printDictionary(self):
        return self.cardDictionary



def main():
    newDeck = theDeck()
    theDictionary = theDeck.printDictionary(newDeck)
    print(theDictionary)

main()
