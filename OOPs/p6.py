class Dog():
    def __init__(self,breed,name,sports):
        self.breed=breed
        self.name=name
        self.sports=sports
my_dog=Dog(breed='lab',name='Sammy',sports=False)
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.sports)

