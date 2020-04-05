num=int(input("숫자를 넣어주삼::::"))
print("Number:", num)
print("Result:")

eqn=0
r1=range(9,0,-1)
for i in r1:
    eqn=num*i
    print("%2s *%2s=" %(num,i),eqn,end=".")