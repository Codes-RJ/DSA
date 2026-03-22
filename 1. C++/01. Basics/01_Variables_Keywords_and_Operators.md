# C++ Variables and Keywords

## Overview
```
- Variables in C++ are named storage locations that hold data values.
- Keywords are reserved words that have special meaning to the C++ compiler and cannot be used as identifiers. 
- Understanding variables and keywords is fundamental to C++ programming.
```
## C++ Keywords

C++ has 97 reserved keywords (as of C++20). These are divided into several categories:

### Fundamental Type Keywords
```cpp
// Basic types
int              // Integer type
float            // Single-precision floating point
double           // Double-precision floating point
char             // Character type
bool             // Boolean type (true/false)
void             // No type
wchar_t          // Wide character type
char16_t         // UTF-16 character
char32_t         // UTF-32 character

// Type modifiers
signed           // Signed integer
unsigned         // Unsigned integer
short            // Short integer
long             // Long integer
long long        // Long long integer (C++11)
```

### Storage Class Specifiers
```cpp
auto             // Automatic storage duration (C++11: type inference)
register         // Register storage (deprecated)
static           // Static storage duration
extern           // External linkage
mutable          // Allows modification of const class members
thread_local     // Thread-local storage (C++11)
```

### Type Qualifiers
```cpp
const            // Constant value
volatile         // Tells compiler not to optimize
```

### Control Flow Keywords
```cpp
// Selection
if               // Conditional statement
else             // Alternative conditional
switch           // Multi-way branch
case             // Switch case label
default          // Default switch case

// Loops
for              // For loop
while            // While loop
do               // Do-while loop

// Jump statements
break            // Exit loop or switch
continue         // Skip to next iteration
goto             // Unconditional jump
return           // Return from function
```

### Object-Oriented Keywords
```cpp
class            // Class definition
struct           // Structure definition
union            // Union definition
public           // Public access specifier
protected        // Protected access specifier
private          // Private access specifier
virtual          // Virtual function
friend           // Friend function/class
this             // Pointer to current object
operator         // Operator overloading
new              // Dynamic allocation
delete           // Dynamic deallocation
```

### Template and Generic Programming
```cpp
template         // Template declaration
typename         // Type parameter
concept          // Concept definition (C++20)
requires         // Requires clause (C++20)
```

### Exception Handling
```cpp
try              // Try block
catch            // Exception handler
throw            // Throw exception
noexcept         // Exception specification (C++11)
```

### Namespace Keywords
```cpp
namespace        // Namespace definition
using            // Using declaration/directive
```

### Modern C++ Keywords (C++11 and later)
```cpp
nullptr          // Null pointer literal
constexpr        // Constant expression
decltype         // Type inference
override         // Override specifier
final            // Final specifier
explicit         // Explicit constructor
decltype         // Declare type
alignas          // Alignment specifier
alignof          // Alignment query
static_assert    // Compile-time assertion
```

## Variable Declaration and Initialization

### Basic Variable Declaration
```cpp
#include <iostream>
#include <string>

int main() {
    // Declaration without initialization
    int age;
    double salary;
    char grade;
    bool isStudent;
    std::string name;
    
    // Declaration with initialization
    int score = 100;
    double pi = 3.14159;
    char initial = 'A';
    bool isValid = true;
    std::string greeting = "Hello, World!";
    
    return 0;
}
```

### Modern Initialization Methods (C++11)
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    // Copy initialization
    int x = 5;
    
    // Direct initialization
    int y(10);
    
    // Uniform initialization (preferred)
    int z{15};
    
    // Auto type inference     
    auto number = 42;                    // int
    auto decimal = 3.14;                 // double
    auto letter = 'A';                   // char
    auto flag = true;                    // bool
    auto text = "Hello";                 // const char*
    auto str = std::string("Hi");        // std::string
    
    // Vector initialization
    std::vector<int> numbers{1, 2, 3, 4, 5};
    return 0;
}
```

## Variable Types in Detail

### Integer Types
```cpp
#include <iostream>
#include <climits> // For limits

void demonstrateIntegers() {
    // Different integer sizes
    short small_number = 100;
    int regular_number = 1000;
    long large_number = 100000;
    long long very_large = 1000000000LL;
    
    // Unsigned variants
    unsigned int positive_only = 42;
    unsigned long large_positive = 1000000UL;
    
    // Display size and limits
    std::cout << "Size of int: " << sizeof(int) << " bytes\n";
    std::cout << "Int max: " << INT_MAX << "\n";
    std::cout << "Int min: " << INT_MIN << "\n";
    std::cout << "Unsigned int max: " << UINT_MAX << "\n";
}
```

### Floating-Point Types
```cpp
#include <iostream>
#include <cfloat> // For floating-point limits
#include <iomanip> // For precision control

void demonstrateFloats() {
    // Different precision levels
    float single_precision = 3.14159f;    // f suffix for float
    double double_precision = 3.141592653589793;
    long double extended_precision = 3.14159265358979323846L; // L suffix
    
    // Scientific notation
    double scientific = 1.23e-4;  // 0.000123
    
    // Precision control
    std::cout << std::fixed << std::setprecision(10);
    std::cout << "Float: " << single_precision << "\n";
    std::cout << "Double: " << double_precision << "\n";
    
    // Floating-point limits
    std::cout << "Float max: " << FLT_MAX << "\n";
    std::cout << "Double max: " << DBL_MAX << "\n";
}
```

### Character Types
```cpp
#include <iostream>
#include <string>

void demonstrateCharacters() {
    // Basic character
    char basic_char = 'A';
    
    // Unicode characters (C++11)
    char16_t utf16_char = u'Ω';  // 2-byte Unicode
    char32_t utf32_char = U'😀'; // 4-byte Unicode
    wchar_t wide_char = L'中';    // Wide character
    
    // Character arrays (C-style strings)
    char c_string[] = "Hello";
    
    // Modern string
    std::string modern_string = "World";
    
    // Raw string literals (C++11)
    std::string raw_string = R"(This is a "raw" string with \n literal backslashes)";
    
    std::cout << "Basic char: " << basic_char << "\n";
    std::cout << "C-string: " << c_string << "\n";
    std::cout << "String: " << modern_string << "\n";
    std::cout << "Raw string: " << raw_string << "\n";
}
```

### Boolean Type
```cpp
#include <iostream>

void demonstrateBooleans() {
    // Boolean values
    bool is_true = true;
    bool is_false = false;
    
    // Booleans from other types (implicit conversion)
    bool from_int = (5 > 3);     // true
    bool from_zero = 0;          // false
    bool from_nonzero = 42;      // true
    
    // Output (boolalpha prints "true"/"false")
    std::cout << std::boolalpha;
    std::cout << "is_true: " << is_true << "\n";
    std::cout << "is_false: " << is_false << "\n";
    std::cout << "from_int: " << from_int << "\n";
    std::cout << "from_zero: " << from_zero << "\n";
    std::cout << "from_nonzero: " << from_nonzero << "\n";
}
```

## Variable Scope and Lifetime

### Local Variables
```cpp
#include <iostream>

void demonstrateLocalScope() {
    int local_var = 10;  // Only exists within this function
    
    if (local_var > 5) {
        int nested_var = 20;  // Only exists within this if block
        std::cout << "Nested: " << nested_var << "\n";
    }
    
    // Error: nested_var is not accessible here
    // std::cout << nested_var;  // Compilation error!
    
    std::cout << "Local: " << local_var << "\n";
}
```

### Global Variables
```cpp
#include <iostream>

// Global variable (accessible throughout the program)
int global_counter = 0;

// Static global variable (accessible only in this file)
static int file_counter = 0;

void incrementCounters() {
    global_counter++;
    file_counter++;
    std::cout << "Global: " << global_counter << ", File: " << file_counter << "\n";
}

int main() {
    incrementCounters();  // Global: 1, File: 1
    incrementCounters();  // Global: 2, File: 2
    return 0;
}
```

### Static Variables
```cpp
#include <iostream>

void demonstrateStatic() {
    // Static local variable (retains value between function calls)
    static int static_counter = 0;
    int regular_counter = 0;
    
    static_counter++;
    regular_counter++;
    
    std::cout << "Static: " << static_counter << ", Regular: " << regular_counter << "\n";
}

int main() {
    demonstrateStatic();  // Static: 1, Regular: 1
    demonstrateStatic();  // Static: 2, Regular: 1
    demonstrateStatic();  // Static: 3, Regular: 1
    return 0;
}
```

## Constants

### const Keyword
```cpp
#include <iostream>

void demonstrateConst() {
    // Constant variables
    const int MAX_SIZE = 100;
    const double PI = 3.14159;
    const std::string GREETING = "Hello";
    
    // Constants must be initialized
    // const int UNINITIALIZED;  // Error!
    
    // Cannot modify constants
    // MAX_SIZE = 200;  // Error!
    
    std::cout << "Max size: " << MAX_SIZE << "\n";
    std::cout << "PI: " << PI << "\n";
    std::cout << "Greeting: " << GREETING << "\n";
}
```

### constexpr (C++11)
```cpp
#include <iostream>

// Compile-time constant
constexpr int SQUARE(int x) {
    return x * x;
}

// constexpr variable
constexpr int BUFFER_SIZE = 1024;
constexpr double PI = 3.14159265358979323846;

int main() {
    // Can be used in array sizes and other compile-time contexts
    int array[BUFFER_SIZE];
    constexpr int result = SQUARE(10);
    
    std::cout << "Square of 10: " << result << "\n";
    std::cout << "Buffer size: " << BUFFER_SIZE << "\n";
    return 0;
}
```

## Type Deduction

### auto Keyword (C++11)
```cpp
#include <iostream>
#include <vector>
#include <map>

void demonstrateAuto() {
    // Basic type deduction
    auto integer = 42;           // int
    auto floating = 3.14;        // double
    auto character = 'A';        // char
    auto boolean = true;         // bool
    
    // Complex types
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    auto it = numbers.begin();   // std::vector<int>::iterator
    
    std::map<std::string, int> scores;
    scores["Alice"] = 95;
    auto pair = scores.begin();  // std::map<std::string, int>::iterator
    
    // Function return type deduction
    auto result = integer * 2;   // int
    
    std::cout << "Auto integer: " << integer << "\n";
    std::cout << "Auto floating: " << floating << "\n";
}
```

### decltype (C++11)
```cpp
#include <iostream>

void demonstrateDecltype() {
    int x = 10;
    double y = 3.14;
    
    // decltype preserves exact type
    decltype(x) same_as_x = 20;        // int
    decltype(y) same_as_y = 2.71;       // double
    decltype(x + y) sum = 13.14;        // double (result of addition)
    
    // decltype with expressions
    decltype((x)) reference_to_x = x;   // int& (due to extra parentheses)
    
    std::cout << "decltype x: " << same_as_x << "\n";
    std::cout << "decltype y: " << same_as_y << "\n";
    std::cout << "decltype sum: " << sum << "\n";
}
```

## Variable Naming Conventions

### Best Practices
```cpp
#include <iostream>

// Good naming conventions
int student_age = 20;                    // snake_case for variables
double average_score = 85.5;              // descriptive names
bool is_valid_input = true;               // boolean prefixes
const int MAX_STUDENTS = 50;              // UPPER_CASE for constants

class StudentManager {                     // PascalCase for classes
private:
    int total_students_;                  // trailing underscore for private members
    
public:
    void AddStudent() {                   // PascalCase for methods
        int new_student_id = 1001;        // descriptive local variables
    }
};

// Avoid these
int x;                                    // meaningless name
int a1, b2, c3;                          // non-descriptive
int temp;                                 // too generic
int num;                                  // abbreviation, be more specific
```

## Type Safety and Conversions

### Implicit Conversions
```cpp
#include <iostream>

void demonstrateImplicitConversions() {
    // Widening conversions (safe)
    int i = 42;
    double d = i;        // int to double (safe)
    
    // Narrowing conversions (potentially unsafe)
    double pi = 3.14159;
    int truncated = pi;  // double to int (loses precision)
    
    // Boolean conversions
    int zero = 0;
    int non_zero = 42;
    bool from_zero = zero;      // false
    bool from_nonzero = non_zero; // true
    
    std::cout << "Truncated pi: " << truncated << "\n";
    std::cout << "From zero: " << from_zero << "\n";
    std::cout << "From non-zero: " << from_nonzero << "\n";
}
```

### Explicit Conversions
```cpp
#include <iostream>

void demonstrateExplicitConversions() {
    double pi = 3.14159;
    int value;
    
    // C-style cast (avoid in modern C++)
    value = (int)pi;
    
    // Functional cast (better)
    value = int(pi);
    
    // Modern C++ casts (preferred)
    value = static_cast<int>(pi);  // Compile-time cast
    
    // const_cast (remove constness)
    const int const_val = 10;
    int& ref = const_cast<int&>(const_val);
    
    // reinterpret_cast (dangerous, for pointer conversions)
    // Only use when absolutely necessary
    
    std::cout << "Static cast result: " << value << "\n";
}
```

## Common Variable Pitfalls

### Uninitialized Variables
```cpp
#include <iostream>

void demonstrateUninitialized() {
    // Dangerous: uninitialized variables
    int uninitialized_int;      // Undefined value
    double uninitialized_double; // Undefined value
    
    // Always initialize variables
    int safe_int = 0;
    double safe_double = 0.0;
    bool safe_bool = false;
    
    std::cout << "Safe int: " << safe_int << "\n";
    // std::cout << "Unsafe int: " << uninitialized_int << "\n"; // Undefined!
}
```

### Variable Shadowing
```cpp
#include <iostream>

int global_var = 100;

void demonstrateShadowing() {
    int global_var = 200;  // Shadows the global variable
    
    std::cout << "Local global_var: " << global_var << "\n";     // 200
    std::cout << "Global global_var: " << ::global_var << "\n"; // 100 (using scope resolution)
    
    {
        int global_var = 300;  // Shadows both
        std::cout << "Nested global_var: " << global_var << "\n"; // 300
    }
}
```

## Memory and Variables

### Stack vs Heap
```cpp
#include <iostream>

void demonstrateMemory() {
    // Stack allocation (automatic)
    int stack_var = 42;  // Automatically managed
    
    // Heap allocation (manual)
    int* heap_var = new int(42);  // Must be manually deleted
    
    std::cout << "Stack: " << stack_var << "\n";
    std::cout << "Heap: " << *heap_var << "\n";
    
    delete heap_var;  // Must free heap memory
    heap_var = nullptr;  // Avoid dangling pointer
}
```
---
## C++ Operators

### Overview
- Operators are symbols that perform operations on variables and values. 
- C++ provides a rich set of operators divided into several categories.
---

### Arithmetic Operators
```cpp
#include <iostream>

void demonstrateArithmeticOperators() {
    int a = 10, b = 3;
    
    // Basic arithmetic
    int sum = a + b;         // Addition: 13
    int difference = a - b;  // Subtraction: 7
    int product = a * b;     // Multiplication: 30
    int quotient = a / b;    // Division: 3 (integer division)
    int remainder = a % b;   // Modulo: 1
    
    // Unary operators
    int x = 5;
    int y = +x;              // Unary plus: 5
    int z = -x;              // Unary minus: -5
    
    // Increment/Decrement
    int counter = 0;
    counter++;               // Post-increment: returns 0, then becomes 1
    ++counter;               // Pre-increment: becomes 2, returns 2
    counter--;               // Post-decrement: returns 2, then becomes 1
    --counter;               // Pre-decrement: becomes 0, returns 0
    
    std::cout << "Sum: " << sum << "\n";
    std::cout << "Remainder: " << remainder << "\n";
}
```

### Relational Operators
```cpp
#include <iostream>

void demonstrateRelationalOperators() {
    int a = 5, b = 10;
    
    bool equal = (a == b);            // Equal to: false
    bool not_equal = (a != b);        // Not equal to: true
    bool less_than = (a < b);         // Less than: true
    bool greater_than = (a > b);      // Greater than: false
    bool less_equal = (a <= b);       // Less than or equal: true
    bool greater_equal = (a >= b);    // Greater than or equal: false
    
    std::cout << std::boolalpha;
    std::cout << "5 == 10: " << equal << "\n";
    std::cout << "5 != 10: " << not_equal << "\n";
}
```

### Logical Operators
```cpp
#include <iostream>

void demonstrateLogicalOperators() {
    bool condition1 = true;
    bool condition2 = false;
    
    bool logical_and = condition1 && condition2;   // AND: false
    bool logical_or = condition1 || condition2;    // OR: true
    bool logical_not = !condition1;                // NOT: false
    
    // Short-circuit evaluation
    int x = 5;
    bool short_circuit = (x > 0) && (++x > 5);     // x becomes 6
    
    std::cout << "AND: " << logical_and << "\n";
    std::cout << "OR: " << logical_or << "\n";
    std::cout << "NOT: " << logical_not << "\n";
}
```

### Bitwise Operators
```cpp
#include <iostream>
#include <bitset>

void demonstrateBitwiseOperators() {
    unsigned int a = 0b1010;            // 10 in binary
    unsigned int b = 0b1100;            // 12 in binary
    
    unsigned int bitwise_and = a & b;   // AND: 1000 (8)
    unsigned int bitwise_or = a | b;    // OR: 1110 (14)
    unsigned int bitwise_xor = a ^ b;   // XOR: 0110 (6)
    unsigned int bitwise_not = ~a;      // NOT: 111...10101 (depends on bit width)
    
    unsigned int left_shift = a << 2;   // Left shift: 101000 (40)
    unsigned int right_shift = a >> 1;  // Right shift: 101 (5)
    
    std::cout << "a & b: " << std::bitset<4>(bitwise_and) << " (" << bitwise_and << ")\n";
    std::cout << "a | b: " << std::bitset<4>(bitwise_or) << " (" << bitwise_or << ")\n";
    std::cout << "a ^ b: " << std::bitset<4>(bitwise_xor) << " (" << bitwise_xor << ")\n";
    std::cout << "a << 2: " << left_shift << "\n";
}
```

### Assignment Operators
```cpp
#include <iostream>

void demonstrateAssignmentOperators() {
    int x = 10;      // Basic assignment
    
    // Compound assignment
    x += 5;          // x = x + 5 → 15
    x -= 3;          // x = x - 3 → 12
    x *= 2;          // x = x * 2 → 24
    x /= 4;          // x = x / 4 → 6
    x %= 2;          // x = x % 2 → 0
    
    // Bitwise compound assignment
    int y = 0b1010;
    y &= 0b1100;     // y = y & 0b1100 → 1000 (8)
    y |= 0b0011;     // y = y | 0b0011 → 1011 (11)
    y ^= 0b0110;     // y = y ^ 0b0110 → 1101 (13)
    y <<= 1;         // y = y << 1 → 11010 (26)
    
    std::cout << "x: " << x << "\n";
    std::cout << "y: " << y << "\n";
}
```

### Comparison and Ternary Operator
```cpp
#include <iostream>

void demonstrateComparisonAndTernary() {
    int a = 5, b = 10;
    
    // Three-way comparison (C++20 spaceship operator)
    #if __cplusplus >= 202002L
    auto result = a <=> b;                        // Returns std::strong_ordering
    if (result < 0) std::cout << "a < b\n";
    else if (result > 0) std::cout << "a > b\n";
    else std::cout << "a == b\n";
    #endif
    
    // Ternary conditional operator
    int max = (a > b) ? a : b;                    // Returns the larger value
    std::cout << "Maximum: " << max << "\n";
    
    // Chained ternary
    int value = 25;
    std::string grade = (value >= 90) ? "A" :
                        (value >= 80) ? "B" :
                        (value >= 70) ? "C" : "F";
    std::cout << "Grade: " << grade << "\n";
}
```

### Operator Precedence
```cpp
#include <iostream>

void demonstrateOperatorPrecedence() {
    // Multiplication has higher precedence than addition
    int result1 = 5 + 3 * 2;                        // 11, not 16

    // Use parentheses to change evaluation order
    int result2 = (5 + 3) * 2;                      // 16
    
    // Logical AND has higher precedence than OR
    bool result3 = true || false && false;          // true (&& evaluated first)
    bool result4 = (true || false) && false;        // false
    
    std::cout << "5 + 3 * 2 = " << result1 << "\n";
    std::cout << "(5 + 3) * 2 = " << result2 << "\n";
}
```

---
### Common precedence rules (highest to lowest):
```
    1. () [] . -> 
    2. ++ -- ! ~ + - (unary)
    3. * / %
    4. + -
    5. << >>
    6. < <= > >=
    7. == !=
    8. &
    9. ^
    10. |
    11. &&
    12. ||
    13. ?:
    14. = += -= etc.
    15. ,
```
---

### Special Operators
```cpp
#include <iostream>

void demonstrateSpecialOperators() {
    // sizeof operator
    int x = 42;
    std::cout << "Size of int: " << sizeof(int) << " bytes\n";
    std::cout << "Size of x: " << sizeof(x) << " bytes\n";
    
    // comma operator
    int a, b, c;
    a = (b = 5, c = 10, b + c);             // a = 15
    
    // typeid operator (requires <typeinfo>)
    #include <typeinfo>
    std::cout << "Type of x: " << typeid(x).name() << "\n";
    
    // address-of and dereference
    int value = 100;
    int* ptr = &value;                      // address-of operator
    int dereferenced = *ptr;                // dereference operator: 100
    
    // member access operators
    struct Point { int x; int y; };
    Point p = {10, 20};
    Point* pptr = &p;
    
    int x_coord = p.x;                      // Direct member access (.)
    int y_coord = pptr->y;                  // Pointer member access (->)
}
```

### Practical Example: Combining Operators
```cpp
#include <iostream>

void demonstrateOperatorCombination() {
    // Calculate compound interest with combined operators
    double principal = 1000.0;
    double rate = 0.05;
    int years = 3;
    
    double amount = principal;
    for (int i = 0; i < years; ++i) {
        amount *= (1 + rate);               // Compound assignment with multiplication
    }
    
    // Multiple operations in one line
    int a = 5, b = 10, c = 15;
    int result = (a + b) * c / 2 - 10;      // (5+10)*15/2-10 = 102.5? No, integer division!
    
    // Using ternary with assignment
    int value = (a > b) ? a : b;
    value = (c > value) ? c : value;        // Find maximum of three numbers
    
    std::cout << "Amount after " << years << " years: $" << amount << "\n";
    std::cout << "Result: " << result << "\n";
    std::cout << "Maximum value: " << value << "\n";
}
```

### 2. Add after "Type Safety and Conversions" section:

## Operator Overloading (Brief Overview)
Operators can be overloaded for user-defined types:

```cpp
#include <iostream>

class Vector {
public:
    int x, y;
    
    Vector(int x_val, int y_val) : x(x_val), y(y_val) {}
    
    // Overload + operator
    Vector operator+(const Vector& other) const {
        return Vector(x + other.x, y + other.y);
    }
    
    // Overload += operator
    Vector& operator+=(const Vector& other) {
        x += other.x;
        y += other.y;
        return *this;
    }
};

void demonstrateOperatorOverloading() {
    Vector v1(1, 2);
    Vector v2(3, 4);
    
    Vector v3 = v1 + v2;  // Uses overloaded + operator
    v1 += v2;              // Uses overloaded += operator
    
    std::cout << "v3: (" << v3.x << ", " << v3.y << ")\n";
}
```

## Best Practices Summary

1. **Always initialize variables** before use
2. **Use meaningful names** that describe the variable's purpose
3. **Prefer const/constexpr** for values that don't change
4. **Use auto** when the type is obvious from the right side
5. **Prefer modern C++ casts** over C-style casts
6. **Minimize global variables** - prefer local or class members
7. **Use appropriate scope** - declare variables in the smallest scope possible
8. **Follow naming conventions** consistently throughout your code
9. **Be aware of type conversions** and their implications
10. **Manage memory properly** when using pointers and dynamic allocation
11. **Use parentheses for clarity** when operator precedence might be ambiguous
12. **Prefer prefix increment (++i)** over postfix (i++) when the old value isn't needed
13. **Use compound operators** (+=, -=, etc.) for cleaner code
14. **Be careful with integer division** - it truncates toward zero
15. **Understand short-circuit evaluation** in logical operators
16. **Use bitwise operators** only when working with bits or flags

## Conclusion

Understanding variables and keywords is fundamental to C++ programming. Modern C++ provides many features for safer and more expressive variable handling. By following best practices and using modern C++ features, you can write more maintainable and error-free code.
