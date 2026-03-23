Here is a comprehensive Markdown document covering Python Variables, Keywords, and Operators, structured similarly to the Java version you provided.

---

# Python Variables, Keywords, and Operators

## Overview
- Variables in Python are names that refer to objects stored in memory. Python is a dynamically-typed language, meaning variables can hold values of any type and can be reassigned to different types during execution.
- Keywords are reserved words that have a predefined meaning in the Python language and cannot be used as identifiers (like variable or function names).
- Understanding variables and keywords is fundamental to Python programming and its philosophy of simplicity and readability.

## Python Keywords

Python has 35 reserved keywords (as of Python 3.11). Here are the most important ones, categorized by their use:

### Value Keywords
```python
True            # Boolean true value
False           # Boolean false value
None            # Null object (absence of value)
```

### Control Flow Keywords
```python
# Conditional statements
if              # Conditional branch
elif            # Else-if branch (unique to Python)
else            # Alternative branch

# Loops
for             # For loop (iteration over sequences)
while           # While loop

# Loop control
break           # Exit loop
continue        # Skip to next iteration
pass            # Null operation (placeholder)

# Exception handling
try             # Start of exception handling block
except          # Catch an exception
finally         # Code that always executes
raise           # Raise an exception
assert          # Debugging assertion
```

### Function and Class Keywords
```python
def             # Define a function
return          # Return a value from a function
lambda          # Create an anonymous function
class           # Define a class
global          # Declare a global variable
nonlocal        # Declare a variable from an outer scope (Python 3+)
```

### Logical and Membership Keywords
```python
and             # Logical AND
or              # Logical OR
not             # Logical NOT
in              # Check membership in a sequence
is              # Check object identity (same object, not value)
```

### Exception-Related Keywords
```python
try             # Start of exception block
except          # Handle an exception
finally         # Code that always executes after try/except
raise           # Explicitly raise an exception
assert          # For debugging assertions
```

### Asynchronous Programming Keywords (Python 3.5+)
```python
async           # Define an asynchronous function
await           # Wait for an asynchronous operation
```

### Context Management
```python
with            # Context manager (automatic resource management)
as              # Assigns the result of a context manager or exception
```

### Import and Module Keywords
```python
import          # Import a module
from            # Import specific attributes from a module
```

### Deletion and Type Keywords
```python
del             # Delete a variable or object
```

### Reserved Keywords (Not used but reserved for future)
```python
# These are reserved for future use and cannot be used as identifiers
# match, case (Python 3.10+ pattern matching)
```

## Variable Declaration and Initialization

### Basic Variable Declaration
```python
# Python doesn't require explicit declaration - assignment creates variables
# Declaration without initialization (impossible - Python requires value)
# Instead, variables are created when first assigned

# Simple assignments
age = 25
salary = 50000.50
grade = 'A'
is_student = True
name = "Alice"

# Multiple assignments in one line
x = y = z = 10           # All three variables reference the same integer 10

# Multiple assignment with different values
a, b, c = 1, 2, 3        # a=1, b=2, c=3

# Swapping variables (Python's unique feature)
a, b = b, a              # Swaps values without temporary variable

# Variables can be reassigned to different types (dynamic typing)
variable = 42            # int
variable = "Hello"       # now str
variable = [1, 2, 3]     # now list

# Checking variable type
print(type(variable))    # <class 'list'>

# Deleting a variable
del variable             # Deletes the variable reference
# print(variable)        # NameError: name 'variable' is not defined
```

### Variable Types in Detail

#### Numeric Types: Integers
```python
def integer_examples():
    # Different integer representations
    decimal = 42                    # Base 10
    binary = 0b101010              # Base 2 (prefix 0b)
    octal = 0o52                   # Base 8 (prefix 0o)
    hexadecimal = 0x2A             # Base 16 (prefix 0x)
    
    # Integers in Python are arbitrary precision (no overflow)
    large_number = 10 ** 100       # 1 followed by 100 zeros
    
    # Using underscores for readability (Python 3.6+)
    million = 1_000_000
    credit_card = 1234_5678_9012_3456
    
    print(f"Decimal: {decimal}")
    print(f"Binary: {binary}")
    print(f"Octal: {octal}")
    print(f"Hexadecimal: {hexadecimal}")
    print(f"Large number: {large_number}")
    print(f"Million: {million}")
```

#### Numeric Types: Floating-Point
```python
def float_examples():
    # Floating-point numbers
    pi = 3.14159
    scientific = 1.23e-4           # 0.000123
    
    # Special floating-point values
    positive_infinity = float('inf')
    negative_infinity = float('-inf')
    not_a_number = float('nan')
    
    # Floating-point precision (Python uses double-precision)
    # Imprecision example
    print(0.1 + 0.2)               # 0.30000000000000004 (not 0.3)
    
    # Better to use Decimal for precise decimal arithmetic
    from decimal import Decimal
    precise = Decimal('0.1') + Decimal('0.2')
    print(precise)                 # 0.3
    
    print(f"PI: {pi}")
    print(f"Scientific: {scientific}")
    print(f"Infinity: {positive_infinity}")
```

#### Numeric Types: Complex Numbers
```python
def complex_examples():
    # Complex numbers (unique to Python among common languages)
    z1 = 3 + 4j                    # 3 + 4i
    z2 = complex(2, 3)             # 2 + 3j
    
    # Access real and imaginary parts
    print(f"Real: {z1.real}, Imaginary: {z1.imag}")
    
    # Operations with complex numbers
    print(f"Addition: {z1 + z2}")
    print(f"Multiplication: {z1 * z2}")
    
    # Magnitude (absolute value)
    print(f"Magnitude: {abs(z1)}")  # 5.0
```

#### Boolean Type
```python
def boolean_examples():
    # Boolean values (subclass of int)
    is_true = True
    is_false = False
    
    # Booleans are actually integers (True = 1, False = 0)
    print(f"True + True = {True + True}")        # 2
    print(f"True * 5 = {True * 5}")              # 5
    print(f"False * 10 = {False * 10}")          # 0
    
    # Boolean from comparisons
    from_comparison = (5 > 3)                    # True
    
    # Boolean operations
    and_result = is_true and is_false            # False
    or_result = is_true or is_false              # True
    not_result = not is_true                     # False
    xor_result = is_true ^ is_false              # True (XOR)
    
    # Truthy and falsy values
    # Falsy values: False, None, 0, 0.0, "" (empty string), [], {}, set()
    # All other values are truthy
    
    print(f"Empty list is falsy: {bool([])}")    # False
    print(f"Non-empty list is truthy: {bool([1, 2])}")  # True
```

#### String Type
```python
def string_examples():
    # String creation (immutable)
    single_quotes = 'Hello, World!'
    double_quotes = "Hello, World!"
    
    # Triple quotes for multi-line strings
    multi_line = """This is a
    multi-line
    string"""
    
    # Raw strings (ignore escape sequences)
    raw_string = r"C:\Users\Name\Documents"      # Backslashes are literal
    
    # F-strings for formatting (Python 3.6+)
    name = "Alice"
    age = 25
    greeting = f"Hello, {name}! You are {age} years old."
    
    # String operations
    print(f"Length: {len(greeting)}")
    print(f"Uppercase: {greeting.upper()}")
    print(f"Split: {greeting.split()}")
    
    # String concatenation
    combined = "Hello" + " " + "World"
    
    # String repetition
    repeated = "Ha" * 3                         # "HaHaHa"
    
    # String indexing and slicing
    text = "Python"
    print(f"First char: {text[0]}")             # 'P'
    print(f"Last char: {text[-1]}")             # 'n'
    print(f"Slicing: {text[1:4]}")              # "yth"
    print(f"Step slicing: {text[::2]}")         # "Pto"
    
    # Check substring
    if "Py" in text:
        print("Contains Py")
```

#### Sequence Types: Lists
```python
def list_examples():
    # Lists are mutable, ordered sequences
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "Hello", 3.14, True, [1, 2]]   # Lists can contain mixed types
    
    # Creating lists
    empty_list = []
    list_from_range = list(range(5))            # [0, 1, 2, 3, 4]
    list_comprehension = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
    
    # List operations
    numbers.append(6)                           # Add to end
    numbers.insert(0, 0)                        # Insert at index
    numbers.extend([7, 8, 9])                   # Extend with another list
    
    # Removing elements
    numbers.remove(5)                           # Remove first occurrence of value
    popped = numbers.pop()                      # Remove and return last element
    numbers.pop(0)                              # Remove and return element at index
    del numbers[1]                              # Delete by index
    
    # List slicing
    sublist = numbers[1:4]                      # Get slice
    reversed_list = numbers[::-1]               # Reverse list
    
    # List concatenation
    combined = [1, 2] + [3, 4]                  # [1, 2, 3, 4]
    
    # List repetition
    repeated = [1, 2] * 3                       # [1, 2, 1, 2, 1, 2]
    
    print(f"List: {numbers}")
    print(f"Length: {len(numbers)}")
    print(f"Sliced: {sublist}")
```

#### Sequence Types: Tuples
```python
def tuple_examples():
    # Tuples are immutable, ordered sequences
    point = (10, 20)
    single_element = (5,)                       # Note: comma is necessary
    empty_tuple = ()
    
    # Without parentheses (tuple packing)
    coordinates = 10, 20, 30                    # This is a tuple
    
    # Tuple unpacking
    x, y, z = coordinates                       # x=10, y=20, z=30
    
    # Named tuples (Python 2.6+)
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    print(f"Point: ({p.x}, {p.y})")
    
    # Tuple methods
    print(f"Count: {coordinates.count(10)}")    # 1
    print(f"Index: {coordinates.index(20)}")    # 1
    
    # Tuples are more memory efficient than lists
    # Used when data should not change (immutable)
    
    print(f"Tuple: {coordinates}")
    print(f"Unpacked: {x}, {y}, {z}")
```

#### Set Types
```python
def set_examples():
    # Sets are unordered collections of unique elements
    fruits = {'apple', 'banana', 'orange', 'apple'}  # Duplicates removed
    empty_set = set()                                # {} is empty dict, not set
    
    # Set operations
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    # Set methods
    set1.add(6)                                     # Add element
    set1.remove(6)                                  # Remove element (raises error if missing)
    set1.discard(10)                                # Remove if exists (no error)
    
    # Mathematical set operations
    union = set1 | set2                             # {1,2,3,4,5,6,7,8}
    intersection = set1 & set2                      # {4,5}
    difference = set1 - set2                        # {1,2,3}
    symmetric_diff = set1 ^ set2                    # {1,2,3,6,7,8}
    
    # Set comprehension
    squares = {x**2 for x in range(10)}             # {0,1,4,9,16,25,36,49,64,81}
    
    # Check membership (very fast - O(1))
    if 3 in set1:
        print("3 is in set1")
    
    print(f"Set1: {set1}")
    print(f"Set2: {set2}")
    print(f"Union: {union}")
```

#### Dictionary Types
```python
def dictionary_examples():
    # Dictionaries are key-value mappings (hash tables)
    person = {
        'name': 'Alice',
        'age': 25,
        'city': 'New York'
    }
    
    empty_dict = {}
    
    # Creating with dict() constructor
    person2 = dict(name='Bob', age=30, city='Boston')
    
    # Accessing values
    name = person['name']                           # 'Alice'
    age = person.get('age', 0)                      # Safe access with default
    # salary = person['salary']                     # KeyError if missing
    
    # Adding/updating
    person['email'] = 'alice@example.com'           # Add new key
    person['age'] = 26                              # Update existing
    
    # Dictionary methods
    keys = person.keys()                            # dict_keys(['name', 'age', ...])
    values = person.values()                        # dict_values(['Alice', 26, ...])
    items = person.items()                          # dict_items([('name', 'Alice'), ...])
    
    # Dictionary comprehension
    squares = {x: x**2 for x in range(5)}           # {0:0, 1:1, 2:4, 3:9, 4:16}
    
    # Merging dictionaries (Python 3.9+)
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    merged = dict1 | dict2                          # {'a':1, 'b':2, 'c':3, 'd':4}
    
    # Looping through dictionaries
    for key, value in person.items():
        print(f"{key}: {value}")
    
    print(f"Person: {person}")
    print(f"Squares: {squares}")
```

#### None Type
```python
def none_examples():
    # None represents absence of value (similar to null in other languages)
    result = None
    
    # None is a singleton (only one instance)
    x = None
    y = None
    print(x is y)                                    # True
    
    # Checking for None
    if result is None:                               # Use 'is', not '=='
        print("No result")
    
    # None in function returns (default)
    def no_return():
        pass
    
    print(no_return())                               # None
    
    # None is falsy
    if not result:
        print("None is falsy")
```

## Variable Scope and Lifetime

### Local Variables
```python
def local_scope():
    """Variables defined inside functions are local"""
    local_var = 10                    # Local to this function
    
    def inner_function():
        inner_var = 20                # Local to inner function
        print(f"Inner: {inner_var}")
        print(f"Can access outer: {local_var}")  # Can access enclosing scope
    
    inner_function()
    # print(inner_var)                # NameError: inner_var not defined
    
    print(f"Local: {local_var}")

# print(local_var)                    # NameError: local_var not defined

# LEGB Rule: Local, Enclosing, Global, Built-in
```

### Global Variables
```python
# Module-level variables are global within the module
global_counter = 0
module_constant = "This is global"

def increment_counter():
    global global_counter            # 'global' keyword needed to modify
    global_counter += 1
    
    # Reading global variable doesn't require 'global'
    print(f"Reading global: {module_constant}")
    
    # Creating a local variable with same name (shadowing)
    module_constant = "Local version"
    print(f"Local version: {module_constant}")

def read_global():
    # Can read global without 'global' keyword
    print(f"Global counter: {global_counter}")
    print(f"Global constant: {module_constant}")    # Original global value

increment_counter()
increment_counter()
read_global()

print(f"Final global counter: {global_counter}")
```

### Nonlocal Variables (Python 3+)
```python
def outer_function():
    outer_var = "outer"
    
    def middle_function():
        middle_var = "middle"
        
        def inner_function():
            nonlocal outer_var, middle_var    # Access enclosing scopes
            outer_var = "modified outer"
            middle_var = "modified middle"
            
            local_var = "local"
            print(f"Inner: {outer_var}, {middle_var}, {local_var}")
        
        inner_function()
        print(f"Middle: {outer_var}, {middle_var}")  # Shows modified values
    
    middle_function()
    print(f"Outer: {outer_var}")               # Shows modified value

outer_function()
```

### Function and Class Scope
```python
def function_scope_examples():
    # Function arguments are local to the function
    def greet(name):                          # 'name' is local
        greeting = f"Hello, {name}"           # 'greeting' is local
        return greeting
    
    # print(name)                             # NameError
    # print(greeting)                         # NameError
    
    # Class scope
    class MyClass:
        class_var = "class variable"           # Class attribute
        
        def __init__(self, instance_var):
            self.instance_var = instance_var   # Instance attribute
        
        def method(self):
            local_var = "method local"         # Local to method
            print(f"Class: {self.class_var}")
            print(f"Instance: {self.instance_var}")
            print(f"Local: {local_var}")
    
    obj = MyClass("instance value")
    obj.method()
    
    # Class attributes can be accessed without instance
    print(f"Class attribute: {MyClass.class_var}")

function_scope_examples()
```

## Constants (Convention-Based)

### Using Uppercase Names
```python
# Python doesn't have true constants - by convention, uppercase indicates constant
MAX_CONNECTIONS = 100
PI = 3.141592653589793
DATABASE_URL = "postgresql://localhost/mydb"

# Can still be modified (no enforcement)
# MAX_CONNECTIONS = 200  # No error, but violates convention

# For stricter enforcement, use properties or custom classes
class Constants:
    """Simulate constants using property decorator"""
    def __init__(self):
        self._max_connections = 100
    
    @property
    def MAX_CONNECTIONS(self):
        return self._max_connections
    
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"Constant '{name}' cannot be modified")

# constants = Constants()
# constants.MAX_CONNECTIONS = 200  # Raises AttributeError
```

## Type Hints (Python 3.5+)

```python
from typing import List, Tuple, Dict, Optional, Union, Any

def type_hints_examples():
    # Variable type hints (informational only)
    age: int = 25
    name: str = "Alice"
    scores: List[int] = [95, 87, 92]
    person: Dict[str, Union[str, int]] = {"name": "Alice", "age": 25}
    coordinates: Tuple[int, int] = (10, 20)
    
    # Optional type (can be None)
    middle_name: Optional[str] = None
    
    # Any type (dynamic)
    anything: Any = "can be anything"
    anything = 42
    
    # Function type hints
    def greet(name: str) -> str:
        return f"Hello, {name}"
    
    def process_data(data: List[int]) -> Optional[int]:
        if data:
            return sum(data)
        return None
    
    # Type hints don't affect runtime - they're for documentation and type checkers
    # mypy or other tools can validate types
    
    print(f"Age: {age}, Name: {name}")
    print(f"Scores: {scores}")
```

## Type Conversions

### Implicit Conversions
```python
def implicit_conversions():
    # Python performs implicit conversions in expressions
    result = 10 + 3.5                     # int + float -> float
    print(f"10 + 3.5 = {result} ({type(result)})")  # 13.5 (float)
    
    result = True + 5                     # bool + int -> int
    print(f"True + 5 = {result} ({type(result)})")  # 6 (int)
    
    result = 5 + 2.5 + 3j                 # int + float + complex -> complex
    print(f"Mixed types: {result} ({type(result)})")
    
    # No automatic conversion between incompatible types
    # "10" + 5                             # TypeError: can only concatenate str to str
```

### Explicit Conversions
```python
def explicit_conversions():
    # Numeric conversions
    int_from_float = int(3.14)            # 3 (truncates toward zero)
    int_from_string = int("123")          # 123
    int_from_binary = int("1010", 2)      # 10 (binary conversion)
    
    float_from_int = float(42)            # 42.0
    float_from_string = float("3.14")     # 3.14
    
    complex_from_numbers = complex(2, 3)  # 2+3j
    
    # String conversions
    str_from_int = str(42)                # "42"
    str_from_float = str(3.14)            # "3.14"
    str_from_list = str([1, 2, 3])        # "[1, 2, 3]"
    
    # Boolean conversion (bool is subclass of int)
    bool_from_int = bool(0)               # False
    bool_from_nonzero = bool(42)          # True
    bool_from_empty = bool("")            # False
    bool_from_nonempty = bool("Hello")    # True
    
    # List conversions
    list_from_string = list("Hello")      # ['H', 'e', 'l', 'l', 'o']
    list_from_tuple = list((1, 2, 3))     # [1, 2, 3]
    list_from_range = list(range(5))      # [0, 1, 2, 3, 4]
    
    # Tuple conversions
    tuple_from_list = tuple([1, 2, 3])    # (1, 2, 3)
    tuple_from_string = tuple("Hello")    # ('H', 'e', 'l', 'l', 'o')
    
    # Set conversions
    set_from_list = set([1, 2, 2, 3])     # {1, 2, 3} (duplicates removed)
    set_from_string = set("Hello")        # {'H', 'e', 'l', 'o'}
    
    # Dictionary conversions
    dict_from_pairs = dict([('a', 1), ('b', 2)])  # {'a': 1, 'b': 2}
    dict_from_kwargs = dict(a=1, b=2)             # {'a': 1, 'b': 2}
    
    print(f"int(3.14): {int_from_float}")
    print(f"bool(0): {bool_from_int}")
    print(f"list('Hello'): {list_from_string}")
```

### Safe Type Conversion with Try-Except
```python
def safe_conversion(value, target_type, default=None):
    """Safely convert value to target_type, return default on failure"""
    try:
        return target_type(value)
    except (ValueError, TypeError):
        return default

# Example usage
print(safe_conversion("123", int, 0))        # 123
print(safe_conversion("abc", int, 0))        # 0
print(safe_conversion("3.14", float, 0.0))   # 3.14
```

## Variable Naming Conventions

```python
"""
Python Naming Conventions (PEP 8)
"""

# Modules: lowercase_with_underscores
# example_module.py

# Classes: CapWords (PascalCase)
class StudentManager:
    pass

# Constants: UPPER_CASE_WITH_UNDERSCORES
MAX_STUDENTS = 50
DATABASE_URL = "postgresql://localhost/mydb"

# Variables and functions: lowercase_with_underscores
student_name = "Alice"
student_age = 25

def calculate_average(scores):
    return sum(scores) / len(scores)

# Private variables (by convention): single leading underscore
_internal_counter = 0

# Name mangling (class-private): double leading underscore (avoids accidental override)
class MyClass:
    def __init__(self):
        self.__private_var = "name-mangled"  # Actually becomes _MyClass__private_var

# Special methods (magic methods): double leading and trailing underscores
def __init__(self):
    pass

# Avoid these
# x = 10                # Too generic
# a1, b2, c3 = 1,2,3    # Non-descriptive
# Temp = "value"        # Capitalized variable (reserved for classes)
# max-value = 10        # Hyphens not allowed

# Good practices
student_count = 10
is_valid = True
get_user_name = lambda: "user"  # But prefer def for readability
```

## Variable Unpacking and Advanced Assignment

### Tuple Unpacking
```python
def tuple_unpacking():
    # Basic unpacking
    point = (10, 20)
    x, y = point
    print(f"Point: ({x}, {y})")
    
    # Swapping variables (Pythonic)
    a, b = 5, 10
    a, b = b, a
    print(f"Swapped: a={a}, b={b}")
    
    # Extended unpacking with * (Python 3+)
    numbers = [1, 2, 3, 4, 5]
    first, *middle, last = numbers
    print(f"First: {first}, Middle: {middle}, Last: {last}")
    
    # Ignoring values with _
    _, second, *_, last = numbers
    print(f"Second: {second}, Last: {last}")
```

### Dictionary Unpacking
```python
def dictionary_unpacking():
    # Unpacking into function arguments
    def greet(name, age):
        return f"{name} is {age} years old"
    
    person = {"name": "Alice", "age": 25}
    print(greet(**person))                      # Alice is 25 years old
    
    # Merging dictionaries (Python 3.5+)
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged = {**dict1, **dict2}                # {'a':1, 'b':2, 'c':3, 'd':4}
    
    # Python 3.9+ merge operator
    merged2 = dict1 | dict2                    # Same result
```

### List and Set Unpacking
```python
def sequence_unpacking():
    # List unpacking
    numbers = [1, 2, 3, 4, 5]
    new_list = [0, *numbers, 6]               # [0, 1, 2, 3, 4, 5, 6]
    
    # Set unpacking
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    combined = {*set1, *set2}                 # {1, 2, 3, 4, 5}
    
    print(f"Extended list: {new_list}")
    print(f"Combined set: {combined}")
```

## Common Variable Pitfalls

### Mutable Default Arguments
```python
def mutable_default_pitfall():
    # WRONG: Mutable default arguments are shared across calls
    def add_item(item, items=[]):             # Default list is created once
        items.append(item)
        return items
    
    print(add_item(1))                        # [1]
    print(add_item(2))                        # [1, 2] (unexpected)
    
    # CORRECT: Use None and create new list each time
    def add_item_correct(item, items=None):
        if items is None:
            items = []
        items.append(item)
        return items
    
    print(add_item_correct(1))                # [1]
    print(add_item_correct(2))                # [2]
```

### Name Shadowing
```python
def name_shadowing():
    # Avoid shadowing built-in names
    # list = [1, 2, 3]                       # Don't do this!
    my_list = [1, 2, 3]                      # Better
    
    # Shadowing outer scope
    value = 10
    
    def inner():
        value = 20                           # Shadows outer value
        print(f"Inner: {value}")
    
    inner()
    print(f"Outer: {value}")                 # Still 10
    
    # Use nonlocal to modify outer
    def outer():
        x = 10
        def inner():
            nonlocal x
            x = 20
        inner()
        print(f"After nonlocal: {x}")        # 20
```

### Reference vs Value
```python
def reference_vs_value():
    # Immutable types (int, float, str, tuple) - copied by value
    a = 10
    b = a
    b = 20
    print(f"a: {a}, b: {b}")                 # a:10, b:20 (independent)
    
    # Mutable types (list, dict, set) - referenced
    list1 = [1, 2, 3]
    list2 = list1
    list2.append(4)
    print(f"list1: {list1}, list2: {list2}")  # Both [1,2,3,4] (shared)
    
    # Create copy instead of reference
    list3 = [1, 2, 3]
    list4 = list3.copy()                     # or list3[:] or list(list3)
    list4.append(4)
    print(f"list3: {list3}, list4: {list4}")  # list3 unchanged
```

### Circular References and Garbage Collection
```python
def circular_references():
    # Circular references can cause memory leaks in older Python
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    # Create circular reference
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node2.next = node1  # Circular
    
    # Python's garbage collector handles this (cyclic GC)
    # Explicitly break reference to avoid memory issues
    node1.next = None
    node2.next = None
```

### UnboundLocalError
```python
def unbound_local_error():
    # Trying to assign to variable before reading it in local scope
    value = 10
    
    def problematic():
        # value += 1                        # UnboundLocalError: local variable referenced before assignment
        # The 'value' here is considered local because of assignment
        pass
    
    def correct():
        global value                         # Declare as global
        value += 1
    
    # Or use nonlocal for nested functions
    def outer():
        x = 10
        def inner():
            nonlocal x
            x += 1
        inner()
        print(f"x after inner: {x}")
    
    correct()
    outer()
```

---
# Python Operators

## Overview
- Operators are symbols that perform operations on operands (variables and values).
- Python provides a comprehensive set of operators with many unique features.

## Arithmetic Operators
```python
def arithmetic_operators():
    a, b = 10, 3
    
    # Basic arithmetic
    sum_result = a + b               # Addition: 13
    difference = a - b               # Subtraction: 7
    product = a * b                  # Multiplication: 30
    quotient = a / b                 # Division: 3.3333333333333335 (always float)
    floor_division = a // b          # Floor division: 3 (integer division, floors)
    remainder = a % b                # Modulo: 1
    power = a ** b                   # Exponentiation: 1000
    
    # Unary operators
    x = 5
    unary_plus = +x                  # 5
    unary_minus = -x                 # -5
    
    # Python-specific operators
    print(f"10 + 3 = {sum_result}")
    print(f"10 / 3 = {quotient}")    # Always returns float
    print(f"10 // 3 = {floor_division}")
    print(f"10 ** 3 = {power}")
    
    # Special cases
    print(f"Negative floor: {-10 // 3}")    # -4 (floor, not truncate)
    print(f"Modulo with negatives: {-10 % 3}")  # 2 (results have same sign as divisor)
```

## Comparison (Relational) Operators
```python
def comparison_operators():
    a, b = 5, 10
    
    # Basic comparisons
    equal = (a == b)                 # Equal: False
    not_equal = (a != b)             # Not equal: True
    less_than = (a < b)              # Less than: True
    greater_than = (a > b)           # Greater than: False
    less_equal = (a <= b)            # Less or equal: True
    greater_equal = (a >= b)         # Greater or equal: False
    
    # Chained comparisons (Python unique feature)
    result = 0 < a < 10              # True (equivalent to 0 < a and a < 10)
    print(f"0 < 5 < 10: {result}")
    
    # Chained comparisons can be chained arbitrarily
    x, y, z = 5, 10, 15
    print(f"x < y < z: {x < y < z}")          # True
    print(f"x == y == z: {x == y == z}")      # False
    print(f"x < y > z: {x < y > z}")          # True
    
    # Identity comparison (is vs ==)
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1
    
    print(f"list1 == list2: {list1 == list2}")  # True (same values)
    print(f"list1 is list2: {list1 is list2}")  # False (different objects)
    print(f"list1 is list3: {list1 is list3}")  # True (same object)
    
    # None comparison
    x = None
    print(f"x is None: {x is None}")            # True
    # Never use == for None
```

## Logical Operators
```python
def logical_operators():
    # Logical operators in Python use words, not symbols
    a, b = True, False
    
    and_result = a and b               # False
    or_result = a or b                 # True
    not_result = not a                 # False
    
    # Short-circuit evaluation
    def expensive_operation():
        print("Expensive operation called")
        return True
    
    # Second operand not evaluated if first determines result
    result = False and expensive_operation()  # expensive_operation not called
    print(f"Short-circuit AND: {result}")
    
    result = True or expensive_operation()    # expensive_operation not called
    print(f"Short-circuit OR: {result}")
    
    # Logical operators return the last evaluated value
    print(f"5 and 10: {5 and 10}")            # 10
    print(f"0 and 10: {0 and 10}")            # 0
    print(f"5 or 10: {5 or 10}")              # 5
    print(f"0 or 10: {0 or 10}")              # 10
    
    # De Morgan's Laws
    x, y = True, False
    de_morgan1 = not (x and y)
    de_morgan2 = (not x) or (not y)
    print(f"De Morgan's Laws hold: {de_morgan1 == de_morgan2}")
```

## Membership Operators
```python
def membership_operators():
    # 'in' and 'not in' operators
    fruits = ['apple', 'banana', 'orange']
    
    print(f"'apple' in fruits: {'apple' in fruits}")        # True
    print(f"'grape' not in fruits: {'grape' not in fruits}") # True
    
    # Works with any sequence/collection
    text = "Hello, World!"
    print(f"'World' in text: {'World' in text}")            # True
    
    # Dictionary membership checks keys
    person = {'name': 'Alice', 'age': 25}
    print(f"'name' in person: {'name' in person}")          # True
    print(f"'Alice' in person: {'Alice' in person}")        # False (values not checked)
    print(f"'Alice' in person.values(): {'Alice' in person.values()}")  # True
    
    # Set membership (very fast)
    numbers = {1, 2, 3, 4, 5}
    print(f"3 in numbers: {3 in numbers}")                  # True
    
    # With custom classes (requires __contains__ method)
    class MyCollection:
        def __init__(self, items):
            self.items = items
        
        def __contains__(self, item):
            return item in self.items
    
    collection = MyCollection([1, 2, 3])
    print(f"2 in collection: {2 in collection}")            # True
```

## Identity Operators
```python
def identity_operators():
    # 'is' and 'is not' check object identity (same object in memory)
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    
    print(f"a is b: {a is b}")          # False (different objects)
    print(f"a is c: {a is c}")          # True (same object)
    print(f"a is not b: {a is not b}")  # True
    
    # Small integers are cached in Python
    x = 256
    y = 256
    print(f"256 is 256: {x is y}")      # True (cached)
    
    # Larger integers not cached
    x = 257
    y = 257
    print(f"257 is 257: {x is y}")      # False (usually)
    
    # Strings are interned in some cases
    s1 = "hello"
    s2 = "hello"
    print(f"'hello' is 'hello': {s1 is s2}")  # True (interning)
    
    # But not always for computed strings
    s3 = "hello" * 100
    s4 = "hello" * 100
    print(f"Computed strings: {s3 is s4}")    # False (usually)
    
    # Use == for value comparison, is for identity (e.g., None)
    result = None
    if result is None:                  # Correct
        print("Result is None")
```

## Bitwise Operators
```python
def bitwise_operators():
    a = 0b1010    # 10
    b = 0b1100    # 12
    
    # Bitwise operations
    bitwise_and = a & b          # 0b1000 (8)
    bitwise_or = a | b           # 0b1110 (14)
    bitwise_xor = a ^ b          # 0b0110 (6)
    bitwise_not = ~a             # -11 (two's complement)
    
    # Shift operations
    left_shift = a << 2          # 0b101000 (40)
    right_shift = a >> 1         # 0b0101 (5)
    
    print(f"a & b: {bin(bitwise_and)} ({bitwise_and})")
    print(f"a | b: {bin(bitwise_or)} ({bitwise_or})")
    print(f"a ^ b: {bin(bitwise_xor)} ({bitwise_xor})")
    print(f"~a: {bitwise_not}")
    print(f"a << 2: {left_shift}")
    print(f"a >> 1: {right_shift}")
    
    # Bitwise operators for flags
    READ = 0b001
    WRITE = 0b010
    EXECUTE = 0b100
    
    permissions = READ | WRITE          # 0b011
    print(f"Can read: {bool(permissions & READ)}")
    print(f"Can write: {bool(permissions & WRITE)}")
    print(f"Can execute: {bool(permissions & EXECUTE)}")
    
    # Toggle flags
    permissions ^= EXECUTE              # Add execute
    print(f"After toggle: {bin(permissions)}")
```

## Assignment Operators
```python
def assignment_operators():
    x = 10                            # Basic assignment
    
    # Compound assignment operators
    x += 5                            # x = x + 5 → 15
    x -= 3                            # x = x - 3 → 12
    x *= 2                            # x = x * 2 → 24
    x /= 4                            # x = x / 4 → 6.0
    x //= 2                           # x = x // 2 → 3.0
    x %= 2                            # x = x % 2 → 1.0
    x **= 3                           # x = x ** 3 → 1.0
    
    # Bitwise compound assignment
    y = 0b1010
    y &= 0b1100                       # y = y & 0b1100 → 0b1000 (8)
    y |= 0b0011                       # y = y | 0b0011 → 0b1011 (11)
    y ^= 0b0110                       # y = y ^ 0b0110 → 0b1101 (13)
    y <<= 1                           # y = y << 1 → 0b11010 (26)
    
    # Walrus operator (Python 3.8+) - assignment expression
    # Allows assignment and use in same expression
    numbers = [1, 2, 3, 4, 5]
    
    # Without walrus
    n = len(numbers)
    if n > 3:
        print(f"Length is {n}")
    
    # With walrus
    if (n := len(numbers)) > 3:
        print(f"Length is {n}")
    
    # In while loops
    while (line := input("Enter text (or 'quit'): ")) != 'quit':
        print(f"You entered: {line}")
    
    print(f"x: {x}, y: {y}")
```

## Ternary (Conditional) Operator
```python
def ternary_operator():
    # Python's ternary operator: value_if_true if condition else value_if_false
    age = 20
    status = "Adult" if age >= 18 else "Minor"
    print(f"Status: {status}")
    
    # Nested ternary (use sparingly)
    score = 85
    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
    print(f"Grade: {grade}")
    
    # With expressions
    x, y = 5, 10
    max_value = x if x > y else y
    print(f"Maximum: {max_value}")
    
    # With function calls
    def get_adult_message():
        return "Welcome, adult!"
    
    def get_minor_message():
        return "Hello, young one!"
    
    message = get_adult_message() if age >= 18 else get_minor_message()
    print(message)
    
    # Conditional assignment
    value = None
    result = value if value is not None else "default"
    print(f"Result: {result}")  # "default"
```

## Operator Precedence
```python
def operator_precedence():
    # Precedence determines which operation is performed first
    # Parentheses have highest precedence
    result1 = 5 + 3 * 2                     # 11 (multiplication first)
    result2 = (5 + 3) * 2                   # 16 (parentheses override)
    
    # Logical operators precedence: not > and > or
    result3 = True or False and False       # True (and evaluated first)
    result4 = (True or False) and False     # False
    
    # Comparison operators have higher precedence than logical
    result5 = 5 > 3 and 10 < 20             # True (comparisons first)
    
    # Chained comparisons are more efficient
    result6 = 1 < 2 < 3 < 4                # True (no intermediate booleans)
    
    print(f"5 + 3 * 2 = {result1}")
    print(f"(5 + 3) * 2 = {result2}")
    print(f"True or False and False = {result3}")
    print(f"1 < 2 < 3 < 4 = {result6}")
```

### Python Operator Precedence Table (Highest to Lowest)
```
1.  () [] {} . (parentheses, indexing, attribute access)
2.  ** (exponentiation)
3.  +x -x ~x (unary operators)
4.  * / % // (multiplication, division, modulo, floor division)
5.  + - (addition, subtraction)
6.  << >> (bitwise shifts)
7.  & (bitwise AND)
8.  ^ (bitwise XOR)
9.  | (bitwise OR)
10. in, not in, is, is not, <, <=, >, >=, !=, == (comparisons)
11. not (logical NOT)
12. and (logical AND)
13. or (logical OR)
14. if-else (ternary)
15. =, +=, -=, etc. (assignment)
16. lambda (lambda expression)
```

## Special Operators and Constructs

### Matrix Multiplication Operator (Python 3.5+)
```python
def matrix_operator():
    # @ operator for matrix multiplication
    import numpy as np
    
    # Using numpy (common use case)
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    
    result = a @ b                      # Matrix multiplication
    print(f"Matrix multiplication:\n{result}")
    
    # For custom classes, implement __matmul__ method
    class Matrix:
        def __init__(self, data):
            self.data = data
        
        def __matmul__(self, other):
            # Simplified matrix multiplication
            n = len(self.data)
            result = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        result[i][j] += self.data[i][k] * other.data[k][j]
            return Matrix(result)
        
        def __str__(self):
            return str(self.data)
    
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    print(f"Custom matrix multiplication: {m1 @ m2}")
```

### Context Manager (`with` operator)
```python
def context_manager():
    # with statement for resource management
    # File handling
    with open('example.txt', 'w') as file:
        file.write('Hello, World!')
        # File automatically closed when block exits
    
    # Multiple context managers
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        outfile.write(infile.read())
    
    # Custom context manager
    class ManagedResource:
        def __enter__(self):
            print("Acquiring resource")
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print("Releasing resource")
            return False  # Don't suppress exceptions
    
    with ManagedResource() as resource:
        print("Using resource")
        # Resource automatically released after block
    
    # Using contextlib for simpler context managers
    from contextlib import contextmanager
    
    @contextmanager
    def managed_resource():
        print("Acquiring")
        try:
            yield
        finally:
            print("Releasing")
    
    with managed_resource():
        print("Using")
```

## Practical Example: Combining Operators
```python
def combined_operators():
    # Calculate compound interest
    principal = 1000.0
    rate = 0.05
    years = 3
    
    # Compound interest calculation
    amount = principal * (1 + rate) ** years
    print(f"Amount after {years} years: ${amount:.2f}")
    
    # Complex expression
    a, b, c = 5, 10, 15
    result = (a + b) * c / 2 - 10
    print(f"(5+10)*15/2-10 = {result}")
    
    # Find maximum using ternary and comparisons
    numbers = [5, 10, 15, 8, 12]
    max_value = numbers[0]
    for n in numbers:
        max_value = n if n > max_value else max_value
    print(f"Maximum: {max_value}")
    
    # Bit flags example
    READ = 0b001
    WRITE = 0b010
    EXECUTE = 0b100
    
    permissions = READ | WRITE
    print(f"Permissions: {bin(permissions)}")
    print(f"Can read: {bool(permissions & READ)}")
    print(f"Can write: {bool(permissions & WRITE)}")
    print(f"Can execute: {bool(permissions & EXECUTE)}")
    
    # Add execute permission
    permissions |= EXECUTE
    print(f"After adding execute: {bin(permissions)}")
    
    # Remove write permission
    permissions &= ~WRITE
    print(f"After removing write: {bin(permissions)}")
    
    # Check if permissions are a superset
    required = READ | EXECUTE
    has_required = (permissions & required) == required
    print(f"Has required permissions (read+execute): {has_required}")
```

## Best Practices Summary

1. **Use meaningful variable names** that describe their purpose (e.g., `student_age` not `sa`)
2. **Follow PEP 8 naming conventions**:
   - Variables/functions: `snake_case`
   - Classes: `PascalCase`
   - Constants: `UPPER_SNAKE_CASE`
3. **Use `is` for None comparison**: `if value is None:` not `if value == None:`
4. **Use `in` for membership tests**: `if item in list:` not manual loops
5. **Take advantage of chained comparisons**: `0 < x < 10` instead of `0 < x and x < 10`
6. **Use the walrus operator (:=)** judiciously for cleaner code (Python 3.8+)
7. **Be aware of mutable default arguments**: Use `None` and create new objects inside
8. **Use `with` for resource management**: Files, locks, database connections
9. **Use `enumerate()` for indexed loops**: `for i, item in enumerate(items):`
10. **Use `zip()` for parallel iteration**: `for name, score in zip(names, scores):`
11. **Use list/dict/set comprehensions**: Cleaner than manual loops
12. **Avoid unnecessary type conversions**: Python is dynamically typed
13. **Use `__slots__` for memory optimization in classes with many instances
14. **Prefer tuple unpacking for swapping**: `a, b = b, a`
15. **Use `f-strings` for formatting** (Python 3.6+): `f"{name}: {age}"`

## Conclusion

Understanding variables, keywords, and operators is fundamental to Python programming. Python's dynamic typing and emphasis on readability make it unique among programming languages. Key takeaways include:

- **Dynamic typing**: Variables can hold any type and change types freely
- **Rich data types**: Lists, tuples, sets, dictionaries, and more built-in
- **Comprehensive operators**: Including unique features like chained comparisons and the walrus operator
- **Clear naming conventions**: PEP 8 provides consistent guidelines
- **Reference semantics**: Understanding mutable vs immutable types is crucial
- **Powerful built-in functions**: `len()`, `type()`, `isinstance()`, etc.

Python's philosophy of "explicit is better than implicit" and "readability counts" is reflected in its variable handling and operator design. By following best practices and understanding the language's unique features, you can write clean, efficient, and maintainable Python code.