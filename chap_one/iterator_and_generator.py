# what is iterator: an obj can be iterated upon, an obj which returns data, one element at a time when next() is called on it.
# iterable: an object which will return an iterator when iter() is called on
# When next() is called on an iterator, the iterator returns the next item. It keeps doing so until it raises a StopIteration error.
test = "hello"
test_iterator = iter(test)
print(test_iterator.__next__())


# DIY loop
def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            print(thing)


my_for("lola")


# create a Counter class:
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


counter1 = Counter(0, 9)
for counter in counter1:
    print(counter)


# generators:
# Generators are iterators
# Generators can be created with generator functions
# Generator functions use the yield keyword
# Generators can be created with generator expressions

# generator:
# generaor is saving memory space: https://www.freecodecamp.org/news/how-and-why-you-should-use-python-generators-f6fb56650888/
# Also called calculation on demand
# Only compute values as needed
# Can help improve performance of your code



# Generator function: using yield, can yield multiple times, when invokes, returns generator
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


counter = count_up_to(5)  # counter is a generator which is a iterator
print(next(counter))

# use a for loop for generator
for num in counter:
    print(num)


# Another example to generate weekdays

def week():
    WEEK = ("Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun")
    day = 1

    while day <= 7:
        yield WEEK[day - 1]
        day += 1


for day in week():
    print(day)


# fib lit
def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


print(fib_list(8))


def fib_gen(max):
    a, b = 0, 1
    count = 0
    while count < max:
        a, b = b, a + b
        yield a
        count += 1


# generator expression:
# You can also create generators from generator expressions
# Generator expressions look a lot like list comprehensions
# Generator expressions use () instead of []

g = (num for num in range(1, 10))
print(g)