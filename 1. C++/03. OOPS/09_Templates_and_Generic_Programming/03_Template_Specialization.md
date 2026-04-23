# 03_Template_Specialization.md

## Template Specialization in C++

### Overview

Template specialization allows providing custom implementations of templates for specific types or type categories. While a generic template works for most types, sometimes you need special behavior for certain types (e.g., `bool`, `char*`, or containers). Specialization enables optimization, type-specific logic, and handling of edge cases without sacrificing the benefits of generic programming.

---

### What is Template Specialization?

Template specialization is a mechanism that lets you define a separate version of a template for a specific set of template arguments. When the compiler encounters a template instantiation, it first looks for a matching specialization before using the primary template.

**Types of Specialization:**

| Type | Description | Example |
|------|-------------|---------|
| **Full Specialization** | Specific implementation for a concrete type | `template <> class Stack<bool>` |
| **Partial Specialization** | Implementation for a category of types | `template <typename T> class Stack<T*>` |
| **Function Template Specialization** | Specialization for function templates | `template <> void swap<Widget>(Widget&, Widget&)` |

---

### Full Specialization for Class Templates

Full specialization provides a completely separate implementation for a specific type.

```cpp
#include <iostream>
#include <cstring>
using namespace std;

// Primary template - works for most types
template <typename T>
class Printer {
public:
    void print(const T& value) {
        cout << "Generic printer: " << value << endl;
    }
};

// Full specialization for bool
template <>
class Printer<bool> {
public:
    void print(const bool& value) {
        cout << "Boolean printer: " << (value ? "true" : "false") << endl;
    }
};

// Full specialization for const char*
template <>
class Printer<const char*> {
public:
    void print(const char* value) {
        cout << "C-string printer: \"" << value << "\"" << endl;
    }
};

// Full specialization for string
template <>
class Printer<string> {
public:
    void print(const string& value) {
        cout << "String printer: \"" << value << "\"" << endl;
    }
};

int main() {
    Printer<int> intPrinter;
    intPrinter.print(42);
    
    Printer<double> doublePrinter;
    doublePrinter.print(3.14159);
    
    Printer<bool> boolPrinter;
    boolPrinter.print(true);
    boolPrinter.print(false);
    
    Printer<const char*> cstrPrinter;
    cstrPrinter.print("Hello, World!");
    
    Printer<string> strPrinter;
    strPrinter.print("C++ Programming");
    
    return 0;
}
```

**Output:**
```
Generic printer: 42
Generic printer: 3.14159
Boolean printer: true
Boolean printer: false
C-string printer: "Hello, World!"
String printer: "C++ Programming"
```

---

### Full Specialization for Function Templates

Function templates can also be fully specialized.

```cpp
#include <iostream>
#include <string>
#include <cstring>
using namespace std;

// Primary function template
template <typename T>
T maxValue(T a, T b) {
    cout << "Generic max: ";
    return (a > b) ? a : b;
}

// Full specialization for const char* (C-style strings)
template <>
const char* maxValue<const char*>(const char* a, const char* b) {
    cout << "C-string max (strcmp): ";
    return (strcmp(a, b) > 0) ? a : b;
}

// Full specialization for string
template <>
string maxValue<string>(string a, string b) {
    cout << "String max (lexicographic): ";
    return (a > b) ? a : b;
}

// Full specialization for int (can optimize)
template <>
int maxValue<int>(int a, int b) {
    cout << "Integer max (optimized): ";
    return (a > b) ? a : b;
}

int main() {
    cout << maxValue(10, 20) << endl;
    cout << maxValue(3.14, 2.71) << endl;
    cout << maxValue('A', 'Z') << endl;
    
    const char* str1 = "apple";
    const char* str2 = "orange";
    cout << maxValue(str1, str2) << endl;
    
    string s1 = "hello";
    string s2 = "world";
    cout << maxValue(s1, s2) << endl;
    
    return 0;
}
```

**Output:**
```
Integer max (optimized): 20
Generic max: 3.14
Generic max: Z
C-string max (strcmp): orange
String max (lexicographic): world
```

---

### Partial Specialization for Class Templates

Partial specialization applies when some (but not all) template parameters are specified. This is only available for class templates (not function templates).

```cpp
#include <iostream>
using namespace std;

// Primary template
template <typename T, typename U>
class Pair {
public:
    void display() {
        cout << "Generic Pair: (" << typeid(T).name() << ", " 
             << typeid(U).name() << ")" << endl;
    }
};

// Partial specialization: Both types are the same
template <typename T>
class Pair<T, T> {
public:
    void display() {
        cout << "Same-type Pair: (" << typeid(T).name() 
             << ", " << typeid(T).name() << ")" << endl;
    }
};

// Partial specialization: First type is pointer
template <typename T, typename U>
class Pair<T*, U> {
public:
    void display() {
        cout << "Pointer-first Pair: (T*, U)" << endl;
    }
};

// Partial specialization: Second type is pointer
template <typename T, typename U>
class Pair<T, U*> {
public:
    void display() {
        cout << "Pointer-second Pair: (T, U*)" << endl;
    }
};

// Partial specialization: Both are pointers
template <typename T, typename U>
class Pair<T*, U*> {
public:
    void display() {
        cout << "Both-pointers Pair: (T*, U*)" << endl;
    }
};

// Partial specialization: First is const
template <typename T, typename U>
class Pair<const T, U> {
public:
    void display() {
        cout << "Const-first Pair: (const T, U)" << endl;
    }
};

int main() {
    Pair<int, double> p1;
    p1.display();
    
    Pair<int, int> p2;
    p2.display();
    
    Pair<int*, double> p3;
    p3.display();
    
    Pair<int, double*> p4;
    p4.display();
    
    Pair<int*, double*> p5;
    p5.display();
    
    Pair<const int, double> p6;
    p6.display();
    
    return 0;
}
```

**Output:**
```
Generic Pair: (i, d)
Same-type Pair: (i, i)
Pointer-first Pair: (T*, U)
Pointer-second Pair: (T, U*)
Both-pointers Pair: (T*, U*)
Const-first Pair: (const T, U)
```

---

### Specialization for Arrays

Partial specialization for array types is common in template metaprogramming.

```cpp
#include <iostream>
using namespace std;

// Primary template
template <typename T>
class ArrayInfo {
public:
    static void show() {
        cout << "Type: " << typeid(T).name() << " (not an array)" << endl;
    }
};

// Partial specialization for array of known size
template <typename T, int N>
class ArrayInfo<T[N]> {
public:
    static void show() {
        cout << "Array of " << N << " elements of type: " 
             << typeid(T).name() << endl;
    }
};

// Partial specialization for unbounded array
template <typename T>
class ArrayInfo<T[]> {
public:
    static void show() {
        cout << "Unbounded array of type: " << typeid(T).name() << endl;
    }
};

// Get array size at compile time
template <typename T, int N>
int getArraySize(T (&)[N]) {
    return N;
}

int main() {
    ArrayInfo<int>::show();
    
    int arr1[10];
    ArrayInfo<decltype(arr1)>::show();
    
    int arr2[];
    ArrayInfo<decltype(arr2)>::show();
    
    // Compile-time array size
    int numbers[] = {1, 2, 3, 4, 5};
    cout << "Array size: " << getArraySize(numbers) << endl;
    
    double prices[] = {10.5, 20.3, 15.8, 30.2};
    cout << "Array size: " << getArraySize(prices) << endl;
    
    return 0;
}
```

---

### Specialization for Pointers and References

Specializing for pointer and reference types is common in type traits.

```cpp
#include <iostream>
using namespace std;

// Primary template - detects if type is a pointer
template <typename T>
struct IsPointer {
    static const bool value = false;
    static void check() {
        cout << typeid(T).name() << " is NOT a pointer" << endl;
    }
};

// Partial specialization for pointer types
template <typename T>
struct IsPointer<T*> {
    static const bool value = true;
    static void check() {
        cout << typeid(T*).name() << " IS a pointer to " 
             << typeid(T).name() << endl;
    }
};

// Partial specialization for const pointers
template <typename T>
struct IsPointer<const T*> {
    static const bool value = true;
    static void check() {
        cout << "const " << typeid(T*).name() << " IS a const pointer" << endl;
    }
};

// Partial specialization for volatile pointers
template <typename T>
struct IsPointer<volatile T*> {
    static const bool value = true;
    static void check() {
        cout << "volatile " << typeid(T*).name() << " IS a volatile pointer" << endl;
    }
};

// For references
template <typename T>
struct IsReference {
    static const bool value = false;
};

template <typename T>
struct IsReference<T&> {
    static const bool value = true;
};

template <typename T>
struct IsReference<T&&> {
    static const bool value = true;
};

int main() {
    IsPointer<int>::check();
    IsPointer<int*>::check();
    IsPointer<const int*>::check();
    IsPointer<volatile int*>::check();
    IsPointer<int**>::check();
    
    cout << "\nIsReference checks:" << endl;
    cout << "int is reference: " << IsReference<int>::value << endl;
    cout << "int& is reference: " << IsReference<int&>::value << endl;
    cout << "int&& is reference: " << IsReference<int&&>::value << endl;
    
    return 0;
}
```

**Output:**
```
i is NOT a pointer
Pi IS a pointer to i
const Pi IS a const pointer
volatile Pi IS a volatile pointer
PPi IS a pointer to Pi

IsReference checks:
int is reference: 0
int& is reference: 1
int&& is reference: 1
```

---

### Real-World Example: Smart Pointer Specialization

```cpp
#include <iostream>
using namespace std;

// Primary template - generic smart pointer
template <typename T>
class SmartPtr {
private:
    T* ptr_;
    
public:
    SmartPtr(T* ptr = nullptr) : ptr_(ptr) {
        cout << "Generic SmartPtr created for " << typeid(T).name() << endl;
    }
    
    ~SmartPtr() {
        delete ptr_;
        cout << "Generic SmartPtr destroyed" << endl;
    }
    
    T* operator->() { return ptr_; }
    T& operator*() { return *ptr_; }
};

// Full specialization for arrays
template <typename T>
class SmartPtr<T[]> {
private:
    T* ptr_;
    int size_;
    
public:
    SmartPtr(T* ptr = nullptr, int size = 0) : ptr_(ptr), size_(size) {
        cout << "Array SmartPtr created for " << typeid(T).name() 
             << "[" << size_ << "]" << endl;
    }
    
    ~SmartPtr() {
        delete[] ptr_;
        cout << "Array SmartPtr destroyed" << endl;
    }
    
    T& operator[](int index) { return ptr_[index]; }
};

// Full specialization for bool (optimization)
template <>
class SmartPtr<bool> {
private:
    unsigned char* ptr_;
    int bits_;
    
public:
    SmartPtr(bool* ptr = nullptr, int bits = 0) : bits_(bits) {
        // Pack booleans into bits
        cout << "Bool SmartPtr (optimized) created" << endl;
    }
    
    ~SmartPtr() {
        cout << "Bool SmartPtr destroyed" << endl;
    }
};

int main() {
    SmartPtr<int> intPtr(new int(42));
    *intPtr = 100;
    cout << "Value: " << *intPtr << endl;
    
    SmartPtr<int[]> arrPtr(new int[5], 5);
    arrPtr[0] = 10;
    arrPtr[1] = 20;
    cout << "arrPtr[0]: " << arrPtr[0] << endl;
    
    SmartPtr<bool> boolPtr(new bool[10], 10);
    
    return 0;
}
```

---

### Specialization Priority Rules

When multiple specializations match, the compiler selects the most specialized one.

```cpp
#include <iostream>
using namespace std;

template <typename T>
struct Selector {
    static void show() { cout << "Primary template" << endl; }
};

// Partial specialization for pointers
template <typename T>
struct Selector<T*> {
    static void show() { cout << "Pointer specialization" << endl; }
};

// Partial specialization for const pointers
template <typename T>
struct Selector<const T*> {
    static void show() { cout << "Const pointer specialization" << endl; }
};

// Full specialization for int*
template <>
struct Selector<int*> {
    static void show() { cout << "int* full specialization" << endl; }
};

// Full specialization for const int*
template <>
struct Selector<const int*> {
    static void show() { cout << "const int* full specialization" << endl; }
};

int main() {
    Selector<double>::show();           // Primary template
    Selector<double*>::show();          // Pointer specialization
    Selector<const double*>::show();    // Const pointer specialization
    Selector<int*>::show();             // int* full specialization
    Selector<const int*>::show();       // const int* full specialization
    
    return 0;
}
```

**Output:**
```
Primary template
Pointer specialization
Const pointer specialization
int* full specialization
const int* full specialization
```

**Priority Order (Highest to Lowest):**

```
1. Full specialization (exact match)
2. Partial specialization (pattern match)
3. Primary template (most general)
```

---

### Limitations of Function Template Partial Specialization

C++ does not allow partial specialization of function templates. Use overloading or class templates as workarounds.

```cpp
#include <iostream>
using namespace std;

// Cannot partially specialize function templates:
// template <typename T>
// void process(T* ptr) { }  // This is overloading, not partial specialization

// Workaround 1: Use overloading
template <typename T>
void process(T value) {
    cout << "Generic: " << value << endl;
}

template <typename T>
void process(T* ptr) {
    cout << "Pointer: " << *ptr << endl;
}

// Workaround 2: Use a helper class template
template <typename T>
struct Processor {
    static void execute(T value) {
        cout << "Generic processor: " << value << endl;
    }
};

template <typename T>
struct Processor<T*> {
    static void execute(T* ptr) {
        cout << "Pointer processor: " << *ptr << endl;
    }
};

template <typename T>
void processWithHelper(T value) {
    Processor<T>::execute(value);
}

int main() {
    int x = 42;
    
    process(x);      // Generic
    process(&x);     // Pointer (overload)
    
    processWithHelper(x);   // Generic processor
    processWithHelper(&x);  // Pointer processor
    
    return 0;
}
```

---

### Summary

| Concept | Key Point |
|---------|-----------|
| **Full Specialization** | Complete custom implementation for a specific type |
| **Partial Specialization** | Custom implementation for a category of types (class templates only) |
| **Function Specialization** | Available for full specialization only |
| **Priority Rules** | Compiler selects the most specialized match |
| **Common Uses** | Type traits, optimizations, container specializations |

---

### Key Takeaways

1. **Full specialization** provides type-specific behavior
2. **Partial specialization** works for patterns (pointers, arrays, const)
3. **Function templates** only support full specialization (use overloading as alternative)
4. **Priority rules** ensure the most specific match is selected
5. **Specialization** is essential for type traits and template metaprogramming
6. **Array and pointer specializations** are common in practice
7. **Specialization does not inherit** members from the primary template

---

### Next Steps

- Go to [04_Variadic_Templates.md](04_Variadic_Templates.md) to understand Variadic Templates.