no1 = int(input("1번째 숫자를 입력 하시오...:"))
no2 = int(input("2번째 숫자를 입력 하시오...:"))
no3 = int(input("3번째 숫자를 입력 하시오...:"))

if no1 > no2 and no1 > no3:
    print(no1)

elif no2 > no1 and no2 > no3:
    print(no2)

else:
    print(no3)
