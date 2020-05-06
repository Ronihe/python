# what is oop:
# Object oriented programming is a method of programming that attempts to model some process or thing in the world as a class or object.
#
# class - a blueprint for objects. Classes can contain methods (functions) and attributes (similar to keys in a dict).
# instance - objects that are constructed from a class blueprint that contain their class's methods and properties.
# With object oriented programming, the goal is to encapsulate your code into logical, hierarchical groupings using classes so that you can reason about your code at a higher level.

# encapsulation: the grouping of public and private attributes and methods into a programmatic class, making abstraction possible
# abstraction: Abstraction - exposing only "relevant" data in a class interface, hiding private attributes and methods (aka the "inner workings") from users

# creating a class:
# instantiating a class :  create a object
#  __init__ method
# self : refers to the current class instance, always the first the param for __init__
class User:
    active_users = 0  # class attr

    @classmethod
    def total_user(cls):
        # cls.total_species += 1
        return cls.active_users

    @classmethod
    def from_string(cls, str):
        return cls(str)

    def __init__(self, first, last=0):
        print("new user has been made")
        self.name = f"{first} {last}"
        self.default_attr = "roni's dog"
        User.active_users += 1

    def __repr__(self):
        return self.name

    def full_name(self):
        return self.name

    def likes(self, thing):
        return f"{self.name} like {thing}"


user1 = User("lola")
user2 = User('roni')

print("what is the user1--", user1)
print(user1.default_attr)
print(user1.likes("roni"))

print(User.active_users)  # called from class
print("classmethod to get total users", User.total_user())

print("classmethod to create a new user", User.from_string("fromClassMethos"))


# dounder __method__, special in python
# _private: convention
# __namemingling: make this attribute particular to this class

# class attr: define one time

class Pet:

    def __init__(self, name, species):
        self.name = name
        self.species = species


cat = Pet("cat", "cat")
print(cat)

# class method: @classmethod decaratr
