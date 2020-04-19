def swap(value):
    #a==>value[0]
    #b==>value[1]
    temp=value[1]
    value[1]=value[0]
    value[0]=temp
    print("swap 안: a=", value[0],", b=",value[1])

#변수의 선언과 초기화
def main():
    #리스트 만들기
    value=[5,3]


    print( "swap 전: a=",value[0],", b=",value[1])
    swap(value)
    print("swap 후: a=",value[0],", b=",value[1])

main()

