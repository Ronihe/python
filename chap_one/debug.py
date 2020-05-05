import pdb
# common errors:
# syntax errors.
# NameError: this occurs when a variable is not defined
# TypeError: occurs when an operation or function is applied to the wrong type.
# ex: python cannot interpret an operation
# IndexError: outside the range of the list or string
# ValueError : built-in operation or func receive an arg with right type but inappropriate value
# int("foo")
# KeyError: when a dict does not have a specific key
# AttributeError: the obj does not have that attribute

# raise own exception:
try:
    print("I am trying...")
    raise ValueError("invalid value")
except ValueError as err:
    print(err)

# handle errors:
# try/except

# try:
# except:
# else:
# finally:
try:
    pdb.set_trace()
    num = int(input("give me a number"))
except (ZeroDivisionError, TypeError) as err:
    print("it is not a number", err)
else:
    print("i a m the else ")
#     can just break here to not run the finally
finally:
    print("run anyway")

# debug with pdb
#  import pdb; pdb.set_trace()
