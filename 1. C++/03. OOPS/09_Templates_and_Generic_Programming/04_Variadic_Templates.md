# 04_Variadic_Templates.md

## Variadic Templates in C++

### Overview

Variadic templates (introduced in C++11) allow templates to accept an arbitrary number of template arguments. This feature enables the creation of functions and classes that can operate on any number of arguments of any types. Variadic templates are the foundation for many modern C++ features including `std::tuple`, `std::function`, perfect forwarding, and compile-time sequences.

---

### What are Variadic Templates?

Variadic templates are templates that can accept a variable number of template arguments. They use a parameter pack (denoted by `...`) to capture zero or more arguments.

**Syntax:**
```cpp
// Template parameter pack
template <typename... Args>
class Tuple { };

// Function parameter pack
template <typename... Args>
void function(Args... args) { }
```

**Key Components:**

| Component | Syntax | Description |
|-----------|--------|-------------|
| **Template Parameter Pack** | `typename... Args` | Captures multiple types |
| **Function Parameter Pack** | `Args... args` | Captures multiple values |
| **Pack Expansion** | `args...` | Expands the pack into individual elements |
| **Fold Expression (C++17)** | `(args + ...)` | Binary operation over pack |

---

### Variadic Function Templates

The most common use of variadic templates is creating functions that accept any number of arguments.

```cpp
#include <iostream>
using namespace std;

// Base case: no arguments
void print() {
    cout << endl;
}

// Variadic template: one or more arguments
template <typename T, typename... Rest>
void print(T first, Rest... rest) {
    cout << first << " ";
    print(rest...);  // Recursive expansion
}

// Alternative: using sizeof... to get pack size
template <typename... Args>
void printCount(Args... args) {
    cout << "Number of arguments: " << sizeof...(args) << endl;
    cout << "Number of types: " << sizeof...(Args) << endl;
}

// Using fold expression (C++17)
template <typename... Args>
void printFold(Args... args) {
    ((cout << args << " "), ...);  // Fold over comma operator
    cout << endl;
}

int main() {
    print(1, 2.5, "hello", 'A');
    // Output: 1 2.5 hello A
    
    printCount(10, 20, 30, 40);
    // Output: Number of arguments: 4
    
    printFold(100, 200, 300);
    // Output: 100 200 300
    
    print();  // Empty call - base case
    printFold();  // Fold with empty pack works
    
    return 0;
}
```

**Output:**
```
1 2.5 hello A 
Number of arguments: 4
Number of types: 4
100 200 300

```

---

### Pack Expansion Patterns

Parameter packs can be expanded in various ways.

```cpp
#include <iostream>
#include <tuple>
#include <utility>
using namespace std;

template <typename... Args>
void demonstrateExpansions(Args... args) {
    // 1. Simple expansion (function arguments)
    // print(args...);  // Expands to print(arg1, arg2, arg3, ...)
    
    // 2. Expression expansion
    int arr[] = { (args, 0)... };  // Creates initializer list
    // Expands to: { (arg1,0), (arg2,0), (arg3,0), ... }
    
    // 3. Function call expansion
    (cout << ... << args);  // Fold expression (left fold)
    // Expands to: ((cout << arg1) << arg2) << arg3 ...
    
    // 4. Comma operator expansion
    ((cout << args << " "), ...);
    // Expands to: (cout << arg1 << " "), (cout << arg2 << " "), ...
}

// Creating a tuple-like structure
template <typename... Types>
struct MyTuple {
    // Tuple implementation using recursive inheritance
};

// Forwarding with variadic templates
template <typename T, typename... Args>
T* createObject(Args&&... args) {
    return new T(forward<Args>(args)...);
}

// Building an array from arguments
template <typename T, typename... Args>
T* buildArray(Args... args) {
    static_assert((is_same_v<T, Args> && ...), "All arguments must have same type");
    T* arr = new T[sizeof...(args)]{args...};
    return arr;
}

int main() {
    // Perfect forwarding example
    class Widget {
    public:
        Widget(int x, double y, string z) {
            cout << "Widget created with " << x << ", " << y << ", " << z << endl;
        }
    };
    
    Widget* w = createObject<Widget>(42, 3.14, "hello");
    delete w;
    
    // Build array
    int* ints = buildArray<int>(1, 2, 3, 4, 5);
    for (int i = 0; i < 5; i++) {
        cout << ints[i] << " ";
    }
    cout << endl;
    delete[] ints;
    
    return 0;
}
```

**Output:**
```
Widget created with 42, 3.14, hello
1 2 3 4 5 
```

---

### Fold Expressions (C++17)

Fold expressions provide a concise way to apply binary operators over parameter packs.

```cpp
#include <iostream>
using namespace std;

// Unary right fold
template <typename... Args>
auto sumRight(Args... args) {
    return (args + ...);  // (arg1 + (arg2 + (arg3 + ...)))
}

// Unary left fold
template <typename... Args>
auto sumLeft(Args... args) {
    return (... + args);  // (((arg1 + arg2) + arg3) + ...)
}

// Binary fold with initial value
template <typename... Args>
auto sumWithInitial(Args... args) {
    return (0 + ... + args);  // (((0 + arg1) + arg2) + ...)
}

// All operators work with folds
template <typename... Args>
bool allTrue(Args... args) {
    return (true && ... && args);  // Logical AND over all
}

template <typename... Args>
bool anyTrue(Args... args) {
    return (false || ... || args);  // Logical OR over all
}

// Fold over comma operator (for side effects)
template <typename... Args>
void printAll(Args... args) {
    ((cout << args << " "), ...);  // Comma fold
}

// Multiple folds
template <typename... Args>
auto sumAndProduct(Args... args) {
    return make_pair((args + ...), (args * ...));
}

int main() {
    cout << "Sum (right): " << sumRight(1, 2, 3, 4) << endl;      // 10
    cout << "Sum (left): " << sumLeft(1, 2, 3, 4) << endl;        // 10
    cout << "Sum with initial: " << sumWithInitial(1, 2, 3) << endl; // 6
    
    cout << "All true: " << allTrue(true, true, true) << endl;     // 1
    cout << "All true (with false): " << allTrue(true, false, true) << endl; // 0
    cout << "Any true: " << anyTrue(false, false, true) << endl;   // 1
    
    printAll(10, 20, 30, 40);
    cout << endl;
    
    auto [sum, product] = sumAndProduct(2, 3, 4);
    cout << "Sum: " << sum << ", Product: " << product << endl;
    
    return 0;
}
```

**Output:**
```
Sum (right): 10
Sum (left): 10
Sum with initial: 6
All true: 1
All true (with false): 0
Any true: 1
10 20 30 40 
Sum: 9, Product: 24
```

---

### Variadic Class Templates

Class templates can also be variadic, enabling powerful abstractions like tuples.

```cpp
#include <iostream>
using namespace std;

// Forward declaration
template <typename... Types>
class Tuple;

// Base case: empty tuple
template <>
class Tuple<> {
public:
    void print() const { }
};

// Recursive case: tuple with head and tail
template <typename Head, typename... Tail>
class Tuple<Head, Tail...> : public Tuple<Tail...> {
private:
    Head value_;
    
public:
    Tuple(Head head, Tail... tail) 
        : Tuple<Tail...>(tail...), value_(head) { }
    
    Head head() const { return value_; }
    
    // Access by index using template recursion
    template <size_t N>
    auto get() const {
        if constexpr (N == 0) {
            return value_;
        } else {
            return Tuple<Tail...>::template get<N-1>();
        }
    }
    
    void print() const {
        cout << value_ << " ";
        Tuple<Tail...>::print();
    }
};

// Helper function for tuple creation
template <typename... Args>
Tuple<Args...> makeTuple(Args... args) {
    return Tuple<Args...>(args...);
}

int main() {
    Tuple<int, double, string> t(42, 3.14, "Hello");
    
    cout << "Tuple elements: ";
    t.print();
    cout << endl;
    
    cout << "Head: " << t.head() << endl;
    cout << "Element 0: " << t.get<0>() << endl;
    cout << "Element 1: " << t.get<1>() << endl;
    cout << "Element 2: " << t.get<2>() << endl;
    
    auto t2 = makeTuple(100, 'A', 3.14f, "World");
    cout << "Auto tuple: ";
    t2.print();
    cout << endl;
    
    return 0;
}
```

**Output:**
```
Tuple elements: 42 3.14 Hello 
Head: 42
Element 0: 42
Element 1: 3.14
Element 2: Hello
Auto tuple: 100 A 3.14 World 
```

---

### Type Traits with Variadic Templates

Variadic templates enable powerful compile-time type queries.

```cpp
#include <iostream>
#include <type_traits>
using namespace std;

// Check if all types are the same
template <typename T, typename... Rest>
struct are_all_same : public conjunction<is_same<T, Rest>...> { };

// Check if any type is pointer
template <typename... Types>
struct any_pointer : public disjunction<is_pointer<Types>...> { };

// Count number of pointers in pack
template <typename... Types>
struct count_pointers {
    static constexpr size_t value = (is_pointer_v<Types> + ... + 0);
};

// Get the first type from pack
template <typename First, typename... Rest>
struct first_type {
    using type = First;
};

// Get the last type from pack
template <typename... Types>
struct last_type;

template <typename First, typename... Rest>
struct last_type<First, Rest...> {
    using type = typename last_type<Rest...>::type;
};

template <typename Last>
struct last_type<Last> {
    using type = Last;
};

// Find index of a type in pack
template <typename T, typename... Types>
struct index_of;

template <typename T, typename First, typename... Rest>
struct index_of<T, First, Rest...> {
    static constexpr size_t value = is_same_v<T, First> ? 0 : 1 + index_of<T, Rest...>::value;
};

template <typename T>
struct index_of<T> {
    static constexpr size_t value = -1;  // Not found
};

int main() {
    cout << boolalpha;
    
    cout << "All same (int, int, int): " 
         << are_all_same<int, int, int>::value << endl;
    cout << "All same (int, double, int): " 
         << are_all_same<int, double, int>::value << endl;
    
    cout << "Any pointer (int, double*, char): " 
         << any_pointer<int, double*, char>::value << endl;
    cout << "Any pointer (int, double, char): " 
         << any_pointer<int, double, char>::value << endl;
    
    cout << "Count pointers (int, double*, char*, float): " 
         << count_pointers<int, double*, char*, float>::value << endl;
    
    using First = first_type<int, double, char>::type;
    cout << "First type: " << typeid(First).name() << endl;
    
    using Last = last_type<int, double, char>::type;
    cout << "Last type: " << typeid(Last).name() << endl;
    
    cout << "Index of double: " << index_of<double, int, double, char>::value << endl;
    cout << "Index of float (not found): " << index_of<float, int, double, char>::value << endl;
    
    return 0;
}
```

---

### Real-World Examples

#### 1. Type-Safe printf (C++11)

```cpp
#include <iostream>
using namespace std;

// Base case
void myPrintf(const char* format) {
    while (*format) {
        if (*format == '%' && *(format + 1) == '%') {
            ++format;
        }
        cout << *format++;
    }
}

// Variadic template
template <typename T, typename... Args>
void myPrintf(const char* format, T value, Args... args) {
    while (*format) {
        if (*format == '%' && *(format + 1) != '%') {
            cout << value;
            myPrintf(format + 1, args...);
            return;
        }
        cout << *format++;
    }
}

int main() {
    myPrintf("Hello, %!\n", "World");
    myPrintf("Values: %, %, %\n", 42, 3.14, "C++");
    myPrintf("% + % = %\n", 10, 20, 30);
    
    return 0;
}
```

#### 2. Maximum of Multiple Values

```cpp
#include <iostream>
using namespace std;

// Base case: single value
template <typename T>
T maxValue(T a) {
    return a;
}

// Recursive case: compare two, then rest
template <typename T, typename... Rest>
T maxValue(T first, Rest... rest) {
    T restMax = maxValue(rest...);
    return (first > restMax) ? first : restMax;
}

// C++17 fold expression version
template <typename... Args>
auto maxFold(Args... args) {
    return (args > ... > 0);  // Not exactly - need max
}

// Correct fold version for max
template <typename... Args>
auto maxFoldCorrect(Args... args) {
    return max({args...});  // Using initializer list
}

int main() {
    cout << "max(10, 20): " << maxValue(10, 20) << endl;
    cout << "max(5, 15, 25, 10): " << maxValue(5, 15, 25, 10) << endl;
    cout << "max(3.14, 2.71, 1.41): " << maxValue(3.14, 2.71, 1.41) << endl;
    
    return 0;
}
```

#### 3. Visitor Pattern with Variadic Templates

```cpp
#include <iostream>
#include <variant>
#include <vector>
using namespace std;

// Variadic visitor
template <typename... Types>
struct Visitor : Types... {
    using Types::operator()...;  // C++17
};

// Deduction guide
template <typename... Types>
Visitor(Types...) -> Visitor<Types...>;

int main() {
    using Variant = variant<int, double, string>;
    
    vector<Variant> values = {42, 3.14, "Hello"};
    
    auto visitor = Visitor{
        [](int x) { cout << "Integer: " << x << endl; },
        [](double x) { cout << "Double: " << x << endl; },
        [](const string& x) { cout << "String: " << x << endl; }
    };
    
    for (auto& v : values) {
        visit(visitor, v);
    }
    
    return 0;
}
```

---

### Summary

| Concept | Key Point |
|---------|-----------|
| **Parameter Pack** | Captures variable number of template arguments |
| **Pack Expansion** | `...` expands the pack into individual elements |
| **Recursive Expansion** | Traditional method using base case and recursion |
| **Fold Expressions (C++17)** | Apply binary operators directly to packs |
| **sizeof...** | Compile-time size of parameter pack |
| **Perfect Forwarding** | `forward<Args>(args)...` preserves value categories |

---

### Key Takeaways

1. **Variadic templates** enable functions and classes with variable arguments
2. **Parameter packs** are denoted by `...` in both template and function parameters
3. **Pack expansion** can be used in many contexts (expressions, initializers, base classes)
4. **Fold expressions (C++17)** provide concise binary operations over packs
5. **Recursive instantiation** is the traditional way to process packs
6. **sizeof...** returns the number of elements in a pack at compile time
7. **Perfect forwarding** with variadic templates enables factory functions like `make_unique`, `make_tuple`

---

### Next Steps

- Go to [05_Template_Metaprogramming.md](05_Template_Metaprogramming.md) to understand Template Metaprogramming.