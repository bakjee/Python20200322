# py02_09ex1_Salary

# 변수 선언 : salary , deposit 변수(메모리 공간) 선언

# 숫자를 입력받고(이것은 문자열) salary 변수 에 저장하시오(넣으시오).

# 10년치 월급의 총합을 구하고 그 값을 deposit 에 저장.

# 10년 동안의 저축액: ?????  원 형태로 출력하시오.

print("\033c")

Salary = input("월급의 액수를 입력하시오")

Salary = int(Salary)

Deposit = input("저축액의 %를 입력하시오")

Deposit = int(Deposit)/100

Savings = Salary*Deposit*12*10

print("10년간의 총 저축액은", Savings, "만원 입니다")
