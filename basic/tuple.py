import calendar

# tuple: ordered the collection of items, data has not be unique
# immutable, cannot be changed
num_tuple = (1, 2, 3, 4, 5, 5, 5)

# why tuple:
# faster than list, makes code sager, can be the valid key in dic
MONTHS = tuple([calendar.month_name[month] for month in range(1, 13)])
print(type(MONTHS), type(num_tuple))

# method: count

print(num_tuple.count(5))
print(num_tuple.count(0))
print(num_tuple.index(5))
print(num_tuple.index(0))


