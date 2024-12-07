# Lecture 10 | Tuples

## Tuples are like lists:
*Tuples are another kind of sequence that functions much like a list - they have clements which are indexed starting at 0*

```python
x = ('sumit', 'sherya', 'akhil')
print(x[2])
y = (1, 6, 34, 3)
print(max(y))

for catch in y:
    print(catch)

#output:
akhil
34
1
6
34
3
```

## But tuple are immutable:

*Unlike a list, once you create a tuple, you cannot alter it constants - similar to string*

```python
x = [9, 8, 7]
x[0] = 6
print(x)

#output:
[6, 8, 7]

y = 'ABC'
y[2] = 'd'
print(y)

#output:
TypeError: 'str' object does not support item assignment

z = (5, 4, 3)
z[2] = 0
print(z)

#output:
TypeError: 'tuple' object does not support item assignment
```

## Things not to do with Tuple:

```python
>>> x = (3, 2, 1)
>>> x.sort()

#output:
AttributeError: 'tuple' object has no attribute 'sort'

>>> x.append()

#output:
AttributeError: 'tuple' object has no attribute 'append'

>>> x.reverse()

#output:
AttributeError: 'tuple' object has no attribute 'reverse'
```

## A tale of Two sequence:

```python
>>> x = tuple()
>>> dir(x)

#output
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

## on this output there are clearly mention, you can only perform that "'count', 'index'"

## In Python, 'count' and 'index' are methods associated with sequence types, such as lists, tuples, and strings.
```

```python
>>> x = list()
>>> dir(x)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

## same way available methods on list

## "'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'"
```

## Tuple are more efficient:

- *since python does not have to build tuple structure to be modifiable, they are simpler and more efficient in term of memory use and performance.*

- *So in our program when we are making "temporary variables", we prefer tuples over list.*

## Tuples and assignments:

- *We can also put a tuple on the left hand side of an assignment statement.*

- *We can even omit the parentheses.*

```python
(x, y) = (4, 'fred')
print(x)

#output:
4

(a, b) = (98, 99)
print(b)

#output:
99
```

## Tuples and Dictionaries:

*The items() method in dictionaries return a list of (key, value) tuple.*

```python
d = dict()
d['sumit'] = 33
d['python'] = 1

for (k, v) in d.items():
    print(k, v)

#output:
sumit 33
python 1

tups = d.items()
print(tups)

#output:
dict_items([('sumit', 33), ('python', 1)])
```

## Tuples are comparable:

*The comparison operator work with tuples and other sequence. If the first item is equal, python goes on to the next element, and so on, until it finds element that differ.*

```python
a = (0, 1, 2)
b = (5, 1, 2)
c = a < b
print(c)

#output:
True

a = (0, 1, 200000)
b = (0, 3, 4)
c = a < b
print(c)

#output:
True

a = ('Jones', 'Sally')
b = ('Jones', 'Sam')
c = a < b
print(c)

#output:
True

a = ('Jones', 'Sally')
b = ('Jones', 'Sam')
c = a > b
print(c)

#output:
False
```

## Sorting Lists of Tuples:

- *We can take advantages of the ability to sort a list of tuples to get a sorted version of a dictionary.*

- *First we sort the dictionary by the key using the items() method and sorted() function.*

```python
d = {'a' : 10, 'c' : 22, 'b' : 1}
e = d.items()
f = sorted(d.items())
print(e)
print(f)

#output:
dict_items([('a', 10), ('c', 22), ('b', 1)])
[('a', 10), ('b', 1), ('c', 22)] #sorted items
```

## Using sorted:

*We can do this even more directly using the built-in function sorted that takes a sequence as a parameter and returns a sorted sequence.*

```python
d = {'b' : 1, 'c' : 22, 'a' : 10}
t = sorted(d.items())
print(t)

#output:
[('a', 10), ('b', 1), ('c', 22)]

for k, v in sorted(d.items()):
    print(k, v)

#output:
a 10
b 1
c 22
```

## Sort by values instead of key:

- *If we could construct a list of tuples of the form (value, key), we could sort by value.*

- *We do this with a "for loop" that creates a list of tuples.*

```python
c = {'a' : 10, 'b' : 1, 'c' : 22}

tmp = list()

for k, v in c.items():
    tmp.append((v, k))
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)

#output:
[(10, 'a'), (1, 'b'), (22, 'c')]
[(22, 'c'), (10, 'a'), (1, 'b')]
```


```python
fhand = open('mbox.txt', encoding='utf-16')
count = dict()

for line in fhand:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

lst = list()
for key, value in count.items():
    newtup = (value, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for value, key in lst:
    print(key, value)

#output:
world 5
python 4
tensorflow 2
hello 2
pandas 1

#sample file content for that code execution: example.txt
hello world hello python world world world world python python tensorflow tensorflow pandas python
```

```python
# Grand Father of previous code
c = {'a' : 10, 'b' : 1, 'c' : 22}
print(sorted([(v, k) for k,v in c.items()]))

#output:
[(1, 'b'), (10, 'a'), (22, 'c')]
```


| **Aspect**               | **UTF-8**                                                      | **UTF-16**                                                      |
|--------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| **Definition**            | A variable-length encoding standard using 1 to 4 bytes per character. | A fixed-length encoding standard using 2 bytes per character, with surrogate pairs for characters beyond the Basic Multilingual Plane. |
| **Purpose**               | To efficiently encode text in many languages, especially for languages that primarily use ASCII characters (like English). | To efficiently represent a large range of characters, particularly non-ASCII characters (like those in Chinese, Japanese, etc.). |
| **Memory Usage**          | Efficient for texts with mostly ASCII characters (uses 1 byte for common characters, up to 4 bytes for others). | Uses 2 bytes for most characters, leading to higher memory usage for texts that use many ASCII characters. |
| **Character Range**       | Supports up to 1,114,112 characters (1-4 bytes per character). | Supports up to 65,536 characters (2 bytes, with surrogate pairs for beyond-BMP characters). |
| **Real-Life Example**     | **Websites and Files**: HTML, JSON, XML, and most web content use UTF-8 because it's space-efficient for English and works well with global character sets. | **Windows File Systems**: Windows operating systems use UTF-16 internally for encoding text (e.g., file paths, registry keys). |
| **Usage in Programming**  | Commonly used in web programming, databases, and APIs. **Languages** like Python, JavaScript, and Go default to UTF-8 encoding for source code and file handling. | Common in Windows systems and environments like Java and .NET. **Languages** like C# often use UTF-16 for strings. |
| **Efficiency**            | Very efficient for English and other Latin-based alphabets (1 byte per character). | More efficient for languages that use characters outside the Latin alphabet (e.g., Chinese, Japanese), but can be inefficient for text with many ASCII characters (2 bytes per character). |
| **Problems**              | **Character Encoding Conflicts**: If a file encoded in UTF-8 is opened in a system expecting UTF-16, the result might be garbled or have incorrect characters. <br> **Overhead for non-ASCII text**: Non-ASCII characters can use more than 1 byte, which increases file size. | **Inefficient for English**: For text with many English characters, UTF-16 takes up more space (2 bytes per character). <br> **Surrogate Pairs**: Characters outside the BMP (e.g., some emoji) require 4 bytes, which adds complexity when handling or processing these characters. |
| **Advantages**            | - Space-efficient for text with mostly ASCII characters.<br>- Widely used on the web (e.g., websites, JSON files, HTML).<br>- Backward compatible with ASCII. | - More efficient for texts with a high number of non-ASCII characters.<br>- Supports a wide range of characters directly (e.g., most languages). |
| **Disadvantages**         | - Can become less efficient for non-Latin languages.<br>- If misinterpreted, may cause issues with text rendering (especially if the wrong encoding is assumed). | - More space-consuming for texts that predominantly use ASCII characters.<br>- Handling surrogate pairs can be complex. |

### **Real-Life Problems and Examples**:
1. **UTF-8 Example (Problem)**:
   - **Problem**: A website may use UTF-8 to display content but someone saves the file in UTF-16 encoding without proper conversion, causing the content to appear as strange symbols (e.g., `ÿþ` or random characters).
   - **Solution**: Use a consistent encoding system for all files and make sure web servers and browsers support UTF-8 properly.

2. **UTF-16 Example (Problem)**:
   - **Problem**: A user on a Windows system with UTF-16 encoding tries to open a file encoded in UTF-8, and the text appears incorrectly (such as `ÿþhello` instead of `hello`).
   - **Solution**: Ensure proper encoding handling, especially when switching between platforms or systems that may default to UTF-8 or UTF-16.

### Summary:
- **UTF-8** is great for general use, especially for web content and applications dealing with English or mixed languages, as it’s more memory-efficient for these cases.
- **UTF-16** is ideal for environments where non-ASCII characters are more frequent, such as applications handling Asian scripts (Chinese, Japanese) or when working with Windows APIs.
