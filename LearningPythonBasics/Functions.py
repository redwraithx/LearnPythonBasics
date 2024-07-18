
# simple function and calling it twice
def prints_four():
    print("this")
    print("is")
    print("an")
    print("Example")


prints_four()
prints_four()


# def function_name():
#   content within function
# NOTE: Make sure to have 2 blank lines after each function
def function_name():
    print("\nFunction no parameters or return value\n")
    print(2 + 2)


# NOTE: Make sure to have 2 blank lines after each function
function_name()


# ==========================================================

# functions with parameters
def function_name(parameter):
    print("\nFunction with parameters but no return value\n")
    print(parameter + 2)


# NOTE: Make sure to have 2 blank lines after each function
function_name(8)


def function_name(p1, p2, p3):
    print("\nFunction with Multiple paramters but no return value\n")
    print(p1,  str(p2), p3)
    # NOTE: can use comma's in place of + but it also will add a space


# NOTE: Make sure to have 2 blank lines after each function
function_name("The Number", 5, "is an integer.")
# ===============================================================

# function with default parameters
def function_name(num1=7, num2=8):
    print("\nFunction with multiple parameters with default values but no return value\n")
    print(num1 * num2)


# NOTE: Make sure to have 2 blank lines after each function
function_name(2, 2)
function_name(2)
function_name()


# =========================================================================

# function with return value
def function_name(num1=7, num2=8):
    print("\nFunction with Multiple parameters with default values and returns the value\n")
    return num1 * num2


# NOTE: Make sure to have 2 blank lines after each function
print(function_name())
print(function_name(2))
print(function_name(10, 10))


# ===========================================================================

# function exercise

# Create a function called hello_world_printer() which takes no parameters and prints the string "hello world"
def hello_world_printer():
    print("hello world")


# Call the function hello_world_printer()
hello_world_printer()


# function exercise 2

# Create a function called name_printer which takes 1 parameter and prints it
def name_printer(p1):
    print(p1)


# Create a variable called name and assign it user input().  input()'s message should ask the user to enter their name.
name = str(input("Enter your name: "))


# Call name_printer() with the variable "name" as its argument.
name_printer(name)

# ===================================================
# PROGRAMMING CHALLENGE: Volume of a rectangular prism

# For this programming challenge, you will be creating a function that calculates the volume of a rectangular
# prism in cubic feet.  The formula to find the volume of a rectangular prism is V = l * w * h where l, w,
# and h are length, width, and height, respectively.

# First, create three variables representing length, width, and height.   Assign each of them an integer as user
# input using the input() function and int().
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))


# Next, create a function to calculate the volume of the rectangular prism.  It should have 3 parameters
# representing length, width, and height and return the volume of a rectangular prism calculated using
# those 3 parameters.
def calculate_rectangular_prism(p1, p2, p3):
    return p1 * p2 * p3


# Finally, use print() to display "The volume of the rectangular prism is [call function  here to calculate volume]
# cubic feet." in the output.  You will have to use str() on the function call to be able to concatenate it with
# strings since it returns an integer.
print("The volume of hte rectangular prism is", calculate_rectangular_prism(length, width, height), "cubic feet.")


# ==============================================
# PROGRAMMING CHALLENGE: Celsius to Fahrenheit

# The formula for converting from degrees Celsius to degrees Fahrenheit is as follows:
# F = 1.8 * C + 32

# Where F is the Fahrenheit temperature and C is the Celsius temperature.

# In a .py file, create a variable and assign it an integer representing a celsius temperature that is
# entered as user input().  input()'s message should prompt the user to enter an integer value.
celsius = int(input("Enter the temperature in celsius: "))

# For this programming challenge, you will then write a function called fahrenheit that takes in an integer
# representing a Celsius temperature as its argument.  The function will return the Fahrenheit equivalent
# temperature of that argument to 1 place after the decimal.
def fahrenheit(celsius_num):
    return round(1.8 * celsius_num + 32, 1)


# At the end of your program, display the Fahrenheit equivalent in a print statement message formatted like so:
# "The Fahrenheit equivalent of [user entered integer] degrees Celsius is [number returned by function]".
print("The Fahrenheit equivalent of", celsius, "degrees Celsius is", fahrenheit(celsius))

# To make sure that the function works, run your program multiple times and call the function on different user
# entered integer values both negative and positive.
celsius = int(input("Enter the temperature in celsius: "))
print("The Fahrenheit equivalent of", celsius, "degrees Celsius is", fahrenheit(celsius))


