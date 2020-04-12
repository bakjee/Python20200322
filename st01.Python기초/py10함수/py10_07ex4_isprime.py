# 사용자 함수 만들기
# 양의 정수가 소수가 되려면 1과 자신만을 약수로 가져야 한다. 예를 들어서 17은 1과 17만이 약수이므로 소수이다.
# 소수를 판별하는 함수 isprime()을 작성하여 사용하여 보자.
# 사용자로 부터 정수를 입력 받아서 변수 n에 저장한다.
# i를 2부터 n까지 1씩 증가시키면서
#     n을 I 로 나누어 나머지가 0인지 본다.
#     나머지가 0이면 약수가 있는 것이므로  소수가 아니다.


##순서##
# isprime 함수 정의
# main 함수 정의
# main 함수 정의
def isprime(n):
    result = True
    try:
        for i in range(2, n, 1):
            if n % i == 0:  # 소수가 아니다
                result = False
                break  # 약수가 있으면 더 이상 반복할 필요가 없다, 탈출
    except Exception as ex:
        pass
    return result


def main():
    num1 = int(input("number?"))
    value = isprime(num1)
    
    print(value)

    try:
        정수 = int(input("두번째?"))
        value = isprime(정수)
    except Exception as ex:
        pass
    
    print(value)

main()

# 반복이 정상적으로 종료되고 나머지가 0인 수가 없다면 소수이다.
#
# 도전. 위의 코드를 이용하여 1부터 100 사이의 모든 소수를 찾는 코드를 작성하시오.


# 왜 main() 함수를 만들어 사용하는가?
# 프로그래밍에서 지향하는 방식은 전역변수를 사용하지 않는다

# main 함수 호출
