# Loops


# while loop needs
# condition like a variable that changes
# counter = 0
#
# the loop its self will test the condition
# while counter < 3:
#   print("something")
#   counter += 1
print("Video 56 - while loop")

counter = 0

while counter < 3:
    print(counter, "- something")
    counter += 1


# while loop Exercise
print("\nExercise while loop")
# Create a loop that will print out numbers 10 to 1 in descending order.
# each number will be on its own line.

# variable = 10
counter = 10

while counter > 0:
    print(counter)
    counter -= 1


# PROGRAMMING CHALLENGE: Sum of Numbers From A Positive Integer
print("\nProgramming Challenge")

# Write a program which gets a positive integer from a user using input() and assigns it to a variable.
result = 0
init_value = value = int(input("Enter a positive Integer: "))

# The program should then use a while loop to get the sum of all the integers from the integer that was
# entered by the user down to 1.  For example, if the integer entered by the user was 6, the while loop would
# find the sum of 6, 5, 4, 3, 2, and 1, which is 21.
while value > 0:
    result += value
    value -= 1

# At the bottom of your program create two print statements.  One will display the user entered integer and the
# other will display the sum found by the while loop.
print("Initial Value: ", init_value)
print("Sum:", result)


# Video 61
print("\nVideo 61")

# for loop

# thing to iterate through
word = "house"

# the for loop, for letter in word:
# letter is current iterator from the item were iterating through word
for letter in word:
    print(letter)


# For loop Exercise
print("\nFor Loop Exercise")

# Use a for loop to print each letter from the string "hello world".
word = "hello world"

for letter in word:
    print(letter)


# PROGRAMMING CHALLENGE: Find the Number of Characters in A String
print("\nProgramming Challenge")

# In a .py file, write a program which calculates the number of characters in a string.
# The string should be entered using input() and assigned to a variable.
word = str(input("Enter a string: "))

counter = 0
for letter in word:
    counter += 1
    # print(letter, counter)

# Use print() twice at the end of your program.  The first print() will print the string that the user
# entered and the second print() will display the number of characters in the string.  For example, if
# the user entered the string "hello world", the number of characters would be 11.
print("you entered:", word)
print("your word is", counter, "in length.")


# Range()
print("\nVideo 66")

one_input = range(5)

for num in one_input:
    print(num)

print(type(one_input))


# example 2

two_inputs = range(5, 10)

for num in two_inputs:
    print(num)

# same type
print(type(two_inputs))


# example 3

# 3 paramaters in order: 1 = initial number, 20 = ending number, 3 = step size
# step size is initial number + step size. so 1 + 3 = 4
three_inputs = range(1, 20, 3)

# NOTE: this will only print numbers within the range of 1 to 20
for num in three_inputs:
    print(num)


# PROGRAMMING CHALLENGE: Fizz Buzz
print("\nProgramming Challenge: Fizz Buzz")


# Write a program that iterates over the integers 1 through 50 using a loop.

# However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the output.  For example,
# 15 is divisible by both 3 and 5, so instead of printing 15, print "FizzBuzz".  For numbers which are
# multiples of 3 but not 5 (such as 42) print “Fizz” instead of the number.  For the numbers that are
# multiples of 5 but not 3 (such as 20) print “Buzz” instead of the number.

# All the integers which are not multiples of 3 or 5 should just be printed as themselves.

values = range(1, 51)

for num in values:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# PROGRAMMING CHALLENGE: Factorial
print("\nProgramming Challenge: Factorial")


# Create a function which takes one positive integer as its input and returns its factorial.
# recursive function
def factorial_recursive(param):
    results = 1
    # print(results)

    if param == 1:
        return results

    results *= param * factorial_recursive(param - 1)
    return results


# function that will use a for loop
def factorial(param):
    results = 1

    for item in range(param, 1, -1):
        results *= item

    return results


# To make sure that your function works correctly, you should call it with the inputs 3, 4, and 5 and
# print what is returned by those calls.  For those inputs, you should get 6, 24, and 120, respectively.

print(factorial(3))
print(factorial(4))
print(factorial(5))

# NOTE: I struggled on this as i did not understand how factorials worked...
#       spend only a few minutes trying to understand the thing, else look up what the thing
#       is in its simplest form to save time
