# Templates and Generic Programming in C++ - Complete Guide

## 📖 Overview

Templates are a powerful C++ feature that enables generic programming - writing code that works with multiple data types without sacrificing type safety. Templates allow you to define functions and classes that can operate on any data type, making your code more reusable, flexible, and maintainable.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Function Templates** | Generic functions that work with multiple types |
| **Class Templates** | Generic classes that can hold any type |
| **Template Specialization** | Custom behavior for specific types |
| **Variadic Templates** | Templates with variable number of arguments |
| **Template Metaprogramming** | Compile-time computation using templates |

---

## 1. **Function Templates**

### Definition
Function templates allow you to write generic functions that can work with different data types.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Generic function template
template <typename T>
T findMax(T a, T b) {
    return (a > b) ? a : b;
}

// Multiple template parameters
template <typename T, typename U>
void printPair(T first, U second) {
    cout << "Pair: " << first << " and " << second << endl;
}

// Template with constraints (C++20 concepts)
template <typename T>
requires requires(T x, T y) { x + y; }
T addValues(T a, T b) {
    return a + b;
}

int main() {
    cout << "=== Function Templates ===" << endl;
    
    // Working with different types
    cout << "Max of 10 and 20: " << findMax(10, 20) << endl;
    cout << "Max of 3.14 and 2.71: " << findMax(3.14, 2.71) << endl;
    cout << "Max of 'A' and 'Z': " << findMax('A', 'Z') << endl;
    
    cout << "\nMultiple template parameters:" << endl;
    printPair(42, "Hello");
    printPair(3.14, "Pi");
    printPair("Age", 25);
    
    cout << "\nConstrained template:" << endl;
    cout << "Add integers: " << addValues(5, 3) << endl;
    cout << "Add doubles: " << addValues(2.5, 1.5) << endl;
    // addValues("Hello", "World"); // Would fail constraint
    
    return 0;
}
```

---

## 2. **Class Templates**

### Definition
Class templates allow you to create generic classes that can work with any data type.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Generic Box class template
template <typename T>
class Box {
private:
    T content;
    
public:
    Box(T value) : content(value) {}
    
    T getContent() const { return content; }
    void setContent(T value) { content = value; }
    
    void display() const {
        cout << "Box contains: " << content << endl;
    }
};

// Generic Stack class template
template <typename T>
class Stack {
private:
    vector<T> items;
    
public:
    void push(const T& item) {
        items.push_back(item);
    }
    
    T pop() {
        if (items.empty()) {
            throw runtime_error("Stack is empty");
        }
        T top = items.back();
        items.pop_back();
        return top;
    }
    
    T& top() {
        if (items.empty()) {
            throw runtime_error("Stack is empty");
        }
        return items.back();
    }
    
    bool isEmpty() const {
        return items.empty();
    }
    
    size_t size() const {
        return items.size();
    }
};

// Template with non-type parameter
template <typename T, int SIZE>
class FixedArray {
private:
    T data[SIZE];
    
public:
    T& operator[](int index) {
        if (index < 0 || index >= SIZE) {
            throw out_of_range("Index out of bounds");
        }
        return data[index];
    }
    
    const T& operator[](int index) const {
        if (index < 0 || index >= SIZE) {
            throw out_of_range("Index out of bounds");
        }
        return data[index];
    }
    
    int getSize() const { return SIZE; }
};

int main() {
    cout << "=== Class Templates ===" << endl;
    
    // Box with different types
    Box<int> intBox(42);
    Box<string> stringBox("Hello Templates");
    Box<double> doubleBox(3.14159);
    
    intBox.display();
    stringBox.display();
    doubleBox.display();
    
    cout << "\nStack template:" << endl;
    Stack<int> intStack;
    intStack.push(10);
    intStack.push(20);
    intStack.push(30);
    
    cout << "Stack size: " << intStack.size() << endl;
    cout << "Top element: " << intStack.top() << endl;
    
    while (!intStack.isEmpty()) {
        cout << "Popped: " << intStack.pop() << endl;
    }
    
    cout << "\nFixed array with non-type parameter:" << endl;
    FixedArray<string, 3> stringArray;
    stringArray[0] = "First";
    stringArray[1] = "Second";
    stringArray[2] = "Third";
    
    for (int i = 0; i < 3; i++) {
        cout << "Array[" << i << "]: " << stringArray[i] << endl;
    }
    
    return 0;
}
```

---

## 3. **Template Specialization**

### Definition
Template specialization allows you to define custom behavior for specific data types.

```cpp
#include <iostream>
#include <cstring>
using namespace std;

// General template
template <typename T>
class Calculator {
public:
    T add(T a, T b) {
        cout << "General template add" << endl;
        return a + b;
    }
    
    T multiply(T a, T b) {
        cout << "General template multiply" << endl;
        return a * b;
    }
};

// Full specialization for const char*
template <>
class Calculator<const char*> {
public:
    const char* add(const char* a, const char* b) {
        cout << "String specialization add" << endl;
        static char result[100];
        strcpy(result, a);
        strcat(result, b);
        return result;
    }
    
    const char* multiply(const char* a, const char* b) {
        cout << "String specialization multiply (concatenation)" << endl;
        return add(a, b); // Reuse add functionality
    }
};

// Partial specialization for pointer types
template <typename T>
class Calculator<T*> {
public:
    T add(T* a, T* b) {
        cout << "Pointer specialization add" << endl;
        return *a + *b;
    }
    
    T multiply(T* a, T* b) {
        cout << "Pointer specialization multiply" << endl;
        return *a * *b;
    }
};

// Template function with specialization
template <typename T>
void printType(T value) {
    cout << "Generic type: " << value << endl;
}

// Full specialization for bool
template <>
void printType<bool>(bool value) {
    cout << "Boolean value: " << (value ? "TRUE" : "FALSE") << endl;
}

int main() {
    cout << "=== Template Specialization ===" << endl;
    
    // General template usage
    Calculator<int> intCalc;
    cout << "5 + 3 = " << intCalc.add(5, 3) << endl;
    cout << "5 * 3 = " << intCalc.multiply(5, 3) << endl;
    
    cout << "\nString specialization:" << endl;
    Calculator<const char*> stringCalc;
    cout << "Hello + World = " << stringCalc.add("Hello", " World") << endl;
    cout << "Hi * There = " << stringCalc.multiply("Hi", " There") << endl;
    
    cout << "\nPointer specialization:" << endl;
    int x = 10, y = 20;
    Calculator<int*> ptrCalc;
    cout << "*x + *y = " << ptrCalc.add(&x, &y) << endl;
    cout << "*x * *y = " << ptrCalc.multiply(&x, &y) << endl;
    
    cout << "\nFunction specialization:" << endl;
    printType(42);
    printType(3.14);
    printType("Hello");
    printType(true);
    
    return 0;
}
```

---

## 4. **Variadic Templates**

### Definition
Variadic templates accept a variable number of template arguments, enabling flexible function and class designs.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Variadic function template
template <typename T>
void print(T value) {
    cout << value;
}

// Recursive variadic function
template <typename T, typename... Args>
void print(T first, Args... args) {
    cout << first;
    if constexpr (sizeof...(args) > 0) {
        cout << ", ";
        print(args...);
    }
}

// Variadic template with fold expression (C++17)
template <typename... Args>
auto sum(Args... args) {
    return (args + ... + 0); // Fold expression
}

// Count arguments
template <typename... Args>
constexpr size_t countArgs(Args... args) {
    return sizeof...(args);
}

// Variadic class template
template <typename... Types>
class Tuple {
public:
    void printTypes() const {
        cout << "Tuple contains " << sizeof...(Types) << " types" << endl;
    }
};

// Template parameter pack expansion
template <typename... Args>
void printAll(Args&&... args) {
    ((cout << args << endl), ...); // Fold expression over comma operator
}

int main() {
    cout << "=== Variadic Templates ===" << endl;
    
    // Variadic function calls
    cout << "Print single: ";
    print(42);
    cout << endl;
    
    cout << "Print multiple: ";
    print(1, 2.5, "Hello", 'A');
    cout << endl;
    
    // Fold expressions
    cout << "\nSum of integers: " << sum(1, 2, 3, 4, 5) << endl;
    cout << "Sum of doubles: " << sum(1.1, 2.2, 3.3) << endl;
    cout << "Sum of mixed: " << sum(1, 2.5, 3) << endl;
    
    // Count arguments
    cout << "\nCount arguments:" << endl;
    cout << "countArgs(1, 2, 3) = " << countArgs(1, 2, 3) << endl;
    cout << "countArgs('a', \"hello\", 3.14) = " << countArgs('a', "hello", 3.14) << endl;
    
    // Variadic class
    cout << "\nVariadic class:" << endl;
    Tuple<int, string, double> myTuple;
    myTuple.printTypes();
    
    // Print all with fold expression
    cout << "\nPrint all:" << endl;
    printAll("First", 2, "Third", 4.5, "Fifth");
    
    return 0;
}
```

---

## 5. **Template Metaprogramming**

### Definition
Template metaprogramming uses templates to perform computations at compile time, enabling zero-overhead abstractions.

```cpp
#include <iostream>
#include <type_traits>
using namespace std;

// Compile-time factorial
template <int N>
struct Factorial {
    static constexpr int value = N * Factorial<N - 1>::value;
};

// Base case
template <>
struct Factorial<0> {
    static constexpr int value = 1;
};

// Compile-time power
template <int Base, int Exp>
struct Power {
    static constexpr int value = Base * Power<Base, Exp - 1>::value;
};

template <int Base>
struct Power<Base, 0> {
    static constexpr int value = 1;
};

// Type traits
template <typename T>
struct is_pointer : false_type {};

template <typename T>
struct is_pointer<T*> : true_type {};

// Conditional type selection
template <bool condition, typename TrueType, typename FalseType>
struct conditional_type {
    using type = TrueType;
};

template <typename TrueType, typename FalseType>
struct conditional_type<false, TrueType, FalseType> {
    using type = FalseType;
};

// Compile-time array size
template <typename T, size_t N>
constexpr size_t arraySize(T (&)[N]) {
    return N;
}

// SFINAE example
template <typename T>
typename enable_if<is_integral<T>::value, T>::type
doubleValue(T value) {
    cout << "Integral version: ";
    return value * 2;
}

template <typename T>
typename enable_if<is_floating_point<T>::value, T>::type
doubleValue(T value) {
    cout << "Floating point version: ";
    return value * 2.0;
}

int main() {
    cout << "=== Template Metaprogramming ===" << endl;
    
    // Compile-time computations
    cout << "Factorial<5>::value = " << Factorial<5>::value << endl;
    cout << "Factorial<6>::value = " << Factorial<6>::value << endl;
    
    cout << "Power<2, 8>::value = " << Power<2, 8>::value << endl;
    cout << "Power<3, 4>::value = " << Power<3, 4>::value << endl;
    
    // Type traits
    cout << "\nType traits:" << endl;
    cout << "is_pointer<int>::value = " << is_pointer<int>::value << endl;
    cout << "is_pointer<int*>::value = " << is_pointer<int*>::value << endl;
    cout << "is_pointer<string>::value = " << is_pointer<string>::value << endl;
    
    // Conditional types
    cout << "\nConditional types:" << endl;
    using TrueType = conditional_type<true, int, double>::type;
    using FalseType = conditional_type<false, int, double>::type;
    
    TrueType trueVal = 42;
    FalseType falseVal = 3.14;
    
    cout << "True type value: " << trueVal << endl;
    cout << "False type value: " << falseVal << endl;
    
    // Array size at compile time
    int arr[] = {1, 2, 3, 4, 5};
    cout << "\nArray size: " << arraySize(arr) << endl;
    
    // SFINAE
    cout << "\nSFINAE:" << endl;
    cout << doubleValue(5) << endl;
    cout << doubleValue(3.14) << endl;
    
    return 0;
}
```

---

## 📊 Template Features Summary

| Feature | Purpose | Example |
|---------|---------|---------|
| **Function Templates** | Generic functions | `template<typename T> T max(T a, T b)` |
| **Class Templates** | Generic classes | `template<typename T> class Stack` |
| **Specialization** | Custom behavior | `template<> class Calculator<bool>` |
| **Variadic Templates** | Variable arguments | `template<typename... Args> void print(Args... args)` |
| **Metaprogramming** | Compile-time computation | `template<int N> struct Factorial` |

---

## ⚡ Performance Considerations

### Advantages
- ✅ **Zero Overhead**: Templates generate optimized code
- ✅ **Type Safety**: Compile-time type checking
- ✅ **Code Reuse**: Single implementation for multiple types
- ✅ **Compile-time Optimization**: Constant folding and inlining

### Considerations
- ⚠️ **Code Bloat**: Can increase executable size
- ⚠️ **Compilation Time**: Longer build times
- ⚠️ **Debugging**: Error messages can be complex
- ⚠️ **Binary Size**: Multiple instantiations

---

## 🐛 Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| **Template definition in .cpp file** | Put definitions in header files |
| **Missing template arguments** | Use type deduction or default parameters |
| **Ambiguous function calls** | Use explicit template specialization |
| **Long compilation times** | Use explicit instantiation for common types |
| **Complex error messages** | Use static_assert for clearer errors |

---

## ✅ Best Practices

1. **Prefer templates over macros** for type safety
2. **Use concepts (C++20)** to constrain templates
3. **Keep template definitions in headers**
4. **Use meaningful template parameter names**
5. **Consider explicit instantiation** for common types
6. **Use static_assert** for better error messages
7. **Document template requirements** and constraints

---

## 📚 Related Topics

- [STL Containers and Algorithms](../04_Encapsulation/01_Data_Hiding.md)
- [Type System and Type Safety](../02_Classes_and_Objects/03_Access_Specifiers.md)
- [Compile-time Optimization](../14_Modern_Cpp_OOP_Features/01_Auto_and_Decltype.md)
- [SFINAE and Concepts](../14_Modern_Cpp_OOP_Features/10_Concepts.md)

---

## 🚀 Next Steps

After mastering templates, explore:
- **STL Implementation**: Understanding how templates power the STL
- **Template Libraries**: Boost, Eigen, and other template-based libraries
- **C++20 Concepts**: Modern template constraints
- **Metaprogramming Techniques**: Advanced compile-time programming

---
---

## Next Step

- Go to [README.md](README.md) to continue.
