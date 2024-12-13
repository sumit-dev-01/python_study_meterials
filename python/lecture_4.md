# Lecture 4 | 4.1

## Function

### Stored and Reused Steps:
```python
def thing():
    print('hello')
    print('fun')

thing()
print('zip')
thing()
```
**Output:**
```
hello
fun
zip
hello
fun
```

### Definition:
- We call these reusable pieces of code **"functions"**.
- A function doesn’t run automatically; it needs to be invoked or called first.

### Python Built-in Functions:
```python
big = max('hello world')
print(big)
```
**Output:**
```
W
```

Another function is `min`:
```python
tiny = min('hello world')
print(tiny)
```
**Output:**
```
( ) (Blank space)
```

### How `max` and `min` Functions Work

#### On the Expression `big = max('hello world')`:

#### `max()` Function:
- The `max()` function returns the largest item in an iterable. Here, the iterable is the string `"hello world"`.
- In strings, Python compares characters based on their ASCII values.
- **ASCII** refers to American Standard Code for Information Interchange.

#### Execution:
- In the string `"hello world"`, characters are compared, and the one with the highest ASCII value is returned.
- **Space (`' '`)** has a lower ASCII value than any letter, so it is ignored in the comparison.
- Among the characters (`'h'`, `'e'`, `'l'`, `'o'`, `'w'`, `'r'`, `'d'`), the character `'w'` has the highest ASCII value.

#### Result:
- The variable `big` will be assigned `'w'`.

#### Why ASCII Values Matter:
- Python treats each character in the string as an individual entity, and ASCII values determine which character is greater.
- **Use of `max`:** This method is often used with numerical values or structured data but can also apply to strings for character comparisons.

**Example:**
```python
print(max('hello world'))
```
**Output:**
```
w
```

---

### What is ASCII?
ASCII is a character encoding standard used to represent text in computers and other devices that work with text.

#### Key Points:
1. **Purpose:**
   - ASCII assigns a unique numeric value (between 0 and 127) to each character, including letters, numbers, punctuation, and control characters.
   - This enables computers to store and communicate text-based data.

2. **Examples:**
   - `'A'` = ASCII value 65
   - `'a'` = ASCII value 97
   - `'0'` = ASCII value 48
   - `' '` (Space) = ASCII value 32

3. **Why It’s Useful:**
   - Computers understand numbers, not characters. ASCII provides a way to convert human-readable characters into numeric codes.

4. **Usage in Python:**
   - To get the ASCII value of a character: `ord('A') = 65`
   - To get the character from an ASCII value: `chr(65) = 'A'`
   
**Examples:**
```python
print(ord('A'))  # Output: 65
print(chr(65))   # Output: 'A'
```

#### Why Numbers Like ASCII Values Exist:
- Computers fundamentally understand only 0s and 1s (binary). These binary states represent off (`0`) and on (`1`) in digital systems.
- Higher-level abstractions like numbers and characters make programming and computing more human-friendly.
- ASCII bridges the gap between human understanding and machine language.

#### Relationship Between Binary and ASCII:
- The ASCII number itself is stored in binary in the computer.
- **Example:**
  - `65` (ASCII for `'A'`) is represented in binary as `0b1000001` (`0b` indicates binary format).
- This system allows computers to represent complex readable text and process it using logical syntax.

### How to Calculate Binary for Any Character:
1. **Find the ASCII Value:**
   - The ASCII value of `'A'` is 65 in decimal.
2. **Convert Decimal to Binary:**
   - To convert 65 to binary, divide the number by 2 repeatedly, recording the remainder at each step.
3. **Write the Remainder from Bottom to Top:**
   - This gives the binary equivalent.

**Example:**
- Calculate the binary equivalent of the ASCII value for `'A'` (65):
  1. Divide 65 by 2 → Quotient: 32, Remainder: 1
  2. Divide 32 by 2 → Quotient: 16, Remainder: 0
  3. Divide 16 by 2 → Quotient: 8, Remainder: 0
  4. Divide 8 by 2 → Quotient: 4, Remainder: 0
  5. Divide 4 by 2 → Quotient: 2, Remainder: 0
  6. Divide 2 by 2 → Quotient: 1, Remainder: 0
  7. Divide 1 by 2 → Quotient: 0, Remainder: 1

Write the remainders from bottom to top: **1000001**.
- The binary equivalent of 65 is **1000001**, which is also the ASCII representation of `'A'`.

---

# Lecture 4 | 4.2

## Building Functions

### Building Your Own Function:
- We create a new function using the `def` keyword followed by parameters in parentheses.
- Indent the body of the function.
- This defines the function but does not execute the body.

**Program:**
```python
def sumit_dev_01():
    print("CloudAdda builds AI that performs any data processing task in just seconds")
    print("Sumit, meanwhile me, is the creator of that AI")
    print("BIBO is the most advanced AI that only works for human help, completing tasks as fast as possible")

# Invoke function()
sumit_dev_01()
```
**Output:**
```
CloudAdda builds AI that performs any data processing task in just seconds
Sumit, meanwhile me, is the creator of that AI
BIBO is the most advanced AI that only works for human help, completing tasks as fast as possible
```

---

### Arguments:
- An **argument** is a value passed into the function as input when calling it.
- Arguments direct the function to perform different tasks at different times.
- We put arguments in parentheses after the function name.

**Example:**
```python
def sumit_dev_01(target):
    print(f"Future Target: {target}")

sumit_dev_01("Build a universal AI")
```

### Parameters:
- A **parameter** is a variable used in the function definition.
- It acts as a "handle" to access arguments passed during a particular function invocation.

**Example:**
```python
def cloudadda(role):  # 'role' is a parameter
    if role == 'CEO':
        print('SUMIT PAUL')
    else:
        print('Data not found')

cloudadda('CEO')  # 'CEO' is an argument
```
**Output:**
```
SUMIT PAUL
```

---

### Return Value:
- A function takes its arguments, performs some computation, and returns a value using the `return` keyword.

**Example:**
```python
def cloudadda():
    return "Sumit"

print(cloudadda(), "- GitHub Administrator")
print(cloudadda(), "- YouTube @cloudadda.001 channel's instructor")
```
**Output:**
```
Sumit - GitHub Administrator
Sumit - YouTube @cloudadda.001 channel's instructor
```

---

### Multiple Parameters/Arguments:
- We can define more than one parameter in a function.
- Add more arguments when calling the function.
- Match the number and order of arguments and parameters.

**Example:**
```python
def addtwo(a, b):  # Parameters
    added = a + b
    return added

x = addtwo(3, 5)  # Arguments
print(x)
```
**Output:**
```
8
```

## Create a dynamic table:

```python
count_table = int(input("enter a no. of table: "))
def multiply(counting):
    while counting <= 10:
        print(f"{count_table} x {counting} = {count_table * counting}")
        counting += 1

multiply(1)
```
**output**
```python
enter a no. of table: 13
13 x 1 = 13
13 x 2 = 26
13 x 3 = 39
13 x 4 = 52
13 x 5 = 65
13 x 6 = 78
13 x 7 = 91
13 x 8 = 104
13 x 9 = 117
13 x 10 = 130
```

# MOST EASY PROGRAM YOU'VE EVER SEEN BEFORE THIS!!😁

#### Here is a easy real-life program based on functions, incorporating advanced concepts like nested conditional statements, decorators, recursion, and error handling. This program simulates a real-world E-commerce system that calculates discounts, taxes, applies offers, and processes different types of customer orders. It also includes some advanced Python features such as lambda functions, higher-order functions, and exception handling.

```python
# Helper function: Calculate the total price of an item
def calculate_item_price(price, quantity, discount=0):
    """Calculates the total price of an item after applying a discount."""
    if price < 0 or quantity < 1:
        raise ValueError("Price must be positive, and quantity must be at least 1.")
    if not (0 <= discount <= 1):
        raise ValueError("Discount should be between 0 and 1.")
    return (price * quantity) * (1 - discount)

# Decorator: Logging order processing time
import time
def log_execution_time(func):
    """Logs the time taken by the function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Function to process discount based on customer type and category
def process_discount(cart_value, customer_type, category, coupon_code=None):
    """Applies discounts based on customer type, category, and available coupon."""
    discount = 0
    if customer_type == 'VIP':
        discount = 0.20  # 20% discount for VIP
    elif customer_type == 'Regular':
        discount = 0.10  # 10% discount for regular
    elif customer_type == 'Guest':
        discount = 0.05  # 5% discount for guests
    
    # Special discount for certain categories
    if category == 'Electronics' and cart_value > 10000:
        discount += 0.10  # Extra 10% off for electronics over ₹10,000
    
    # Apply coupon code if provided
    if coupon_code == "EXTRA10":
        discount += 0.10  # Apply an extra 10% discount

    # Ensure the discount is capped at 50%
    if discount > 0.50:
        discount = 0.50
    return discount

# Function to calculate taxes based on state and product type
def calculate_taxes(cart_value, state, product_type):
    """Calculates applicable taxes for an order based on state and product type."""
    tax_rate = 0.12  # Default tax rate
    if product_type == "Luxury":
        tax_rate = 0.18  # Luxury goods tax rate
    elif product_type == "Groceries":
        tax_rate = 0.05  # Lower tax for groceries
    
    if state == "California":
        tax_rate += 0.03  # California has an additional 3% tax
    
    return cart_value * tax_rate

# Function to apply shipping cost based on distance and urgency
def apply_shipping(cart_value, distance, urgency="Normal"):
    """Calculates shipping cost based on distance and urgency of the order."""
    shipping_cost = 0
    if urgency == "Urgent":
        shipping_cost += 200  # Urgent orders incur an extra ₹200
    if distance < 50:
        shipping_cost += 50  # ₹50 for local delivery
    elif distance < 200:
        shipping_cost += 150  # ₹150 for deliveries within 200 km
    else:
        shipping_cost += 300  # ₹300 for long-distance delivery

    # Shipping discount for high cart values
    if cart_value > 5000:
        shipping_cost *= 0.9  # 10% discount on shipping for cart value > ₹5000
    
    return shipping_cost

# Main function to calculate total order cost
@log_execution_time
def process_order(cart, customer_type, state, category, coupon_code=None, urgency="Normal", distance=0):
    """Calculates the final cost of an order based on various parameters."""
    total_value = 0
    
    # Calculate the total value of the cart after applying item-specific discounts
    for item in cart:
        try:
            total_value += calculate_item_price(item['price'], item['quantity'], item['discount'])
        except ValueError as e:
            print(f"Error in item {item['name']}: {e}")
            return None

    # Process customer discounts
    discount = process_discount(total_value, customer_type, category, coupon_code)
    total_value -= total_value * discount

    # Apply taxes based on state and product type
    taxes = calculate_taxes(total_value, state, category)
    total_value += taxes

    # Apply shipping costs
    shipping_cost = apply_shipping(total_value, distance, urgency)
    total_value += shipping_cost

    # Return the final calculated cost
    return total_value

# Input: Sample order and customer details
cart = [
    {"name": "Laptop", "price": 50000, "quantity": 1, "discount": 0.10},
    {"name": "Headphones", "price": 3000, "quantity": 2, "discount": 0.05},
    {"name": "Smartphone", "price": 15000, "quantity": 1, "discount": 0.15}
]

customer_type = input("Enter customer type (VIP/Regular/Guest): ").capitalize()
category = input("Enter category of items (Electronics/Groceries/Luxury): ").capitalize()
state = input("Enter state (California/New York/Other): ").capitalize()
coupon_code = input("Enter coupon code (if any): ").upper()
urgency = input("Enter urgency (Normal/Urgent): ").capitalize()
distance = int(input("Enter shipping distance in km: "))

# Process the order
final_cost = process_order(cart, customer_type, state, category, coupon_code, urgency, distance)

# Output the final cost
if final_cost is not None:
    print(f"\n--- Final Billing Details ---")
    print(f"Total Order Cost: ₹{final_cost:.2f}")
else:
    print("There was an error processing the order.")

```

### USED RAW-MATERIALS IN THAT BUILDING 🏗️

Here are the main bullet points without descriptions:

- Functions:
  - `calculate_item_price(price, quantity, discount=0)`
  - `log_execution_time(func)` (Decorator)
  - `process_discount(cart_value, customer_type, category, coupon_code=None)`
  - `calculate_taxes(cart_value, state, product_type)`
  - `apply_shipping(cart_value, distance, urgency="Normal")`
  - `process_order(cart, customer_type, state, category, coupon_code=None, urgency="Normal", distance=0)`

- Attributes/Variables:
  - `cart`
  - `customer_type`
  - `category`
  - `state`
  - `coupon_code`
  - `urgency`
  - `distance`

- Libraries:
  -`time`
  - `ValueError`

- Key Concepts:
  - Decorator (`log_execution_time`)
  - Exception Handling (`try` and `except`)
  - Conditionals (`if-else` statements)
  - Loops (`for loop`)
  - Default Parameters (`discount=0`)

- Data Structures:
  - List of Dictionaries (`cart`)
  - Dictionaries

- Calculations:
  - Price Calculation
  - Discount Calculation
  - Tax Calculation
  - Shipping Calculation

- Control Flow:
  - Conditional Statements (if-elif-else)
  - Capping Values

  