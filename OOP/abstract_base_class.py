# class Shape:  # Shape is a child class of ABC
#     def area(self):
#         pass

#     def perimeter(self):
#         pass

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return (self.length * self.length)

#     def perimeter(self):
#         return (4 * self.length)

# shape = Shape()
# square = Square(4)

# In the example above, you can see that an instance of Shape can be created even though an object from this class cannot stand on its own. Square class, which is the child class of Shape, actually implements the methods, area() and perimeter(), of the Shape class. Shape class should provide a blueprint for its child classes to implement methods in it. To prevent the user from making a Shape class object, we use abstract base classes.
# from abc import ABC, abstractmethod

# class Shape(ABC):  # Shape is a child class of ABC
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

# square = Square(4)
# this will code will not compile since abstarct methods have not been
# defined in the child class, Square
from abc import ABC, abstractmethod


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self, shape):
        return shape.area()

    @abstractmethod
    def perimeter(self, shape):
        return shape.perimeter()


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)

square = Square(3)
shape = Shape()
# this will code will not compile since Shape has abstract methods without
# method definitions in it