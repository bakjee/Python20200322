# 현대인들은 축약어를 많이 사용한다.  예를 들어서 "B4(Before)" "TX(Thanks)"
# "BBL(Be Back Later)" "BCNU(Be Seeing You)" "HAND(Have A Nice Day)"와
# 같은 축약어들이 있다. 축약어를 풀어서 일반적인 문장으로 변환하는
# 프로그램을 작성하여 보자.
#
# 실행 예시)
# 번역할 문장을 입력하시오: TX Mr. Park!
# Thanks Mr.Park!

# 작업 순서
# 0. table 사전 만들기
# 1. 문자열 입력 받기
# 2. 문자열을 split() 해서 array 리스트로 만든다.
# 3. 반복문을 사용하여 array 리스트를 루프를 돌면서
#    딕셔너리 table에서 찾는다.
#     ==> table에서 찾을 때는 get()메서드나 in 연산자를 사용한다
# 3-1 table에서 찾고 있으면 바꾼다. replace()
#     찾을 때는 get()메서드나 in 연산자를 사용한다
#     arry[0] = Tx    일때 table에서 찾으려면( get(), in )
#     arry[1] = Mr.   일때 table에서 찾으려면( get(), in )
#     arry[2] = Park! 일때 table에서 찾으려면( get(), in )
# 4. 찾기 끝나면 출력한다.

# 함수정의


def main():
    # 0. table 사전 만들기
    table = {
        "B4": "Before",
        "TX": "Thanks",
        "BBL": "Be Back Later",
        "BCNU": "Be Seeing You",
        "HAND": "Have a Nice Day"
    }

    # 1. 문자열 입력 받기
    문자열 = input("번역할 문장을 입력하시오:")

    # 2.변환 작업
    array = 문자열.split(" ")  # 공백 으로 자르기
    print(array)  # [TX, Mr. Park!]

    # 3. 반복문을 사용하여 array 리스트를 루플를 돌면서 table 딕셔너리에서 찾아본다
    result = ""
    for i in array:
        # array[0]=TX
        # array[1]=Mr.
        # array[2]=Park!
        value = table.get(i)  # i==array[0]== ==> value=TX=>Thanks
        if value == None:
            result = result+i+" "
        else:  # if can be found on the table
            result = result+value+" "

    # 변환이 끝나면 출력한다.
    print(result)


main()
