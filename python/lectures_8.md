# lecture 8 | 8.1 Lists

## programming:

- **Algorithms**
  - A set of rules or steps used to solve a problem
- **Data Structures**
  - A particular way of organizing data in a computer

## What is NOT a 'collection'?

Most of our variable have one value in them - when we put a new value in the variable the old value is overwriten.

```python
x = 2
x = 4
print(x)
# output:
4
```

## A list is a kind of collection:

1. A collection allows upto put many values in a single "variable".

2. A collection is nice because we can carry many values around in one convenient package.

```python
friends = ['Joshef', 'Glenn', 'Sally']
print(friends)
print(type(friends))

#output:
['Joshef', 'Glenn', 'Sally']
<class 'list'>
```

## List constants:

- List constant are surrounded by square bracketes [] and the elements in the list are separated by commas(,).

- A list element can be any python object even another list.

- A list can be empty.

```python
print([1, 24, 76]) # interger
print(['red', 'blue', 'yellow']) # stirng
print([1, [5, 6], 7]) # list on another list
print([]) #blank list

# output:
[1, 24, 76]
['red', 'blue', 'yellow']
[1, [5, 6], 7]
[]
```

## We already use list!

```python
for i in [5, 4, 3, 2, 1]:
    print(i)
print('done!!')

# output:
5
4
3
2
1
done!!
```

## List and Definite loops - Best pals

```python
friends = ['Sumit','Rohan', 'Sally']
for friend in friends:
    print('Happy New Year', friend)
print('done!!')

# output:
Happy New Year Sumit
Happy New Year Rohan
Happy New Year Sally
done!!
```

## Looking inside Lists:

_Just like strings we can get at any single element in a list using an index specified in square brackets []_

```python
friends = ['Sumit', 'Shreya', 'Sayan']
print(friends[1])

# output:
Shreya
```

## List are Mutable:

- Strings are 'immutable' - we cannot change the content of a string - we must make a new string to make any change

- Lists are 'mutable' - we can change element of a list using the index operator.

```python
fruit = 'Banana'
fruit[0] = 'b'

# output:
TypeError: 'str' object does not support item assignment

fruit = 'Banana'
x = fruit.lower()
print(x)

# output:
banana

lotto = [2, 14, 26, 41, 65]
print(lotto)

# output:
[2, 14, 26, 41, 65]

lotto[2] = 28
print(lotto)

# output:
[2, 14, 28, 41, 65]
```

## How long as a list?

- The len() function takes a list as a parameter and return the number of element in the list.

- Actually len() function tells us the number of elements of any set or sequence (such as a string...)

```python
greet = 'Hello Bob'
print(len(greet))

# output:
9

x = [1, 2, 'Sneha', 99]
print(len(x))

# output:
4
```

## Using range() function;

- The range() function returns a list of numbers that range from zero to one less than parameter.

- We can construct an index loop using for and an integer iterate

```python
print(range(4))
print(list(range(4)))

#output:
range(0, 4)
[0, 1, 2, 3]

friends = ['Sumit', 'Harry Bhai', 'Rahul']
print(len(friends))

# output:
3

print(list(range(len(friends))))

#output:
[0, 1, 2]
```

## A Tale of two loops:

```python
friends = ['Sneha', 'Tanmoy', 'Debjit']
for friend in friends:
    print('Happy New Year', friend)

# output;
Happy New Year Sneha
Happy New Year Tanmoy
Happy New Year Debjit

# try another way

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year', friend)

# output:
Happy New Year Sneha
Happy New Year Tanmoy
Happy New Year Debjit
```

# lecture 8 | 8.2 Manipulating Lists

## Concatenating lists using (+) operator

_we can create a new list by adding two existing list together_

```python
a = [1, 2 , 3]
b = [4, 5, 6]
c = a + b
print(c)
# output:
[1, 2, 3, 4, 5, 6]

print(a)

# output:
[1, 2, 3]
```

## Lists can be sliced using colon(:)

```python
lst = [9, 12, 41, 3, 74, 15]
print(lst[1:3])
print(lst[:4])
print(lst[3:])
print(lst[:])

# output:
[12, 41]
[9, 12, 41, 3]
[3, 74, 15]
[9, 12, 41, 3, 74, 15]
```

*just like in strings, the second number is upto but not including*

## List methods:

```python
x = list()
print(type(x))

# output:
<class 'list'>

print(dir(x))

# output:
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

## Building a list from scratch:

- *We can create an empty list and then add element using the append() method.*

- *The list stays in order and new elements are added at the end of the list.*

```python
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# output:
['book', 99]
['book', 99, 'cookie']
```

 ## Is something in a list:

 - *Python provides two operators that let you check if an item is in a list.*

 - *These are logical operators that returns True or False.*

 - *They do not modify the list.*

```python
same = [1, 9, 21, 10, 16]
print(9 in same)
print(15 in same)
print(20 not in same)
# output:
True
False
True
```

# Lists are in order:
- *A list can hold many items and keeps those items in the order until we do something to change the order.*

- *A list can be sorted (i.e. chage the order)*

- *The sort method (inlike in strings) means "sort yourself"*

```python
friends = ['Rohit', 'Sayan', 'Esha', 'Muskan']
friends.sort()
print(friends)
print(friends[2]) # output returns based on sorted result

# output:
['Esha', 'Muskan', 'Rohit', 'Sayan']
Rohit
```

## Built-in functions and lists:

- *There are a number of functions built into python that take lists is parameter.*

- *Remember theloops we built? - These are much simpler.*

```python
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums) / len(nums))

# output:
6
74
3
154
25.666666666666668
```

## Programs:

```python
total = 0
count = 0
print('After your input is done, then type "done", so that result will display')
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count +1

average = total / count
print('Average', average)

# output:
After your input is done, then type "done", so that result will display
Enter a number: 65
Enter a number: 34
Enter a number: 23
Enter a number: 53
Enter a number: 654
Enter a number: 23
Enter a number: 33
Enter a number: 54
Enter a number: done
Average 117.375
```

```python
numlist = []
print('When your input is done, then make sure please type "done"')

while True:
    inp = input('Enter number: ')
    if inp.lower() == 'done':  # Check if the user typed 'done'
        break
    try:
        num = float(inp)  # Try converting input to a number
        numlist.append(num)  # Add the number to the list
    except ValueError:
        print('Invalid input. Please enter a number or "done" to finish.')

average = sum(numlist) / len(numlist)
print('Average', average)

# output"
When your input is done, then make sure please type "done"
Enter number: 736
Enter number: 376
Enter number: 7
Enter number: 737
Enter number: 92
Enter number: 37
Enter number: done
Average 330.8333333333333

# Error handling output:
When your input is done, then make sure please type "done"
Enter number: 36  
Enter number: 43
Enter number: 23
Enter number: 43
Enter number: 33
Enter number: jhgjhj
Invalid input. Please enter a number or "done" to finish.
Enter number: dkj
Invalid input. Please enter a number or "done" to finish.
Enter number: done
Average 35.6
```







