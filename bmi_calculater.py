weigth = float(input("enter weight: "))
height  = float(input("enter height : "))
if height <= 0 :
    print("invalid height. ")
else:
    bmi= weigth/(height*height)
    if bmi<18.5:
        print("underweight",bmi)
    elif 18.5<bmi<25:
        print("normal",bmi)
    elif 25<bmi<30:
        print("overweighht",bmi)
    else:
        print("obese")