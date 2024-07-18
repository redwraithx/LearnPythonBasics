from random import randint


# bools
# ex: not True ? False and "green" ? "red"
# true == true
# true == false
# false == true
# false == false


# flow - IF | ELSE
# if True:
#    "do stuff here"

# vid 47
print("Video 47")

veg = input("type the name of the vegetable: ")

if veg == "corn":
    print("the vegetable is corn")



# vid 48
print("Video 48")

if veg == "corn":
    print("corn 2")
else:
    print("the vegetable is not corn")


# vid 49
print("Video 49")

gpa = float(input("What was the application's grade point average: "))
inst_app = input("Is the student going to be educated at an approved institution? ")

if gpa >= 3.7:
    if inst_app == "yes":
        print("the applicant qualifies for a low APR student loan.")
    else:
        print("The applicant does not qualify since they have not been accepted into an approved institution.")
else:
    print("The applicant did not have high enough grades to qualify.")


# PROGRAMMING CHALLENGE: Grade Determiner

# Professor Fuentes teaches a Python class and uses the following grading scale for all of her exams.
# You work as a teacher's assistant and due to her busy schedule she has requested that you write a
# program which will determine the grades of the class's students.

# Her grading scale is as follows:

# A score of 90 or above is an A
# A score of 80 or above is a B
# A score of 70 or above is a C
# A score of 60 or above is a D
# A score any lower is an F

# For this exercise, start by creating a variable and assigning that variable a student's score as an
# integer using input().
score = int(input("Enter a students score: "))

# Then, using nested if and else statements and the following set of rules, determine and then display the
# student's grade along with their score using print().

# If the student's score is greater than or equal to 90, then the student will receive an A grade.
if score >= 90:
    print("Grade A")
# Otherwise, if the student's score is greater than or equal to 80, then the student will receive an B grade.
else:
    if score >= 80:
        print("Grade B")
# Otherwise, if the student's score is greater than or equal to 70, then the student will receive an C grade.
    else:
        if score >= 70:
            print("Grade C")
# Otherwise, if the student's score is greater than or equal to 60, then the student will receive an D grade.
        else:
            if score >= 60:
                print("Grade D")
# Otherwise, the student will receive an F grade.
            else:
                print("Grade F")
# Make sure to run your program multiple times and test it with values for each 5 of the different grades to
# make sure that the correct output is displayed for any value entered as a student's score.



# using the if and else if
test_num = 6

if test_num == 5:
    print("Number == 5")
elif test_num > 5:
    print("Number is > 5")
else:
    print("was not 5 or greater")



# PROGRAMMING CHALLENGE: Roman Numeral Equivalent

# For this exercise, start by creating a variable and assigning it a randomly generated integer
# between and inclusive of both 1 and 10.
num_1 = randint(1, 10)


def get_text(p1, p2):
    return "the roman numeral equivalent of " + str(p1) + " is " + p2 + "."


# Then, using your knowledge of if, elif, and else statements, create a program which prints the
# roman numeral equivalent of the randomly generated number.
if num_1 == 1:
    print(get_text(num_1, "I"))
elif num_1 == 2:
    print(get_text(num_1, "II"))
elif num_1 == 3:
    print(get_text(num_1, "III"))
elif num_1 == 4:
    print(get_text(num_1, "IV"))
elif num_1 == 5:
    print(get_text(num_1, "V"))
elif num_1 == 6:
    print(get_text(num_1, "VI"))
elif num_1 == 7:
    print(get_text(num_1, "VII"))
elif num_1 == 8:
    print(get_text(num_1, "VIII"))
elif num_1 == 9:
    print(get_text(num_1, "IX"))
else:
    print(get_text(num_1, "X"))
# For example, if the randomly generated integer was 9, then the program would say that the
# roman numeral equivalent of 9 is IX in the output.


# truthy and falsey values
# Vid 55
print("Video 55")

strings_example = input("Enter any string other than an empty one: ")

if strings_example:
    print("Thank you for entering something.")
else:
    print("you did not enter a string.")
