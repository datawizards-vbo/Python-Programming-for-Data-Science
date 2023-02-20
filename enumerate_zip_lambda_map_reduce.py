# enumerate: enumerate is a built-in Python function that allows you to loop over a list while keeping track of the index of each element.
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry


# zip: zip is a built-in Python function that allows you to combine two or more lists into one list of tuples, where the nth tuple contains the nth elements from each list.
fruits = ['apple', 'banana', 'cherry']
prices = [1.2, 2.5, 3.0]
for fruit, price in zip(fruits, prices):
    print(fruit, price)

# Output:
# apple 1.2
# banana 2.5
# cherry 3.0


# lambda: lambda is a short way of writing small, anonymous functions in Python.
square = lambda x: x * x
print(square(5))

# Output:
# 25


# map: map is a built-in Python function that applies a function to each element in an iterable and returns a map object with the results.
fruits = ['apple', 'banana', 'cherry']
uppercase_fruits = list(map(lambda x: x.upper(), fruits))
print(uppercase_fruits)

# Output:
# ['APPLE', 'BANANA', 'CHERRY']



# reduce: reduce is a built-in function from the functools module in Python that applies a function to the first two elements of an iterable and then to the result and the next element, and so on, until all elements have been processed.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# Output:
# 120
