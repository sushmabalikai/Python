def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
print(myfunc(fruit='apple',veggie='lettuce'))        
