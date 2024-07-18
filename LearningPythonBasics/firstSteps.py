print("hello world")

Var_1 = 1
Var_2 = 2.0
Var_3 = True
print(Var_1)

Var_1 = 3

print(Var_1)
# testing comment


# Exponentation = 4 ** 4 = 246
exponentation = 4 ** 4
print("Exponentation: " + exponentation.__str__())

# Floor_division = 16 // 5 = 3
floor_division = 16 // 5
print("floor division: " + floor_division.__str__())

# Modulo = 7 % 3 = 1
modulo = 7 % 3
print("Modulo: " + modulo.__str__())


# math operator precedence
# in order of precedence
# =======================
# ()
# %, /, //, and *
# + and -

# example
Expression = (9 - 7) * 2 ** 3 + 10 % 6 // -1 * 2 - 1
# step 1: 2 * 2 ** 3 + 10 % 6 // -1 * 2 - 1
# step 2: 2 * 8 + 10 % 6 // -1 * 2 - 1
# step 3: 16 + -8 - 1
# step 4: 7
print("Expression: " + Expression.__str__())


# Exercises 2.8
print("Exercises 2.8")

# Create a variable and assign it the sum of two integers
var2_8_1 = 2 + 3
print(var2_8_1)

# Create a variable and assign it the difference of two integers
var2_8_2 = 10 - 8
print(var2_8_2)

# Create a variable and assign it the result of one integer being divided by another integer
var2_8_3 = 1000 / 10
print(var2_8_3)

# Create a variable and assign it the product of two integers
var2_8_4 = 7 * 5
print(var2_8_4)

# Create a variable and assign it the result of 3 raised to the 8th power
var2_8_5 = 3 ** 8
print(var2_8_5)

# Create a variable and assign it the result of 10 floor division 3
var2_8_6 = 10 // 3
print(var2_8_6)

# Create a variable and assign it the integer 2 using the expression 17 modulo [number]
var2_8_7 = 17 % 15
print(var2_8_7)


# exercise 2.11
print("Exercise 2.11")

var2_11_1 = 21
print(var2_11_1)
print(True)
print(3 ** 3 % 17)


# add 1.23 + 2.80
print(1.23 + 2.80)
# results are close but not correct = 4.029999999999999 (approximation errors)

# alternative is to use Integers
# add 123 + 280, then divide by 100 = 4.03
print((123 + 280) / 100)

# round() can fix the approximation errors
# round(expression, number of decimel places
print(round(1.23 + 2.80, 2))


# programming challenge: Grocery Store purchase
print("Grocery Store Purchase Challenge")

print(round(12.68 + 6.98 + 12.78 + 15.26 + 3.0 + 4.39, 2))


# strings are made of a array items
var_2_17_0 = "orange"
print(var_2_17_0[2])
print("apple"[4])


var_2_17_1 = "apricots"
print(var_2_17_1[:3]) # begining slice to index - 1
print(var_2_17_1[2:5]) # index to index - 1
print(var_2_17_1[4:]) # index to end of string (includes last character)


# Exercises 2.18
print("Exercises 2.18")

# Create a variable and assign it the string "Just do it!"
var_2_17_2 = "Just do it!"

# Access the "!" from the variable by index and print() it
print(var_2_17_2[10:])
# NOTE: this would work also for single characters
print(var_2_17_2[10])


# Print the slice "do" from the variable
print(var_2_17_2[5:7])

# Get and print the slice "it!" from the variable
print(var_2_17_2[8:])

# Print the slice "Just" from the variable
print(var_2_17_2[:4])

# Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".
# Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.
print("Don't " + var_2_17_2[5:])


# using the TYPE function returns the type of value something is
# str = string
# int = integer
# bool = boolean
print(type(var_2_17_2))

# using STR function converts type to string
# str(2) = "2"
# str(6.55) = "6.55"
print(str(6.55))

# new line = \n
print("Line one\nLine two")


# Exercises 2.22
print("Exercises 2.22\n")

# Create a variable and assign it a float
var_2_22_0 = 42.0

# Use print() and type() to print the data type of the variable in the output
print(type(var_2_22_0))

# Use str() on the variable from step 1 and concatenate it with the string " is a float." then use print() to display the result
print(str(var_2_22_0) + " is a float")

# print() the string "Hello, I'm [name], it's nice to meet you!"
# including quotes (you will need to use the \' or \" escape sequence depending on whether you enclose your strings in single quotes or double quotes.)
print("Hello, I'm Brian, it's nice to meet you!")


# Programming Challenge: Asterisk
print("Programming Challenge: Asterisk")

# Using your knowledge of escape sequences,
# create a single print() statement with single string inside of it that displays this when the program is run:
# *******
#  *****
#   ***
#    *

print("*******\n *****\n  ***\n   *")


# taking input from user like: name = input("enter your name: ")
var_2_26_0 = input("Enter your name: ")
print("Your name is " + var_2_26_0 + ".")
print(type(var_2_26_0))


# Programming Challenge: Monty Python
print("Programming Challenge: Monty Python\n")

# In a .py file, create a program and use input() three times to get answers to the following questions from a user.  \
# Store each of the answers in a variable.

# What is your name?
var_2_27_0 = input("What is your Name: ")

# What is your quest?
var_2_27_1 = input("What is your Quest: ")

# What is your favorite color?
var_2_27_2 = input("What is your favorite color: ")

# Then, concatenate everything into a string within a print() statement with the form "So your name is [name],
# your quest is [quest], and your favorite color is [color]."
print("So your name is " + var_2_27_0 + ", your quest is " + var_2_27_1 + ", and your favorite color is " + var_2_27_2 + ".")

