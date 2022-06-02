class Dog():
    def __init__(self,mybreed):
        self.my_attribute=mybreed
my_dog=Dog(mybreed='Huskie')
print(type(my_dog))
print(my_dog.my_attribute)
