# Python Basic Data Structures

## Overview

Python provides a rich set of built-in data structures that are essential for implementing algorithms and solving problems efficiently. Understanding these fundamental data structures is crucial for writing effective Python programs and implementing data structures and algorithms.

## Built-in Data Structures

### Lists

#### List Basics
```python
# List creation
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2, 3]]
nested = [[1, 2], [3, 4], [5, 6]]

# List operations
print(f"Original: {numbers}")
print(f"Length: {len(numbers)}")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Slice [1:4]: {numbers[1:4]}")
print(f"Step slice: {numbers[::2]}")

# Modifying lists
numbers.append(6)
numbers.insert(0, 0)
numbers.extend([7, 8, 9])
numbers[2] = 99

print(f"After modifications: {numbers}")

# Removing elements
removed = numbers.pop()
numbers.remove(99)
del numbers[0]

print(f"After removals: {numbers}")
print(f"Removed element: {removed}")

# List methods
numbers.sort()
numbers.reverse()
count = numbers.count(2)
index = numbers.index(3)

print(f"Sorted: {numbers}")
print(f"Count of 2: {count}")
print(f"Index of 3: {index}")
```

#### List Comprehensions
```python
# Basic list comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]

print(f"Squares: {squares}")
print(f"Evens: {evens}")
print(f"Uppercase: {uppercase}")

# Nested list comprehension
matrix = [[i * j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Conditional list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
processed = [x * 2 if x % 2 == 0 else x * 3 for x in numbers]
print(f"Processed: {processed}")

# Flattening nested lists
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print(f"Flattened: {flattened}")
```

#### Advanced List Operations
```python
# List as stack (LIFO)
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(f"Stack: {stack}")

top = stack.pop()
print(f"Popped: {top}")
print(f"Stack after pop: {stack}")

# List as queue (FIFO)
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
front = queue.popleft()
print(f"Queue after popleft: {queue}")

# Sorting with custom key
students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]

# Sort by age
students.sort(key=lambda x: x["age"])
print(f"Sorted by age: {students}")

# Sort by name
students.sort(key=lambda x: x["name"])
print(f"Sorted by name: {students}")

# Binary search in sorted list
import bisect

sorted_list = [1, 3, 5, 7, 9, 11, 13]
index = bisect.bisect_left(sorted_list, 7)
print(f"Index of 7: {index}")

# Insert while maintaining sort
bisect.insort(sorted_list, 8)
print(f"After inserting 8: {sorted_list}")
```

### Tuples

#### Tuple Basics
```python
# Tuple creation
empty_tuple = ()
single_element = (1,)  # Note the comma
coordinates = (10, 20)
rgb = (255, 128, 0)
mixed = (1, "hello", 3.14, True)

# Tuple operations
print(f"Coordinates: {coordinates}")
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")
print(f"Slice: {coordinates[1:]}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked: x={x}, y={y}")

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Tuple methods
numbers = (1, 2, 3, 2, 1)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

# Immutability
try:
    coordinates[0] = 99
except TypeError as e:
    print(f"Error: {e}")
```

#### Named Tuples
```python
from collections import namedtuple

# Create named tuple class
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances
p1 = Point(10, 20)
p2 = Point(x=5, y=15)

person = Person("Alice", 25, "New York")

print(f"Point: {p1}")
print(f"X: {p1.x}, Y: {p1.y}")
print(f"Person: {person.name}, Age: {person.age}")

# Convert to dictionary
person_dict = person._asdict()
print(f"As dict: {person_dict}")

# Replace values
new_person = person._replace(age=26)
print(f"Updated: {new_person}")

# Default values (Python 3.7+)
from typing import NamedTuple

class Employee(NamedTuple):
    name: str
    age: int = 30
    department: str = "Engineering"

emp1 = Employee("Bob")
emp2 = Employee("Charlie", 25, "Marketing")

print(f"Employee 1: {emp1}")
print(f"Employee 2: {emp2}")
```

### Dictionaries

#### Dictionary Basics
```python
# Dictionary creation
empty_dict = {}
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "swimming"]
}

# Alternative creation methods
person2 = dict(name="Bob", age=30, city="Los Angeles")
person3 = dict([("name", "Charlie"), ("age", 35)])

# Dictionary operations
print(f"Name: {person['name']}")
print(f"Age: {person.get('age', 'Unknown')}")

# Adding and updating
person["email"] = "alice@example.com"
person.update({"age": 26, "status": "active"})

print(f"Updated: {person}")

# Removing items
removed_email = person.pop("email")
del person["hobbies"]

print(f"After removals: {person}")
print(f"Removed email: {removed_email}")

# Dictionary methods
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Checking existence
print(f"Has 'name': {'name' in person}")
print(f"Has 'phone': {'phone' in person}")
```

#### Dictionary Comprehensions
```python
# Basic dictionary comprehension
squares = {x: x**2 for x in range(10)}
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}

print(f"Squares: {squares}")
print(f"Word lengths: {word_lengths}")

# Conditional dictionary comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Transforming dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
upper_person = {k.upper(): str(v).upper() for k, v in person.items()}
print(f"Upper case: {upper_person}")

# Nested dictionary comprehension
matrix = {(i, j): i * j for i in range(3) for j in range(3)}
print(f"Multiplication table: {matrix}")
```

#### Advanced Dictionary Operations
```python
# Default dictionary
from collections import defaultdict

dd = defaultdict(int)
dd["missing"] += 1
dd["another_missing"] += 2

print(f"Default dict: {dict(dd)}")

# Default dict with list
dd_list = defaultdict(list)
dd_list["fruits"].append("apple")
dd_list["fruits"].append("banana")
dd_list["vegetables"].append("carrot")

print(f"List default dict: {dict(dd_list)}")

# OrderedDict (preserves insertion order)
from collections import OrderedDict

od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3

print(f"Ordered dict: {od}")

# Counter
from collections import Counter

words = "hello world hello python hello world"
word_count = Counter(words.split())
print(f"Word count: {word_count}")

# Most common
print(f"Most common: {word_count.most_common(2)}")

# Dictionary merging (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print(f"Merged: {merged}")

# Dictionary update with |
dict1 |= {"e": 5, "a": 10}  # Updates existing 'a'
print(f"Updated: {dict1}")
```

### Sets

#### Set Basics
```python
# Set creation
empty_set = set()
numbers = {1, 2, 3, 4, 5}
duplicates = {1, 2, 2, 3, 3, 3}  # Automatically removes duplicates

print(f"Numbers: {numbers}")
print(f"Without duplicates: {duplicates}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
print(f"Symmetric difference: {set1 ^ set2}")

# Set methods
numbers.add(6)
numbers.update([7, 8, 9])
numbers.remove(1)  # Raises KeyError if not found
numbers.discard(10)  # Doesn't raise error

print(f"After operations: {numbers}")

# Set operations
print(f"Is subset: {set2.issubset(set1)}")
print(f"Is superset: {set1.issuperset(set2)}")
print(f"Is disjoint: {set1.isdisjoint({10, 11, 12})}")

# Pop random element
popped = numbers.pop()
print(f"Popped: {popped}")
print(f"Remaining: {numbers}")
```

#### Set Comprehensions
```python
# Set comprehension
squares = {x**2 for x in range(10)}
even_numbers = {x for x in range(20) if x % 2 == 0}
unique_chars = {char for word in ["hello", "world", "python"] for char in word}

print(f"Squares: {squares}")
print(f"Even numbers: {even_numbers}")
print(f"Unique chars: {unique_chars}")

# Set comprehension with condition
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
large_squares = {x**2 for x in numbers if x > 5}
print(f"Large squares: {large_squares}")
```

#### Frozenset
```python
# Frozenset (immutable set)
fs = frozenset([1, 2, 3, 4, 5])

print(f"Frozen set: {fs}")

# Can be used as dictionary keys
set_dict = {
    frozenset([1, 2]): "set 1-2",
    frozenset([3, 4]): "set 3-4"
}

print(f"Set dict: {set_dict}")

# Set operations with frozenset
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

print(f"Union: {fs1 | fs2}")
print(f"Intersection: {fs1 & fs2}")
```

## Specialized Data Structures

### Strings as Data Structures
```python
# String operations
text = "Hello, World! Python is awesome."

# Indexing and slicing
print(f"First char: {text[0]}")
print(f"Last char: {text[-1]}")
print(f"Slice [7:12]: {text[7:12]}")
print(f"Every 3rd char: {text[::3]}")

# String methods
words = text.split()
print(f"Words: {words}")

joined = "-".join(words)
print(f"Joined: {joined}")

# String as list of characters
chars = list(text)
print(f"First 5 chars: {chars[:5]}")

# Character frequency
from collections import Counter
char_count = Counter(text.replace(" ", "").replace(".", ""))
print(f"Char count: {dict(char_count)}")

# Palindrome check
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print(f"Is 'racecar' palindrome: {is_palindrome('racecar')}")
print(f"Is 'hello' palindrome: {is_palindrome('hello')}")
```

### Range Objects
```python
# Range as sequence
r1 = range(10)  # 0 to 9
r2 = range(1, 11)  # 1 to 10
r3 = range(0, 20, 2)  # Even numbers 0 to 18

print(f"Range 0-9: {list(r1)}")
print(f"Range 1-10: {list(r2)}")
print(f"Range even: {list(r3)}")

# Range operations
print(f"Length of r1: {len(r1)}")
print(f"5 in r1: {5 in r1}")
print(f"r1[5]: {r1[5]}")

# Range slicing
print(f"r1[2:8]: {list(r1[2:8])}")

# Negative step
r4 = range(10, 0, -1)
print(f"Countdown: {list(r4)}")

# Memory efficiency
import sys
large_range = range(1000000)
large_list = list(range(1000000))

print(f"Range memory: {sys.getsizeof(large_range)} bytes")
print(f"List memory: {sys.getsizeof(large_list)} bytes")
```

### Bytes and Bytearray
```python
# Bytes (immutable)
b1 = b"Hello"
b2 = bytes([72, 101, 108, 108, 111])

print(f"Bytes: {b1}")
print(f"From list: {b2}")
print(f"Are equal: {b1 == b2}")

# Bytearray (mutable)
ba = bytearray(b"Hello")
ba[0] = 74  # Change 'H' to 'J'
print(f"Modified: {ba}")

# Bytes operations
text = "Hello, 世界"
encoded = text.encode('utf-8')
decoded = encoded.decode('utf-8')

print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")

# Hex representation
hex_data = encoded.hex()
print(f"Hex: {hex_data}")

# From hex
back_to_bytes = bytes.fromhex(hex_data)
print(f"Back to bytes: {back_to_bytes}")
```

## Data Structure Performance

### Time Complexity Comparison
```python
import timeit

# List vs Set membership test
large_list = list(range(10000))
large_set = set(range(10000))

def list_membership():
    return 9999 in large_list

def set_membership():
    return 9999 in large_set

list_time = timeit.timeit(list_membership, number=1000)
set_time = timeit.timeit(set_membership, number=1000)

print(f"List membership test: {list_time:.6f} seconds")
print(f"Set membership test: {set_time:.6f} seconds")
print(f"Set is {list_time / set_time:.1f}x faster")

# List vs dict lookup
large_dict = {i: f"value_{i}" for i in range(10000)}

def dict_lookup():
    return large_dict[9999]

def list_lookup():
    return large_list[9999]

dict_time = timeit.timeit(dict_lookup, number=1000)
list_time = timeit.timeit(list_lookup, number=1000)

print(f"Dict lookup: {dict_time:.6f} seconds")
print(f"List lookup: {list_time:.6f} seconds")
print(f"Dict is {list_time / dict_time:.1f}x faster")
```

### Memory Usage Comparison
```python
import sys

# Memory usage of different data structures
def memory_comparison():
    # Same data in different structures
    data = list(range(1000))
    
    list_obj = data
    tuple_obj = tuple(data)
    set_obj = set(data)
    frozenset_obj = frozenset(data)
    
    print(f"List: {sys.getsizeof(list_obj)} bytes")
    print(f"Tuple: {sys.getsizeof(tuple_obj)} bytes")
    print(f"Set: {sys.getsizeof(set_obj)} bytes")
    print(f"Frozenset: {sys.getsizeof(frozenset_obj)} bytes")
    
    # Dictionary memory
    dict_obj = {i: i for i in range(1000)}
    print(f"Dict: {sys.getsizeof(dict_obj)} bytes")
    
    # String vs list of chars
    text = "hello world " * 100
    char_list = list(text)
    
    print(f"String: {sys.getsizeof(text)} bytes")
    print(f"Char list: {sys.getsizeof(char_list)} bytes")

memory_comparison()
```

## Advanced Data Structure Patterns

### Graph Representation
```python
# Adjacency list representation
class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_edge(self, u, v, weight=1):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append((v, weight))
        
        # For undirected graph
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[v].append((u, weight))
    
    def get_neighbors(self, node):
        return self.adj_list.get(node, [])
    
    def __str__(self):
        return str(self.adj_list)

# Usage
g = Graph()
g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'D', 2)
g.add_edge('C', 'D', 4)

print(f"Graph: {g}")
print(f"Neighbors of A: {g.get_neighbors('A')}")

# Adjacency matrix representation
def adjacency_matrix(edges, nodes):
    matrix = [[0] * len(nodes) for _ in range(len(nodes))]
    node_index = {node: i for i, node in enumerate(nodes)}
    
    for u, v, weight in edges:
        i, j = node_index[u], node_index[v]
        matrix[i][j] = weight
        matrix[j][i] = weight  # For undirected
    
    return matrix

edges = [('A', 'B', 5), ('A', 'C', 3), ('B', 'D', 2), ('C', 'D', 4)]
nodes = ['A', 'B', 'C', 'D']
matrix = adjacency_matrix(edges, nodes)

print(f"Adjacency matrix:")
for row in matrix:
    print(row)
```

### Tree Representation
```python
# Binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"

# Tree construction
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Tree traversal
def inorder_traversal(node):
    if node:
        yield from inorder_traversal(node.left)
        yield node.val
        yield from inorder_traversal(node.right)

print(f"Inorder traversal: {list(inorder_traversal(root))}")

# Tree as nested dictionary
tree_dict = {
    'val': 1,
    'left': {
        'val': 2,
        'left': {'val': 4, 'left': None, 'right': None},
        'right': {'val': 5, 'left': None, 'right': None}
    },
    'right': {
        'val': 3,
        'left': None,
        'right': None
    }
}

print(f"Tree as dict: {tree_dict}")
```

### Stack and Queue Implementations
```python
# Stack implementation using list
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Queue implementation using collections.deque
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.popleft()
    
    def peek(self):
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(f"Stack pop: {stack.pop()}")
print(f"Stack peek: {stack.peek()}")

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(f"Queue dequeue: {queue.dequeue()}")
print(f"Queue peek: {queue.peek()}")
```

## Data Structure Algorithms

### Searching Algorithms
```python
# Linear search
def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

# Binary search (requires sorted array)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Usage
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

linear_result = linear_search(numbers, target)
binary_result = binary_search(numbers, target)

print(f"Linear search result: {linear_result}")
print(f"Binary search result: {binary_result}")

# Search in different data structures
def search_in_structures(target):
    # List search
    list_data = [1, 2, 3, 4, 5]
    list_result = target in list_data
    
    # Set search
    set_data = {1, 2, 3, 4, 5}
    set_result = target in set_data
    
    # Dict search
    dict_data = {1: "one", 2: "two", 3: "three"}
    dict_result = target in dict_data
    
    return {
        'list': list_result,
        'set': set_result,
        'dict': dict_result
    }

print(f"Search results for 3: {search_in_structures(3)}")
print(f"Search results for 6: {search_in_structures(6)}")
```

### Sorting Algorithms
```python
# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Using built-in sort
def builtin_sort(arr):
    return sorted(arr)

# Sort dictionary by values
def sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Sort list of dictionaries
def sort_list_of_dicts(lst, key):
    return sorted(lst, key=lambda x: x[key])

# Usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Bubble sort: {bubble_sort(numbers.copy())}")
print(f"Selection sort: {selection_sort(numbers.copy())}")
print(f"Built-in sort: {builtin_sort(numbers)}")

# Sort dictionary
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
sorted_scores = sort_dict_by_values(scores)
print(f"Sorted scores: {sorted_scores}")

# Sort list of dictionaries
students = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 30}
]
sorted_by_age = sort_list_of_dicts(students, 'age')
print(f"Sorted by age: {sorted_by_age}")
```

## Data Structure Best Practices

### Choosing the Right Data Structure
```python
def choose_data_structure():
    """
    Guidelines for choosing data structures:
    
    1. List: When you need ordered, mutable sequences
    2. Tuple: When you need ordered, immutable sequences
    3. Set: When you need unique elements and fast membership testing
    4. Dictionary: When you need key-value pairs and fast lookups
    5. String: When you need text manipulation
    """
    
    # Example scenarios
    scenarios = {
        "Shopping cart": "List (ordered, can have duplicates)",
        "Coordinates": "Tuple (immutable, fixed size)",
        "Unique users": "Set (no duplicates, fast membership)",
        "User profiles": "Dictionary (key-value lookup)",
        "Text processing": "String (text manipulation)",
        "Configuration": "Dictionary (structured key-value)"
    }
    
    for scenario, recommendation in scenarios.items():
        print(f"{scenario}: {recommendation}")

choose_data_structure()
```

### Performance Optimization
```python
# Optimize list operations
def optimize_list_operations():
    # Bad: O(n²) for large lists
    def bad_remove_duplicates(lst):
        result = []
        for item in lst:
            if item not in result:  # O(n) search in result
                result.append(item)
        return result
    
    # Good: O(n) using set
    def good_remove_duplicates(lst):
        return list(set(lst))
    
    # Preserve order: O(n) with set for tracking
    def preserve_order_remove_duplicates(lst):
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    
    # Test
    import time
    large_list = list(range(10000)) + list(range(5000))
    
    start = time.time()
    bad_result = bad_remove_duplicates(large_list[:1000])  # Small for demo
    bad_time = time.time() - start
    
    start = time.time()
    good_result = good_remove_duplicates(large_list)
    good_time = time.time() - start
    
    start = time.time()
    preserve_result = preserve_order_remove_duplicates(large_list)
    preserve_time = time.time() - start
    
    print(f"Bad method (1000 items): {bad_time:.6f}s")
    print(f"Good method (10000 items): {good_time:.6f}s")
    print(f"Preserve order method (10000 items): {preserve_time:.6f}s")

optimize_list_operations()

# Memory-efficient processing
def memory_efficient_processing():
    # Generator instead of list
    def number_generator(n):
        for i in range(n):
            yield i * i
    
    # Process large data without loading all into memory
    def process_large_file(filename):
        with open(filename, 'r') as f:
            for line in f:
                yield line.strip().lower()
    
    print("Memory-efficient patterns:")
    print("1. Use generators for large sequences")
    print("2. Use iterators for file processing")
    print("3. Use sets for membership testing")
    print("4. Use dictionaries for lookups instead of linear search")

memory_efficient_processing()
```

## Common Data Structure Patterns

### Memoization
```python
# Memoization using dictionary
def memoize(func):
    cache = {}
    
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test memoization
import time

start = time.time()
result = fibonacci(35)
end = time.time()

print(f"Fibonacci(35) = {result}")
print(f"Time with memoization: {end - start:.6f}s")
```

### Caching with LRU
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(x):
    # Simulate expensive computation
    import time
    time.sleep(0.1)
    return x * x

# Test LRU cache
import time

start = time.time()
result1 = expensive_function(42)
end = time.time()
print(f"First call: {end - start:.6f}s")

start = time.time()
result2 = expensive_function(42)
end = time.time()
print(f"Cached call: {end - start:.6f}s")
```

## Best Practices

1. **Choose the right data structure** for your specific use case
2. **Use sets for membership testing** when you need fast lookups
3. **Use dictionaries for key-value mappings** and fast access
4. **Prefer tuples over lists** for immutable sequences
5. **Use comprehensions** for concise and efficient data structure creation
6. **Consider memory usage** when working with large datasets
7. **Use generators** for memory-efficient processing of large sequences
8. **Leverage built-in functions** and methods for optimal performance
9. **Profile your code** to identify bottlenecks
10. **Use appropriate data structures** for algorithms (e.g., sets for intersection, dicts for counting)

## Conclusion

Python's built-in data structures provide a powerful and flexible foundation for implementing algorithms and solving problems. Understanding the characteristics, performance implications, and appropriate use cases for each data structure is essential for writing efficient and maintainable Python code. By leveraging Python's rich set of data structures and following best practices, you can create elegant solutions that are both readable and performant.
