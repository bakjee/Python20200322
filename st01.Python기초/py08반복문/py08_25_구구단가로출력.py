
# 2단부터 19단까지 1씩 증가시키면서
# 1부터 9까지 1씩 증기시키면서
# 구구단을 출력하시오.
# 2*1= 2 2*2= 4 2*3= 6 ....
# 3*1= 3 3*2= 6 3*3= 9 ....
# 중첩 for문
for i in range(2, 20, 1):
    for j in range(1, 10, 1):
        str1 = "%2s*%s=%3s" % (i, j, i*j)
        if i == 19 and j == 9:
            print("%2s*%s=%3s" % (i, j, i*j), end=".")
        else:
            print(str1, end=",")
    print()
