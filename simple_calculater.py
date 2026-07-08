number_1 = float(input("enter no : "))
number_2 = float(input("enter no : "))
operator = input("enter operator(+-*/) : ")
if(operator == "+"):
    add = number_1 + number_2
    print(add)
elif(operator== "-"):
    sub = number_1-number_2
    print(sub)
elif(operator== "*"):
    multiply = number_1*number_2
    print(multiply)
elif(operator== "/"):
    if (number_2==0):
        print("invalid division")
    else:
        division = number_1/number_2
        print(division)    
    
else:
    print("invalid operator")