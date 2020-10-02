# Task a
"""This program is for week 7 - Beginning python, Python sampler: loops"""
horizontal_line = '-' * 15
practiceList = ["1", "2", "3", "4", "5"]
loopList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
practiceDictionary = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# Task b
print("Display every value in your list")
for x in practiceList:
    print(x)

print(horizontal_line)

print("Display every pair of index in your list by colon")
num = 0
for i in range(len(practiceList)):
    practiceList[i] = str(num) + ": " + practiceList[i]
    num = num + 1
    print(practiceList[i])

print(horizontal_line)

# Task c
print("Display every key in your dictionary")
for key, value in practiceDictionary.items():
    print(key)
print(horizontal_line)

print("Display every value in your dictionary")
for key, value in practiceDictionary.items():
    print(value)
print(horizontal_line)

print("Display every key-value pair in your dictionary, as tuples")
for key, value in practiceDictionary.items():
    print(key, value)
print(horizontal_line)

print("Display every key-value in your dictionary, as unpacked tuples")
for key, value in practiceDictionary.items():
    print(key, value)
print(horizontal_line)

# Task d
print("Display every integer from 0-9 inclusive")
x = range(10)
for n in x:
    print(n)
print(horizontal_line)

print("Display every integer from 1-10 inclusive")
x = range(1, 11)
for n in x:
    print(n)
print(horizontal_line)

print("Display every odd number from 1-10 inclusive")
x = range(1, 11, 2)
for n in x:
    print(n)
print(horizontal_line)

print("Display every number from -100 to -90 inclusive")
x = range(-110, -89)
for n in x:
    print(n)
print(horizontal_line)

# Task e
print("Write a while loop to add up all numbers in a list until a target total of 100 or more is reached")
total = 0
i = 1
while total <= 100:
    total = total + i
    i += 1
print("The finishing total was", total)
print("It took", i, "iterations to total or reach more than 100 and how many numbers it took to reach the target")
print(horizontal_line)

# Task f
print("Write a for loop to add up all numbers in a list until a target of total of 200 or more is reached")
total = 0
i = 1
reached = False
for x in range(0, 100):
    total = total + i
    if total >= 200:
        reached = True
        break
    i += 1

print("Was the target met:", reached)
print("The total was", total)
print(horizontal_line)
