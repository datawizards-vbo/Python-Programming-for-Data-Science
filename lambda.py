# Define a simple function using the def keyword
def add(x, y):
    return x + y

# Call the add function
print(add(2, 3))  # Output: 5

# Define the same function using a lambda function
add_lambda = lambda x, y: x + y

# Call the lambda function
print(add_lambda(2, 3))  # Output: 5

# Create a list of integers
numbers = [1, 2, 3, 4, 5]

# Use the filter function with a lambda function to filter out even numbers
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Print the filtered list
print(filtered_numbers)  # Output: [2, 4]

# Use the map function with a lambda function to square each number in the list
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Print the squared list
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
