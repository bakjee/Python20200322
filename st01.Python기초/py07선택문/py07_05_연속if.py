# py04_02_ifelse

# 하나의 점수를 입력 받고, 입력 받은 점수에 해당하는 학점을 출력하는 프로그램을 작성하시오.
score = int(input("점수는요: "))

if 101 > score >= 90:
    print("학점:A")

elif 90 > score >= 80:
    print("학점:B")

elif 80 > score >= 70:
    print("학점:C")

elif 70 > score >= 60:
    print("학점:D")

else:
    print("학점:F")

# 입력 받는 정수는 0~100까지이고
# 90점 이상이고 이하이면 A,


# 80점 이상이면 B,
# 70점 이상이면 C,
# 60점 이상이면 D,
# 나머지는 F

############################
# 비교 연산자와 논리 연산자 결합한 방법
grade = int(input("grade :")) #95
level="F"
if 90<= grade and grade <=100:
    print("A")
    level = "A"
elif 80<= grade and grade <90:
    print("B")
    level = "B"
elif 70<= grade and grade <80:
    print("C")
    level = "C"
elif 70<= grade and grade <60:
    print("D")
    level = "D"
else:
    level = "F"

print("학점: ", level)
############################
# 비교 연산자만 사용한 방법
grade = int(input("grade :")) #95
level="F"
if 90<= grade:
    print("A")
    level = "A"
elif 80<= grade:
    print("B")
    level = "B"
elif 70<= grade:
    print("C")
    level = "C"
elif 70<= grade:
    print("D")
    level = "D"
else:
    level = "F"

print("학점: ", level)


#######################
#도전과제
print()
print()
print("----------------------------------------------")
print("도전과제")
#grade 는 0부터 100사이의 값만 가능해야 한다.
#그 이ㅚ의 값이 오면  grade를 다시 입력 받게 작성하시오
grade = int(input("grade :"))

while grade<0 or grade>100 :
    grade=int(input("grade :"))

    if 0<= grade <=100:
        #반복문을 종료
        break
    else:
        #다시 입력 받는다
        pass

    level="F"
if 90<= grade:
    print("A")
    level = "A"
elif 80<= grade:
    print("B")
    level = "B"
elif 70<= grade:
    print("C")
    level = "C"
elif 70<= grade:
    print("D")
    level = "D"
else:
    level = "F"

print("학점: ", level)
