# `std::variant` — Type-Safe Sum Types

> **Minimum standard:** C++17
>
> **Canonical location:** Standard-library reference. Data-structure lessons should link here instead of repeating this API.

## std::variant (Type-Safe Union - C++17)

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

## Next Step

Continue with the next vocabulary-type lesson in the [standard-library index](README.md).

