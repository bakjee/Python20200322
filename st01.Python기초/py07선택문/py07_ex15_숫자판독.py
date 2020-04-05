# 문자열을 입력 받고 숫자인지 문자인지 판별하는 프로그램을 작성하시오.

ident = ["1"]  # input("끄적여보시오 : ")
for value in ident:
    print("value:", value)
    print("ascii:", ord(value))
    if 122 >= ord(value) >= 65:
        print("문자에유")
    elif 57 >= ord(value) >= 48:
        print("숫자에유")
    else:
        break
print()
print()
print("======================================================================================")

x = 5
y = 4
if x > 4 and y > 2:
    print(x*y)
else:
    print(x+y)
