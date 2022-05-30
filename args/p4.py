def master(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)
list=["Harry",22,865676]
marklist={"Harry":100,"Rohan Das":97,"Aman":91}
master("normal",*list,**marklist)
