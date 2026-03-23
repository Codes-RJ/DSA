# Utility Data Structures in C++

## Overview
Utility data structures are helper types that provide additional functionality for storing and manipulating data. C++ provides several utility structures: `std::pair` for storing two related values, `std::tuple` for storing multiple values, `std::optional` for optional values, `std::variant` for type-safe unions, and `std::any` for type-safe containers of any type.

## Key Characteristics

| Structure | Purpose | Elements | Type Safety | Memory Overhead |
|-----------|---------|----------|-------------|-----------------|
| pair | Store two values | 2 | Strong | Minimal |
| tuple | Store multiple values | N | Strong | Minimal |
| optional | Optional value | 0 or 1 | Strong | Small |
| variant | Type-safe union | 1 of N types | Strong | Size of largest type + index |
| any | Any type | 1 | Weak (type erasure) | Dynamic |

---

## 1. std::pair (Two-Value Container)

### Theory
`std::pair` is a simple container that stores two heterogeneous values. It's commonly used to return two values from a function, as elements in associative containers, and for building more complex data structures. Pairs are lexicographically comparable (compare first, then second).

**Use Cases:**
- Returning two values from a function
- Key-value pairs in maps
- Representing coordinates (x, y)
- Edge representation in graphs (from, to)
- Range queries (lower_bound, upper_bound results)

### All Functions and Operations

```cpp
#include <iostream>
#include <utility>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

void demonstratePair() {
    std::cout << "\n========== STD::PAIR ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default constructor (values are default-initialized)
    std::pair<int, double> p1;
    
    // Value constructor
    std::pair<int, std::string> p2(42, "Hello");
    
    // Using make_pair (C++98)
    auto p3 = std::make_pair(3.14, "Pi");
    
    // Using brace initialization (C++11)
    std::pair<int, char> p4{65, 'A'};
    
    // Copy constructor
    std::pair<int, std::string> p5(p2);
    
    // Move constructor (C++11)
    std::pair<int, std::string> p6(std::move(p2));
    
    // Structured binding (C++17)
    auto [num, str] = p3;
    std::cout << "Structured binding: " << num << ", " << str << "\n";
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::pair<std::string, int> person("Alice", 25);
    
    std::cout << "First: " << person.first << "\n";
    std::cout << "Second: " << person.second << "\n";
    
    // Using get (C++11)
    std::cout << "get<0>: " << std::get<0>(person) << "\n";
    std::cout << "get<1>: " << std::get<1>(person) << "\n";
    
    // Using structured binding (C++17)
    auto [name, age] = person;
    std::cout << "Structured binding - Name: " << name << ", Age: " << age << "\n";
    
    // ==================== MODIFYING VALUES ====================
    std::cout << "\n--- Modifying Values ---\n";
    
    std::pair<int, int> point(10, 20);
    std::cout << "Original: (" << point.first << ", " << point.second << ")\n";
    
    point.first = 30;
    point.second = 40;
    std::cout << "After modification: (" << point.first << ", " << point.second << ")\n";
    
    // Swap values
    std::pair<int, int> p7(1, 2);
    std::pair<int, int> p8(3, 4);
    p7.swap(p8);
    std::cout << "After swap - p7: (" << p7.first << ", " << p7.second 
              << "), p8: (" << p8.first << ", " << p8.second << ")\n";
    
    // ==================== COMPARISON ====================
    std::cout << "\n--- Comparison (Lexicographical) ---\n";
    
    std::pair<int, int> a(1, 2);
    std::pair<int, int> b(1, 3);
    std::pair<int, int> c(2, 1);
    
    std::cout << "a (1,2) vs b (1,3):\n";
    std::cout << "  a == b: " << (a == b ? "true" : "false") << "\n";
    std::cout << "  a < b: " << (a < b ? "true" : "false") << "\n";
    std::cout << "  a > b: " << (a > b ? "true" : "false") << "\n";
    
    std::cout << "a (1,2) vs c (2,1):\n";
    std::cout << "  a < c: " << (a < c ? "true" : "false") << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Returning Multiple Values from Function
    std::cout << "\n--- Example 1: Returning Multiple Values ---\n";
    
    auto minMax = [](const std::vector<int>& vec) -> std::pair<int, int> {
        if (vec.empty()) return {0, 0};
        int min_val = vec[0], max_val = vec[0];
        for (int v : vec) {
            if (v < min_val) min_val = v;
            if (v > max_val) max_val = v;
        }
        return {min_val, max_val};
    };
    
    std::vector<int> data = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    auto [min_val, max_val] = minMax(data);
    std::cout << "Min: " << min_val << ", Max: " << max_val << "\n";
    
    // Example 2: Map Insertion Returns Pair
    std::cout << "\n--- Example 2: Map Insertion Returns Pair ---\n";
    
    std::map<std::string, int> scores;
    auto result = scores.insert({"Alice", 95});
    
    if (result.second) {
        std::cout << "Inserted Alice with score " << result.first->second << "\n";
    } else {
        std::cout << "Alice already exists with score " << result.first->second << "\n";
    }
    
    // Example 3: Vector of Pairs
    std::cout << "\n--- Example 3: Vector of Pairs ---\n";
    
    std::vector<std::pair<std::string, int>> students = {
        {"Alice", 95}, {"Bob", 87}, {"Charlie", 92}, {"David", 88}
    };
    
    // Sort by score (second element)
    std::sort(students.begin(), students.end(),
              [](const auto& a, const auto& b) {
                  return a.second > b.second;  // Descending by score
              });
    
    std::cout << "Students sorted by score:\n";
    for (const auto& [name, score] : students) {
        std::cout << "  " << name << ": " << score << "\n";
    }
    
    // Example 4: Edge Representation in Graph
    std::cout << "\n--- Example 4: Graph Edges ---\n";
    
    struct Edge {
        int from, to, weight;
    };
    
    std::vector<std::pair<int, int>> edges = {{0, 1}, {1, 2}, {2, 3}, {3, 0}};
    
    std::cout << "Graph edges:\n";
    for (const auto& [u, v] : edges) {
        std::cout << "  " << u << " -> " << v << "\n";
    }
    
    // Example 5: Range Queries with equal_range
    std::cout << "\n--- Example 5: Range Queries ---\n";
    
    std::vector<int> sorted = {1, 2, 2, 2, 3, 4, 4, 5, 6, 7};
    auto range = std::equal_range(sorted.begin(), sorted.end(), 2);
    
    std::cout << "Range of 2: from index " << (range.first - sorted.begin())
              << " to " << (range.second - sorted.begin() - 1) << "\n";
    
    // Example 6: Coordinate System
    std::cout << "\n--- Example 6: Coordinate System ---\n";
    
    using Point = std::pair<int, int>;
    
    auto distance = [](const Point& p1, const Point& p2) {
        int dx = p1.first - p2.first;
        int dy = p1.second - p2.second;
        return std::sqrt(dx*dx + dy*dy);
    };
    
    Point origin(0, 0);
    Point target(3, 4);
    std::cout << "Distance from (0,0) to (3,4): " << distance(origin, target) << "\n";
    
    // Example 7: Creating Custom Comparators
    std::cout << "\n--- Example 7: Custom Comparator ---\n";
    
    auto compareBySecond = [](const std::pair<int, int>& a, 
                               const std::pair<int, int>& b) {
        return a.second < b.second;
    };
    
    std::vector<std::pair<int, int>> pairs = {{1, 5}, {2, 3}, {3, 8}, {4, 1}};
    std::sort(pairs.begin(), pairs.end(), compareBySecond);
    
    std::cout << "Pairs sorted by second element:\n";
    for (const auto& [first, second] : pairs) {
        std::cout << "  (" << first << ", " << second << ")\n";
    }
    
    // Example 8: Pair in Priority Queue
    std::cout << "\n--- Example 8: Priority Queue with Pairs ---\n";
    
    // Min-heap by second element
    auto cmp = [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
        return a.second > b.second;
    };
    
    std::priority_queue<std::pair<int, int>, 
                        std::vector<std::pair<int, int>>, 
                        decltype(cmp)> pq(cmp);
    
    pq.push({1, 100});
    pq.push({2, 50});
    pq.push({3, 75});
    pq.push({4, 25});
    
    std::cout << "Processing by priority (lowest second first):\n";
    while (!pq.empty()) {
        auto [id, priority] = pq.top();
        std::cout << "  ID: " << id << ", Priority: " << priority << "\n";
        pq.pop();
    }
}
```

---

## 2. std::tuple (Multiple-Value Container)

### Theory
`std::tuple` (C++11) is a generalization of `std::pair` that can store an arbitrary number of heterogeneous values. It provides a fixed-size collection of elements of different types. Tuples are useful for returning multiple values, grouping related data, and metaprogramming.

**Use Cases:**
- Returning multiple values from a function (more than 2)
- Grouping heterogeneous data without creating a struct
- Creating compile-time lists of types
- Implementing variadic template functions
- Storing multiple return values

### All Functions and Operations

```cpp
#include <iostream>
#include <tuple>
#include <string>
#include <vector>
#include <algorithm>

void demonstrateTuple() {
    std::cout << "\n========== STD::TUPLE ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default constructor (value-initialized)
    std::tuple<int, double, std::string> t1;
    
    // Value constructor
    std::tuple<int, double, std::string> t2(42, 3.14, "Hello");
    
    // Using make_tuple
    auto t3 = std::make_tuple(100, 2.718, "World");
    
    // Using brace initialization (C++11)
    std::tuple<int, char, bool> t4{65, 'A', true};
    
    // Using forward_as_tuple (creates tuple of references)
    int a = 10, b = 20;
    auto t5 = std::forward_as_tuple(a, b);
    
    // Using tie (creates tuple of references)
    int x, y;
    std::tie(x, y) = std::make_pair(30, 40);
    std::cout << "After tie: x=" << x << ", y=" << y << "\n";
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::tuple<std::string, int, double> person("Alice", 25, 3.8);
    
    // Using std::get by index (compile-time)
    std::cout << "Name: " << std::get<0>(person) << "\n";
    std::cout << "Age: " << std::get<1>(person) << "\n";
    std::cout << "GPA: " << std::get<2>(person) << "\n";
    
    // Using std::get by type (only works if types are unique)
    std::cout << "Name (by type): " << std::get<std::string>(person) << "\n";
    std::cout << "Age (by type): " << std::get<int>(person) << "\n";
    
    // Structured binding (C++17)
    auto [name, age, gpa] = person;
    std::cout << "Structured binding - Name: " << name 
              << ", Age: " << age << ", GPA: " << gpa << "\n";
    
    // ==================== MODIFYING ELEMENTS ====================
    std::cout << "\n--- Modifying Elements ---\n";
    
    std::tuple<int, int, int> triple(1, 2, 3);
    std::cout << "Original: (" << std::get<0>(triple) << ", " 
              << std::get<1>(triple) << ", " << std::get<2>(triple) << ")\n";
    
    std::get<0>(triple) = 10;
    std::get<1>(triple) = 20;
    std::get<2>(triple) = 30;
    std::cout << "After modification: (" << std::get<0>(triple) << ", " 
              << std::get<1>(triple) << ", " << std::get<2>(triple) << ")\n";
    
    // ==================== TUPLE OPERATIONS ====================
    std::cout << "\n--- Tuple Operations ---\n";
    
    // Tuple size (compile-time)
    std::cout << "Tuple size: " << std::tuple_size<decltype(person)>::value << "\n";
    
    // Tuple element types
    using FirstType = std::tuple_element<0, decltype(person)>::type;
    std::cout << "First element type: " << typeid(FirstType).name() << "\n";
    
    // Concatenating tuples (C++11)
    auto t6 = std::make_tuple(1, 2);
    auto t7 = std::make_tuple(3, 4, 5);
    auto t8 = std::tuple_cat(t6, t7);
    std::cout << "Concatenated tuple: (" << std::get<0>(t8) << ", " 
              << std::get<1>(t8) << ", " << std::get<2>(t8) << ", " 
              << std::get<3>(t8) << ", " << std::get<4>(t8) << ")\n";
    
    // ==================== COMPARISON ====================
    std::cout << "\n--- Comparison (Lexicographical) ---\n";
    
    std::tuple<int, int, int> tuple_a(1, 2, 3);
    std::tuple<int, int, int> tuple_b(1, 2, 4);
    std::tuple<int, int, int> tuple_c(1, 3, 2);
    
    std::cout << "tuple_a (1,2,3) vs tuple_b (1,2,4):\n";
    std::cout << "  a == b: " << (tuple_a == tuple_b ? "true" : "false") << "\n";
    std::cout << "  a < b: " << (tuple_a < tuple_b ? "true" : "false") << "\n";
    
    std::cout << "tuple_a (1,2,3) vs tuple_c (1,3,2):\n";
    std::cout << "  a < c: " << (tuple_a < tuple_c ? "true" : "false") << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Returning Multiple Values from Function (More than 2)
    std::cout << "\n--- Example 1: Returning Multiple Values ---\n";
    
    auto analyzeVector = [](const std::vector<int>& vec) {
        if (vec.empty()) return std::make_tuple(0, 0, 0, 0.0);
        
        int sum = 0, min_val = vec[0], max_val = vec[0];
        for (int v : vec) {
            sum += v;
            if (v < min_val) min_val = v;
            if (v > max_val) max_val = v;
        }
        double avg = static_cast<double>(sum) / vec.size();
        
        return std::make_tuple(min_val, max_val, sum, avg);
    };
    
    std::vector<int> numbers = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    auto [min_val, max_val, sum, avg] = analyzeVector(numbers);
    
    std::cout << "Vector analysis:\n";
    std::cout << "  Min: " << min_val << "\n";
    std::cout << "  Max: " << max_val << "\n";
    std::cout << "  Sum: " << sum << "\n";
    std::cout << "  Average: " << avg << "\n";
    
    // Example 2: Database Record Representation
    std::cout << "\n--- Example 2: Database Record ---\n";
    
    using Record = std::tuple<int, std::string, double, std::string>;
    
    std::vector<Record> employees = {
        {101, "Alice", 75000.0, "Engineering"},
        {102, "Bob", 85000.0, "Sales"},
        {103, "Charlie", 65000.0, "Marketing"},
        {104, "Diana", 95000.0, "Engineering"}
    };
    
    std::cout << "Employee records:\n";
    for (const auto& emp : employees) {
        std::cout << "  ID: " << std::get<0>(emp)
                  << ", Name: " << std::get<1>(emp)
                  << ", Salary: $" << std::get<2>(emp)
                  << ", Dept: " << std::get<3>(emp) << "\n";
    }
    
    // Sort employees by salary
    std::sort(employees.begin(), employees.end(),
              [](const Record& a, const Record& b) {
                  return std::get<2>(a) > std::get<2>(b);  // Descending
              });
    
    std::cout << "\nEmployees sorted by salary:\n";
    for (const auto& emp : employees) {
        std::cout << "  " << std::get<1>(emp) << ": $" << std::get<2>(emp) << "\n";
    }
    
    // Example 3: Compile-Time Tuple Iteration (C++17)
    std::cout << "\n--- Example 3: Tuple Iteration (Compile-Time) ---\n";
    
    auto printTuple = [](const auto& tuple) {
        std::apply([](const auto&... args) {
            ((std::cout << args << " "), ...);
        }, tuple);
        std::cout << "\n";
    };
    
    std::tuple<int, double, std::string, char> mixed(42, 3.14, "Hello", 'A');
    std::cout << "Tuple contents: ";
    printTuple(mixed);
    
    // Example 4: Tuple as Function Arguments
    std::cout << "\n--- Example 4: Tuple as Function Arguments ---\n";
    
    auto addThree = [](int a, int b, int c) { return a + b + c; };
    
    std::tuple<int, int, int> values(10, 20, 30);
    int result = std::apply(addThree, values);
    std::cout << "Sum of tuple (10,20,30): " << result << "\n";
    
    // Example 5: Zipping Tuples
    std::cout << "\n--- Example 5: Zipping Tuples ---\n";
    
    auto zipTuples = [](const auto& t1, const auto& t2) {
        return std::apply([&](const auto&... args1) {
            return std::apply([&](const auto&... args2) {
                return std::make_tuple(std::make_pair(args1, args2)...);
            }, t2);
        }, t1);
    };
    
    std::tuple<int, double, std::string> names(1, 2.5, "three");
    std::tuple<char, float, long> values2('A', 3.14f, 100L);
    auto zipped = zipTuples(names, values2);
    
    std::cout << "Zipped tuples:\n";
    std::apply([](const auto&... pairs) {
        ((std::cout << "  (" << pairs.first << ", " << pairs.second << ")\n"), ...);
    }, zipped);
    
    // Example 6: Tuple of References
    std::cout << "\n--- Example 6: Tuple of References ---\n";
    
    int i1 = 10, i2 = 20, i3 = 30;
    auto ref_tuple = std::tie(i1, i2, i3);
    
    std::cout << "Before: " << i1 << ", " << i2 << ", " << i3 << "\n";
    std::get<0>(ref_tuple) = 100;
    std::get<1>(ref_tuple) = 200;
    std::get<2>(ref_tuple) = 300;
    std::cout << "After modifying tuple: " << i1 << ", " << i2 << ", " << i3 << "\n";
    
    // Example 7: Creating Heterogeneous Container
    std::cout << "\n--- Example 7: Heterogeneous Container ---\n";
    
    std::vector<std::tuple<std::string, int, double>> data_points = {
        {"Point A", 1, 1.5},
        {"Point B", 2, 2.5},
        {"Point C", 3, 3.5}
    };
    
    std::cout << "Data points:\n";
    for (const auto& [label, id, value] : data_points) {
        std::cout << "  " << label << ": ID=" << id << ", Value=" << value << "\n";
    }
}
```

---

## 3. std::optional (Optional Value - C++17)

### Theory
`std::optional` (C++17) represents a value that may or may not exist. It's a type-safe alternative to using sentinel values (like -1) or pointers (nullptr) to indicate absence. Optionals prevent null pointer dereferences and make code more expressive.

**Use Cases:**
- Function return values that may fail
- Optional configuration parameters
- Caching with missing values
- Parsing where a value may be absent
- Representing nullable types

### All Functions and Operations

```cpp
#include <iostream>
#include <optional>
#include <string>
#include <vector>
#include <map>
#include <cmath>

void demonstrateOptional() {
    std::cout << "\n========== STD::OPTIONAL ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Empty optional
    std::optional<int> opt1;
    std::optional<int> opt2 = std::nullopt;
    
    // With value
    std::optional<int> opt3(42);
    std::optional<int> opt4 = 100;
    std::optional<std::string> opt5("Hello");
    
    // Using make_optional (C++17)
    auto opt6 = std::make_optional(3.14);
    
    // Copy/move constructors
    std::optional<int> opt7(opt3);
    std::optional<int> opt8(std::move(opt3));
    
    // ==================== CHECKING VALUE EXISTENCE ====================
    std::cout << "\n--- Checking Value Existence ---\n";
    
    std::optional<int> has_value(42);
    std::optional<int> no_value;
    
    // has_value() method
    std::cout << "has_value() - has: " << (has_value.has_value() ? "Yes" : "No") << "\n";
    std::cout << "has_value() - none: " << (no_value.has_value() ? "Yes" : "No") << "\n";
    
    // bool conversion operator
    if (has_value) {
        std::cout << "Bool conversion: has value\n";
    }
    
    if (!no_value) {
        std::cout << "Bool conversion: no value\n";
    }
    
    // ==================== ACCESSING VALUES ====================
    std::cout << "\n--- Accessing Values ---\n";
    
    std::optional<std::string> name("Alice");
    
    // operator* and operator->
    std::cout << "operator*: " << *name << "\n";
    std::cout << "operator->: " << name->size() << "\n";
    
    // value() - throws std::bad_optional_access if empty
    try {
        std::cout << "value(): " << name.value() << "\n";
        
        std::optional<int> empty;
        // std::cout << empty.value() << "\n";  // Throws exception
    } catch (const std::bad_optional_access& e) {
        std::cout << "Exception: " << e.what() << "\n";
    }
    
    // value_or() - provide default
    std::optional<int> maybe_number;
    int value = maybe_number.value_or(0);
    std::cout << "value_or(0): " << value << "\n";
    
    // ==================== MODIFYING VALUES ====================
    std::cout << "\n--- Modifying Values ---\n";
    
    std::optional<int> opt;
    
    // assign value
    opt = 42;
    std::cout << "After assignment: " << *opt << "\n";
    
    // emplace - construct in place
    opt.emplace(100);
    std::cout << "After emplace: " << *opt << "\n";
    
    // reset - clear value
    opt.reset();
    std::cout << "After reset - has value? " << (opt.has_value() ? "Yes" : "No") << "\n";
    
    // ==================== COMPARISON ====================
    std::cout << "\n--- Comparison ---\n";
    
    std::optional<int> o1(10);
    std::optional<int> o2(20);
    std::optional<int> o3;
    
    std::cout << "o1 (10) vs o2 (20):\n";
    std::cout << "  o1 < o2: " << (o1 < o2 ? "true" : "false") << "\n";
    std::cout << "  o1 == 10: " << (o1 == 10 ? "true" : "false") << "\n";
    
    std::cout << "o1 (10) vs o3 (nullopt):\n";
    std::cout << "  o1 < o3: " << (o1 < o3 ? "true" : "false") << "\n";
    std::cout << "  o1 == nullopt: " << (o1 == std::nullopt ? "true" : "false") << "\n";
    std::cout << "  o3 == nullopt: " << (o3 == std::nullopt ? "true" : "false") << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Safe Division
    std::cout << "\n--- Example 1: Safe Division ---\n";
    
    auto safeDivide = [](int numerator, int denominator) -> std::optional<double> {
        if (denominator == 0) {
            return std::nullopt;
        }
        return static_cast<double>(numerator) / denominator;
    };
    
    auto printDivision = [&](int a, int b) {
        auto result = safeDivide(a, b);
        if (result) {
            std::cout << a << " / " << b << " = " << *result << "\n";
        } else {
            std::cout << a << " / " << b << " = undefined (division by zero)\n";
        }
    };
    
    printDivision(10, 2);
    printDivision(10, 0);
    
    // Example 2: Finding Element in Container
    std::cout << "\n--- Example 2: Find Element ---\n";
    
    std::vector<int> vec = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    auto findElement = [&](int target) -> std::optional<int> {
        auto it = std::find(vec.begin(), vec.end(), target);
        if (it != vec.end()) {
            return *it;
        }
        return std::nullopt;
    };
    
    auto found = findElement(7);
    if (found) {
        std::cout << "Found element: " << *found << "\n";
    } else {
        std::cout << "Element not found\n";
    }
    
    found = findElement(99);
    if (!found) {
        std::cout << "Element 99 not found\n";
    }
    
    // Example 3: Configuration/Environment Variables
    std::cout << "\n--- Example 3: Configuration Lookup ---\n";
    
    std::map<std::string, std::string> config = {
        {"server", "localhost"},
        {"port", "8080"},
        {"debug", "true"}
    };
    
    auto getConfig = [&](const std::string& key) -> std::optional<std::string> {
        auto it = config.find(key);
        if (it != config.end()) {
            return it->second;
        }
        return std::nullopt;
    };
    
    auto server = getConfig("server");
    auto port = getConfig("port");
    auto timeout = getConfig("timeout");
    
    std::cout << "Server: " << server.value_or("not set") << "\n";
    std::cout << "Port: " << port.value_or("not set") << "\n";
    std::cout << "Timeout: " << timeout.value_or("default: 30s") << "\n";
    
    // Example 4: Cache with Optional
    std::cout << "\n--- Example 4: Cache Implementation ---\n";
    
    class Cache {
    private:
        std::map<std::string, int> cache;
        
    public:
        void put(const std::string& key, int value) {
            cache[key] = value;
            std::cout << "Cached: " << key << " = " << value << "\n";
        }
        
        std::optional<int> get(const std::string& key) {
            auto it = cache.find(key);
            if (it != cache.end()) {
                return it->second;
            }
            return std::nullopt;
        }
    };
    
    Cache cache;
    cache.put("user1", 1001);
    cache.put("user2", 1002);
    
    auto user1 = cache.get("user1");
    auto user3 = cache.get("user3");
    
    if (user1) std::cout << "user1: " << *user1 << "\n";
    if (!user3) std::cout << "user3: not found\n";
    
    // Example 5: Parsing with Optional
    std::cout << "\n--- Example 5: Safe Parsing ---\n";
    
    auto parseInt = [](const std::string& str) -> std::optional<int> {
        try {
            return std::stoi(str);
        } catch (...) {
            return std::nullopt;
        }
    };
    
    auto parseDouble = [](const std::string& str) -> std::optional<double> {
        try {
            return std::stod(str);
        } catch (...) {
            return std::nullopt;
        }
    };
    
    auto processInput = [&](const std::string& input) {
        if (auto num = parseInt(input)) {
            std::cout << "Parsed integer: " << *num << "\n";
        } else if (auto num = parseDouble(input)) {
            std::cout << "Parsed double: " << *num << "\n";
        } else {
            std::cout << "Cannot parse: " << input << "\n";
        }
    };
    
    processInput("42");
    processInput("3.14");
    processInput("abc");
    
    // Example 6: Chaining Operations
    std::cout << "\n--- Example 6: Chaining Operations ---\n";
    
    auto square = [](int x) -> std::optional<int> { return x * x; };
    auto invert = [](int x) -> std::optional<int> {
        if (x == 0) return std::nullopt;
        return 1 / x;
    };
    
    auto process = [&](int x) -> std::optional<double> {
        return square(x)
            .and_then(invert)
            .transform([](int y) { return static_cast<double>(y); });
    };
    
    auto result1 = process(2);   // 1/4 = 0.25
    auto result2 = process(0);   // division by zero
    
    if (result1) std::cout << "Process 2: " << *result1 << "\n";
    if (!result2) std::cout << "Process 0: failed\n";
    
    // Example 7: Optional with Custom Types
    std::cout << "\n--- Example 7: Custom Type with Optional ---\n";
    
    struct Person {
        std::string name;
        int age;
    };
    
    std::vector<Person> people = {
        {"Alice", 25}, {"Bob", 30}, {"Charlie", 35}
    };
    
    auto findPerson = [&](const std::string& name) -> std::optional<Person> {
        auto it = std::find_if(people.begin(), people.end(),
                               [&](const Person& p) { return p.name == name; });
        if (it != people.end()) {
            return *it;
        }
        return std::nullopt;
    };
    
    auto alice = findPerson("Alice");
    auto unknown = findPerson("Unknown");
    
    if (alice) {
        std::cout << "Found: " << alice->name << ", age " << alice->age << "\n";
    }
    
    if (!unknown) {
        std::cout << "Person not found\n";
    }
}
```

---

## 4. std::variant (Type-Safe Union - C++17)

### Theory
`std::variant` (C++17) is a type-safe union that can hold one value from a specified set of types. Unlike unions in C, variants know which type they currently hold and provide safe access. They are useful for representing data that can be one of several types.

**Use Cases:**
- Parsing where value can be different types
- State machines
- Error handling with multiple error types
- Heterogeneous collections
- Protocol implementations

### All Functions and Operations

```cpp
#include <iostream>
#include <variant>
#include <string>
#include <vector>
#include <cmath>
#include <iomanip>

void demonstrateVariant() {
    std::cout << "\n========== STD::VARIANT ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default constructor (first type value-initialized)
    std::variant<int, double, std::string> v1;
    
    // Value constructor
    std::variant<int, double, std::string> v2(42);
    std::variant<int, double, std::string> v3(3.14);
    std::variant<int, double, std::string> v4("Hello");
    
    // Using in_place constructors
    std::variant<int, double, std::string> v5(std::in_place_type<std::string>, "World");
    std::variant<int, double, std::string> v6(std::in_place_index<1>, 2.718);
    
    // Using make_variant (C++17)
    auto v7 = std::make_variant<int, double, std::string>(100);
    
    // ==================== CHECKING CURRENT TYPE ====================
    std::cout << "\n--- Checking Current Type ---\n";
    
    std::variant<int, double, std::string> var = 42;
    
    // index() - returns zero-based index of current type
    std::cout << "Current index: " << var.index() << "\n";
    
    // holds_alternative - check if holds specific type
    std::cout << "Holds int? " << std::holds_alternative<int>(var) << "\n";
    std::cout << "Holds double? " << std::holds_alternative<double>(var) << "\n";
    std::cout << "Holds string? " << std::holds_alternative<std::string>(var) << "\n";
    
    // ==================== ACCESSING VALUES ====================
    std::cout << "\n--- Accessing Values ---\n";
    
    std::variant<int, double, std::string> v = 3.14;
    
    // get - throws std::bad_variant_access if wrong type
    try {
        double d = std::get<double>(v);
        std::cout << "get<double>: " << d << "\n";
        
        // std::get<int>(v);  // Throws exception
    } catch (const std::bad_variant_access& e) {
        std::cout << "Exception: " << e.what() << "\n";
    }
    
    // get_if - returns pointer (nullptr if wrong type)
    if (auto* ptr = std::get_if<double>(&v)) {
        std::cout << "get_if<double>: " << *ptr << "\n";
    }
    
    if (auto* ptr = std::get_if<int>(&v)) {
        std::cout << "get_if<int>: " << *ptr << "\n";
    } else {
        std::cout << "get_if<int>: not int\n";
    }
    
    // ==================== MODIFYING VALUES ====================
    std::cout << "\n--- Modifying Values ---\n";
    
    std::variant<int, double, std::string> mv = 10;
    std::cout << "Current: " << std::get<int>(mv) << "\n";
    
    // Assignment
    mv = 3.14;
    std::cout << "After double assignment: " << std::get<double>(mv) << "\n";
    
    mv = "Hello";
    std::cout << "After string assignment: " << std::get<std::string>(mv) << "\n";
    
    // emplace - construct in place
    mv.emplace<int>(42);
    std::cout << "After emplace<int>: " << std::get<int>(mv) << "\n";
    
    mv.emplace<1>(2.718);  // emplace by index
    std::cout << "After emplace<1>: " << std::get<double>(mv) << "\n";
    
    // ==================== VISIT (Type-Safe Access) ====================
    std::cout << "\n--- Visit (Type-Safe Access) ---\n";
    
    std::variant<int, double, std::string> visitor_var = 42;
    
    auto print = [](const auto& value) {
        std::cout << "Value: " << value << "\n";
    };
    
    std::visit(print, visitor_var);
    
    visitor_var = 3.14;
    std::visit(print, visitor_var);
    
    visitor_var = "World";
    std::visit(print, visitor_var);
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Parsing JSON-like Data
    std::cout << "\n--- Example 1: JSON-like Data ---\n";
    
    using JsonValue = std::variant<int, double, std::string, bool, std::vector<JsonValue>>;
    
    auto printJson = [](const JsonValue& value, int indent = 0) {
        std::string spaces(indent, ' ');
        
        std::visit([&](const auto& val) {
            using T = std::decay_t<decltype(val)>;
            if constexpr (std::is_same_v<T, int>) {
                std::cout << spaces << val;
            } else if constexpr (std::is_same_v<T, double>) {
                std::cout << spaces << std::fixed << std::setprecision(2) << val;
            } else if constexpr (std::is_same_v<T, std::string>) {
                std::cout << spaces << "\"" << val << "\"";
            } else if constexpr (std::is_same_v<T, bool>) {
                std::cout << spaces << (val ? "true" : "false");
            } else if constexpr (std::is_same_v<T, std::vector<JsonValue>>) {
                std::cout << spaces << "[\n";
                for (size_t i = 0; i < val.size(); i++) {
                    printJson(val[i], indent + 2);
                    if (i < val.size() - 1) std::cout << ",";
                    std::cout << "\n";
                }
                std::cout << spaces << "]";
            }
        }, value);
    };
    
    JsonValue json_data = std::vector<JsonValue>{
        42,
        3.14,
        "Hello, World!",
        true,
        std::vector<JsonValue>{1, 2, 3, 4, 5}
    };
    
    std::cout << "JSON-like data:\n";
    printJson(json_data);
    std::cout << "\n";
    
    // Example 2: Calculator with Multiple Types
    std::cout << "\n--- Example 2: Calculator ---\n";
    
    using CalcValue = std::variant<int, double>;
    
    auto add = [](const CalcValue& a, const CalcValue& b) -> CalcValue {
        return std::visit([](const auto& x, const auto& y) -> CalcValue {
            return x + y;
        }, a, b);
    };
    
    auto multiply = [](const CalcValue& a, const CalcValue& b) -> CalcValue {
        return std::visit([](const auto& x, const auto& y) -> CalcValue {
            return x * y;
        }, a, b);
    };
    
    CalcValue val1 = 10;
    CalcValue val2 = 3.5;
    
    auto sum = add(val1, val2);
    auto product = multiply(val1, val2);
    
    std::cout << "10 + 3.5 = ";
    std::visit([](const auto& v) { std::cout << v; }, sum);
    std::cout << "\n";
    
    std::cout << "10 * 3.5 = ";
    std::visit([](const auto& v) { std::cout << v; }, product);
    std::cout << "\n";
    
    // Example 3: State Machine
    std::cout << "\n--- Example 3: State Machine ---\n";
    
    struct Idle {};
    struct Running { int progress; };
    struct Paused { int elapsed; };
    struct Stopped { int final_result; };
    
    using State = std::variant<Idle, Running, Paused, Stopped>;
    
    class StateMachine {
    private:
        State state = Idle{};
        
    public:
        void start() {
            state = Running{0};
            std::cout << "Started\n";
        }
        
        void update(int step) {
            if (auto* running = std::get_if<Running>(&state)) {
                running->progress += step;
                std::cout << "Progress: " << running->progress << "\n";
                if (running->progress >= 100) {
                    state = Stopped{running->progress};
                    std::cout << "Completed!\n";
                }
            }
        }
        
        void pause() {
            if (auto* running = std::get_if<Running>(&state)) {
                state = Paused{running->progress};
                std::cout << "Paused at " << running->progress << "\n";
            }
        }
        
        void resume() {
            if (auto* paused = std::get_if<Paused>(&state)) {
                state = Running{paused->elapsed};
                std::cout << "Resumed from " << paused->elapsed << "\n";
            }
        }
        
        void status() {
            std::visit([](const auto& s) {
                using T = std::decay_t<decltype(s)>;
                if constexpr (std::is_same_v<T, Idle>) {
                    std::cout << "State: Idle\n";
                } else if constexpr (std::is_same_v<T, Running>) {
                    std::cout << "State: Running (progress: " << s.progress << ")\n";
                } else if constexpr (std::is_same_v<T, Paused>) {
                    std::cout << "State: Paused (elapsed: " << s.elapsed << ")\n";
                } else if constexpr (std::is_same_v<T, Stopped>) {
                    std::cout << "State: Stopped (final: " << s.final_result << ")\n";
                }
            }, state);
        }
    };
    
    StateMachine sm;
    sm.status();
    sm.start();
    sm.update(30);
    sm.update(40);
    sm.pause();
    sm.status();
    sm.resume();
    sm.update(50);
    sm.status();
    
    // Example 4: Error Handling
    std::cout << "\n--- Example 4: Error Handling ---\n";
    
    struct Success { std::string message; };
    struct Warning { std::string message; int code; };
    struct Error { std::string message; int code; };
    
    using Result = std::variant<Success, Warning, Error>;
    
    auto process = [](int value) -> Result {
        if (value > 0 && value < 100) {
            return Success{"Valid input"};
        } else if (value >= 100) {
            return Warning{"Value too high", 1001};
        } else {
            return Error{"Invalid input", 1002};
        }
    };
    
    auto handleResult = [](const Result& result) {
        std::visit([](const auto& res) {
            using T = std::decay_t<decltype(res)>;
            if constexpr (std::is_same_v<T, Success>) {
                std::cout << "✓ " << res.message << "\n";
            } else if constexpr (std::is_same_v<T, Warning>) {
                std::cout << "⚠ " << res.message << " (Code: " << res.code << ")\n";
            } else if constexpr (std::is_same_v<T, Error>) {
                std::cout << "✗ " << res.message << " (Code: " << res.code << ")\n";
            }
        }, result);
    };
    
    handleResult(process(50));
    handleResult(process(150));
    handleResult(process(-5));
    
    // Example 5: Heterogeneous Collection
    std::cout << "\n--- Example 5: Heterogeneous Collection ---\n";
    
    using Data = std::variant<int, double, std::string>;
    std::vector<Data> mixed_data = {42, 3.14, "Hello", 100, 2.718, "World"};
    
    std::cout << "Mixed data collection:\n";
    for (const auto& item : mixed_data) {
        std::visit([](const auto& value) {
            std::cout << "  " << value << "\n";
        }, item);
    }
    
    // Example 6: Summing Variants
    std::cout << "\n--- Example 6: Summing Variants ---\n";
    
    auto sum = 0.0;
    for (const auto& item : mixed_data) {
        std::visit([&](const auto& value) {
            using T = std::decay_t<decltype(value)>;
            if constexpr (std::is_arithmetic_v<T>) {
                sum += static_cast<double>(value);
            }
        }, item);
    }
    std::cout << "Sum of numeric values: " << sum << "\n";
}
```

---

## 5. std::any (Type-Safe Any Type - C++17)

### Theory
`std::any` (C++17) is a type-safe container that can hold a single value of any type. Unlike `std::variant`, which has a fixed set of types, `any` can hold any type. It uses type erasure and requires runtime type checking.

**Use Cases:**
- Generic containers that can hold any type
- Plugin systems
- Configuration systems
- Implementing dynamic typing
- Storing values when type is not known at compile time

### All Functions and Operations

```cpp
#include <iostream>
#include <any>
#include <string>
#include <vector>
#include <map>

void demonstrateAny() {
    std::cout << "\n========== STD::ANY ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default constructor (empty)
    std::any a1;
    
    // With value
    std::any a2 = 42;
    std::any a3 = 3.14;
    std::any a4 = std::string("Hello");
    std::any a5 = "World";  // const char*
    
    // Copy constructor
    std::any a6(a2);
    
    // Move constructor
    std::any a7(std::move(a2));
    
    // Using in_place constructor
    std::any a8(std::in_place_type<std::string>, "Direct");
    
    // Using make_any (C++17)
    auto a9 = std::make_any<int>(100);
    
    // ==================== CHECKING VALUE EXISTENCE ====================
    std::cout << "\n--- Checking Value Existence ---\n";
    
    std::any has_value(42);
    std::any empty;
    
    std::cout << "has_value has value? " << (has_value.has_value() ? "Yes" : "No") << "\n";
    std::cout << "empty has value? " << (empty.has_value() ? "Yes" : "No") << "\n";
    
    // ==================== ACCESSING VALUES ====================
    std::cout << "\n--- Accessing Values ---\n";
    
    std::any any_val = 42;
    
    // type() - returns type_info of stored value
    std::cout << "Type: " << any_val.type().name() << "\n";
    
    // any_cast - safe access (throws if wrong type)
    try {
        int i = std::any_cast<int>(any_val);
        std::cout << "any_cast<int>: " << i << "\n";
        
        // std::any_cast<double>(any_val);  // Throws exception
    } catch (const std::bad_any_cast& e) {
        std::cout << "Exception: " << e.what() << "\n";
    }
    
    // any_cast with pointer (returns nullptr if wrong type)
    if (int* ptr = std::any_cast<int>(&any_val)) {
        std::cout << "any_cast<int*>: " << *ptr << "\n";
    }
    
    if (double* ptr = std::any_cast<double>(&any_val)) {
        std::cout << "any_cast<double*>: " << *ptr << "\n";
    } else {
        std::cout << "any_cast<double*>: nullptr\n";
    }
    
    // ==================== MODIFYING VALUES ====================
    std::cout << "\n--- Modifying Values ---\n";
    
    std::any mv;
    
    // assignment
    mv = 42;
    std::cout << "After int assignment: " << std::any_cast<int>(mv) << "\n";
    
    mv = 3.14;
    std::cout << "After double assignment: " << std::any_cast<double>(mv) << "\n";
    
    mv = std::string("Hello");
    std::cout << "After string assignment: " << std::any_cast<std::string>(mv) << "\n";
    
    // emplace - construct in place
    mv.emplace<int>(100);
    std::cout << "After emplace<int>: " << std::any_cast<int>(mv) << "\n";
    
    // reset - clear value
    mv.reset();
    std::cout << "After reset - has value? " << (mv.has_value() ? "Yes" : "No") << "\n";
    
    // ==================== SWAPPING ====================
    std::cout << "\n--- Swapping ---\n";
    
    std::any swap1 = 100;
    std::any swap2 = std::string("Hello");
    
    swap1.swap(swap2);
    std::cout << "After swap - swap1: " << std::any_cast<std::string>(swap1) << "\n";
    std::cout << "After swap - swap2: " << std::any_cast<int>(swap2) << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Configuration System
    std::cout << "\n--- Example 1: Configuration System ---\n";
    
    class Config {
    private:
        std::map<std::string, std::any> settings;
        
    public:
        template<typename T>
        void set(const std::string& key, T value) {
            settings[key] = value;
        }
        
        template<typename T>
        T get(const std::string& key, const T& default_value = T{}) const {
            auto it = settings.find(key);
            if (it != settings.end() && it->second.type() == typeid(T)) {
                return std::any_cast<T>(it->second);
            }
            return default_value;
        }
        
        void print() const {
            for (const auto& [key, value] : settings) {
                std::cout << "  " << key << ": ";
                if (value.type() == typeid(int)) {
                    std::cout << std::any_cast<int>(value);
                } else if (value.type() == typeid(double)) {
                    std::cout << std::any_cast<double>(value);
                } else if (value.type() == typeid(std::string)) {
                    std::cout << std::any_cast<std::string>(value);
                } else if (value.type() == typeid(bool)) {
                    std::cout << (std::any_cast<bool>(value) ? "true" : "false");
                } else {
                    std::cout << "unknown type";
                }
                std::cout << "\n";
            }
        }
    };
    
    Config config;
    config.set("port", 8080);
    config.set("host", "localhost");
    config.set("debug", true);
    config.set("timeout", 30.5);
    
    std::cout << "Configuration:\n";
    config.print();
    
    std::cout << "\nRetrieved values:\n";
    std::cout << "  port: " << config.get<int>("port") << "\n";
    std::cout << "  host: " << config.get<std::string>("host") << "\n";
    std::cout << "  debug: " << config.get<bool>("debug") << "\n";
    std::cout << "  timeout: " << config.get<double>("timeout") << "\n";
    std::cout << "  missing: " << config.get<std::string>("missing", "default") << "\n";
    
    // Example 2: Heterogeneous Container
    std::cout << "\n--- Example 2: Heterogeneous Container ---\n";
    
    std::vector<std::any> container;
    container.push_back(42);
    container.push_back(3.14);
    container.push_back(std::string("Hello"));
    container.push_back(true);
    container.push_back('X');
    
    std::cout << "Container contents:\n";
    for (const auto& item : container) {
        if (item.type() == typeid(int)) {
            std::cout << "  int: " << std::any_cast<int>(item) << "\n";
        } else if (item.type() == typeid(double)) {
            std::cout << "  double: " << std::any_cast<double>(item) << "\n";
        } else if (item.type() == typeid(std::string)) {
            std::cout << "  string: " << std::any_cast<std::string>(item) << "\n";
        } else if (item.type() == typeid(bool)) {
            std::cout << "  bool: " << (std::any_cast<bool>(item) ? "true" : "false") << "\n";
        } else if (item.type() == typeid(char)) {
            std::cout << "  char: " << std::any_cast<char>(item) << "\n";
        }
    }
    
    // Example 3: Event System
    std::cout << "\n--- Example 3: Event System ---\n";
    
    using EventHandler = std::function<void(const std::any&)>;
    std::map<std::string, std::vector<EventHandler>> event_handlers;
    
    auto registerHandler = [&](const std::string& event, EventHandler handler) {
        event_handlers[event].push_back(handler);
    };
    
    auto emitEvent = [&](const std::string& event, const std::any& data) {
        std::cout << "Emitting event: " << event << "\n";
        for (const auto& handler : event_handlers[event]) {
            handler(data);
        }
    };
    
    registerHandler("integer", [](const std::any& data) {
        if (data.type() == typeid(int)) {
            std::cout << "  Handler received int: " << std::any_cast<int>(data) << "\n";
        }
    });
    
    registerHandler("string", [](const std::any& data) {
        if (data.type() == typeid(std::string)) {
            std::cout << "  Handler received string: " << std::any_cast<std::string>(data) << "\n";
        }
    });
    
    registerHandler("any", [](const std::any& data) {
        std::cout << "  Universal handler: ";
        if (data.type() == typeid(int)) {
            std::cout << "int=" << std::any_cast<int>(data);
        } else if (data.type() == typeid(std::string)) {
            std::cout << "string=" << std::any_cast<std::string>(data);
        }
        std::cout << "\n";
    });
    
    emitEvent("integer", 42);
    emitEvent("string", std::string("Hello"));
    emitEvent("integer", 100);
    emitEvent("any", 3.14);
    
    // Example 4: Type-Safe Print Function
    std::cout << "\n--- Example 4: Type-Safe Print ---\n";
    
    auto safePrint = [](const std::any& value) {
        if (value.type() == typeid(int)) {
            std::cout << std::any_cast<int>(value);
        } else if (value.type() == typeid(double)) {
            std::cout << std::any_cast<double>(value);
        } else if (value.type() == typeid(std::string)) {
            std::cout << std::any_cast<std::string>(value);
        } else if (value.type() == typeid(const char*)) {
            std::cout << std::any_cast<const char*>(value);
        } else if (value.type() == typeid(bool)) {
            std::cout << (std::any_cast<bool>(value) ? "true" : "false");
        } else {
            std::cout << "unknown type";
        }
    };
    
    std::cout << "Type-safe printing:\n";
    safePrint(42);
    std::cout << "\n";
    safePrint(3.14159);
    std::cout << "\n";
    safePrint(std::string("Hello"));
    std::cout << "\n";
    safePrint(true);
    std::cout << "\n";
    
    // Example 5: Any with Custom Types
    std::cout << "\n--- Example 5: Custom Type with Any ---\n";
    
    struct Point {
        int x, y;
        Point(int x, int y) : x(x), y(y) {}
    };
    
    std::any custom = Point(10, 20);
    
    if (custom.type() == typeid(Point)) {
        Point& p = std::any_cast<Point&>(custom);
        std::cout << "Custom point: (" << p.x << ", " << p.y << ")\n";
    }
    
    // Example 6: Performance Consideration
    std::cout << "\n--- Example 6: Performance Note ---\n";
    
    std::any small = 42;
    std::any large = std::vector<int>(1000000);
    
    std::cout << "Small type: " << small.type().name() << "\n";
    std::cout << "Large type: " << large.type().name() << "\n";
    std::cout << "Note: std::any uses dynamic memory for large objects\n";
    
    // Example 7: nullptr Handling
    std::cout << "\n--- Example 7: nullptr Handling ---\n";
    
    std::any null_any;
    std::any ptr_any = nullptr;
    
    std::cout << "Empty any has value? " << null_any.has_value() << "\n";
    std::cout << "nullptr any has value? " << ptr_any.has_value() << "\n";
    
    if (ptr_any.type() == typeid(std::nullptr_t)) {
        std::cout << "Stored nullptr\n";
    }
}
```

---

## Performance Summary

| Structure | Construction | Copy | Move | Access | Memory |
|-----------|-------------|------|------|--------|--------|
| pair | O(1) | O(1) | O(1) | O(1) | Stack |
| tuple | O(1) | O(1) | O(1) | O(1) | Stack |
| optional | O(1) | O(1) | O(1) | O(1) | Stack |
| variant | O(1) | O(1) | O(1) | O(1) | Stack + index |
| any | O(1) | O(n)* | O(1) | O(1) | Stack/Heap |

*Copy of any requires copying the stored object (size-dependent)

---

## Best Practices

1. **Use `pair` for two values** - Simple and efficient
2. **Use `tuple` for more than two values** - When creating a struct is overkill
3. **Use `optional` for nullable values** - More expressive than sentinel values
4. **Use `variant` for type-safe unions** - When value can be one of several types
5. **Use `any` for truly unknown types** - When type is only known at runtime
6. **Prefer structured bindings (C++17)** - Cleaner code with tuples and pairs
7. **Use `std::visit` with variants** - Type-safe pattern matching
8. **Check `has_value()` before accessing optional** - Avoid exceptions
9. **Use `value_or()` for defaults** - Cleaner than if/else
10. **Use `emplace()` for in-place construction** - More efficient

---

## Common Pitfalls

1. **Using `std::get` with wrong type** - Throws `std::bad_variant_access`
2. **Accessing empty optional** - Undefined behavior with `*` or `->`
3. **Storing large objects in `any`** - May cause heap allocations
4. **Using `any_cast` with wrong type** - Throws `std::bad_any_cast`
5. **Assuming tuple types are ordered** - They are ordered lexicographically
6. **Forgetting `std::tie` for unpacking** - Use structured binding in C++17
7. **Not handling variant visitation exhaustively** - Use `std::visit` with generic lambda
