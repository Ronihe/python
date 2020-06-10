# Base Types:
# int, float, boolean, string, bytes
# https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf
def base_types():
    '''
    https://realpython.com/python-data-types/
    Returns:
    '''

    print("int, float, boolean, string, bytes")
    print("int, without any prefix is a decimal number")
    print("10 is a decimal int-", 10)
    print("use type() to get the type", type(10 / 2), 10 / 2)
    print(9 > float("-inf"))
    print(bool(""), "\\newline")
    print("hi tab \tafter tab")

    test = "I am a test"
    print(f'i am a fstrng {test}')

    print(type(True))

    built_in_func = """
    abs()	Returns absolute value of a number
    divmod()	Returns quotient and remainder of integer division
    max()	Returns the largest of the given arguments or items in an iterable
    min()	Returns the smallest of the given arguments or items in an iterable
    pow()	Raises a number to a power
    round()	Rounds a floating-point value
    sum()	Sums the items of an iterable
    """

    type_conversion = """
    ascii()	Returns a string containing a printable representation of an object
    bin()	Converts an integer to a binary string
    bool()	Converts an argument to a Boolean value
    chr()	Returns string representation of character given by integer argument
    complex()	Returns a complex number constructed from arguments
    float()	Returns a floating-point object constructed from a number or string
    hex()	Converts an integer to a hexadecimal string
    int()	Returns an integer object constructed from a number or string
    oct()	Converts an integer to an octal string
    ord()	Returns integer representation of a character
    repr()	Returns a string containing a printable representation of an object
    str()	Returns a string version of an object
    type()	Returns the type of an object or creates a new type object    
    """
    print("built-in functions", built_in_func)
    print(divmod(5, 2), pow(2, 3))

    iterables_iterator = """
    enumerate()	Returns a list of tuples containing indices and values from an iterable
    len()	Returns the length of an object
    sorted()	Returns a sorted list from an iterable
    """


def container_type():
    '''
    ordered sequences: list, tuples
    key containers: dict, set
    non_changable: tuple
    Returns:

    '''


def loop_control():
    '''
    key word: break continue, else
    Returns:

    '''


def operations_list():
    lst = []
    append_return = lst.append("first")
    print(lst, append_return, "append return None")
    extend_return = lst.extend(["extending"])
    print(lst, extend_return, "list extendd return None")
    insert_return = lst.insert(1, "idx one")
    print(lst, insert_return, "list insert return None")
    remove_list = lst.remove("extending")
    print(lst, remove_list, "list remove return None")
    pop_list = lst.pop(0)
    print(lst, pop_list, "pop list remove and return value")
    lst.sort()
    lst.reverse()


def operations_dict():
    d = {"name": "roni", "hobby": "eating"}
    keys = d.keys()
    values = d.values()
    items = d.items()
    d.update()
    print(keys, values, items)
    print("new d--", d)

    poped = d.pop("name")
    print(poped, d)
    d["name"] = "Roni"
    popedItem = d.popitem()
    print(popedItem, d)
    print(d.get("x", "yyy"))


def operations_set():
    pass


if __name__ == '__main__':
    # base_types()
    # operations_list()
    operations_dict()
