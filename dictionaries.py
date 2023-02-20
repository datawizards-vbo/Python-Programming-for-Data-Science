# Initialize an empty dictionary
my_dict = {}

# Add key-value pairs to the dictionary using the {} or the dict() constructor
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict = dict(a=1, b=2, c=3)

# Access values in the dictionary using keys
value = my_dict['a']
print(value) # 1

# Use the get() method to access values without raising an error if the key doesn't exist
value = my_dict.get('d')
print(value) # None

# Update the value of a key
my_dict['a'] = 4
print(my_dict) # {'a': 4, 'b': 2, 'c': 3}

# Remove a key-value pair from the dictionary
del my_dict['b']
print(my_dict) # {'a': 4, 'c': 3}

# Check if a key is in the dictionary using the in keyword
print('a' in my_dict) # True

# Get the length of the dictionary using the len function
print(len(my_dict)) # 2


############################
# Dictionary methods:
############################

# Initialize a dictionary with some key-value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Use the clear method to remove all key-value pairs from the dictionary
my_dict.clear()
print(my_dict) # {}

# Use the copy method to create a shallow copy of the dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = original_dict.copy()
print(new_dict) # {'a': 1, 'b': 2, 'c': 3}

# Use the fromkeys method to create a new dictionary with the specified keys and value
keys = ['a', 'b', 'c']
default_value = 0
my_dict = dict.fromkeys(keys, default_value)
print(my_dict) # {'a': 0, 'b': 0, 'c': 0}

# Use the get method to access values without raising an error if the key doesn't exist
value = my_dict.get('a', 'Key not found')
print(value) # 0

# Use the items method to return a new object of the dictionary's items in (key, value) format
items = my_dict.items()
print(items) # dict_items([('a', 0), ('b', 0), ('c', 0)])

# Use the keys method to return a new object of the dictionary's keys
keys = my_dict.keys()
print(keys) # dict_keys(['a', 'b', 'c'])

# Use the pop method to remove a key-value pair from the dictionary
value = my_dict.pop('a', 'Key not found')
print(value) # 0
print(my_dict) # {'b': 0, 'c': 0}

# Use the popitem method to remove and return an arbitrary (key, value) pair
key, value = my_dict.popitem()
print(key) # 'b'
print(value) # 0

# Use the setdefault method to set the value of a key if it doesn't already exist
value = my_dict.setdefault('b', 0)
print(value) # 0

# Use the update method to add key-value pairs from another dictionary
other_dict = {'d': 4, 'e': 5}
my_dict.update(other_dict)
print(my_dict) # {'c': 0, 'd': 4, 'e': 5}

# Use the values method to return a new object of the dictionary's values
values = my_dict.values()
print(values) # dict_values([0, 4, 5])
