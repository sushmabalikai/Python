def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))
print(myfunc(10,20,30,fruit='orange',food='eggs',animal='dog'))    
