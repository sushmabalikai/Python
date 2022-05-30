def printmarks(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)
marklist={"Harry":100,"Rohan Das":97,"Aman":91,"Mani":89}
printmarks(**marklist)
