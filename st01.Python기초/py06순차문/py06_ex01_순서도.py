a = "Hello python"
b=a[:5]
c=a[6:]
d=a[1]

print(len(a))
#page 222~224

s=input("값을 입력하시오 :")
try:
    m=s//60
    s=s%60
    print("m:",m)
    print("s:",s)
except TypeError as identifier:
    print (identifier)
