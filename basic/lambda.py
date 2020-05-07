# lambdas

def square(num): return num * num


square2 = lambda num: num * num

# map(func, iterable_obj)
doubles = map(lambda num: num ** 3, [1, 2, 3])

print(tuple(doubles))

# filter: (func, iterable_obj)
# There is a lambda for each value in the iterable.
# Returns filter object which can be converted into other iterables
# The object contains only the values that return true to the lambda

evens = filter(lambda num: num % 2 == 0, [1, 2, 3, 4, 5])
print(list(evens))

# combine map and filter
names = ["roni", "lola", "andrew"]
map_filter = map(lambda name: "Your instructor is :" + name, filter(lambda name: len(name) == 4, names))
print(list(map_filter))

list_compre = ["Your instructor is : " + name for name in names if len(name) == 4]
print(list_compre)

# all() if all el are Truthy
# any(): return true if any element if the iterable is truthy, if the iterable is empty retrun false.
# generator expression: https://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehension

# sorted: return a new list, reverse = True,
# sorted: for dict: sorted(dict, key=func), ex. sort by the len, sorted(dict, key=len)

# max(iterable_obj, optional key=func)
# min(iterable_obj, optional key=func)

# reversed() return a reversed iterator.

# zip() : combine the element of each iterable object in sequence until the shortest one exhausts, return iterable sequence of tuple
zip_test1 = [1, 2, 3]
zip_test2 = ["a", "b", "c"]
zip_test3 = [65, 66, 67]

zipped = zip(zip_test1, zip_test2, zip_test3)
max_zippped = {pair[1]: max(pair[0], pair[2], key=lambda num: -num) for pair in zipped}
print(max_zippped)

# closure: accessing vars defined in outer functions after they have returned.
# pr
test = dict([(1, 3), (2, 4)])
print(test)

def extract_full_name(names):
    return [f"{name['first']} {name['last']}" for name in names]

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))