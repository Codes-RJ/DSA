# Python Conditional Statements

## Overview

Conditional statements allow programs to make decisions and execute different code paths based on specific conditions. Python provides several conditional constructs that enable branching logic, which is fundamental to algorithm implementation and problem-solving.

## if Statement

### Basic if Statement
```python
# Simple if statement
age = 18
if age >= 18:
    print("You are eligible to vote")

# if-else statement
score = 85
if score >= 90:
    print("Grade: A")
else:
    print("Grade: Not A")

# if-elif-else ladder
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Nested if statements
temperature = 25
is_raining = False

if temperature > 20:
    print("Warm weather")
    if is_raining:
        print("But it's raining")
    else:
        print("Perfect weather for a walk")
else:
    print("Cool weather")

# Multiple conditions
number = 42
if number > 0 and number % 2 == 0:
    print("Positive and even")

if number < 0 or number > 100:
    print("Out of range")
```

### Complex Conditions
```python
# Logical operators
age = 25
has_license = True
has_car = False
country = "USA"

# Multiple conditions with AND
if age >= 18 and has_license and has_car:
    print("You can drive")
else:
    print("You cannot drive")

# Multiple conditions with OR
if age >= 18 or (country == "USA" and age >= 16):
    print("You can get a license")

# Combining AND and OR
can_drive = (age >= 18 and has_license) or \
           (age >= 16 and has_license and country == "USA")

if can_drive and has_car:
    print("You can drive your car")
elif can_drive and not has_car:
    print("You can drive but need a car")
else:
    print("You cannot drive")

# NOT operator
if not has_car:
    print("You don't have a car")

# Short-circuit evaluation
text = None
if text is not None and len(text) > 0:
    print("Text has content")
else:
    print("Text is None or empty")

# Chained comparisons
x = 10
if 0 < x < 20:
    print("x is between 0 and 20")

# Membership tests
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Apple is in the list")

if "grape" not in fruits:
    print("Grape is not in the list")

# Identity tests
a = [1, 2, 3]
b = [1, 2, 3]
c = a

if a is c:
    print("a and c are the same object")
if a is not b:
    print("a and b are different objects")
if a == b:
    print("a and b have the same content")
```

### Ternary Operator
```python
# Basic ternary operator
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Nested ternary (avoid for readability)
score = 75
grade = "A" if score >= 90 else \
        "B" if score >= 80 else \
        "C" if score >= 70 else "F"
print(f"Grade: {grade}")

# Ternary in expressions
x, y = 10, 20
max_val = x if x > y else y
print(f"Maximum: {max_val}")

# Ternary with function calls
def get_adult_message():
    return "Welcome, adult!"

def get_minor_message():
    return "Hello, minor!"

message = get_adult_message() if age >= 18 else get_minor_message()
print(message)

# Ternary in list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
processed = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"Processed: {processed}")

# Ternary with multiple conditions
result = "positive" if x > 0 else "negative" if x < 0 else "zero"
print(f"Result: {result}")
```

## Advanced Conditional Patterns

### Conditional Expressions with Data Structures
```python
# Conditional list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
odds = [x for x in numbers if x % 2 != 0]
print(f"Evens: {evens}")
print(f"Odds: {odds}")

# Conditional dictionary comprehension
person = {"name": "Alice", "age": 25, "city": "New York"}
filtered_person = {k: v for k, v in person.items() if len(k) > 3}
print(f"Filtered person: {filtered_person}")

# Conditional set comprehension
unique_chars = {char for word in ["hello", "world", "python"] for char in word if char.isalpha()}
print(f"Unique chars: {unique_chars}")

# Conditional generator expression
even_squares = (x**2 for x in numbers if x % 2 == 0)
print(f"Even squares: {list(even_squares)}")

# Nested conditional comprehension
matrix = [[i * j for j in range(3)] for i in range(3)]
filtered_matrix = [[cell for cell in row if cell > 0] for row in matrix]
print(f"Filtered matrix: {filtered_matrix}")
```

### Conditional Function Definition
```python
# Function with conditional return
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(f"Grade for 85: {get_grade(85)}")

# Function with conditional parameters
def process_data(data, uppercase=False, reverse=False):
    result = data.copy()
    
    if uppercase:
        result = [item.upper() if isinstance(item, str) else item for item in result]
    
    if reverse:
        result = result[::-1]
    
    return result

words = ["hello", "world", "python"]
print(f"Processed: {process_data(words, uppercase=True, reverse=True)}")

# Conditional function execution
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")

# Function with conditional logic
def classify_number(n):
    category = "zero" if n == 0 else \
              "positive even" if n > 0 and n % 2 == 0 else \
              "positive odd" if n > 0 else \
              "negative even" if n % 2 == 0 else \
              "negative odd"
    return category

for num in [-3, -2, -1, 0, 1, 2, 3]:
    print(f"{num}: {classify_number(num)}")
```

## Modern Python Conditional Features

### Walrus Operator (Python 3.8+)
```python
# Walrus operator in conditions
import random

# Traditional approach
numbers = []
num = random.randint(1, 100)
while num <= 90:
    numbers.append(num)
    num = random.randint(1, 100)

# With walrus operator
numbers = []
while (num := random.randint(1, 100)) <= 90:
    numbers.append(num)

print(f"Numbers before >90: {numbers}")

# Walrus in if statement
def process_data(data):
    if (processed := [x * 2 for x in data if x > 5]):
        return sum(processed)
    else:
        return 0

result = process_data([1, 2, 3, 6, 7, 8])
print(f"Processed sum: {result}")

# Walrus in list comprehension
words = ["hello", "world", "python", "programming"]
long_words = [word.upper() for word in words if (length := len(word)) > 5]
print(f"Long words: {long_words}")

# Walrus in while loop for file processing
def count_long_lines(filename):
    count = 0
    with open(filename, 'r') as file:
        while (line := file.readline()):
            if len(line.strip()) > 50:
                count += 1
    return count

# Usage example (commented out as it requires a file)
# print(f"Long lines: {count_long_lines('example.txt')}")
```

### Pattern Matching (Python 3.10+)
```python
# Structural pattern matching
def process_command(command):
    match command:
        case "start":
            return "Starting..."
        case "stop":
            return "Stopping..."
        case "restart":
            return "Restarting..."
        case _:
            return "Unknown command"

print(f"Command 'start': {process_command('start')}")
print(f"Command 'pause': {process_command('pause')}")

# Pattern matching with values
def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"Point on x-axis at {x}"
        case (0, y):
            return f"Point on y-axis at {y}"
        case (x, y) if x == y:
            return f"Point on diagonal at ({x}, {y})"
        case (x, y):
            return f"Point at ({x}, {y})"

print(f"Point (0,0): {describe_point((0, 0))}")
print(f"Point (5,0): {describe_point((5, 0))}")
print(f"Point (3,3): {describe_point((3, 3))}")
print(f"Point (2,5): {describe_point((2, 5))}")

# Pattern matching with dictionaries
def process_user(user):
    match user:
        case {"name": name, "age": age} if age >= 18:
            return f"Adult {name}, age {age}"
        case {"name": name, "age": age}:
            return f"Minor {name}, age {age}"
        case {"name": name}:
            return f"{name}, age unknown"
        case _:
            return "Invalid user data"

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie"},
    {"invalid": "data"}
]

for user in users:
    print(f"User: {process_user(user)}")

# Pattern matching with classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def match_point(point):
    match point:
        case Point(x=0, y=0):
            return "Origin"
        case Point(x=x, y=y) if x > 0 and y > 0:
            return f"First quadrant ({x}, {y})"
        case Point(x=x, y=y):
            return f"Other quadrant ({x}, {y})"

p1 = Point(0, 0)
p2 = Point(3, 4)
p3 = Point(-2, 5)

print(f"p1: {match_point(p1)}")
print(f"p2: {match_point(p2)}")
print(f"p3: {match_point(p3)}")
```

## Conditional Statements with Data Structures

### List Operations
```python
# Conditional list processing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter with condition
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(f"Evens: {evens}")

# Conditional transformation
processed = []
for num in numbers:
    if num % 2 == 0:
        processed.append(num * 2)
    else:
        processed.append(num * 3)
print(f"Processed: {processed}")

# Conditional aggregation
categories = {"even": [], "odd": []}
for num in numbers:
    if num % 2 == 0:
        categories["even"].append(num)
    else:
        categories["odd"].append(num)
print(f"Categories: {categories}")

# Multi-condition processing
results = []
for num in numbers:
    if num < 3:
        results.append(f"small: {num}")
    elif num < 7:
        results.append(f"medium: {num}")
    else:
        results.append(f"large: {num}")
print(f"Results: {results}")

# Conditional removal
numbers_copy = numbers.copy()
for num in numbers_copy:
    if num % 3 == 0:
        numbers.remove(num)
print(f"After removing multiples of 3: {numbers}")
```

### Dictionary Operations
```python
# Conditional dictionary processing
people = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 20,
    "David": 35,
    "Eve": 28
}

# Filter dictionary
adults = {}
for name, age in people.items():
    if age >= 25:
        adults[name] = age
print(f"Adults: {adults}")

# Conditional transformation
age_groups = {}
for name, age in people.items():
    if age < 25:
        age_groups[name] = "young"
    elif age < 35:
        age_groups[name] = "middle-aged"
    else:
        age_groups[name] = "senior"
print(f"Age groups: {age_groups}")

# Conditional aggregation
stats = {"young": 0, "middle-aged": 0, "senior": 0}
for age in people.values():
    if age < 25:
        stats["young"] += 1
    elif age < 35:
        stats["middle-aged"] += 1
    else:
        stats["senior"] += 1
print(f"Statistics: {stats}")

# Nested dictionary processing
data = {
    "users": {
        "active": 150,
        "inactive": 50
    },
    "products": {
        "available": 200,
        "out_of_stock": 20
    }
}

summary = {}
for category, items in data.items():
    for status, count in items.items():
        if count > 100:
            summary[f"{category}_{status}"] = "high"
        elif count > 50:
            summary[f"{category}_{status}"] = "medium"
        else:
            summary[f"{category}_{status}"] = "low"
print(f"Summary: {summary}")
```

### Set Operations
```python
# Conditional set processing
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Filter set
evens = set()
for num in numbers:
    if num % 2 == 0:
        evens.add(num)
print(f"Evens: {evens}")

# Conditional classification
categories = {"small": set(), "medium": set(), "large": set()}
for num in numbers:
    if num <= 3:
        categories["small"].add(num)
    elif num <= 7:
        categories["medium"].add(num)
    else:
        categories["large"].add(num)
print(f"Categories: {categories}")

# Set operations with conditions
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Conditional union
union = set()
for item in set1:
    union.add(item)
for item in set2:
    if item not in union:
        union.add(item)
print(f"Union: {union}")

# Conditional intersection
intersection = set()
for item in set1:
    if item in set2:
        intersection.add(item)
print(f"Intersection: {intersection}")
```

## Advanced Conditional Patterns

### Strategy Pattern with Conditionals
```python
# Strategy pattern using dictionaries
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Cannot divide by zero"
}

def calculate(a, b, op):
    if op in operations:
        return operations[op](a, b)
    else:
        return "Unknown operation"

print(f"10 + 5 = {calculate(10, 5, '+')}")
print(f"10 - 5 = {calculate(10, 5, '-')}")
print(f"10 * 5 = {calculate(10, 5, '*')}")
print(f"10 / 5 = {calculate(10, 5, '/')}")
print(f"10 / 0 = {calculate(10, 0, '/')}")
print(f"10 ^ 5 = {calculate(10, 5, '^')}")

# Strategy pattern with functions
def process_data(data, strategy):
    if strategy == "sum":
        return sum(data)
    elif strategy == "average":
        return sum(data) / len(data)
    elif strategy == "max":
        return max(data)
    elif strategy == "min":
        return min(data)
    else:
        return "Unknown strategy"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Sum: {process_data(numbers, 'sum')}")
print(f"Average: {process_data(numbers, 'average')}")
print(f"Max: {process_data(numbers, 'max')}")
print(f"Min: {process_data(numbers, 'min')}")
```

### State Machine with Conditionals
```python
# Simple state machine
class TrafficLight:
    def __init__(self):
        self.state = "red"
    
    def change(self):
        if self.state == "red":
            self.state = "green"
        elif self.state == "green":
            self.state = "yellow"
        elif self.state == "yellow":
            self.state = "red"
    
    def get_action(self):
        if self.state == "red":
            return "Stop"
        elif self.state == "yellow":
            return "Caution"
        elif self.state == "green":
            return "Go"
    
    def __str__(self):
        return f"TrafficLight(state={self.state})"

# Test state machine
light = TrafficLight()
for i in range(6):
    print(f"{light} - Action: {light.get_action()}")
    light.change()

# State machine with transitions
class OrderProcessor:
    def __init__(self):
        self.state = "pending"
    
    def process(self, action):
        if self.state == "pending":
            if action == "confirm":
                self.state = "confirmed"
                return "Order confirmed"
            elif action == "cancel":
                self.state = "cancelled"
                return "Order cancelled"
            else:
                return "Invalid action for pending order"
        
        elif self.state == "confirmed":
            if action == "ship":
                self.state = "shipped"
                return "Order shipped"
            elif action == "cancel":
                self.state = "cancelled"
                return "Order cancelled"
            else:
                return "Invalid action for confirmed order"
        
        elif self.state == "shipped":
            if action == "deliver":
                self.state = "delivered"
                return "Order delivered"
            else:
                return "Invalid action for shipped order"
        
        elif self.state == "delivered":
            return "Order already delivered"
        
        elif self.state == "cancelled":
            return "Order cancelled, cannot process"
        
        else:
            return "Unknown state"

# Test order processor
processor = OrderProcessor()
actions = ["confirm", "ship", "deliver", "deliver"]
for action in actions:
    result = processor.process(action)
    print(f"Action: {action}, Result: {result}, State: {processor.state}")
```

### Validation with Conditionals
```python
# Input validation
def validate_email(email):
    if not email:
        return False
    if "@" not in email:
        return False
    if email.count("@") != 1:
        return False
    
    local, domain = email.split("@")
    if not local or not domain:
        return False
    
    if "." not in domain:
        return False
    
    return True

# Test email validation
emails = ["user@example.com", "invalid-email", "user@.com", "@example.com", "user@domain."]
for email in emails:
    print(f"{email}: {'Valid' if validate_email(email) else 'Invalid'}")

# Complex validation
def validate_user_data(data):
    errors = []
    
    # Name validation
    if not data.get("name"):
        errors.append("Name is required")
    elif len(data["name"]) < 2:
        errors.append("Name must be at least 2 characters")
    elif not data["name"].replace(" ", "").isalpha():
        errors.append("Name must contain only letters")
    
    # Age validation
    age = data.get("age")
    if age is None:
        errors.append("Age is required")
    elif not isinstance(age, int) or age < 0 or age > 120:
        errors.append("Age must be a number between 0 and 120")
    
    # Email validation
    email = data.get("email")
    if not email:
        errors.append("Email is required")
    elif not validate_email(email):
        errors.append("Invalid email format")
    
    return errors

# Test user validation
users = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "B", "age": -5, "email": "invalid"},
    {"name": "", "age": "twenty", "email": ""},
    {"name": "Charlie", "age": 30, "email": "charlie@test.com"}
]

for user in users:
    errors = validate_user_data(user)
    print(f"User {user.get('name', 'Unknown')}:")
    if errors:
        for error in errors:
            print(f"  Error: {error}")
    else:
        print("  Valid user data")
```

## Performance Considerations

### Conditional Performance
```python
import timeit

# Test different conditional approaches
def approach1_if_elif(x):
    if x < 10:
        return "small"
    elif x < 20:
        return "medium"
    elif x < 30:
        return "large"
    else:
        return "extra large"

def approach2_dict_lookup(x):
    ranges = {
        range(0, 10): "small",
        range(10, 20): "medium",
        range(20, 30): "large"
    }
    for r, label in ranges.items():
        if x in r:
            return label
    return "extra large"

def approach3_binary_search(x):
    if x < 10:
        return "small"
    if x < 20:
        return "medium"
    if x < 30:
        return "large"
    return "extra large"

# Benchmark
test_values = [5, 15, 25, 35] * 1000

time1 = timeit.timeit(lambda: [approach1_if_elif(x) for x in test_values], number=100)
time2 = timeit.timeit(lambda: [approach2_dict_lookup(x) for x in test_values], number=100)
time3 = timeit.timeit(lambda: [approach3_binary_search(x) for x in test_values], number=100)

print(f"if-elif approach: {time1:.6f}s")
print(f"dict lookup approach: {time2:.6f}s")
print(f"binary search approach: {time3:.6f}s")

# Short-circuit evaluation impact
def expensive_operation():
    import time
    time.sleep(0.001)
    return True

def test_short_circuit():
    # First condition is False, so expensive_operation() is not called
    result1 = False and expensive_operation()
    
    # First condition is True, so expensive_operation() is called
    result2 = True and expensive_operation()
    
    return result1, result2

# Test short-circuit
import time
start = time.time()
result1, result2 = test_short_circuit()
end = time.time()
print(f"Short-circuit test took: {end - start:.6f}s")
```

### Memory Efficiency
```python
# Memory-efficient conditional processing
def memory_efficient_filter(data, condition):
    """Generator-based filtering"""
    for item in data:
        if condition(item):
            yield item

def memory_inefficient_filter(data, condition):
    """List-based filtering"""
    result = []
    for item in data:
        if condition(item):
            result.append(item)
    return result

# Test with large dataset
large_data = range(1000000)

# Memory efficient (generator)
gen_result = memory_efficient_filter(large_data, lambda x: x % 2 == 0)
print(f"Generator result: {next(gen_result)}")  # Only processes when needed

# Memory inefficient (creates full list)
list_result = memory_inefficient_filter(large_data[:1000], lambda x: x % 2 == 0)
print(f"List result length: {len(list_result)}")

# Conditional processing with early exit
def find_first_match(data, condition):
    for item in data:
        if condition(item):
            return item
    return None

# Efficient: stops at first match
first_even = find_first_match(range(1000000), lambda x: x % 2 == 0)
print(f"First even number: {first_even}")
```

## Common Conditional Patterns

### Guard Clauses
```python
# Guard clauses vs nested conditions
def process_payment_bad(amount, user_balance, credit_limit):
    if amount > 0:
        if user_balance >= amount:
            if amount <= credit_limit:
                # Process payment
                user_balance -= amount
                return "Payment processed", user_balance
            else:
                return "Amount exceeds credit limit", user_balance
        else:
            return "Insufficient balance", user_balance
    else:
        return "Invalid amount", user_balance

def process_payment_good(amount, user_balance, credit_limit):
    # Guard clauses
    if amount <= 0:
        return "Invalid amount", user_balance
    if user_balance < amount:
        return "Insufficient balance", user_balance
    if amount > credit_limit:
        return "Amount exceeds credit limit", user_balance
    
    # Main logic
    user_balance -= amount
    return "Payment processed", user_balance

# Test
print(process_payment_bad(100, 50, 200))
print(process_payment_good(100, 50, 200))
```

### Conditional Default Values
```python
# Setting default values conditionally
def get_user_preference(user, key, default=None):
    preferences = {
        "theme": "dark",
        "language": "en",
        "notifications": True
    }
    
    return preferences.get(key, default)

# Using conditional expressions for defaults
def process_config(config):
    return {
        "host": config.get("host") or "localhost",
        "port": config.get("port") or 8080,
        "debug": config.get("debug", False),
        "timeout": config.get("timeout") if config.get("timeout") is not None else 30
    }

# Test
config1 = {"host": "example.com", "debug": True}
config2 = {"port": 9000, "timeout": 60}

print(f"Config 1: {process_config(config1)}")
print(f"Config 2: {process_config(config2)}")
```

### Error Handling with Conditionals
```python
# Conditional error handling
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid types for division"
    else:
        return result
    finally:
        print("Division operation completed")

# Conditional validation with errors
def calculate_discount(price, discount_percent):
    errors = []
    
    if price <= 0:
        errors.append("Price must be positive")
    
    if discount_percent < 0 or discount_percent > 100:
        errors.append("Discount must be between 0 and 100")
    
    if errors:
        return {"error": "Validation failed", "details": errors}
    
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    
    return {
        "original_price": price,
        "discount_percent": discount_percent,
        "discount_amount": discount_amount,
        "final_price": final_price
    }

# Test
print(f"10 / 2 = {divide_numbers(10, 2)}")
print(f"10 / 0 = {divide_numbers(10, 0)}")
print(f"'10' / 2 = {divide_numbers('10', 2)}")

result = calculate_discount(100, 20)
print(f"Discount result: {result}")

error_result = calculate_discount(-50, 150)
print(f"Error result: {error_result}")
```

## Best Practices

1. **Use guard clauses** to handle edge cases early
2. **Prefer simple conditions** over complex nested ones
3. **Use meaningful variable names** in conditions
4. **Leverage Python's chaining** for range comparisons
5. **Use ternary operators** for simple conditional assignments
6. **Consider dictionaries** for complex conditional logic
7. **Use early returns** to reduce nesting
8. **Validate inputs** with clear error messages
9. **Use appropriate data structures** for conditional lookups
10. **Consider performance** for frequently executed conditions

## Conclusion

Conditional statements are fundamental to Python programming, providing the decision-making capabilities needed for implementing algorithms and solving problems. From basic if-else statements to advanced pattern matching and modern language features, Python offers expressive and readable ways to implement branching logic. Understanding the various conditional constructs, their performance implications, and best practices enables writing clean, efficient, and maintainable Python code that effectively handles complex decision-making scenarios.
