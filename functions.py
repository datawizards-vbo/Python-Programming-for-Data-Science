# Define a function that takes in two numbers and returns their sum
def add_numbers(a, b):
    return a + b

# Define a function that returns the square of a number
# Also, add a docsting.
def square(number):
    """
    This function returns the square of a given number.
    
    Parameters:
    number (int): The number to be squared.
    
    Returns:
    int: The squared number.
    """
    return number ** 2

print(square(3))

# Define a function that takes in a list and returns the largest element
def find_max(my_list):
    return max(my_list)

# Define a function that takes in a string and returns the number of vowels
def count_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in my_string:
        if char.lower() in vowels:
            count += 1
    return count

# Define a function that takes in a list of numbers and returns a new list with only the even numbers
def filter_even(my_list):
    return [num for num in my_list if num % 2 == 0]

# Define a function that takes in a string and a character, and returns the number of times that character appears in the string
def count_char(my_string, char):
    return my_string.count(char)

# Define a function that takes in a list of strings and returns a new list with the strings sorted in alphabetical order
def sort_strings(my_list):
    return sorted(my_list)

# Define a function that includes another function
def greet(name):
    """
    This function greets the person passed in as a parameter.
    
    Parameters:
    name (str): The name of the person to be greeted.
    
    Returns:
    str: The greeting message.
    """
    def get_message(name):
        """
        This function returns the greeting message.
        
        Parameters:
        name (str): The name of the person to be greeted.
        
        Returns:
        str: The greeting message.
        """
        return "Hello " + name + ". How are you today?"
    
    return get_message(name)

print(greet("John"))
# Output: "Hello John. How are you today?"