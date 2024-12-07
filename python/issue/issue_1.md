# Issues i faced....when i started learning python

## faces issues on tuples

### issue:

```python
x = ('sumit', 'sherya', 'akhil')
print(x[2])
y = (1, 6, 34, 3)
print(max(y))

for catch in y:
    print(catch)
    con_str = catch
    con_str = str(catch)
    print(max(con_str))
    print(min(con_str))
```

### break-down the issue in bullet point format

- *Unnecessary conversion of integers to strings.*

- *Misleading behavior of max() and min() on strings due to lexicographical comparison.*

- *Potential confusion due to inconsistent handling of numeric vs. string types.*

- *Lack of clarity in the intent of string conversion for processing digits.*
