
# 숫자가 아닌 것을 정수로 변환하려고 할 때

# 숫자가 아닌 것을 실수로 변환 할 때

# 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환하려고 할 때

# IndexError

#테스트 방법 
# 테스트1. abc 입력
#테스트2. 숫자 0 입력
#테스트3. 숫자 12.5 입력
try:
    입력값 =  input("숫자를 입력하세요: ")

    정수값 =  int(입력값) #입력값 "abc" 이면 에러 발생
 
    실수값 =  float(입력값) #입력값 "abc" 이면 에러 발생

    실수값 =  int("12.3") #입력값 "12.5" 이면 에러 발생

    나누기 = 10 /  정수값
except TypeError as ex:
    print( "TypeError" )
    pass
except Exception as ex:
    print(ex)
    pass

print("정상종료")


 
