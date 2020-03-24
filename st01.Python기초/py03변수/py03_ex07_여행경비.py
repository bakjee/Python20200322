# 미국으로 여행을 떠났다.
# 파이썬을 이용하여 총 소요 경비를 계산하는 프로그램을 작성하시오.
ExRate=1147
Adults=int(input("성인 x 명: "))
Kids=int(input("소아 x 명: "))
Infants=int(input("유아는 x명: "))
Group=Adults+Kids+Infants

Flight=953200*(Adults+Kids)+(953200*0.1*Infants)

AccomFee=125
AccomDays=int(input("호텔 예약은 x박: "))

Accom=AccomFee*AccomDays*ExRate

ResortsDays=int(input("리조트 사용 일 수는?: "))
ResortsFee=(45+(45*0.055))*ExRate

Resorts=ResortsFee*ResortsDays

ExIn=int(input("환전할 금액은? ($): "))

Exchange=ExIn*ExRate+ExRate*0.0045

Dinner=float(input("첫날 저녁 식대는? ($): "))
VAT=6.75/100
Tip=15/100

DinnerTotal=(Dinner+(Dinner*(VAT+Tip)))*ExRate

import math
PTime=int(input("주차시간은?(분): "))
parking15=math.ceil(((PTime-30)/15))

Parking=(2.5+(1.25*parking15))*ExRate

Total=Parking+DinnerTotal+Exchange+Resorts+Accom+Flight
print()
print()
print()

print("비행기 값: ", Flight/10000, "만 원")
print("숙박비 값: ", Accom/10000, "만 원")
print("리조트 값: ", Resorts/10000, "만 원")
print("환전 값: ", Exchange/10000, "만 원")
print("첫날 저녁 식대", DinnerTotal/10000, "만 원")
print("주차비 : ", Parking/10000, "만 원")
print("======================================================================================")
print("총 여행비는:", Total/10000, " 만원 입니다.")
print()
print("--------------------------------------------------------------------------------------")