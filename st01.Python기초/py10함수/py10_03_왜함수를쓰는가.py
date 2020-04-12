
# 1부터 10까지의 합계를 구하고
# 그 합계를 sum에 저장하고 sum 값을 한번만 출력한다.
sum1=0 #합계를 구할 때는 0으로 초기화, 곱하기 할 때는 1로 초기화
for i in range(0,11,1):
    sum1=sum1+i
print1="Summation of %s to %s equals to: %s" %(1,10,sum1)
print(print1)
# 1부터 100까지의 합계를 구하고
# 그 합계를 sum2 에 저장하고 sum2 값을 한번만 출력한다

sum2=0 #합계를 구할 때는 0으로 초기화, 곱하기 할 때는 1로 초기화
for i in range(0,101,1):
    sum2=sum2+i
print1="Summation of %s~%s equals to: %s" %(1,100,sum2)
print(print1)


# 100부터 sum2까지의 합계를 구하고
# 그 합계를 sum3 에 저장하고 sum3 값을 한번만 출력한다.
sum3=0 #합계를 구할 때는 0으로 초기화, 곱하기 할 때는 1로 초기화
for i in range(0,sum2+1,1):
    sum3=sum2+i
print1="Summation of %s~%s equals to: %s" %(100,sum2,sum3)
print(print1)


# 반복 코드는 함수를 만들어 사용한다
# get_sum() 함수 만들기
# 함수에서 바뀌는 값은 입력으로 처리한다. 
# 매개 변수는 함수에서 입력으로 사용되는 변수다. x, y

def get_sum(num1,num2):
    sum1=0 #합계를 구할 때는 0으로 초기화, 곱하기 할 때는 1로 초기화
    for i in range(num1,num2+1,1):
        sum1=sum1+i
    print1="Summation of %s~%s equals to: %s" %(num1,num2,sum1)
    print(print1)

    return sum1



##################################
# 함수 호출 == 함수 사용.
# 1부터 10까지의 합계를 구하고 출력
# 1부터 100까지의 합계를 구하고 출력
# 100부터 sum2까지의 합계를 구하고 출력
get_sum(1,10)

sum22=get_sum(1,100)

get_sum(100,sum22)
#합계의 시작값과 종료값을 키도브드로 부터 입력 받고 합계를 출력하시오.
#시작값이 종료값보다 큰 경우에도 합계를 구하여 출력하게 하시오.


start=int(input("Type in your start number:"))
end=int(input("Type in your end number:"))

if start>end:
    conv=start
    start=end
    end=conv
else:
    pass

get_sum(start,end)