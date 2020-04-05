for y in range(1, 11, 1):
    for x in range(1, 11, 1):
        print("*"*x, end="")
    print("")


for i in range(0, 11, 1):
    for j in range(0, i+1, 1):
        print("*", end="")
    print()

print("------------------------------------------------------------------------")

for i in range(1, 11, 1):
    for j in range(1, i+1, 1):
        print(" ", end="")
    for j in range(i+1, 11, 1):
        print("*", end="")
    print()


print("         ++++++++++++++++++++++++++++++++++++++++++++++++")
for i in range(0, 11, 1):
    for j in range(0, i+1, 1):
        print("*", end="")
    print()
for i in range(1, 11, 1):
    for j in range(11, i+1, 1):
        print(" ", end="")
    for j in range(i+1, 11, 1):
        print("*", end="")
    print()
