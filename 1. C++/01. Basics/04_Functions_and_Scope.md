# Functions and Scope

## Overview
Functions are fundamental building blocks in C++ that allow code reuse, modularization, and abstraction. They encapsulate specific tasks and can be called multiple times with different inputs.

## Function Declaration and Definition

### Basic Function Structure
```cpp
// Function declaration (prototype)
returnType functionName(parameter1Type parameter1, parameter2Type parameter2);

// Function definition
returnType functionName(parameter1Type parameter1, parameter2Type parameter2) {
    // Function body
    // ...
    return returnValue;  // Optional for void functions
}
```

### Function Examples
```cpp
// Function with no parameters and no return value
void printHello() {
    std::cout << "Hello, World!" << std::endl;
}

// Function with parameters and return value
int add(int a, int b) {
    return a + b;
}

// Function with default parameters
int multiply(int a, int b = 2) {
    return a * b;
}

// Function with reference parameters
void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

// Function with constant reference parameters
void printVector(const std::vector<int>& vec) {
    for (int val : vec) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}
```

## Parameter Passing Methods

### 1. Pass by Value
```cpp
void modifyValue(int x) {
    x = 100;  // Only modifies local copy
}

int main() {
    int num = 5;
    modifyValue(num);  // num remains 5
    return 0;
}
```

### 2. Pass by Reference
```cpp
void modifyReference(int& x) {
    x = 100;  // Modifies original variable
}

int main() {
    int num = 5;
    modifyReference(num);  // num becomes 100
    return 0;
}
```

### 3. Pass by Constant Reference
```cpp
void printValue(const int& x) {
    std::cout << x << std::endl;
    // x = 100;  // Error: cannot modify const reference
}
```

### 4. Pass by Pointer
```cpp
void modifyPointer(int* x) {
    *x = 100;  // Modifies value pointed to
}

int main() {
    int num = 5;
    modifyPointer(&num);  // num becomes 100
    return 0;
}
```

## Function Overloading

### Multiple Functions with Same Name
```cpp
int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}

int add(int a, int b, int c) {
    return a + b + c;
}

std::string add(const std::string& a, const std::string& b) {
    return a + b;
}
```

## Return Types

### Multiple Return Values
```cpp
// Using std::pair
std::pair<int, int> getMinMax(const std::vector<int>& arr) {
    if (arr.empty()) return {0, 0};
    
    int minVal = arr[0], maxVal = arr[0];
    for (int val : arr) {
        minVal = std::min(minVal, val);
        maxVal = std::max(maxVal, val);
    }
    return {minVal, maxVal};
}

// Using std::tuple
std::tuple<int, double, std::string> getMixedValues() {
    return {42, 3.14, "Hello"};
}

// Using struct
struct Result {
    int sum;
    double average;
    bool success;
};

Result calculateStats(const std::vector<int>& arr) {
    Result result;
    if (arr.empty()) {
        result = {0, 0.0, false};
        return result;
    }
    
    int sum = 0;
    for (int val : arr) {
        sum += val;
    }
    
    result = {sum, static_cast<double>(sum) / arr.size(), true};
    return result;
}
```

## Scope in C++

### Types of Scope

#### 1. Global Scope
```cpp
int globalVar = 100;  // Global variable

void function() {
    std::cout << globalVar << std::endl;  // Accessible
}

int main() {
    std::cout << globalVar << std::endl;  // Accessible
    return 0;
}
```

#### 2. Function Scope
```cpp
void function() {
    int localVar = 50;  // Local to this function
    std::cout << localVar << std::endl;
}

int main() {
    // std::cout << localVar << std::endl;  // Error: not accessible
    return 0;
}
```

#### 3. Block Scope
```cpp
int main() {
    int x = 10;
    
    if (x > 5) {
        int y = 20;  // Block scope
        std::cout << x << " " << y << std::endl;
    }
    
    // std::cout << y << std::endl;  // Error: y not accessible here
    return 0;
}
```

#### 4. Namespace Scope
```cpp
namespace MyNamespace {
    int namespaceVar = 30;
    
    void namespaceFunction() {
        std::cout << "Namespace function" << std::endl;
    }
}

int main() {
    std::cout << MyNamespace::namespaceVar << std::endl;
    MyNamespace::namespaceFunction();
    return 0;
}
```

## Storage Classes

### auto
```cpp
void function() {
    auto x = 10;  // Type deduced as int
    auto y = 3.14;  // Type deduced as double
}
```

### register
```cpp
void function() {
    register int counter = 0;  // Suggest storing in register
    for (int i = 0; i < 1000; i++) {
        counter++;
    }
}
```

### static
```cpp
// Static local variable
void counter() {
    static int callCount = 0;  // Initialized once
    callCount++;
    std::cout << "Called " << callCount << " times" << std::endl;
}

// Static global variable (internal linkage)
static int globalCounter = 0;

// Static class member
class MyClass {
private:
    static int objectCount;
public:
    MyClass() {
        objectCount++;
    }
    
    static int getObjectCount() {
        return objectCount;
    }
};

int MyClass::objectCount = 0;  // Definition outside class
```

### extern
```cpp
// In header file (example.h)
extern int sharedVariable;

// In one source file (example.cpp)
int sharedVariable = 100;

// In another source file (main.cpp)
#include "example.h"
void function() {
    sharedVariable = 200;  // Access external variable
}
```

## Lambda Functions

### Basic Lambda Syntax
```cpp
int main() {
    // Simple lambda
    auto add = [](int a, int b) { return a + b; };
    std::cout << add(5, 3) << std::endl;
    
    // Lambda with capture
    int multiplier = 2;
    auto multiply = [multiplier](int x) { return x * multiplier; };
    std::cout << multiply(5) << std::endl;
    
    // Lambda with mutable capture
    int counter = 0;
    auto increment = [counter]() mutable { 
        counter++; 
        return counter; 
    };
    
    std::cout << increment() << std::endl;  // 1
    std::cout << increment() << std::endl;  // 2
    std::cout << counter << std::endl;     // 0 (original unchanged)
    
    return 0;
}
```

## Function Pointers and std::function

### Function Pointers
```cpp
int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int main() {
    // Function pointer declaration
    int (*operation)(int, int);
    
    // Assign function to pointer
    operation = add;
    std::cout << operation(5, 3) << std::endl;  // 8
    
    operation = subtract;
    std::cout << operation(5, 3) << std::endl;  // 2
    
    // Using function pointer as parameter
    auto calculate = [](int a, int b, int (*op)(int, int)) {
        return op(a, b);
    };
    
    std::cout << calculate(10, 5, add) << std::endl;  // 15
    
    return 0;
}
```

### std::function
```cpp
#include <functional>

int main() {
    // std::function can hold any callable target
    std::function<int(int, int)> operation;
    
    // Assign regular function
    operation = add;
    std::cout << operation(5, 3) << std::endl;
    
    // Assign lambda
    operation = [](int a, int b) { return a * b; };
    std::cout << operation(5, 3) << std::endl;
    
    // Use with algorithms
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    std::function<bool(int)> predicate = [](int x) { return x % 2 == 0; };
    
    auto countEven = std::count_if(numbers.begin(), numbers.end(), predicate);
    std::cout << "Even numbers: " << countEven << std::endl;
    
    return 0;
}
```

## Recursive Functions

### Basic Recursion
```cpp
// Factorial
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// Fibonacci
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Power function
double power(double base, int exp) {
    if (exp == 0) return 1.0;
    if (exp < 0) return 1.0 / power(base, -exp);
    return base * power(base, exp - 1);
}
```

### Tail Recursion Optimization
```cpp
// Tail-recursive factorial
int factorialTail(int n, int accumulator = 1) {
    if (n <= 1) return accumulator;
    return factorialTail(n - 1, n * accumulator);
}

// Tail-recursive sum
int sumArray(const std::vector<int>& arr, int index = 0, int accumulator = 0) {
    if (index >= arr.size()) return accumulator;
    return sumArray(arr, index + 1, accumulator + arr[index]);
}
```

## Inline Functions

### Inline Function Declaration
```cpp
inline int square(int x) {
    return x * x;
}

// Class member functions can be inline
class Calculator {
public:
    inline int add(int a, int b) {  // Inline by definition
        return a + b;
    }
    
    int multiply(int a, int b);  // Declaration
};

inline int Calculator::multiply(int a, int b) {  // Inline definition
    return a * b;
}
```

## constexpr Functions

### Compile-Time Functions
```cpp
constexpr int square(int x) {
    return x * x;
}

constexpr int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}

int main() {
    constexpr int result = square(5);  // Computed at compile time
    constexpr int fact = factorial(5);  // Computed at compile time
    
    int arr[factorial(4)];  // Valid: factorial(4) = 24
    
    return 0;
}
```

## Best Practices

### 1. Function Design
- Keep functions small and focused on a single task
- Use descriptive names that clearly indicate the function's purpose
- Limit the number of parameters (ideally ≤ 5)
- Use const correctness for parameters that shouldn't be modified

### 2. Parameter Passing
- Use pass by value for small, cheap-to-copy types
- Use pass by const reference for large objects
- Use pass by reference when you need to modify the argument
- Use pointers when you need to handle nullability

### 3. Return Values
- Return by value for most cases
- Return by reference when returning existing objects
- Use smart pointers for dynamic memory ownership
- Consider std::optional for functions that might not return a value

### 4. Scope Management
- Minimize global variables
- Use the smallest scope necessary for variables
- Prefer namespaces over global variables
- Use RAII for resource management

## Common Pitfalls

### 1. Scope Issues
```cpp
// Wrong: Using local variable outside scope
int* badFunction() {
    int local = 10;
    return &local;  // Error: returning pointer to local variable
}

// Correct: Use static or dynamic allocation
int* goodFunction() {
    static int local = 10;  // Static storage
    return &local;
}
```

### 2. Reference Issues
```cpp
// Wrong: Returning reference to local
int& badReference() {
    int local = 10;
    return local;  // Error: reference to local variable
}

// Correct: Return by value or static reference
int goodReference() {
    static int local = 10;
    return local;
}
```

### 3. Recursion Issues
```cpp
// Wrong: No base case
int infiniteRecursion(int n) {
    return infiniteRecursion(n - 1);  // Stack overflow
}

// Correct: Proper base case
int finiteRecursion(int n) {
    if (n <= 0) return 0;  // Base case
    return finiteRecursion(n - 1);
}
```

---

*This guide provides a comprehensive overview of functions and scope in C++, covering fundamental concepts and advanced techniques for effective function design and usage.*
---

## Next Step

- Go to [05_Arrays_and_Strings.md](05_Arrays_and_Strings.md) to continue with Arrays and Strings.
