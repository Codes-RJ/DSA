# Python Loops and Iteration

## Overview

Loops are fundamental control structures that allow repeated execution of code blocks. Python provides several types of loops and iteration mechanisms, each suited for different scenarios. Understanding loops and their relationship with data structures is crucial for efficient algorithm implementation.

## Types of Loops

### for Loop

#### Basic for Loop
```python
# Loop over range
for i in range(5):
    print(f"Iteration {i}")

# Loop over range with start and end
for i in range(2, 8):
    print(f"Number {i}")

# Loop over range with step
for i in range(0, 10, 2):
    print(f"Even number {i}")

# Loop over range backwards
for i in range(10, 0, -1):
    print(f"Countdown {i}")

# Loop over string
text = "Python"
for char in text:
    print(f"Character: {char}")

# Loop over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Loop over tuple
coordinates = (10, 20, 30)
for coord in coordinates:
    print(f"Coordinate: {coord}")

# Loop over dictionary keys
person = {"name": "Alice", "age": 25, "city": "New York"}
for key in person:
    print(f"Key: {key}")

# Loop over dictionary values
for value in person.values():
    print(f"Value: {value}")

# Loop over dictionary items
for key, value in person.items():
    print(f"{key}: {value}")
```

#### Advanced for Loop Features
```python
# Enumerate - get index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Enumerate with start index
for index, fruit in enumerate(fruits, start=1):
    print(f"Item {index}: {fruit}")

# Zip - iterate over multiple sequences
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Zip with different lengths (stops at shortest)
names = ["Alice", "Bob", "Charlie", "David"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Zip longest (with itertools)
from itertools import zip_longest
for name, age in zip_longest(names, ages, fillvalue="Unknown"):
    print(f"{name} is {age} years old")

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# List comprehension in loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    square = num ** 2
    print(f"{num} squared is {square}")
```

### while Loop

#### Basic while Loop
```python
# Simple counter
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop with user input
# password = ""
# while password != "secret":
#     password = input("Enter password: ")
# print("Access granted!")

# While loop with condition
number = 0
while number < 100:
    number = int(input("Enter a number (0-99): "))
    print(f"You entered: {number}")

# While True with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break
    print(f"You said: {user_input}")

# While loop for validation
age = -1
while age < 0 or age > 120:
    try:
        age = int(input("Enter valid age (0-120): "))
        if age < 0 or age > 120:
            print("Invalid age! Please try again.")
    except ValueError:
        print("Please enter a number!")

print(f"Valid age: {age}")
```

#### while Loop with Data Structures
```python
# Process queue
from collections import deque

queue = deque(["task1", "task2", "task3", "task4"])
while queue:
    task = queue.popleft()
    print(f"Processing: {task}")

# Process stack
stack = [1, 2, 3, 4, 5]
while stack:
    item = stack.pop()
    print(f"Popped: {item}")

# Read lines until empty
lines = ["line1", "line2", "line3", "", "line4", "line5"]
index = 0
while index < len(lines) and lines[index]:
    print(f"Processing: {lines[index]}")
    index += 1

# Game loop simulation
game_running = True
player_health = 100
while game_running and player_health > 0:
    print(f"Player health: {player_health}")
    # Simulate damage
    player_health -= 10
    if player_health <= 0:
        game_running = False
        print("Game Over!")

# Menu loop
while True:
    print("\nMenu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        print("You chose Option 1")
    elif choice == "2":
        print("You chose Option 2")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
```

## Loop Control Statements

### break Statement
```python
# Break out of loop
for i in range(10):
    if i == 5:
        print(f"Breaking at i = {i}")
        break
    print(f"i = {i}")

# Break in nested loops
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
found = False

for i, num in enumerate(numbers):
    if num == target:
        print(f"Found {target} at index {i}")
        found = True
        break

if not found:
    print(f"{target} not found")

# Break in while loop
count = 0
while True:
    print(f"Count: {count}")
    count += 1
    if count >= 5:
        break

# Break with search algorithm
def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

numbers = [10, 20, 30, 40, 50]
index = linear_search(numbers, 30)
print(f"Found 30 at index: {index}")

# Break in data processing
data = [1, 2, 3, -1, 4, 5, 6]
sum_positive = 0
for num in data:
    if num < 0:
        break  # Stop at first negative
    sum_positive += num
print(f"Sum of positive numbers: {sum_positive}")
```

### continue Statement
```python
# Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"Odd: {i}")

# Skip specific values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 3 == 0:
        continue  # Skip multiples of 3
    print(f"Not multiple of 3: {num}")

# Continue in while loop
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(f"Odd count: {count}")

# Continue with data validation
scores = [85, -5, 92, 105, 78, -10, 88]
valid_scores = []
for score in scores:
    if score < 0 or score > 100:
        print(f"Invalid score: {score}")
        continue
    valid_scores.append(score)
print(f"Valid scores: {valid_scores}")

# Continue in nested loops
for i in range(3):
    for j in range(3):
        if i == j:
            continue  # Skip diagonal elements
        print(f"({i}, {j})")
```

### pass Statement
```python
# Pass as placeholder
for i in range(5):
    pass  # TODO: implement later

# Pass in conditional
x = 10
if x > 5:
    pass  # TODO: handle this case

# Pass in function/class definition
def my_function():
    pass  # Implementation coming soon

class MyClass:
    pass  # Implementation coming soon

# Pass in exception handling
try:
    # Some operation
    pass
except ValueError:
    pass  # Handle silently
```

## Iterators and Generators

### Iterator Protocol
```python
# Custom iterator
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# Use custom iterator
countdown = Countdown(5)
for num in countdown:
    print(f"Countdown: {num}")

# Iterator with list
my_list = [1, 2, 3, 4, 5]
iterator = iter(my_list)

print(f"First: {next(iterator)}")
print(f"Second: {next(iterator)}")
print(f"Remaining: {list(iterator)}")

# Manual iteration
iterator = iter(my_list)
while True:
    try:
        item = next(iterator)
        print(f"Item: {item}")
    except StopIteration:
        break
```

### Generators
```python
# Generator function
def count_up_to(n):
    current = 1
    while current <= n:
        yield current
        current += 1

# Use generator
for num in count_up_to(5):
    print(f"Number: {num}")

# Generator expression
squares = (x**2 for x in range(10))
for square in squares:
    print(f"Square: {square}")

# Fibonacci generator
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Use Fibonacci generator
for fib in fibonacci(10):
    print(f"Fibonacci: {fib}")

# Generator for file processing
def read_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# Use file generator (example)
# for line in read_lines('example.txt'):
#     print(f"Line: {line}")

# Infinite generator
def infinite_counter():
    count = 0
    while True:
        yield count
        count += 1

# Use with break
counter = infinite_counter()
for i, num in enumerate(counter):
    if i >= 5:
        break
    print(f"Count: {num}")
```

## Loops with Different Data Structures

### List Operations
```python
# List iteration patterns
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic iteration
print("Basic iteration:")
for num in numbers:
    print(f"Number: {num}")

# With index
print("\nWith index:")
for i, num in enumerate(numbers):
    print(f"Index {i}: {num}")

# Modify while iterating (create new list)
print("\nFilter and modify:")
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num * 2)
print(f"Even numbers doubled: {even_numbers}")

# Safe removal while iterating
print("\nSafe removal:")
numbers_copy = numbers.copy()
for num in numbers_copy:
    if num % 3 == 0:
        numbers.remove(num)
print(f"After removing multiples of 3: {numbers}")

# List comprehension vs loop
print("\nList comprehension:")
squares_loop = []
for num in range(10):
    squares_loop.append(num ** 2)
print(f"Loop squares: {squares_loop}")

squares_comp = [num ** 2 for num in range(10)]
print(f"Comprehension squares: {squares_comp}")

# Nested list processing
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nMatrix processing:")
for row in matrix:
    for element in row:
        print(f"Element: {element}")

# Flatten nested list
print("\nFlatten matrix:")
flattened = []
for row in matrix:
    for element in row:
        flattened.append(element)
print(f"Flattened: {flattened}")
```

### Dictionary Operations
```python
# Dictionary iteration patterns
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "email": "alice@example.com",
    "phone": "555-1234"
}

# Iterate over keys
print("Keys:")
for key in person:
    print(f"Key: {key}")

# Iterate over values
print("\nValues:")
for value in person.values():
    print(f"Value: {value}")

# Iterate over items
print("\nItems:")
for key, value in person.items():
    print(f"{key}: {value}")

# Filter dictionary
print("\nFilter dictionary:")
filtered_person = {}
for key, value in person.items():
    if len(key) > 3:
        filtered_person[key] = value
print(f"Filtered: {filtered_person}")

# Transform dictionary
print("\nTransform dictionary:")
upper_person = {}
for key, value in person.items():
    upper_person[key.upper()] = str(value).upper()
print(f"Upper case: {upper_person}")

# Nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30},
    "person3": {"name": "Charlie", "age": 35}
}

print("\nNested dictionary:")
for person_id, person_data in nested_dict.items():
    print(f"{person_id}:")
    for key, value in person_data.items():
        print(f"  {key}: {value}")

# Dictionary comprehension vs loop
print("\nDictionary comprehension:")
squares_loop = {}
for i in range(5):
    squares_loop[i] = i ** 2
print(f"Loop squares: {squares_loop}")

squares_comp = {i: i ** 2 for i in range(5)}
print(f"Comprehension squares: {squares_comp}")
```

### Set Operations
```python
# Set iteration patterns
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Basic iteration
print("Set iteration:")
for num in numbers:
    print(f"Number: {num}")

# Note: Sets are unordered
print(f"\nSet order: {numbers}")

# Filter set
print("\nFilter set:")
even_numbers = set()
for num in numbers:
    if num % 2 == 0:
        even_numbers.add(num)
print(f"Even numbers: {even_numbers}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nSet operations:")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

# Process set elements
print("\nProcess set:")
for num in set1:
    if num in set2:
        print(f"{num} is in both sets")
    else:
        print(f"{num} is only in first set")

# Set comprehension vs loop
print("\nSet comprehension:")
squares_loop = set()
for i in range(5):
    squares_loop.add(i ** 2)
print(f"Loop squares: {squares_loop}")

squares_comp = {i ** 2 for i in range(5)}
print(f"Comprehension squares: {squares_comp}")
```

### String Operations
```python
# String iteration patterns
text = "Hello, World! Python is awesome."

# Character iteration
print("Character iteration:")
for char in text:
    print(f"Char: {char}")

# Word iteration
print("\nWord iteration:")
words = text.split()
for word in words:
    print(f"Word: {word}")

# Line iteration
multiline_text = """Line 1
Line 2
Line 3"""

print("\nLine iteration:")
for line in multiline_text.split('\n'):
    print(f"Line: {line}")

# Character processing
print("\nCharacter processing:")
vowels = 0
consonants = 0
for char in text.lower():
    if char in 'aeiou':
        vowels += 1
    elif char.isalpha():
        consonants += 1
print(f"Vowels: {vowels}, Consonants: {consonants}")

# String transformation
print("\nString transformation:")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(f"Reversed: {reversed_text}")

# Word processing
print("\nWord processing:")
word_lengths = {}
for word in words:
    word_lengths[word] = len(word)
print(f"Word lengths: {word_lengths}")
```

## Advanced Loop Patterns

### Nested Loops with Data Structures
```python
# Matrix multiplication
def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    if cols_A != rows_B:
        return "Cannot multiply: dimensions don't match"
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = matrix_multiply(A, B)
print(f"Matrix multiplication result: {result}")

# Cartesian product
def cartesian_product(list1, list2):
    product = []
    for item1 in list1:
        for item2 in list2:
            product.append((item1, item2))
    return product

colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]
combinations = cartesian_product(colors, sizes)
print(f"Combinations: {combinations}")

# Find pairs in array
def find_pairs(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
pairs = find_pairs(numbers, target)
print(f"Pairs that sum to {target}: {pairs}")
```

### Loop with Functions
```python
# Map function simulation
def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

# Filter function simulation
def my_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

# Reduce function simulation
def my_reduce(func, iterable, initial=None):
    iterator = iter(iterable)
    if initial is None:
        result = next(iterator)
    else:
        result = initial
    
    for item in iterator:
        result = func(result, item)
    
    return result

# Usage
numbers = [1, 2, 3, 4, 5]
squared = my_map(lambda x: x**2, numbers)
print(f"Mapped squares: {squared}")

evens = my_filter(lambda x: x % 2 == 0, numbers)
print(f"Filtered evens: {evens}")

sum_result = my_reduce(lambda x, y: x + y, numbers)
print(f"Reduced sum: {sum_result}")

# Loop with callback
def process_items(items, callback):
    for item in items:
        callback(item)

def print_item(item):
    print(f"Processing: {item}")

process_items(numbers, print_item)

# Loop with generator
def process_with_generator(items, processor):
    for item in items:
        yield processor(item)

processed = list(process_with_generator(numbers, lambda x: x * 2))
print(f"Generator processing: {processed}")
```

## Performance Considerations

### Loop Optimization
```python
import timeit

# List vs generator
def list_comprehension():
    return [x**2 for x in range(1000)]

def generator_expression():
    return list(x**2 for x in range(1000))

def traditional_loop():
    result = []
    for x in range(1000):
        result.append(x**2)
    return result

# Benchmark
list_time = timeit.timeit(list_comprehension, number=1000)
gen_time = timeit.timeit(generator_expression, number=1000)
loop_time = timeit.timeit(traditional_loop, number=1000)

print(f"List comprehension: {list_time:.6f}s")
print(f"Generator expression: {gen_time:.6f}s")
print(f"Traditional loop: {loop_time:.6f}s")

# Local variable optimization
def slow_loop():
    total = 0
    for i in range(1000):
        total += i * i
    return total

def fast_loop():
    total = 0
    mul = total.__mul__  # Cache method lookup
    for i in range(1000):
        total += mul(i, i)
    return total

slow_time = timeit.timeit(slow_loop, number=1000)
fast_time = timeit.timeit(fast_loop, number=1000)

print(f"Slow loop: {slow_time:.6f}s")
print(f"Fast loop: {fast_time:.6f}s")
```

### Memory Efficiency
```python
# Memory-efficient processing
def memory_efficient_processing():
    # Bad: Creates large list in memory
    def bad_approach():
        large_list = [x**2 for x in range(1000000)]
        total = sum(large_list)
        return total
    
    # Good: Uses generator
    def good_approach():
        total = sum(x**2 for x in range(1000000))
        return total
    
    # Very good: Uses math formula
    def best_approach():
        n = 1000000
        return n * (n - 1) * (2 * n - 1) // 6
    
    return bad_approach(), good_approach(), best_approach()

bad_result, good_result, best_result = memory_efficient_processing()
print(f"Bad approach: {bad_result}")
print(f"Good approach: {good_result}")
print(f"Best approach: {best_result}")

# Processing large files
def process_large_file(filename):
    # Memory efficient: process line by line
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip().lower()

# Usage example (commented out as it requires a file)
# for line in process_large_file('large_file.txt'):
#     print(f"Processing: {line[:50]}...")  # First 50 chars
```

## Modern Python Loop Features

### Walrus Operator (Python 3.8+)
```python
# Walrus operator in while loop
import random

# Traditional approach
numbers = []
while True:
    num = random.randint(1, 100)
    if num > 90:
        break
    numbers.append(num)

# With walrus operator
numbers = []
while (num := random.randint(1, 100)) <= 90:
    numbers.append(num)

print(f"Numbers before >90: {numbers}")

# Walrus in list comprehension
processed = [result for num in range(10) if (result := num * 2) > 10]
print(f"Processed: {processed}")

# Walrus in file processing
def find_long_lines(filename):
    long_lines = []
    with open(filename, 'r') as file:
        while (line := file.readline().strip()):
            if len(line) > 50:
                long_lines.append(line)
    return long_lines
```

### Positional Parameters (Python 3.8+)
```python
# Function with positional only parameters
def process_data(data, /, multiplier=1, *, adder=0):
    """Process data with positional only and keyword only parameters"""
    result = []
    for item in data:
        processed = item * multiplier + adder
        result.append(processed)
    return result

# Usage
numbers = [1, 2, 3, 4, 5]
result = process_data(numbers, 2, adder=10)
print(f"Processed data: {result}")
```

## Common Loop Patterns and Idioms

### Loop with Accumulator
```python
# Sum accumulator
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Product accumulator
def product_numbers(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# String accumulator
def join_strings(strings):
    result = ""
    for s in strings:
        result += s + " "
    return result.strip()

# List accumulator
def filter_even(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

# Test
nums = [1, 2, 3, 4, 5]
print(f"Sum: {sum_numbers(nums)}")
print(f"Product: {product_numbers(nums)}")
print(f"Joined: {join_strings(['Hello', 'World', 'Python'])}")
print(f"Even numbers: {filter_even(nums)}")
```

### Loop with Early Exit
```python
# Find first match
def find_first_match(items, condition):
    for item in items:
        if condition(item):
            return item
    return None

# Check all conditions
def all_positive(numbers):
    for num in numbers:
        if num <= 0:
            return False
    return True

# Check any condition
def any_long_string(strings):
    for s in strings:
        if len(s) > 10:
            return True
    return False

# Test
items = ["apple", "banana", "cherry"]
first_b = find_first_match(items, lambda x: x.startswith('b'))
print(f"First starting with 'b': {first_b}")

numbers = [1, 2, 3, 4, 5]
print(f"All positive: {all_positive(numbers)}")
print(f"Any long string: {any_long_string(['hello', 'world', 'python programming'])}")
```

### Loop with Index Tracking
```python
# Find index of element
def find_index(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

# Find all indices
def find_all_indices(items, target):
    indices = []
    for i, item in enumerate(items):
        if item == target:
            indices.append(i)
    return indices

# Find max with index
def find_max_with_index(items):
    max_item = items[0]
    max_index = 0
    for i, item in enumerate(items):
        if item > max_item:
            max_item = item
            max_index = i
    return max_item, max_index

# Test
numbers = [3, 7, 2, 7, 1, 9]
print(f"Index of 7: {find_index(numbers, 7)}")
print(f"All indices of 7: {find_all_indices(numbers, 7)}")
print(f"Max and index: {find_max_with_index(numbers)}")
```

## Best Practices

1. **Use comprehensions** for simple transformations and filters
2. **Prefer enumerate()** when you need both index and value
3. **Use generators** for memory-efficient processing of large sequences
4. **Avoid modifying lists** while iterating over them
5. **Use appropriate loop type** based on the use case
6. **Leverage built-in functions** like sum(), max(), min() when possible
7. **Use zip()** for parallel iteration over multiple sequences
8. **Consider performance** for large datasets
9. **Use meaningful variable names** in loops
10. **Keep loops simple** and move complex logic to functions

## Conclusion

Loops and iteration are fundamental to Python programming, providing various ways to process data structures efficiently. From basic for and while loops to advanced generator patterns and modern language features, Python offers flexible and expressive iteration mechanisms. Understanding the relationship between loops and data structures, along with performance considerations and best practices, enables writing efficient, readable, and maintainable Python code that effectively processes collections and implements algorithms.
