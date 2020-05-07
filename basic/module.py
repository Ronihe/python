# why moudule:
#  to keep python files small.
# reuse code across multi files by importing
# just a python file, it helps creating our own file


# built-in module:
# https://docs.python.org/3/py-modindex.html
import random as so_random

so_random.randint(1, 10)

from random import randint, choice

randint(1, 100)
choice(["apple", "banana"])

from keyword import iskeyword


def contains_keyword(*words):
    return any(iskeyword(word) for word in words)


# external moudule:
is_contaoned = contains_keyword("hello", "lol", "True")
print(is_contaoned)

# creating your own modules-------------------------

# external moudules
# pip install
import termcolor

text = termcolor.colored("hi", color="red")
print(text)

import pyfiglet

hello = pyfiglet.figlet_format("hello")
colored_hello = termcolor.colored(hello, color="yellow")
print(colored_hello)

# name variable
# every python file has a name var : __ name__
# if the file is the main file being run, its value is "__main__"
#  otherwi

import roni_module
def say_hi():
    roni_module.say_moudule_name()

    print(f"hi the name var is {__name__}")


say_hi()
