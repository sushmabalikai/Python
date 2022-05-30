def my_func(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
my_func(name='tom',spot='football',roll=10)        
