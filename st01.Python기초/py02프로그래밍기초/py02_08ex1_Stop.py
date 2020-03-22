# 디버깅을 이용하여 반복 되는 과정을 이해한다.
# F5 / F10 단축 버튼을 사용하시오.
# 주의사항!!! 줄 맞춤
print("\033c")
sign = "stop"



while sign == "stop":
    sign = input("현재 신호를 입력하시요:")
    print("입력값>>>", sign)

print("OK! 진행합니다.")
