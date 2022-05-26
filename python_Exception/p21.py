a=5
b=2
try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("Hey,you cannot divide a number by zero",e)
finally:
    print("resource closed")
