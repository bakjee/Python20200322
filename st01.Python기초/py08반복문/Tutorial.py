marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number+1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number, mark, ",점")


for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

print()
print()
print("===========================================================================================")

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

i = 0
while True:
    i += 1
    if i > 201:
        break
    print('*'*i)

A = [70, 60, 55, 75, 95, 80, 80, 85, 100]
total=0
for score in A:
    total+=score
    print(total)
average=total/len(A)
print(average)

numbers=[1,2,3,4,5]
result=[n*2 for n in numbers if n%2==1]
print(result)

    

