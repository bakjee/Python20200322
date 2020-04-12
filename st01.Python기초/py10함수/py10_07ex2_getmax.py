# 사용자 함수 만들기
# 두 개의 정수가 주어지면 두수 중에서 더 큰 수를 찾아서 이것을 반환하는 함수를 만들어보자.

# 함수 정의
# get_max:함수이름
# x : 매개변수
# y : 매개변수


def get_max(x, y):
    result = None
    try:
        if (x > y):
            result = x
        else:
            result = y
    except Exception as ex:
        pass
    return result

# 왜 main() 함수를 만들어 사용하는가?
# 프로그래밍에서 지향하는 방식은 전역변수를 사용하지 않는다

# main 함수 호출


def main():
    num1 = newmethod696("num1")
    num2 = newmethod696("num2")
    value = get_max(num1, num2)
    if (value == None):
        print("error")

    else:
        print(value)


def newmethod696(str):
    try:
        num1 = input(str+" number?")
        num1 = int(num1)
    except Exception as ex:
        pass
    return num1


main()
