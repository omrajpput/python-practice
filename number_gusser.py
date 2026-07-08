number = 39 
won = False
attempt= 1
while attempt<=5:
    guess = int(input("enter no: "))
    if guess<number:
        print("low")
    elif guess>number:
        print("high")
    elif guess==number:
        print("you won")
        won = True
        break
    attempt+=1
if won== False :

    print(f"nice try bitch game over , the number is {number}")
else :
    print("congratulations mf")