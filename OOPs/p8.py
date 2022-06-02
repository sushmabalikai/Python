class Dog():
    species='mammal'
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
    def bark(self):
        print("WOOF!")
my_dog=Dog("Lab","Frankie")
print(type(my_dog))
print(my_dog.species)
print(my_dog.name)
