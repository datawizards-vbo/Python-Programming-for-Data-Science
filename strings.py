#String methods in Python:
# define a string
string = "This is a sample string for demonstration purposes."

# find method
print("find:", string.find("sample")) # returns the index of the first occurrence of the specified substring

# replace method
print("replace:", string.replace("sample", "test")) # returns a new string with all occurrences of the specified substring replaced by another substring

# upper method
print("upper:", string.upper()) # returns the string in uppercase

# lower method
print("lower:", string.lower()) # returns the string in lowercase

# split method
print("split:", string.split(" ")) # returns a list of substrings separated by the specified delimiter

# strip method
string2 = "  This is another string with leading and trailing whitespaces.  "
print("strip:", string2.strip()) # returns a new string with leading and trailing whitespaces removed

# capitalize method
print("capitalize:", string.capitalize()) # returns a copy of the string with only the first character capitalized

# startswith method
print("startswith:", string.startswith("This")) # returns True if the string starts with the specified substring, otherwise False
