# Lecture 7 | 7.1 Files

## File Processing:
- A text file can be through of as a sequence of lines.

### Opening a File:
- Before we can read the contents of the file, we must tell Python which file we are going to work with and what we will be doing with the file.
- This is done with the `open()` function.
- `open()` returns a “file handle” – a variable used to perform operations on the file.
- Similar to “File -> Open” in a word processor.

### Using `open()`:
```python
handle = open(filename, mode)
# Example:
fhand = open('example.txt', 'r')
print(fhand)
```
- Returns a handle used to manipulate the file.
- File name is a string.
- Mode is optional and should be `'r'` if we are planning to read the file and `'w'` if we are going to write the file.

#### What is a handle?

*In Python, a file handle is a reference to an open file, which allows a program to read from, write to, or manipulate the file. It acts as a connection between the Python application and the file stored on the disk.*

`**variable name** = **file handle**`

```python
file_handle = open('example.txt', 'r')
print(file_handle)
# Output:
<_io.TextIOWrapper name='example.txt' mode='r' encoding='cp1252'>

#change encoding type:
fhand = open('example.txt', 'r', encoding="utf-16") #we'll discuss later why utf-16 in necessary.

#output:
<_io.TextIOWrapper name='example.txt' mode='r' encoding='utf-16'>
```

#### When a File is Missing:
```python
fhand = open('stuff.txt')
# Output:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'stuff.txt'
```

## The Newline Character:
- We use a special character called the “newline” to indicate when a line ends.
- We represent it as `\n` in strings.
- Newline is still one character – not two.
```python
stuff = 'hello\nsumit'
print(stuff)
# Output:
hello
sumit

stuff = 'x\ny'
print(stuff)
# Output:
x
y

len(stuff)
# Output:
3
```

### File Processing Example:
```text
From: sumitpaul@cloudadda.net
To: Sumit Paul <sumitpaul27202@gmail.com>
Subject: mail check
Message-ID: <19b8c18bd141012a15e2f9ac48c6ddf6@cloudadda.net>
X-Sender: sumitpaul@cloudadda.net
Disposition-Notification-To: sumitpaul@cloudadda.net
X-Priority: 1 (Highest)
```

- A text file has newlines at the end of each line.

```text
From: sumitpaul@cloudadda.net\n
To: Sumit Paul <sumitpaul27202@gmail.com>\n
Subject: mail check\n
Message-ID: <19b8c18bd141012a15e2f9ac48c6ddf6@cloudadda.net>\n
```


## Lecture 7.2 | Processing Files

### File Handle as a Sequence:
- A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence.
- We can use the `for` statement to iterate through a sequence.
- Remember – sequence is an ordered set.

#### Example:
```python
#read line through "for loop"
xfile = open("example.txt")
for line in xfile:
    print(line)
```
**output:**
```text
Creating a file via the terminal can be done using several commands, depending on your operating system and shell. Here are the most common methods:

Creating a file via the terminal can be done using several commands, depending on your operating system and shell. Here are the most common methods:

Creating a file via the terminal can be done using several commands, depending on your operating system and shell. Here are the most common methods:



From: sumitpaul@cloudadda.net mon jan 4 2024 18:57:09
```

### Counting Lines in a File:
```python
line = open("example.txt")
count = 0
for i in line:
    count += 1
print("Total lines in that file: ", count)

#output:
Total lines in that file:  5
```

#### Note:
- Each newline character (`\n`) adds to the line count, whether or not there’s visible content on the line.

### Reading the Whole File:
- We can read the whole file (newlines and all) into a single string.
```python
#count characters
file = open("example.txt")
con_file = file.read()
print(len(con_file)) 

#output:
1544
```

```python
#use indexing if needed
file = open("example.txt")
con_file = file.read()
print(con_file[:34])

#output:
Creating a file via the terminal c
```

```python
#read file
file = open("example.txt")
con_file = file.read()
print(con_file)

#output:
Creating a file via the terminal can be done using several commands, depending on your operating system and shell. Here are the most common methods:
Creating a file via the terminal can be done using several commands, depending on your operating system and shell. Here are the most common methods:
Creating a file via the terminal can be done using several commands, depending on your operating system and shell. Here are the most common methods:
From: sumitpaul@cloudadda.net mon jan 4 2024 18:57:09
```

### Searching Through a File:

*We can put an "if statement" in our "for loop" to only print lines that meet some criteria.*
#### Example:
```python
file = open("example.txt")
for i in file:
    if i.startswith("From: "):
        print(i)

#output:
From: sumitpaul@cloudadda.net mon jan 4 2024 18:57:09
```

### Searching Without Whitespaces:

- *We can strip the white space from the right-hand side of the string using rstrip() from the string library.*

- *The new line is cnsidered "white space" and is stripped.*

```python
file = open("example.txt")
for i in file:
    i = i.rstrip()
    if i.startswith("From: "):
        print(i)

#output:
From: sumitpaul@cloudadda.net mon jan 4 2024 18:57:09
```

### Skipping with `continue`:

*We can conveniently skip a line by using the "continue" statement.*

```python
file = open("example.txt")
for i in file:
    i = i.rstrip()
    if not i.startswith("From: "):
        continue
    print(i)

#output:
From: sumitpaul@cloudadda.net mon jan 4 2024 18:57:09
```

### Using `in` to Select Lines:

*We can look for a string anywhere in a line as our selection criteria.*

```python
file = open("example.txt")
for i in file:
    i = i.rstrip()
    if "sumitpaul@cloudadda.net" not in i:
        continue
    print(i)

#output:
From: sumitpaul@cloudadda.net mon jan 4 2024 18:57:09
```

### Prompt for File Name:
```python
file_name = input("Enter file name: ")
file_handle = open(file_name)
count = 0
for i in file_handle:
    if i.startswith("Subject: "):
        print(i)
        count += 1
print("There were", count, "Subject lines in", file_name)

#output:
Enter file name: example.txt
Subject: Business enquiry
There were 1 Subject lines in example.txt
```

### Handling a Bad File Name:
```python
file_name = input("Enter file name: ")
try:
    file = open(file_name)
except:
    print("File cannot open", file_name)
    quit()
count = 0
for i in file:
    if i.startswith("Subject: "):
        print(i)
        count += 1
print("There were", count, "subject line in", file_name)

#when file is successfully open and fetch data, output like:
Enter file name: example.txt
Subject: Business enquiry
There were 1 subject line in example.txt

#when user input is not understandable then handle that error
Enter file name: dasfe
File cannot open dasfe
```

