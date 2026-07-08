unit = int(input("enter units: "))
if unit<0:
    print("invalid units")
elif unit<=100:
    bill = unit*5
elif unit<=200:
    bill = 100*5+(unit-100)*7
else:
    bill = 100*5+100*7+(unit-200)*10
print(bill)