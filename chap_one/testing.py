# why test:
# reduce bugs in existing code
# ensure bugs fixed and stay fixed
# ensure the new features don't break the old ones
# ensure that cleaning up code does not introduce new bugs
# development is more fun

# Test driven development:
# Development begins by writing tests
# Once tests are written, write code to make tests pass
# Once tests pass, a feature is considered complete

# Red - Write a test that fails
# Green - Write the minimal amount of code necessary to make the test pass
# Refactor - Clean up the code, while ensuring that tests still pass

# assertion:
# We can make simple assertions with the assert keyword
# assert accepts an expression
# Returns None if the expression is truthy
# Raises an AssertionError if the expression is falsy
# Accepts an optional error message as a second argument

# If a Python file is run with the -O flag, assertions will not be evaluated!


def add_positive_numbers(x, y):
    # assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y


add_positive_numbers(1, 1)  # 2
add_positive_numbers(1, -1)  # AssertionError: Both numbers must be positive!


# DOCTEST
# We can write tests for functions inside of the docstring
# Write code that looks like it's inside of a REPL

# Syntax is a little strange
# Clutters up our function code
# Lacks many features of larger testing tools
# Tests can be brittle


def add(x, y):
    """add together x and y

    >>> add(1, 2)
    3

    >>> add(8, "hi")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return x + y

# UNITTEST
# Test smallest parts of an application in isolation (e.g. units)
# Good candidates for unit testing: individual classes, modules, or functions
# Bad candidates for unit testing: an entire application, dependencies across several classes or modules

# Python comes with a built-in module called unittest
# You can write unit tests encapsulated as classes that inherit from unittest.TestCase
# This inheritance gives you access to many assertion helpers that let you test the behavior of your functions

# You can run tests by calling unittest.main()

# self.assertEqual(x, y)
# self.assertNotEqual(x, y)
# self.assertTrue(x)
# self.assertFalse(x)
# self.assertIsNone(x)
# self.assertIsNotNone(x)
# self.assertIn(x, y)
# self.assertNotIn(x, y)



def eat(food, is_healthy):
    return "something"

def nap(num_hours):
    return num_hours

import unittest
# from activities import eat, nap

class ActivityTests(unittest.TestCase):
    print("running")
    def test_eat(self):
        """testing a thing"""
        print('eating')
        self.assertEqual(eat("apple", True), "something")

    def test_nap(self):
        """testing another thing"""
        self.assertEqual(nap(5), 5)

# to see the docstring run python name_of_file.py -v
if __name__ == "__main__":
    unittest.main()