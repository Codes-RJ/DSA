# Python Variables and Keywords

## Overview

Variables in Python are named storage locations that hold data values. Unlike statically-typed languages, Python is dynamically typed, meaning variables don't need explicit type declarations. Keywords are reserved words that have special meaning to the Python interpreter and cannot be used as identifiers.

## Python Keywords

Python has 35 reserved keywords (as of Python 3.11). These are divided into several categories:

### Value Keywords
```python
True        # Boolean true value
False       # Boolean false value
None        # Null/absent value
```

### Operator Keywords
```python
and         # Logical AND
or          # Logical OR
not         # Logical NOT
in          # Membership test
is          # Identity test
```

### Control Flow Keywords
```python
if          # Conditional statement
elif        # Else if conditional
else        # Else conditional
for         # For loop
while       # While loop
break       # Exit loop
continue    # Skip to next iteration
pass        # Null statement
return      # Return from function
```

### Structure Keywords
```python
def         # Function definition
class       # Class definition
lambda      # Anonymous function
```

### Import Keywords
```python
import      # Import module
from        # Import specific from module
as          # Alias for import
```

### Exception Handling Keywords
```python
try         # Try block
except      # Exception handler
finally     # Finally block
raise       # Raise exception
```

### Async Programming Keywords
```python
async       # Async function definition
await      # Await expression
```

### Other Keywords
```python
del         # Delete object
global      # Global variable declaration
nonlocal    # Nonlocal variable declaration
yield       # Generator function
with        # Context manager
assert      # Assertion statement
```

## Variable Declaration and Assignment

### Basic Variable Assignment
```python
# Simple assignments
name = "Alice"
age = 25
height = 5.7
is_student = True

# Multiple assignments
x, y, z = 10, 20, 30
first_name, last_name = "John", "Doe"

# Same value to multiple variables
a = b = c = 0

# Swapping variables
x, y = y, x

print(f"Name: {name}, Age: {age}")
print(f"Coordinates: ({x}, {y}, {z})")
print(f"Swapped: x={x}, y={y}")
```

### Dynamic Typing
```python
# Variables can change type dynamically
value = 42          # Integer
print(f"Type: {type(value)}, Value: {value}")

value = "Hello"     # String
print(f"Type: {type(value)}, Value: {value}")

value = [1, 2, 3]   # List
print(f"Type: {type(value)}, Value: {value}")

value = 3.14       # Float
print(f"Type: {type(value)}, Value: {value}")

# Type checking
if isinstance(value, float):
    print("value is a float")

if type(value) == float:
    print("value is exactly a float")
```

### Type Annotations (Python 3.5+)
```python
# Basic type annotations
name: str = "Alice"
age: int = 25
height: float = 5.7
grades: list = [90, 85, 88]

# Function type annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

def calculate_area(length: float, width: float) -> float:
    return length * width

# Complex type annotations
from typing import List, Dict, Optional, Union

numbers: List[int] = [1, 2, 3, 4, 5]
person: Dict[str, Union[str, int]] = {"name": "Bob", "age": 30}
optional_value: Optional[str] = None

print(greet("World"))
print(f"Area: {calculate_area(10.5, 5.2)}")
```

## Variable Types in Detail

### Numeric Types
```python
# Integer
integer_var = 42
large_integer = 123456789012345678901234567890
negative_integer = -17
binary_integer = 0b1010  # 10 in decimal
octal_integer = 0o12     # 10 in decimal
hexadecimal_integer = 0xA  # 10 in decimal

# Float
float_var = 3.14159
scientific_notation = 1.23e-4  # 0.000123
negative_float = -2.5

# Complex numbers
complex_var = 2 + 3j
another_complex = complex(1, -1)

print(f"Integer: {integer_var}")
print(f"Large integer: {large_integer}")
print(f"Binary: {binary_integer}")
print(f"Float: {float_var}")
print(f"Complex: {complex_var}")
print(f"Complex real: {complex_var.real}, imag: {complex_var.imag}")

# Type conversions
int_from_float = int(3.9)      # 3 (truncates)
float_from_int = float(42)     # 42.0
int_from_string = int("123")   # 123
float_from_string = float("3.14")  # 3.14

print(f"int(3.9) = {int_from_float}")
print(f"float(42) = {float_from_int}")
```

### String Type
```python
# String creation
single_quote = 'Hello'
double_quote = "World"
triple_quote = """Multi-line
string"""

# String operations
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"

# String formatting (f-strings - Python 3.6+)
age = 25
formatted = f"{name} is {age} years old"
precision = f"Pi: {3.14159:.2f}"

print(full_greeting)
print(formatted)
print(precision)

# String methods
text = "Hello, World!"
print(f"Lower: {text.lower()}")
print(f"Upper: {text.upper()}")
print(f"Title: {text.title()}")
print(f"Length: {len(text)}")
print(f"Contains 'Hello': {text.startswith('Hello')}")
print(f"Ends with '!': {text.endswith('!')}")
print(f"Find 'World': {text.find('World')}")
print(f"Replace: {text.replace('World', 'Python')}")

# String slicing
substring = text[7:12]  # "World"
print(f"Substring: {substring}")

# Multiline string formatting
multiline = f"""
Name: {name}
Age: {age}
Status: {'Active' if age > 18 else 'Minor'}
"""
print(multiline)
```

### Boolean Type
```python
# Boolean values
is_true = True
is_false = False

# Truthy and falsy values
truthy_values = [
    True, 1, -1, 3.14, "hello", [1, 2, 3], (1, 2), {"key": "value"}
]

falsy_values = [
    False, 0, 0.0, "", [], (), {}, set(), None
]

print("Truthy values:")
for val in truthy_values:
    print(f"  {val} -> {bool(val)}")

print("Falsy values:")
for val in falsy_values:
    print(f"  {val} -> {bool(val)}")

# Boolean operations
x, y = True, False
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# Short-circuit evaluation
def expensive_operation():
    print("Expensive operation called!")
    return True

# Second operand not evaluated due to short-circuit
result = False and expensive_operation()
print(f"Result: {result}")

result = True or expensive_operation()
print(f"Result: {result}")
```

### Collection Types

#### Lists
```python
# List creation
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# List operations
numbers.append(6)
numbers.insert(0, 0)
numbers.extend([7, 8, 9])

print(f"Numbers: {numbers}")
print(f"Length: {len(numbers)}")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Slice [1:4]: {numbers[1:4]}")

# List comprehension
squares = [x**2 for x in range(10)]
even_numbers = [x for x in range(20) if x % 2 == 0]

print(f"Squares: {squares}")
print(f"Even numbers: {even_numbers}")

# List methods
numbers.remove(5)
popped = numbers.pop()
numbers.sort()

print(f"After operations: {numbers}")
print(f"Popped: {popped}")
```

#### Tuples
```python
# Tuple creation
empty_tuple = ()
single_element = (1,)  # Note the comma
coordinates = (10, 20)
mixed_tuple = (1, "hello", 3.14)

# Tuple operations
x, y = coordinates  # Unpacking
print(f"Coordinates: x={x}, y={y}")

# Tuple methods
numbers = (1, 2, 3, 2, 1)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

# Immutable nature
try:
    numbers[0] = 99
except TypeError as e:
    print(f"Error: {e}")

# Named tuples (Python 3.6+)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Point: x={p.x}, y={p.y}")
```

#### Dictionaries
```python
# Dictionary creation
empty_dict = {}
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Dictionary operations
print(f"Name: {person['name']}")
print(f"Age: {person.get('age', 'Unknown')}")

person["email"] = "alice@example.com"
person.update({"age": 26, "status": "active"})

print(f"Updated: {person}")

# Dictionary methods
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Dictionary comprehension
squares = {x: x**2 for x in range(10)}
word_count = {word: len(word) for word in ["hello", "world", "python"]}

print(f"Squares: {squares}")
print(f"Word lengths: {word_count}")

# Default dictionary
from collections import defaultdict
dd = defaultdict(int)
dd["missing"] += 1
print(f"Default dict: {dict(dd)}")
```

#### Sets
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
numbers.remove(1)

print(f"After operations: {numbers}")

# Set comprehension
squares = {x**2 for x in range(10)}
print(f"Square set: {squares}")

# Frozen set (immutable set)
frozen = frozenset([1, 2, 3])
print(f"Frozen set: {frozen}")
```

## Variable Scope and Lifetime

### Local and Global Variables
```python
# Global variable
global_var = "I am global"

def demonstrate_scope():
    # Local variable
    local_var = "I am local"
    
    print(f"Inside function - global_var: {global_var}")
    print(f"Inside function - local_var: {local_var}")
    
    # Modify global variable
    global global_var
    global_var = "Modified global"
    
    # Nested function
    def nested_function():
        nonlocal_var = "I am nonlocal"
        print(f"Nested - global_var: {global_var}")
        print(f"Nested - nonlocal_var: {nonlocal_var}")
    
    nested_function()

demonstrate_scope()
print(f"Outside function - global_var: {global_var}")

# Error: local_var not accessible outside function
try:
    print(local_var)
except NameError as e:
    print(f"Error: {e}")
```

### LEGB Rule
```python
# Local, Enclosing, Global, Built-in scope

x = "global"  # Global scope

def outer_function():
    x = "enclosing"  # Enclosing scope
    
    def inner_function():
        x = "local"  # Local scope
        print(f"Local x: {x}")
    
    inner_function()
    print(f"Enclosing x: {x}")

outer_function()
print(f"Global x: {x}")

# Accessing different scopes
def scope_demo():
    global_var = "global"
    
    def nested():
        nonlocal global_var  # Error: no nonlocal variable
        pass

# Built-in scope
print(f"Built-in len function: {len}")
```

### Closures
```python
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

times_two = make_multiplier(2)
times_five = make_multiplier(5)

print(f"10 * 2 = {times_two(10)}")
print(f"10 * 5 = {times_five(10)}")

# Closure with mutable default
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c1 = counter()
c2 = counter()

print(f"Counter 1: {c1()}, {c1()}, {c1()}")
print(f"Counter 2: {c2()}, {c2()}")
```

## Advanced Variable Features

### Variable Attributes and Properties
```python
class Person:
    def __init__(self, name):
        self._name = name  # Private convention
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
    
    @property
    def name_length(self):
        return len(self._name)

person = Person("Alice")
print(f"Name: {person.name}")
print(f"Name length: {person.name_length}")

person.name = "Bob"
print(f"New name: {person.name}")

try:
    person.name = ""
except ValueError as e:
    print(f"Error: {e}")
```

### Dynamic Variable Creation
```python
class DynamicVariables:
    def __init__(self):
        pass
    
    def __setattr__(self, name, value):
        print(f"Setting {name} = {value}")
        super().__setattr__(name, value)
    
    def __getattr__(self, name):
        print(f"Getting {name}")
        return f"Dynamic value for {name}"

obj = DynamicVariables()
obj.dynamic_attr = "Hello"
print(f"Dynamic attr: {obj.nonexistent_attr}")

# Using globals() and locals()
def create_variables():
    for i in range(3):
        var_name = f"var_{i}"
        globals()[var_name] = i * 10

create_variables()
print(f"var_0: {var_0}")
print(f"var_1: {var_1}")
print(f"var_2: {var_2}")
```

### Memory Management and References
```python
# Reference counting
import sys

a = [1, 2, 3]
b = a  # b references the same list
c = a.copy()  # c is a separate copy

print(f"a id: {id(a)}")
print(f"b id: {id(b)}")
print(f"c id: {id(c)}")

print(f"a is b: {a is b}")
print(f"a is c: {a is c}")

b.append(4)
print(f"After modifying b:")
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

# Weak references
import weakref

class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"MyClass({self.value})"

obj = MyClass(42)
weak_ref = weakref.ref(obj)

print(f"Object: {obj}")
print(f"Weak ref: {weak_ref()}")

del obj
print(f"After deletion: {weak_ref()}")  # None
```

## Special Variables and Dunder Methods

### Built-in Special Variables
```python
# __name__ - module name
if __name__ == "__main__":
    print("Running as main script")

# __file__ - current file path
print(f"Current file: {__file__}")

# __doc__ - docstring
"""This is a module docstring."""
print(f"Module docstring: {__doc__}")

# __package__ - package name
print(f"Package: {__package__}")

# __annotations__ - type annotations
def annotated_function(x: int, y: str) -> float:
    return float(x)

print(f"Annotations: {annotated_function.__annotations__}")
```

### Dunder Methods in Classes
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        return 2
    
    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError("Index out of range")

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"v1 == v2: {v1 == v2}")
print(f"len(v1): {len(v1)}")
print(f"v1[0]: {v1[0]}")
```

## Variable Naming Conventions

### Naming Rules and Conventions
```python
# Valid names
variable = 1
_variable = 2
variable_ = 3
_var_iable_ = 4
variable123 = 5

# Invalid names (will cause SyntaxError)
# 123variable = 1  # Cannot start with number
# variable-name = 2  # Cannot contain hyphen
# variable name = 3  # Cannot contain space
# class = 4         # Cannot use keyword

# Naming conventions (PEP 8)
# Variables and functions: snake_case
my_variable = 10
def calculate_sum():
    pass

# Constants: UPPER_SNAKE_CASE
MAX_SIZE = 100
PI = 3.14159

# Classes: PascalCase
class MyClass:
    pass

# Private variables: single underscore prefix
_private_var = "private"

# "Magic" variables: double underscore prefix
__magic_var = "magic"

# Avoid these
x = 1                    # Meaningless name
a1, b2, c3 = 1, 2, 3    # Non-descriptive
temp = "temporary"       # Too generic
num = 42                 # Abbreviation, be more specific

# Good practices
user_age = 25
email_address = "user@example.com"
max_retry_attempts = 3
is_valid_input = True
```

## Type Hints and Advanced Typing

### Generic Types
```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()
    
    def is_empty(self) -> bool:
        return not self._items

# Usage
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
print(f"Popped: {int_stack.pop()}")

str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")
print(f"Popped: {str_stack.pop()}")
```

### Union and Optional Types
```python
from typing import Union, Optional

def process_value(value: Union[int, str, float]) -> str:
    if isinstance(value, int):
        return f"Integer: {value}"
    elif isinstance(value, str):
        return f"String: {value}"
    elif isinstance(value, float):
        return f"Float: {value:.2f}"
    else:
        return "Unknown type"

def find_user(user_id: int) -> Optional[str]:
    # Simulate database lookup
    if user_id == 1:
        return "Alice"
    return None

print(process_value(42))
print(process_value("hello"))
print(process_value(3.14159))

user = find_user(1)
if user:
    print(f"Found user: {user}")
else:
    print("User not found")
```

## Performance Considerations

### Variable Lookup Performance
```python
import timeit

# Local vs global variable lookup
def local_lookup():
    x = 10
    return x

def global_lookup():
    return global_var

global_var = 10

# Benchmark
local_time = timeit.timeit(local_lookup, number=1000000)
global_time = timeit.timeit(global_lookup, number=1000000)

print(f"Local lookup: {local_time:.6f} seconds")
print(f"Global lookup: {global_time:.6f} seconds")
print(f"Ratio: {global_time / local_time:.2f}x slower")

# Attribute lookup performance
class TestClass:
    def __init__(self):
        self.attr = 10

obj = TestClass()

def attribute_lookup():
    return obj.attr

def local_var_lookup():
    x = 10
    return x

attr_time = timeit.timeit(attribute_lookup, number=1000000)
local_time = timeit.timeit(local_var_lookup, number=1000000)

print(f"Attribute lookup: {attr_time:.6f} seconds")
print(f"Local var lookup: {local_time:.6f} seconds")
print(f"Ratio: {attr_time / local_time:.2f}x slower")
```

### Memory Usage
```python
import sys

# Memory usage of different types
def memory_usage():
    i = 42
    f = 3.14159
    s = "hello"
    l = [1, 2, 3, 4, 5]
    t = (1, 2, 3, 4, 5)
    d = {"a": 1, "b": 2}
    
    print(f"Integer size: {sys.getsizeof(i)} bytes")
    print(f"Float size: {sys.getsizeof(f)} bytes")
    print(f"String size: {sys.getsizeof(s)} bytes")
    print(f"List size: {sys.getsizeof(l)} bytes")
    print(f"Tuple size: {sys.getsizeof(t)} bytes")
    print(f"Dict size: {sys.getsizeof(d)} bytes")

memory_usage()

# List vs tuple memory
large_list = list(range(1000))
large_tuple = tuple(range(1000))

print(f"Large list: {sys.getsizeof(large_list)} bytes")
print(f"Large tuple: {sys.getsizeof(large_tuple)} bytes")
print(f"Tuple is {sys.getsizeof(large_list) / sys.getsizeof(large_tuple):.1f}x smaller")
```

## Best Practices

1. **Use descriptive names** that clearly indicate the variable's purpose
2. **Follow PEP 8 naming conventions** consistently
3. **Use type hints** for better code documentation and IDE support
4. **Minimize global variables** - prefer local variables and function parameters
5. **Use constants** (uppercase) for values that don't change
6. **Avoid single-letter variables** except for loop counters or mathematical contexts
7. **Use meaningful variable names** even if they're longer
8. **Initialize variables** before use to avoid NameError
9. **Use appropriate data types** for the data you're storing
10. **Consider memory usage** when working with large datasets

## Common Pitfalls

### Mutable Default Arguments
```python
# Bad practice - mutable default argument
def bad_append(item, items=[]):
    items.append(item)
    return items

# Good practice - immutable default argument
def good_append(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print("Bad practice:")
print(bad_append(1))  # [1]
print(bad_append(2))  # [1, 2] - unexpected!

print("\nGood practice:")
print(good_append(1))  # [1]
print(good_append(2))  # [1, 2] - expected
```

### Late Binding in Closures
```python
# Problem: Late binding
multipliers = []
for i in range(3):
    multipliers.append(lambda x: x * i)

print("Late binding problem:")
for m in multipliers:
    print(m(2))  # All print 4, not 0, 2, 4

# Solution: Early binding
multipliers = []
for i in range(3):
    multipliers.append(lambda x, i=i: x * i)  # Capture current i

print("\nEarly binding solution:")
for m in multipliers:
    print(m(2))  # 0, 2, 4 as expected
```

## Conclusion

Understanding variables and keywords is fundamental to Python programming. Python's dynamic typing system, combined with modern features like type hints and comprehensive built-in data types, provides both flexibility and power. By following naming conventions, understanding scope rules, and being aware of performance implications, you can write clean, efficient, and maintainable Python code that effectively leverages the language's dynamic nature while maintaining clarity and reliability.
