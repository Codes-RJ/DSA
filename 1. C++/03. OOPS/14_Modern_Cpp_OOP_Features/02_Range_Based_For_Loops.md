# 14_Modern_Cpp_OOP_Features/02_Range_Based_For_Loops.md

# Range-Based For Loops in C++ - Complete Guide

## 📖 Overview

Range-based for loops (also known as for-each loops) were introduced in C++11 to simplify iteration over containers and arrays. They provide a cleaner, safer, and more readable syntax compared to traditional iterator-based loops. C++17 and C++20 added further enhancements to this feature.

---

## 🎯 Key Concepts

| Feature | Version | Description |
|---------|---------|-------------|
| **Basic range-for** | C++11 | Simplified iteration over containers |
| **auto&** | C++11 | Modify elements |
| **const auto&** | C++11 | Read-only iteration |
| **Structured bindings** | C++17 | Decompose pairs/tuples |
| **Initializer** | C++20 | Range expression with initializer |

---

## 1. **Basic Range-Based For Loops**

```cpp
#include <iostream>
#include <vector>
#include <array>
#include <string>
#include <list>
#include <set>
using namespace std;

int main() {
    cout << "=== Basic Range-Based For Loops ===" << endl;
    
    // C-style array
    int arr[] = {1, 2, 3, 4, 5};
    cout << "Array: ";
    for (int x : arr) {
        cout << x << " ";
    }
    cout << endl;
    
    // Vector
    vector<string> words = {"Hello", "World", "C++"};
    cout << "Vector: ";
    for (const string& word : words) {
        cout << word << " ";
    }
    cout << endl;
    
    // List
    list<double> prices = {19.99, 29.99, 39.99};
    cout << "List: ";
    for (double price : prices) {
        cout << "$" << price << " ";
    }
    cout << endl;
    
    // Set
    set<int> numbers = {5, 2, 8, 1, 9, 3};
    cout << "Set: ";
    for (int n : numbers) {
        cout << n << " ";
    }
    cout << endl;
    
    // String
    string text = "Hello";
    cout << "String characters: ";
    for (char c : text) {
        cout << c << " ";
    }
    cout << endl;
    
    // Initializer list
    cout << "Initializer list: ";
    for (int x : {10, 20, 30, 40, 50}) {
        cout << x << " ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
=== Basic Range-Based For Loops ===
Array: 1 2 3 4 5 
Vector: Hello World C++ 
List: $19.99 $29.99 $39.99 
Set: 1 2 3 5 8 9 
String characters: H e l l o 
Initializer list: 10 20 30 40 50 
```

---

## 2. **Modifying Elements**

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    cout << "=== Modifying Elements ===" << endl;
    
    // Modifying vector elements
    vector<int> numbers = {1, 2, 3, 4, 5};
    
    cout << "Original: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Use auto& to modify
    for (auto& n : numbers) {
        n *= 2;
    }
    
    cout << "Doubled: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Modifying strings in vector
    vector<string> words = {"hello", "world", "c++"};
    
    for (auto& word : words) {
        word[0] = toupper(word[0]);
    }
    
    cout << "Capitalized: ";
    for (const auto& word : words) {
        cout << word << " ";
    }
    cout << endl;
    
    // Modifying array
    int arr[] = {10, 20, 30, 40, 50};
    
    for (auto& x : arr) {
        x += 5;
    }
    
    cout << "Incremented: ";
    for (int x : arr) cout << x << " ";
    cout << endl;
    
    return 0;
}
```

**Output:**
```
=== Modifying Elements ===
Original: 1 2 3 4 5 
Doubled: 2 4 6 8 10 
Capitalized: Hello World C++ 
Incremented: 15 25 35 45 55 
```

---

## 3. **auto with Range-Based For**

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <typeinfo>
using namespace std;

int main() {
    cout << "=== auto with Range-Based For ===" << endl;
    
    // Using auto for type deduction
    vector<int> numbers = {1, 2, 3, 4, 5};
    
    cout << "1. auto (by value): ";
    for (auto x : numbers) {
        cout << x << " ";
    }
    cout << endl;
    
    cout << "2. auto& (by reference, modifiable): ";
    for (auto& x : numbers) {
        x *= 2;
        cout << x << " ";
    }
    cout << endl;
    
    cout << "3. const auto& (read-only): ";
    for (const auto& x : numbers) {
        // x = 100;  // Error! const
        cout << x << " ";
    }
    cout << endl;
    
    // Map iteration with auto
    map<string, int> scores = {
        {"Alice", 95},
        {"Bob", 87},
        {"Charlie", 92}
    };
    
    cout << "\n4. Map iteration with auto:" << endl;
    for (const auto& pair : scores) {
        cout << "  " << pair.first << ": " << pair.second << endl;
    }
    
    // Structured bindings (C++17)
    cout << "\n5. Structured bindings (C++17):" << endl;
    for (const auto& [name, score] : scores) {
        cout << "  " << name << ": " << score << endl;
    }
    
    // Vector of pairs
    vector<pair<int, string>> pairs = {
        {1, "one"}, {2, "two"}, {3, "three"}
    };
    
    cout << "\n6. Vector of pairs:" << endl;
    for (const auto& [num, word] : pairs) {
        cout << "  " << num << " -> " << word << endl;
    }
    
    return 0;
}
```

---

## 4. **Range-Based For with Custom Containers**

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Custom container with begin/end
class IntRange {
private:
    int start_;
    int end_;
    
public:
    IntRange(int start, int end) : start_(start), end_(end) {}
    
    class Iterator {
    private:
        int current_;
        
    public:
        Iterator(int current) : current_(current) {}
        
        int operator*() const { return current_; }
        
        Iterator& operator++() {
            ++current_;
            return *this;
        }
        
        bool operator!=(const Iterator& other) const {
            return current_ != other.current_;
        }
    };
    
    Iterator begin() const { return Iterator(start_); }
    Iterator end() const { return Iterator(end_); }
};

// Container that holds another container
class Container {
private:
    vector<int> data_ = {1, 2, 3, 4, 5};
    
public:
    auto begin() { return data_.begin(); }
    auto end() { return data_.end(); }
    auto begin() const { return data_.begin(); }
    auto end() const { return data_.end(); }
};

int main() {
    cout << "=== Range-Based For with Custom Containers ===" << endl;
    
    // Custom range
    cout << "1. Custom IntRange (1 to 10): ";
    for (int x : IntRange(1, 11)) {
        cout << x << " ";
    }
    cout << endl;
    
    // Container wrapper
    Container c;
    cout << "2. Container wrapper: ";
    for (int x : c) {
        cout << x << " ";
    }
    cout << endl;
    
    // Modifying through container
    for (auto& x : c) {
        x *= 2;
    }
    cout << "3. After modification: ";
    for (int x : c) {
        cout << x << " ";
    }
    cout << endl;
    
    // Const iteration
    const Container cc;
    cout << "4. Const container: ";
    for (int x : cc) {
        cout << x << " ";
    }
    cout << endl;
    
    return 0;
}
```

---

## 5. **Performance Considerations**

```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <string>
using namespace std;
using namespace chrono;

class LargeObject {
public:
    int data[1000];
    LargeObject() {
        for (int i = 0; i < 1000; i++) data[i] = i;
    }
};

int main() {
    cout << "=== Performance Considerations ===" << endl;
    
    vector<int> numbers(10000000, 1);
    vector<LargeObject> objects(10000);
    
    // Test 1: By value (copies)
    auto start = high_resolution_clock::now();
    long long sum1 = 0;
    for (int x : numbers) {  // Copies each element (inefficient for large types)
        sum1 += x;
    }
    auto end = high_resolution_clock::now();
    auto time1 = duration_cast<milliseconds>(end - start).count();
    
    // Test 2: By reference (no copy)
    start = high_resolution_clock::now();
    long long sum2 = 0;
    for (const int& x : numbers) {  // No copy
        sum2 += x;
    }
    end = high_resolution_clock::now();
    auto time2 = duration_cast<milliseconds>(end - start).count();
    
    cout << "\n1. Performance comparison (int vector):" << endl;
    cout << "   By value: " << time1 << " ms" << endl;
    cout << "   By reference: " << time2 << " ms" << endl;
    
    // Test 3: Large objects by value vs reference
    start = high_resolution_clock::now();
    for (LargeObject obj : objects) {  // Copies each object (expensive!)
        volatile int x = obj.data[0];
    }
    end = high_resolution_clock::now();
    auto time3 = duration_cast<milliseconds>(end - start).count();
    
    start = high_resolution_clock::now();
    for (const LargeObject& obj : objects) {  // No copy
        volatile int x = obj.data[0];
    }
    end = high_resolution_clock::now();
    auto time4 = duration_cast<milliseconds>(end - start).count();
    
    cout << "\n2. Large objects performance:" << endl;
    cout << "   By value: " << time3 << " ms" << endl;
    cout << "   By const reference: " << time4 << " ms" << endl;
    cout << "   Speedup: " << (double)time3 / time4 << "x" << endl;
    
    cout << "\n3. Recommendations:" << endl;
    cout << "   ✓ Use const auto& for read-only iteration" << endl;
    cout << "   ✓ Use auto& when modifying elements" << endl;
    cout << "   ✓ Use auto for small/primitive types (int, char, etc.)" << endl;
    cout << "   ✓ Avoid copying large objects" << endl;
    
    return 0;
}
```

---

## 6. **Advanced Features (C++20)**

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <ranges>
using namespace std;

int main() {
    cout << "=== Advanced Features (C++20) ===" << endl;
    
    // Range-based for with initializer (C++20)
    cout << "\n1. Range-based for with initializer:" << endl;
    for (auto vec = vector<int>{1, 2, 3, 4, 5}; int x : vec) {
        cout << x << " ";
    }
    cout << endl;
    
    // With structured bindings
    for (auto map = map<string, int>{{"A", 1}, {"B", 2}, {"C", 3}}; 
         const auto& [key, value] : map) {
        cout << key << ":" << value << " ";
    }
    cout << endl;
    
    // C++20 ranges (requires C++20)
    #if __cplusplus >= 202002L
    cout << "\n2. C++20 ranges with views:" << endl;
    vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    auto even = numbers | views::filter([](int n) { return n % 2 == 0; });
    cout << "Even numbers: ";
    for (int n : even) {
        cout << n << " ";
    }
    cout << endl;
    
    auto squares = numbers | views::transform([](int n) { return n * n; });
    cout << "Squares: ";
    for (int n : squares) {
        cout << n << " ";
    }
    cout << endl;
    
    auto first_five = numbers | views::take(5);
    cout << "First five: ";
    for (int n : first_five) {
        cout << n << " ";
    }
    cout << endl;
    #endif
    
    return 0;
}
```

---

## 📊 Range-Based For Summary

| Syntax | Copy | Modification | Use Case |
|--------|------|--------------|----------|
| `for (auto x : c)` | Yes | No | Small/primitive types |
| `for (auto& x : c)` | No | Yes | Modifying elements |
| `for (const auto& x : c)` | No | No | Large types, read-only |
| `for (auto&& x : c)` | No | Yes | Perfect forwarding |

---

## ✅ Best Practices

1. **Use const auto&** for read-only iteration of large objects
2. **Use auto&** when you need to modify elements
3. **Use auto** for small/primitive types (int, char, etc.)
4. **Use structured bindings** for pairs/maps (C++17)
5. **Avoid copying** large objects in loop headers
6. **Use initializer** for temporary containers (C++20)

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Copying large objects** | Performance | Use const auto& |
| **Modifying while iterating** | Iterator invalidation | Be careful with containers |
| **const auto** | Can't modify | Use auto& for modification |
| **vector<bool> proxy** | Unexpected behavior | Use explicit type |

---

## ✅ Key Takeaways

1. **Range-based for** simplifies container iteration
2. **Use auto&** for modification
3. **Use const auto&** for read-only large objects
4. **Structured bindings** work with pairs/maps (C++17)
5. **Performance matters** - avoid unnecessary copies
6. **Custom containers** need begin()/end() methods
7. **C++20** adds initializers and ranges support

---