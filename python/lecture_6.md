# Lecture 6 | 6.1

## String

### String Data Type:
- **Definition**: A string is a sequence of characters.
- **String Literals**: Use quotes for strings, e.g., `'hello'` or `"hello"`.
- **Concatenation**: The `+` operator concatenates strings.
- **String Containing Numbers**: Strings with numbers are still strings.
- **Conversion**: Convert strings containing numbers to integers using `int()`.

#### Example:
```python
str1 = "Hello"
str2 = "There"
bob = str1 + str2
print(bob)  # Output: HelloThere

str3 = 123
str3 = str3 + 1
print(str3)  # Output: 124

str4 = '125'
# str4 = str4 + 5  # Raises TypeError
x = int(str4) + 5
print(x)  # Output: 130
```

### Reading and Converting:
- **Preferred Method**: Read data as a string and then parse and convert as needed for better error handling.
- **Example**:
```python
name = input('Enter name: ')
apple = input('Apple quantity: ')
print(apple)
x = int(apple) - 5
print(x)
```

### Looking Inside Strings:
- **Indexing**: Use square brackets `[]` to access characters in a string.
- **Index Values**: Start at `0`.
- **Example**:
```python
fruit = 'banana'
letter = fruit[1]
print(letter)  # Output: a
x = 3
w = fruit[x - 1]
print(w)  # Output: n
```

### A Character Too Far:
- **Error**: Indexing beyond the string length raises an `IndexError`.
- **Example**:
```python
zot = 'abc'
# print(zot[5])  # Raises IndexError
```

### String Length:
- Use the built-in `len()` function to get the length of a string.
- **Example**:
```python
fruit = 'banana'
print(len(fruit))  # Output: 6
```

### Looping Through Strings:
- **While Loop**:
```python
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
```
- **For Loop** (Recommended):
```python
fruit = 'banana'
for letter in fruit:
    print(letter)
```

### Looping and Counting:
- **Counting Specific Characters**:
```python
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)  # Output: 3
```

### "in" Operator:
- **Definition**: Checks if one string exists within another.
- **Example**:
```python
fruit = 'banana'
if 'a' in fruit:
    print('Found it!')
```

### Slicing Strings:
- **Colon Operator `:`**: Extracts a substring.
- **Example**:
```python
s = 'Monty Python'
print(s[0:4])  # Output: Mont
print(s[6:])   # Output: Python
```

# Lecture 6 | 6.2

## Manipulating Strings

### String Concatenation:
- **Definition**: The `+` operator concatenates strings.
- **Example**:
```python
a = 'hello'
b = a + ' there'
print(b)  # Output: hello there
```

### "in" as Logical Operator:
- **Example**:
```python
fruit = 'banana'
if 'n' in fruit:
    print('Found it!')
```

### String Library:
- **Built-in Functions**: String methods do not modify the original string; they return a new string.
- **Examples**:
```python
greet = 'Hello Bob'
print(greet.lower())  # Output: hello bob
print(greet.upper())  # Output: HELLO BOB
```

### Searching a String:
- **Using `find()`**: Finds the first occurrence of a substring.
- **Example**:
```python
fruit = 'banana'
pos = fruit.find('na')
print(pos)  # Output: 2
```

### Replace in Strings:
- **Search and Replace**:
```python
greet = 'Hello Bob'
new_greet = greet.replace('Bob', 'Sumit')
print(new_greet)  # Output: Hello Sumit
```

### Stripping Whitespaces:
- **Methods**: `lstrip()`, `rstrip()`, and `strip()`.
- **Example**:
```python
greet = '   hello   '
print(greet.strip())  # Output: hello
```

### Parsing and Extracting:
- **Example**:
```python
data = "from sumitpaul@cloudadda.net   Sat Jan 01:53:55"
sf = data.find('@')
lf = data.find(' ', sf)
host = data[sf + 1 : lf]
print(host)  # Output: cloudadda.net
