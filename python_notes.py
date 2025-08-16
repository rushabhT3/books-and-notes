# to run this file, use: python python_notes.py

# ++i, i++ NOT SUPPORTED
# we DON'T have "of" keyword in python at all like in JS


# ========= variables =========

x = y = z = 0
x, y = 23, 45

# MIN and MAX
min = min(x, y, z)
max = max(x, y, z)

# absolute value
abs = abs(x)

# remainder
remainder = x % y

# power
result = x ** 2

# to find mid (useful in binary search)
mid = x + (y - x) // 2


# ========== Array ==========

array = ["a", "b", "c"]

# basic operations

# empty array check
if not array:
    print("Array is empty")

array.append("d")
print(array)
# output: ["a", "b", "c", "d"]

array.pop()
print(array)
# output: ["a", "b", "c"]

# slice
print(array[:])
# output: ["a", "b", "c"]

print(array[:-1])
# output: ["a", "b"]

print(array[1:])
# output: ["b", "c"]

# intialize with all zero elements
array_of_size_5 = [0] * 5
print(array_of_size_5)
# output: [0, 0, 0, 0, 0]

# for loop
for i in range(len(array)):
    print(array[i])
# output: a
#         b
#         c

for x in array:
    if x == "b":
        print("Found b")
    elif x != "c":
        print("Found a")
    else:
        print("Found c")
# output: Found a
#         Found b
#         Found c

for i, x in enumerate(array):
    print(i, x)
# output: 0 a
#         1 b
#         2 c

for i in array:
    print(i)
# output: a
#         b
#         c

# check if element is in array
if "a" in array:
    print("Found a")

# reverse array
i, j = 0, len(array) - 1

while i < j:
    array[i], array[j] = array[j], array[i]
    i += 1
    j -= 1

print(array)
# output: ["c", "b", "a"]

# sort the array
# e.g. Sort by start time in intervals = [[start, end], ...]
intervals.sort(key = lambda x: x[0])


# ========== Dictionary ==========

dictionary = {"a": 1, "b": 2, "c": 3}

# basic operations
dictionary["d"] = 4
print(dictionary)
# output: {"a": 1, "b": 2, "c": 3, "d": 4}

dictionary.pop("a")
print(dictionary)
# output: {"b": 2, "c": 3, "d": 4}

dictionary["a"] = dictionary.get("a", 0) + 1
print(dictionary)
# output: {"b": 2, "c": 3, "d": 4, "a": 1}

# check if key is in dictionary
if "a" in dictionary:
    print("Found a")

# check if key is NOT in dictionary
if "a" not in dictionary:
    print("Not found a")

dictionary = {"a": 1, "b": 2, "c": 3}

# for loop
for key, value in dictionary.items():
    print(key, value)
# output: a 1
#         b 2
#         c 3

for key in dictionary.keys():
    print(key)
# output: a
#         b
#         c

for value in dictionary.values():
    print(value)
# output: 1
#         2
#         3

for key in dictionary:
    print(key)
# output: a
#         b
#         c


# ========== Set ==========

my_set = {"a", "b", "c"}
# or, my_set = set(["a", "b", "c"])
array = ["x", "y", "z"]

# length
length = len(my_set)

# basic operations and for loop
for x in array:
    my_set.add(x)

print(my_set)
# output: {"a", "b", "c", "x", "y", "z"}

for x in array:
    my_set.remove(x)

print(my_set)
# output: {"a", "b", "c"}

for x in my_set:
    print(x)
# output: a
#         b
#         c


# ========== String ==========

string = "abc"

# change case
print(string.upper()) # ABC
print(string.lower()) # abc

# for loop
for x in string:
    print(x)
# output: a
#         b
#         c

for i, x in enumerate(string):
    print(i, x)
# output: 0 a
#         1 b
#         2 c

for i in range(len(string)):
    print(string[i])
# output: a
#         b
#         c

new_string = "xyz"
for x in new_string:
    string += x

print(string)
# output: abcxyz


# reverse string
i, j = 0, len(string) - 1
array_string = list(string)

while i < j:
    array_string[i], array_string[j] = array_string[j], array_string[i]
    i += 1
    j -= 1

# array to string
print("".join(array_string))
# output: "cba"

# or,
print(string[::-1])
# output: "cba"

# f-string
print(f"any string {string} {len(string)}")
# output: any string abc 3


# ========== Conversations string to array to dictionary count ==========

string = "abcaakc"
array = list(string)
dictionary = {}

for i, x in enumerate(array):
    dictionary[x] = dictionary.get(x, 0) + 1

print(array)
# output: ["a", "b", "c", "a", "a", "k", "c"]

print(dictionary)
# output: {"a": 3, "b": 1, "c": 2, "k": 1}


# ========= functions ==========

def add(a, b):
    return a + b

print(add(1, 2))
# output: 3

# lambda function
lambda_add = lambda a, b: a + b
print(lambda_add(1, 2))
# output: 3


# ========== class ==========

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + " " + str(self.age)

person = Person("John", 30)
print(person)
# output: John 30

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return self.name + " " + str(self.age) + " " + str(self.grade)

student = Student("John", 30, "A")
print(student)
# output: John 30 A


# ========== some other useful things ==========

# when input is a list of numbers
array = list(map(int, input("Enter a list of numbers separated by spaces").split()))
print(array)
# output: [1, 2, 3]


# pythonic ways
array = [1, 2, 3]
print(array)
# output: [1, 2, 3]

array = [x if x % 2 == 0 else x * 2 for x in array]
print(array)
# output: [2, 2, 6]
