# Lecture 4 | 4.1

## Function

### Stored and Reused Steps:
```python
def thing():
    print('hello')
    print('fun')

thing()
print('zip')
thing()
```
**Output:**
```
hello
fun
zip
hello
fun
```

### Definition:
- We call these reusable pieces of code **"functions"**.
- A function doesn’t run automatically; it needs to be invoked or called first.

### Python Built-in Functions:
```python
big = max('hello world')
print(big)
```
**Output:**
```
W
```

Another function is `min`:
```python
tiny = min('hello world')
print(tiny)
```
**Output:**
```
( ) (Blank space)
```

### How `max` and `min` Functions Work

#### On the Expression `big = max('hello world')`:

#### `max()` Function:
- The `max()` function returns the largest item in an iterable. Here, the iterable is the string `"hello world"`.
- In strings, Python compares characters based on their ASCII values.
- **ASCII** refers to American Standard Code for Information Interchange.

#### Execution:
- In the string `"hello world"`, characters are compared, and the one with the highest ASCII value is returned.
- **Space (`' '`)** has a lower ASCII value than any letter, so it is ignored in the comparison.
- Among the characters (`'h'`, `'e'`, `'l'`, `'o'`, `'w'`, `'r'`, `'d'`), the character `'w'` has the highest ASCII value.

#### Result:
- The variable `big` will be assigned `'w'`.

#### Why ASCII Values Matter:
- Python treats each character in the string as an individual entity, and ASCII values determine which character is greater.
- **Use of `max`:** This method is often used with numerical values or structured data but can also apply to strings for character comparisons.

**Example:**
```python
print(max('hello world'))
```
**Output:**
```
w
```

---

### What is ASCII?
ASCII is a character encoding standard used to represent text in computers and other devices that work with text.

#### Key Points:
1. **Purpose:**
   - ASCII assigns a unique numeric value (between 0 and 127) to each character, including letters, numbers, punctuation, and control characters.
   - This enables computers to store and communicate text-based data.

2. **Examples:**
   - `'A'` = ASCII value 65
   - `'a'` = ASCII value 97
   - `'0'` = ASCII value 48
   - `' '` (Space) = ASCII value 32

3. **Why It’s Useful:**
   - Computers understand numbers, not characters. ASCII provides a way to convert human-readable characters into numeric codes.

4. **Usage in Python:**
   - To get the ASCII value of a character: `ord('A') = 65`
   - To get the character from an ASCII value: `chr(65) = 'A'`
   
**Examples:**
```python
print(ord('A'))  # Output: 65
print(chr(65))   # Output: 'A'
```

#### Why Numbers Like ASCII Values Exist:
- Computers fundamentally understand only 0s and 1s (binary). These binary states represent off (`0`) and on (`1`) in digital systems.
- Higher-level abstractions like numbers and characters make programming and computing more human-friendly.
- ASCII bridges the gap between human understanding and machine language.

#### Relationship Between Binary and ASCII:
- The ASCII number itself is stored in binary in the computer.
- **Example:**
  - `65` (ASCII for `'A'`) is represented in binary as `0b1000001` (`0b` indicates binary format).
- This system allows computers to represent complex readable text and process it using logical syntax.

### How to Calculate Binary for Any Character:
1. **Find the ASCII Value:**
   - The ASCII value of `'A'` is 65 in decimal.
2. **Convert Decimal to Binary:**
   - To convert 65 to binary, divide the number by 2 repeatedly, recording the remainder at each step.
3. **Write the Remainder from Bottom to Top:**
   - This gives the binary equivalent.

**Example:**
- Calculate the binary equivalent of the ASCII value for `'A'` (65):
  1. Divide 65 by 2 → Quotient: 32, Remainder: 1
  2. Divide 32 by 2 → Quotient: 16, Remainder: 0
  3. Divide 16 by 2 → Quotient: 8, Remainder: 0
  4. Divide 8 by 2 → Quotient: 4, Remainder: 0
  5. Divide 4 by 2 → Quotient: 2, Remainder: 0
  6. Divide 2 by 2 → Quotient: 1, Remainder: 0
  7. Divide 1 by 2 → Quotient: 0, Remainder: 1

Write the remainders from bottom to top: **1000001**.
- The binary equivalent of 65 is **1000001**, which is also the ASCII representation of `'A'`.

---

# Lecture 4 | 4.2

## Building Functions

### Building Your Own Function:
- We create a new function using the `def` keyword followed by parameters in parentheses.
- Indent the body of the function.
- This defines the function but does not execute the body.

**Program:**
```python
def sumit_dev_01():
    print("CloudAdda builds AI that performs any data processing task in just seconds")
    print("Sumit, meanwhile me, is the creator of that AI")
    print("BIBO is the most advanced AI that only works for human help, completing tasks as fast as possible")

# Invoke function()
sumit_dev_01()
```
**Output:**
```
CloudAdda builds AI that performs any data processing task in just seconds
Sumit, meanwhile me, is the creator of that AI
BIBO is the most advanced AI that only works for human help, completing tasks as fast as possible
```

---

### Arguments:
- An **argument** is a value passed into the function as input when calling it.
- Arguments direct the function to perform different tasks at different times.
- We put arguments in parentheses after the function name.

**Example:**
```python
def sumit_dev_01(target):
    print(f"Future Target: {target}")

sumit_dev_01("Build a universal AI")
```

### Parameters:
- A **parameter** is a variable used in the function definition.
- It acts as a "handle" to access arguments passed during a particular function invocation.

**Example:**
```python
def cloudadda(role):  # 'role' is a parameter
    if role == 'CEO':
        print('SUMIT PAUL')
    else:
        print('Data not found')

cloudadda('CEO')  # 'CEO' is an argument
```
**Output:**
```
SUMIT PAUL
```

---

### Return Value:
- A function takes its arguments, performs some computation, and returns a value using the `return` keyword.

**Example:**
```python
def cloudadda():
    return "Sumit"

print(cloudadda(), "- GitHub Administrator")
print(cloudadda(), "- YouTube @cloudadda.001 channel's instructor")
```
**Output:**
```
Sumit - GitHub Administrator
Sumit - YouTube @cloudadda.001 channel's instructor
```

---

### Multiple Parameters/Arguments:
- We can define more than one parameter in a function.
- Add more arguments when calling the function.
- Match the number and order of arguments and parameters.

**Example:**
```python
def addtwo(a, b):  # Parameters
    added = a + b
    return added

x = addtwo(3, 5)  # Arguments
print(x)
```
**Output:**
```
8

## Create a dynamic table:

```python
count_table = int(input("enter a no. of table: "))
def multiply(counting):
    while counting <= 10:
        print(f"{count_table} x {counting} = {count_table * counting}")
        counting += 1

multiply(1)
```
**output**
```python
enter a no. of table: 13
13 x 1 = 13
13 x 2 = 26
13 x 3 = 39
13 x 4 = 52
13 x 5 = 65
13 x 6 = 78
13 x 7 = 91
13 x 8 = 104
13 x 9 = 117
13 x 10 = 130
```