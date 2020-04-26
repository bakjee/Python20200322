import os #파일 처리 모듈
def getAbsFileName(fileName):
    result=""

    absfile=os.path.abspath(__file__)
    curDir=os.path.dirname(os.path.abspath(__file__))
    txtA=os.path.join("/",fileName)
    result=os.path.normpath(curDir+txtA) #==>절대 경로

    return result


fileName=getAbsFileName("/bb.txt")
pfw= open(fileName,"w",encoding="utf=8")
####################################
pfw.write("홍길동 010-1234-5678\n")
pfw.write("김철수 010-1234-5679\n")
pfw.writelines("김영희 010-1234-5680")

pfw.close()




