try:
    num=100
    print(num)
except NameError as err:
    print(err.args[0])
else:
    print("Inside else block")
finally:
    print("Hello World")
    print("Always executes")
