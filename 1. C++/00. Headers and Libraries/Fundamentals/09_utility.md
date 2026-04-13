# 09_utility.md - Generic Helper Utilities

The `utility` header contains fundamental utility components used throughout the C++ standard library. It provides essential tools for working with pairs, moving objects, and generic programming.

## 📖 Overview

`utility` is a core header that provides basic building blocks for C++ programming, including `std::pair`, move semantics utilities, and various helper functions. These components are fundamental to modern C++ programming.

## 🎯 Key Components

1. **std::pair** - Two-element tuple
2. **Move Semantics** - std::move, std::forward
3. **Swap Operations** - std::swap, std::exchange
4. **Relational Operators** - Comparison helpers
5. **Integer Sequences** - Compile-time sequences

## 🔧 std::pair - Two-Element Container

### Basic Usage
```cpp
#include <iostream>
#include <utility>
#include <string>
#include <vector>

int main() {
    // Different ways to create pairs
    std::pair<int, std::string> p1 = {42, "Answer"};
    auto p2 = std::make_pair(3.14, "Pi");
    std::pair p3(100, "Hundred");  // CTAD (C++17)
    
    // Access elements
    std::cout << "First: " << p1.first << ", Second: " << p1.second << std::endl;
    
    // Structured bindings (C++17)
    auto [key, value] = p2;
    std::cout << "Key: " << key << ", Value: " << value << std::endl;
    
    return 0;
}
```

### Pair Operations
```cpp
void demonstratePairOperations() {
    std::pair<int, std::string> p1 = {1, "First"};
    std::pair<int, std::string> p2 = {2, "Second"};
    
    // Assignment
    p1 = p2;
    
    // Comparison (lexicographical)
    if (p1 == p2) {
        std::cout << "Pairs are equal" << std::endl;
    }
    
    if (p1 < p2) {
        std::cout << "p1 is less than p2" << std::endl;
    }
    
    // Make pair helper
    auto p3 = std::make_pair(42, std::string("Answer"));
    
    // Piecewise construction
    std::pair<std::vector<int>, std::string> p4 = 
        std::make_pair(std::vector<int>{1, 2, 3}, "Vector");
}
```

## 🔧 Move Semantics

### std::move
```cpp
#include <iostream>
#include <utility>
#include <vector>
#include <string>

class Resource {
private:
    std::string m_name;
    std::vector<int> m_data;
    
public:
    Resource(const std::string& name) : m_name(name) {
        m_data.resize(1000, 42);  // Simulate large data
        std::cout << "Resource " << m_name << " constructed" << std::endl;
    }
    
    // Copy constructor
    Resource(const Resource& other) : m_name(other.m_name), m_data(other.m_data) {
        std::cout << "Resource " << m_name << " copy constructed" << std::endl;
    }
    
    // Move constructor
    Resource(Resource&& other) noexcept 
        : m_name(std::move(other.m_name)), m_data(std::move(other.m_data)) {
        std::cout << "Resource " << m_name << " move constructed" << std::endl;
    }
    
    // Copy assignment
    Resource& operator=(const Resource& other) {
        if (this != &other) {
            m_name = other.m_name;
            m_data = other.m_data;
            std::cout << "Resource " << m_name << " copy assigned" << std::endl;
        }
        return *this;
    }
    
    // Move assignment
    Resource& operator=(Resource&& other) noexcept {
        if (this != &other) {
            m_name = std::move(other.m_name);
            m_data = std::move(other.m_data);
            std::cout << "Resource " << m_name << " move assigned" << std::endl;
        }
        return *this;
    }
    
    void display() const {
        std::cout << "Resource " << m_name << " with " << m_data.size() << " items" << std::endl;
    }
};

void demonstrateMove() {
    Resource r1("Original");
    Resource r2("Copy");
    
    std::cout << "\n--- Copy Assignment ---" << std::endl;
    r2 = r1;  // Copy assignment
    
    std::cout << "\n--- Move Assignment ---" << std::endl;
    Resource r3("Move Target");
    r3 = std::move(r1);  // Move assignment
    
    std::cout << "\n--- Move Construction ---" << std::endl;
    Resource r4 = std::move(r2);  // Move construction
    
    std::cout << "\n--- Final State ---" << std::endl;
    r1.display();  // r1 is in a valid but unspecified state
    r2.display();  // r2 is in a valid but unspecified state
    r3.display();
    r4.display();
}
```

### std::forward and Perfect Forwarding
```cpp
template<typename T>
void wrapper(T&& arg) {
    // Perfect forwarding to another function
    process(std::forward<T>(arg));
}

void process(int& value) {
    std::cout << "Processing lvalue: " << value << std::endl;
}

void process(int&& value) {
    std::cout << "Processing rvalue: " << value << std::endl;
}

void demonstrateForwarding() {
    int x = 42;
    
    std::cout << "Calling wrapper with lvalue:" << std::endl;
    wrapper(x);  // Forwards as lvalue
    
    std::cout << "\nCalling wrapper with rvalue:" << std::endl;
    wrapper(100);  // Forwards as rvalue
}
```

## 🔧 Swap and Exchange Operations

### std::swap
```cpp
#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

void demonstrateSwap() {
    // Basic types
    int a = 10, b = 20;
    std::cout << "Before swap: a=" << a << ", b=" << b << std::endl;
    std::swap(a, b);
    std::cout << "After swap: a=" << a << ", b=" << b << std::endl;
    
    // Containers
    std::vector<int> vec1 = {1, 2, 3};
    std::vector<int> vec2 = {4, 5, 6};
    
    std::cout << "\nBefore container swap:" << std::endl;
    std::cout << "vec1: ";
    for (int x : vec1) std::cout << x << " ";
    std::cout << "\nvec2: ";
    for (int x : vec2) std::cout << x << " ";
    std::cout << std::endl;
    
    std::swap(vec1, vec2);  // Efficient swap (usually just swaps pointers)
    
    std::cout << "\nAfter container swap:" << std::endl;
    std::cout << "vec1: ";
    for (int x : vec1) std::cout << x << " ";
    std::cout << "\nvec2: ";
    for (int x : vec2) std::cout << x << " ";
    std::cout << std::endl;
}
```

### std::exchange
```cpp
#include <iostream>
#include <utility>
#include <string>

class StateMachine {
private:
    std::string m_state;
    
public:
    StateMachine(const std::string& initialState) : m_state(initialState) {}
    
    std::string transition(const std::string& newState) {
        // Exchange returns the old value and sets the new value
        std::string oldState = std::exchange(m_state, newState);
        std::cout << "Transitioning from " << oldState << " to " << newState << std::endl;
        return oldState;
    }
    
    const std::string& getCurrentState() const { return m_state; }
};

void demonstrateExchange() {
    StateMachine sm("Initial");
    
    std::string old1 = sm.transition("Processing");
    std::string old2 = sm.transition("Complete");
    
    std::cout << "Current state: " << sm.getCurrentState() << std::endl;
    std::cout << "Previous states: " << old1 << " -> " << old2 << std::endl;
    
    // Another use case: reset and return old value
    int value = 42;
    int oldValue = std::exchange(value, 0);  // value becomes 0, oldValue is 42
    std::cout << "Old value: " << oldValue << ", New value: " << value << std::endl;
}
```

## 🎮 Practical Examples

### Example 1: Coordinate System with Pairs
```cpp
#include <iostream>
#include <utility>
#include <vector>
#include <cmath>

class PointSystem {
public:
    using Point = std::pair<double, double>;
    using Point3D = std::pair<Point, double>;  // 2D point + height
    
    // Create points
    static Point makePoint(double x, double y) {
        return {x, y};
    }
    
    static Point3D makePoint3D(double x, double y, double z) {
        return {{x, y}, z};
    }
    
    // Calculate distance between 2D points
    static double distance(const Point& p1, const Point& p2) {
        double dx = p1.first - p2.first;
        double dy = p1.second - p2.second;
        return std::sqrt(dx * dx + dy * dy);
    }
    
    // Calculate distance between 3D points
    static double distance3D(const Point3D& p1, const Point3D& p2) {
        double dx = p1.first.first - p2.first.first;
        double dy = p1.first.second - p2.first.second;
        double dz = p1.second - p2.second;
        return std::sqrt(dx * dx + dy * dy + dz * dz);
    }
    
    // Find closest point
    static Point findClosest(const Point& target, const std::vector<Point>& points) {
        if (points.empty()) {
            return {0, 0};
        }
        
        Point closest = points[0];
        double minDist = distance(target, closest);
        
        for (const auto& point : points) {
            double dist = distance(target, point);
            if (dist < minDist) {
                minDist = dist;
                closest = point;
            }
        }
        
        return closest;
    }
    
    // Display point
    static void display(const Point& p) {
        std::cout << "(" << p.first << ", " << p.second << ")";
    }
    
    static void display3D(const Point3D& p) {
        std::cout << "(" << p.first.first << ", " << p.first.second << ", " << p.second << ")";
    }
};

int main() {
    // 2D points
    PointSystem::Point p1 = PointSystem::makePoint(0, 0);
    PointSystem::Point p2 = PointSystem::makePoint(3, 4);
    
    std::cout << "Distance between ";
    PointSystem::display(p1);
    std::cout << " and ";
    PointSystem::display(p2);
    std::cout << ": " << PointSystem::distance(p1, p2) << std::endl;
    
    // 3D points
    PointSystem::Point3D p3d1 = PointSystem::makePoint3D(0, 0, 0);
    PointSystem::Point3D p3d2 = PointSystem::makePoint3D(1, 2, 2);
    
    std::cout << "3D distance between ";
    PointSystem::display3D(p3d1);
    std::cout << " and ";
    PointSystem::display3D(p3d2);
    std::cout << ": " << PointSystem::distance3D(p3d1, p3d2) << std::endl;
    
    // Find closest point
    std::vector<PointSystem::Point> points = {
        {1, 1}, {5, 5}, {-2, 3}, {10, -1}
    };
    
    PointSystem::Point target = {2, 2};
    PointSystem::Point closest = PointSystem::findClosest(target, points);
    
    std::cout << "Closest to ";
    PointSystem::display(target);
    std::cout << " is ";
    PointSystem::display(closest);
    std::cout << std::endl;
    
    return 0;
}
```

### Example 2: Generic Container with Move Semantics
```cpp
#include <iostream>
#include <utility>
#include <vector>
#include <memory>

template<typename T>
class SmartContainer {
private:
    std::vector<T> m_data;
    std::string m_name;
    
public:
    // Constructor
    SmartContainer(const std::string& name) : m_name(name) {
        std::cout << "Container " << m_name << " created" << std::endl;
    }
    
    // Copy constructor
    SmartContainer(const SmartContainer& other) : m_data(other.m_data), m_name(other.m_name) {
        std::cout << "Container " << m_name << " copy constructed" << std::endl;
    }
    
    // Move constructor
    SmartContainer(SmartContainer&& other) noexcept 
        : m_data(std::move(other.m_data)), m_name(std::move(other.m_name)) {
        std::cout << "Container " << m_name << " move constructed" << std::endl;
    }
    
    // Copy assignment
    SmartContainer& operator=(const SmartContainer& other) {
        if (this != &other) {
            m_data = other.m_data;
            m_name = other.m_name;
            std::cout << "Container " << m_name << " copy assigned" << std::endl;
        }
        return *this;
    }
    
    // Move assignment
    SmartContainer& operator=(SmartContainer&& other) noexcept {
        if (this != &other) {
            m_data = std::move(other.m_data);
            m_name = std::move(other.m_name);
            std::cout << "Container " << m_name << " move assigned" << std::endl;
        }
        return *this;
    }
    
    // Add element (perfect forwarding)
    template<typename U>
    void add(U&& item) {
        m_data.push_back(std::forward<U>(item));
    }
    
    // Transfer ownership of an element
    T extract(size_t index) {
        if (index >= m_data.size()) {
            throw std::out_of_range("Index out of range");
        }
        
        T item = std::move(m_data[index]);
        m_data.erase(m_data.begin() + index);
        return item;
    }
    
    // Swap contents with another container
    void swap(SmartContainer& other) noexcept {
        std::swap(m_data, other.m_data);
        std::swap(m_name, other.m_name);
        std::cout << "Swapped containers " << m_name << " and " << other.m_name << std::endl;
    }
    
    // Get size
    size_t size() const { return m_data.size(); }
    
    // Display contents
    void display() const {
        std::cout << "Container " << m_name << " (" << size() << " items): ";
        for (const auto& item : m_data) {
            std::cout << item << " ";
        }
        std::cout << std::endl;
    }
};

int main() {
    SmartContainer<int> container1("First");
    SmartContainer<int> container2("Second");
    
    // Add elements (perfect forwarding)
    container1.add(1);
    container1.add(2);
    container1.add(3);
    
    int value = 42;
    container1.add(value);  // lvalue
    container1.add(100);   // rvalue
    
    std::cout << "\nAfter adding elements:" << std::endl;
    container1.display();
    
    // Move construction
    std::cout << "\nMove construction:" << std::endl;
    SmartContainer<int> container3 = std::move(container1);
    container3.display();
    
    // Move assignment
    std::cout << "\nMove assignment:" << std::endl;
    container2 = std::move(container3);
    container2.display();
    
    // Extract element (move out)
    std::cout << "\nExtract element:" << std::endl;
    if (container2.size() > 0) {
        int extracted = container2.extract(0);
        std::cout << "Extracted: " << extracted << std::endl;
        container2.display();
    }
    
    // Swap containers
    std::cout << "\nSwap containers:" << std::endl;
    SmartContainer<int> container4("Fourth");
    container4.add(99);
    container4.add(88);
    
    container2.swap(container4);
    container2.display();
    container4.display();
    
    return 0;
}
```

### Example 3: Configuration Manager with Pairs
```cpp
#include <iostream>
#include <utility>
#include <vector>
#include <string>
#include <map>
#include <variant>

class ConfigManager {
private:
    using ConfigValue = std::variant<int, double, std::string, bool>;
    std::map<std::string, ConfigValue> m_config;
    std::vector<std::pair<std::string, ConfigValue>> m_history;
    
public:
    // Set configuration value
    template<typename T>
    void set(const std::string& key, T&& value) {
        // Store old value in history
        auto it = m_config.find(key);
        if (it != m_config.end()) {
            m_history.emplace_back(key, it->second);
        }
        
        // Set new value (perfect forwarding)
        m_config[key] = std::forward<T>(value);
        std::cout << "Set " << key << " = " << value << std::endl;
    }
    
    // Get configuration value
    template<typename T>
    T get(const std::string& key, const T& defaultValue = T{}) const {
        auto it = m_config.find(key);
        if (it != m_config.end()) {
            if (auto val = std::get_if<T>(&it->second)) {
                return *val;
            }
        }
        return defaultValue;
    }
    
    // Get all key-value pairs
    std::vector<std::pair<std::string, std::string>> getAll() const {
        std::vector<std::pair<std::string, std::string>> result;
        
        for (const auto& [key, value] : m_config) {
            std::string valueStr;
            
            std::visit([&valueStr](const auto& arg) {
                if constexpr (std::is_same_v<decltype(arg), bool>) {
                    valueStr = arg ? "true" : "false";
                } else {
                    valueStr = std::to_string(arg);
                }
            }, value);
            
            result.emplace_back(key, valueStr);
        }
        
        return result;
    }
    
    // Swap with another config manager
    void swap(ConfigManager& other) noexcept {
        std::swap(m_config, other.m_config);
        std::swap(m_history, other.m_history);
        std::cout << "Swapped configuration managers" << std::endl;
    }
    
    // Reset to default values
    void reset() {
        std::vector<std::pair<std::string, ConfigValue>> defaults = {
            {"debug", false},
            {"version", 1},
            {"threshold", 0.5},
            {"name", std::string("default")}
        };
        
        for (auto& [key, value] : defaults) {
            m_config[key] = std::move(value);
        }
        
        m_history.clear();
        std::cout << "Reset to default configuration" << std::endl;
    }
    
    // Display configuration
    void display() const {
        std::cout << "Configuration:" << std::endl;
        auto all = getAll();
        for (const auto& [key, value] : all) {
            std::cout << "  " << key << " = " << value << std::endl;
        }
    }
    
    // Display history
    void displayHistory() const {
        std::cout << "Change History:" << std::endl;
        for (const auto& [key, value] : m_history) {
            std::cout << "  " << key << " = ";
            std::visit([](const auto& arg) {
                if constexpr (std::is_same_v<decltype(arg), bool>) {
                    std::cout << (arg ? "true" : "false");
                } else if constexpr (std::is_same_v<decltype(arg), std::string>) {
                    std::cout << arg;
                } else {
                    std::cout << arg;
                }
            }, value);
            std::cout << std::endl;
        }
    }
};

int main() {
    ConfigManager config;
    
    // Set various configuration values
    config.set("debug", true);
    config.set("version", 2);
    config.set("threshold", 0.75);
    config.set("name", std::string("MyApp"));
    
    std::cout << "\nCurrent configuration:" << std::endl;
    config.display();
    
    // Get values
    std::cout << "\nRetrieved values:" << std::endl;
    std::cout << "Debug: " << config.get<bool>("debug") << std::endl;
    std::cout << "Version: " << config.get<int>("version") << std::endl;
    std::cout << "Threshold: " << config.get<double>("threshold") << std::endl;
    std::cout << "Name: " << config.get<std::string>("name") << std::endl;
    std::cout << "Missing key: " << config.get<int>("missing", -1) << std::endl;
    
    // Modify some values
    config.set("debug", false);
    config.set("version", 3);
    
    std::cout << "\nHistory:" << std::endl;
    config.displayHistory();
    
    // Swap with another config
    ConfigManager otherConfig;
    otherConfig.set("debug", true);
    otherConfig.set("name", std::string("OtherApp"));
    
    std::cout << "\nBefore swap:" << std::endl;
    config.display();
    otherConfig.display();
    
    config.swap(otherConfig);
    
    std::cout << "\nAfter swap:" << std::endl;
    config.display();
    otherConfig.display();
    
    // Reset
    config.reset();
    std::cout << "\nAfter reset:" << std::endl;
    config.display();
    
    return 0;
}
```

### Example 4: Template Metaprogramming with Integer Sequences
```cpp
#include <iostream>
#include <utility>
#include <array>
#include <tuple>

// Function to print parameter pack
template<typename... Args>
void printArgs(Args&&... args) {
    ((std::cout << args << " "), ...);
    std::cout << std::endl;
}

// Function that works with index sequence
template<typename Tuple, size_t... Indices>
void printTupleImpl(const Tuple& tuple, std::index_sequence<Indices...>) {
    std::cout << "Tuple elements: ";
    (std::cout << ... << (std::get<Indices>(tuple) << (Indices + 1 == sizeof...(Indices) ? "" : ", ")));
    std::cout << std::endl;
}

// Wrapper function
template<typename... Args>
void printTuple(const std::tuple<Args...>& tuple) {
    printTupleImpl(tuple, std::make_index_sequence<sizeof...(Args)>{});
}

// Create array from parameter pack
template<typename... Args>
auto makeArray(Args&&... args) {
    return std::array<std::common_type_t<Args...>, sizeof...(Args)>{std::forward<Args>(args)...};
}

// Sum parameter pack
template<typename... Args>
auto sum(Args&&... args) {
    return (args + ... + 0);
}

// Check if all arguments are equal
template<typename... Args>
bool allEqual(Args&&... args) {
    if constexpr (sizeof...(Args) <= 1) {
        return true;
    } else {
        return ((args == ... ) && true);
    }
}

int main() {
    // Print parameter pack
    std::cout << "Printing arguments: ";
    printArgs(1, 2.5, "hello", true);
    
    // Work with tuples
    auto tuple = std::make_tuple(42, 3.14, std::string("Pi"));
    printTuple(tuple);
    
    // Create array from arguments
    auto arr = makeArray(1, 2, 3, 4, 5);
    std::cout << "Array: ";
    for (int x : arr) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    
    // Sum arguments
    auto sumResult = sum(1, 2, 3, 4, 5);
    std::cout << "Sum: " << sumResult << std::endl;
    
    // Check equality
    std::cout << "All equal (1, 1, 1): " << allEqual(1, 1, 1) << std::endl;
    std::cout << "All equal (1, 2, 1): " << allEqual(1, 2, 1) << std::endl;
    
    return 0;
}
```

## 📊 Complete Function Reference

### Pair Operations
| Function/Operation | Description | Example |
|-------------------|-------------|---------|
| `std::pair<T1, T2>` | Two-element container | `std::pair<int, string>` |
| `std::make_pair()` | Create pair with type deduction | `auto p = make_pair(1, "one")` |
| `pair.first` | Access first element | `p.first` |
| `pair.second` | Access second element | `p.second` |
| `operator==` | Equality comparison | `p1 == p2` |
| `operator<` | Less than comparison | `p1 < p2` |

### Move Semantics
| Function | Description | Example |
|----------|-------------|---------|
| `std::move()` | Cast to rvalue reference | `std::move(obj)` |
| `std::forward()` | Perfect forwarding | `std::forward<T>(arg)` |
| `std::move_if_noexcept()` | Conditional move | `std::move_if_noexcept(obj)` |

### Swap Operations
| Function | Description | Example |
|----------|-------------|---------|
| `std::swap()` | Exchange two values | `std::swap(a, b)` |
| `std::exchange()` | Replace and return old value | `old = std::exchange(var, new_val)` |

### Relational Operations
| Function | Description | Example |
|----------|-------------|---------|
| `std::rel_ops::operator!=` | Inequality from `<` | `a != b` |
| `std::rel_ops::operator>` | Greater than from `<` | `a > b` |
| `std::rel_ops::operator<=` | Less equal from `<` | `a <= b` |
| `std::rel_ops::operator>=` | Greater equal from `<` | `a >= b` |

## ⚡ Performance Considerations

### Efficient Pair Usage
```cpp
// Use structured bindings for cleaner code (C++17)
auto [key, value] = getPair();

// Use make_pair for type deduction
auto pair = std::make_pair(42, std::string("answer"));

// For complex types, consider move semantics
std::pair<std::vector<int>, std::string> p = 
    std::make_pair(std::vector<int>{1,2,3}, std::string("test"));
```

### Move Semantics Best Practices
```cpp
// Use std::move when transferring ownership
std::vector<int> source = {1, 2, 3};
std::vector<int> dest = std::move(source);  // Efficient move

// Don't use std::move on const objects
const std::vector<int> const_vec = {1, 2, 3};
auto copy = std::move(const_vec);  // Actually copies, not moves

// Use std::forward in templates for perfect forwarding
template<typename T>
void factory(T&& arg) {
    process(std::forward<T>(arg));
}
```

## 🎯 Common Patterns

### Pattern 1: Return Multiple Values
```cpp
std::pair<bool, int> parseNumber(const std::string& str) {
    try {
        int value = std::stoi(str);
        return {true, value};
    } catch (...) {
        return {false, 0};
    }
}

// Usage (C++17)
auto [success, value] = parseNumber("123");
```

### Pattern 2: Efficient Resource Transfer
```cpp
class ResourceManager {
    std::unique_ptr<int[]> m_data;
    size_t m_size;
    
public:
    std::pair<std::unique_ptr<int[]>, size_t> releaseData() {
        return {std::move(m_data), std::exchange(m_size, 0)};
    }
};
```

## 🐛 Common Pitfalls & Solutions

### 1. Using Moved Objects
```cpp
// Problem
std::string s1 = "Hello";
std::string s2 = std::move(s1);
std::cout << s1;  // Undefined behavior!

// Solution
std::string s1 = "Hello";
std::string s2 = std::move(s1);
if (!s1.empty()) {  // Check if still valid
    std::cout << s1;
}
```

### 2. Unnecessary Moves
```cpp
// Problem - unnecessary move
std::pair<int, std::string> createPair() {
    int x = 42;
    std::string s = "answer";
    return std::make_pair(std::move(x), std::move(s));  // x is not movable
}

// Solution - let NRVO handle it
std::pair<int, std::string> createPair() {
    return {42, "answer"};
}
```

### 3. Forwarding References vs Universal References
```cpp
// Correct - forwarding reference in template
template<typename T>
void func(T&& arg) {  // T is deduced
    std::forward<T>(arg);
}

// Wrong - not a forwarding reference
void func(std::string&& arg) {  // T is not deduced
    std::forward<std::string>(arg);  // Unnecessary
}
```

## 📚 Related Headers

- `tuple.md` - For more than two elements
- `memory.md` - For smart pointers and move semantics
- `type_traits.md` - For type utilities
- `functional.md` - For function objects

## 🚀 Best Practices

1. **Use `std::make_pair`** for type deduction and readability
2. **Use structured bindings** (C++17) for cleaner pair unpacking
3. **Use `std::move`** only when you want to transfer ownership
4. **Use `std::forward`** in templates for perfect forwarding
5. **Prefer `std::exchange`** over manual swap-and-assign patterns
6. **Use `std::swap`** for efficient container exchanges

## 🎯 When to Use utility

✅ **Use utility when:**
- Working with pairs of values
- Implementing move semantics
- Writing generic templates
- Need efficient value exchange
- Working with tuples and structured bindings

❌ **Avoid when:**
- You need more than two elements (use `std::tuple`)
- Working with simple built-in types only
- Performance is not a concern
---

## Next Step

- Go to [10_tuple.md](10_tuple.md) to continue with tuple.
