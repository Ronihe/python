# dictionary: key values, no ordering


# Init a dict:
roni = {"name": "roni", "job": "software engineer", 12: "roni's lucy number"}
print(roni)
# To access the key
print("roni[\"name\"]: ", roni["name"])
new_dict = dict()

# To get all the values:
print("to get all the values in the dict")
for val in roni.values():
    print(val)
# To get all the keys
print("to get all the keys in the dict")
for key in roni.keys():
    print(key)

print("to get all the values in the dict")
for item in roni.items():
    print(type(item), item[0], item[1])

for key, value in roni.items():
    print(type(key), key, value)

# check if a key is int he dict.
if "name" in roni:
    print(True)
else:
    print("cannot find it")
# check if a value in the dict.

if "roni" in roni.values():
    print("yes, roni is a value in dict roni")
else:
    print("roni is not a value in dic roni")

# method
# clear(): clear all the keys and values in a dictionary
test = dict(name="test", age=21, d12="luck")
print("test dict:", test)

test.clear()
print("test dict:", test)

# make a copy:
test_copy = test.copy()

# fromkeys(iterable_obj, value)
dict_from_keys = dict.fromkeys({"email", "email", "email"})
print(dict_from_keys)

# get(key)
# d.get("no_key") # None
# pop(key), if not exist, KeyError, return the value of the key
# popitem() remove a random key, re
# update(): set of key and value pairs.
first = dict(a=1, b=2, c=3, d=4, e=5)
second = {"name": "roni"}

second.update(first)
print(second)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# let's overwrite an existng key
second['a'] = "AMAZING"

# if we update again
second.update({"upate": True})  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# the update overrides our values
print(second)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# dict comprehension
# { _ : _ for _ in _ }
# iterate over keys by default, /to iterate over keys and values using .items()
numbers = dict(first=1, second=2, third=3)
squared_numbers = {key + "_update": value ** 2 for key, value in numbers.items()}
print(squared_numbers)  # {'first': 1, 'second': 4, 'third': 9}

# conditional logic with dicionaries
num_list = [1, 2, 3, 4]

num_dict = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(num_dict)

# can just use dict() to turn list to dict
