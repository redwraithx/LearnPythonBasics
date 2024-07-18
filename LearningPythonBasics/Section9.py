# Dictionary

# key value pairs
# variable = key: value
# NOTE: NO Space before the collen's
# NOTE: use comma's to separate sets of key value pairs
# NOTE: NO Spaces for the open { and closing} before the Quotes
# NOTE: Entries are CAse SensiTIVE, when wrong it would be looking for a different entry then the possible expected one

console = {"nintendo": "nes"}
print(console["nintendo"])
consoles = {"nintendo": "wii", "microsoft": "xbox", "sony": "playstation"}
print(consoles["microsoft"])

# you can even save entries as a variable
EntryVal = consoles["sony"]
print(EntryVal)
# using the string function .format() makes things look neat as well as very easy to read
print("The {} 4 is Sony's newest gaming console.".format(EntryVal))
# or old concatenation
print("The", EntryVal, "4 is Sony's newest gaming console.")


# Dictionaries are unordered
# meaning that [1, 2, 3] is NOT Equal to [3, 2, 1]
# order matters not the items
print("Ordered Comparison:", [2, 4, 6] == [2, 4, 6])
print("UnOrdered Comparison:", [2, 4, 6] == [6, 4, 2])


# Comparison example
first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
second = {2: 2.3, 0: 2.1, 3: 2.4, 1: 2.2}

# NOTE: that when comparing 2 or more dictionaries they must contain the same key, value pairs to be considered equal
# NOTE: They do not need to be in the same order for this comparison to equate to True
print("Comparing first & second, are they equal:", first == second)

# check if a key is in a dictionary using the following
# returns True if found and False if not (also avoids errors with key not found)
print("Does Exist in dictionary:", 0 in first)
print("Does Exist in dictionary:", 5 in first)

# to check if a key is not in a Dictionary us the 'not in" key
print("is 1 not in dictionary?", 1 not in first)
print("is 11 not in dictionary?", 11 not in first)


# Intro to Dictionaries Exercises
print("Intro to Dictionaries Exercises")

# create a variable and assign it a dictionary that has 5 key value pairs
val = {"brian": "Programmer", "natasha": "miracle worker", "john": "bc man",
       "albert": "retired", "john_h": "wood Carver"}

# print and access the value held at the third key in the dictionary
print("3rd key's value:", val["john"])

# use the in keyword to check if a key appears in the dictionary and print the result
print("In key to check if key is in dictionary:", 1 in val)

# use not in to check if a key does not appear in the dictionary and print the result
print("Not in key to check if key is not in dictionary:", 6 not in val)


# .keys()
print("Video 96")

birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print("Get Keys From Dictionary:", birth_years.keys())


for key in birth_years.keys():
    print("Dictionary Key:", key)


# .values()
print("Get values from dictionary:", birth_years.values())

for value in birth_years.values():
    print("Dictionary Value:", value)


# .items()
# this gets the keys and values at the same time
print("Get Keys & Values form dictionary:", birth_years.items())

print("\n")

for item in birth_years.items():
    print("Dictionary key,value:", item)

print("\n")

for key, value in birth_years.items():
    print("Dictionary key, value:", key, value)
    print("Dictionary key {}, value {}:".format(key, value))


# data type of the values
print("Dictionary Keys type:", type(birth_years.keys()))
print("Dictionary values type:", type(birth_years.values()))
print("Dictionary items type:", type(birth_years.items()))

# convert data to a list for use
print("Dictionary Keys list:", list(birth_years.keys()))
print("Dictionary values list:", list(birth_years.values()))
print("Dictionary items list:", list(birth_years.items()))


# check for a value within the dictionary
print("does natasha exist in the dictionary's values:", "natasha" in birth_years.values())
print("does elizabeth exist in the dictionary's values:", "elizabeth" in birth_years.values())


# .get()
# to avoid errors when checking items not in dictionary

# if & else is a way to do this but it is not efficient
if 1975 in birth_years:
    print(birth_years[1975])
else:
    print("1975 is not a key in birth_years.")


# USE THE .get() method instead
print(birth_years.get(1975, "1975 is not a key in birth years."))


# copies of a dictionary is still references the pointer of the original dictionary.
# use deepcopy for a truly new version


# using len() on a dictionary will get the number of key value pairs within
print("Dictionary len:", len(birth_years))


# Dictionary Methods 1 exercises
print("Dictionary methods 1 exercises")

# create a variable and assign it the following dictionary:
# {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean",
# "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
# make the dictionary span multiple lines so that the line the dictionary starts on is not too long.
my_dict = {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean",
           "The Betles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}

# print the length of the dictionary.
print("my_dict's key/value pairs:", len(my_dict))

# use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines.
print("keys:", my_dict.keys())

print("for loop keys")
for key in my_dict.keys():
    print("Key:", key)

# print all of the values from the dictionary using the .values() method.
print("Values:", my_dict.values())

print("for loop values")
for value in my_dict.values():
    print("Value:", value)

# use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.
print("keys & values of type items:", my_dict.items())

print("for loop keys & values as items")
for item in my_dict.items():
    print("item:", item)

print("for loop keys & values")
for key, value in my_dict.items():
    print("key:", key, "value:", value)

# use the .get() method to check the dictionary for the key
# "Promise of the Real"
# and create a message that will print if the key is not found in the dictionary.
song = "Promise of the Real"
print("Use .Get():", my_dict.get(song, "Failed to find {}".format(song)))


# Video 99
print("\nVideo 99")

# .fromkeys()
# .fromkeys() can have up to 2 parameters:
#   1) iterable value - can be a: List, String
#       these items are used as a key
#   2) value type: Bool, float, integer, List, String or dictionary (any value type)

# example using list:
# would return the value for each listed item
ex_1 = {}.fromkeys(["address"], "1600 Pennsylvania Avenue NW")
print("Example 1:", ex_1)

# example using a string
# would return the value for each character of the string
# duplicate characters are ignored
ex_2 = {}.fromkeys("addr", "1600 Pennsylvania Avenue NW")
print("Example 2:", ex_2)

# example using a list but with no value, returns None as a value
ex_3 = {}.fromkeys(["Brand"])
print("Example 3:", ex_3)


# .pop() on dictionaries must take a key to remove
ex_4 = {"make": "Honda", "model": "civic", "year": 2016}
print("Example before .pop(\"model\")", ex_4)
popped = ex_4.pop("model")
print("Example using .pop(\"model\"):", ex_4)
print("what was popped off the dictionary:", popped)

# NOTE: you will get a key error message if you try to pop something that does not exist in the dictionary

# .popitem()
# no argument required, and will remove the last item in the dictionary.
# NOTE: if used with an older version of python of 3.7 it will remove a random item in the dictionary
# NOTE: .popItem Takes 0 arguments and will get an error if you try use them
ex_5 = {"name": "bob", "age": 38, "occupation": "accountant", "workplace": "H&R block"}
print("before popitem():", ex_5)
ex_5.popitem()
print("after popitem():", ex_5)


# Dictionary method 2 exercises
print("\nDictionary method 2 exercises\n")

# use .fromkeys() to create a dictionary that has the consonants from the alphabet as its keys and the
# string "consonant" as the value for each of those keys.  Only use lower case letters for the consonants.
# "y" counts as a consonant for this exercise.  Use a for loop and the .items() method to print each of
# those key: value pairs on a different line.  For example, the first 3 lines in the output should be the following:
# b consonant
# c consonant
# d consonant
fromkeys_dict = {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")

for key, value in fromkeys_dict.items():
    print(key, value)

# paste this dictionary into your .py file then pop and print "Big Mac" from it
fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}

# use .popitem() to remove the last key: value pair from the dictionary assigned to fast_food_items then print
# new fast_food_items dictionary.
popped_item = fast_food_items.popitem()
print("new Fast food items:", fast_food_items)


# Dictionary Medthods 3:
#   .clear(), .copy(), and .update()
print("\nVideo 102\n")

# .clear()
# empties the dictionary
ex_6 = {1: "England", 2: "Scotland", 3: "Wales", 4: "Northern Ireland"}
print(ex_6)
ex_6.clear()
print(ex_6)

# .copy(),
# returns a copy of a dictionary but with its own references

# example of a shallow copy
print("birth years:", birth_years)
people = birth_years
people[1982] = "madeline"
print("birth years:", birth_years)
print("people: ", people)

# example of a deep copy
people[1982] = "elizabeth"
people = birth_years.copy()
people[1982] = "natasha"
print("birth years:", birth_years)
print("people:", people)

# .update()
# allows us to add key value pairs from one dictionary to another or overwrite values already within a dictionary
city_info = {"country": "Canada", "province": "Ontario", "city": "Toronto"}
population = {"population": 2930000}
# NOTE: gives a warning about it not being of the same data types in the city_info which is String, String...
# but will work
city_info.update(population)
print(city_info)
# .update does nothing to the original data that was added/updated
print(population)
# update the value to population
city_info["population"] = 3000000
print(city_info)
# reverts the data back to the original value
city_info.update(population)
print(city_info)

# .update() with no value will do nothing or remain unchanged

# dictionary methods 3 exercises
print("\nDictionary Methods 3 exercises\n")

# paste these 2 dictionaries into your file
internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}

# use .update() to add the contents of another_one to internet_celebrities.
internet_celebrities.update(another_one)

# create a variable and assign it a copy of internet_celebrities.
yet_another_one = internet_celebrities.copy()

# use the .clear() method to get rid of the contents of internet celebrities.
internet_celebrities.clear()

# print internet_celebrities.
print(internet_celebrities)

# print the variable you created in step 3.
print(yet_another_one)


# Dictionary Methods 4: .setdefault()
computers = {"Google": "ChromeBook", "Apple": "MacBook", "Microsoft": "Surface Pro"}

# we could manually add values for a key like this example:
if "Lenovo" not in computers:
    computers["Lenovo"] = "ThinkPad"

print(computers)

# we should possibly use .setdefault to give something a value when being added, for example:
computers.setdefault("Lenovo", "ThinkPad")
print(computers)

# calling setdefault again on something that is already been called but has a different value, it will not do anything
# same goes for something that existed before setdefault was called it would do nothing
computers.setdefault("Lenovo", "IdeaPad")
print(computers)

# example if something is already in the dictionary
computers.setdefault("Apple", "Macbook Pro")
print(computers)


# dict()
print("\nVideo 106 - dict()\n")

empty = dict()
print(empty)
# NOTE: make sure when adding items in dict(key=value, key=value, etc...)
# NOTE: that there can be NO SPACES before or after the =
# NOTE: that keys added with dict() must be created with
#       Letters, Numbers and Underscores only as they show up as a string
# NOTE: Make sure that the first item must NOT be a number
with_values = dict(a=1, b=2, c=3, d_1=4, e1=5, f_=6)
print(with_values)

