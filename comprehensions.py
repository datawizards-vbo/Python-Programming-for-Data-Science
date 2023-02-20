# Idea of list comprehension: 
# new_list = [expression for item in iterable if condition]

# Create a list of even numbers from a list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Create a list of first elements in a list of lists
list_of_lists = [[1, 2], [3, 4], [5, 6]]
first_elements = [inner_list[0] for inner_list in list_of_lists]
print(first_elements)  # Output: [1, 3, 5]

# Create a list of squares of numbers from 1 to 10
squares = [num**2 for num in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Create a list of all uppercase letters in a given string
string = "Hello World!"
uppercase_letters = [letter for letter in string if letter.isupper()]
print(uppercase_letters)  # Output: ['H', 'W']

# Create a dictionary that maps names to their lengths
names = ["Alice", "Bob", "Charlie", "David"]
name_length = {name: len(name) for name in names}
print(name_length)  # Output: {'Alice': 5, 'Bob': 3, 'Charlie': 7, 'David': 5}

# Create a dictionary that maps integers to their squares
numbers = [1, 2, 3, 4, 5]
squares = {num: num**2 for num in numbers}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Create a dictionary that maps the lengths of words in a string to the words themselves
string = "The quick brown fox jumps over the lazy dog"
word_lengths = {len(word): word for word in string.split()}
print(word_lengths)  # Output: {3: 'The', 5: 'quick', 5: 'brown', 3: 'fox', 5: 'jumps', 4: 'over', 3: 'the', 4: 'lazy', 3: 'dog'}
