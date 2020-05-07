# func: a object, first-class obj. can be assigned to var, stored in collections, created and delted dynamically and passed as args.
# closure: a nested function object that has access to a free var from enclosing functions that has finished its execution.
#   chars:
# 1. nested func
# 2. access to a fee var in outer scope
# 3. returned from the enclosing function
# python stores a function together with env:
# It is a record that stores a function together with an environment: a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.
# A closure—unlike a plain function—allows the function to access those captured variables through the closure’s copies of their values or references, even when the function is invoked outside their scope.


# How to modify a var with immutable type in outer function
# python class - self : alternate solution to small class
#

def outer():
    outer_var = "I am outer var"

    def inner():
        nonlocal outer_var  #
        outer_var += "I changed ourter_var"
        print("testing closure--", outer_var)

    return inner()


outer()


def counter():
    print("what is the counter-", counter)
    counter.count = 0

    def inner():
        counter.count += 1
        return counter.count

    return inner(), counter.count


print(counter())


# when just using the variable through a closure, you dont need to use nonlocal or objects
def outer(a):
    def inner(b):
        return a + b

    return inner


result = outer(10)

print(outer(20)(10))
