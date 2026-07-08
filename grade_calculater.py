english = int(input("enter engish mark: "))
math = int(input("enter math mark: "))
japnese = int(input("enter japanese mark: "))
python = int(input("enter python mark: "))
dsa = int(input("enter dsa mark: "))
total = english+math+japnese+python+dsa
maximum = 500
percentage = (total/maximum)*100
if english< 0 or english> 100 or math< 0 or math> 100 or japnese< 0 or japnese> 100 or python< 0 or python> 100 or dsa<0 or dsa>100:
    print("invalid marks")
elif english<=33 or math<=33 or japnese<=33 or python<=33 or dsa<=33 :
    print("fail")

elif percentage>=90:
    print("grade a+")
elif percentage>=75:
    print("grade a")
elif percentage>=60:
    print("grade b")
elif percentage>=40:
    print("grade c ")
else :
    print("fail")