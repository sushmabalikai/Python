try:
    num=100
    ret=12/0
    print(num)
except NameError as err:
    print(err.args[0])
else:
    print("Inside else block")
finally:
    print("Hello World")
    print("Always executes")
