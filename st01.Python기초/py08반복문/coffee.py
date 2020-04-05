# coffee2.py
coffee = 10
while True:
    money = int(input("돈을 넣어주세용:"))
    if money == 300:
        print("커피를줍니다!!!")
        coffee = coffee-1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money-300))
        coffee = coffee-1
    else:
        print("돈을 다시 돌려주고 커피를 안줘용~")
        print("남은 커피의 양은 %d잔 입니당....!" % coffee)
    if coffee == 0:
        print("커피 없슈")

