# inheritance: define a class based on another class which is called parent class.
# How it works: passing the parent class as an arg to the child class.

# keyword: super() to call the __init__ function of a parent.
class Animal:
    def __init__(self, species, age):
        print("animal  init")
        self.species = species
        self._age = age

    def make_sound(self, sound):
        return f"{self.species} make this sounds {sound}"

    @property
    def age(self):
        print("in age property")
        return self._age

    @age.setter
    def age(self, new_age):
        print("seting new age")
        if new_age > 0:
            self._age = new_age
        else:
            raise ValueError("age cannot be negative")


class Ambulatory:
    def __init__(self, name, toy):
        print("ambulatory init")
        self.name = name
        self.snore = True
        self.cute = None
        self.toy = toy

    def make_sound(self):
        return f"bulldog making sound"

    def walk(self):
        return f"{self.name} is walking"

    def play(self):
        return f"{self.name} is playing {self.toy}"

    def be_cute(self):
        self.cute = True


class Dog(Animal, Ambulatory):
    def __init__(self, name, species, age, mom, toy):
        super().__init__(species=species, age=age)  # the same as Animal.__init__(species, age)
        # it is interesting, the init in Amulatory is never called, but can use the method.
        # in order to run the init in Ambulatory, just need to run:
        Ambulatory.__init__(self, name=name, toy=toy)
        self.name = name
        self.mom = mom

    def __repr__(self):
        return f"{self.name} loves {self.mom}"


lola = Dog("lola", "bull dog", 6, "roni", "piggy")
print(lola)

print(lola.age)
lola.age = 20  # no need to create get_age set_age, or get the private _age
lola.species = "family"
print(lola.__dict__)

print(lola.make_sound("wooph"))
print(lola.walk())
print(lola.play())


# method resolution order:
# Whenever you create a class, Python sets a Method Resolution Order, or MRO, for that class, which is the order in which Python will look for methods on instances of that class.

# You can programmatically reference the MRO three ways:
#
# __mro__ attribute on the class
# use the mro() method on the class
# use the builtin help(cls) method
# print("the method resolution order: ", Dog.__mro__)
# print("use mro()", Dog.mro())
# print("use help()", help(Dog))

# polymorphism: an object can take on many (poly) forms (morph).
# here are two important practical applications:
# 1. the same class method works in a similar way, but different for different classes
# 2. the same operation works for different kinds of objects

# Polymorphism & Inheritance
# 1. The same class method works in a similar way for different classes
#
# A common implementation of this is to have a method in a base (or parent) class that is overridden by a subclass. This is called method overriding.
# Each subclass will have a different implementation of the method.
# If the method is not implemented in the subclass, the version in the parent class is called instead.

# special method: __magic__
class GrumpyDog(dict):
    # if there are no __init__, then will just run dict init
    def __repr__(self):
        print("I am a bad ass dog")
        return super().__repr__()

    def __missing__(self, key):
        print("what you want key is not here")
    def __setitem__(self, key, value):
        print("you want to change the grumpy dog", key, value)
        return super().__setitem__(key, value)



d = GrumpyDog({"name": "dog", "city": "SF"})
print(d)
missing_key = d["missing_key"]
d["city"] = "San Leandro"

