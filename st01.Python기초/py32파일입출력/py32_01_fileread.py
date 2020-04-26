
# 파일 존재 여부 확인
# 현재 폴더에 phones.txt 파일이 존재하는지 확인한다.
# os.path.isfile() 메서는 있으면 True 없으면 False 를 반환한다.

import os #파일 처리 모듈

####################################
def getAbsFileName(fileName):
    result=""

    absfile=os.path.abspath(__file__)
    curDir=os.path.dirname(os.path.abspath(__file__))
    txtA=os.path.join("/",fileName)
    result=os.path.normpath(curDir+txtA) #==>절대 경로

    return result


#########################
# readline() 파일에서 한 줄씩 읽기
# 읽기 모드로 파일 열기, 이 때 encoding 을 지정한다.
fileName=getAbsFileName("/file/phones.txt")
pfr=open(fileName,"r",encoding="UTF-8")  #encoding 미지정시 ascii by default

####################################파일에서 한 줄씩 읽기: readline()
value=pfr.readline()
print(value,end="")
value=pfr.readline()
print(value,end="")
value=pfr.readline()
print(value,end="")
# 파일 닫기
pfr.close()

#########################
## 반복문으로 파일에서 읽어서 모니터에 출력하기 
# 읽기 모드로 파일 열기, 이 때 encoding 을 지정한다.
fileName=getAbsFileName("/file/phones.txt")
pfr=open(fileName,"r",encoding="UTF-8")  #encoding 미지정시 ascii by default


value=pfr.readline()
while value!="":
    print(value,end="")
    value=pfr.readline()
pfr.close()