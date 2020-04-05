# 중첩 for문
for i in range(2, 20, 1):
    for j in range(1, 10, 1):
        str1 = "%2s*%s=%3s" % (i, j, i*j)
        if i == 19 and j == 9:
            print("%2s*%s=%3s" % (i, j, i*j), end=".")
        else:
            print(str1, end=",")
    print()
