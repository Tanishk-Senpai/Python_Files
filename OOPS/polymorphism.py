# The word polymorphism means having many forms. In Programming context, it means that a function can have
# the same function name (but different signatures) being used for different types.

# Example of Polymorphism via Method Overriding
# Different classes can have the same methods with the same name, but the behavior will be different
# depending upon the object type.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        return "Some Generic animal sound"

class Dog(Animal):
    def __int__(self, name: str):
        super().__init__(name)

    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def __intit__(self, name: str):
        super().__init__(name)

    def make_sound(self):
        return ("Meow")

def animal_sound(animal):
    print(animal.make_sound())

dog = Dog('Tommy')
cat = Cat('Kitty')

animal_sound(dog)
animal_sound(cat)

# Example of Polymorphism in Functions

# A function can take different types of object and execute the same method if that method is defined in those objects.

class Rectangle:
    def __init__(self, width: int, height: int):
        assert width >= 0 and height >= 0

        self.width = width
        self.height = height

    def area(self):
        return f"The area of Reactangle is: {self.width * self.height}"

class Circle:
    def __init__(self, radius: int):
        assert radius >= 0
        self.radius = radius

    def area(self):
        from math import pi
        return f"The area of Circle {pi * (self.radius)**2}"

def calculate_area(object):
    print(object.area())
rectangle = Rectangle(10, 10)
circle = Circle(10)
calculate_area(rectangle)
calculate_area(circle)

# Polymorphism via built in functions

# Python's inbuilt functions like len() work in a polymorphic way because they can handle
# different types of objects as long as they implement the appropriate method (__len__ in this case)

print(len('tanishk'))
print(len([1,2,3,4,5]))
print(len({'tanishk': 18, 'ritik': 18}))

# Duck Typing in Python
# In python, the actual type of object is less important the method it implements
# if it walks like a duck and quacks like a duck, then its a duck and it will give the desired output

# Kind of same like method overriding
