# Task a
"""This program is for week 8 - Further Python functions, Python sampler: exceptions"""
horizontal_line = '-' * 15


# Task b
def function_open_and_read_file(file_name):
    try:
        with open(file_name) as f:
            for i, l in enumerate(f):
                pass
            return i + 1
    except OSError as error:
        print("The file was not found")
        print(error)


print("Number of lines in the file: ", function_open_and_read_file("texts.txt"))
print(horizontal_line)


# Task c
def function_open_and_read_first_line_words(file_name):
    try:
        with open(file_name) as f:
            first_line = f.read()
            if len(first_line.strip()) == 0:
                print("The line is empty")
            else:
                print(len(first_line.split()))
    except OSError as error:
        print("The file was not found")
        print(error)


print(function_open_and_read_first_line_words("text.txt"))
print(horizontal_line)


# Task d
def function_add_two_parameters(parameter1, parameter2):
    print(parameter1 + parameter2)


"""print("Testing with ints")
print(function_add_two_parameters(2, 3))
print("Testing with float")
print(function_add_two_parameters(1.5, 1.5))
print("Testing with int and float")
print(function_add_two_parameters(1, 1.5))
print("Testing with string")
print(function_add_two_parameters("parameter 1", "parameter 2"))
print("Testing with string and int")
print(function_add_two_parameters("parameter 1", 2))
print("Testing with boolean")
print(function_add_two_parameters(True, True))
print(horizontal_line)"""


# Task e
def function_divide_two_parameters(parameter1, parameter2):
    try:
        print(parameter1 / parameter2)
    except ZeroDivisionError as error:
        print(error)


print("Divide 10 by 3")
print(function_divide_two_parameters(10, 3))
print("Divide 21 by 0")
print(function_divide_two_parameters(21, 0))
print(horizontal_line)


# Task f
def function_rest_of_exceptions():
    try:
        print("")
    except ZeroDivisionError as error:
        print(error)
    else:
        print("nothing went wrong")
    finally:
        print("The 'try except' is finished")
