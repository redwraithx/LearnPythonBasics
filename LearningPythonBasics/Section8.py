import copy

# lists

# items in list but be seperated by a comma and a space

# examples of valid lists
example_list_1 = [5, 4, 3, 2, 1]
example_list_2 = [2.123, 4.2342, 234234.1]
example_list_3 = ["blue", "red", "green", "Purple"]
example_list_4 = [True, False, False, True, True, True, False]
example_list_5 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
example_list_6 = [10, 3.2345, "tree", False, [1, 2, 3]]

# returns a list that looks like: ['b', 'l', 'a', 'h']
print(list("blah"))

# look at list for an item
checked_list = [1, 2, 3, 4]
print(1 in checked_list)
print(8 in checked_list)

not_in_example = 9 not in checked_list
print(not_in_example)


# Intruduction to list exercises

# Create a variable and assign it a list that contains an integer, a float, a Boolean value, a string,
# and a list of 3 integers.
intro_list = [10, 3.14, False, "string", [1, 2, 3]]

# Create another variable and assign it a call of the list() function with a string as its argument.
intro_var = list("astring")

# Use the keyword "in" to check if the letter "e" is in the list assigned to the variable from step 2
# and print the result.
print("E:", "e" in intro_var)

# Use the keyword "not in" to check if the letter "a" is not in the list assigned to the variable from
# step 2 and print the result.
print("A:", "a" not in intro_var)


# Video 86
print("Video 86")

indexes_example = ["carpet", "hardwood", "linoleum"]
print(indexes_example[1])

# a list within a list, getting its element
indexes_example2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(indexes_example2[1][0])


# using items accessed by index in expressions
mixed = [False, 365, 4.24, "this is a string"]
print(mixed[2] + 1.76)
print("I have used \"" + mixed[-1] + "\" as an example too many times.")


# slicing a list
sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sliced[:4])
print(sliced[3:8])
print(sliced[6:])


# reassigning a list's items
example_reassign = [2, 4, 6, 8, 0]
print(example_reassign)
example_reassign[3] = 10
print(example_reassign)
example_reassign[1:4] = [3, 2, 1]
print(example_reassign)

# can also add to the list index that are not in the original list
example_reassign[4:7] = [7, 6, 5]
print(example_reassign)


# Indexes and list slicing exercises
print("Indexes and list slicing exercises")

# Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]
exercise_list = [[0, 2], [4, 6], [8, 10], [12, 14]]

# Access the first list from the list of lists in step 1 by index then print it.
print(exercise_list[0])

# Access the 14 from the list in step 1 then print it.
print(exercise_list[-1][1]) # shows 14, -1 is the inverse selection (last element)
print(exercise_list[3][1]) # these 2 prints are the same

# Create a second variable and assign it the list ["chair", "table", "desk", "lamp", "bed"]
exercise_list_2 = ["chair", "table", "desk", "lamp", "bed"]

# Use a negative integer to access "chair" from the variable in step 4 by index then print it.
print(exercise_list_2[-5])
print(exercise_list_2[0])

# Print "Most people own at least 2 chairs." by concatenating the 2 from the list in step 1 and the "chair"
# from the list in step 4 with "Most people own at least ", a space, and a period.
print("Most people own at least {} {}.".format(exercise_list[0][1], exercise_list_2[0]))

# Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]
exercise_list_3 = [0.98, 8.76, 6.54, 4.32]

# Print the slice [8.76, 6.54, 4.32] from the variable you created in step 7.
print(exercise_list_3[1:])

# Print the slice [8.76, 6.54] from the variable you created in step 7.
print(exercise_list_3[1:3])

# Print the slice [0.98, 8.76] from the variable you created in step 7.
print(exercise_list_3[:2])


# Video 89 - del and list methods
print("Video 89")

planets = ["pluto", "mars", "earth", "venus", "ice"]
print(planets)
del planets[0] # removed pluto
print(planets)

# alternative way to remove items
planets.remove("ice")
print(planets)

# if removing an item that appears multiple times from a list it will remove the first instance of that item
colors = ["blue", "red", "White", "blue", "Orange", "Blue"]
colors.remove("blue")
print(colors)

# del deletes an item found in a list using the index
# remove removes the item from the list using the item


# .append(item) to list
pets = ["cat", "dog", "parrot"]
print(pets)
pets.append("fish")
print(pets)

# .insert(index, item) to list
pets = ["cat", "dog", "parrot"]
print(pets)
pets.insert(1, "turtle")
print(pets)


# .sort()

# sorting list of all numbers
num_list = [2.718, 4, -19, 10000, 0]
print(num_list)
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print("Desending:", num_list)

# sorting list of all strings
str_list = ["Ringo", "John", "George", "Paul"]
print(str_list)
str_list.sort()
print(str_list)
str_list.sort(reverse=True)
print("Descending:", str_list)

# NOTE: sort() can not be used on Mixed lists as it would not know how to compare the items
# unless, the list has a list of only Integers, floats and booleans values
print("testing mixed list with int, bool and float")

mixed = [False, 5.67, -2]
mixed.sort()
print("Works:", mixed)

# using ASCIIbetical order, upper case letters come first
ASCIIbetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
print(ASCIIbetical)

ASCIIbetical.sort()
print(ASCIIbetical)
# checks using lowercase for example
ASCIIbetical.sort(key=str.lower)
print(ASCIIbetical)

metals = ["copper", "gold", "silver", "iron"]
print(metals)
# get the index of an item
print("Silver Index:", metals.index("silver"))
# get the index of item NOT in the list gives an error
#   print("Platinum Index:", metals.index("platinum"))

numbers = [4, 3, 2, 1, 0, 1, 2, 3, 4]
print(numbers)
print("number 3 index:", numbers.index(3))


# .pop() removes item and returns it to be used
bands = ["Queen", "Led Zepplin", "The Beatles", "MUSE", "Radiohead"]
print(bands)
# take last item of list out of list and place it into the variable end
end = bands.pop()
print(bands)
print(end)
#lets find "The Beatles" index and pop that item
end = bands.pop(bands.index("The Beatles"))
print(end)
print(bands)


# del and list methods exercises
print("del and list methods exercises")

# Create a variable called arctic_animals and assign it the
# list ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]

# Use del to remove "tiger" from the list assigned to arctic_animals.
del arctic_animals[4]

# Use the .remove() method to remove the string "elephant" from the list assigned to arctic_animals.
arctic_animals.remove("elephant")

# Use the .append() method to add the string "arctic fox" to the list arctic_animals.
arctic_animals.append("arctic fox")

# Use .insert() to insert the string "snowy owl" between the strings "polar bear" and "walrus" inside of arctic_animals.
arctic_animals.insert(2, "snowy owl")
print(arctic_animals)

# Use the .sort() method to rearrange the strings in arctic_animals into alphabetical order.
arctic_animals.sort()

# Use print() to display the list assigned to arctic_animals
print(arctic_animals)

# Use .index() to get the index number of "reindeer" from arctic_animals then print it.
print(arctic_animals.index("reindeer"))

# Use .pop() to get the last item from the list arctic_animals then print it.
print(arctic_animals.pop())


# List vs Strings
# both contain ordered items
# list = mutable, can reassign individual indexed items
# strings = immutable, can NOT be reassigned individual indexed items, you need to assign a whole new string to it.

ex_1 = [1, 2, 3]
ex_1[1] = 5
print("reassignment works:", ex_1)

ex_2 = "123"
print(ex_2)
# ex_2[1] = 5
# print("Reassignment would fail:", ex_2)
ex_2 = "153"
print("total reassignment works:", ex_2)

# it is better practice to use part of the original string as part of the new index with slicing
ex_2 = "new: " + ex_2[0] + "5" + ex_2[2]
print(ex_2)


# references, these lists use the same list
ex_9 = [1, 2, 3, 4, 5]
ex_10 = ex_9
ex_10[2] = 4
print(ex_9)
print(ex_10)

# deepcopy will allow you to make a copy of a list as a new list
ex_12 = [1, 2, 3, 4, 5]
ex_13 = copy.deepcopy(ex_12)
ex_13[2] = 5
print(ex_12)
print(ex_13)

# list line continuation, unlike other types which can NOT do this but there are exceptions
ex_15 = ["bush",
         "fern",
         "tree",
         "moss"]
print(ex_15)

# \ line continueation
ex_16 = 2 + \
        4 + \
        1
print(ex_16)

# \ line continuation with strings, do not add spaces if using this else they will be added to the string
ex_17 = "The Empire \
Strikes \
Back"
print(ex_17)

# concatenated string alignment, just align the quotes
ex_18 = "Hello " + \
        "World"
print(ex_18)


