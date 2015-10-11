#Kristina Keenan
#4/29/15
#The purpose of this lab is to create a credit card and perform operations on it.

class creditCard:
    """This class creates a credit card"""

    def __init__(self,name,number,score):

        self.holderName = name
        self.cardNumber = number
        self.balance = 0
        
        if score > 750:
            self.creditLimit = 10000
            self.interestRate = .08
        elif score >= 600 and score <= 750:
            self.creditLimit = 5000
            self.interestRate = .12
        else:
            self.creditLimit = 2000
            self.interestRate = .2

    def chargeAmount(self):
        """This method charges an amount to the credit card or declines the charge if the requested amount exceeds the allowed amount."""

        chargeAmount = int(input("How much do you want to charge?"))
        newBalance = self.balance + chargeAmount
        if newBalance > self.creditLimit:
            return False
        else:
            self.balance = newBalance
            return newBalance
            
    def checkBalance(self):
        """This method returns the card's balance."""
        
        return self.balance


    def payOff(self):
        """This method subtracts the amount paid off from the balance."""
        
        payingAmount = int(input("How much do you want to pay off?"))
        paidBalance = self.balance - payingAmount
        self.balance = paidBalance
        return self.balance

    def monthlyInterest(self):
        """This method calculates the monthly interest for the account and either adds it on to the balance or does nothing if the balance is 0 or negative."""
        
        if self.balance > 0:
            addedInterest = self.balance * self.interestRate
            interestBalance = int(self.balance + addedInterest)
            self.balance = interestBalance
        else:
            interestBalance = self.balance

        return interestBalance

    def transferMoney(self,referenceCard):
        """This method transfers part of the balance of one card onto the balance of another card, or does nothing if the value transferred exceeds the second card's allowing in accordance with its credit score."""
        
        transferAmount = int(input("How much do you want to transfer from the first card to the second card?"))
        firstBalance = self.balance - transferAmount
        self.balance = firstBalance
        if transferAmount > referenceCard.creditLimit:
            return False
        else:
            secondBalance = transferAmount + referenceCard.balance
            referenceCard.balance = secondBalance
            return transferAmount
        


def createCard():
    """This function creates a card object."""
    
    holderName = input("What is your name?")
    cardNumber = input("What is your card number?")
    creditScore = int(input("What is your credit score?"))

    cardCreate = creditCard(holderName,cardNumber,creditScore)

    return cardCreate


def bankFunctions(theDictionary):
    """This function performs any and all bank functions that the card can go through."""
    
    theCard = createCard()


    theDictionary[theCard.cardNumber] = theCard
    
    doSomething = input("Do you want to do anything? Yes or No:")

    if doSomething == "Yes" or doSomething == "yes":
        goAgain = True
    else:
        goAgain = False
    
    while goAgain == True:
        toDo = input("Do you want to: Charge, Check, Pay, Interest, Transfer, or Stop?")

        if toDo == "Charge" or toDo == "charge":
            charging = theCard.chargeAmount()
            if charging == False:
                print("Your charge was declined.")
            else:
                print("Your balance is now",charging,"dollars.")

        elif toDo == "Check" or toDo == "check":
            balance = theCard.checkBalance()
            print("Your balance is",balance,"dollars.")

        elif toDo == "Pay" or toDo == "pay":
            paidBalance = theCard.payOff()
            print("Your balance is now",paidBalance,"dollars.")

        elif toDo == "Interest" or toDo == "interest":
            interestBalance = theCard.monthlyInterest()
            print("Your balance after adding the monthly interest is",interestBalance,"dollars.")

        elif toDo == "Transfer" or toDo == "transfer":
            
            newCard = input("Do you want to transfer to an old card or a new card?")
            if newCard == "New" or newCard =="new":
                referenceCard = createCard()
            if newCard == "Old" or newCard == "old":
                referenceAccountNumber = input("What is the second card's account number?")
                if referenceAccountNumber in theDictionary:
                    referenceCard = theDictionary[referenceAccountNumber]
            transferResult = theCard.transferMoney(referenceCard)
            if transferResult == False:
               print("The transfer was declined.")
            else:
               print("You have successfully transferred",transferResult,"dollars from the first card to the second card.")

        else:
            goAgain = False


def main():
    """The main function starts and ultimately ends the program."""
    
    savingDictionary = {}
    print("Welcome to the BankProgram 2000!")
    createNew = True
    while createNew == True:
        createACard = input("Do you want enter a card?")
        if createACard == "yes" or createACard == "Yes":
            bankFunctions(savingDictionary)
        else:
            createNew = False
            print("Goodbye!")
    

         
main()
    
