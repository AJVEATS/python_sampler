"""This program is for week 7 - Beginning python, Python sampler: data"""
# Practicing an ordinary comment for python
from typing import Dict, Any, Union

horizontal_line = '-' * 15
print("Hello world")
print(horizontal_line)

# Integer variable
variableInteger = 28
print(variableInteger)
print(type(variableInteger))
print(horizontal_line)
print("Hello world")

# Float variable
variableFloat = 28.0
print(variableFloat)
print(type(variableFloat))
print(horizontal_line)

# Boolean variable
variableBoolean = True
print(variableBoolean)
print(type(variableBoolean))
print(horizontal_line)

# String variable
variableString = "String variable"
print(variableString)
print(type(variableString))
print(horizontal_line)

practiceTuple = ("Title of the book", 2020, 3.28, False)
print(practiceTuple)
print(practiceTuple[0])
print(practiceTuple[1])
print(practiceTuple[2])
print(practiceTuple[3])

practiceList = [6, 3.28, True, "string in a list", practiceTuple]
print(practiceList)
print(practiceList[0])
print(practiceList[1])
print(practiceList[2])
print()
print(practiceList[3])
print(practiceList[4])

practiceDictionary = {
    "name": "Alexander Veats",
    "age": 18,
    "salary": 0
}
print(practiceDictionary)
print(practiceDictionary["name"])
print(practiceDictionary["age"])
print(practiceDictionary["salary"])

dictionaryMonths: Dict[Union[int, Any], Union[str, Any]] = {
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
print(dictionaryMonths[1])
print(dictionaryMonths[2])
print(dictionaryMonths[3])
print(dictionaryMonths[4])
print(dictionaryMonths[5])
print(dictionaryMonths[6])
print(dictionaryMonths[7])
print(dictionaryMonths[8])
print(dictionaryMonths[9])
print(dictionaryMonths[10])
print(dictionaryMonths[11])
print(dictionaryMonths[12])

practiceTuple2 = ("a", "b", "c")
print(practiceTuple2)
practiceTupleTemp = list(practiceTuple2)
practiceTupleTemp[1] = "c"
practiceTuple2 = tuple(practiceTupleTemp)
print(practiceTuple2)

practiceList2 = ["a", "b", "c"]
print(practiceList2)
practiceList2[1] = "c"
print(practiceList2)

practiceDictionary2 = {"first": 1, "second": 2, "third": 4}
print(practiceDictionary2)
