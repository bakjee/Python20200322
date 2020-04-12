# 사용자 함수 만들기
# 정수를 입력받아서 제곱한 값을 반환하는 square() 함수를 만들어보자.


def square(x,p):
    result = None
    #가정1  n이 문자열이면 에러발생. 어떻게 처리할까?
    try:
        result = x**p 
    except Exception as ex:
        pass #로그에 출력하도록 변경
    
    
    return result




value=square(10,2) #Value = None if there is no return statement within a function, if the function does have a return statement, whatever the variable will be returend.
print(value)


