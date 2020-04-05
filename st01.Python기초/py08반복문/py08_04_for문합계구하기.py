
###########################
# 0부터 9까지의 합계를 구하시오
sum = 0

for i in range(0, 10, 1):
    sum = sum+i
print(sum)
###########################
# 문제. 0부터 100까지 짝수의 합계를 구하시오

sum = 0

for i in range(0, 101, 1):
    if i%2==0:
        sum = sum+i
    else:
        pass
print(sum)