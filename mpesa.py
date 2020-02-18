balance = 0
def menu ():
    global balance 
    print("CHOOSE OPTION\n 1.Send Money\n 2.Withdraw Cash\n 3.Deposit\n 4.Lipa na Mpesa\n 5.Exit ")
    opt = input("Enter option: ")

    if opt=="1":
        Send_Money()
    elif opt=="2":
        Withdraw_cash()
    elif opt=="3":
        Deposit()
    elif opt=="4":
        Lipa_na_Mpesa()
    else:
        exit()

def Send_Money():
    global balance
    phone=input("Enter Phone number: ")
    amount = input("Enter amount: ")
    pin = input("Enter pin: ")
    amount = int(amount)
    if pin=="8776":
        if amount<=balance:
            balance = balance-amount
            print("Transaction Successful, Balance is ",balance)
            menu()
        else:
            print("Not enough Funds\n Balance is ",balance)
            menu()
    else:
        print("Wrong pin")
        menu()

def Withdraw_cash():
    global balance
    agent=input("Enter Agent number: ")
    amount = input("Enter amount: ")
    pin = input("Enter pin: ")
    amount = int(amount)
    if pin=="8776":
        if balance>=amount:
            balance = balance-amount
            print("Withdrawal Successful, Balance is ",balance)
            menu()
        else:
            print("Not enough Funds\n Balance is ",balance)
            menu()
    else:
        print("Wrong pin")
        menu()

def Deposit():
    global balance
    amount = input("Enter amount: ")
    pin = input("Enter pin: ")
    amount = int(amount)
    if pin=="8776":
        balance = balance+amount                 
        print("Successful \n Balance is ",balance)
        menu()
    else:
            print("Wrong pin")
            menu()

def Lipa_na_Mpesa():
    global balance
    till=input("Enter till number: ")
    amount = input("Enter amount: ")
    pin = input("Enter pin: ")
    amount = int(amount)
    if pin=="8776":
        if balance>=amount:
            balance = balance-amount
            print("Transaction Successful, Balance is ",balance)
            menu()
        else:
            print("Not enough Funds\n Balance is ",balance)
            menu()
    else:
        print("Wrong pin")
        menu()

menu()
