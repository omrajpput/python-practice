balance = 5000
total_expence = 0
transactions = 0
while True:
    print("check balance press 1 ")
    print("for deposit press 2 ")
    print("for withdraw press 3 ")
    print("for calculate daily expensis press 4")
    print("for exit press 5")
    n = int(input("enter no (1,2,3,4): "))
    if n == 1 :
        print(f"your balance is {balance}")
    elif n==2:
        amount = int(input("enter deposit amount: "))
        if amount <= 0:
            print("please enter valid amount")
            
        else:
            balance = balance + amount
            transactions+=1
            print (f"you depsite .{amount} and your current balance is {balance} ")
            
    elif n == 3:
        withdraw = int(input("enter you amount: "))
        if balance< withdraw :
            print ("balance is too low for this transaction:")
        elif withdraw <= 0: 
            print("invalid amount")

        else:
            balance= balance - withdraw
            transactions+=1
            print(f"your currrent balance is {balance}")
    elif n == 4:
        while True:
            reason = input("reason for expense :  ")
            expense = int (input("enter amount: "))
            if expense <=0:
                print ("invalid expense ")
            elif expense<=balance:
                total_expence+=expense 
                balance = balance - expense
                transactions+=1 
                print(f"your new balance is{balance}and today expenses is {total_expence} ")
            else:
                print("expense  is not vaild")
            leave = int (input("if you want to exit from daily expenses press 1:"))
            if leave==1:
                break
            else :
                continue
        saving = balance 
        print(f"saving is {balance} ")
    elif n == 5:
        print (f"balance : {balance} ")
        print(f"today expences: {total_expence}")
        print(f"transactions : {transactions}")
        print("thanks")
        break
    else :
        print("please enter valid chocie: ")    

    

