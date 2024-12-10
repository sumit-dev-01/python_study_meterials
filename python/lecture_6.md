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
name = input("enter name: ")
apple = input("apple quantity: ")
print(apple)
print(type(apple))
con_apple = int(apple) + 4
print(type(con_apple))
print(f"{name} you have now {con_apple} apples")

#output:
enter name: sumit
apple quantity: 34
34
<class 'str'>
<class 'int'>
sumit you have now 38 apples
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
fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

#output:
0 b
1 a
2 n
3 a
4 n
5 a
```
- **For Loop**:
```python
fruit = "banana"
count = 0
for letter in fruit:
    print(count, letter)
    count += 1

#output:
0 b
1 a
2 n
3 a
4 n
5 a
```

### Looping and Counting:
- **Counting Specific Characters**:
```python
word = input("Enter fruit name: ")
count = 0
times_of_iterate = 1
for letter in word:
    if letter == "j":
        count += 1
    if times_of_iterate == 2:
        print(f"{times_of_iterate}nd iteration, {count}")
    elif times_of_iterate == 3:
        print(f"{times_of_iterate}rd iteration, {count}")
    elif times_of_iterate >= 4:
        print(f"{times_of_iterate}th iteration, {count}")
    else:
        print(f"{times_of_iterate}st iteration, {count}")
    times_of_iterate += 1
print(f"total count {count}")
```

```python
#output:
Enter fruit name: jack fruit
1st iteration, 1
2nd iteration, 1
3rd iteration, 1
2nd iteration, 1
3rd iteration, 1
3rd iteration, 1
4th iteration, 1
5th iteration, 1
6th iteration, 1
7th iteration, 1
7th iteration, 1
8th iteration, 1
9th iteration, 1
9th iteration, 1
10th iteration, 1
total count 1
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

## Parsing and Extracting:
### Syntax

`str.find(sub[, start[, end]])`

**substring**: *The string to be searched.*

**start**(optional): *The starting index where the search begins.*

**end**(optional): *The ending index where the search stops.*

- **Example**:
```python
data = "from sumitpual@cloudadda.net sat jan 4 08:34:33"
finding_arg1 = data.find("@") # substring "@"
print(finding_arg1)
finding_arg2 = data.find(" ", finding_arg1)
print(finding_arg2)
domain_name = data[finding_arg1 + 1 : finding_arg2] # finding_arg1 is starting argument, where search start and finding_arg2 is where search stops.
print(domain_name)

#output:
14
28
cloudadda.net
```

*In this scenario we'll find a **domain name** `cloudadda.net` from a professional email address not regular email like gmail. That is my professional email id `sumitpaul@cloudadda.net`*

*First you know about how looks like or a structure of professional email id. `@` is common for both gmail and professional email id.*

*My first task is find out `@` from that email.*

*Secondly find first space after `@`. Because there are so many things on a professinal email's header portion.*

*Third combind all the index value on `find()` syntax. Make sure index value starts from default and ending is upto but not include. Now add (+1)  on stating index, so count start from `cloudadda.net`'s `c` not starts from `@`*