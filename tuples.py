# Initialize a tuple with some elements
my_tuple = (1, 'hello', 3.14, [4, 5, 6])

# Access elements in the tuple using indexing
first_element = my_tuple[0]
print(first_element) # 1

# Use slicing to access a subset of the tuple
sub_tuple = my_tuple[1:3]
print(sub_tuple) # ('hello', 3.14)

# Use the + operator to concatenate tuples
other_tuple = (7, 8, 9)
combined_tuple = my_tuple + other_tuple
print(combined_tuple) # (1, 'hello', 3.14, [4, 5, 6], 7, 8, 9)

# Use the * operator to repeat a tuple
repeated_tuple = my_tuple * 2
print(repeated_tuple) # (1, 'hello', 3.14, [4, 5, 6], 1, 'hello', 3.14, [4, 5, 6])

# Check if an item is in the tuple using the in keyword
print(3.14 in my_tuple) # True

# Get the length of the tuple using the len function
print(len(my_tuple)) # 4

