class BankAccount:
    def __init__(self,accountNumber,name):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = 0
        self.currentTransaction = 1
        self.transactionHistory = {self.currentTransaction:"Account Created"}
    
    def deposit(self,depositAmount):
        self.balance = self.balance + depositAmount
        self.currentTransaction = self.currentTransaction + 1
        self.transactionHistory[self.currentTransaction] = "Deposit of $" + str(depositAmount)

    def withdraw(self,withdrawAmount):
        self.balance = self.balance - withdrawAmount
        self.currentTransaction = self.currentTransaction + 1
        self.transactionHistory[self.currentTransaction] = "Withdrawl of $" + str(withdrawAmount)

    def printDetails(self):
        print("Account Details for account #",self.accountNumber,":",sep="")
        print("Name:",self.name)
        print("Balance: $",self.balance,sep="",end="\n")
        #print(self.transactionHistory)
        for k in self.transactionHistory:
            print(k,"=>",self.transactionHistory[k])
        print()



def main():
    account1 = BankAccount(12345,"Kristina Keenan")
    account1.deposit(100)
    account1.printDetails()
    
    account2 = BankAccount(67890, "Liz Lavin")
    account2.deposit(200)
    account2.withdraw(50)
    account2.printDetails()

    

main()
