# Task a
"""This program is for week 7 - Beginning python, Python sampler: logic"""
variableInteger = 28
variableFloat = 28.0
variableBoolean = True
variableString = "String variable"
print(variableInteger)
print(variableFloat)
print(variableBoolean)
# Task b
if variableInteger == 28:
    print("The variable is the same as the number")

if variableFloat == 28.0:
    print("The variable is the same as the number")

if variableBoolean:
    print("The variable is the same as the value")

if variableString == "String variable":
    print("The variable is the same as the string")
# Task c
if variableInteger != 28:
    print("The variable is not the name as the number")

if variableFloat != 28.0:
    print("The variable is not the name as the number")

if not variableBoolean:
    print("The variable is not the name as the value")

if variableString != "String variable":
    print("The variable is not the name as the string")
# Task d Boolean is excluded from this task as a boolean value can only be True or False, meaning it can not be more
# than or less than. It can either be the same or not the same
if variableInteger < 28:
    print("The variable is less than the number")
elif variableInteger <= 28:
    print("The variable is less than or equal to the number")
elif variableInteger > 28:
    print("The variable is more than the number")
elif variableInteger >= 28:
    print("The variable is more than or equal to the number")

if variableFloat < 28.0:
    print("The variable is less than the number")
elif variableFloat <= 28.0:
    print("The variable is less than or equal to the number")
elif variableFloat > 28.0:
    print("The variable is more than the number")
elif variableFloat >= 28.0:
    print("The variable is more than or equal to the number")

if variableString < "String variable":
    print("The variable is less than the string")
elif variableString <= "String variable":
    print("The variable is less than or equal to the string")
elif variableString > "String variable":
    print("The variable is more than the number")
elif variableString >= "String variable":
    print("The variable is more than or equal to the string")
# Task e
if 40 <= variableInteger <= 100:
    print("The number is between 40 and 100")
# Task f
if 27 <= variableInteger <= 29:
    print("The number is between 27 and 29")
elif variableInteger >= 30 or variableInteger <= 31:
    print("The number is equal to or more than 30 and less than or equal to 31")
else:
    print()
