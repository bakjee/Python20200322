# Variables of different types

# 기본형 타입
b= True  #불린
i= 1        #정수
f= 0.1      #실수
c= "c"      #문자
str = "Hello"     #문자열
n = None        #None "값이 없을"을 의미

# 변수 타입 확인

print("b",b, type(b))
print("i",i, type(i))
print("f",f, type(f))
print(c,c, type(c))
print("str",str, type(str))

# 복합형 타입
l=[0, 1, 2, 0, 3]                        #리스트 : 중복 가능 배열
d= {0: "zero," ,1: "one"}          #사전:
t= (0 , 1, 2)                             #튜플: 읽기 전용 배열
se1=set([1, 2 , 3, 1 ,2])           #세트: 중복 불가 배열
se2=set(["Hello"])                  #세트: 중복 불가 배열

# 변수 타입 확인

print("l",l, type(l))
print("d",d, type(d))
print("t",t, type(t))
print("se1",se1, type(se1))
print("se2",se2, type(se2))
