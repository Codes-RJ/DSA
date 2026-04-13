# 01_Variables_Keywords_and_Operators.md

## C++ Variables, Keywords and Operators

### Overview

Variables in C++ are named storage locations that hold data values. Keywords are reserved words that have special meaning to the C++ compiler and cannot be used as identifiers. Operators are symbols that perform operations on variables and values. Understanding these three fundamental concepts is essential for writing any C++ program.

---

## Part 1: Variables

### What are Variables?

A variable is a named memory location that stores a value. The value stored in a variable can change during program execution (hence the name "variable").

### Rules for Naming Variables

Before declaring variables, you must follow these naming rules:

| Rule | Description | Valid Example | Invalid Example |
|------|-------------|---------------|-----------------|
| 1. | Can contain letters, digits, and underscore | `student_age` | `student-age` |
| 2. | Must start with a letter or underscore | `_counter` | `1st_value` |
| 3. | Cannot start with a digit | `value1` | `1value` |
| 4. | Cannot use C++ keywords | `int_value` | `int` |
| 5. | Case-sensitive | `age` and `Age` are different | - |
| 6. | No spaces allowed | `my_var` | `my var` |

### Variable Declaration Syntax

The basic syntax for declaring a variable is:

```cpp
data_type variable_name;
data_type variable_name = initial_value;
```

### Basic Data Types in C++

C++ provides several built-in data types:

| Data Type | Keyword | Size (typical) | Range | Example |
|-----------|---------|----------------|-------|---------|
| Integer | `int` | 4 bytes | -2,147,483,648 to 2,147,483,647 | `int age = 25;` |
| Short Integer | `short` | 2 bytes | -32,768 to 32,767 | `short count = 100;` |
| Long Integer | `long` | 4 or 8 bytes | Depends on system | `long distance = 100000L;` |
| Long Long | `long long` | 8 bytes | -9 quintillion to 9 quintillion | `long long big = 10000000000LL;` |
| Unsigned Int | `unsigned int` | 4 bytes | 0 to 4,294,967,295 | `unsigned int positive = 4000000000U;` |
| Floating Point | `float` | 4 bytes | ±1.2e-38 to ±3.4e38 | `float pi = 3.14f;` |
| Double Float | `double` | 8 bytes | ±2.2e-308 to ±1.8e308 | `double precise = 3.1415926535;` |
| Character | `char` | 1 byte | -128 to 127 or 0 to 255 | `char grade = 'A';` |
| Boolean | `bool` | 1 byte | true or false | `bool isValid = true;` |
| Void | `void` | - | No value | `void functionName();` |

### Variable Declaration Examples

```cpp
#include <iostream>
#include <string>

int main() {
    // Declaration without initialization (value is garbage/unpredictable)
    int age;
    double salary;
    char grade;
    
    // Declaration with initialization
    int student_count = 30;
    double pi = 3.14159;
    char initial = 'J';
    bool is_active = true;
    
    // Multiple variables of same type
    int x = 5, y = 10, z = 15;
    
    // String variables (requires <string> header)
    std::string name = "John Doe";
    
    return 0;
}
```

### Variable Initialization Methods

C++ provides multiple ways to initialize variables:

```cpp
#include <iostream>

int main() {
    // Method 1: Copy initialization (traditional)
    int a = 10;
    
    // Method 2: Direct initialization
    int b(20);
    
    // Method 3: Uniform initialization (braced initialization) - Preferred in modern C++
    int c{30};
    
    // Method 4: Zero initialization
    int d{};      // d = 0
    double e{};   // e = 0.0
    bool f{};     // f = false
    
    // Method 5: Auto type deduction (C++11)
    auto g = 42;        // g is int
    auto h = 3.14;      // h is double
    auto i = 'A';       // i is char
    
    return 0;
}
```

### Variable Scope and Lifetime

Variables exist only within the scope where they are declared:

| Scope Type | Description | Lifetime |
|------------|-------------|----------|
| Local scope | Declared inside a function or block | Exists until block ends |
| Global scope | Declared outside all functions | Exists throughout program |
| Static local | Declared with `static` keyword inside function | Exists throughout program |
| Namespace scope | Declared inside a namespace | Exists throughout program |

```cpp
#include <iostream>

int global_var = 100;  // Global variable - accessible anywhere

void demonstrateScope() {
    int local_var = 50;  // Local variable - only inside this function
    
    if (local_var > 0) {
        int block_var = 25;  // Block variable - only inside this if block
        std::cout << block_var << std::endl;
    }
    // block_var is NOT accessible here
    
    static int static_var = 0;  // Static local - retains value between calls
    static_var++;
    std::cout << "Static: " << static_var << std::endl;
}
```

### Constants in C++

Constants are variables whose values cannot be changed after initialization:

```cpp
#include <iostream>

// Method 1: const keyword (runtime constant)
const int MAX_STUDENTS = 100;
const double PI = 3.14159;

// Method 2: constexpr keyword (compile-time constant) - C++11
constexpr int BUFFER_SIZE = 1024;
constexpr double GRAVITY = 9.81;

int main() {
    const int local_max = 50;
    // local_max = 60;  // Error: cannot modify constant
    
    std::cout << "MAX_STUDENTS: " << MAX_STUDENTS << std::endl;
    std::cout << "PI: " << PI << std::endl;
    std::cout << "BUFFER_SIZE: " << BUFFER_SIZE << std::endl;
    
    return 0;
}
```

---

## Part 2: C++ Keywords

### What are Keywords?

Keywords are reserved words that have special meaning to the C++ compiler. They cannot be used as variable names, function names, or any other identifiers.

### Complete List of C++ Keywords (C++20)

C++ has 97 reserved keywords. Here they are organized by category:

#### Fundamental Type Keywords

| Keyword | Purpose |
|---------|---------|
| `int` | Integer type |
| `float` | Single-precision floating point |
| `double` | Double-precision floating point |
| `char` | Character type |
| `bool` | Boolean type (true/false) |
| `void` | No type / empty |
| `wchar_t` | Wide character type |
| `char16_t` | UTF-16 character (C++11) |
| `char32_t` | UTF-32 character (C++11) |

#### Type Modifiers

| Keyword | Purpose |
|---------|---------|
| `signed` | Signed integer (explicit) |
| `unsigned` | Unsigned integer (non-negative only) |
| `short` | Short integer (typically 2 bytes) |
| `long` | Long integer (typically 4 or 8 bytes) |
| `long long` | Long long integer (typically 8 bytes, C++11) |

#### Storage Class Specifiers

| Keyword | Purpose |
|---------|---------|
| `auto` | Automatic type deduction (C++11) |
| `register` | Register storage (deprecated) |
| `static` | Static storage duration |
| `extern` | External linkage |
| `mutable` | Allows modification of const class members |
| `thread_local` | Thread-local storage (C++11) |

#### Type Qualifiers

| Keyword | Purpose |
|---------|---------|
| `const` | Value cannot be modified |
| `volatile` | Value may change unexpectedly (hardware, signals) |

#### Control Flow Keywords

| Keyword | Purpose |
|---------|---------|
| `if` | Conditional statement |
| `else` | Alternative conditional branch |
| `switch` | Multi-way branch |
| `case` | Label in switch statement |
| `default` | Default label in switch |
| `for` | For loop |
| `while` | While loop |
| `do` | Do-while loop |
| `break` | Exit loop or switch |
| `continue` | Skip to next iteration |
| `goto` | Unconditional jump (avoid when possible) |
| `return` | Return from function |

#### Object-Oriented Keywords

| Keyword | Purpose |
|---------|---------|
| `class` | Class definition |
| `struct` | Structure definition |
| `union` | Union definition (shared memory) |
| `public` | Public access specifier |
| `protected` | Protected access specifier |
| `private` | Private access specifier |
| `virtual` | Virtual function (polymorphism) |
| `friend` | Friend function/class (access to private members) |
| `this` | Pointer to current object |
| `operator` | Operator overloading |
| `new` | Dynamic memory allocation |
| `delete` | Dynamic memory deallocation |

#### Template Keywords

| Keyword | Purpose |
|---------|---------|
| `template` | Template declaration |
| `typename` | Type parameter in template |
| `concept` | Concept definition (C++20) |
| `requires` | Requires clause (C++20) |

#### Exception Handling Keywords

| Keyword | Purpose |
|---------|---------|
| `try` | Try block (exception monitoring) |
| `catch` | Exception handler |
| `throw` | Throw exception |
| `noexcept` | Exception specification (C++11) |

#### Namespace Keywords

| Keyword | Purpose |
|---------|---------|
| `namespace` | Namespace definition |
| `using` | Using declaration/directive |

#### Modern C++ Keywords (C++11 and later)

| Keyword | Purpose | Version |
|---------|---------|---------|
| `nullptr` | Null pointer literal | C++11 |
| `constexpr` | Compile-time constant expression | C++11 |
| `decltype` | Type inference from expression | C++11 |
| `override` | Override specifier for virtual functions | C++11 |
| `final` | Final specifier (no further override) | C++11 |
| `explicit` | Explicit constructor (no implicit conversion) | C++11 |
| `alignas` | Alignment specifier | C++11 |
| `alignof` | Alignment query operator | C++11 |
| `static_assert` | Compile-time assertion | C++11 |

### Important Rules for Keywords

1. **Cannot be used as identifiers** - You cannot name a variable `int` or `class`
2. **Case-sensitive** - `Int` is not a keyword, but `int` is
3. **Some keywords are context-sensitive** - `final` and `override` are keywords only in certain contexts
4. **Always lowercase** - All C++ keywords are in lowercase

```cpp
// These are INVALID:
int int = 5;        // Error: 'int' is a keyword
float class = 3.14; // Error: 'class' is a keyword

// These are VALID:
int myInt = 5;      // 'myInt' is not a keyword
float myClass = 3.14; // 'myClass' is not a keyword
int Int = 10;       // 'Int' is not a keyword (case-sensitive)
```

---

## Part 3: C++ Operators

### What are Operators?

Operators are symbols that tell the compiler to perform specific mathematical, relational, or logical operations on operands (variables and values).

### Types of Operators in C++

| Category | Operators | Purpose |
|----------|-----------|---------|
| Arithmetic | `+ - * / %` | Basic math operations |
| Relational | `== != < > <= >=` | Compare values |
| Logical | `&& || !` | Boolean logic |
| Bitwise | `& | ^ ~ << >>` | Bit-level operations |
| Assignment | `= += -= *= /= %=` | Assign values |
| Increment/Decrement | `++ --` | Add or subtract 1 |
| Ternary | `? :` | Conditional evaluation |
| Special | `sizeof , . -> & *` | Various special operations |

---

### 1. Arithmetic Operators

Arithmetic operators perform basic mathematical operations.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `a + b` | Sum of a and b |
| `-` | Subtraction | `a - b` | Difference of a and b |
| `*` | Multiplication | `a * b` | Product of a and b |
| `/` | Division | `a / b` | Quotient of a divided by b |
| `%` | Modulo (remainder) | `a % b` | Remainder after division |

**Rules for Arithmetic Operators:**
- Integer division truncates toward zero (discards fractional part)
- Modulo operator `%` works only with integers
- Division by zero causes runtime error

```cpp
#include <iostream>

int main() {
    int a = 10, b = 3;
    
    // Basic arithmetic
    int sum = a + b;          // 13
    int difference = a - b;   // 7
    int product = a * b;      // 30
    int quotient = a / b;     // 3 (integer division, not 3.333)
    int remainder = a % b;    // 1
    
    // Mixed type arithmetic
    double result = 10 / 3;           // 3.0 (integer division, then converted to double)
    double correct = 10.0 / 3;        // 3.3333 (floating point division)
    
    // Unary arithmetic
    int x = 5;
    int y = +x;               // 5 (unary plus)
    int z = -x;               // -5 (unary minus)
    
    std::cout << "10 + 3 = " << sum << std::endl;
    std::cout << "10 / 3 = " << quotient << std::endl;
    std::cout << "10 % 3 = " << remainder << std::endl;
    
    return 0;
}
```

---

### 2. Relational Operators

Relational operators compare two values and return a boolean result (`true` or `false`).

| Operator | Name | Example | Returns true if |
|----------|------|---------|-----------------|
| `==` | Equal to | `a == b` | a equals b |
| `!=` | Not equal to | `a != b` | a does not equal b |
| `<` | Less than | `a < b` | a is less than b |
| `>` | Greater than | `a > b` | a is greater than b |
| `<=` | Less than or equal | `a <= b` | a is less than or equal to b |
| `>=` | Greater than or equal | `a >= b` | a is greater than or equal to b |

```cpp
#include <iostream>

int main() {
    int a = 5, b = 10;
    
    // Store comparison results in boolean variables
    bool isEqual = (a == b);      // false
    bool isNotEqual = (a != b);   // true
    bool isLess = (a < b);        // true
    bool isGreater = (a > b);     // false
    bool isLessEqual = (a <= b);  // true
    bool isGreaterEqual = (a >= b); // false
    
    // Print with boolalpha to show "true"/"false" instead of 1/0
    std::cout << std::boolalpha;
    std::cout << "5 == 10: " << isEqual << std::endl;
    std::cout << "5 != 10: " << isNotEqual << std::endl;
    std::cout << "5 < 10: " << isLess << std::endl;
    
    // Using in conditions
    if (a < b) {
        std::cout << "a is less than b" << std::endl;
    }
    
    return 0;
}
```

---

### 3. Logical Operators

Logical operators combine boolean values and return a boolean result.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `&&` | Logical AND | `a && b` | true if both a AND b are true |
| `||` | Logical OR | `a || b` | true if either a OR b is true |
| `!` | Logical NOT | `!a` | true if a is false (inverts) |

**Truth Table:**

| a | b | a && b | a \|\| b | !a |
|---|---|--------|---------|----|
| true | true | true | true | false |
| true | false | false | true | false |
| false | true | false | true | true |
| false | false | false | false | true |

**Short-Circuit Evaluation:**
- In `a && b`, if `a` is false, `b` is NOT evaluated
- In `a || b`, if `a` is true, `b` is NOT evaluated

```cpp
#include <iostream>

int main() {
    bool x = true, y = false;
    
    bool andResult = x && y;   // false
    bool orResult = x || y;    // true
    bool notResult = !x;       // false
    
    std::cout << std::boolalpha;
    std::cout << "true && false = " << andResult << std::endl;
    std::cout << "true || false = " << orResult << std::endl;
    std::cout << "!true = " << notResult << std::endl;
    
    // Short-circuit demonstration
    int a = 5;
    bool result = (a > 0) && (++a > 5);  // second part executed because first is true
    std::cout << "a after AND with short-circuit: " << a << std::endl;  // a becomes 6
    
    a = 5;
    result = (a < 0) && (++a > 5);  // second part NOT executed because first is false
    std::cout << "a after AND with short-circuit: " << a << std::endl;  // a remains 5
    
    return 0;
}
```

---

### 4. Bitwise Operators

Bitwise operators perform operations at the individual bit level.

| Operator | Name | Example | Description |
|----------|------|---------|-------------|
| `&` | Bitwise AND | `a & b` | 1 if both bits are 1 |
| `\|` | Bitwise OR | `a \| b` | 1 if at least one bit is 1 |
| `^` | Bitwise XOR | `a ^ b` | 1 if bits are different |
| `~` | Bitwise NOT | `~a` | Flips all bits (0→1, 1→0) |
| `<<` | Left shift | `a << n` | Shifts bits left by n positions |
| `>>` | Right shift | `a >> n` | Shifts bits right by n positions |

**Bitwise Operation Examples:**

```
a = 10 (binary: 1010)
b = 6  (binary: 0110)

a & b = 0010 (2)
a | b = 1110 (14)
a ^ b = 1100 (12)
~a    = 1111...0101 (depends on bit width)
a << 1 = 10100 (20)
a >> 1 = 0101 (5)
```

```cpp
#include <iostream>
#include <bitset>

int main() {
    unsigned int a = 10;  // Binary: 1010
    unsigned int b = 6;   // Binary: 0110
    
    unsigned int bitwise_and = a & b;   // 2 (0010)
    unsigned int bitwise_or = a | b;    // 14 (1110)
    unsigned int bitwise_xor = a ^ b;   // 12 (1100)
    unsigned int bitwise_not = ~a;      // Flips all bits
    unsigned int left_shift = a << 2;   // 40 (101000)
    unsigned int right_shift = a >> 1;  // 5 (0101)
    
    // Display binary representation
    std::cout << "a = " << std::bitset<4>(a) << " (" << a << ")" << std::endl;
    std::cout << "b = " << std::bitset<4>(b) << " (" << b << ")" << std::endl;
    std::cout << "a & b = " << std::bitset<4>(bitwise_and) << " (" << bitwise_and << ")" << std::endl;
    std::cout << "a | b = " << std::bitset<4>(bitwise_or) << " (" << bitwise_or << ")" << std::endl;
    std::cout << "a ^ b = " << std::bitset<4>(bitwise_xor) << " (" << bitwise_xor << ")" << std::endl;
    std::cout << "a << 2 = " << left_shift << std::endl;
    std::cout << "a >> 1 = " << right_shift << std::endl;
    
    return 0;
}
```

---

### 5. Assignment Operators

Assignment operators assign values to variables.

| Operator | Name | Example | Equivalent to |
|----------|------|---------|---------------|
| `=` | Simple assignment | `x = y` | `x = y` |
| `+=` | Add and assign | `x += y` | `x = x + y` |
| `-=` | Subtract and assign | `x -= y` | `x = x - y` |
| `*=` | Multiply and assign | `x *= y` | `x = x * y` |
| `/=` | Divide and assign | `x /= y` | `x = x / y` |
| `%=` | Modulo and assign | `x %= y` | `x = x % y` |
| `&=` | Bitwise AND and assign | `x &= y` | `x = x & y` |
| `\|=` | Bitwise OR and assign | `x \|= y` | `x = x \| y` |
| `^=` | Bitwise XOR and assign | `x ^= y` | `x = x ^ y` |
| `<<=` | Left shift and assign | `x <<= n` | `x = x << n` |
| `>>=` | Right shift and assign | `x >>= n` | `x = x >> n` |

```cpp
#include <iostream>

int main() {
    int x = 10;
    
    // Basic assignment
    x = 20;        // x becomes 20
    
    // Compound assignments
    x += 5;        // x = 20 + 5 = 25
    x -= 3;        // x = 25 - 3 = 22
    x *= 2;        // x = 22 * 2 = 44
    x /= 4;        // x = 44 / 4 = 11
    x %= 3;        // x = 11 % 3 = 2
    
    // Multiple assignments (right-associative)
    int a, b, c;
    a = b = c = 10;  // All three become 10
    
    std::cout << "x = " << x << std::endl;
    std::cout << "a = " << a << ", b = " << b << ", c = " << c << std::endl;
    
    return 0;
}
```

---

### 6. Increment and Decrement Operators

These operators add or subtract 1 from a variable.

| Operator | Name | Example | Effect |
|----------|------|---------|--------|
| `++` (prefix) | Pre-increment | `++x` | Increments x, then returns new value |
| `++` (postfix) | Post-increment | `x++` | Returns old value, then increments x |
| `--` (prefix) | Pre-decrement | `--x` | Decrements x, then returns new value |
| `--` (postfix) | Post-decrement | `x--` | Returns old value, then decrements x |

**Important Rule:** Use prefix increment (++x) when the old value is not needed. It's more efficient because it doesn't need to store the old value.

```cpp
#include <iostream>

int main() {
    int x = 5;
    
    // Post-increment
    int old = x++;  // old = 5, x becomes 6
    std::cout << "x++: old=" << old << ", new x=" << x << std::endl;
    
    x = 5;
    
    // Pre-increment
    int newVal = ++x;  // x becomes 6, newVal = 6
    std::cout << "++x: new=" << newVal << ", x=" << x << std::endl;
    
    // In loops (pre-increment is preferred)
    for (int i = 0; i < 5; ++i) {  // ++i, not i++
        std::cout << i << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

---

### 7. Ternary Operator (Conditional Operator)

The ternary operator `?:` is a shorthand for `if-else` statements.

**Syntax:**
```cpp
condition ? expression1 : expression2
```

**Rule:** If `condition` is true, `expression1` is evaluated; otherwise, `expression2` is evaluated.

```cpp
#include <iostream>
#include <string>

int main() {
    int a = 5, b = 10;
    
    // Find maximum
    int max = (a > b) ? a : b;  // max = 10
    
    // Find minimum
    int min = (a < b) ? a : b;  // min = 5
    
    // Chained ternary (use sparingly - can be hard to read)
    int score = 85;
    std::string grade = (score >= 90) ? "A" :
                        (score >= 80) ? "B" :
                        (score >= 70) ? "C" :
                        (score >= 60) ? "D" : "F";
    
    std::cout << "Maximum: " << max << std::endl;
    std::cout << "Minimum: " << min << std::endl;
    std::cout << "Grade for " << score << ": " << grade << std::endl;
    
    return 0;
}
```

---

### 8. Operator Precedence and Associativity

Operator precedence determines the order of evaluation when multiple operators are used in an expression. Operators with higher precedence are evaluated first.

**Precedence Table (highest to lowest):**

| Precedence | Operators | Associativity |
|------------|-----------|---------------|
| 1 | `::` | Left to right |
| 2 | `() [] . -> ++ --` (postfix) | Left to right |
| 3 | `++ --` (prefix) `+ - ! ~ & *` (unary) `(type)` `sizeof` | Right to left |
| 4 | `.* ->*` | Left to right |
| 5 | `* / %` | Left to right |
| 6 | `+ -` | Left to right |
| 7 | `<< >>` | Left to right |
| 8 | `< <= > >=` | Left to right |
| 9 | `== !=` | Left to right |
| 10 | `&` | Left to right |
| 11 | `^` | Left to right |
| 12 | `\|` | Left to right |
| 13 | `&&` | Left to right |
| 14 | `\|\|` | Left to right |
| 15 | `?:` | Right to left |
| 16 | `= += -= *= /= %=` etc. | Right to left |
| 17 | `,` | Left to right |

```cpp
#include <iostream>

int main() {
    // Multiplication has higher precedence than addition
    int result1 = 5 + 3 * 2;     // 11, NOT 16 (3*2 = 6, then 5+6 = 11)
    
    // Use parentheses to change order
    int result2 = (5 + 3) * 2;   // 16
    
    // Precedence with relational and logical operators
    bool result3 = 5 > 3 && 2 < 4;   // (5>3) && (2<4) → true && true → true
    
    // Associativity example
    int a = 10, b = 5, c = 2;
    int result4 = a - b - c;     // (10 - 5) - 2 = 3 (left associative)
    
    std::cout << "5 + 3 * 2 = " << result1 << std::endl;
    std::cout << "(5 + 3) * 2 = " << result2 << std::endl;
    std::cout << "5 > 3 && 2 < 4 = " << std::boolalpha << result3 << std::endl;
    
    return 0;
}
```

---

### 9. Special Operators

| Operator | Name | Purpose |
|----------|------|---------|
| `sizeof` | Size of | Returns size in bytes of a type or variable |
| `&` | Address-of | Returns memory address of a variable |
| `*` | Dereference | Accesses value at a memory address |
| `.` | Member access | Accesses member of a structure/class |
| `->` | Pointer member access | Accesses member through a pointer |
| `,` | Comma | Evaluates multiple expressions, returns last |
| `(type)` | Cast | Converts value to specified type |

```cpp
#include <iostream>
#include <typeinfo>

int main() {
    // sizeof operator
    int x = 42;
    std::cout << "Size of int: " << sizeof(int) << " bytes" << std::endl;
    std::cout << "Size of x: " << sizeof(x) << " bytes" << std::endl;
    
    // Address-of and dereference operators
    int value = 100;
    int* ptr = &value;      // ptr holds address of value
    int dereferenced = *ptr; // dereferenced = 100
    
    // Comma operator
    int a, b, c;
    a = (b = 5, c = 10, b + c);  // a = 15
    
    // Type cast
    double pi = 3.14159;
    int truncated = (int)pi;      // 3 (C-style cast)
    int modernCast = static_cast<int>(pi);  // 3 (C++ style cast)
    
    std::cout << "Address of value: " << &value << std::endl;
    std::cout << "Value via pointer: " << *ptr << std::endl;
    std::cout << "Comma operator result: " << a << std::endl;
    
    return 0;
}
```

---

## Best Practices Summary

### Variables
1. **Always initialize variables** before use to avoid undefined behavior
2. **Use meaningful names** that describe the variable's purpose
3. **Prefer `const` or `constexpr`** for values that don't change
4. **Use `auto`** when the type is obvious from the right-hand side
5. **Minimize global variables** - prefer local or class members
6. **Use appropriate scope** - declare variables in the smallest scope possible
7. **Follow naming conventions** consistently (snake_case for variables, UPPER_CASE for constants)

### Keywords
1. **Never use keywords as identifiers** - the compiler will reject your code
2. **Remember keywords are case-sensitive** - `Int` is allowed but confusing
3. **Stay updated** - new keywords are added in each C++ version

### Operators
1. **Use parentheses for clarity** when precedence might be ambiguous
2. **Prefer prefix increment `++i`** over postfix `i++` when the old value isn't needed
3. **Use compound operators** (`+=`, `-=`) for cleaner code
4. **Be careful with integer division** - it truncates toward zero
5. **Understand short-circuit evaluation** in logical operators
6. **Use bitwise operators only when working with bits or flags**
7. **Avoid using the comma operator** - it often confuses readers

---

## Common Mistakes to Avoid

| Mistake | Problem | Solution |
|---------|---------|----------|
| `int x;` without initialization | Contains garbage value | `int x = 0;` or `int x{};` |
| `if (x = 5)` instead of `if (x == 5)` | Assignment instead of comparison | Use `==` for comparison |
| `10 / 3` expecting 3.33 | Integer division truncates | Use `10.0 / 3` for floating result |
| `&&` and `||` short-circuit confusion | Second expression may not execute | Be aware of the behavior |
| Using keywords as variable names | Compilation error | Choose different name |
| Forgetting `break` in `switch` | Falls through to next case | Add `break` or comment fall-through |
| `x++` vs `++x` confusion | Wrong value used | Understand the difference |

---

## Conclusion

Variables, keywords, and operators form the foundation of C++ programming. Variables store data, keywords provide the language structure, and operators perform actions on data. Understanding these three concepts thoroughly will allow you to write clear, efficient, and correct C++ code.

Modern C++ provides many features for safer and more expressive variable handling, including uniform initialization, type deduction, and constexpr. By following best practices and using modern C++ features, you can write more maintainable and error-free code.

---

## Next Step

- Go to [02_Conditional_Statements.md](02_Conditional_Statements.md) to continue with Conditional Statements.

---

Is this the style and depth you want for all tutorial files?