# 0번째부터 12번째 자리까지 있음.
# prov 길이는 13이다.
prov = "A barking Dog"

#################################
# 문자열 연산자
#################################

# 문자열 결합 연산자 : +
# "A barking Dog never Bites!"를 출력하시오.
erb = " never bites!"
proverb = prov+erb

print(proverb)
# 문자열 반복 연산자 : *
proverb2 = proverb*3


# 문자열 일치 연산자 : ==

# s09 = "abcde"; s10 = "abcde" 일 때
# s09 과 s10 이 같으면 "same"을 아니면 "not same"을 출력하시오

s09 = "abcde"
s10 = "abcde"

if s09 == s10:
    print("same")

else:
    print("not same")


# 문자열 연산자를 사용하여 첫번째 b 문자를 출력하시오.
# prov = "A barking Dog"
# Where is the fisrt letter "b"
# 출력예시) "b"

print(prov[2])


# 문자열 연산자를 사용하여 2번부터 4번째자리까지 추출하여 출력하시오
# prov = "A barking Dog"
# 출력예시) "bar"
print(prov[2:5])

# 문자열 연산자를 사용하여 prov 에서 Dog 전까지만 출력하시오
# prov = "A barking Dog"
# 출력예시) "A barking "
print(prov[0:-3])

# 문자열 연산자를 사용하여 문자열 추출:
# prov = "A barking Dog"
# "A barking Dog"에서 마지막 g 빼고 "A barking Do" 만을 출력하시오.
print(prov[0:len(prov)-1])
