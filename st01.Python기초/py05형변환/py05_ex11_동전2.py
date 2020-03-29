# 자동 판매기를 시뮬레이션하는 프로그램을 작성하여 보자.
# 사용자는 1000원짜리 지폐와 500원짜리 동전, 100원짜리 동전을 사용할 수 있다.
# 물건값을 입력하고 1000원권, 500원짜리 동전, 100원짜리 동전의 개수를 입력하면
# 거스름돈을 계산하여서 동전으로 반환한다.

price = int(input("물건 값은...? : "))
Thousand = int(input("천 원권의 개수....?:"))
Fivehund = int(input("오백 원 동전의 개수....?:"))
Hund = int(input("백 원 동전의 개수....?:"))


Total=Thousand*1000 + Fivehund * 500 + Hund*100
print("입금액은 " , Total, "원 입니다...")
#거스름돈
change=Total-price
print("거스름돈은 " , change, "원 입니다...")
#거스름돈 오백원의 동전 반환 개수
change1000=change//1000
change=change%1000
#거스름돈 오백원의 동전 반환 개수
change500=change//500

#거스름돈에서 천원을 먼저 돌려줬다. 나은 거스름돈은 얼마인가
change=change%500 #150
#거스름돈 백원 동전 개수 구하기
change100=change//100 #백원의 개수 ==>1
#거스름돈에서 백단위까지 먼저 돌려줬다. 남은 거스름돈은 얼마인가?
change=change%100 #150 % 100 ==>50
#거스름돈 십원 동전 개수 구하기
change10=change//10
#남은 거스름돈은?
change=change%10
change1=change

print(change1000, "x 1000원 지폐")
print(change500, "x 500원 동전")
print(change100, "x 100원 동전")
print(change10, "x 10원 동전")
print(change1, "x 1원 동전")