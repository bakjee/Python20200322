#################################
# os 모듈의 사용법을 익힌다.
#
# os.path.isfile() 메서드는 있으면 True 없으면 False 를 반환한다.
# os.path.dirname() 메서드는 현재 실행되는 스크립트의 절대 경로 반환.
# os.path.normpath() 메서드는 파일명 만들기
#################################


# os 모듈을 읽어 들입니다.


#######################
# 파일 존재 유무 체크. 
# os.path.isfile() 을 사용하여 파일의 존재 여부를 확인 할 수 있다. 
# os.path.isfile() 메서는 있으면 True 없으면 False 를 반환한다.
# 1. 상대 경로를 사용하는 경우 
#    ../ 부모 폴더
#    ./  현재 폴더 
# 2. 절대 경로를 사용하는 경우 
#   C:\Intel\aa.txt
#   D:\Intel\aa.txt
# 
# 현재 폴더에 phones.txt 파일이 존재하는지 확인한다.
# os.path.isfile() 메서드는 있으면 True 없으면 False 를 반환한다.
#현재 작업 디렉토리 구하기
import os

dir=os.getcwd()
print("현재 작업 디렉토리", dir)

#현재 실행되는 스크립트 파일의 절대경로 구하기
absfile=os.path.abspath(__file__)
print(absfile)

curDir=os.path.dirname(os.path.abspath(__file__))
print(curDir)



#######################
# 현재 폴더의 파일/폴더를 출력합니다.
#phones.txt. 의 파일 절대 경로 만들기 = #폴더명 + "\" + 파일명
fileName="phones.txt"
#폴더명==>curDir
#"\"+파일명==>os.path.join("\",phones.txt)   #==> "\phones.txt"
txtA=os.path.join("/","phones.txt")
txtFile=os.path.normpath(curDir+txtA) #==>절대 경로
print(txtFile)

###########################
#현재 폴더에 phones.txt 파일이 존재하는지 확인한다.
#os.path.isfile(파일의절대경로) 메서드는 있으면 True 없으면 False를 반환

if (os.path.isfile(txtFile)):
    print("파일존재")
else: #파일이 없으면
    print("파일없음")
#######################
# 현재 폴더의 파일/폴더를 구분합니다.


#######################
# 폴더를 읽어 들이는 함수
# 폴더의 요소 읽어 들이기
# 폴더의 요소 구분하기
#         폴더라면 계속 읽어 들이기
#         파일이라면 출력하기
# 현재 폴더의 파일/폴더를 출력합니다.

#######################
# 기본 정보를 몇 개 출력해봅시다.

#######################
# 폴더를 만들고 제거합니다[폴더가 비어있을 때만 제거 가능].

#######################
# 파일을 생성하고 + 파일 이름을 변경합니다.

#######################
# 파일을 제거합니다.

#######################
# 시스템 명령어 실행


#######################
# environ({'PROGRAMFILES': 'C:\\Program Files', 'APPDATA': … 생략 …})
