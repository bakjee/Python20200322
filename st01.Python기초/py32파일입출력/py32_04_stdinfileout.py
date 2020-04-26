
#########################
# 키보드 입력을 파일에 쓰는 프로그램을 작성하여 본다.
#########################
import os

# read file
pfw = open("phones.txt", "a", encoding="utf-8")

# Input values and write it onto a file.
while True:
    valuein = input("입력하세요. 입력을 끝낼려면 엔터를 치세요>>>")
    if valuein == "":
        break
    else:
        pfw.write(valuein)  # Can't change lines, how do you do it?
        pfw.write("\n")
# pfw.writelines()
# pfw.write(valuein+"\n")


pfw.close()


#########################
# Using Loops

#########################
##
