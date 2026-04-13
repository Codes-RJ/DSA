# Lambda Expressions in C++ - Complete Guide

## 📖 Overview

Lambda expressions (introduced in C++11) are anonymous function objects that can capture variables from their enclosing scope. They provide a concise way to define functions inline, especially useful for short functions passed to algorithms, callbacks, and custom comparators. Modern C++ (C++14, C++17, C++20) has significantly enhanced lambda capabilities.

---

## 🎯 Key Concepts

| Feature | Version | Description |
|---------|---------|-------------|
| **Basic lambda** | C++11 | `[capture](params) -> ret { body }` |
| **Generic lambda** | C++14 | `auto` parameters |
| **Lambda capture init** | C++14 | Move capture, init capture |
| **constexpr lambda** | C++17 | Compile-time evaluation |
| **Lambda templates** | C++20 | Explicit template parameters |
| **Stateless lambda** | C++20 | Default constructible |

---

## 1. **Basic Lambda Syntax**

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    cout << "=== Basic Lambda Syntax ===" << endl;
    
    // Basic lambda
    auto greet = []() {
        cout << "Hello, World!" << endl;
    };
    greet();
    
    // Lambda with parameters
    auto add = [](int a, int b) {
        return a + b;
    };
    cout << "add(5, 3) = " << add(5, 3) << endl;
    
    // Lambda with explicit return type
    auto divide = [](double a, double b) -> double {
        if (b == 0) return 0;
        return a / b;
    };
    cout << "divide(10, 3) = " << divide(10, 3) << endl;
    
    // Lambda with auto parameters (generic lambda - C++14)
    auto generic_add = [](auto a, auto b) {
        return a + b;
    };
    cout << "generic_add(5, 3) = " << generic_add(5, 3) << endl;
    cout << "generic_add(3.14, 2.71) = " << generic_add(3.14, 2.71) << endl;
    cout << "generic_add(string(\"Hello\"), string(\" World\")) = " 
         << generic_add(string("Hello"), string(" World")) << endl;
    
    // Lambda stored in variable
    auto multiply = [](int a, int b) { return a * b; };
    cout << "multiply(5, 3) = " << multiply(5, 3) << endl;
    
    return 0;
}
```

**Output:**
```
=== Basic Lambda Syntax ===
Hello, World!
add(5, 3) = 8
divide(10, 3) = 3.33333
generic_add(5, 3) = 8
generic_add(3.14, 2.71) = 5.85
generic_add(string("Hello"), string(" World")) = Hello World
multiply(5, 3) = 15
```

---

## 2. **Lambda Capture Modes**

```cpp
#include <iostream>
#include <string>
#include <functional>
using namespace std;

int main() {
    cout << "=== Lambda Capture Modes ===" << endl;
    
    int x = 10;
    int y = 20;
    
    // Capture by value (copy)
    auto by_value = [x, y]() {
        // x = 100;  // Error! x is const by default
        cout << "by_value: x=" << x << ", y=" << y << endl;
    };
    by_value();
    
    // Capture by reference
    auto by_ref = [&x, &y]() {
        x = 100;
        y = 200;
        cout << "by_ref: x=" << x << ", y=" << y << endl;
    };
    by_ref();
    cout << "After by_ref: x=" << x << ", y=" << y << endl;
    
    // Reset values
    x = 10;
    y = 20;
    
    // Capture all by value
    auto all_by_value = [=]() {
        cout << "all_by_value: x=" << x << ", y=" << y << endl;
    };
    all_by_value();
    
    // Capture all by reference
    auto all_by_ref = [&]() {
        x = 1000;
        y = 2000;
        cout << "all_by_ref: x=" << x << ", y=" << y << endl;
    };
    all_by_ref();
    
    // Mix: capture x by value, y by reference
    x = 10;
    y = 20;
    auto mix = [x, &y]() {
        // x = 100;  // Error! x captured by value (const)
        y = 200;
        cout << "mix: x=" << x << ", y=" << y << endl;
    };
    mix();
    cout << "After mix: x=" << x << ", y=" << y << endl;
    
    // Mutable lambda (can modify captured values)
    int counter = 0;
    auto mutable_lambda = [counter]() mutable {
        counter++;
        cout << "mutable lambda: counter=" << counter << endl;
    };
    mutable_lambda();  // counter=1
    mutable_lambda();  // counter=2
    cout << "Original counter: " << counter << endl;
    
    // Capture with initializer (C++14)
    auto init_capture = [value = 42]() {
        cout << "init_capture: value=" << value << endl;
    };
    init_capture();
    
    // Move capture (C++14)
    auto unique_ptr = make_unique<int>(100);
    auto move_capture = [ptr = move(unique_ptr)]() {
        cout << "move_capture: *ptr=" << *ptr << endl;
    };
    move_capture();
    // unique_ptr is now empty
    
    return 0;
}
```

---

## 3. **Lambdas with STL Algorithms**

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
using namespace std;

class Person {
public:
    string name;
    int age;
    
    Person(string n, int a) : name(n), age(a) {}
};

int main() {
    cout << "=== Lambdas with STL Algorithms ===" << endl;
    
    vector<int> numbers = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    
    // Sort with lambda
    cout << "1. Sorting:" << endl;
    sort(numbers.begin(), numbers.end(), [](int a, int b) {
        return a > b;  // descending
    });
    cout << "   Descending: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Find with lambda
    auto it = find_if(numbers.begin(), numbers.end(), [](int n) {
        return n > 5;
    });
    if (it != numbers.end()) {
        cout << "   First element > 5: " << *it << endl;
    }
    
    // Count with lambda
    int count = count_if(numbers.begin(), numbers.end(), [](int n) {
        return n % 2 == 0;
    });
    cout << "   Even numbers count: " << count << endl;
    
    // Transform with lambda
    vector<int> squares(numbers.size());
    transform(numbers.begin(), numbers.end(), squares.begin(), [](int n) {
        return n * n;
    });
    cout << "   Squares: ";
    for (int n : squares) cout << n << " ";
    cout << endl;
    
    // For each with lambda
    cout << "2. For each:" << endl;
    for_each(numbers.begin(), numbers.end(), [](int& n) {
        n *= 2;
    });
    cout << "   Doubled: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Accumulate with lambda
    int sum = accumulate(numbers.begin(), numbers.end(), 0, [](int acc, int n) {
        return acc + n;
    });
    cout << "   Sum: " << sum << endl;
    
    // Sorting vector of objects
    vector<Person> people = {
        {"Alice", 30},
        {"Bob", 25},
        {"Charlie", 35},
        {"Diana", 28}
    };
    
    cout << "3. Sorting objects:" << endl;
    sort(people.begin(), people.end(), [](const Person& a, const Person& b) {
        return a.age < b.age;
    });
    cout << "   Sorted by age: ";
    for (const auto& p : people) {
        cout << p.name << "(" << p.age << ") ";
    }
    cout << endl;
    
    return 0;
}
```

---

## 4. **Lambda with Captures in Algorithms**

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    cout << "=== Lambda with Captures in Algorithms ===" << endl;
    
    vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // Capture by value
    int threshold = 5;
    auto greater_than = [threshold](int n) {
        return n > threshold;
    };
    
    auto it = find_if(numbers.begin(), numbers.end(), greater_than);
    cout << "First number > " << threshold << ": " << *it << endl;
    
    // Capture by reference (modify)
    int sum = 0;
    for_each(numbers.begin(), numbers.end(), [&sum](int n) {
        sum += n;
    });
    cout << "Sum of all numbers: " << sum << endl;
    
    // Capture by reference (modify vector)
    int multiplier = 3;
    for_each(numbers.begin(), numbers.end(), [multiplier](int& n) {
        n *= multiplier;
    });
    cout << "Multiplied by " << multiplier << ": ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Multiple captures
    int min_val = 3;
    int max_val = 7;
    auto in_range = [min_val, max_val](int n) {
        return n >= min_val && n <= max_val;
    };
    
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    auto it2 = find_if(numbers.begin(), numbers.end(), in_range);
    cout << "First number in range [" << min_val << ", " << max_val << "]: " << *it2 << endl;
    
    // Capture with initializer
    int base = 10;
    auto add_base = [base = base](int n) {
        return n + base;
    };
    cout << "add_base(5) = " << add_base(5) << endl;
    
    // Move capture
    auto data = make_unique<int>(42);
    auto process = [data = move(data)]() {
        cout << "Processing data: " << *data << endl;
    };
    process();
    // data is now empty
    
    return 0;
}
```

---

## 5. **Lambda as Function Parameter**

```cpp
#include <iostream>
#include <vector>
#include <functional>
#include <string>
using namespace std;

// Function taking lambda as parameter
void apply(vector<int>& data, function<int(int)> func) {
    for (auto& n : data) {
        n = func(n);
    }
}

// Template version (more efficient)
template<typename Func>
void apply_template(vector<int>& data, Func func) {
    for (auto& n : data) {
        n = func(n);
    }
}

// Function returning lambda
auto make_multiplier(int factor) {
    return [factor](int x) {
        return x * factor;
    };
}

// Lambda stored in class
class Processor {
private:
    function<int(int)> operation_;
    
public:
    Processor(function<int(int)> op) : operation_(op) {}
    
    int process(int value) {
        return operation_(value);
    }
};

int main() {
    cout << "=== Lambda as Function Parameter ===" << endl;
    
    vector<int> numbers = {1, 2, 3, 4, 5};
    
    // Pass lambda directly
    apply(numbers, [](int n) { return n * n; });
    cout << "Squares: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Store lambda in variable
    auto doubler = [](int n) { return n * 2; };
    numbers = {1, 2, 3, 4, 5};
    apply(numbers, doubler);
    cout << "Doubled: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Template version
    numbers = {1, 2, 3, 4, 5};
    apply_template(numbers, [](int n) { return n + 10; });
    cout << "Added 10: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    // Return lambda from function
    auto times3 = make_multiplier(3);
    cout << "times3(5) = " << times3(5) << endl;
    
    // Lambda in class
    Processor square([](int n) { return n * n; });
    cout << "square(5) = " << square.process(5) << endl;
    
    // Lambda as comparator for priority_queue
    auto cmp = [](int a, int b) { return a > b; };
    priority_queue<int, vector<int>, decltype(cmp)> pq(cmp);
    pq.push(5);
    pq.push(1);
    pq.push(9);
    pq.push(3);
    
    cout << "Priority queue (min-heap): ";
    while (!pq.empty()) {
        cout << pq.top() << " ";
        pq.pop();
    }
    cout << endl;
    
    return 0;
}
```

---

## 6. **Advanced Lambda Features (C++14/17/20)**

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <type_traits>
using namespace std;

// C++14: Generic lambda with auto
auto generic_lambda = [](auto a, auto b) {
    return a + b;
};

// C++14: Lambda with init capture
auto init_capture = [value = 42]() {
    return value;
};

// C++17: constexpr lambda
constexpr auto square = [](int n) constexpr {
    return n * n;
};

// C++17: lambda with constexpr condition
auto check = [](auto n) {
    if constexpr (is_integral_v<decltype(n)>) {
        return n * 2;
    } else {
        return n + n;
    }
};

// C++20: lambda with template parameters
auto template_lambda = []<typename T>(T a, T b) {
    return a + b;
};

// C++20: stateless lambda (default constructible)
auto stateless = [](int x) { return x * 2; };
decltype(stateless) stateless2;  // Default constructible in C++20

int main() {
    cout << "=== Advanced Lambda Features ===" << endl;
    
    // Generic lambda (C++14)
    cout << "generic_lambda(5, 3) = " << generic_lambda(5, 3) << endl;
    cout << "generic_lambda(3.14, 2.71) = " << generic_lambda(3.14, 2.71) << endl;
    cout << "generic_lambda(string(\"Hello\"), string(\" World\")) = " 
         << generic_lambda(string("Hello"), string(" World")) << endl;
    
    // Init capture (C++14)
    cout << "init_capture() = " << init_capture() << endl;
    
    // constexpr lambda (C++17)
    constexpr int sq = square(5);
    cout << "square(5) = " << sq << endl;
    
    // Lambda with constexpr if
    cout << "check(5) = " << check(5) << endl;
    cout << "check(3.14) = " << check(3.14) << endl;
    
    // Template lambda (C++20)
    cout << "template_lambda(5, 3) = " << template_lambda(5, 3) << endl;
    
    // Lambda with capture and return type
    auto lambda = [](int x) -> double {
        if (x > 0) return x * 1.5;
        return 0.0;
    };
    cout << "lambda(5) = " << lambda(5) << endl;
    
    // Recursive lambda (C++14)
    function<int(int)> factorial = [&](int n) -> int {
        return n <= 1 ? 1 : n * factorial(n - 1);
    };
    cout << "factorial(5) = " << factorial(5) << endl;
    
    return 0;
}
```

---

## 7. **Practical Example: Event System**

```cpp
#include <iostream>
#include <vector>
#include <functional>
#include <string>
#include <map>
using namespace std;

class EventSystem {
private:
    map<string, vector<function<void(const string&)>>> listeners_;
    
public:
    void subscribe(const string& event, function<void(const string&)> callback) {
        listeners_[event].push_back(callback);
    }
    
    void emit(const string& event, const string& data) {
        auto it = listeners_.find(event);
        if (it != listeners_.end()) {
            for (const auto& callback : it->second) {
                callback(data);
            }
        }
    }
};

int main() {
    cout << "=== Practical Example: Event System ===" << endl;
    
    EventSystem events;
    
    // Subscribe with lambdas
    events.subscribe("user_login", [](const string& data) {
        cout << "[LOG] User logged in: " << data << endl;
    });
    
    events.subscribe("user_login", [](const string& data) {
        cout << "[EMAIL] Welcome email sent to: " << data << endl;
    });
    
    events.subscribe("data_update", [](const string& data) {
        cout << "[CACHE] Cache updated: " << data << endl;
    });
    
    events.subscribe("data_update", [](const string& data) {
        cout << "[DB] Database updated: " << data << endl;
    });
    
    events.subscribe("error", [](const string& data) {
        cout << "[ERROR] Error occurred: " << data << endl;
    });
    
    // Emit events
    cout << "\nEmitting events:" << endl;
    events.emit("user_login", "alice@example.com");
    events.emit("data_update", "User profile");
    events.emit("error", "Connection timeout");
    
    // Lambda with capture for event tracking
    int event_count = 0;
    events.subscribe("stats", [&event_count](const string& data) {
        event_count++;
        cout << "[STATS] Event #" << event_count << ": " << data << endl;
    });
    
    events.emit("stats", "First event");
    events.emit("stats", "Second event");
    events.emit("stats", "Third event");
    
    return 0;
}
```

---

## 📊 Lambda Summary

| Feature | Syntax | Use Case |
|---------|--------|----------|
| **Basic** | `[](){}` | Simple inline function |
| **Capture by value** | `[=]` | Read-only access to local variables |
| **Capture by reference** | `[&]` | Modify local variables |
| **Mixed capture** | `[x, &y]` | Specific capture needs |
| **Generic lambda** | `[](auto x)` | Template-like behavior |
| **Mutable lambda** | `[x]() mutable` | Modify captured values |
| **Init capture** | `[x = move(y)]` | Move semantics |

---

## ✅ Best Practices

1. **Use lambdas** for short, single-use functions
2. **Capture by reference** for modification
3. **Capture by value** for read-only small types
4. **Use `const auto&`** for read-only large types
5. **Avoid default captures** `[=]` and `[&]` when possible
6. **Use `mutable`** only when needed
7. **Use generic lambdas** for template-like behavior

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Capturing by value** | Copies are const | Use mutable or capture by reference |
| **Dangling reference** | Captured reference outlives lambda | Capture by value or ensure lifetime |
| **Default capture** | Unintended captures | Explicit capture list |
| **Recursive lambda** | Need explicit type | Use std::function |

---

## ✅ Key Takeaways

1. **Lambdas** are anonymous function objects
2. **Capture list** defines accessible variables
3. **Capture by value** makes copies (const)
4. **Capture by reference** allows modification
5. **Generic lambdas** work with any type (C++14)
6. **constexpr lambdas** evaluated at compile time (C++17)
7. **Stateless lambdas** are default constructible (C++20)
8. **Use with STL algorithms** for concise code

---
---

## Next Step

- Go to [04_Smart_Pointers.md](04_Smart_Pointers.md) to continue with Smart Pointers.
