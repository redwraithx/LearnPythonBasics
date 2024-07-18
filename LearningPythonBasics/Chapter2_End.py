
# int from user input

user_int = int(input("Please enter an integer: "))
print(user_int)
print(type(user_int))

# possible outcomes from using int on input data

# int("numb3rs 4nd $ymbols!")   == Error
# int("1.59")                   == Error
# int(11.9)                     == Nearest integer that is less than or equal to float
# int(10.1 + 9.3")              == Error
# int(10.1 + 9.3)               == Nearest integer that is less than or equal to float


# float from user input

user_float = float(input("Please enter a float: "))
print(user_float)
print(type(user_float))

# possible outcomes from using float on input data

# float("numb3rs 4nd $ymbols!")     == Error
# float("1")                        == float
# float(1)                          == float
# float(10 + 9")                    == Error
# float(10 + 9)                     == float


# Exercise int()

# In a Python file, use input() to ask the user to enter an integer that 10 will be added to.
# Assign what they type to a variable.
int_var0 = int(input("Enter an integer that will be added to 10: "))
print(type(int_var0))

# print() the sum of the integer they entered and 10.
print("10 + " + str(int_var0) + " = " + str(int_var0 + 10))
