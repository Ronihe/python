# def of a function: a prpcess for execting a task
# It can accept input and return an output :
# https://stackoverflow.com/questions/15300550/return-return-none-and-no-return-at-all
# Useful for executing similar procedures over and over


# WHY:
# Stay DRY - Don't Repeat Yourself!
# Clean up and prevent code duplication
# "Abstract away" code for other users
# Imagine if you had to rewrite the "print()" function for every program you wrote

# return:
# exists the function
# outputs whatever value is placed after the return keyword
# Pops the function off of the call stack

# Parameters vs Arguments
# A parameter is a variable in a method definition.
# when a method is called, the arguments are the data you pas into the method's parameters.

# Parameter is variable in the declaration of function.
# Argument is the actual value of this variable that gets passed to function.

def add(a=10, b=20):
    return a + b


# why default params.
# Allows you to be more defensive
# Avoids errors with incorrect parameters
# More readable examples!
def add(a, b):
    return a + b


def math(a, b, fn=add):
    return fn(a, b)


def subtract(a, b):
    return a - b


math(2, 2)  # 4

math(2, 2, subtract)  # 0

# Scope:
# Variables created in functions are scoped in that function!

# global:
total = 0


def increment():
    global total
    total += 1  # if you want to modify the variable
    return total


print(increment())  # Error!

name = 'meme'


def say_hello():
    print(f'Hello {name}')


say_hello()


# nonlocal
# the variable in the parent variable

# keyword arguments : Order does not matt
def full_name(first, last):
    return "Your name is {first} {last}"


print(full_name(first='Colt', last='Steele'))  # Your name is Colt Steele

full_name(last='Steele', first='Colt')  # Your name is Colt Steele


# When you define a function and use an = you are setting a default parameter
#
# When you invoke a function and use an = you are making a keyword argument

# doc functions:
# use """ """


# *args, a special operator we can pass to functions:
# gathers remaining args as tuple
# just a param - call whatever you want

def what_are_args(*args):
    return type(args), args


print(what_are_args(1, 2, 3, "yes", True))


# kwargs, pass in key values
# Gathers remaining keyword arguments as a dictionary

def favorite_colors(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}'s favorite color is {value}")


favorite_colors(rusty='green', colt='blue')


# rusty's favorite color is green
# colt's favorite color is blue
def special_greeting(**kwargs):
    print("what is kwargs---", type(kwargs), kwargs)
    if "Colt" in kwargs and kwargs["Colt"] == "special":
        print("You get a special greeting Colt!")
        return
    elif "Colt" in kwargs:
        print(f"{kwargs['Colt']} Colt!")
        return
    print("Not sure who this is...")


special_greeting(Colt='Hello', test="abs")  # Hello Colt!
special_greeting(Bob='hello')  # Not sure who this is...
special_greeting(Colt='special')  # You get a special greeting Colt!


# Parameter Ordering
# parameters
# *args
# default parameters
# **kwargs

def display_info(a, b, *args, instructor="Colt", **kwargs):
    return [a, b, args, instructor, kwargs]


print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))


# * to unpack an argument
def sum_all_values(*args):
    # there's a built in sum function - we'll see more later!
    print("what is the args--", args)
    return sum(args)


# sum_all_values([1, 2, 3, 4])  # nope...
# sum_all_values((1, 2, 3, 4))  # this does not work either...

sum_all_values(*[1, 2, 3, 4])  # 10
sum_all_values(*(1, 2, 3, 4))  # 10


# ** dictionary unpacking
def display_names(first, second):
    return f"{first} says hello to {second}"


names = {"first": "Colt", "second": "Rusty"}

# display_names(names)  # nope..

display_names(**names)  # "Colt says hello to Rusty"
