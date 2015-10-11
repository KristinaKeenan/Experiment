#bank account

#Data
#account #, balance, name, interest rate, card #, Transaction history

#Methods
#withdraw, deposit, transfer, creating a history, constructer


class bankAccount:

    #constructer
    def __init__(self):

        self.accountNumber = "123-456-7890"
        self.balance = 5000000
        self.patronName = "Kristina Keenan"
        self.interestRate = .05
        self.cardNumber = "098-765-4321"

    def viewBalance(self):
        print("Your balance is",self.balance,"dollars.")

    def withdrawMoney(self):
        withdrawlAmount = int(input("How much money do you want to withdraw?"))
        print("You are withdrawing", withdrawlAmount,"dollars.")
        self.balance = self.balance - withdrawlAmount
        print("Your balance is now",self.balance,"dollars.")

    def depositMoney(self):
        depositAmount = int(input("How much money do you want to deposit?"))
        print("You are depositing", depositAmount,"dollars.")
        self.balance = self.balance + depositAmount
        print("Your balance is now",self.balance,"dollars.")

    def transferMoney(self):
        transferNumber = input("Enter the account number you are transferring to:")
        transferAmount = int(input("How much money are you transferring?"))
        print("You are transferring",transferAmount,"dollars to account number",transferNumber)
        self.balance = self.balance - transferAmount
        print("Your balance is now",self.balance,"dollars.")



def main():
    doAction = bankAccount()
    
    actionWord = input("What do you want to do today? View Balance, Withdraw, Deposit, or Transfer?")

    
    if actionWord == "View Balance" or actionWord =="view balance" or actionWord == "View balance" or actionWord == "view Balance":
        doAction.viewBalance()
    
    if actionWord == "Withdraw" or actionWord == "withdraw":
        doAction.withdrawMoney()
    if actionWord == "Deposit" or actionWord == "deposit":
        doAction.depositMoney()
    if actionWord == "Transfer" or actionWord == "transfer":
        doAction.transferMoney()

    yesOrNo = input("Is that everything you needed to do? Yes or No?")

    if yesOrNo == "no" or yesOrNo == "No":
        main()



main()
