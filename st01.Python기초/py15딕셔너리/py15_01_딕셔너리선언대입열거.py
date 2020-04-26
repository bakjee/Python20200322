
# 딕셔너리의 CRUD2S 사용법을 익힌다. 
# 딕셔너리에 담을 수 있는 것은? ==> 다
# 딕셔너리 선언 ==>  dic = { }
# 딕셔너리 추가(C) ==> dic["key값"] = "값" = <==없으면 만든다.
# 딕셔너리 읽기(R) ==> dic["key값"]
# 딕셔너리 수정(U) ==> dic["key값"] = "값" <==있으면 바꾼다.
# 딕셔너리 삭제(D) ==> dic.pop("key값")
# 딕셔너리 정렬(S) ==> 없음. 왜냐하면 순서가 없기 때문
# 딕셔너리 검색(S) ==> 반복문 
# 딕셔너리 길이    ==> len(dic.keys() ) , len(dic.values() ) ,


# 딕셔너리 선언하기

# 딕셔너리 전체 내용을 출력해봅니다.
dictionary = {}
dictionary = {
    "name": "망고",
    "type": "당",
    "ingredient": ["망고", "Sugar", "Salt", "치자"],
    "origin": "필리핀",
}
print(dictionary)
# R: 요소 추가 전에 내용을 출력해봅니다.


# 1. 선택 연산자를 사용하는 방법, name, type의 값을 출력
# 2. get() 메서드를 사용하는 방법 ingredient,origin 의 값을 출력

print(dictionary["name"])  # key=name 방의 값을 출력
print(dictionary["type"])  # key=type 방의 값을 출력
print(dictionary.get("ingredient"))  # key=name 방의 값을 출력
print(dictionary.get("origin"))  # key=name 방의 값을 출력


# C: 딕셔너리 추가
# dictionary의 key 에 head와 body 를 추가하고 값을 출력하시오
dictionary["head"] = "body"
print(dictionary)
print(dictionary["head"])
print(dictionary.get("head"))

# U: 딕셔너리 수정
# name 값을 "8D 망고" 로 수정하시오.
print(dictionary["name"])
dictionary["name"] = "8D Mango"
print(dictionary["name"])


# D: 딕셔너리 삭제.
# 1. 연산자 방식 ==> del . 비추천
# 2. 메서드 방식 ==> .pop("key"). 추천
# name, type 키를 삭제
print("삭제 전", dictionary)
dictionary.pop("name")  # 방이름 : name을 삭제
dictionary.pop("type")  # 방이름 : type을 삭제
print("삭제 후", dictionary)

# S: 정렬. 딕셔너리는 정렬하는 방법이 없다.
# => 왜냐하면 순서(방번호)가 없기 때문에.
# 단, key 값만 정렬하는 것은 가능하다. 왜냐하면 key 값들만 있으면 리스트로
# 처리 가능 하기 때문에. value 값만 정렬하는 것은 가능하다.


# S: 검색. 특별하는 방법이 없다.
# 선택연산자를 사용하면 바로 검색 되기 때문 dictionary["name"]


# 존재하지 않는 키: 선택 연산자로 없는 키에 접근하면 에러 발생.
# try ~ except 를 추가하시오.
# KeyError
try:
    name = dictionary["name"]  # "사전"에는 name 키값이 없어서 에러가 난다.
except KeyError as ex:
    print("Exception", ex)
except Exception as ex:
    print("key error", ex, "does not exist")
name = dictionary.get("name")
print("name", name)


# 존재하지 않는 키에 접근하면 에러 발생. try ~ except 를 추가하시오.
# 딕셔너리에서 키의 존재 여부 확인.
# 방법1. get() 메서드 사용하는 방법
#       get() 메서드 키가 존재하지 않는 경우에  None을 반환한다.
# 방법2. in 연산자를 사용하는 방법

# 방법1. get() 메서드 사용하는 방법
#       vaule 값이 None 이면 키가 없다는 의미다.
name = dictionary.get("name")
print("name", name)
# 방법2. in 연산자를 사용하는 방법

if "name" in dictionary:
    print("Key exists")
    # No "name" exists in "Dictionary" therefore = Error
    name = dictionary["name"]
else:
    print("Key does not exist")
    name = None

print("name", name)

###################
# 딕셔너리 열거
# key 만 열거. keys() 메서드 사용.
# value 만 열거. values() 메서드 사용.
# key 와 value를 쌍으로 열거. items() 메서드 사용.
##################
for i in dictionary:
    print(i)  # i는 키값(방이름)이다.
    print(type(i))  # class<str>
    print(i, dictionary[i]) #i는 


# key 만 열거. keys() 메서드 사용.
for i in dictionary.keys():
    print(i)
# value 만 열거. values() 메서드 사용.
for i in dictionary.values():
    print(i)
# key, value를 쌍으로 열거. items() 메서드 사용.
for i in dictionary.items():
    print("items()>>",i) #i는 튜플(읽기 전용 리스트 ) 이다.
    print("items()>>",i[0],i[1]) #i는 튜플(읽기 전용 리스트 ) 이다.



#####################
# dictionary sorting
# sorting keys only . keys() method

keys = list(dictionary.keys())

print("keys 정렬 전",keys)
keys.sort()
print("keys 정렬 후", keys)

#sorting values only. values() method.

# values= list(dictionary.values())
# print("values 정렬전," values)
# values.sort() #Error is normal since not all values have the same "type()
# print("values 정렬후," values)

