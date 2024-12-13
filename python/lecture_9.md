# Lecture 9 | 9.1 - Dictionaries

## What is a collection?

- *A collection is nice because we can put more than one value in it and carry them all around in one convenient package.*

- *We have a bunch of values in a single 'variable'.*

- *We do this by having more than one place in the variable.*

- *We have ways of finding the different places in the variable.*

## What is NOT a "Collection"?

- *Most of our variable have one value in them - when we put a new value in the variable - the old value is overwritten.*

```python
x = 2
print(x)
x = 4
print(x)

#output:
2
4
```

## A story of two collection:

### List:
*A linear collection of values lookup by position 0...length -1*

### Dictionaries:
*A linear collection of key-value pairs lookup by "tag" or "key"*

## Dictionaries:
- *Dictionaries are python's most powerful data collection*

- *Dictionaries allow us to do fast database like operations in python*

- *Similar concepts in different programming language*
    1. Associative Arrays - perl / PHP
    
    2. Properties or Map or HashMap - java

    3. Property Bag - c# / .Net

## Dictionaries over time in python:

- *Prior to python  3.7 dictionaries did not keep entries in the order of insertion* 

- *Python 3.7 (2018) and later dictionaries keep entries in the order they were inserted*

- *"Insertion 'order' is not" always sorted order*

## Below the obstraction:
- *Python lists dictionaries and tuples are 'abstract object' designed to be easy to use*

- *For now we will just understand them and use them and thank the creators of python for making that easy for us*

## List(review that only now)
- *We opened values to the end of a list and look them up by position*

- We insert values into a dictionaries using a key and retrieve them using a key

```python
cards = list() 
cards.append(12)
cards.append(323)
cards.append('sumit')
print(cards)
print(cards[1])
cards[0] = cards[0] + 3
print(cards)

#output:
[12, 323, 'sumit']
323
[15, 323, 'sumit']
```

## Dictionaries:
- *We append values to the end of a list and look them up by position*

- *We insert values into a dictionaries using a key and retrieve them using a key*

```python
cabinet = dict()
cabinet['summer'] = 12
cabinet['virant'] = 34
cabinet['pritha'] = 36
print(cabinet)
# type of variable
print(type(cabinet))
# value of "vikrant"
print(cabinet['virant'])
# update "pritha's" value pair 
cabinet['pritha'] = cabinet['pritha'] + 23
print(cabinet)

# output:
{'summer': 12, 'virant': 34, 'pritha': 36}
<class 'dict'>
34
{'summer': 12, 'virant': 34, 'pritha': 59}
```

## Comparing list and dictionaries:

*Dictionaries are like list, except that they use keys instead of number to lookup values*

### List:
```python
lst = list()
lst.append(21)
lst.append(25)
print(lst)
lst[0] = 334
print(lst)

# output:
[21, 25] # previous [0] indexing value pair
[334, 25] # updated value pair by indexing [0]
```

### Dictionary:

```python
ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
# updating age value by key pair
ddd['age'] = 34
print(ddd)

#output:
{'age': 21, 'course': 182} #previously assigned value pair
{'age': 34, 'course': 182} # now that's a updated value pair by key pair
```

## Dictionary literals:
- *Dictionary literals use curly braces "{}" and have a list of "key:value" pairs*

- *You can make an empty dictionary using empty curly braces "{}" or dict()*

```python
jjj = {'sumit' : 32, 'fred' : 36}
print(jjj)
ooo = {}
print(ooo)
print(type(ooo))

#output:
{'sumit': 32, 'fred': 36}
{}
<class 'dict'>
```

# Lecture 9 | 9.2 - Counting with Dictionaries

## Many counters with a Dictionary:

*One common use of dictionaries is counting how often we see something*

```python
ccc = dict()
ccc['book'] = 1
ccc['python'] = 1
print(ccc)
ccc['python'] = ccc['python'] + 34
print(ccc)

#output:
{'book': 1, 'python': 1}
{'book': 1, 'python': 35}
```

## Dictionary Traceback:
- *It is an error to reference a key which is not in the dictionary*

- *We can use the "in" operator to see if key is in the dictionary*

```python
ccc = dict()
print(ccc['python'])

#output:
KeyError: 'python'
```

```python
print('python' in ccc)

#output:
False
```

- *We use True or False related output so that we can't get an error*

- *use "in" operator for checking something if there is available or not*

## When we see a new name:

```python
counts = dict()
names = ['python', 'tensorflow', 'python', 'flask', 'tensorflow']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#output:
{'python': 2, 'tensorflow': 2, 'flask': 1}
```

## The get() method for dictionaries:

- *The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common that there is a method called get() that does this for us*

- *Default value if the key does not exist nad no traceback*


### Simplified counting with get():

```python
count = dict()
names = ['python', 'tensorflow', 'python', 'pandas', 'numpy', 'tensorflow']

for name in names:
    count[name] = count.get(name, 0) + 1
print(count)

#output:
{'python': 2, 'tensorflow': 2, 'pandas': 1, 'numpy': 1}
```

*We can use get() and provide a default value of zero(0) when the is not yet in the dictionary - and then add 1(one value)*


# Lecture 9 | 9.3 - Dictionaries and Files

## Counting pattern:

```python
count = dict()
print('Enter a line of text : ')
line = input('')

words = line.split()
print('word: ', words)
print("Boss give me 2 second, i'll ready this file for you!")
print('countint words....')

for word in words:
    count[word] = count.get(word, 0) + 1
print('countings: ', count)
print('Done boss!!')

#output:
Enter a line of text : 
We insert values into a dictionaries using a key and retrieve them using a key
word:  ['We', 'insert', 'values', 'into', 'a', 'dictionaries', 'using', 'a', 'key', 'and', 'retrieve', 'them', 'using', 'a', 'key']
Boss give me 2 second, i'll ready this file for you!
countint words....
countings:  {'We': 1, 'insert': 1, 'values': 1, 'into': 1, 'a': 3, 'dictionaries': 1, 'using': 2, 'key': 2, 'and': 1, 'retrieve': 1, 'them': 1}
Done boss!!
```

*The general pattern of count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of each word independently*

## Definite loops and Dictionaries:

*Even through dictionaries are not started order, we can write a "for loop" that goes through all the entries in a dictionary - actually it goes through all of the keys in the dictionary and look up the values*

```python
count = {'sumit' : 1, 'fred' : 32, 'janee' : 23}
for key in count:
    print(key, count[key])

#output:
sumit 1
fred 32
janee 23
```

## Retrieving lists of keys and values:

*You can get a list of keys, values or items(both) from a dictionary*

```python
jjj = {'sumit' : 23, 'suman' : 54, 'samm' : 34}
print(list(jjj))

#print keys():
print(list(jjj.keys()))

#print values():
print(list(jjj.values()))

#print items():
print(list(jjj.items()))

#output:
['sumit', 'suman', 'samm']
['sumit', 'suman', 'samm'] #keys
[23, 54, 34] #values
[('sumit', 23), ('suman', 54), ('samm', 34)] #items
```

## BONUS: Two iteration variables

- *We loop through the key-value pair in a dictionary using **two** iteration variables*

- *Each iteration, the first variable is the key and second variable is the corresponding value for the key*

```python
jjj = {'sumit' : 34, 'sayani' : 56, 'kushal' : 53}
for aaa, bbb in jjj.items():
    print(aaa, bbb)

#output:
sumit 34
sayani 56
kushal 53
```

## Know most frequent word in dectionary:

```python
name = input('enter file name: ')
handle = open(name)

count = dict()
for line in handle:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) +1
big_count = None
big_word = None

for word, count in count.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count
print(big_count, big_word)

#output:
5 world

# sample_file.txt content
hello world hello python world world world world python python
```

## HOW TO DEAL 🫱🏻‍🫲🏻 WITH AI's UNSTRUCTURE DATA
```python
import pandas as pd
from datetime import datetime

# Sample unstructured data (like chatbot conversation logs)
unstructured_data = [
    {"timestamp": "2024-12-13T10:01:00", "user": "John", "message": "Hi there!"},
    {"timestamp": "2024-12-13T10:01:30", "user": "AI", "message": "Hello! How can I assist you today?"},
    {"timestamp": "2024-12-13T10:02:00", "user": "John", "message": "I need help with data science."},
    {"timestamp": None, "user": "AI", "message": "Sure! What specific topic are you interested in?"}
]

# Function to process the unstructured data
def process_data(unstructured_data):
    # Create a DataFrame from the unstructured data
    df = pd.DataFrame(unstructured_data)

    # Convert the 'timestamp' to a standard datetime format (ISO format)
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

    # Fill missing timestamps with the previous timestamp (or a default value, here we use current time)
    df['timestamp'].fillna(datetime.now(), inplace=True)

    # Handle missing values for 'user' and 'message' columns
    df['user'].fillna('Unknown User', inplace=True)
    df['message'].fillna('No message provided', inplace=True)

    # Ensure the data is sorted by timestamp
    df = df.sort_values(by='timestamp')

    # Return the structured DataFrame
    return df

# Process the data
structured_data = process_data(unstructured_data)

# Save the structured data to a CSV file for future analysis
structured_data.to_csv('structured_chatbot_data.csv', index=False)

# Display the structured data
print(structured_data)
```

```python
#output
                   timestamp  user                                           message
0 2024-12-13 10:01:00.000000  John                                         Hi there!
1 2024-12-13 10:01:30.000000    AI                Hello! How can I assist you today?
2 2024-12-13 10:02:00.000000  John                    I need help with data science.
3 2024-12-13 19:21:02.064450    AI  Sure! What specific topic are you interested in?
```