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
- `>` : Greater than
- `<` : Less than
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

---

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
