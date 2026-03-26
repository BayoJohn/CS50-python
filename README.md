# CS50 Python Learning Guide

A comprehensive collection of Python programming concepts and examples from CS50's Introduction to Computer Science course.

## Contents

### 1. **Conditionals & Control Flow**
- Harry Potter house sorting using `if`, `elif`, `else`
- `match` and `case` statements (Python 3.10+)
- Grade calculation based on score ranges

### 2. **Data Types & Input/Output**
- Integer and float arithmetic
- Type conversion with `int()` and `float()`
- Rounding values with `round()`

### 3. **Functions**
- Defining and calling functions
- Return statements
- Parameter passing
- The `square()` function examples

### 4. **Random Module**
- `random.choice()` - select random elements
- `random.randint()` - generate random integers
- `random.shuffle()` - randomize lists

### 5. **Data Structures**
- **Lists** - storing multiple values
- **Dictionaries** - key-value pairs
- **Lists of Dictionaries** - complex data structures

### 6. **Exception Handling**
- `try` and `except` blocks
- `ValueError` handling
- `pass` statement for silent exceptions

### 7. **File I/O**
- Reading files with `open()`
- Writing to files
- Using context managers (`with` statement)
- Reading and parsing CSV files
- CSV reader and DictReader

### 8. **Advanced Concepts**
- Lambda functions for sorting
- Regular expressions (regex)
- Object-Oriented Programming (OOP) with classes
- JSON parsing from API responses
- Log file parsing with `Counter`

### 9. **Libraries Used**
- `requests` - HTTP requests to APIs
- `csv` - CSV file handling
- `json` - JSON parsing
- `PIL/Pillow` - Image manipulation
- `re` - Regular expressions
- `collections.Counter` - Frequency counting

## Key Patterns

### Error Handling
```python
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
```

### File Operations
```python
with open("file.txt", "r") as file:
    lines = file.readlines()
```

### List Comprehension
```python
errors = [line for line in logs if "ERROR" in line]
```

### Lambda Functions
```python
sorted(students, key=lambda student: student["name"])
```

## Running the Code

Each section is self-contained. Run any code block with:

```bash
python3 CS50.py
```

Or run individual sections by copying them into a new file.

## Notes

- Some examples require input files (`names.txt`, `students.csv`, `app.log`)
- API examples require the `requests` library: `pip install requests`
- Image manipulation requires Pillow: `pip install pillow`
- Created: March 26, 2026

---

Study tip: Go through each section, understand the concept, then modify the code to practice!
