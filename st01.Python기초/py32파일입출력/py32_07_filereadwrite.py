
#  proverbs.txt 파일에서 줄 단위로 읽어서 output.txt 에 쓰시오 
 
import os

def getAbsFileName(fileName):
    result=""

    absfile=os.path.abspath(__file__)
    curDir=os.path.dirname(os.path.abspath(__file__))
    txtA=os.path.join("/",fileName)
    result=os.path.normpath(curDir+txtA) #==>절대 경로

    return result

#파일 열기
readfile=getAbsFileName("/file/proverbs.txt")
pfr=open(readfile, "r", encoding="utf-8") #읽기용 파일열기
writefile=getAbsFileName("/file/out.txt")
pfw=open(writefile, "a", encoding="utf-8") #쓰기용 파일열기
#파일 처리
#proverbs.txt에서 줄 단위로 읽어 들여 output.txt
읽기=pfr.readline() #readline includes next line.
while 읽기!="":
    pfw.write(읽기)
    # pfw.write("\n") ### This code is not necessary
    읽기=pfr.readline()






#파일 닫기

pfr.close()
pfw.close()




#쓰기용 파일 열기
