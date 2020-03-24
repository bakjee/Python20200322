myMoney = 5000
candyPrice = 120
# 최대한 살 수 있는 사탕 수

maxCandies = myMoney // candyPrice
print(maxCandies, " 개")

# 최대한 사탕을 구입하고 남은 돈

change= myMoney % candyPrice
print(change, " 원")
