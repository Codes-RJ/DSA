# 01_Function_Templates.md

## Function Templates in C++

### Overview

Function templates allow writing a single function that works with multiple data types. Instead of writing multiple overloaded functions for different types, you write one template function, and the compiler generates the appropriate version for each type used. Function templates are the foundation of generic programming in C++.

---

### What is a Function Template?

A function template is a blueprint for creating functions. It defines a family of functions that differ only by the types of their parameters or return values. When you call a function template, the compiler deduces the template arguments and generates a concrete function.

**Syntax:**
```cpp
template <typename T>
T functionName(T parameter) {
    // function body
}
```

**Key Components:**

| Component | Description | Example |
|-----------|-------------|---------|
| `template <typename T>` | Template parameter declaration | `template <typename T>` |
| `typename` or `class` | Keyword indicating a type parameter | `typename T` or `class T` |
| `T` | Template parameter name (placeholder for type) | Any valid identifier |
| Function body | Uses `T` as a regular type | `T result = a + b;` |

---

### Basic Function Template Example

This example demonstrates a simple function template that finds the maximum of two values.

```cpp
#include <iostream>
using namespace std;

// Function template definition
template <typename T>
T getMax(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    // Using with integers
    int x = 10, y = 20;
    int intMax = getMax(x, y);
    cout << "Max of " << x << " and " << y << " is " << intMax << endl;
    
    // Using with doubles
    double a = 3.14, b = 2.71;
    double doubleMax = getMax(a, b);
    cout << "Max of " << a << " and " << b << " is " << doubleMax << endl;
    
    // Using with characters
    char c1 = 'A', c2 = 'Z';
    char charMax = getMax(c1, c2);
    cout << "Max of '" << c1 << "' and '" << c2 << "' is '" << charMax << "'" << endl;
    
    // Using with strings
    string s1 = "apple", s2 = "orange";
    string stringMax = getMax(s1, s2);
    cout << "Max of \"" << s1 << "\" and \"" << s2 << "\" is \"" << stringMax << "\"" << endl;
    
    return 0;
}
```

**Output:**
```
Max of 10 and 20 is 20
Max of 3.14 and 2.71 is 3.14
Max of 'A' and 'Z' is 'Z'
Max of "apple" and "orange" is "orange"
```

---

### Function Template with Multiple Parameters

Function templates can have multiple type parameters.

```cpp
#include <iostream>
using namespace std;

// Function template with two different type parameters
template <typename T1, typename T2>
void display(T1 first, T2 second) {
    cout << "First: " << first << ", Second: " << second << endl;
    cout << "Size of first: " << sizeof(T1) << " bytes" << endl;
    cout << "Size of second: " << sizeof(T2) << " bytes" << endl;
}

// Function template with mixed return type
template <typename T1, typename T2>
auto add(T1 a, T2 b) -> decltype(a + b) {
    return a + b;
}

int main() {
    // Different type combinations
    display(10, 3.14);           // int and double
    display('A', "Hello");       // char and const char*
    display(3.14f, 100L);        // float and long
    
    // Auto return type deduction
    cout << "\nAdding different types:" << endl;
    cout << "10 + 3.14 = " << add(10, 3.14) << endl;      // returns double
    cout << "3.14f + 5 = " << add(3.14f, 5) << endl;     // returns float
    cout << "100 + 200L = " << add(100, 200L) << endl;    // returns long
    
    return 0;
}
```

**Output:**
```
First: 10, Second: 3.14
Size of first: 4 bytes
Size of second: 8 bytes
First: A, Second: Hello
Size of first: 1 bytes
Size of second: 8 bytes
First: 3.14, Second: 100
Size of first: 4 bytes
Size of second: 8 bytes

Adding different types:
10 + 3.14 = 13.14
3.14f + 5 = 8.14
100 + 200 = 300
```

---

### Template Parameter Deduction

When you call a function template, the compiler attempts to deduce the template arguments from the function arguments.

```cpp
#include <iostream>
using namespace std;

template <typename T>
T square(T value) {
    return value * value;
}

template <typename T>
void process(T a, T b) {
    cout << "Both arguments of same type: " << a << ", " << b << endl;
}

// Overload for different types
template <typename T1, typename T2>
void process(T1 a, T2 b) {
    cout << "Arguments of different types: " << a << ", " << b << endl;
}

int main() {
    // Type deduction examples
    int x = 5;
    double y = 3.14;
    
    // Deduced as int
    int intSquare = square(x);
    cout << "Square of " << x << " = " << intSquare << endl;
    
    // Deduced as double
    double doubleSquare = square(y);
    cout << "Square of " << y << " = " << doubleSquare << endl;
    
    // Both int - T deduced as int
    process(10, 20);
    
    // Both double - T deduced as double
    process(3.14, 2.71);
    
    // Different types - calls the two-parameter version
    process(10, 3.14);
    
    return 0;
}
```

**Output:**
```
Square of 5 = 25
Square of 3.14 = 9.8596
Both arguments of same type: 10, 20
Both arguments of same type: 3.14, 2.71
Arguments of different types: 10, 3.14
```

**Deduction Rules:**

| Scenario | Deduction Result |
|----------|------------------|
| Same type used for all parameters | Single type parameter deduced |
| Different types for same parameter | Compilation error (ambiguous) |
| Different types for different parameters | Use multiple type parameters |

---

### Explicit Template Instantiation

You can explicitly specify template arguments instead of relying on deduction.

```cpp
#include <iostream>
using namespace std;

template <typename T>
T multiply(T a, T b) {
    return a * b;
}

template <typename T>
T convert(int value) {
    return static_cast<T>(value);
}

int main() {
    int a = 5, b = 3;
    
    // Implicit deduction (T = int)
    int result1 = multiply(a, b);
    cout << "Implicit: " << a << " * " << b << " = " << result1 << endl;
    
    // Explicit instantiation (T = double)
    double result2 = multiply<double>(a, b);
    cout << "Explicit (double): " << a << " * " << b << " = " << result2 << endl;
    
    // Cannot deduce return type - must be explicit
    double d = convert<double>(42);
    cout << "Convert 42 to double: " << d << endl;
    
    float f = convert<float>(100);
    cout << "Convert 100 to float: " << f << endl;
    
    return 0;
}
```

**Output:**
```
Implicit: 5 * 3 = 15
Explicit (double): 5 * 3 = 15
Convert 42 to double: 42
Convert 100 to float: 100
```

**When to Use Explicit Instantiation:**

| Scenario | Reason |
|----------|--------|
| Return type differs from parameter types | Compiler cannot deduce return type |
| Template arguments cannot be deduced | No function arguments to deduce from |
| Ambiguous deduction | Multiple possible deductions |
| Want specific type conversion | Force conversion of arguments |

---

### Function Template Overloading

Function templates can be overloaded with other function templates or regular functions.

```cpp
#include <iostream>
using namespace std;

// Regular function
void print(int value) {
    cout << "Regular function (int): " << value << endl;
}

// Function template
template <typename T>
void print(T value) {
    cout << "Template function: " << value << endl;
}

// Overloaded function template
template <typename T>
void print(T value, int repeat) {
    for (int i = 0; i < repeat; i++) {
        cout << value << " ";
    }
    cout << endl;
}

// Template specialization (discussed in detail later)
template <>
void print<bool>(bool value) {
    cout << "Specialized template (bool): " << (value ? "true" : "false") << endl;
}

int main() {
    // Calls regular function (exact match)
    print(42);
    
    // Calls template (no exact regular function match)
    print(3.14);
    
    // Calls overloaded template
    print("Hello", 3);
    
    // Calls specialized template
    print(true);
    
    return 0;
}
```

**Output:**
```
Regular function (int): 42
Template function: 3.14
Hello Hello Hello 
Specialized template (bool): true
```

**Overload Resolution Rules:**

| Priority | Function Type |
|----------|---------------|
| 1 (Highest) | Regular function (exact match) |
| 2 | Template specialization |
| 3 | Function template (deduced) |
| 4 (Lowest) | Regular function (after conversion) |

---

### Non-Type Template Parameters

Function templates can also accept non-type parameters (compile-time constants).

```cpp
#include <iostream>
using namespace std;

// Non-type template parameter
template <typename T, int size>
T arraySum(T (&arr)[size]) {
    T sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

// Default non-type parameter
template <typename T, int multiplier = 2>
T multiplyBy(T value) {
    return value * multiplier;
}

// Using non-type parameter for compile-time checks
template <int N>
void printNTimes(const string& message) {
    for (int i = 0; i < N; i++) {
        cout << message << endl;
    }
}

int main() {
    // Array size deduced as non-type parameter
    int numbers[] = {1, 2, 3, 4, 5};
    int sum = arraySum(numbers);
    cout << "Sum of array: " << sum << endl;
    
    double prices[] = {10.5, 20.3, 15.8};
    double total = arraySum(prices);
    cout << "Total of prices: " << total << endl;
    
    // Using default multiplier
    cout << "5 * 2 (default) = " << multiplyBy(5) << endl;
    
    // Explicit multiplier
    cout << "5 * 3 = " << multiplyBy<int, 3>(5) << endl;
    
    // Compile-time loop
    printNTimes<3>("Hello, World!");
    
    return 0;
}
```

**Output:**
```
Sum of array: 15
Total of prices: 46.6
5 * 2 (default) = 10
5 * 3 = 15
Hello, World!
Hello, World!
Hello, World!
```

**Non-Type Parameter Restrictions:**

| Restriction | Description |
|-------------|-------------|
| **Integral types** | int, char, bool, enum, etc. |
| **Pointers** | To objects with external linkage |
| **References** | To objects with external linkage |
| **Nullptr** | `std::nullptr_t` |
| **Not allowed** | float, double, string, class objects |

---

### Function Templates with Default Parameters

Function templates can have default template arguments (C++11 and later).

```cpp
#include <iostream>
using namespace std;

// Default template parameter
template <typename T = int>
T getDefaultValue() {
    return T();
}

// Multiple defaults
template <typename T = double, int size = 10>
class Container {
    // Class template with defaults
};

// Function with default template parameter
template <typename T = int>
void displayValue(T value = T()) {
    cout << "Value: " << value << endl;
}

int main() {
    // Uses default (int)
    int defaultInt = getDefaultValue();
    cout << "Default int: " << defaultInt << endl;
    
    // Explicitly specify double
    double defaultDouble = getDefaultValue<double>();
    cout << "Explicit double: " << defaultDouble << endl;
    
    // Using default template parameter
    displayValue(42);      // T deduced as int
    displayValue(3.14);    // T deduced as double
    displayValue();        // Uses default T (int) and default value (0)
    
    return 0;
}
```

**Output:**
```
Default int: 0
Explicit double: 0
Value: 42
Value: 3.14
Value: 0
```

---

### Common Function Template Examples

#### 1. Swap Function Template

```cpp
template <typename T>
void swapValues(T& a, T& b) {
    T temp = a;
    a = b;
    b = temp;
}

// Usage
int x = 5, y = 10;
swapValues(x, y);  // x=10, y=5
```

#### 2. Find Minimum

```cpp
template <typename T>
T minValue(T a, T b) {
    return (a < b) ? a : b;
}

// Usage
int smallest = minValue(10, 20);     // 10
double smaller = minValue(3.14, 2.71); // 2.71
```

#### 3. Linear Search

```cpp
template <typename T>
int linearSearch(const T arr[], int size, const T& target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

// Usage
int numbers[] = {10, 20, 30, 40, 50};
int index = linearSearch(numbers, 5, 30);  // Returns 2
```

#### 4. Print Array

```cpp
template <typename T, int N>
void printArray(const T (&arr)[N]) {
    cout << "[";
    for (int i = 0; i < N; i++) {
        cout << arr[i];
        if (i < N - 1) cout << ", ";
    }
    cout << "]" << endl;
}

// Usage
int nums[] = {1, 2, 3, 4, 5};
printArray(nums);  // [1, 2, 3, 4, 5]
```

---

### Summary

| Concept | Key Point |
|---------|-----------|
| **Function Template** | Blueprint for creating functions for different types |
| **Template Parameter** | Placeholder for a type (or value) |
| **Type Deduction** | Compiler infers template arguments from function arguments |
| **Explicit Instantiation** | Manually specify template arguments |
| **Overloading** | Templates can be overloaded with functions or other templates |
| **Non-Type Parameters** | Compile-time constants as template arguments |
| **Default Parameters** | Default values for template arguments (C++11) |

---

### Key Takeaways

1. **Function templates** enable writing type-independent code
2. **Compiler deduces** template arguments in most cases
3. **Explicit instantiation** is needed when deduction fails
4. **Overloading rules** prefer regular functions over templates
5. **Non-type parameters** allow compile-time constants
6. **Function templates are defined in headers** (not .cpp files)
7. **Template code is generated** at compile time for each type used

---

### Next Steps

- Go to [02_Class_Templates.md](02_Class_Templates.md) to understand Class Templates.