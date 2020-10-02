# Task a
"""This program is for week 8 - Further Python functions, Python sampler: functions"""
horizontal_line = '-' * 15
print(horizontal_line)

# Task b
print("Create a function, that takes no parameter, returns no value")


def function_b():
    """This function takes in no parameters and returns no values,
    has a docstring to explain what it does,
    executes a loop to display something a fixed number of times,
    displays a message once after the loop finishes"""
    i = 0
    for x in range(0, 5):
        i += 1
        print(i)


print(function_b())
print("The loop inside the first function has be completed")
print(horizontal_line)

# Task c
print("Create a function, that takes a sequence parameter, returns each item in the sequence")


def function_c(loop_list=["H", "e", "l", "l", "o"]):
    """This function takes in a sequence parameter and returns each item in the sequence
    :param loop_list
    :rtype object"""

    i = 0
    for _ in loop_list:
        print(loop_list[i])
        i += 1


print(function_c())
print(horizontal_line)

# Task d
print("Create a function that takes no parameters and asks the user to enter yes or no")


def function_d():
    """This function takes in no parameters and asks the user to enter 'yes' or 'no'.
    The users response is validated, looping until the user enters a valid response.
    The function returns 'True' if they answer 'yes' and returns 'False' if they answer 'no'."""
    response = False
    user_response = input("Enter 'yes' or 'no':")
    while user_response.lower() != "yes" or user_response.lower() != "no":
        if user_response.lower() == "yes":
            response = True
            print(response)
            break
        elif user_response.lower() == "no":
            print(response)
            break


print(function_d())
print(horizontal_line)

# Task e
print("Create a function that takes in a bool parameter and returns a value depending on the parameter value")


def function_e(boolean_value):
    """This function takes in a boolean parameter and depending the on the
    passed parameter, it will return a different value.
    :param boolean_value
    :return string"""
    if boolean_value:
        print("The boolean value was", boolean_value)
    elif not boolean_value:
        print("The boolean value was", boolean_value)


print(function_e(boolean_value=True))
print(function_e(boolean_value=False))
print(horizontal_line)

# Task f
print("Create a function that takes in an int parameter and displays a string that many times")


def function_f(repeated_string, number_of_times):
    """This function takes in a string and an integer. It then repeats the string the number
    of the integer.
    :param repeated_string
    :param number_of_times:"""
    i = 0
    while i < number_of_times:
        print(repeated_string)
        i += 1


print(function_f("hello", 10))
print(horizontal_line)

# Task g
print("Create a function that takes in two or more number parameters and performs a calculation with the numbers")


def function_g(number1, number2, number3):
    """This function takes in two or more numbers and performs a calculations with the numbers.
    :param number1
    :param number2
    :param number3
    :return result"""
    result = (number1 + number2) * number3
    print(result)


print(function_g(1, 2, 3))
print(horizontal_line)

# Task h
print("Create a function that takes in no parameters, and asks for the users age and shoe size")


def function_h():
    """This function takes in no parameters and asks for the users age and shoe size.
    It then displays the difference between their age and shoe size"""
    user_shoe_size = int(input("Enter your shoe size"))
    user_age = int(input("Enter your age"))
    difference = (user_age - user_shoe_size)
    print(difference)


print(function_h())
print(horizontal_line)