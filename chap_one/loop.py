import os

# iterable object definition:
# An iterable is any Python object capable of returning its members one at a time, permitting it to be iterated over in a for-loop.

# ranges, string, list, tuple

# for loop : for item in iterable_object
print(list(range(0, 11, 2)))

for el in "coffee":
    print(el, end="")

x = 0
for i in range(10, 21):
    if i % 2 == 0:
        continue
    x += i
print(x, sep="")

# while loop
#  while True:
#       do something
# be careful: termination: **break**