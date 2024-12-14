# Lecture 1: Introduction to Python

## 1. Definition

### 1.1 CPU (Central Processing Unit)
- Runs the program – the CPU is always wondering "what to do next".
- Not the brain exactly – very dumb but very fast.

### 1.2 Input Device
- Keyboard, Mouse, Touch screen.

### 1.3 Output Device
- Screen, Printer, DVD burner, Speaker.

### 1.4 Main Memory
- Fast, small, temporary storage – lost on reboot.
- Also known as RAM.

### 1.5 Secondary Memory
- Slower, large, permanent storage.
- Lasts until deleted (e.g., Disk drive, Memory stick).

---

## 2. Inventor of Python

- Python was created by **Guido van Rossum**, a Dutch programmer, in the late 1980s.
- The first public release (version 0.9.0) was in **February 1991**.
- Guido’s goal was to design a language that was easy to read and use, with clean and simple syntax.
- He led Python’s development until stepping down as "Benevolent Dictator For Life" (BDFL) in **2018**, but remains an influential figure in the community.

---

## 3. Download Python in Windows

1. Visit: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download and install Python.

### Check Version:
1. Open CMD by pressing `[Windows + R]`, then type `cmd`.
2. Type:
   ```
   py --version
   ```

### Enable Python in CMD:
Type:
```bash
py
```

### Quit Python:
Use either:
```python
quit()
```
or
```python
exit()
```

---

## 4. Your First "Hello World"

### Using CMD:
1. Open CMD.
2. Type:
   ```python
   print("hello world!!")
   ```
   Hit Enter.

### Using Visual Studio Code:
1. Download VS Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Open VS Code and then open terminal in VS code.
3. Create a file named `hello.py`.
4. Write the following code in the file:
   ```python
   print("hello world!!")
   ```
5. Run the file using:
   ```bash
   py hello.py
   ```

---

## 5. Reserved Keywords in Python

Reserved keywords are predefined words that cannot be used as variable names, function names, or identifiers.

### List of Reserved Keywords:
```python
import keyword
print(keyword.kwlist)
```
**Output:**
```python
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

### Example of Reserved Keyword Error:
```python
False = 'sumit'
print(False)
```
**Error:**
```bash
SyntaxError: cannot assign to False
```

---

## 6. Variables in Python

A **variable** is a symbolic name that refers to a value or an object in memory. It acts as a container for storing data.

### Example:
```python
s = 'sumit'
print(s)
```
**Output:**
```python
sumit
```

---

## 7. Operators in Python

Operators are symbols or functions used to perform operations on values or variables.

### Types of Operators:

#### 7.1 Arithmetic Operators:
- `+` : Addition
- `-` : Subtraction
- `*` : Multiplication
- `/` : Division (float result)
- `//` : Floor division (integer result)
- `%` : Modulus (remainder)
- `**` : Exponentiation (power)

#### 7.2 Comparison Operators:
- `==` : Equal to
- `!=` : Not equal to
- `>` : Greater than (The greater than operator `>` is used to compare two values. It checks if the value on the left side is strictly larger than the value on the right side.)
- `<` : Less than (The less than operator `<` is used to compare two values. It checks if the value on the left side is strictly smaller than the value on the right side.)
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

#### 7.3 Logical Operators:
- `and` : Returns `True` if both conditions are true.
- `or` : Returns `True` if at least one condition is true.
- `not` : Reverses the result.

#### 7.4 Assignment Operators:
- `=` : Assign value.
- `+=` : Add and assign.
- `-=` : Subtract and assign.
- `*=` : Multiply and assign.
- `/=` : Divide and assign.

#### 7.5 Membership Operators:
- `in` : True if value exists in a sequence.
- `not in` : True if value does not exist in a sequence.

#### 7.6 Identity Operators:
- `is` : True if variables point to the same object.
- `is not` : True if variables point to different objects.

#### 7.7 Bitwise Operators:
- `&` : AND
- `|` : OR
- `^` : XOR
- `~` : NOT
- `<<` : Left shift
- `>>` : Right shift

---

## 8. Constants in Python

A **constant** is a variable whose value is intended to remain unchanged. By convention, constants are written in uppercase.

### Example:
```python
PI = 3.14159
GRAVITY = 9.8
SPEED_OF_LIGHT = 299792458
```

---

## 9. Functions in Python

A **function** is a reusable block of code that performs a specific task.

### Example:
```python
print("hello world!!")
```
- `print()` is a built-in function.

### User-defined Function:
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Sumit"))
```
**Output:**
```python
Hello, Sumit!
```
___

## What is an f-string?
*An f-string (formatted string literal) is a way to embed expression inside string literals using curly braces {}. It was introduced in python 3.6 and is now the preferred method for string formatting.*

*An f-string starts with an (f or F) before the opening quotation (") mark of the string. Inside the string, expression or variables can be embedded by enclosing them in curly braces {}. These expression are embedded and included in the string runtime.*


## Simplicity and Readability
- *Embed expressions directly in the string using `{}` without needing cumbersome string concatenation or `.format()` calls.*

```python
name = "Sumit"
age = 22
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Sumit and I am 25 years old.
```

## Faster Performance
- *f-strings are faster than both `.format()` and string concatenation because they are evaluated at runtime as a single expression.*

```python
import timeit

# Measure time taken by .format() method
format_time = timeit.timeit('"Hello, {}!".format("World")', number=100000000)

# Measure time taken by f-string
fstring_time = timeit.timeit('f"Hello, {"World"}!"', number=100000000)

# Print the results
print(f"Time taken by .format(): {format_time:.6f} seconds")
print(f"Time taken by f-strings: {fstring_time:.6f} seconds")

# Calculate time difference
time_difference = abs(format_time - fstring_time)

# Compare which is faster and print the time difference
if format_time > fstring_time:
    print("f-strings are faster!")
    print(f"f-strings are {time_difference:.6f} seconds faster.")
else:
    print(".format() is faster!")
    print(f".format() is {time_difference:.6f} seconds faster.")

#output:
Time taken by .format(): 18.676581 seconds
Time taken by f-strings: 5.067684 seconds
f-strings are faster!
f-strings are 13.608897 seconds faster.
```
#### comparing the execution time of two ways to format strings in Python: using `.format()` and `f-strings`.

#### This measures how long a small piece of code takes to run. Specify the code as a string and the **number=100000000** argument means it will run the code **10cr.** times to get an accurate measure.


## Supports Any Expression
- *f-strings can evaluate any Python expression within `{}`, including function calls, calculations, and object attributes.*

```python
import math
print(f"The square root of 16 is {math.sqrt(16)}.")
# Output: The square root of 16 is 4.0.
```

## Easier Debugging
- *You can use the `=` syntax inside an f-string to display both the variable name and its value.*

```python
x = 10
y = 20
print(f"x={x}, y={y}, sum={x + y}")
# Output: x=10, y=20, sum=30
```

## Cleaner Multi-Line Formatting
- *f-strings work seamlessly with multi-line strings, improving readability for complex templates.*

```python
user = "Sumit"
balance = 150.75
message = f"""
Hello {user},
Your current account balance is ${balance}.
"""
print(message)
```


## No Need for Explicit Conversion
- *Automatically converts non-string types to strings.*

```python
items = 5
print(f"You have {items} items.")
# Output: You have 5 items.
```

## Using f-string with formatting:
```python
pi = 3.14159
formatted_pi = f"pi is approximately {pi:.2f}"

print(formatted_pi)

#output:
pi is approximately 3.14
```

## Multiline string:
*You can create multiline string with the help of (""" """)*

```python

name = "sumit"
age = 22
message = f"""
Hello {name}
I'm {age} years old
"""
print(message)

#output:
Hello sumit
I'm 22 years old
```

## Escaping curly braces:
*If you meed to include curly braces { or } in the output string, you can escape them by doubling the braces {{ or }}*

```python

name = "sumit"
message = f"{{hello}} {name}"
print(message)

#output:
{hello} sumit
```

```python
price = 49.99
print(f"The price is ${price:.2f}.")

#output:
The price is $49.99.
```

## Date and Time formatting

```python
from datetime import datetime
current_time = datetime.now()
print(f"Current date and time is: {current_time:%Y-%m-%d %H:%M:%S}")

#output:
Current date and time is: 2024-12-09 01:52:25
```

---

| Format Code | Meaning                                        | Example |
|-------------|------------------------------------------------|---------|
| `%d`        | Day of the month (01 to 31)                    | 05      |
| `%m`        | Month (01 to 12)                               | 09      |
| `%Y`        | Year with century (e.g., 2024)                 | 2024    |
| `%H`        | Hour (00 to 23, 24-hour clock)                 | 15      |
| `%I`        | Hour (01 to 12, 12-hour clock)                 | 03      |
| `%M`        | Minute (00 to 59)                              | 45      |
| `%S`        | Second (00 to 59)                              | 30      |
| `%p`        | AM or PM                                       | PM      |
| `%A`        | Full weekday name                              | Monday  |
| `%a`        | Abbreviated weekday name                       | Mon     |
| `%B`        | Full month name                                | December|
| `%b`        | Abbreviated month name                         | Dec     |
| `%c`        | Locale’s date and time (full)                  | Thu Dec 13 15:45:30 2024 |
| `%x`        | Locale’s date (short format)                   | 12/13/24|
| `%X`        | Locale’s time (short format)                   | 15:45:30 |
| `%f`        | Microsecond (000000 to 999999)                 | 123456  |
| `%z`        | UTC offset in the form +HHMM or -HHMM          | +0200   |
| `%Z`        | Time zone abbreviation                         | UTC     |


## 10. Expressions in Python

An **expression** is a combination of values, variables, operators, and function calls that evaluates to produce a result.

### Example:
```python
x = 2
x = x + 2
print(x)
```
**Output:**
```python
4
```

---

## 11. About Python Script

1. Python is suitable for short experiments and small programs.
2. Longer programs are written in files with the `.py` extension.
3. These files are referred to as **Python scripts**.

---

## 12. Program Steps or Flow

### Sequential Steps:
```python
x = 2
print(x)
x = x + 2
print(x)
```
**Output:**
```python
2
4
```

### Conditional Steps:
```python
x = 7
if x < 10:
    print("smaller")
if x > 20:
    print("bigger")
print("finish")
```
**Output:**
```python
smaller
finish
```

### Repeated Steps:
```python
n = 1
while n <= 5:
    print(n)
    n = n + 1
```
**Output:**
```python
1
2
3
4
5
```
