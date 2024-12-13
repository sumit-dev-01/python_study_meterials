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
```

# MOST EASIEST REAL LIFE EXAMPLES ON CONDITIONAL STATRMENTS | ROCK ON 😎👍🏼:

## Example 1:
### Student Grading System
```text
Question:
Student Grading System

You are required to write a Python program that takes a student's exam score as input and categorizes the score into different grades. The program should work as follows:

If the score is exactly 100, print: "Perfect! You scored 100%. Excellent work!".
If the score is 90 or higher, print: "Great job! You scored an A.".
If the score is 80 or higher, print: "Good work! You scored a B.".
If the score is 70 or higher, print: "Not bad! You scored a C.".
If the score is 60 or higher, print: "You passed! You scored a D.".
If the score is below 60, print: "You failed the exam. Better luck next time.".
Instructions:

Accept the student's score as an integer input.
Use conditional statements (if, elif, else) to print the appropriate message based on the score.
Example Input/Output:

Input: 85
Output: Good work! You scored a B.
```

```python
#___code___

# Input: Student's score
score = int(input("Enter your exam score: "))

# Conditional statements to determine the grade
if score == 100:
    print("Perfect! You scored 100%. Excellent work!")
elif score >= 90:
    print("Great job! You scored an A.")
elif score >= 80:
    print("Good work! You scored a B.")
elif score >= 70:
    print("Not bad! You scored a C.")
elif score >= 60:
    print("You passed! You scored a D.")
else:
    print("You failed the exam. Better luck next time.")
```

## Example 2:
### Car Rental Pricing System
```text
Car Rental Pricing System
You are asked to create a car rental pricing system. The program will take the following inputs:

Age of the customer: Determines if the customer qualifies for a special rate or is eligible for renting certain types of cars.
Car type: The customer can rent either a "Sedan", "SUV", or "Luxury" car.
Rental duration (in days): The number of days the customer intends to rent the car.
Based on these inputs, calculate the total rental price. The rules are as follows:

Age:
If the customer is under 18, they cannot rent any car.
If the customer is 18-25, they can rent a car, but must pay an extra 10% surcharge on all car types.
If the customer is 26 or older, they can rent any car without additional charges.
Car type:
Sedan: ₹500/day
SUV: ₹800/day
Luxury: ₹1200/day
Rental duration:
If the rental duration exceeds 7 days, offer a 15% discount on the total price.
```

```python
age = int(input("Enter your age: "))
if age < 18:
    print(f"You must be at least 18 years old to rent a car. You are currently {age} years old.")
    exit()

car_type = input("Enter car type (Sedan/SUV/Luxury): ").lower()  # Convert input to lowercase for consistent comparison
try:
    rental_duration = int(input("Enter rental duration in days: "))
except:
    print("Please a valid input")
    exit()

# Price per day based on car type
if car_type == "sedan":
    price_per_day = 500
elif car_type == "suv":
    price_per_day = 800
elif car_type == "luxury":
    price_per_day = 1200
else:
    print("Invalid car type.")
    exit()

# Age-related surcharges
if age <= 25:
    surcharge = 0.10  # 10% surcharge for ages 18-25
else:
    surcharge = 0  # No surcharge for ages 26 and older

# Calculate base price
base_price = price_per_day * rental_duration

# Apply surcharge based on age
total_price = base_price + (base_price * surcharge)

# Apply discount if rental duration is more than 7 days
if rental_duration > 7:
    total_price -= total_price * 0.15  # 15% discount

# Output the total price
print(f"Total rental price: ₹{total_price:.2f}")
```

## Example 3:
### Loan Eligibility System

```text
Age: Minimum age requirement for different loan types.
Income: Minimum income required for certain loans.
Credit score: Impacts loan eligibility.
Employment status: Employment status and job duration.
Loan amount requested: Determines eligibility based on the loan amount.
This program will involve:

Multiple if, elif, and else conditions.
Nested conditions (conditions within conditions).
Multiple criteria to determine loan eligibility.
Loan Eligibility System
Criteria:
Age:

For personal loans, the customer must be at least 21 years old.
For home loans, the customer must be at least 25 years old.
For business loans, the customer must be at least 28 years old.
Income:

Personal loan: Minimum income of ₹30,000 per month.
Home loan: Minimum income of ₹50,000 per month.
Business loan: Minimum income of ₹70,000 per month.
Credit Score:

A credit score of 750 or higher qualifies the customer for any loan without conditions.
A score between 600 and 749 requires verification of additional factors like employment and loan amount.
A score below 600 is not eligible for a loan.
Employment:

Must be employed for at least 1 year for personal loans, 2 years for home loans, and 3 years for business loans.
Self-employed individuals have different conditions based on their business income.
Loan Amount Requested:

Personal loan: Up to ₹5,00,000.
Home loan: Up to ₹1,00,00,000.
Business loan: Up to ₹50,00,000.
```

```python
# Input: Customer's details
age = int(input("Enter your age: "))
credit_score = int(input("Enter your credit score: "))
income = int(input("Enter your monthly income: "))
employment_status = input("Are you employed or self-employed? (Employed/Self-employed): ").lower()
years_of_employment = int(input("How many years have you been employed/self-employed? "))
loan_type = input("Enter the loan type (Personal/Home/Business): ").lower()
loan_amount = int(input("Enter the loan amount requested: "))

# Eligibility for loan
if credit_score < 600:
    print("Sorry, you are not eligible for a loan due to your credit score being too low.")
elif age < 21:
    print("You must be at least 21 years old for a Personal loan.")
elif loan_type == "personal":
    if income < 30000:
        print("You do not meet the minimum income requirement for a Personal loan.")
    elif loan_amount > 500000:
        print("The loan amount exceeds the maximum limit for a Personal loan.")
    elif years_of_employment < 1:
        print("You must have at least 1 year of employment for a Personal loan.")
    else:
        print("You are eligible for a Personal loan.")
elif loan_type == "home":
    if age < 25:
        print("You must be at least 25 years old for a Home loan.")
    elif income < 50000:
        print("You do not meet the minimum income requirement for a Home loan.")
    elif loan_amount > 100000000:
        print("The loan amount exceeds the maximum limit for a Home loan.")
    elif years_of_employment < 2:
        print("You must have at least 2 years of employment for a Home loan.")
    else:
        print("You are eligible for a Home loan.")
elif loan_type == "business":
    if age < 28:
        print("You must be at least 28 years old for a Business loan.")
    elif income < 70000:
        print("You do not meet the minimum income requirement for a Business loan.")
    elif loan_amount > 50000000:
        print("The loan amount exceeds the maximum limit for a Business loan.")
    elif years_of_employment < 3:
        print("You must have at least 3 years of employment for a Business loan.")
    else:
        print("You are eligible for a Business loan.")
else:
    print("Invalid loan type entered.")
```

## Example 4:
### Advanced Shopping Cart Price Calculation

```text
Inputs Required:
Membership Type: The customer can be a Regular, Prime, or Guest member.
Cart Value: Total value of items in the cart.
Purchase Category: Choose from Electronics, Clothing, or Groceries.
Payment Method: Options include Credit/Debit Card, Wallet, or EMI.
Special Occasion Sale: Indicate if a special sale is ongoing (Yes/No).
Customer Location: Specify if the customer resides in a metro city (Yes/No).

Billing Rules to Apply:

Membership Discounts:
Prime: 15%, Regular: 10%, Guest: 5%.

Cart Value-Based Discounts:
Carts over ₹10,000: 20%.
Carts between ₹7,000 and ₹9,999: 15%.
Carts between ₹5,000 and ₹6,999: 10%.

Category-Based Discounts:
Electronics: 25% for cart values over ₹15,000, otherwise 10%.
Clothing: 30% flat discount.
Groceries: 5% for cart values over ₹2,000, otherwise 2%.

Payment Surcharges:
Credit/Debit Card: No surcharge.
Wallet: 2% surcharge.
EMI: 5% surcharge.

Special Occasion Discounts:
Electronics: Extra 10%.
Clothing: Extra 20%.
All other categories: Extra 5%.

Shipping Costs:
Metro city: Free shipping.
Non-metro city:
Cart value below ₹3,000: ₹100 shipping.
Cart value ₹3,000 and above: ₹50 shipping.
Discount Cap: Total discounts should not exceed 50%.
```

```python
# Input user details
membership = input("Enter your membership type (Regular/Prime/Guest): ").lower()
cart_value = float(input("Enter the total cart value: ₹"))
category = input("Enter the category of your purchase (Electronics/Clothing/Groceries): ").lower()
payment_method = input("Enter payment method (Credit/Debit Card/Wallet/EMI): ").lower()
special_occasion = input("Is there a special occasion sale? (Yes/No): ").lower()
location = input("Are you from a metro city? (Yes/No): ").lower()

# Initialize discounts and surcharges
membership_discount = 0
cart_discount = 0
category_discount = 0
payment_surcharge = 0
special_discount = 0
shipping_cost = 0

# Membership-based discounts
if membership == "prime":
    membership_discount = 0.15  # 15% for Prime members
elif membership == "regular":
    membership_discount = 0.10  # 10% for Regular members
elif membership == "guest":
    membership_discount = 0.05  # 5% for Guests
else:
    print("Invalid membership type.")
    exit()

# Cart value-based discounts (nested logic)
if cart_value >= 5000:
    if cart_value >= 10000:
        cart_discount = 0.20  # 20% discount for carts over ₹10,000
    elif cart_value >= 7000:
        cart_discount = 0.15  # 15% discount for carts between ₹7000 and ₹9999
    else:
        cart_discount = 0.10  # 10% discount for carts between ₹5000 and ₹6999

# Category-based discounts
if category == "electronics":
    if cart_value >= 15000:
        category_discount = 0.25  # 25% discount for electronics over ₹15,000
    else:
        category_discount = 0.10  # 10% discount for electronics
elif category == "clothing":
    category_discount = 0.30  # 30% discount for clothing
elif category == "groceries":
    if cart_value >= 2000:
        category_discount = 0.05  # 5% discount for groceries over ₹2,000
    else:
        category_discount = 0.02  # 2% discount for groceries
else:
    print("Invalid category.")
    exit()

# Payment method logic
if payment_method == "credit/debit card":
    payment_surcharge = 0  # No surcharge
elif payment_method == "wallet":
    payment_surcharge = 0.02  # 2% surcharge for wallet payments
elif payment_method == "emi":
    payment_surcharge = 0.05  # 5% surcharge for EMI
else:
    print("Invalid payment method.")
    exit()

# Special occasion discounts
if special_occasion == "yes":
    if category == "electronics":
        special_discount = 0.10  # Extra 10% discount for electronics on special occasions
    elif category == "clothing":
        special_discount = 0.20  # Extra 20% discount for clothing
    else:
        special_discount = 0.05  # Extra 5% discount for other categories

# Shipping costs based on location
if location == "yes":
    shipping_cost = 0  # Free shipping for metro cities
else:
    if cart_value < 3000:
        shipping_cost = 100  # ₹100 shipping for non-metro with low cart value
    else:
        shipping_cost = 50  # ₹50 shipping for non-metro with higher cart value

# Calculate total discounts
total_discount = membership_discount + cart_discount + category_discount + special_discount
if total_discount > 0.50:  # Cap the total discount at 50%
    total_discount = 0.50

# Calculate the final price
price_after_discounts = cart_value * (1 - total_discount)
final_price = price_after_discounts + (price_after_discounts * payment_surcharge) + shipping_cost

# Output the result
print("\n--- Final Billing Details ---")
print(f"Cart Value: ₹{cart_value:.2f}")
print(f"Total Discount Applied: ₹{cart_value * total_discount:.2f}")
print(f"Price After Discounts: ₹{price_after_discounts:.2f}")
print(f"Payment Surcharge: ₹{price_after_discounts * payment_surcharge:.2f}")
print(f"Shipping Cost: ₹{shipping_cost:.2f}")
print(f"Final Price to Pay: ₹{final_price:.2f}")
```

## Example 5:
### Advanced Healthcare Billing System

```text
Inputs Required:
Patient Type: Emergency, In-Patient, or Out-Patient.
Treatment Type: Surgery, Diagnostic, or Consultation.
Room Type: General, Semi-Private, Private, or ICU.
Doctor Category: Specialist, Consultant, or Resident.
Insurance Coverage: Percentage covered by insurance (0-100%).
Membership Status: Indicate if the patient is a premium hospital member (Yes/No).
Days Admitted: Applicable for in-patients only.

Billing Rules:
1. Base Treatment Costs:
Emergency Surgery: ₹1,00,000.
Non-Emergency Surgery: ₹75,000.
Diagnostic Tests: ₹15,000.
Consultation: ₹5,000.

2. Room Costs (Per Day):
General: ₹2,000.
Semi-Private: ₹5,000.
Private: ₹10,000.
ICU: ₹25,000.

3. Doctor's Fees:
Specialist: ₹20,000.
Consultant: ₹15,000.
Resident: ₹8,000.

4. Emergency Surcharge:
Surgery: 20% of the treatment cost.
Diagnostic: 10% of the treatment cost.
Consultation: ₹1,000 flat surcharge.

5. Membership Discounts:
Premium members in Private/ICU rooms: 15% of the treatment cost.
Other cases: 10% of the treatment cost.

6. Insurance Coverage:
Reduces the total cost by the entered insurance percentage.

7. Extended Stay Fee:
For in-patients admitted for more than 5 days, add ₹500 per additional day.

Your Task:
Take all the inputs from the user (as described above).
Calculate the total cost before insurance by applying the following:
Add base treatment costs, room costs, doctor fees, emergency surcharges, and extended stay fees.
Subtract any applicable membership discounts.
Apply insurance coverage to calculate the final cost.
Display a detailed billing breakdown, including:
Base Treatment Cost.
Room Cost.
Doctor's Fee.
Emergency Surcharge.
Membership Discount.
Extended Stay Fee.
Total Cost Before Insurance.
Insurance Deduction.
Final Cost to Pay.
```

```python
# Input: Patient details
patient_type = input("Enter patient type (Emergency/In-Patient/Out-Patient): ").lower()
treatment_type = input("Enter treatment type (Surgery/Diagnostic/Consultation): ").lower()
room_type = input("Enter room type (General/Semi-Private/Private/ICU): ").lower()
doctor_category = input("Enter doctor's category (Specialist/Consultant/Resident): ").lower()
insurance_coverage = float(input("Enter insurance coverage percentage (0-100): ")) / 100
membership = input("Are you a premium hospital member? (Yes/No): ").lower()

# Base costs for treatments
base_treatment_cost = 0
if treatment_type == "surgery":
    if patient_type == "emergency":
        base_treatment_cost = 100000  # Emergency surgery
    else:
        base_treatment_cost = 75000  # Non-emergency surgery
elif treatment_type == "diagnostic":
    base_treatment_cost = 15000  # Cost for diagnostic tests
elif treatment_type == "consultation":
    base_treatment_cost = 5000  # General consultation
else:
    print("Invalid treatment type.")
    exit()

# Room costs
room_cost = 0
if room_type == "general":
    room_cost = 2000  # Per day for general ward
elif room_type == "semi-private":
    room_cost = 5000
elif room_type == "private":
    room_cost = 10000
elif room_type == "icu":
    room_cost = 25000
else:
    print("Invalid room type.")
    exit()

# Doctor's fees
doctor_fee = 0
if doctor_category == "specialist":
    doctor_fee = 20000
elif doctor_category == "consultant":
    doctor_fee = 15000
elif doctor_category == "resident":
    doctor_fee = 8000
else:
    print("Invalid doctor category.")
    exit()

# Emergency surcharge (nested logic)
surcharge = 0
if patient_type == "emergency":
    if treatment_type == "surgery":
        surcharge = base_treatment_cost * 0.20  # 20% extra for emergency surgery
    elif treatment_type == "diagnostic":
        surcharge = base_treatment_cost * 0.10  # 10% extra for emergency diagnostics
    else:
        surcharge = 1000  # Flat surcharge for emergency consultations

# Membership discount
membership_discount = 0
if membership == "yes":
    if room_type == "private" or room_type == "icu":
        membership_discount = base_treatment_cost * 0.15  # 15% for premium members in private rooms
    else:
        membership_discount = base_treatment_cost * 0.10  # 10% for other cases

# Calculate total cost before insurance
total_cost = base_treatment_cost + room_cost + doctor_fee + surcharge - membership_discount

# Apply insurance coverage
final_cost = total_cost * (1 - insurance_coverage)

# Additional fees for extended stays (if in-patient for more than 5 days)
extended_stay_fee = 0
if patient_type == "in-patient":
    days_admitted = int(input("Enter the number of days admitted: "))
    if days_admitted > 5:
        extended_stay_fee = days_admitted * 500  # ₹500 per day after 5 days
        final_cost += extended_stay_fee

# Output the total billing details
print("\n--- Final Billing Details ---")
print(f"Base Treatment Cost: ₹{base_treatment_cost:.2f}")
print(f"Room Cost: ₹{room_cost:.2f}")
print(f"Doctor's Fee: ₹{doctor_fee:.2f}")
print(f"Emergency Surcharge: ₹{surcharge:.2f}")
print(f"Membership Discount: ₹-{membership_discount:.2f}")
print(f"Extended Stay Fee: ₹{extended_stay_fee:.2f}")
print(f"Total Cost Before Insurance: ₹{total_cost:.2f}")
print(f"Insurance Coverage: ₹-{total_cost * insurance_coverage:.2f}")
print(f"Final Cost to Pay: ₹{final_cost:.2f}")
```