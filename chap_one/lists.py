# Intro to lists:
#  built-in functions: len(), in,
#
#
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

i = 0
while i < len(numbers):
    print(numbers[i], end=" ", flush=True)
    i += 1
# built-in functions:
# append():
numbers.append(numbers[-1] + 1)
print("append() one number to the end -", numbers)

# extend(): add iterable object
numbers.extend([10, 100, 1000])
numbers.extend("abc")
numbers.extend(range(-12, -2, 2))
print(numbers)

# insert(): at given position
numbers.insert(len(numbers), "insert")
print(numbers)

# pop(): remove the last one item, provide index
numbers.pop(1)
print(numbers)
# clear(): remove all the items from the list
numbers.clear()
print(numbers)
# remove(): remove by value, return error if not found
try:
    numbers.remove(1)
    print("removed the first 1 ")
except ValueError:
    print(ValueError.args)
numbers = [1, 2, 4, 6, 1, 9]

# index(): return the specified item in the list.
print("the first index of 1-", numbers.index(1))
print("this fist index of 1 after index 1-", numbers.index(1, 1))
print("this fist index of 1 after index 1and before 5-", numbers.index(1, 1, 5))

# count(): number of times x appears, no error if not found
print(numbers.count(10))

# reverse(): reverse the elements in the list
print("before the reverse", numbers)
print("after the reverse", numbers.reverse(), numbers)

# sort(): sort in place
numbers.sort()
print(numbers)

# join(): string method, return a new string, all str instance in the iterable_object
str_list = []
for number in numbers:
    str_list.append(str(number))

print(" ".join(str_list))

# slice:[start:end:step]: a new list of the the old list, exclusive counting
# if the step is negative,
print(numbers[:2])

# swap values: occasions: shuffling, sorting
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

# list comprehension: new list
comprehensed_list = [num * 10 for num in numbers]
print(comprehensed_list)

my_name = "roni"
my_name_upper = [letter.upper() for letter in my_name]
print(my_name_upper)

# list comprehension with logics
even_numbers = ["I am even" + str(number) for number in numbers if number % 2 == 0]
print(even_numbers)
even_numbers_string = " ".join("I am even" + str(number) for number in numbers if number % 2 == 0)
print(even_numbers_string)

# nested list with list comprehension
nested_list = [[11, 12, 13], [22, 23, 24], [33, 34, 35]]
flattend_nested_list = []
[[flattend_nested_list.append(j) for j in i] for i in nested_list]
print(flattend_nested_list, nested_list)

answer = [[i for i in range(0,3)] for num in range(0,3)]
print(answer)
