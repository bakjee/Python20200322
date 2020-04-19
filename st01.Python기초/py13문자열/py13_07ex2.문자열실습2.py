# 문자열에서 가장 큰 수를 찾으시오.
# ※ 프로그램의 시작점은 main() 메서드가 되도록 만든다.
# ※ 프로그램을 최대한 작은 조각으로 분리하여 작성한다.
#
# 문자열로 본다면 가장 큰 수는 9883 이지만
# 정수로 본다면 가장 큰 수는 73646 이다.
#
# a. 문자열 자르기 --> 리스트를 얻게 됨.
# b. 문자열을 정수 리스트로 만든다.
# c. 정수리스트를 오름차순 정렬하시오
# d. 정수리스트에서 최대값을 찾는다.
# temp3 = "74 874 9883 73 9 73646 774"


def conv_lst(list1):
    result = None
    print("문자열 가장 큰 수", max(list1))
    result = [int(i) for i in list1]
    return result


def sort_lst(list1):
    result = None
    result = list1.sort()
    print(max(list1))
    return result


def main():
    list1 = "74 874 9883 73 9 73646 774"
    list1 = list1.split(" ")
    list2 = conv_lst(list1)
    sort_lst(list2)


main()

#list1 = temp3.split(" ")
# print(max(list1))
#list1 =[int(i) for i in list1]
# list1.sort()
# print(max(list1))


# def main():
