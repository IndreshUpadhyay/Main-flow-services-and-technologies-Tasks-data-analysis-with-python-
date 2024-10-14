# Lists
print("Lists:")
my_list = [1, 2, 10, 14, 8]
print("Initial List:", my_list)

# Add element
my_list.append(20)
print("After adding 20:", my_list)

# Remove element
my_list.remove(1)
print("After removing 1:", my_list)

# Modify element
my_list[0] = 18
print("After modifying first element:", my_list)

# Dictionaries
print("\n Dictionaries:")
my_dict = {"name": "Indresh", "age": 22, "city": "Noida"}
print("Initial Dictionary:", my_dict)

# Add key-value pair
my_dict["country"] = "India"
print("After adding country:", my_dict)

# Initail Set
initial_set={1,2,3,4,5}

# After adding 6
initial_set.add(10)
print("After adding 6:", initial_set)

# Remove Element
initial_set.remove(1)
print("After removing 4:", initial_set)

# Union, intersection, and difference
my_set = {4, 5, 6, 7, 8}
set2 = {6, 7, 8, 9, 10}  # Define set2

print("Union:", my_set.union(set2))
print("Intersection:", my_set.intersection(set2))
print("Difference:", my_set.difference(set2))
