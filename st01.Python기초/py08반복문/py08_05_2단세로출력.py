# 2단의 구구단을 출력하는 프로그램을 만드시오
# 1부터 9까지 2단의 구구단을 출력하시오.
# range()함수를 사용한다.
sum = 0
r1 = range(1, 10, 1)

for i in r1:
    sum = i*2
    print(" 2 *%2s =" % i, sum)
