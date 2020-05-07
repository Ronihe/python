# higher order functions:
# def sum(n, func=lambda num: num):
#     total = 0
#     for i in range(n + 1):
#         total += func(i)
#     return total
#
#
# print(sum(2, lambda n: n ** 2))


# what is decorator:
# decorators are functions
# Decorators wrap other functions and enhance their behavior
# Decorators are examples of higher order functions
# Decorators have their own syntax, using "@" (syntactic sugar)

# why decorators?
# Removing code duplication across functions
# More easily perform function analytics/logging
# Exit out of a function early if certain conditions aren't met

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")

    return wrapper


@be_polite
def greet():
    print("My name is Roni.")


# greet = be_polite(greet)
greet()


# we are decorating our function
# with politeness!

def shout(fn):
    def wrapper(*name):
        return fn(*name).upper()

    return wrapper


@shout
def greet(name):
    return f"Hi, I'm {name}."


@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."


print(order("fish", "chicken"))


# decorator pattern
def my_decorator(fn):
    def wrapper(*args, **kwargs):
        # do some stuff with fn(*args, **kwargs)
        pass

    return wrapper


def log_function_data(fn):
    def wrapper(*args, **kwargs):
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)

    return wrapper


@log_function_data
def add(x, y):
    '''Adds two numbers together.'''
    return x + y;


add(5, 6)

from functools import wraps


# wraps preserves a function's metadata
# when it is decorated
def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # do some stuff with fn(*args, **kwargs)
        pass

    return wrapper


from time import time


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"Time Elapsed: {t2 - t1} seconds.")
        return result

    return wrapper


@speed_test
def sum_wrap(max):
    return sum(num for num in range(max + 1))


sum_wrap(10000000)

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            return "No keyword arguments allowed!"
        return fn(*args)
    return wrapper

def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                print(f"Invalid! First argument must be {val}")
            return fn(*args, **kwargs)
        return wrapper
    return inner

@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)

fav_foods("burrito", "ice cream")
  # ('burrito', 'ice cream')
fav_foods("ice cream", "burrito")
  # 'Invalid! First argument must be burrito'

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2

add_to_ten(10, 12) # 12
add_to_ten(1, 2)
  # 'Invalid! First argument must be 10'