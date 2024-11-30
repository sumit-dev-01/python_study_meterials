# Lecture 3: Conditional Statements in Python

## 3.1 Conditional Statement

### Conditional Steps
```python
x = 5 
if x < 10:
    print('smaller')
if x > 20:
    print('bigger')
print('done')
```
**Output:**
```
smaller
done
```

### Comparison Operators
- **Boolean expressions** ask a question and produce a yes/no result to control program flow.
- Boolean expressions using comparison operators evaluate to `True` or `False`.
- **Comparison operators** look at variables but do not change them.

| Python | Meaning                |
|--------|------------------------|
| `<`    | Less than              |
| `<=`   | Less than or equal to  |
| `==`   | Equal to               |
| `>=`   | Greater than or equal to|
| `>`    | Greater than           |
| `!=`   | Not equal to           |

> **Note:** `=` is used for assignment.

#### Examples of Comparison Operators
```python
x = 5 
if x == 5:
    print('equal to 5')
if x > 4:
    print('greater than 4')
if x >= 5:
    print('greater than or equal to 5')
if x < 6:
    print('less than 6')
if x <= 5:
    print('less than or equal to 5')
if x != 6:
    print('not equal to 6')
```
**Output:**
```
equal to 5
greater than 4
greater than or equal to 5
less than 6
less than or equal to 5
not equal to 6
```

### One-Way Decision
```python
x = 5
print('before 5')

if x == 5:
    print('is 5')
    print('is still 5')
    print('third 5')
print('afterward 5')
print('before 6')

if x == 6:
    print('is 6')
    print('is still 6')
    print('third 6')
print('afterward 6')
```
**Output:**
```
before 5
is 5
is still 5
third 5
afterward 5
before 6
afterward 6
```

- **Indentation:** Python requires proper indentation to indicate the end of a block.

### Example with Indentation
```python
x = 5
if x > 2:
    print('bigger than 2')
    print('still bigger')
print('done with 2')

for i in range(5):
    print(i)
    if i > 2:
        print('bigger than 2')
    print('done with i', i)
print('print all done')
```
**Output:**
```
bigger than 2
still bigger
done with 2
0
done with i 0
1
done with i 1
2
done with i 2
3
bigger than 2
done with i 3
4
bigger than 2
done with i 4
print all done
```

### Nested Decision
```python
x = 42
if x > 1:
    print('more than 1')
    if x < 100:
        print('less than 100')
print('all done')
```
**Output:**
```
more than 1
less than 100
all done
```

## 3.2 Two-Way Decision with `else`
- Executes one block if a condition is `True`, otherwise executes another block.
- It acts like a fork in the road.

```python
x = 1

if x > 2:
    print('bigger')
else:
    print('smaller')
print('all set')
```
**Output:**
```
smaller
all set
```

## Multi-Way Decision with `elif`
```python
x = 7
if x < 2:
    print('smaller')
elif x < 10:
    print('bigger')
else:
    print('large')
print('all done')
```
**Output:**
```
bigger
all done
```

### Example: Bike Gear Design
```python
speedo_meter = int(input('fetching bike speed: '))

if speedo_meter < 160:
    print('Gear 1st, below speed 160')
elif speedo_meter < 200:
    print('Gear 2nd, below speed 200')
elif speedo_meter < 290:
    print('Gear 3rd, below speed 290')
elif speedo_meter < 350:
    print('Gear 4th, below speed 350')
elif speedo_meter <= 500:
    print('Gear 5th, above speed 350+')
else:
    print('please enter a valid input')
```

### Multi-Way Without `else`
```python
x = 5
if x < 2:
    print('smaller')
if x < 10:
    print('medium')
print('all done')
```
**Output:**
```
medium
all done
```

### Multi-Way Puzzle
```python
x = 5
if x < 2:
    print('below 2')
elif x >= 2:
    print('two or more')
else:
    print('something else')
```
**Output:**
```
two or more
```

**Conclusion:** The `else` statement does not run because the `elif` condition (`x >= 2`) includes all possible remaining cases.

```python
x = 4 
if x < 2:
    print('below 2')
elif x < 20:
    print('below 20')
elif x < 10:
    print('below 10')
else:
    print('something else')
print('done')
```
**Output:**
```
below 20
done
```
**Conclusion:** The second `elif` statement (`x < 10`) is correct but does not execute because Python evaluates conditions line by line and stops at the first true condition.

## `try` and `except` Structure
- Surround dangerous code with `try` and `except` to handle potential errors.

### Example 1
```python
astr = 'hello bob'
try:
    istr = int(astr)
except:
    istr = -1
print(istr)
```
**Output:**
```
-1
```
**Conclusion:** The code fails but does not throw an error; instead, the `except` block runs.

### Example 2
```python
anum = '123'
try:
    xnum = int(anum)
except:
    xnum = -1
print(xnum)
```
**Output:**
```
123
```
**Conclusion:** The code runs successfully and skips the `except` block.

### Sample Example
```python
raw_str = input('enter a number: ')
try:
    con_num = int(raw_str)
except:
    con_num = -1
if con_num > 0:
    print("that's a number")
else:
    print("sorry, I can't understand")
```
**Output:**
```
enter a number: 56
that's a number
