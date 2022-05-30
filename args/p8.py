def funargs(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(key,value)
har=["Harry","Rohan","Hammad"]
normal="The normal programmer"
kw={"Rohan":"monitor","Harry":"fitness instructor"}
funargs(normal,*har,**kw)
