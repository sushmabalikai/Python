class circle():
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
    def get_circumference(self):
        return self.radius*self.pi*2
my_circle=circle()
print(my_circle.pi)
print(my_circle.radius)
my_circle=circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())
