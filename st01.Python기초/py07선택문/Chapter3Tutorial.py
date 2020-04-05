pocket = ["paper", "cellphone"]
card = True

if 'money' in pocket:
    print("택시 타고 가라")
elif card:
    print("택시 타고 가라")

else:
    print("걷자잉")

print()
print()
print()
print("--------------------------------------------------------------------------------------")

treeHit = 0
while treeHit < 10:
    treeHit = treeHit+1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("the tree has fallen")
print()
print()
print()
print("--------------------------------------------------------------------------------------")
# coffee.py
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니당.")
    coffee = coffee-1
    print("남은 커피는 %d 잔 입니다." % coffee)
    if coffee==0:
        print("커피 없음요. 커피 판매중지요")
        break
