class Dog():
    species='mammal'
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
    def bark(self,number):
        print("WOOF! My name is {} and the number is {}".format(self.name,number))
my_dog=Dog('Lab','Frankie')
print(type(my_dog))
print(my_dog.species)
print(my_dog.bark)
print(my_dog.bark(10))
