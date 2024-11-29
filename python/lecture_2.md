# Lecture 2

## 2.1 Expressions

### Constant
- Fixed values such as numbers, letters, and strings are called constants because their value does not change. 
- Numeric constants are as expected.
- Strings are stored using single quotes (`'`) or double quotes (`"`).

### Variables
- A variable is a named place in the memory where a programmer can store data and later retrieve the data using the variable 'name'.
- Programmers get to choose the names of variables.
- You can change the content of a variable in a later statement.

**Examples:**
```python
x = 343  # int
y = 43.3  # float
```

### Python Variable Naming Criteria
- Must start with a letter or underscore (`_`).
- Must consist of letters, numbers, and underscores.
- Case sensitive.

**Examples:**
- Good: `span`, `eggs`, `span33`, `_speed`
- Bad: `23span`, `#sign`, `var.12`
- Different: `span`, `Span`, `SPAM`

**Make variable names sensible:**
```python
# Without sense:
a = int(input("Please enter: "))
b = 8.30
c = a * b
print(f"Today's your total income: {c}")
# Output: 846.6

# With sense:
customer = int(input("Please enter blouse quantity of the day in dozens: "))
dozen_1 = 8.30
total_income = dozen_1 * customer
print(f"Today's your total income: {total_income}")
# Output: 846.6
```

### Assignment Statement
- We assign a value to a variable using the assignment statement (`=`).
- An assignment statement consists of an expression on the right-hand side and a variable to store the result.

**Example:**
```python
x = 0.6
x = 3.9 * x * (1 - x)
print(x)
# Output: 0.9359999999999999
```

## 2.2 Numeric Expressions

### Operators
| Operator | Operation        |
|----------|------------------|
| `+`      | Addition         |
| `-`      | Subtraction      |
| `*`      | Multiplication   |
| `/`      | Division         |
| `**`     | Power            |
| `%`      | Remainder        |

### Order of Evaluation
- When operators are combined, Python determines the order using **Operator Precedence**.

**Operator Precedence Rules (from highest to lowest):**
1. Parentheses (`()`)
2. Exponentiation (`**`)
3. Multiplication (`*`), Division (`/`), and Remainder (`%`)
4. Addition (`+`) and Subtraction (`-`)
5. Left to right for operators of the same precedence.

**Example:**
```python
x = 1 + 2 * 3 - 4 / 5 ** 6
print(x)
# Output: 6.999744
```

**BODMAS Rule vs Precedence Rule:**
- **BODMAS Rule:** Used in manual calculations for mathematical operations.
- **Precedence Rule:** Applied by programming languages like Python, covering a broader range of operators.

### What Does "Type" Mean?
- In Python, variables, literals, and constants have a **type**.
- Python can differentiate between an integer and a string.

**Example:**
```python
add = 1 + 4
print(add)  # Output: 5

join = "sumit" + "paul"
print(join)  # Output: sumitpaul
```

**Type Checking:**
```python
join = 1 + 1
print(type(join))  # Output: <class 'int'>

join = 'sumit'
print(type(join))  # Output: <class 'str'>
```

### Types of Numbers
- **Integer:** Whole numbers (e.g., `-14`, `-2`, `0`, `1`, `100`)
- **Floating Point:** Numbers with decimal parts (e.g., `-2.5`, `0.0`, `98.6`)

### Type Conversion
- **Implicit Conversion:** Integer is implicitly converted to float in mixed expressions.
- **Explicit Conversion:** Use `int()` and `float()` for manual conversion.

**Example:**
```python
print(float(99) + 100)  # Output: 199.0

i = 42
print(type(i))  # Output: <class 'int'>

f = float(i)
print(type(f))  # Output: <class 'float'>
print(f)        # Output: 42.0
```

### Integer Division
- Produces a floating-point result.
```python
print(10 / 2)  # Output: 5.0
```

### String Conversion
- Use `int()` and `float()` to convert strings to numbers.
- An error occurs if the string does not contain numeric characters.

**Example:**
```python
num = '123'
print(type(num))  # Output: <class 'str'>

con_num = int(num)
print(type(con_num))  # Output: <class 'int'>
print(con_num + 1)    # Output: 124
```

### User Input
- Use the `input()` function to read data from the user.
- The `input()` function always returns a string.

**Example:**
```python
user = input('Please enter your name: ')
print('Welcome', user)
# Output: Welcome sumit
```

### Comments in Python
- Anything after a `#` is ignored by Python.
- **Why comments are required?**
  1. Describe what is going to happen in a sequence of code.
  2. Document who wrote the code or other ancillary information.
  3. Temporarily turn off a line of code.

**Example:**
```python
# Author: Sumit Paul
# Date: 29th November 2024
# This script handles user authentication
```

### Converting User Input
- Convert user input from a string to a number using type conversion functions.

**Example:**
```python
inp = input('Europe floors? ')
usf = int(inp) + 1 
print('US floors:', usf)
# Output: US floors: 4
