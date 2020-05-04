# set is like normal math set
# no duplicaet
# no orders
# cannot access the items in a set by index

# Sets cannot have duplictes
s = set({1, 2, 3, 4, 5, 5, 5})  # {1, 2, 3, 4, 5}

# Creating a new set
s = set({1, 4, 5})

# Creates a set with the same values as above
s = {1, 4, 5}

4 in s
# True

8 in s
# False

# Add:
s.add("abc")

print(s)

# remove / discard

s.remove(4)
print(s.discard(99))  # avoid the keyError

# copy creates a copy of the set

# clear

# math:
# intersection:
# symmetric_difference
# union

# set comprehension:
set_exponentiation = {x ** 2 for x in range(10)}
print(set_exponentiation)


#
def are_all_vowels_in_string(string):
    return len({char for char in string if char in "aeiou"}) == 5
