# `std::any` — Type-Erased Values

> **Minimum standard:** C++17
>
> **Canonical location:** Standard-library reference. Data-structure lessons should link here instead of repeating this API.

## std::any (Type-Safe Any Type - C++17)

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

## Next Step

Continue with the next vocabulary-type lesson in the [standard-library index](README.md).

