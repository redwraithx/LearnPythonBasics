# Tuples
# NOTE: Tuples are a immutable data type


# examples of tuples:
tuple_1 = ("a", "b", "c", "d", "e")
tuple_2 = (2.718, False, [1, 2, 3])
tuple_3 = (1, 1, 0, 0, 0)

# items in the tuples can be different data types or the same
# you can have multiple instances of the same item within a tuple, like in tuple_3

# there are 2 ways to create a tuple
# using parenthisis enclose a group of items
tuple_4 = (5, 4, 3, 2, 1)

# OR, use the tuple function
# NOTE: that strings entered into the tuple() function will be broken up into characters each being its own item
tuple_5 = tuple([3.14, 2.205, 10])
tuple_6 = tuple("edcba")
print(tuple_5)
print(tuple_6)

# you can use a dictionary of using a tuple() function
# NOTE: Only the keys are made into tuples so the values are lost
tuple_7 = tuple({"a": 1, "b": 2, "c": 3})
print(tuple_7)

# you can access the index of a tuple just like a list or dictionary using the format: tuple_name[index]
tuple_8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_8[2])

# you can slice tuples just like strings, returning a tuple
print(tuple_8[:8])
print(tuple_8[2:7])
print(tuple_8[3:])


# examples of things that won't change that would work in a tuple are:
# Days of the Week
# Seasons of the Year
# Alphabet

# tuples take up less space in memory than say a list
tuple_9 = (1, 3, 5)
list_1 = [1, 3, 5]
print(tuple_9.__sizeof__(), "BYTES")
print(list_1.__sizeof__(), "BYTES")

# a good use of a tuple is a key in a dictionary
occupations = {("Angus", "Young"): "musician",
               ("Narendra", "modi"): "prime minister",
               ("Richard", "Branson"): "entrepreneur",
               ("Quentin", "Tarantino"): "filmmaker"}

seven_wonders = {("29,58'44\"N", "31,08'02\"E"): "The Great Pyramid of Giza, Egypt",
                 ("33,13'23\"N", "43,40'45\"E"): "Hanging Gardens of Babylon",
                 ("37,38'18\"N", "21,37'47\"E"): "Archaeological Site of Olympia, Greece",
                 ("37,55'33\"N", "23,59'36\"E"): "Temple of Artemis at Ephesus",
                 ("37,02'16\"N", "27,25'26\"E"): "Mausoleum at Halicarnassus",
                 ("36,26'02\"N", "28,13'03\"E"): "Rhodes, Greece",
                 ("31,12'51\"N", "29,53'28\"E"): "Lighthouse of Alexandria, Egypt"}

print("occupations:", occupations)
print("seven wonders:", seven_wonders)


# Video 108
print("\nVideo 108 - Iterating a tuple\n")

# iterating a tuple is the same as iterating a list
major_cities = ("Tokyo", "London", "New York", "Shanghai", "Sydney")

print("\nFor loop")
for city in major_cities:
    print("city:", city)

print("\nwhile loop")
# while loop
count = 0
while count < len(major_cities):
    print("city:", major_cities[count])
    count += 1

print("\nBackward city list in for loop")
for city in major_cities[len(major_cities) - 1::-1]:
    print("city:", city)

print("\nBackward city list in while loop")
backwards = len(major_cities) - 1
while backwards >= 0:
    print("city:", major_cities[backwards])
    backwards -= 1

print("\n")

# tuple slicing with step
# VERY IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# stride length of 3
print(ints[::3])
# evens only
print(ints[1::2])
# backwards from 8
print(ints[7::-1])
# odds only backwards
print(ints[8::-2])


# Video 109
print("\nVide 109 - Tuple Methods")

nested = (1, 2, 3, (4, 5, 6), (7, 8, 9), (10, 11, 12))
print(nested[4])
print(nested[5][1])


# .count()
# counts the occurrence of an item within the tuple
repeat = (7, 3, 3, 3, 0, 0, 7, 0, 0)
print(repeat.count(7))
print(repeat.count(3))
print(repeat.count(0))

# .index()
# NOTE: you will get an error if you call something that is not in the tuple

ints = (1, 1, 7)
print(ints.index(7))
print(ints.index(1))

