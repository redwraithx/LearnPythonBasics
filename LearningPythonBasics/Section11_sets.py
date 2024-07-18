# sets are like a list, except they have 2 differences
# 1) they are unordered
# 2) they can not have duplicate items

# there are 2 ways to create sets
# 1) using { }
# also called a literal set
set_1 = {9, 8, 7, 6}
print(set_1)

# 2) using the set() function
set_2 = set({"a", "b", "c", "d", "e"})
print(set_2)

# we can create an empty set using the set() with no arguments
set_3 = set()
print(set_3)

# or us range within the set() with 3 variables
# start, stop & step
set_4 = set(range(1, 12, 2))
print(set_4)

# set can hold items of different item types
set_5 = {"a", 3.14, 18, True}
print(set_5)


# unlike lists or tupes, sets can NOT access the items by index, you can use a for loop
set_6 = {3, 6, 9, 12, 15}

for num in set_6:
    print(num)

# check if a value is in the set by using the in keyword
print(12 in set_6)
print(10 in set_6)


# if we had a list of places, that appear multiple times but maybe we only want to see items once.
# you can use a set to print those values without any duplicates
my_cities = ["halifax", "dartmouth", "halifax", "vancouver", "surrey", "kamloops", "chilliwack", "halifax", "kamloops"]
print(my_cities)
print(len(my_cities))
print(set(my_cities))
print(len(set(my_cities)))

# you can convert this set into a new list
print(list(set(my_cities)))
print(len(list(set(my_cities))))


# Set Methods
# add, remove, discard, clear, copy, union, intersection, difference

scifi = {"star trek", "star wars", "halo"}

# .add()
# NOTE: adding an item that is already in the list will do nothing and give no error message
scifi.add("mass effect")
print(scifi)

# .remove() & discard
# NOTE: removing an item that does not exist will give an error
# NOTE: Discard will not give an error when removing an item that does not exist in the set
scifi.remove("halo")
print(scifi)
scifi.add("halo")
print(scifi)
scifi.discard("halo")
print(scifi)
scifi.discard("halo")
print(scifi)


# .clear()
# clears the set of all items
scifi.clear()
print(scifi)

# .copy()
mountains = {"Everest", "Kilimanjaro", "fuji"}
set_7 = mountains.copy()
print("of the same set:", set_7 is mountains)
print(set_7)


# .union()
# combines sets into 1 set
set_8 = {1, 2, 3, 4, 5}
set_9 = {6, 7, 8, 9, 10}
set_10 = set_8.union(set_9)
print(set_8)
print(set_9)
print(set_10)

# you can use the pipe character | to combine sets also
set_11 = set_8 | set_9
print(set_11)


# .intersection()
set_12 = {4, 5, 6, 7, 8}
set_13 = {6, 7, 8, 9, 10}
set_14 = set_12.intersection(set_13)
print(set_14)

# you can also use the & to get the intersections of sets
set_15 = set_12 & set_13
print(set_15)


# . subtraction & .difference()
set_16 = set_13 - set_13
print(set_16)

set_17 = set_13.difference(set_12)
print(set_17)
set_18 = set_12.difference(set_13)
print(set_18)


# set comprehension
# Example:
# NOTE: math opperators should have NO Spaces
# action: even+2, loops over range(start, stop, step)
comp_1 = {even+2 for even in range(2, 11, 2)}
print(comp_1)

# NOTE: that items in this new set comp_2 will be random as sets are unordered
comp_2 = {char.lower() for char in "ALLCAPS"}
print(comp_2)


