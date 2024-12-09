# Lecture 5

## 5.1 Loops and Iteration

### Repeated Steps:
```python
n = 5
while n > 0:
    print(n)
    n = n - 1
print('done, all set')
print(n)
```
#### Output:
```
5
4
3
2
1
done, all set
0
```
Loops (repeated steps) have iteration variables that change each time through a loop. Often these iteration variables go through a sequence of numbers.

### An Infinite Loop:
```python
n = 5 
while n > 0:
    print('leather')
    print('Rinse')
print('dryoff')
```
#### Output:
```
Rinse
leather
Rinse
leather
...
```
- The value of `n` does not change, causing the condition to always evaluate to `True`.

___

## CREATA INFINITE LOOP:
## ⚠️ **WARNING** ⚠️
*Run that loop at your own risk. Code is dengerous, when "YOU" don't know what you run. Maybe your system is crashed...THAT ONLY FOR EDUCATIONAL PURPOSE. REPO AUTHOR OR REPO NOT RESPONSIBLE FOR THAT OPERATION.*

[Before CPU condition](https://github.com/sumit-dev-01/python_study_meterials/blob/main/python/pics/before.png)

[After CPU condition](https://github.com/sumit-dev-01/python_study_meterials/blob/main/python/pics/after.png)


```python
loop_start = int(input("enter number: "))
while loop_start <= 0:
        print("enter a valid no.")
        loop_start = int(input("enter number: "))
while loop_start > 0:
    print("cloudadda.net")
```

```python
#output:
## when condition not met the requirements; so in this case, loop runs until user enter a value that grater than 0
enter number: -2
enter a valid no.
enter number: -4
enter a valid no.
enter number:

# when enter value that grater than 0 
enter number: 4

cloudadda.net
cloudadda.net
cloudadda.net
cloudadda.net
cloudadda.net
......
```

## Same code but when Loops (repeated steps) have iteration variables that change each time through a loop:

```python
loop_start = int(input("enter number: "))
while loop_start <= 0:
        print("enter a valid no.")
        loop_start = int(input("enter number: "))
while loop_start <= 10:
    print(loop_start)
    loop_start += 1

# output:
enter number: 2
2
3
4
5
6
7
8
9
10
```
*Here 1st "**while block**" condition is met the requirements then goto next code block, other wise 1st **while block** run and run endlessly...*

### Another Example:
```python
n = 0 
while n > 0:
    print('leather')
    print('winter')
print('dry off')
```
This behaves like an `if` statement and does not run because the condition evaluates to `False`.

### Breaking Out of a Loop:
- The `break` statement ends the current loop and jumps to the statement immediately following the loop.
- It acts like a loop test that can happen anywhere in the body of the loop.

Example:
```python
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('done')
```
#### Output:
```
> hello there
hello there
> cloudadda
cloudadda
> done
done
```
This is an example of an interactive loop that keeps running until the user types "done".

### Finishing an Iteration with Continue:
- The `continue` statement ends the current iteration and jumps to the top of the loop to start the next iteration.

Example:
```python
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('done')
```
#### Output:
```
> sumit
sumit
> cloud computing
cloud computing
> #cloudadda
> done
done
```

#### Purpose of the Code:
- Filters out unwanted input lines starting with `#`.
- Processes valid input dynamically.
- Allows users to gracefully terminate the loop using `done`.

#### Applications:
- Command-line utilities
- Console applications
- Text file parsers
- Educational tools
- Data cleaning

---

## 5.2 Simple Definite Loop
### Example:
```python
for i in [1, 2, 3, 4, 5]:
    print(i)
print('done')
```
#### Output:
```
1
2
3
4
5
done
```

### A Definite Loop with Strings:
```python
data = ['sumit-dev-01(github)', '@cloudadda.001(youtube)', 'cloudadda(Pvt. Ltd.)']
for cloudadda in data:
    print('My assets: ', cloudadda)
```
#### Output:
```
My assets:  sumit-dev-01(github)
My assets:  @cloudadda.001(youtube)
My assets:  cloudadda(Pvt. Ltd.)
```

### Iteration with Numbers:
```python
for i in [5, 4, 3, 2, 1]:
    print(i)
print(i)
```
#### Output:
```
5
4
3
2
1
1
```
Definite loops (for loops) have explicit iteration variables that change each time through a loop.

---

## 5.3 Finding the Largest Value
### Example of a Loop:
```python
print('before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('after')
```
#### Output:
```
before
9
41
12
3
74
15
after
```

### Finding the Largest Value:
```python
largest_so_far = -1
print('before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('after', largest_so_far)
```
#### Output:
```
before -1
9 9
41 41
41 12
41 3
74 74
74 15
after 74
```
---

## 5.4 Counting in a Loop
```python
zark = 0 
print('before', zark)
for thing in [9, 41, 12, 3, 74, 15]:
    zark = zark + 1
    print(zark, thing)
print('after', zark)
```
#### Output:
```
before 0
1 9
2 41
3 12
4 3
5 74
6 15
after 6
```

### Summing in a Loop:
```python
zark = 0 
print('before', zark)
for thing in [9, 41, 12, 3, 74, 15]:
    zark = zark + thing
    print(zark, thing)
print('after', zark)
```
#### Output:
```
before 0
9 9
50 41
62 12
65 3
139 74
154 15
after 154
```

### Finding the Average in a Loop:
```python
count = 0 
sum = 0
print('before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('after', count, sum, sum/count)
```
#### Output:
```
before 0 0
1 9 9
2 50 41
3 62 12
4 65 3
5 139 74
6 154 15
after 6 154 25.666666666666668
```

### Filtering in a Loop:
```python
print('before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('large number', value)
print('after')
```
#### Output:
```
before
large number 41
large number 74
after
```

---

## Searching Using a Boolean Variable
```python
found = False
print('before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        print(value)
        break
    print(found, value)
print('after', found)
```
#### Output:
```
before False
False 9
False 41
False 12
3
after True
```

---

## Finding the Smallest Value
```python
smallest = None
print('before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('after', smallest)
```
#### Output:
```
before
9 9
9 41
9 12
3 3
3 74
3 15
after 3
```

---

### Notes:
- **`None` as a Flag Value:** Indicates a variable that has not been set.
- **`is` and `is not` Operators:** Used for logical comparisons, stronger than `==`. Implies identity rather than equality.
