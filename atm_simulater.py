balance = 25000000
print("welcome in our atm ")
while True:
    print("check balance press 1 ")
    print("for deposit press 2 ")
    print("for withdraw press 3 ")
    print("for exit press 4 ")
    n = int(input("enter no (1,2,3,4): "))
    if n == 1 :
        print(f"your balance is {balance}")
        
    elif n==2:
        amount = int(input("enter deposit amount: "))
        if amount <= 0:
            print("please enter valid amount")
            
        else:
            balance = balance + amount
            print (f"your current balance is {balance} ")
            
    elif n == 3:
        withdraw = int(input("enter you amount: "))
        if balance< withdraw or withdraw <= 0:
            print ("balance is too low for this transaction:")
            
        else:
            balance= balance - withdraw
            print(f"your currrent balance is {balance}")
            
    elif n == 4:
        print ("thanks for visiting our atm sir sayonara ")
        exit()
    else :
        print ("invald value plese enter right valve sir ")
    
            