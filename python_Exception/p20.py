a=5
b=2
try:
    print("resource open")
    print(a/b)
    print("resource closed")
except Exception as e:
    print("Hey,you cannot divide a number by zero",e)
