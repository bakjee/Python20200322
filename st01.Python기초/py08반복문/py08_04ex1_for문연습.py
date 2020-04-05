# 500과 1000사이에 있는 홀수의 합계

sum = 0

for i in range(500, 1000, 1):
    if i % 2 == 1:
        sum = sum+i
    else:
        pass
print("500과 1000사이에 있는 홀수의 합계 :", sum)

print()
print()
print("==============================")

# 0과 100사이에 있는 7의 배수 합계:735

sum = 0
for i in range(0, 101, 7):
    sum = sum+i
print("0과 100사이에 있는 7의 배수 합계:", sum)

print()
print()
print("==============================")
# 1에서 100까지의 합계

sum = 0
for i in range(0, 101, 1):
    sum = sum+i
print("0과 100까지의 합계:", sum)

print()
print()
print("==============================")

# 시작값,끝갑,증가값

x = int(input("시작값을 입력하세요:"))
y = int(input("끝값을 입력하세요:"))
z = int(input("증가값을 입력하세요:"))

sq1 = range(x, y, z)

sum = 0

for i in sq1:
    sum = sum+i
print("%d 에서 %d 까지 %d 씩 증가시킨 값의 합계:" % (x, y, z), sum)
