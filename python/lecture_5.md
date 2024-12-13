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


# SUPER SIMPLEST CODE EVER!! 👨🏼‍💻
## Dynamic Banking System Code
```python
# Function to display menu
def display_menu():
    print("\n--- Banking System ---")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. View Balance")
    print("4. Exit")

# Function to process deposit
def deposit(balance):
    try:
        amount = float(input("Enter the amount to deposit: ₹"))
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
    except ValueError as e:
        print(f"Error: {e}")
    return balance

# Function to process withdrawal
def withdraw(balance):
    try:
        amount = float(input("Enter the amount to withdraw: ₹"))
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > balance:
            raise ValueError("Insufficient funds.")
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
    except ValueError as e:
        print(f"Error: {e}")
    return balance

# Function to display balance
def view_balance(balance):
    print(f"Your current balance is: ₹{balance:.2f}")

# Main function
def main():
    balance = 0.0  # Initial balance
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                balance = deposit(balance)
            elif choice == 2:
                balance = withdraw(balance)
            elif choice == 3:
                view_balance(balance)
            elif choice == 4:
                print("Thank you for using the banking system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the program
if __name__ == "__main__":
    main()
```


## Dynamic Version of the Ticketing System
```python
def calculate_ticket_price(age, seat_preference):
    """Calculates the ticket price based on age and seat preference."""
    base_price = 500

    # Age-based discount
    if age < 12:
        discount = 0.50  # 50% discount for children
    elif age > 60:
        discount = 0.30  # 30% discount for senior citizens
    else:
        discount = 0.0  # No discount for others

    # Seat preference charges
    if seat_preference.lower() == "window":
        extra_charge = 100
    elif seat_preference.lower() == "aisle":
        extra_charge = 50
    elif seat_preference.lower() == "middle":
        extra_charge = 0
    else:
        raise ValueError("Invalid seat preference.")

    # Final ticket price
    ticket_price = (base_price * (1 - discount)) + extra_charge
    return ticket_price

def get_passenger_data(index):
    """Collects data for each passenger."""
    print(f"\nPassenger {index + 1}:")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    seat_preference = input("Enter Seat Preference (Window/Middle/Aisle): ")
    return name, age, seat_preference

def print_ticket_summary(passenger_details, total_fare, group_discount):
    """Prints the summary of the ticket details."""
    print("\n--- Ticket Summary ---")
    for passenger in passenger_details:
        print(f"Passenger: {passenger['name']}, Age: {passenger['age']}, Seat: {passenger['seat']}, Price: ₹{passenger['price']:.2f}")
    print(f"\nTotal Fare Before Group Discount: ₹{total_fare + group_discount:.2f}")
    print(f"Group Discount Applied: ₹{group_discount:.2f}")
    print(f"Total Fare to Pay: ₹{total_fare:.2f}")

def main():
    try:
        # Input: Number of passengers
        num_passengers = int(input("Enter number of passengers: "))
        if num_passengers < 1 or num_passengers > 50:
            raise ValueError("Number of passengers must be between 1 and 50.")

        passenger_details = []
        total_fare = 0

        # Collect data for each passenger
        for i in range(num_passengers):
            name, age, seat_preference = get_passenger_data(i)
            ticket_price = calculate_ticket_price(age, seat_preference)
            passenger_details.append({
                'name': name,
                'age': age,
                'seat': seat_preference.capitalize(),
                'price': ticket_price
            })
            total_fare += ticket_price

        # Apply group discount if applicable
        group_discount = 0
        if num_passengers > 10:
            group_discount = total_fare * 0.10  # 10% discount for groups larger than 10
            total_fare -= group_discount

        # Print ticket summary
        print_ticket_summary(passenger_details, total_fare, group_discount)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

## Dynamic Pathfinding on a Grid
```python
def display_grid(grid):
    """Displays the grid in a formatted way."""
    print("\nGrid Layout:")
    for row in grid:
        print(" ".join(row))

def create_grid(size, obstacles):
    """Creates the grid with obstacles."""
    grid = [["O" for _ in range(size)] for _ in range(size)]  # "O" for open
    for obs in obstacles:
        x, y = obs
        if 0 <= x < size and 0 <= y < size:
            grid[x][y] = "X"  # "X" for obstacle
    return grid

def find_paths(grid, x, y, path, paths):
    """Recursive function to find all unique paths."""
    n = len(grid)
    if x == n - 1 and y == n - 1:
        paths.append(path.copy())
        return

    # Mark current position as visited
    grid[x][y] = "V"

    # Move right
    if y + 1 < n and grid[x][y + 1] == "O":
        path.append((x, y + 1))
        find_paths(grid, x, y + 1, path, paths)
        path.pop()

    # Move down
    if x + 1 < n and grid[x + 1][y] == "O":
        path.append((x + 1, y))
        find_paths(grid, x + 1, y, path, paths)
        path.pop()

    # Backtrack
    grid[x][y] = "O"

def main():
    try:
        # Input: Grid size and obstacles
        size = int(input("Enter grid size (N x N): "))
        if size < 2:
            raise ValueError("Grid size must be at least 2x2.")

        num_obstacles = int(input("Enter number of obstacles: "))
        obstacles = []
        for i in range(num_obstacles):
            obs = tuple(map(int, input(f"Enter obstacle {i + 1} coordinates (x y): ").split()))
            obstacles.append(obs)

        # Create grid
        grid = create_grid(size, obstacles)
        display_grid(grid)

        # Initialize pathfinding
        paths = []
        if grid[0][0] == "X" or grid[size - 1][size - 1] == "X":
            raise ValueError("Start or End point cannot be an obstacle!")

        find_paths(grid, 0, 0, [(0, 0)], paths)

        # Display results
        if paths:
            print(f"\nTotal unique paths: {len(paths)}")
            print("All paths:")
            for path in paths:
                print(" -> ".join(map(str, path)))
        else:
            print("No valid paths found.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

```python
Enter grid size (N x N): 4
Enter number of obstacles: 2
Enter obstacle 1 coordinates (x y): 2 1
Enter obstacle 2 coordinates (x y): 1 2

Grid Layout:
O O O O
O O X O
O X O O
O O O O

Total unique paths: 2
All paths:
(0, 0) -> (0, 1) -> (0, 2) -> (0, 3) -> (1, 3) -> (2, 3) -> (3, 3)
(0, 0) -> (1, 0) -> (2, 0) -> (3, 0) -> (3, 1) -> (3, 2) -> (3, 3)
```

### Real-Life Applications
- **Robotics Navigation**: Robots navigating grids in warehouses or delivery systems.
- **Route Optimization**: Tools like Google Maps for traffic-based routing.
- **Game Development**: Character movement in grid-based games.
- **Logistics and Operations**: Delivery route planning and warehouse management.

### AI Development Applications
- **Reinforcement Learning**: AI agents learning to navigate in grid environments.
- **Planning Algorithms**: A*, Dijkstra's, BFS for intelligent pathfinding.
- **Robot Motion Planning**: Autonomous navigation for drones and robots.
- **Data Science & Simulation**: Modeling scenarios like disease spread or evacuations.

### Why Train on This?
- **Concept Mastery**: Master nested loops, recursion, and backtracking.
- **AI Foundations**: Introduces pathfinding and constraint satisfaction concepts.
- **Adaptability**: Extendable to 3D spaces or graph-based systems.

### Future Enhancements
- **Algorithm Optimization**: Dynamic programming or memoization.
- **Integrate Heuristics**: Use A* or greedy approaches for shortest pathfinding.
- **AI Simulation**: Simulate dynamic environments with rewards/penalties.
- **Real-World Data**: Apply to real-world maps or traffic datasets.
