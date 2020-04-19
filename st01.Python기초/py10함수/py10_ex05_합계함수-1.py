# 데이터 수집
# readList 반환값은 리스트라고 가정한다


def newmethod387():
    result = None
    반환값 = int(input("정수를 입력하세요 : "))
    return 반환값


def readList():
    result = None
    result = []

    반환값 = newmethod387()
    result.append(반환값)  # result[0]=1

    반환값 = newmethod387()
    result.append(반환값)  # result[1]=4

    return result



# 실행결과 예시
# 시작값:4
# 종료값:1
# 1부터 4까지의 합계는 10 입니다

# main 함수의 처리 순서
# 1. 데이터 수집
    # 1.1 입력 받고 정수 변환 후 리스트에 저장
    # 1.2 입력 받고 정수 변환 후 리스트에 저장
    # 1.3 리스트를 반환

# 2. 데이터 처리
    # 2.1 리스트 정렬
    # 2.2 합계 구하고 리스트에 합계값 추가==> 합계 구하는 함수 만들기
    # 여기서 반환되는 리스트는 아래와 같다
    # 0번방 값은 시작 값 ==> 예시 :1
    # 1번방 값은 종료  값==> 예시 4:
    # 2번방 값은 합계 값 ==> 예시:10
    # 반환되는 리스트는 아래와 같다
    # 0번방 값은 시작갑==> 예시:1
    # 1번방 값은 종료값==> 예시:4
    # 2번방 값은 합계값 ==> 예시:10
# 데이터 출력


# 데이터 처리
# nlist:리스트다


def processList(nlist):
    result = None
    result = sorted(nlist)
    return result  # 0번방값: 1, 1번방 값:4

# 데이터 합계:
# 매개변수:리스트다


def sumList(nlist):
    result = 0
    for i in nlist:
        result = result+i  # i의 의미는 : i번째 방의 값이다.
    return result  # 합계값

# 데이;터 출력


def printList(nlist):
    result = None
    result = "%s 부터 %s 까지의 합계는 %s 입니다" % (nlist[0], nlist[1], nlist[2])
    print(result)
    return result

# 프로그램 시작


def main():
    result = None
    # main 함수의 처리 순서
    # 1. 데이터 수집 ==> readList() 함수 사용
    # 2. 데이터 처리==> processList() 함수 사용
    # 3. 데이터 합계==>
    # 3. 데이터 출력==> printList() 함수 사용

    result = readList()
    result = processList(result)  # [시작값,종료값]
    # 합계값을 리스트, result에 추가 하시오
    합계값=sumList(result)
    result.append(합계값)  # [시작값, 종료값, 합계값]
    result = printList(result)

    return result


# 이 모듈이 단독으로 사용되면 main()를 호출하라.
main()
