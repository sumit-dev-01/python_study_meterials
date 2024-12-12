# Lecture 2

## 2.1 Expressions

### Constant
- Fixed values such as numbers, letters, and strings are called constants because their value does not change. 
- Numeric constants are as expected.
- Strings are stored using single quotes (`'`) or double quotes (`"`).

## Let's break down concepts of Constant:
### String immutability and how Python handles strings

#### Example 1: Attempting direct modification through indexing (raises TypeError)

```python
a = 'sumit'
print(a[2])
a[2] ='j'
print(a) # that raise a TypeError

#output:
TypeError: 'str' object does not support item assignment
```
### conclusion:
#### Why it fails:
- Strings are immutable in Python, meaning their contents cannot be changed in place.

- The operation `a[2]` = `'j'` tries to modify the character at index 2 directly, which is not allowed.

## Example 2: String modification using slicing (works)

```python
a = 'sumit'
print(f"Here '{a[2]}' is a substring")
b = a[:2] + "j" + a[3:]
print(f"In this operation we can assign a new variable called 'b' and that doesn't override variable 'a' value '{a}', now 'b' is {b}") 
print(f"variable 'a' value doesn't change yet '{a}'") # "m" is still be there, that shoudn't be updated. We can just reassign "m" to "j" in another vriable 
```
### Conclusion:
#### Why it works:
- Slicing creates substrings (`a[:2]` and `a[3:]`), which are then concatenated with the new character `'j'`.

- This doesn't modify the original string but creates a new string (b), showing how to effectively "modify" a string.

## Integers are not like strings.
- Strings are sequences of characters, so they support indexing and slicing.

- Integers, however, are atomic values in Python, meaning they are treated as a single entity and do not have "parts" you can access like a sequence.

```python
x = 3454
print(x[1])

#output:
TypeError: 'int' object is not subscriptable
```
- The integer 3454 is treated as a single, indivisible value.
- It does not have `"digits"` that can be accessed via indexing like characters in a string.

# We see numbers are not manipulated by indexing but still we can do:
## Suppose you work on an organization and you assigned for a work -
### `TASK ASSIGNED` 
**To extract the 3rd digit from the right (4) in the number 3`4`54**

"That approach works well for single operations, but it's not suitable for `millions of datasets`. When dealing with `millions of datasets`, we need more efficient data structures like `lists`, `dictionaries`, or `tuples`."
___
## Now complete the Assignment, which i assigned
```python
x = 3454
digit = (x // 100) % 10

print(digit)
```
### Step-by-Step Explanation:
1. `x // 100` (Remove the last 2 digits):
  - Floor division (`//`) removes the last 2 digits from the number.
  - For `x = 3454`:
  ```python
  3454 // 100 = 34
  ```
  - Now, the number `34` is left after removing the last two digits (`54`).

2. `34 % 10` (Get the last digit of 34):
  - Modulo (`%`) finds the remainder when dividing 34 by 10
  - Division:
  ```text
  34 ÷ 10 = 3 (quotient) with a remainder of 4
  ```
  - Find Remainder:
  - Multiply the quotient (`3`) by the divisor (`10`) to find how much of `34` is accounted for:
  ```text
  3×10=30
  ```
  - Subtract this from the original number (`34`):
  ```text
  34−30=4
  ```
  - This remainder (`4`) is the result of the modulo operation.

3. Result:
  - The last digit of `34` is `4`, which corresponds to the 3rd digit from the right of the original number `3454`.

### That's not end...that's just some examples of what we can do with python in large set data
## We're gonna one more thing 😎

## Converting and Manipulating Data Types in Python (Float to String and Back)
`float > str > float`
`3.14` to `3.34`

```python
PI = 3.14
print(PI)
print(type(PI))
con_pi = str(PI)
print(con_pi[2]) 
print(type(con_pi))
# con_pi[2] = "3" # TypeError: 'str' object does not support item assignment
reassign_pi_val = con_pi[:2] + "3" + con_pi[3]
print(reassign_pi_val)
print(type(reassign_pi_val))
change_pi_type = float(reassign_pi_val)
print(change_pi_type)
print(type(change_pi_type))

#output:
3.14
<class 'float'>
1
<class 'str'>
3.34
<class 'str'>
3.34
<class 'float'>
```

`PI`: **Capitalization Meaning** - *It suggests the value should not be changed during the program's* execution.

*In my earlier days of learning Python, I had the misconception that `capitalized variable` names can't be modified. Then I thought... hopefully, they really can't be changed!* 🤔💭 But later, I realized it's just a **convention** to indicate to other developers: **'Don't change the `PI` value throughout the program.'**

### Where need that data manipulation work:

- **Data Processing & Reporting:** *Formatting numbers for display or concatenation.*

- **User Input Handling:** *Converting user input from string to numeric for calculations.*

- **Data Export/Import:** *Converting data between strings and numbers for file compatibility.*

- **String Formatting:** *Adjusting number display (e.g., rounding, adding currency symbols).*

- **File Parsing:** *Parsing numeric data from text files or logs for processing.*

#### Here we clear two things 
- One is where need data manipulation.

- Another one is clear a misconception about `capitalizes variable`.

- Because 
π (pi) is a mathematical constant representing the ratio of a circle's circumference to its diameter.

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
