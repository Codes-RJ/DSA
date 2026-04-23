# Concepts in C++ - Complete Guide

## 📖 Overview

Concepts (introduced in C++20) are a revolutionary feature that allows developers to specify requirements on template parameters. They enable clearer error messages, better code organization, and more expressive interfaces. Concepts are the foundation for "constrained templates" in modern C++.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Concept** | Named set of requirements for template arguments |
| **Constraints** | Conditions that template arguments must satisfy |
| **Requires Clause** | Specifies requirements for templates |
| **Requires Expression** | Compile-time predicate checking |
| **Abbreviated Templates** | Using `auto` with concepts for simpler syntax |

---

## 1. **Basic Concepts**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <concepts>
#include <type_traits>
using namespace std;

// Basic concept definition
template<typename T>
concept Numeric = is_arithmetic_v<T>;

// Using concept with requires clause
template<typename T>
requires Numeric<T>
T add(T a, T b) {
    return a + b;
}

// Alternative syntax (trailing requires)
template<typename T>
T multiply(T a, T b) requires Numeric<T> {
    return a * b;
}

// Using concept as template parameter
template<Numeric T>
T subtract(T a, T b) {
    return a - b;
}

// Abbreviated template syntax (C++20)
Numeric auto divide(Numeric auto a, Numeric auto b) {
    return a / b;
}

int main() {
    cout << "=== Basic Concepts ===" << endl;
    
    cout << "\n1. Numeric operations:" << endl;
    cout << "add(5, 3) = " << add(5, 3) << endl;
    cout << "multiply(4.5, 2.0) = " << multiply(4.5, 2.0) << endl;
    cout << "subtract(10, 4) = " << subtract(10, 4) << endl;
    cout << "divide(15.0, 3.0) = " << divide(15.0, 3.0) << endl;
    
    // This would cause compilation error
    // add("Hello", "World");  // Error! string is not Numeric
    
    cout << "\n2. Concept constraints prevent invalid instantiations:" << endl;
    cout << "   Only numeric types can be used with these functions" << endl;
    
    return 0;
}
```

**Output:**
```
=== Basic Concepts ===

1. Numeric operations:
add(5, 3) = 8
multiply(4.5, 2.0) = 9
subtract(10, 4) = 6
divide(15.0, 3.0) = 5

2. Concept constraints prevent invalid instantiations:
   Only numeric types can be used with these functions
```

---

## 2. **Standard Library Concepts**

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <concepts>
#include <algorithm>
using namespace std;

// Using standard library concepts
template<typename T>
requires integral<T>
T factorial(T n) {
    T result = 1;
    for (T i = 2; i <= n; ++i) {
        result *= i;
    }
    return result;
}

// Using floating_point concept
template<floating_point T>
T square_root(T x) {
    return sqrt(x);
}

// Using movable concept for efficient operations
template<movable T>
void swap_elements(T& a, T& b) {
    T temp = move(a);
    a = move(b);
    b = move(temp);
}

// Using random_access_iterator concept
template<random_access_iterator Iter>
void print_range(Iter first, Iter last) {
    for (auto it = first; it != last; ++it) {
        cout << *it << " ";
    }
    cout << endl;
}

int main() {
    cout << "=== Standard Library Concepts ===" << endl;
    
    cout << "\n1. integral concept:" << endl;
    cout << "factorial(5) = " << factorial(5) << endl;
    // cout << factorial(3.14) << endl;  // Error! double is not integral
    
    cout << "\n2. floating_point concept:" << endl;
    cout << "square_root(25.0) = " << square_root(25.0) << endl;
    // cout << square_root(25) << endl;  // Error! int is not floating_point
    
    cout << "\n3. movable concept:" << endl;
    string s1 = "Hello", s2 = "World";
    cout << "Before swap: " << s1 << ", " << s2 << endl;
    swap_elements(s1, s2);
    cout << "After swap: " << s1 << ", " << s2 << endl;
    
    cout << "\n4. random_access_iterator concept:" << endl;
    vector<int> vec = {1, 2, 3, 4, 5};
    list<int> lst = {10, 20, 30, 40, 50};
    
    print_range(vec.begin(), vec.end());  // OK - vector has random access iterators
    // print_range(lst.begin(), lst.end());  // Error! list iterators are bidirectional, not random access
    
    return 0;
}
```

---

## 3. **Custom Concepts**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <type_traits>
using namespace std;

// Concept for types that have a .size() method
template<typename T>
concept HasSize = requires(T t) {
    { t.size() } -> convertible_to<size_t>;
};

// Concept for types that can be compared
template<typename T>
concept Comparable = requires(T a, T b) {
    { a == b } -> convertible_to<bool>;
    { a < b } -> convertible_to<bool>;
};

// Concept for containers that support iteration
template<typename T>
concept Container = requires(T c) {
    typename T::value_type;
    { c.begin() } -> input_iterator;
    { c.end() } -> input_iterator;
    { c.size() } -> convertible_to<size_t>;
};

// Concept for printable types
template<typename T>
concept Printable = requires(T t, ostream& os) {
    { os << t } -> convertible_to<ostream&>;
};

// Function using HasSize concept
template<HasSize T>
void print_size(const T& container) {
    cout << "Size: " << container.size() << endl;
}

// Function using Comparable concept
template<Comparable T>
T max_value(const T& a, const T& b) {
    return a > b ? a : b;
}

// Function using Printable concept
template<Printable T>
void print(const T& value) {
    cout << value << endl;
}

// Custom container that satisfies Container concept
class MyContainer {
private:
    vector<int> data_ = {1, 2, 3, 4, 5};
    
public:
    using value_type = int;
    auto begin() const { return data_.begin(); }
    auto end() const { return data_.end(); }
    size_t size() const { return data_.size(); }
};

int main() {
    cout << "=== Custom Concepts ===" << endl;
    
    cout << "\n1. HasSize concept:" << endl;
    vector<int> vec = {1, 2, 3, 4, 5};
    string str = "Hello";
    MyContainer my;
    
    print_size(vec);
    print_size(str);
    print_size(my);
    // print_size(42);  // Error! int has no size() method
    
    cout << "\n2. Comparable concept:" << endl;
    cout << "max(10, 20) = " << max_value(10, 20) << endl;
    cout << "max(3.14, 2.71) = " << max_value(3.14, 2.71) << endl;
    cout << "max('A', 'Z') = " << max_value('A', 'Z') << endl;
    // cout << max_value("Hello", "World") << endl;  // Error! const char* not Comparable
    
    cout << "\n3. Printable concept:" << endl;
    print(42);
    print(3.14159);
    print("Hello World");
    print(string("C++ Concepts"));
    
    return 0;
}
```

---

## 4. **Compound Concepts and Requires Expressions**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

// Concept for equality comparable
template<typename T>
concept EqualityComparable = requires(T a, T b) {
    { a == b } -> convertible_to<bool>;
    { a != b } -> convertible_to<bool>;
};

// Concept for ordered types
template<typename T>
concept Ordered = requires(T a, T b) {
    { a < b } -> convertible_to<bool>;
    { a > b } -> convertible_to<bool>;
    { a <= b } -> convertible_to<bool>;
    { a >= b } -> convertible_to<bool>;
};

// Compound concept combining multiple requirements
template<typename T>
concept Sortable = EqualityComparable<T> && Ordered<T>;

// Concept with nested requirements
template<typename T>
concept Container = requires(T c) {
    typename T::value_type;
    typename T::iterator;
    typename T::const_iterator;
    { c.begin() } -> same_as<typename T::iterator>;
    { c.end() } -> same_as<typename T::iterator>;
    { c.cbegin() } -> same_as<typename T::const_iterator>;
    { c.cend() } -> same_as<typename T::const_iterator>;
    { c.size() } -> convertible_to<size_t>;
    { c.empty() } -> convertible_to<bool>;
};

// Concept with type requirements
template<typename T>
concept Numeric = requires(T a, T b) {
    requires is_arithmetic_v<T>;
    { a + b } -> same_as<T>;
    { a - b } -> same_as<T>;
    { a * b } -> same_as<T>;
    { a / b } -> same_as<T>;
};

// Function using compound concept
template<Sortable T>
T min_value(const T& a, const T& b) {
    return a < b ? a : b;
}

template<Sortable T>
void sort_pair(T& a, T& b) {
    if (a > b) {
        swap(a, b);
    }
}

template<Container C>
void print_container(const C& container) {
    for (const auto& item : container) {
        cout << item << " ";
    }
    cout << endl;
}

int main() {
    cout << "=== Compound Concepts and Requires Expressions ===" << endl;
    
    cout << "\n1. Sortable concept:" << endl;
    int x = 10, y = 5;
    cout << "min(10, 5) = " << min_value(x, y) << endl;
    
    sort_pair(x, y);
    cout << "Sorted pair: " << x << ", " << y << endl;
    
    cout << "\n2. Container concept:" << endl;
    vector<int> vec = {1, 2, 3, 4, 5};
    list<string> lst = {"apple", "banana", "cherry"};
    
    print_container(vec);
    print_container(lst);
    
    cout << "\n3. Numeric concept with requires expression:" << endl;
    auto add = [](Numeric auto a, Numeric auto b) { return a + b; };
    auto multiply = [](Numeric auto a, Numeric auto b) { return a * b; };
    
    cout << "add(5, 3) = " << add(5, 3) << endl;
    cout << "multiply(2.5, 4.0) = " << multiply(2.5, 4.0) << endl;
    
    return 0;
}
```

---

## 5. **Practical Example: Generic Algorithms with Concepts**

```cpp
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
#include <concepts>
#include <iterator>
using namespace std;

// Concept for forward iterators (simplified)
template<typename I>
concept ForwardIterator = requires(I i) {
    typename iterator_traits<I>::value_type;
    { *i } -> same_as<typename iterator_traits<I>::reference>;
    { ++i } -> same_as<I&>;
    { i++ } -> same_as<I>;
    { i == i } -> convertible_to<bool>;
    { i != i } -> convertible_to<bool>;
};

// Custom find algorithm with concept constraints
template<ForwardIterator I, typename T>
requires EqualityComparable<typename iterator_traits<I>::value_type, T>
I my_find(I first, I last, const T& value) {
    for (auto it = first; it != last; ++it) {
        if (*it == value) {
            return it;
        }
    }
    return last;
}

// Concept for random access iterators
template<typename I>
concept RandomAccessIterator = ForwardIterator<I> && requires(I i, I j, size_t n) {
    { i + n } -> same_as<I>;
    { i - n } -> same_as<I>;
    { i - j } -> same_as<ptrdiff_t>;
    { i[n] } -> same_as<typename iterator_traits<I>::reference>;
    { i < j } -> convertible_to<bool>;
};

// Binary search algorithm with concept constraints
template<RandomAccessIterator I, typename T>
requires Ordered<T> && EqualityComparable<typename iterator_traits<I>::value_type, T>
I my_binary_search(I first, I last, const T& value) {
    while (first != last) {
        I mid = first + (last - first) / 2;
        if (*mid == value) {
            return mid;
        } else if (*mid < value) {
            first = mid + 1;
        } else {
            last = mid;
        }
    }
    return last;
}

// Concept for output iterators
template<typename O, typename T>
concept OutputIterator = requires(O o, T t) {
    { *o = t } -> same_as<O&>;
    { ++o } -> same_as<O&>;
    { o++ } -> same_as<O>;
};

// Copy algorithm with concept constraints
template<ForwardIterator I, OutputIterator<typename iterator_traits<I>::value_type> O>
O my_copy(I first, I last, O out) {
    while (first != last) {
        *out = *first;
        ++first;
        ++out;
    }
    return out;
}

// Sort algorithm with concept constraints (simplified)
template<RandomAccessIterator I>
requires Ordered<typename iterator_traits<I>::value_type>
void my_sort(I first, I last) {
    // Simple bubble sort for demonstration
    for (auto i = first; i != last; ++i) {
        for (auto j = first; j != last - 1; ++j) {
            if (*j > *(j + 1)) {
                swap(*j, *(j + 1));
            }
        }
    }
}

int main() {
    cout << "=== Generic Algorithms with Concepts ===" << endl;
    
    // Test my_find
    cout << "\n1. my_find algorithm:" << endl;
    vector<int> vec = {10, 20, 30, 40, 50};
    auto it = my_find(vec.begin(), vec.end(), 30);
    if (it != vec.end()) {
        cout << "Found: " << *it << endl;
    }
    
    list<string> lst = {"apple", "banana", "cherry", "date"};
    auto lit = my_find(lst.begin(), lst.end(), string("cherry"));
    if (lit != lst.end()) {
        cout << "Found: " << *lit << endl;
    }
    
    // Test my_binary_search (requires sorted range)
    cout << "\n2. my_binary_search algorithm:" << endl;
    vector<int> sorted = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    auto bit = my_binary_search(sorted.begin(), sorted.end(), 7);
    if (bit != sorted.end()) {
        cout << "Binary search found: " << *bit << endl;
    }
    
    // Test my_copy
    cout << "\n3. my_copy algorithm:" << endl;
    vector<int> source = {1, 2, 3, 4, 5};
    vector<int> dest(5);
    my_copy(source.begin(), source.end(), dest.begin());
    
    cout << "Copied: ";
    for (int x : dest) cout << x << " ";
    cout << endl;
    
    // Test my_sort
    cout << "\n4. my_sort algorithm:" << endl;
    vector<int> unsorted = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    my_sort(unsorted.begin(), unsorted.end());
    
    cout << "Sorted: ";
    for (int x : unsorted) cout << x << " ";
    cout << endl;
    
    return 0;
}
```

---

## 📊 Concepts Summary

| Feature | Description | Use Case |
|---------|-------------|----------|
| **Basic Concept** | Named requirement set | Simple constraints |
| **Standard Concepts** | Library-provided concepts | Common constraints |
| **Custom Concept** | User-defined requirements | Domain-specific constraints |
| **Requires Clause** | Constraint specification | Template constraints |
| **Requires Expression** | Compile-time predicate | Complex conditions |

---

## ✅ Best Practices

1. **Use concepts** for clear template constraints
2. **Prefer standard library concepts** when possible
3. **Create custom concepts** for domain-specific requirements
4. **Use requires clauses** for readability
5. **Combine concepts** for complex constraints
6. **Document concepts** clearly
7. **Test concepts** with type traits

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Over-constrained** | Too restrictive | Use minimal necessary constraints |
| **Under-constrained** | Still compiles with invalid types | Add appropriate constraints |
| **Complex requires expressions** | Hard to read | Break into smaller concepts |
| **Missing includes** | Concept not found | Include `<concepts>` header |

---

## ✅ Key Takeaways

1. **Concepts** define requirements for template parameters
2. **Enable clearer error messages** when constraints fail
3. **Improve code readability** and maintainability
4. **Standard library** provides many useful concepts
5. **Custom concepts** can be created for specific domains
6. **Requires clauses** specify constraints
7. **C++20 feature** - revolutionizes template programming

---
---

## Next Step

- Go to [15_Projects_and_Applications](../15_Projects_and_Applications/README.md) to continue with making projects and practice what you learnt.