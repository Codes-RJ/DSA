# `std::optional` — Optional Values

> **Minimum standard:** C++17
>
> **Canonical location:** Standard-library reference. Data-structure lessons should link here instead of repeating this API.

## std::optional (Optional Value - C++17)

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

## Next Step

Continue with the next vocabulary-type lesson in the [standard-library index](README.md).

