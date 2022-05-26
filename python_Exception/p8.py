try:
    x=int(input("enter the value of x"))
    y=int(input("enter the value of y"))
    ret=x/y
    print("result=",ret)
except ZeroDivisionError:
    print("Division by zero")
