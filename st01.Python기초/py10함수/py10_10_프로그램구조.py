# 데이터 수집
# readList 반환값은 리스트라고 가정한다


def readList():
    result = None
    # 코드 작성
    # 1. 무한 루프 만들고
    # 2. 키보드 입력 받고
    # 3. 입력 값이 음수 이면 루프 탈출 아니면 리스트에 저장하고 반복한다
    result = []  # 리스트츠 생성
    while True:
        입력값 = int(input("정수를 입력하세요 : "))

        if 입력값 < 0:
            break
        else:
            # 리스트에 저장
            result.append(입력값)

    return result

# 데이터 처리
# nlist:리스트다


def processList(nlist):
    result = None
    result = sorted(nlist)
    return result
# 데이터 출력


def printList(nlist):
    result = None
    for i in nlist:
        str = "성적 : %s " % i
        print(str)
    return result

# 프로그램 시작


def main():
    result = None
    # main 함수의 처리 순서
    # 1. 데이터 수집 ==> readList() 함수 사용
    # 2. 데이터 처리==> processList() 함수 사용
    # 3. 데이터 출력==> printList() 함수 사용

    result = readList()
    result = processList(result)
    result = printList(result)

    return result

  
# 이 모듈이 단독으로 사용되면 main()를 호출하라.
main()

