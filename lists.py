# Initialize an empty list
my_list = []

# Add items to the list using the append method
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list) # [1, 2, 3]

# Access items in the list using indexing
first_item = my_list[0]
print(first_item) # 1

# Use slicing to access a subset of the list
sublist = my_list[1:3]
print(sublist) # [2, 3]

# Use the + operator to concatenate lists
other_list = [4, 5, 6]
combined_list = my_list + other_list
print(combined_list) # [1, 2, 3, 4, 5, 6]

# Use the * operator to repeat a list
repeated_list = my_list * 2
print(repeated_list) # [1, 2, 3, 1, 2, 3]

# Check if an item is in the list using the in keyword
print(3 in my_list) # True

# Get the length of the list using the len function
print(len(my_list)) # 3

#############
#List Methods
#############

# Initialize a list with some items
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Use the append method to add an item to the end of the list
my_list.append(7)
print(my_list) # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 7]

# Use the insert method to insert an item at a specific position in the list
my_list.insert(3, 8)
print(my_list) # [3, 1, 4, 8, 1, 5, 9, 2, 6, 5, 3, 5, 7]

# Use the remove method to remove the first occurrence of an item from the list
my_list.remove(5)
print(my_list) # [3, 1, 4, 8, 1, 9, 2, 6, 5, 3, 5, 7]

# Use the pop method to remove and return the last item in the list
last_item = my_list.pop()
print(my_list) # [3, 1, 4, 8, 1, 9, 2, 6, 5, 3, 5]
print(last_item) # 7

# Use the index method to find the index of an item in the list
index = my_list.index(3)
print(index) # 0

# Use the count method to count the number of occurrences of an item in the list
count = my_list.count(5)
print(count) # 2

# Use the sort method to sort the items in the list in ascending order
my_list.sort()
print(my_list) # [1, 1, 2, 3, 3, 4, 5, 5, 5, 8, 9]

# Use the reverse method to reverse the order of the items in the list
my_list.reverse()
print(my_list) # [9, 8, 5, 5, 5, 4, 3, 3, 2, 1, 1]
