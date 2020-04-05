# 중첩 for문
x=int(input("시작값: "))
y=int(input("종료값: "))

if x>y:
    for i in range(y,x+1,1):
        for j in range(1,10,1):
            str1="%2s*%s=%3s" % (i, j, i*j)
            print(str1, end=",")
else:
    for i in range(x,y+1,1):
        for j in range(1,10,1):
            str1="%2s*%s=%3s" % (i, j, i*j)
            print(str1, end=",")