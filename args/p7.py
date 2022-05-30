def funargs(normal,*args):
    print(normal)
    for item in args:
        print(item)
har=["Harry","Rohan","Skillf","Hammad"]
normal="The normal function"
funargs(normal,*har)

