def myfunc(**kwargs):
    if 'veggie' in kwargs:
        print('my veggie of choice is {}'.format(kwargs['veggie']))
    else:
        print('I did not find any fruit here')
    
myfunc(fruit='apple',veggie='lettuce')
print(myfunc)
        
