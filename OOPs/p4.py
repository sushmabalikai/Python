class Dog():
    def __init__(self,mybreed):
        self.breed=mybreed
my_dog=Dog(mybreed='Huskie')
print(type(my_dog))
print(my_dog.breed)
