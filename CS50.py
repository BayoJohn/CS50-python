# Main Version
name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")


# Consolidated Version

name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")

elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# Using match and case

name = input("What's your name? ")
match name:
    case "Harry":
        print("Gryffindor")
match name:
    case "Hermione":
        print("Gryffindor")
match name:
    case "Ron":
        print("Gryffindor")
match name:
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")    


# Cosolidated version for match

name = input("What's your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
match name:
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")    


# Simple log parser

from collections import Counter

def parse_logs(file="app.log"):
    with open(file, "r") as f:
        logs = f.readlines()

    errors = [line for line in logs if "ERROR" in line]
    warnings = [line for line in logs if "WARNING" in line]
    infos = [line for line in logs if "INFO" in line]

    error_types = Counter([line.split("ERROR: ")[1] for line in errors if "ERROR:" in line])

    return {
        "errors": len(errors),
        "warnings": len(warnings),
        "infos": len(infos),
        "top_error": error_types.most_common(1)
    }

stats = parse_logs()
print(stats)



# Using the request to get API's

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=songs&limit=50&term=" + sys.argv[1])
o = response.json()
for result in o["result"]:
    print(result["trackName"])







# Version 1
x = input("What is x? ")
y = input("What is y? ")

z = int(x) + int(y)
print(z)

# Version 2
x = int(input("What is x? "))
y = int(input("What is y? "))

print (x + y)

# Version 3 with float values
x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x / y, 2)

print(z)


# Return function

def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()



# First version
score = int(input("Score: "))
if score >= 90 and score < 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60  and score < 100:
    print("Grade: D")
else:
    print("Grade:F")

# Second version

score = int(input("Score: "))
if 90 <= score < 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade:F")

# Third version
score = int(input("Score: "))
if score >= 90:
    print("Grade:A")
elif score >= 80:
    print("Grade:B")
elif score >= 70:
    print("Grade:C")
elif score >= 60:
    print("Grade:D")
else:
    print("Grade: F")




# Random Module
import random
coin = random.choice(["heads","tails"])
print(coin)

# Using the randint
import random
number = random.randint(1, 10)
print("number")


# Random Module calling out choice
from random import choice
coin = random.choice(["heads","tails"])
print(coin)

# Using the shuffle function
import random
cards = ["Jack","King","Queen"]
random.shuffle(cards)
for card in cards:
    print(card)



# list
students = ["Hermione", "Harry", "Ron"]
print(students[0])

for student in students:
    print(student)

# list
students = ["Hermione", "Harry", "Ron"]
print(students[0])

for i in range(len(students)):
    print(i + 1, students[i])
   
# Dictionaries
students = {"Hermione": "Gryffindor", 
            "Harry": "Gryffindor", 
            "Ron": "Gryffindor",
            "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep=",")

# Dictonary with more keys

students  = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Rusell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for students in students:
    print(students["name"], students["house"], students["patronus"], sep=",")








# Exceptions

while True:

    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")

    else:
        break

print(f"x is {x}")


# With functions

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
        return x

main()

# Using the Pass statement

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            pass

main()





# First version
def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        False

main()

# Pyhtonic version
def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return True if n % 2 == 0 else False

main()





# first version
x = int(input("What is x? "))
y = int(input("What is y? "))

if x < y:
    print("x is greater than y")
if x > y:
    print("x is less than y")
if x == y:
    print("x is equal to y")

# second version
x = int(input("What is x? "))
y = int(input("What is y? "))

if x < y:
    print("x is greater than y")
elif x > y:
    print("x is less than y")
elif x == y:
    print("x is equal to y")

# third version

x = int(input("What is x? "))
y = int(input("What is y? "))

if x < y:
    print("x is greater than y")
if x > y:
    print("x is less than y")
else:
    print("x is equal to y")



# fourth version

x = int(input("What is x? "))
y = int(input("What is y? "))
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# fifth version

x = int(input("What is x? "))
y = int(input("What is y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# sixth version

x = int(input("What is x? "))
y = int(input("What is y? "))

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")


# Code itself

def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))

def square(n):
    return n + n


if __name__ == "__main__":
    main()



# Test for calculator

from calculator import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")

    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
 

if __name__ == "__main__":
    main()

# Storing file in a list

names = []

for _ in range(3):
    name = input("what's your name? ")
    names.append(name)


for name in sorted(names):
    print(f"hello,{name}")



# Writing to a file
name  = input("What's your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")




# Read an existing file
with open("names.txt", "r") as file:
    lines = file.readlines()


for line in lines:
    print("hello,",line.rstrip())


# Sorting an existing file

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.strip())


for line in sorted(names):
    print(f"Hello, {line}")


# Reading a CSV file

with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")



# Reading a CSV file (unpacking sequence)

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")



# Reading a CSV file (unpacking sequence)
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
        




# Reading a CSV file (unpacking sequence)
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}
        students.append(student)


for students in sorted(students):
    print(f"{student['name']} is in {student['house']}")



# Reading a CSV file (using the key parameter of the sorted function)
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}
        students.append(student)


def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")



# Reading a CSV file (using the lambda to create a function)
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}
        students.append(student)



for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")


 



# Reading a CSV file (using the CSV library)
import csv

students = []
with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name":name, "home":home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# Reading a CSV file (using the DicReader function in the CSV library)

import csv

students = []


with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})



for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
    



# Reading a CSV file (Writing to a CSV file)

import csv

name = input("What's your name? ")
home = input("Where's your name? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])


# Reading a CSV file (Writing to a CSV file)

import csv

name = input("What's your name? ")
home = input("Where's your house? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})



# Creating a GIF using the pillow library


import sys

from PIL import image

images = []

for arg in sys.argv[1]:
    image = image.open(arg)
    images.append(image)


images[0].save(
    "costumes.gif" , save_all=True, append_images=[images[1]], duration=200, loop=0
)




# Regular Expression

import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")





# Object Oriented Programming


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student



if __name__ == "__main__":
    main()






