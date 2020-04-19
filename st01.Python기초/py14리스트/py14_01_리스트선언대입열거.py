
############################
# 리스트의 CRUD3S
# C: create.
# R: read
# U: update
# D: delete
# S: search
# S: sort
# S: shuffle
############################


############################
# 리스트 선언
# 리스트에는 다 담을 수 있다. 함수도 담을 수 있다.
############################
def func():
    print("합수")


array = []

array = list()
array = [None, 1, 1.1, "문자열", True, False, [], {}, func]
array[-1]()

############################
# 문자 H, e, l, l, o를 요소로 가지는 리스트
# 문자열 Hello를 요소로 가지는 리스트
# 문자열을 리스트로 변환. 문자 H, e, l, l, o를 요소로 가지는 리스트 생성
# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
############################
list1=["H","e","l","l","o"]
print(list1, type(list1))
list2=list("Hello")
print(list2, type(list2))
list3=["hello"]
print(list3, type(list3))
list4=[0,1,2.3,4]
print(list4, type(list4))
list5=list(range(0,5,1))
print(list5, type(list5))

############################
# 리스트 요소 출력
# 리스트의 시작은 0번부터다.
# 리스트  Read : [] 선택 연산자를 사용한다.
############################
array = [None, 1, 1.1, "문자열", True, [1,2,3], {"a":1}, func]
print(array[0], type(array[0])) #None, <class 'None'>
print(array[1], type(array[1])) #1, <class 'Int'>
print(array[2], type(array[2])) #1.1, <class 'Float'>
print(array[3], type(array[3])) #"문자열", <class 'Str'>
print(array[4], type(array[4])) #True, <class 'Bool'>
print(array[5], type(array[5])) #[1,2,3], <class 'List'>
print(array[6], type(array[6])) #{a:1}, <class 'dict'>
print(array[7], type(array[7])) #<function func at 0x00E2D>, <class 'Func'>





############################
# 리스트 전체 출력
############################
print(array)
############################
# 리스트 슬라이싱 :
# 1. 선택 연산자 사용하는 방법.
############################
array[0]="변경"

print(array[0], type(array[0])) #"변경", <class 'str'>
print(array)

############################
# 리스트 요소 대입
# 리스트의 0번 값을 문자열 "변경"값으로 바꾸시오.
############################


############################
# 리스트 요소 추가: C. create
#  추가 : 리스트의 마지막에 넣는다. --> .append() 메서드 사용
#  삽입 : 리스트의 중간에 넣는다.   --> .insert() 메서드 사용
############################
array = [None, 1, 1.1, "문자열", True, [1,2,3], {"a":1}, func]
print(array)
array.append("추가")
array.insert(0,"삽입") #["삽입",None, 1, 1.1, "문자열", True, [1,2,3], {"a":1}, func]
print(array)
############################
# 리스트 요소 삭제: D. deletef
#  메서드 방식 --> pop() 메서드 . 추천
#  연산자 방식 --> del. 비추천
############################
array=[None, 1, 1.1, "문자열", True, [1,2,3], {"a":1}, func]
array.pop(0) #[1, 1.1, "문자열", True, [1,2,3], {"a":1}, func]

############################
# 리스트 검색
############################
array=[ "A","a","b","B","A","a","b","B"]
pos=array.index("a")
slist=[]
for i in range(0,len(array),1):
    pos=array.index("a",i)
    if pos>=0:
        slist.append(pos)
        i=pos+1
print(slist) #[1,5]


#리스트 열거

array = [ "A","a","b","B","A","a","b","B"]
for i in array:
    print(i,end=" ,")
print()


############################
# 리스트에 담을 수 있는 것은? ==> 다
# 리스트 선언 ==> [] , list()
# 리스트 추가(C) ==> .append(), .insert()
# 리스트 읽기(R) ==> [방번호]
# 리스트 수정(U) ==> [방번호] = 값
# 리스트 삭제(D) ==> .pop()
# 리스트 정렬(S) ==> sorted()
# 리스트 정렬(S) ==> .find() + 반복문 , .rfind() + 반복문
# 리스트 길이    ==> len()
# 리스트 출력
# 리스트 열거
############################
