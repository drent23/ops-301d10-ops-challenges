#!/usr/bin/env python3

# Assign to a variable a list of 10 string elements
grocery_list = ["chicken", "bananas", "cereal", "oatmilk", "apples", "grapes", "tomatoes", "juice", "bread", "bleach"]
print("I have to get 10 things from the grocery store.  They include: ", grocery_list)

# Print the 4th element of the list
print("The 4th item on my grocery list is: ", grocery_list[3])

# Print the 6th through 10th elemnt of the list
print("The 6th through 10th items are: ", grocery_list[5:])

# Change the value of the 7th element to onion
grocery_list[6] = "onion"
print("I don't need tomatoes after all, but my wife asked me to add the following instead: ", grocery_list[6])

# Add/append to list
grocery_list.append("pie")
print("I have a sweet tooth so after adding something sweet my list now reads: ", grocery_list)

# Clear
print("If I take everything off the list, it looks like this: ", grocery_list.clear)

# Copy
print("Here's a copy of the list: ", grocery_list.copy)

# Count
print("This is how many boxes of cereal I need to get: ", grocery_list.count("cereal"))

# Extend
new_items = ["butter", "cilantro", "pretzels"]
grocery_list.extend(new_items)
print("I'm going to extend the list with a few more items: ", grocery_list)

# Index
print("Butter is at the following index on my list: ", grocery_list.index("butter"))

# Insert
grocery_list.insert(0, "mangos")
print("I need to make sure I don't forget my wife's favorite fruit so I'll put the following as the first thing on my list: ", grocery_list[0])

# Pop
print("I need to take off the last item of the list, so I'll remove: ", grocery_list.pop())

# Remove
grocery_list.remove("juice")
print("We don't need juice any more so now my list is as follows: ", grocery_list)

# Reverse
grocery_list.reverse()
print("If you want to see my list in reverse order, it's as follows: ", grocery_list)

# Sort
grocery_list.sort()
print("If you want to see my list in alphabetical order, it's as follows: ", grocery_list)