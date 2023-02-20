# Initialize an empty set
my_set = set()

# Add items to the set using the {} or the set() constructor
my_set = {1, 2, 3, 4}
my_set = set([1, 2, 3, 4])

# Check if an item is in the set using the in keyword
print(2 in my_set) # True

# Add an item to the set using the add() method
my_set.add(5)

# Remove an item from the set using the remove() method
my_set.remove(4)

# Get the length of the set using the len() function
print(len(my_set)) # 4

# Perform set operations
other_set = {3, 4, 5, 6}
union_set = my_set.union(other_set)
print(union_set) # {1, 2, 3, 4, 5, 6}
intersection_set = my_set.intersection(other_set)
print(intersection_set) # {3, 4}
