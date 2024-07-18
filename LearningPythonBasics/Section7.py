# strings

# .upper() & .lower()
# makes the string that .upper() or .lower()
print("UPPER:", "upper".upper())
print("upper:", "lower".lower())


# .isupper() & .islower()

# Must be all UPPER case letters for .isupper()
print("is not upper:", "is not upper".isupper())
print("ISUPPER:", "ISUPPER".isupper())

# MUST BE ALL LOWER CASE LETTERS FOR .islower()
print("IS NOT LOWER:", "IS NOT LOWER".islower())
print("islower:", "islower".islower())


# combining isupper and upper
print("IS UPPER?", "upper".upper().isupper())


# .isalpha()
print("is batman123 all letters:", "Batman123".isalpha())
print("is BatMan all letters:", "BatMan".isalpha())

# .isalnum()
print("is batman123 alpha &/or numerical:", "batman123".isalnum())
print("is 123 alpha &/or numerical:", "123".isalnum())
print("is Batman alpha &/or numerical:", "Batman".isalnum())


# .isdecimal()

# 123 is a decimal because it's a number but if you use it on a string with puncuation
# like 3.14 it will fail because it's a string not a number.
print("is 123 decimal:", "123".isdecimal())
print("is 3.14 decimal:", "3.14".isdecimal())

# this still fails as it would need to be converted to a string to use.
decimal_num = 3.14
print("is 3.14 decimal:", str(decimal_num).isdecimal())


# .isspace()
print("is space:", " ".isspace())
print("is space:", "                                 ".isspace())
print("is not space:", "               d                  ".isspace())


# .istitle()
print("is title:", "Super Smash Brothers: Ultimate!".istitle())
print("is not title:", "Super Smash Brothers: ultimate!".istitle())

# .title()
# this will make the string given title case
print("Make the great gatsby title cased:", "the great gatsby".title())


# .startswith() & .endswith()
# this will be case sensitive
# takes in an argument and tests that to see if it has the argument to test with.
print("does, this is a string. start with this:", "this is a string".startswith("this"))
print("does, this is a string. start with t:", "this is a string".startswith("t"))
print("does, this is a string. start with T:", "this is a string".startswith("T"))
print("does, this is a string. start with b:", "this is a string".startswith("b"))

# the final character must be included in the endswith
print("does, To Infinity and beyone! end with beyond!:", "To infinity and beyond!".endswith("beyond!"))
print("does, To Infinity and beyone! end with beyond:", "To infinity and beyond!".endswith("beyond"))


# .join()
# this only joins the included items within the bracket list. the string as part of the intake can apply an
# in between character addition to the join.
print("".join(["one", "two", "three"]))
print(" ".join(["one", "two", "three"]))
print(",".join(["one", "two", "three"]))
print(", ".join(["one", "two", "three"]))
print("...".join(["one", "two", "three"]))
print("join".join(["me"]))
print("this will add join in between each word joined:", "join".join(["me", "please"]))


# .split()

# created a list of the words seperated by spaces by default
print("Eggs, Milk, Waffles, Bacon".split())

# we can have it use different a seperator by entering it into the split parameters
# this example will add the string seperated by the comma but includes the space
print("Eggs, Milk, Waffles, Bacon".split(","))
# remove the comma and space from being added to the list
print("Eggs, Milk, Waffles, Bacon".split(", "))



# STRING METHODS 1 EXERCISES
print("String Methods 1 Exercises")

# Create a variable called mixed_case and assign it the string "A Song of Ice and Fire"
mixed_case = "A Song of Ice and Fire"

# Use .isupper() to check if mixed_case is a string of all upper case letters.  print() the result.
print("is stirng upper case:", mixed_case.isupper())

# Use .islower() to check if mixed_case is a string of all lower case letters.  print() the result.
print("is string lower case:", mixed_case.islower())

# Change all of the letters in mixed_case to upper case letters using .upper() and print() the result.
print("changed to upper:", mixed_case.upper())

# Change all of the letters in mixed_case to lower case letters using .lower() and print() the result.
print("changed to lower:", mixed_case.lower())

# Use the .istitle() method to check if mixed_case is title case and print the result.
print("is string a title:", mixed_case.istitle())

# Create a variable called title_case and assign it the result of .title() being called on mixed_case.
title_case = mixed_case.title()

# print() title_case
print(title_case)

# Call startswith() on mixed_case with the letter mixed_case starts with as its argument.  print() the result.
print("does title_case start with the letter", mixed_case[0] + ":", title_case.startswith(mixed_case[0]))

# Call endswith() on mixed_case with the letter mixed_case ends with as its argument.  print() the result.
print("does title_case end with the letter", mixed_case[len(mixed_case) - 1])

# Create a variable called words and assign it the result of split() being used on mixed_case.
words = mixed_case.split()

# print the variable "words"
print("mixed_case split into an array of words:", words)

# Use the .join() method to join together all of the items in the list assigned to words as a single string.
print("joining the words list into a single string:", "".join(words))

# Use .isalpha() to check if the string is made up entirely of letters.  Finally, use print() to display the result.
print("check if is joined words are is alpha:", "".join(words).isalpha())



# Video 74
print("Video 74")

# .rjust(param int)

# using .rjust on a string will add spaces to right justify the string so its a length of say 15
print("Hello World".rjust(15))

# as this string will be greater than 15 nothing is done
print("Hello _ _ _ _ _ _ _ _ _ _ _ _ _ World".rjust(15))

# .ljust(param int)
print("Hello World".ljust(15) + ".")

print("Hello _ _ _ _ _ _ _ _ _ World".ljust(15) + ".")


# with .rjust() & .ljust() you can add a single character if you want to use something other than a space
# .rjust(int, character) & .ljust(int, character)
print("Hello".rjust(15, "*"))
print("Hello".ljust(15, "*"))
print("Hello".rjust(15, "*").ljust(15, "*"))
print("Hello".rjust(15, "*").ljust(30, "+"))


# .center()
# adds characters on the left and right side of a string
print("Hello".center(15))

# also using a character on the same string
print("Hello".center(15, "^"))


# .strip()
# removes spaces from both sides of a string
# NOTE you can add a second argument as a character and will remove that type
print("1111111I had an exciting 1111 trip!!!11111111".strip("1"))

# .rstrip()
# removes spaces from the right side of a string
# NOTE you can add a second argument as a character and will remove that type
print("1111111I had an exciting trip!!!11111111".rstrip("1"))

# .lstrip()
# removes spaces from the left side of a string
# NOTE you can add a second argument as a character and will remove that type
print("1111111I had an exciting trip!!!11111111".lstrip("1"))


# you can remove multiple characters from a string
print("juice, bread, cheese, beef, bread".rstrip(", bread"))
# this also works, as it starts from the comma
print("juice, bread, cheese, beef, bread".rstrip(",ed arb"))

# .strip can also remove all characters from a string that is suppose to find until there are no characters to remove
print("blueblueblueyellowblue".strip("eulb"))


# .replace()
# will replace a string with a new string
print("Good morning.".replace("morning", "afternoon"))



# string methods 2 exercises
print("String Methods 2 exercises")

# Create a variable called the_string and assign it the string "North Dakota".
the_string = "North Dakota"

# Call .rjust() on the_string with 17 as its argument and print() the result.
print(the_string.rjust(17))

# Call .ljust() on the_string with the arguments 17 and "*" then print() the result.
print(the_string.ljust(17, "*"))

# Create a variable called center_plus and assign it the result of .center() being called on the_string
# with 16 and "+" as arguments.
center_plus = the_string.center(16, "+")

# Use print() to display the string assigned to center_plus.
print(center_plus)

# Call .lstrip() on the_string to remove "North" then print() the result.
print(center_plus.lstrip("North"))

# Call .rstrip() on center_plus with "+" as its argument and print() the result.
print(center_plus.rstrip("+"))

# Call .strip() on center_plus with "+" as its argument and print() the result.
print(center_plus.strip("+"))

# Call .replace() on the_string and replace "North" with "South".  print() the result.
print(center_plus.replace("North", "South"))


# Video 77
print("Video 77")

# len(argument)
# this will count string length, even on added strings and slices
print("Length:", len("Tree"))
print("Length:", len("This " + "is a " + "string."))
print("Length:", len("lsjdflsjkdfoiwejrlsjkdfisoerjwlekrj"[7:20]))


# PROGRAMMING CHALLENGE: String Reverser
print("Programming Challenge: String Reverser")

# For this challenge, you will be writing a program which uses a for loop to reverse a string.

# Start by creating a variable and assigning it a string as user input using input().
input_word = input("Enter a string to reverse: ")

# Use a for loop to reverse the string.  You will need to use range with all 3 inputs for this.  In addition,
# you should create a variable before the for loop and assign it an empty string.  The variable will be
# reassigned multiple times within the for loop and end up holding the new reversed string.
reversed_word = ""

# this using the length of the word to reverse - 1 as indexing starts at 0, want to stop when we hit -1,
# and we want to iterate through the word 1 letter at a time using -1 as were moving in reverse.
for letter in range(len(input_word) - 1, -1, -1):
    reversed_word += input_word[letter]

# Print the reversed string at the bottom of your program.
print(reversed_word)


# PROGRAMMING CHALLENGE: Word Counter
print("Programming Challenge: Word Counter")

# For this programming challenge, write a function in a .py file which takes 1 string as an argument,
# finds out the number of words in that string, then returns that number.

#answers solution
def word_counter(words):
    spaces_and_letters = ""
    word_count = 1
    for i in words:
        if i.isalnum() or i.isspace() or i == "-" or i == "'":
            spaces_and_letters += i
    for j in spaces_and_letters:
        if j == " ":
            word_count += 1

    return word_count


# remake of function
print("NEW")


# i was slightly off but only had to change 2 things and put back 1 to have it work was simple changes as well.
def count_words_in_string(words_string):
    counter = 1
    word = ""
    for x in words_string:
        if x.isalnum() or x.isspace() or x == "'" or x == "-":
            word += x

    for y in words_string:
        if y == " ":
            counter += 1

    return counter


# For example, if the program was used on the string "This is a string.", then the function would return 4.

# Assumptions:
# Assume that the string will be assigned to a variable and that it will contain at least 1 word.
# Assume that there will never be 2 or more consecutive spaces in a row within the string.

# Contractions and possessive words with an apostrophe like "it's" or "Brian's" count as 1 word.

# Hyphenated words like "ice-cream" count as 1 word.

# Numbers in the string such as the "007" in "James Bond is 007." count as words

# There will be no double quotes "" within in the string.

# Hints for this problem:

# Use string methods to filter out characters besides numbers, letters, spaces, apostrophes, and hyphens.

# Count the number of spaces in the filtered string and add 1 to that since the string will always contain at
# least 1 word.  This will give you the number of words it contains.

# You should test your program with many different strings.

# However, the strings that the solution code is being used on are the 3 strings below.

str_1 = "James Bond is 007."
str_11 = "James \ Bond- is 007"
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \ saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \ shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \ shrimp burger, shrimp sandwich. That- that's about it."

#solutions prints

print(count_words_in_string(str_1))
print(count_words_in_string(str_11))
print(count_words_in_string(str_2))
print(count_words_in_string(str_3))

# So, for your final solution, copy the above into your .py file and print() 3 calls of your function,
# once for each of the 3 variables above.


# .format()
print("Video 82")

name = input("What is the job applicant's name? ")
degree = input("What did they major in at college? ")
job = input("What is their current occupation? ")
experience = input("How many years have they been working in their field? ")

# bad version
print(name + " majored in:", degree, "works as a:", job, " and has", experience, "years of experience.")

# formatted version
print("{} majored in {}, works as a {}, and has {} years of experience.".format(name, degree, job, experience))

