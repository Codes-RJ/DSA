# Variadic Templates

## 📖 Overview

Variadic templates are a powerful C++ feature that allows templates to accept a variable number of template arguments. Introduced in C++11, they enable the creation of highly flexible and generic functions and classes that can work with any number of parameters of different types.

---

## 🎯 Key Concepts

- **Parameter Pack**: A template parameter that represents zero or more parameters
- **Pack Expansion**: Expanding a parameter pack into separate arguments
- **Fold Expressions**: C++17 feature for operating on parameter packs
- **Recursive Variadic Templates**: Processing parameter packs recursively
- **Variadic Class Templates**: Classes with variable number of template parameters

---

## 💻 Syntax Overview

### Variadic Function Template
```cpp
template <typename... Args>
returnType functionName(Args... args) {
    // Function body
}
```

### Variadic Class Template
```cpp
template <typename... Types>
class ClassName {
    // Class definition
};
```

---

## 🔍 Detailed Explanation

### 1. **Basic Variadic Function Templates**

```cpp
#include <iostream>
using namespace std;

// Basic variadic function
template <typename... Args>
void print(Args... args) {
    cout << "Number of arguments: " << sizeof...(Args) << endl;
}

// Variadic function with parameter pack expansion
template <typename T, typename... Args>
void printFirst(T first, Args... args) {
    cout << "First: " << first << endl;
    cout << "Remaining arguments: " << sizeof...(Args) << endl;
}

// Simple print function (recursive approach)
void printRecursive() {
    cout << endl; // Base case
}

template <typename T, typename... Args>
void printRecursive(T first, Args... args) {
    cout << first << " ";
    printRecursive(args...); // Recursive call
}

int main() {
    cout << "=== Basic Variadic Function Templates ===" << endl;
    
    // Different numbers of arguments
    print();
    print(42);
    print(42, "Hello", 3.14);
    
    cout << endl;
    
    printFirst(1, 2, 3, "four", 5.5);
    
    cout << "\nRecursive print:" << endl;
    printRecursive(1, 2, 3, 4, 5);
    printRecursive("Hello", "World", "!");
    
    return 0;
}
```

### 2. **Fold Expressions (C++17)**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Unary right fold
template <typename... Args>
auto sumRight(Args... args) {
    return (args + ... + 0); // (args1 + (args2 + (... + (argsN + 0))))
}

// Unary left fold
template <typename... Args>
auto sumLeft(Args... args) {
    return (0 + ... + args); // (((0 + args1) + args2) + ... + argsN)
}

// Binary fold
template <typename... Args>
auto sumBinary(Args... args) {
    return (args + ...); // Requires at least one argument
}

// Fold over comma operator (for printing)
template <typename... Args>
void printAll(Args&&... args) {
    ((cout << args << endl), ...); // Expands to (cout << arg1 << endl), (cout << arg2 << endl), ...
}

// Fold with custom operation
template <typename... Args>
auto multiplyAll(Args... args) {
    return (args * ... * 1);
}

// Fold with logical operations
template <typename... Args>
bool allTrue(Args... args) {
    return (args && ...); // Returns true if all args are true
}

template <typename... Args>
bool anyTrue(Args... args) {
    return (args || ...); // Returns true if any arg is true
}

// Fold with comparisons
template <typename T, typename... Args>
bool allEqual(T first, Args... args) {
    return ((first == args) && ...);
}

int main() {
    cout << "=== Fold Expressions (C++17) ===" << endl;
    
    // Sum operations
    cout << "Sum right: " << sumRight(1, 2, 3, 4, 5) << endl;
    cout << "Sum left: " << sumLeft(1, 2, 3, 4, 5) << endl;
    cout << "Sum binary: " << sumBinary(10, 20, 30) << endl;
    
    cout << endl;
    
    // Print all
    cout << "Print all:" << endl;
    printAll(1, "Hello", 3.14, true);
    
    cout << endl;
    
    // Multiply all
    cout << "Multiply all: " << multiplyAll(2, 3, 4) << endl;
    cout << "Multiply with single: " << multiplyAll(5) << endl;
    
    cout << endl;
    
    // Logical operations
    cout << "All true: " << allTrue(true, true, false, true) << endl;
    cout << "Any true: " << anyTrue(false, false, true, false) << endl;
    
    cout << endl;
    
    // Equality checks
    cout << "All equal (5,5,5): " << allEqual(5, 5, 5) << endl;
    cout << "All equal (5,5,3): " << allEqual(5, 5, 3) << endl;
    
    return 0;
}
```

### 3. **Variadic Class Templates**

```cpp
#include <iostream>
#include <tuple>
using namespace std;

// Simple variadic class template
template <typename... Types>
class TypeContainer {
public:
    static constexpr size_t size = sizeof...(Types);
    
    void printTypes() const {
        cout << "Container holds " << size << " types" << endl;
    }
};

// Variadic class that stores values
template <typename... Types>
class TupleStorage {
private:
    tuple<Types...> data;
    
public:
    TupleStorage(Types... args) : data(args...) {}
    
    template <size_t Index>
    auto get() {
        return get<Index>(data);
    }
    
    void display() const {
        cout << "TupleStorage with " << sizeof...(Types) << " elements" << endl;
        displayHelper(data);
    }
    
private:
    template <size_t I = 0, typename... T>
    void displayHelper(const tuple<T...>& t) const {
        if constexpr (I < sizeof...(T)) {
            cout << "  Element " << I << ": " << get<I>(t) << endl;
            displayHelper<I + 1>(t);
        }
    }
};

// Variadic class with inheritance
template <typename... Types>
class MultiInherit : public Types... {
public:
    MultiInherit(Types... bases) : Types(bases)... {}
    
    void printAll() {
        (Types::print(), ...); // Fold expression to call print on all bases
    }
};

// Base classes for inheritance example
class PrintableInt {
private:
    int value;
public:
    PrintableInt(int v) : value(v) {}
    void print() const { cout << "Int: " << value << endl; }
};

class PrintableString {
private:
    string value;
public:
    PrintableString(string v) : value(v) {}
    void print() const { cout << "String: " << value << endl; }
};

class PrintableDouble {
private:
    double value;
public:
    PrintableDouble(double v) : value(v) {}
    void print() const { cout << "Double: " << value << endl; }
};

int main() {
    cout << "=== Variadic Class Templates ===" << endl;
    
    // Simple type container
    TypeContainer<int, string, double> container1;
    container1.printTypes();
    
    TypeContainer<> container2;
    container2.printTypes();
    
    cout << endl;
    
    // Tuple storage
    TupleStorage<int, string, double> storage(42, "Hello", 3.14);
    storage.display();
    
    cout << "Element 0: " << storage.get<0>() << endl;
    cout << "Element 1: " << storage.get<1>() << endl;
    cout << "Element 2: " << storage.get<2>() << endl;
    
    cout << endl;
    
    // Multiple inheritance
    MultiInherit<PrintableInt, PrintableString, PrintableDouble> multi(
        PrintableInt(100), PrintableString("World"), PrintableDouble(2.71)
    );
    
    cout << "Multiple inheritance example:" << endl;
    multi.printAll();
    
    return 0;
}
```

### 4. **Advanced Variadic Template Techniques**

```cpp
#include <iostream>
#include <vector>
#include <type_traits>
using namespace std;

// Variadic template with perfect forwarding
template <typename... Args>
auto makeVector(Args&&... args) {
    return vector<common_type_t<Args...>>{forward<Args>(args)...};
}

// Variadic template with type constraints
template <typename... Args>
enable_if_t<(is_arithmetic_v<Args> && ...), auto>
sumArithmetic(Args... args) {
    return (args + ... + 0);
}

// Variadic template factory
template <typename T, typename... Args>
unique_ptr<T> makeUnique(Args&&... args) {
    return make_unique<T>(forward<Args>(args)...);
}

// Variadic template for function wrapper
template <typename Func, typename... Args>
auto callFunction(Func&& func, Args&&... args) {
    return forward<Func>(func)(forward<Args>(args)...);
}

// Variadic template with index sequence
template <typename... Args, size_t... Indices>
void printWithIndicesHelper(tuple<Args...> t, index_sequence<Indices...>) {
    ((cout << "Index " << Indices << ": " << get<Indices>(t) << endl), ...);
}

template <typename... Args>
void printWithIndices(Args&&... args) {
    auto t = make_tuple(forward<Args>(args)...);
    printWithIndicesHelper(t, make_index_sequence<sizeof...(Args)>{});
}

// Variadic template for type checking
template <typename T, typename... Args>
bool containsType() {
    return (is_same_v<T, Args> || ...);
}

// Variadic template for maximum value
template <typename T>
T maxVariadic(T value) {
    return value;
}

template <typename T, typename... Args>
T maxVariadic(T first, Args... args) {
    T restMax = maxVariadic(args...);
    return (first > restMax) ? first : restMax;
}

// Variadic template with custom separator
template <typename Separator, typename First, typename... Args>
void printWithSeparator(Separator sep, First first, Args... args) {
    cout << first;
    ((cout << sep << args), ...);
    cout << endl;
}

int main() {
    cout << "=== Advanced Variadic Template Techniques ===" << endl;
    
    // Perfect forwarding vector
    auto vec1 = makeVector(1, 2, 3, 4, 5);
    auto vec2 = makeVector(1.1, 2.2, 3.3);
    
    cout << "Vector from integers: ";
    for (auto v : vec1) cout << v << " ";
    cout << endl;
    
    cout << "Vector from doubles: ";
    for (auto v : vec2) cout << v << " ";
    cout << endl;
    
    cout << endl;
    
    // Type-constrained sum
    cout << "Arithmetic sum: " << sumArithmetic(1, 2, 3, 4.5) << endl;
    // sumArithmetic(1, "hello", 3); // Would not compile
    
    cout << endl;
    
    // Function wrapper
    auto add = [](int a, int b) { return a + b; };
    auto multiply = [](int a, int b) { return a * b; };
    
    cout << "Function call result: " << callFunction(add, 5, 3) << endl;
    cout << "Function call result: " << callFunction(multiply, 4, 6) << endl;
    
    cout << endl;
    
    // Print with indices
    printWithIndices("Hello", 42, 3.14, true);
    
    cout << endl;
    
    // Type checking
    cout << "Contains int in (int, double, string): " << containsType<int, int, double, string>() << endl;
    cout << "Contains float in (int, double, string): " << containsType<float, int, double, string>() << endl;
    
    cout << endl;
    
    // Maximum value
    cout << "Max of 1, 5, 3, 9, 2: " << maxVariadic(1, 5, 3, 9, 2) << endl;
    cout << "Max of 3.14, 2.71, 1.41: " << maxVariadic(3.14, 2.71, 1.41) << endl;
    
    cout << endl;
    
    // Custom separator
    printWithSeparator(" | ", "Apple", "Banana", "Cherry", "Date");
    printWithSeparator(" - ", 1, 2, 3, 4, 5);
    
    return 0;
}
```

### 5. **Practical Variadic Template Applications**

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

// String formatter
template <typename... Args>
string format(const string& formatStr, Args&&... args) {
    stringstream result;
    size_t pos = 0;
    size_t argIndex = 0;
    
    auto argsTuple = make_tuple(forward<Args>(args)...);
    
    while (pos < formatStr.length()) {
        if (pos + 1 < formatStr.length() && formatStr[pos] == '{' && formatStr[pos + 1] == '}') {
            if (argIndex < sizeof...(Args)) {
                result << get<argIndex>(argsTuple);
                argIndex++;
            } else {
                result << "{}"; // Not enough arguments
            }
            pos += 2;
        } else {
            result << formatStr[pos];
            pos++;
        }
    }
    
    return result.str();
}

// Logger class with variadic templates
class Logger {
private:
    ofstream logFile;
    
public:
    Logger(const string& filename) : logFile(filename, ios::app) {}
    
    template <typename... Args>
    void log(const string& level, Args&&... args) {
        string message = format("[{}] {}", level, args...);
        cout << message << endl;
        if (logFile.is_open()) {
            logFile << message << endl;
        }
    }
    
    template <typename... Args>
    void info(Args&&... args) {
        log("INFO", args...);
    }
    
    template <typename... Args>
    void error(Args&&... args) {
        log("ERROR", args...);
    }
    
    template <typename... Args>
    void debug(Args&&... args) {
        log("DEBUG", args...);
    }
};

// Event system with variadic templates
template <typename... Args>
class Event {
private:
    vector<function<void(Args...)>> handlers;
    
public:
    void connect(function<void(Args...)> handler) {
        handlers.push_back(handler);
    }
    
    void emit(Args... args) {
        for (auto& handler : handlers) {
            handler(args...);
        }
    }
    
    size_t handlerCount() const {
        return handlers.size();
    }
};

// Variadic template for method chaining
class ChainBuilder {
private:
    string result;
    
public:
    template <typename... Args>
    ChainBuilder& add(Args&&... args) {
        ((result += to_string(args)), ...);
        return *this;
    }
    
    template <typename... Args>
    ChainBuilder& addWithSpace(Args&&... args) {
        ((result += to_string(args) + " "), ...);
        return *this;
    }
    
    string build() const {
        return result;
    }
    
    void reset() {
        result.clear();
    }
};

// Variadic template for tuple operations
template <typename... Types>
class TupleOperations {
private:
    tuple<Types...> data;
    
public:
    TupleOperations(Types... args) : data(args...) {}
    
    template <typename Func>
    void apply(Func&& func) {
        applyHelper(func, make_index_sequence<sizeof...(Types)>{});
    }
    
    template <typename Func, size_t... Indices>
    void applyHelper(Func&& func, index_sequence<Indices...>) {
        (func(get<Indices>(data)), ...);
    }
    
    auto toString() const {
        return toStringHelper(make_index_sequence<sizeof...(Types)>{});
    }
    
    template <size_t... Indices>
    string toStringHelper(index_sequence<Indices...>) const {
        stringstream ss;
        ss << "(";
        ((ss << get<Indices>(data) << (Indices + 1 < sizeof...(Types) ? ", " : "")), ...);
        ss << ")";
        return ss.str();
    }
};

int main() {
    cout << "=== Practical Variadic Template Applications ===" << endl;
    
    // String formatter
    string formatted = format("Hello {}, you are {} years old and your score is {}", 
                             "Alice", 25, 95.5);
    cout << "Formatted: " << formatted << endl;
    
    cout << endl;
    
    // Logger
    Logger logger("app.log");
    logger.info("Application started");
    logger.info("User {} logged in from IP {}", "john_doe", "192.168.1.100");
    logger.error("Database connection failed: {}", "Connection timeout");
    
    cout << endl;
    
    // Event system
    Event<string, int> userEvent;
    
    userEvent.connect([](string name, int score) {
        cout << "Handler 1: User " << name << " scored " << score << endl;
    });
    
    userEvent.connect([](string name, int score) {
        cout << "Handler 2: Score " << score << " saved for " << name << endl;
    });
    
    cout << "Emitting event with 2 handlers:" << endl;
    userEvent.emit("Alice", 100);
    
    cout << endl;
    
    // Method chaining
    ChainBuilder builder;
    string result = builder.add(1).addWithSpace(2, 3).add(4).build();
    cout << "Chain result: " << result << endl;
    
    builder.reset();
    result = builder.add("Hello").addWithSpace("World", 2024).build();
    cout << "Chain result 2: " << result << endl;
    
    cout << endl;
    
    // Tuple operations
    TupleOperations<int, string, double> tupleOps(42, "Hello", 3.14);
    
    cout << "Tuple: " << tupleOps.toString() << endl;
    
    cout << "Applying function to all elements:" << endl;
    tupleOps.apply([](const auto& elem) {
        cout << "  Element: " << elem << endl;
    });
    
    return 0;
}
```

---

## 🎮 Complete Example: Variadic Template Library

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include <functional>
#include <any>
using namespace std;

// Variadic template signal/slot system
template <typename... Args>
class Signal {
private:
    vector<function<void(Args...)>> slots;
    
public:
    // Connect a slot (function)
    void connect(function<void(Args...)> slot) {
        slots.push_back(slot);
    }
    
    // Connect a member function
    template <typename T>
    void connect(T* obj, void (T::*method)(Args...)) {
        slots.push_back([obj, method](Args... args) {
            (obj->*method)(args...);
        });
    }
    
    // Emit signal to all connected slots
    void emit(Args... args) {
        for (auto& slot : slots) {
            slot(args...);
        }
    }
    
    // Disconnect all slots
    void disconnect() {
        slots.clear();
    }
    
    size_t slotCount() const {
        return slots.size();
    }
};

// Variadic template factory
template <typename BaseType, typename... Args>
unique_ptr<BaseType> create(Args&&... args) {
    return make_unique<BaseType>(forward<Args>(args)...);
}

// Variadic template property system
template <typename... Types>
class PropertyBag {
private:
    tuple<Types...> properties;
    
public:
    PropertyBag(Types... props) : properties(props...) {}
    
    template <size_t Index>
    auto get() {
        return get<Index>(properties);
    }
    
    template <size_t Index>
    void set(typename tuple_element<Index, tuple<Types...>>::type value) {
        get<Index>(properties) = value;
    }
    
    void printAll() const {
        printHelper(make_index_sequence<sizeof...(Types)>{});
    }
    
private:
    template <size_t... Indices>
    void printHelper(index_sequence<Indices...>) const {
        ((cout << "Property " << Indices << ": " << get<Indices>(properties) << endl), ...);
    }
};

// Variadic template command pattern
template <typename... Args>
class Command {
private:
    function<void(Args...)> action;
    tuple<Args...> arguments;
    bool executed = false;
    
public:
    Command(function<void(Args...)> cmd, Args... args) 
        : action(cmd), arguments(args...) {}
    
    void execute() {
        if (!executed) {
            apply(action, arguments);
            executed = true;
        }
    }
    
    bool isExecuted() const {
        return executed;
    }
};

// Variadic template validator
template <typename... Validators>
class Validator {
private:
    tuple<Validators...> validators;
    
public:
    Validator(Validators... valids) : validators(valids...) {}
    
    template <typename T>
    bool validate(const T& value) const {
        return validateHelper(value, make_index_sequence<sizeof...(Validators)>{});
    }
    
private:
    template <typename T, size_t... Indices>
    bool validateHelper(const T& value, index_sequence<Indices...>) const {
        return (get<Indices>(validators)(value) && ...);
    }
};

// Example validator functions
auto isPositive = [](int value) { return value > 0; };
auto isEven = [](int value) { return value % 2 == 0; };
auto isLessThan100 = [](int value) { return value < 100; };

// Test classes for signal/slot demo
class Button {
public:
    Signal<> onClick;
    
    void click() {
        cout << "Button clicked!" << endl;
        onClick.emit();
    }
};

class Dialog {
public:
    void onButtonClicked() {
        cout << "Dialog: Button was clicked!" << endl;
    }
    
    void showMessageBox() {
        cout << "Dialog: Showing message box" << endl;
    }
};

int main() {
    cout << "=== Variadic Template Library Demo ===" << endl;
    
    // Signal/Slot system
    cout << "Signal/Slot System:" << endl;
    Button button;
    Dialog dialog;
    
    // Connect lambda
    button.onClick.connect([]() {
        cout << "Lambda handler: Button clicked!" << endl;
    });
    
    // Connect member function
    button.onClick.connect(&dialog, &Dialog::onButtonClicked);
    button.onClick.connect(&dialog, &Dialog::showMessageBox);
    
    cout << "Connected " << button.onClick.slotCount() << " slots" << endl;
    button.click();
    
    cout << endl;
    
    // Factory pattern
    cout << "Factory Pattern:" << endl;
    auto intPtr = create<int>(42);
    auto stringPtr = create<string>("Hello from factory");
    
    cout << "Created int: " << *intPtr << endl;
    cout << "Created string: " << *stringPtr << endl;
    
    cout << endl;
    
    // Property bag
    cout << "Property Bag:" << endl;
    PropertyBag<int, string, double, bool> props(25, "Property", 3.14, true);
    props.printAll();
    
    props.set<0>(100);
    props.set<2>(2.71);
    cout << "After modification:" << endl;
    props.printAll();
    
    cout << endl;
    
    // Command pattern
    cout << "Command Pattern:" << endl;
    auto printCommand = [](const string& msg, int times) {
        for (int i = 0; i < times; i++) {
            cout << msg << " ";
        }
        cout << endl;
    };
    
    Command<string, int> cmd1(printCommand, "Hello", 3);
    Command<string, int> cmd2(printCommand, "World", 2);
    
    cout << "Executing command 1:" << endl;
    cmd1.execute();
    cout << "Command 1 executed: " << cmd1.isExecuted() << endl;
    
    cout << "Executing command 2:" << endl;
    cmd2.execute();
    
    cout << endl;
    
    // Validator system
    cout << "Validator System:" << endl;
    Validator<decltype(isPositive), decltype(isEven), decltype(isLessThan100)> 
        positiveEvenValidator(isPositive, isEven, isLessThan100);
    
    cout << "Validating 4: " << (positiveEvenValidator.validate(4) ? "Valid" : "Invalid") << endl;
    cout << "Validating 8: " << (positiveEvenValidator.validate(8) ? "Valid" : "Invalid") << endl;
    cout << "Validating 10: " << (positiveEvenValidator.validate(10) ? "Valid" : "Invalid") << endl;
    cout << "Validating 12: " << (positiveEvenValidator.validate(12) ? "Valid" : "Invalid") << endl;
    cout << "Validating 14: " << (positiveEvenValidator.validate(14) ? "Valid" : "Invalid") << endl;
    
    return 0;
}
```

---

## ⚡ Performance Considerations

### Advantages
- ✅ **Compile-Time Optimization**: All processing happens at compile time
- ✅ **Type Safety**: Strong typing with template constraints
- ✅ **Zero Overhead**: No runtime cost for variadic features
- ✅ **Flexibility**: Handle any number of arguments

### Considerations
- ⚠️ **Compilation Time**: Can significantly increase build time
- ⚠️ **Code Bloat**: Multiple instantiations increase binary size
- ⚠️ **Error Messages**: Can be complex and hard to understand
- ⚠️ **Debugging**: More difficult to debug template code

---

## 🐛 Common Pitfalls

| Problem | Solution |
|---------|----------|
| **Recursive instantiation depth** | Use fold expressions (C++17) instead of recursion |
| **Ambiguous overloads** | Be specific with template constraints |
| **Pack expansion in wrong context** | Understand where pack expansion is allowed |
| **Perfect forwarding issues** | Use `std::forward` correctly with `Args&&...` |

---

## ✅ Best Practices

1. **Prefer fold expressions** over recursion when using C++17
2. **Use `std::forward`** for perfect forwarding
3. **Add constraints** with concepts (C++20) or SFINAE
4. **Keep variadic templates simple** when possible
5. **Document expected types** and behavior
6. **Use `static_assert`** for better error messages
7. **Consider overload resolution** carefully

---

## 📚 Related Topics

- [Function Templates](01_Function_Templates.md)
- [Class Templates](02_Class_Templates.md)
- [Template Specialization](03_Template_Specialization.md)
- [Template Metaprogramming](05_Template_Metaprogramming.md)

---

## 🚀 Next Steps

Continue learning about:
- **Template Metaprogramming**: Compile-time computation
- **C++20 Concepts**: Modern template constraints
- **Advanced Template Techniques**: SFINAE, tag dispatch, and more
- **STL Implementation**: Understanding how variadic templates power the STL

---
