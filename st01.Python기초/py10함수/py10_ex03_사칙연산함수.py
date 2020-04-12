def Add(x, y):
    result = None
    try:
        result = x+y
    except Exception as ex:
        pass
    return result


def Minus(x, y):
    result = None
    try:
        result = x-y
    except Exception as ex:
        pass
    return result


def Mul(x, y):
    result = None
    try:
        result = x*y
    except Exception as ex:
        pass
    return result


def Div(x, y):
    result = None
    try:
        result = x/y
    except ZeroDivisionError as ex:
        print("Zero Division")
        pass
    except Exception as ex:
        pass
    return result


def myinput():
    result = None
    try:
        result = int(input(" Number : "))
    except Exception as ex:
        pass
    return result


def myprint(str, value):
    # 사용예시 myprint("Add",10)
    result = None
    try:
        result = "%s : %s" % (str, value)
        print(result)
    except Exception as ex:
        pass

    return result


def main():

 # Purpose of function 'main'
    # Input 1st number
    # Input 2nd Number
    # Call 'Add, Minus,Mul&Div' functions and print results

    num1 = myinput()
    num2 = myinput()
    value = Add(num1, num2)
    myprint("Add", value)

    value = Minus(num1, num2)
    myprint("Minus", value)

    value = Mul(num1, num2)
    myprint("Mul", value)

    value = Div(num1, num2)
    myprint("Div", value)

    return


main()
