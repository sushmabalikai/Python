try:
    f=open('test file','w')
    f.write("write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print('Hey you have an OS Error')
finally:
    print("I always run")
