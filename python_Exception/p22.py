a=5
b=2
try:
    print("resource open")
    print(a/b)
    k=int(input("Enter a number"))
    print(K)
except ZeroDivisionError as e:
    print("Hey,you cannot divide a number by zero",e)
except ValueError as e:
    print("Invalid Input")
except Exception as e:
    print("something went wrong....")
finally:
    print("resource closed")
