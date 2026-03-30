# auto and decltype in C++ - Complete Guide

## 📖 Overview

`auto` and `decltype` are type inference features introduced in C++11 that allow the compiler to deduce types automatically. `auto` deduces the type of a variable from its initializer, while `decltype` deduces the type of an expression. These features reduce code verbosity, improve maintainability, and are essential for modern C++ programming.

---

## 🎯 Key Concepts

| Feature | Purpose | Syntax |
|---------|---------|--------|
| **auto** | Type deduction from initializer | `auto var = expression;` |
| **decltype** | Type deduction from expression | `decltype(expression) var;` |
| **auto&** | Reference deduction | `auto& var = expression;` |
| **const auto** | Const type deduction | `const auto var = expression;` |
| **decltype(auto)** | Perfect forwarding | `decltype(auto) var = expression;` |

---

## 1. **Basic auto Usage**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <typeinfo>
using namespace std;

class Widget {
public:
    int value = 42;
};

int add(int a, int b) {
    return a + b;
}

int main() {
    cout << "=== Basic auto Usage ===" << endl;
    
    // Basic type deduction
    auto i = 42;           // int
    auto d = 3.14;         // double
    auto b = true;         // bool
    auto c = 'A';          // char
    auto s = "Hello";      // const char*
    auto str = string("World");  // std::string
    
    cout << "Type of i: " << typeid(i).name() << endl;
    cout << "Type of d: " << typeid(d).name() << endl;
    cout << "Type of b: " << typeid(b).name() << endl;
    cout << "Type of c: " << typeid(c).name() << endl;
    cout << "Type of s: " << typeid(s).name() << endl;
    cout << "Type of str: " << typeid(str).name() << endl;
    
    // auto with complex types
    vector<int> numbers = {1, 2, 3, 4, 5};
    auto it = numbers.begin();  // vector<int>::iterator
    cout << "First element: " << *it << endl;
    
    // auto with function return
    auto result = add(10, 20);
    cout << "add(10, 20) = " << result << endl;
    
    // auto with pointer
    int x = 100;
    auto ptr = &x;  // int*
    *ptr = 200;
    cout << "x = " << x << endl;
    
    // auto with reference
    auto& ref = x;  // int&
    ref = 300;
    cout << "x = " << x << endl;
    
    // const auto
    const auto cx = x;
    // cx = 400;  // Error! cx is const
    
    return 0;
}
```

**Output:**
```
=== Basic auto Usage ===
Type of i: i
Type of d: d
Type of b: b
Type of c: c
Type of s: PKc
Type of str: NSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
First element: 1
add(10, 20) = 30
x = 300
x = 300
```

---

## 2. **auto with Containers and Iterators**

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
using namespace std;

int main() {
    cout << "=== auto with Containers and Iterators ===" << endl;
    
    // Vector iteration
    vector<int> vec = {10, 20, 30, 40, 50};
    
    cout << "\n1. Vector iteration:" << endl;
    for (auto it = vec.begin(); it != vec.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;
    
    // Range-based for with auto
    for (const auto& elem : vec) {
        cout << elem << " ";
    }
    cout << endl;
    
    // Modifying elements
    for (auto& elem : vec) {
        elem *= 2;
    }
    cout << "Doubled: ";
    for (auto elem : vec) cout << elem << " ";
    cout << endl;
    
    // Map iteration
    map<string, int> scores = {
        {"Alice", 95},
        {"Bob", 87},
        {"Charlie", 92}
    };
    
    cout << "\n2. Map iteration:" << endl;
    for (auto it = scores.begin(); it != scores.end(); ++it) {
        cout << it->first << ": " << it->second << endl;
    }
    
    // Structured bindings with auto (C++17)
    cout << "\n3. Structured bindings:" << endl;
    for (const auto& [name, score] : scores) {
        cout << name << ": " << score << endl;
    }
    
    // Set iteration
    set<int> numbers = {5, 2, 8, 1, 9, 3};
    cout << "\n4. Set iteration:" << endl;
    for (auto x : numbers) {
        cout << x << " ";
    }
    cout << endl;
    
    // Unordered map
    unordered_map<string, int> umap = {{"one", 1}, {"two", 2}, {"three", 3}};
    cout << "\n5. Unordered map:" << endl;
    for (const auto& pair : umap) {
        cout << pair.first << ": " << pair.second << endl;
    }
    
    return 0;
}
```

---

## 3. **auto with Templates**

```cpp
#include <iostream>
#include <string>
#include <type_traits>
using namespace std;

// Function with auto return type (C++14)
auto add(int a, int b) {
    return a + b;
}

// Function with trailing return type
auto multiply(int a, int b) -> int {
    return a * b;
}

// Generic lambda (C++14)
auto generic_lambda = [](auto a, auto b) { return a + b; };

// auto in template parameters (C++17)
template<auto N>
struct Value {
    static constexpr auto value = N;
};

// decltype with auto
template<typename T, typename U>
auto add_template(T a, U b) -> decltype(a + b) {
    return a + b;
}

int main() {
    cout << "=== auto with Templates ===" << endl;
    
    // auto return type
    cout << "add(5, 3) = " << add(5, 3) << endl;
    cout << "multiply(5, 3) = " << multiply(5, 3) << endl;
    
    // Generic lambda
    cout << "generic_lambda(5, 3) = " << generic_lambda(5, 3) << endl;
    cout << "generic_lambda(3.14, 2.71) = " << generic_lambda(3.14, 2.71) << endl;
    cout << "generic_lambda(string(\"Hello\"), string(\" World\")) = " 
         << generic_lambda(string("Hello"), string(" World")) << endl;
    
    // Template auto parameter
    Value<42> v;
    cout << "Value<42>::value = " << v.value << endl;
    
    // decltype with auto in template
    cout << "add_template(5, 3.14) = " << add_template(5, 3.14) << endl;
    
    // auto with decltype for perfect forwarding
    auto&& forwarder = [](auto&& arg) -> decltype(auto) {
        return std::forward<decltype(arg)>(arg);
    };
    
    int x = 10;
    forwarder(x) = 20;
    cout << "x after forwarding: " << x << endl;
    
    return 0;
}
```

---

## 4. **decltype and decltype(auto)**

```cpp
#include <iostream>
#include <string>
#include <type_traits>
using namespace std;

class Container {
private:
    int data_[10];
    
public:
    int& operator[](size_t index) { return data_[index]; }
    const int& operator[](size_t index) const { return data_[index]; }
    
    decltype(auto) get(size_t index) {
        return data_[index];
    }
};

int add(int a, int b) { return a + b; }
int& getReference(int& x) { return x; }
const int& getConstReference(const int& x) { return x; }

int main() {
    cout << "=== decltype and decltype(auto) ===" << endl;
    
    // Basic decltype
    int x = 42;
    const int cx = x;
    int& rx = x;
    const int& crx = x;
    
    cout << "decltype(x): " << typeid(decltype(x)).name() << endl;
    cout << "decltype(cx): " << typeid(decltype(cx)).name() << endl;
    cout << "decltype(rx): " << typeid(decltype(rx)).name() << endl;
    cout << "decltype(crx): " << typeid(decltype(crx)).name() << endl;
    
    // decltype with parentheses
    cout << "decltype((x)): " << typeid(decltype((x))).name() << endl;  // int&
    
    // decltype with function calls
    cout << "decltype(add(5, 3)): " << typeid(decltype(add(5, 3))).name() << endl;
    
    // decltype(auto)
    int y = 100;
    decltype(auto) result1 = getReference(y);  // int&
    decltype(auto) result2 = getConstReference(y);  // const int&
    
    result1 = 200;
    cout << "y after modification: " << y << endl;
    
    // Container with decltype(auto)
    Container c;
    c[0] = 42;
    auto val1 = c.get(0);    // int (by value)
    decltype(auto) val2 = c.get(0);  // int&
    val2 = 100;
    cout << "c[0] after modification: " << c[0] << endl;
    
    // decltype with lambda (C++14)
    auto lambda = [](int a, int b) -> decltype(a + b) { return a + b; };
    cout << "lambda(5, 3) = " << lambda(5, 3) << endl;
    
    return 0;
}
```

---

## 5. **auto Best Practices and Pitfalls**

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <type_traits>
using namespace std;

class Widget {
public:
    int value = 42;
};

vector<bool> flags = {true, false, true, false};

int main() {
    cout << "=== auto Best Practices and Pitfalls ===" << endl;
    
    cout << "\n1. GOOD: Use auto for complex types:" << endl;
    vector<string> words = {"apple", "banana", "cherry"};
    for (auto it = words.begin(); it != words.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;
    
    cout << "\n2. GOOD: Use auto for lambda expressions:" << endl;
    auto cmp = [](int a, int b) { return a > b; };
    cout << "cmp(5, 3) = " << cmp(5, 3) << endl;
    
    cout << "\n3. PITFALL: vector<bool> proxy problem:" << endl;
    // auto flag = flags[0];  // auto deduces vector<bool>::reference (proxy)
    // flag = !flag;  // Modifies proxy, not original?
    
    bool flag = flags[0];  // Better: explicit type
    cout << "flag = " << flag << endl;
    
    cout << "\n4. PITFALL: auto with initializer_list:" << endl;
    auto x = {1, 2, 3};  // std::initializer_list<int>
    // auto y = 1, 2, 3;  // Error! Can't deduce multiple expressions
    
    cout << "\n5. GOOD: Use const auto& for read-only iteration:" << endl;
    for (const auto& word : words) {
        cout << word << " ";
    }
    cout << endl;
    
    cout << "\n6. GOOD: Use auto& for modification:" << endl;
    for (auto& word : words) {
        word[0] = toupper(word[0]);
    }
    for (const auto& word : words) {
        cout << word << " ";
    }
    cout << endl;
    
    cout << "\n7. PITFALL: auto drops references and const:" << endl;
    int value = 42;
    const int& cref = value;
    auto a = cref;      // int (const and reference dropped)
    auto& b = cref;     // const int& (preserved)
    
    cout << "typeid(a).name(): " << typeid(a).name() << endl;
    cout << "typeid(b).name(): " << typeid(b).name() << endl;
    
    cout << "\n8. GOOD: Use decltype(auto) to preserve references:" << endl;
    decltype(auto) c = cref;  // const int&
    
    return 0;
}
```

---

## 📊 auto and decltype Summary

| Feature | Deduction | Use Case |
|---------|-----------|----------|
| **auto** | Value type | Local variables, iterators |
| **auto&** | Lvalue reference | Modifying original |
| **const auto&** | Const reference | Read-only access |
| **auto&&** | Universal reference | Perfect forwarding |
| **decltype** | Exact type | Templates, trailing returns |
| **decltype(auto)** | Perfect forwarding | Preserving reference/const |

---

## ✅ Best Practices

1. **Use auto** for complex types (iterators, lambdas)
2. **Use const auto&** for read-only iteration
3. **Use auto&** when you need to modify
4. **Be careful** with vector<bool> and proxy types
5. **Use decltype(auto)** for perfect forwarding
6. **Don't overuse auto** for simple types where type is obvious
7. **Use auto** with structured bindings (C++17)

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Proxy types** | vector<bool> reference | Use explicit type |
| **Dropping const** | auto discards const | Use const auto& |
| **Dropping reference** | auto discards & | Use auto& or decltype(auto) |
| **Initializer list** | auto deduces initializer_list | Be explicit |

---

## ✅ Key Takeaways

1. **auto** deduces type from initializer
2. **decltype** deduces type from expression
3. **auto** drops const and references by default
4. **auto&** preserves references
5. **const auto&** is safe for read-only iteration
6. **decltype(auto)** perfect forwarding
7. **Use auto** to reduce code verbosity
8. **Be aware** of pitfalls with proxy types

---