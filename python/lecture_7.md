
# Lecture 7 | 7.1 Files

## File Processing:
- A text file can be thought of as a sequence of lines.

### Opening a File:
- Before we can read the contents of the file, we must tell Python which file we are going to work with and what we will be doing with the file.
- This is done with the `open()` function.
- `open()` returns a “file handle” – a variable used to perform operations on the file.
- Similar to “File -> Open” in a word processor.

### Using `open`:
```python
handle = open(filename, mode)
# Example:
fhand = open('mbox.txt', 'r')
```
- Returns a handle used to manipulate the file.
- File name is a string.
- Mode is optional and should be `'r'` if we are planning to read the file and `'w'` if we are going to write the file.

#### What is a handle?
```python
fhand = open('mbox.txt')
print(fhand)
# Output:
<_io.TextIOWrapper name='mbox.txt' mode='r' encoding='UTF-8'>
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

### Reading the Whole File:
- We can read the whole file (newlines and all) into a single string.
```python
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))  # Output: 2296
print(inp[:20])  # Output: 'This is sample line'
```

## Lecture 7.2 | Processing Files

### File Handle as a Sequence:
- A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence.
- We can use the `for` statement to iterate through a sequence.
- Remember – sequence is an ordered set.

#### Example:
```python
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)
```

### Counting Lines in a File:
```python
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line count:', count)  # Output: Line count 61
```

#### Note:
- Each newline character (`\n`) adds to the line count, whether or not there’s visible content on the line.

### Searching Through a File:
#### Example:
```python
fhand = open('mbox-shorts.txt')
for line in fhand:
    if line.startswith('From: '):
        print(line)
```

### Searching Without Whitespaces:
```python
fhand = open('mbox-shorts.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)
```

### Skipping with `continue`:
```python
fhand = open('mbox-shorts.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From: '):
        continue
    print(line)
```

### Using `in` to Select Lines:
```python
fhand = open('mbox-shorts.txt')
for line in fhand:
    line = line.rstrip()
    if 'sumitpaul@cloudadda.net' not in line:
        continue
    print(line)
```

### Prompt for File Name:
```python
fname = input('Enter file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('There were', count, 'subject lines in', fname)
```

### Handling a Bad File Name:
```python
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('There were', count, 'subject lines in', fname)
```

