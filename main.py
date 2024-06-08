import pickle
import os
import pathlib

class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
    
    def createAccount(self):
        self.accNo= int(input("\tEnter The Account No : "))
        self.name = input("\tEnter The Account Holder Name : ")
        self.type = input("\tEnte The Type Of Account [current/saving] : ")
        self.deposit = int(input("\tDeposit Some Amount(min=500) : "))
        print("\n\n\tAccount Has Been Created")
    
    def showAccount(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type Of Account",self.type)
        print("Balance : ",self.deposit)
    
    def modifyAccount(self):
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify Type Of Account :")
        self.deposit = int(input("Modify Balance :"))
        
    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
    
    def report(self):
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)
    
    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")

    print("\t\t\t    Created By Vansh And It's Team:")
    print()
    print("\tPress Enter To Continue" ,end=" ")
    
    input()



def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        print("\tALL ACCOUNT HOLDER LIST ")
        print()
        print("\t Account No", "\t Account Holder Name", "\t\t Account Type", "\t Amount")
        for item in mylist:
            print("\t",item.accNo,"\t ", item.name, "\t\t\t ",item.type, "\t",item.deposit )
        infile.close()
    else :
        print("No Records To Display")
        

def displaySp(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("\tYour Account Balance Is : ",item.deposit)
                found = True
    else :
        print("No Records To Search")
    if not found :
        print("No Existing Record With This Number")

def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input("\tEnter The Amount To Deposit : "))
                    item.deposit += amount
                    print("\tYour Amount Has Been Deposit With", amount ,".Your Current Balance Is INR",item.deposit)
                    #print("\tYour account is updted")
                elif num2 == 2 :
                    amount = int(input("\tEnter The Amount To Withdraw : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                        print("\tYour Amount Has Been Withdraw With", amount ,".Your Current Balance Is INR",item.deposit)
                    else :
                        print("You Cannot Withdraw Larger Amount")
                
    else :
        print("No Records To Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

    
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()

        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
        print("\tThe Account Of",item.name , "Has Been Closed")
     
def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("\tEnter The New Name Of Account Holder  : ")
                item.type = input("\tEnter The New Type Of Account : ")
                # item.deposit = int(input("Enter the Amount : "))
        
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
   

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
        

ch=''
num=0
intro()

while ch != 8:
    
    print()
    print("\tMAIN MENU")
    print()
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    print()
    ch = input("\t")
    
    
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tEnter The Account No. : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter The Account No. : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter The Account No. : "))
        displaySp(num)
    elif ch == '5':
        displayAll()
    elif ch == '6':
        num =int(input("\tEnter The Account No. : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEnter The Account No. : "))
        modifyAccount(num)
    elif ch == '8':
        print("\tThanks For Using Bank Managemnt System")
        break
    else :
        print("Invalid Choice")
    print()
    ch = input("\tPress Enter To Continue -> ")
    


    
    
    
    
    
    
    
    
    
    
