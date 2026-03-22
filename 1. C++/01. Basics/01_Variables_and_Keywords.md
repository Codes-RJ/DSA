# C++ Variables and Keywords

## Overview

Variables in C++ are named storage locations that hold data values. Keywords are reserved words that have special meaning to the C++ compiler and cannot be used as identifiers. Understanding variables and keywords is fundamental to C++ programming.

## C++ Keywords

C++ has 97 reserved keywords (as of C++20). These are divided into several categories:

### Fundamental Type Keywords
```cpp
// Basic types
int        // Integer type
float      // Single-precision floating point
double     // Double-precision floating point
char       // Character type
bool       // Boolean type (true/false)
void       // No type
wchar_t    // Wide character type
char16_t   // UTF-16 character
char32_t   // UTF-32 character

// Type modifiers
signed     // Signed integer
unsigned   // Unsigned integer
short      // Short integer
long       // Long integer
long long  // Long long integer (C++11)
```

### Storage Class Specifiers
```cpp
auto       // Automatic storage duration (C++11: type inference)
register   // Register storage (deprecated)
static     // Static storage duration
extern     // External linkage
mutable    // Allows modification of const class members
thread_local // Thread-local storage (C++11)
```

### Type Qualifiers
```cpp
const      // Constant value
volatile   // Tells compiler not to optimize
```

### Control Flow Keywords
```cpp
// Selection
if         // Conditional statement
else       // Alternative conditional
switch     // Multi-way branch
case       // Switch case label
default    // Default switch case

// Loops
for        // For loop
while      // While loop
do         // Do-while loop

// Jump statements
break      // Exit loop or switch
continue   // Skip to next iteration
goto       // Unconditional jump
return     // Return from function
```

### Object-Oriented Keywords
```cpp
class      // Class definition
struct     // Structure definition
union      // Union definition
public     // Public access specifier
protected  // Protected access specifier
private    // Private access specifier
virtual    // Virtual function
friend     // Friend function/class
this       // Pointer to current object
operator   // Operator overloading
new        // Dynamic allocation
delete     // Dynamic deallocation
```

### Template and Generic Programming
```cpp
template   // Template declaration
typename   // Type parameter
concept    // Concept definition (C++20)
requires   // Requires clause (C++20)
```

### Exception Handling
```cpp
try        // Try block
catch      // Exception handler
throw      // Throw exception
noexcept   // Exception specification (C++11)
```

### Namespace Keywords
```cpp
namespace  // Namespace definition
using      // Using declaration/directive
```

### Modern C++ Keywords (C++11 and later)
```cpp
nullptr    // Null pointer literal
constexpr  // Constant expression
decltype   // Type inference
override   // Override specifier
final      // Final specifier
explicit   // Explicit constructor
decltype   // Declare type
alignas    // Alignment specifier
alignof    // Alignment query
static_assert // Compile-time assertion
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
    auto number = 42;        // int
    auto decimal = 3.14;     // double
    auto letter = 'A';       // char
    auto flag = true;        // bool
    auto text = "Hello";      // const char*
    auto str = std::string("Hi"); // std::string
    
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

## Conclusion

Understanding variables and keywords is fundamental to C++ programming. Modern C++ provides many features for safer and more expressive variable handling. By following best practices and using modern C++ features, you can write more maintainable and error-free code.
