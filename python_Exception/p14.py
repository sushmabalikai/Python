try:
    n=0
    ret=12/n
except ZeroDivisionError as err:
    print(err.args[0])
except:
    print("some exception happened")
else:
    print("result: ",ret)
