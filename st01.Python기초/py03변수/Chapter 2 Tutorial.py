b = True
c = "a"
i = 7
d = 0.05

print(b)
print(type(b))
print()
# Class=bool=>불,불리언 (참 또는 거짓)
print(c)
print(type(c))
print()
# Class=String=>문자열 (문자,단어 등으로 구성된 문자들의 집합 " ")
print(i)
print(type(i))
print()
# Class=Integer=>정수 (1,2,3 +,-이 포함된 정수)
print(d)
print(type(d))
# Class=Floating-point=>소수점이 포함된 숫자
# print("----------------------------------------------------------------------------------------")
##number = input("먹은 사과의 개수는?")
##day = input("아펐던 일수는?")
# print(type(number))
# print(type(day))
##Statement = "I ate %s apples. so I was sick for %s days." % (number, day)

# print(Statement)

# print("----------------------------------------------------------------------------------------")

# Question 1

a = {'국어': '80', '영어': '75', '수학': '55'}
sum = int(a['국어'])+int(a['영어'])+int(a['수학'])  # 여기서 잘라내기로도 가능 할듯? 딕트내에 값은열은 무엇?
average = sum/3
print("철수의 평균 점수는:", average)
print()
print("----------------------------------------------------------------------------------------")
###############################
# Question 2
a = input("숫자를 넣으시오:")
b = int(a)
test = b % 2
result = [test]
if bool(result):
    print("Odd")
else:
    print("Even")
print()
print("----------------------------------------------------------------------------------------")
################################
# Question 3
# ID={'pin':[881120,1068234]}
# print("yyyymmdd",ID[2])

pin = "881120-1068234"
yyyymdd = [:6]
num = pin[7:]
print(yyyymmdd)
print(num)
