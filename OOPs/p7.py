class Dog():
    species='mammal'
    def __init__(self,breed,name,spots):
        self.breed=breed
        self.name=name
        self.spots=spots
my_dog=Dog(breed='Lab',name='Sam',spots=False)
print(type(my_dog))
print(my_dog.species)

