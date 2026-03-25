# 25_functional.md - Function Objects and Call Wrappers

The `functional` header provides predicates, comparators, and callable wrappers for functional programming patterns in C++.

## 📖 Overview

The `functional` header contains essential utilities for working with callable objects, function pointers, and implementing functional programming patterns. It provides type erasure, function composition, and standard function objects that work seamlessly with STL algorithms.

## 🎯 Key Features

- **Function wrappers** - Type-erased function objects with `std::function`
- **Function binding** - Partial function application with `std::bind`
- **Standard function objects** - Predefined comparators and operations
- **Negators** - Logical negation of predicates
- **Reference wrappers** - Pass objects by reference to function objects
- **Memory management** - Smart pointer utilities for functions

## 🔧 std::function - Type Erasure for Callables

### Basic std::function Usage
```cpp
#include <iostream>
#include <functional>
#include <vector>
#include <algorithm>

void demonstrateFunction() {
    std::cout << "=== std::function Examples ===" << std::endl;
    
    // Store free function
    std::function<int(int, int)> add_func = [](int a, int b) {
        return a + b;
    };
    
    std::cout << "Lambda: 5 + 3 = " << add_func(5, 3) << std::endl;
    
    // Store member function
    class Calculator {
    public:
        int multiply(int a, int b) { return a * b; }
        static int divide(int a, int b) { return a / b; }
    };
    
    Calculator calc;
    std::function<int(int, int)> multiply_func = std::bind(&Calculator::multiply, &calc, 
                                                          std::placeholders::_1, 
                                                          std::placeholders::_2);
    
    std::cout << "Member function: 6 * 7 = " << multiply_func(6, 7) << std::endl;
    
    // Store static member function
    std::function<int(int, int)> divide_func = &Calculator::divide;
    std::cout << "Static function: 20 / 4 = " << divide_func(20, 4) << std::endl;
    
    // Function with no parameters
    std::function<void()> greet_func = []() {
        std::cout << "Hello from function!" << std::endl;
    };
    
    greet_func();
    
    // Function returning void with parameters
    std::function<void(int)> print_func = [](int x) {
        std::cout << "Value: " << x << std::endl;
    };
    
    print_func(42);
}
```

### std::function with Different Callables
```cpp
void demonstrateFunctionTypes() {
    std::cout << "\n=== std::function with Different Callables ===" << std::endl;
    
    // Free function
    auto free_function = [](int x) { return x * 2; };
    
    // Function object (functor)
    struct Doubler {
        int operator()(int x) const { return x * 2; }
    };
    
    // Lambda with capture
    int multiplier = 3;
    auto lambda_with_capture = [multiplier](int x) { return x * multiplier; };
    
    // Store all in std::function
    std::function<int(int)> func1 = free_function;
    std::function<int(int)> func2 = Doubler();
    std::function<int(int)> func3 = lambda_with_capture;
    
    std::cout << "Free function: " << func1(10) << std::endl;
    std::cout << "Function object: " << func2(10) << std::endl;
    std::cout << "Lambda with capture: " << func3(10) << std::endl;
    
    // Function returning another function
    std::function<std::function<int(int)>(int)> make_adder = [](int n) {
        return [n](int x) { return x + n; };
    };
    
    auto add_5 = make_adder(5);
    std::cout << "Curried function: add_5(10) = " << add_5(10) << std::endl;
}
```

## 🔧 std::bind - Partial Function Application

### Basic std::bind Usage
```cpp
void demonstrateBind() {
    std::cout << "\n=== std::bind Examples ===" << std::endl;
    
    // Simple function binding
    auto multiply = [](int a, int b) { return a * b; };
    
    // Bind first argument
    auto multiply_by_2 = std::bind(multiply, 2, std::placeholders::_1);
    std::cout << "multiply_by_2(5) = " << multiply_by_2(5) << std::endl;
    
    // Bind second argument
    auto multiply_5_by = std::bind(multiply, std::placeholders::_1, 5);
    std::cout << "multiply_5_by(3) = " << multiply_5_by(3) << std::endl;
    
    // Bind both arguments
    auto multiply_4_7 = std::bind(multiply, 4, 7);
    std::cout << "multiply_4_7() = " << multiply_4_7() << std::endl;
    
    // Reorder arguments
    auto subtract = [](int a, int b) { return a - b; };
    auto reverse_subtract = std::bind(subtract, std::placeholders::_2, std::placeholders::_1);
    std::cout << "reverse_subtract(3, 10) = " << reverse_subtract(3, 10) << std::endl;
    
    // Member function binding
    class Printer {
    public:
        void print(const std::string& message, int times) const {
            for (int i = 0; i < times; ++i) {
                std::cout << message << " ";
            }
            std::cout << std::endl;
        }
    };
    
    Printer printer;
    auto print_hello = std::bind(&Printer::print, &printer, "Hello", std::placeholders::_1);
    print_hello(3);
}
```

### Advanced std::bind Techniques
```cpp
void demonstrateAdvancedBind() {
    std::cout << "\n=== Advanced std::bind Techniques ===" << std::endl;
    
    // Bind with function composition
    auto add = [](int a, int b) { return a + b; };
    auto square = [](int x) { return x * x; };
    
    // Create function that squares sum of two numbers
    auto square_of_sum = std::bind(square, std::bind(add, std::placeholders::_1, std::placeholders::_2));
    std::cout << "square_of_sum(3, 4) = " << square_of_sum(3, 4) << std::endl;
    
    // Bind with multiple placeholders
    auto process_three = [](int a, int b, int c) {
        return a * b + c;
    };
    
    auto bind_first = std::bind(process_three, 2, std::placeholders::_1, std::placeholders::_2);
    auto bind_second = std::bind(process_three, std::placeholders::_1, 3, std::placeholders::_2);
    auto bind_third = std::bind(process_three, std::placeholders::_1, std::placeholders::_2, 4);
    
    std::cout << "bind_first(5, 6) = " << bind_first(5, 6) << std::endl;
    std::cout << "bind_second(5, 6) = " << bind_second(5, 6) << std::endl;
    std::cout << "bind_third(5, 6) = " << bind_third(5, 6) << std::endl;
    
    // Using std::bind with STL algorithms
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    std::vector<int> results;
    
    // Transform using bound function
    std::transform(numbers.begin(), numbers.end(), std::back_inserter(results),
                  std::bind(multiply, std::placeholders::_1, 10));
    
    std::cout << "Original: ";
    for (int n : numbers) std::cout << n << " ";
    std::cout << std::endl;
    
    std::cout << "Multiplied by 10: ";
    for (int r : results) std::cout << r << " ";
    std::cout << std::endl;
}
```

## 🔧 Standard Function Objects

### Comparison Objects
```cpp
void demonstrateComparators() {
    std::cout << "\n=== Standard Comparison Objects ===" << std::endl;
    
    std::vector<int> numbers = {5, 2, 8, 1, 9, 3};
    
    // Sort with different comparators
    std::vector<int> ascending = numbers;
    std::sort(ascending.begin(), ascending.end(), std::less<int>());
    
    std::vector<int> descending = numbers;
    std::sort(descending.begin(), descending.end(), std::greater<int>());
    
    std::cout << "Ascending: ";
    for (int n : ascending) std::cout << n << " ";
    std::cout << std::endl;
    
    std::cout << "Descending: ";
    for (int n : descending) std::cout << n << " ";
    std::cout << std::endl;
    
    // Custom comparison with standard objects
    std::vector<std::pair<int, std::string>> pairs = {
        {3, "three"}, {1, "one"}, {2, "two"}
    };
    
    // Sort by first element using less
    std::sort(pairs.begin(), pairs.end(),
              std::less<std::pair<int, std::string>>());
    
    std::cout << "Pairs sorted by first element: ";
    for (const auto& p : pairs) {
        std::cout << "(" << p.first << "," << p.second << ") ";
    }
    std::cout << std::endl;
    
    // Use with std::map
    std::map<int, std::string, std::greater<int>> reverse_map;
    reverse_map[1] = "one";
    reverse_map[3] = "three";
    reverse_map[2] = "two";
    
    std::cout << "Map with greater comparator: ";
    for (const auto& [key, value] : reverse_map) {
        std::cout << "(" << key << "," << value << ") ";
    }
    std::cout << std::endl;
}
```

### Arithmetic and Logical Operations
```cpp
void demonstrateArithmeticLogical() {
    std::cout << "\n=== Arithmetic and Logical Operations ===" << std::endl;
    
    std::vector<int> numbers1 = {1, 2, 3, 4, 5};
    std::vector<int> numbers2 = {5, 4, 3, 2, 1};
    std::vector<int> results;
    
    // Element-wise addition
    std::transform(numbers1.begin(), numbers1.end(),
                  numbers2.begin(), std::back_inserter(results),
                  std::plus<int>());
    
    std::cout << "Addition: ";
    for (int r : results) std::cout << r << " ";
    std::cout << std::endl;
    
    // Element-wise multiplication
    results.clear();
    std::transform(numbers1.begin(), numbers1.end(),
                  numbers2.begin(), std::back_inserter(results),
                  std::multiplies<int>());
    
    std::cout << "Multiplication: ";
    for (int r : results) std::cout << r << " ";
    std::cout << std::endl;
    
    // Logical operations
    std::vector<bool> bool1 = {true, false, true, false, true};
    std::vector<bool> bool2 = {true, true, false, false, true};
    std::vector<bool> bool_results;
    
    std::transform(bool1.begin(), bool1.end(),
                  bool2.begin(), std::back_inserter(bool_results),
                  std::logical_and<bool>());
    
    std::cout << "Logical AND: ";
    for (bool b : bool_results) std::cout << (b ? "T" : "F") << " ";
    std::cout << std::endl;
    
    // Bitwise operations
    results.clear();
    std::transform(numbers1.begin(), numbers1.end(),
                  numbers2.begin(), std::back_inserter(results),
                  std::bit_and<int>());
    
    std::cout << "Bitwise AND: ";
    for (int r : results) std::cout << r << " ";
    std::cout << std::endl;
}
```

## 🔧 std::not_fn and Negators

### Predicate Negation
```cpp
void demonstrateNotFn() {
    std::cout << "\n=== std::not_fn Examples ===" << std::endl;
    
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // Original predicate
    auto is_even = [](int x) { return x % 2 == 0; };
    
    // Negated predicate
    auto is_odd = std::not_fn(is_even);
    
    std::vector<int> evens, odds;
    std::copy_if(numbers.begin(), numbers.end(), std::back_inserter(evens), is_even);
    std::copy_if(numbers.begin(), numbers.end(), std::back_inserter(odds), is_odd);
    
    std::cout << "Even numbers: ";
    for (int n : evens) std::cout << n << " ";
    std::cout << std::endl;
    
    std::cout << "Odd numbers: ";
    for (int n : odds) std::cout << n << " ";
    std::cout << std::endl;
    
    // Negate standard function objects
    auto not_less = std::not_fn(std::less<int>());
    std::vector<int> sorted_desc = numbers;
    std::sort(sorted_desc.begin(), sorted_desc.end(), not_less);
    
    std::cout << "Sorted with not_less: ";
    for (int n : sorted_desc) std::cout << n << " ";
    std::cout << std::endl;
    
    // Complex predicate negation
    auto is_prime = [](int n) {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; ++i) {
            if (n % i == 0) return false;
        }
        return true;
    };
    
    auto is_composite = std::not_fn(is_prime);
    std::vector<int> primes, composites;
    std::copy_if(numbers.begin(), numbers.end(), std::back_inserter(primes), is_prime);
    std::copy_if(numbers.begin(), numbers.end(), std::back_inserter(composites), is_composite);
    
    std::cout << "Prime numbers: ";
    for (int n : primes) std::cout << n << " ";
    std::cout << std::endl;
    
    std::cout << "Composite numbers: ";
    for (int n : composites) std::cout << n << " ";
    std::cout << std::endl;
}
```

## 🔧 Reference Wrappers

### std::ref and std::cref
```cpp
void demonstrateReferenceWrappers() {
    std::cout << "\n=== Reference Wrapper Examples ===" << std::endl;
    
    // Problem: function objects copy their arguments
    auto modify_value = [](int& x) { x *= 2; };
    
    int value = 5;
    // modify_value(value);  // Error: can't bind temporary to int&
    
    // Solution: use reference wrapper
    auto modify_with_ref = [](std::reference_wrapper<int> ref) {
        ref.get() *= 2;
    };
    
    modify_with_ref(std::ref(value));
    std::cout << "Value after modification: " << value << std::endl;
    
    // Using reference wrappers with std::bind
    void print_and_modify(int& x, const std::string& prefix) {
        std::cout << prefix << x << std::endl;
        x += 10;
    }
    
    int number = 42;
    auto bound_print = std::bind(print_and_modify, std::ref(number), "Number: ");
    bound_print();
    std::cout << "Number after bind call: " << number << std::endl;
    
    // Using with STL algorithms
    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::for_each(vec.begin(), vec.end(), [](int& x) { x *= 3; });
    
    std::cout << "Vector after for_each: ";
    for (int n : vec) std::cout << n << " ";
    std::cout << std::endl;
    
    // const reference wrapper
    const int const_value = 100;
    auto use_const_ref = [](std::reference_wrapper<const int> ref) {
        std::cout << "Const value: " << ref.get() << std::endl;
    };
    
    use_const_ref(std::cref(const_value));
}
```

## 🎮 Practical Examples

### Example 1: Event System with std::function
```cpp
#include <iostream>
#include <functional>
#include <vector>
#include <string>
#include <unordered_map>
#include <memory>

class EventSystem {
private:
    using EventCallback = std::function<void(const std::string&)>;
    std::unordered_map<std::string, std::vector<EventCallback>> listeners;
    
public:
    // Subscribe to an event
    void subscribe(const std::string& event_name, EventCallback callback) {
        listeners[event_name].push_back(callback);
    }
    
    // Emit an event
    void emit(const std::string& event_name, const std::string& data) {
        auto it = listeners.find(event_name);
        if (it != listeners.end()) {
            for (const auto& callback : it->second) {
                callback(data);
            }
        }
    }
    
    // Unsubscribe all listeners for an event
    void unsubscribe(const std::string& event_name) {
        listeners.erase(event_name);
    }
    
    // Get number of listeners for an event
    size_t getListenerCount(const std::string& event_name) const {
        auto it = listeners.find(event_name);
        return it != listeners.end() ? it->second.size() : 0;
    }
};

class Player {
private:
    std::string name;
    int health;
    EventSystem* event_system;
    
public:
    Player(const std::string& n, int h, EventSystem* es) 
        : name(n), health(h), event_system(es) {
        
        // Subscribe to events with member functions
        event_system->subscribe("damage", 
            std::bind(&Player::takeDamage, this, std::placeholders::_1));
        
        event_system->subscribe("heal",
            std::bind(&Player::heal, this, std::placeholders::_1));
    }
    
    void takeDamage(const std::string& damage_str) {
        int damage = std::stoi(damage_str);
        health -= damage;
        std::cout << name << " took " << damage << " damage, health: " << health << std::endl;
        
        if (health <= 0) {
            event_system->emit("player_death", name);
        }
    }
    
    void heal(const std::string& heal_str) {
        int heal_amount = std::stoi(heal_str);
        health += heal_amount;
        std::cout << name << " healed " << heal_amount << ", health: " << health << std::endl;
    }
    
    int getHealth() const { return health; }
};

int main() {
    std::cout << "=== Event System Example ===" << std::endl;
    
    EventSystem event_system;
    
    // Create players
    Player player1("Alice", 100, &event_system);
    Player player2("Bob", 80, &event_system);
    
    // Add lambda listener for death events
    event_system.subscribe("player_death", [](const std::string& player_name) {
        std::cout << "💀 " << player_name << " has died!" << std::endl;
    });
    
    // Add logging listener
    event_system.subscribe("damage", [](const std::string& damage_str) {
        std::cout << "📝 Damage event: " << damage_str << std::endl;
    });
    
    // Simulate game events
    std::cout << "\n--- Game Events ---" << std::endl;
    event_system.emit("damage", "20");  // Both players take 20 damage
    event_system.emit("heal", "10");   // Both players heal 10
    event_system.emit("damage", "50");  // Both players take 50 damage
    event_system.emit("damage", "30");  // Bob dies, Alice survives
    
    std::cout << "\n--- Final Status ---" << std::endl;
    std::cout << "Alice health: " << player1.getHealth() << std::endl;
    std::cout << "Bob health: " << player2.getHealth() << std::endl;
    
    return 0;
}
```

### Example 2: Command Pattern with std::function
```cpp
#include <iostream>
#include <functional>
#include <vector>
#include <stack>
#include <string>
#include <memory>

// Command interface using std::function
class Command {
public:
    virtual ~Command() = default;
    virtual void execute() = 0;
    virtual void undo() = 0;
    virtual std::string getDescription() const = 0;
};

// Concrete command class
class SimpleCommand : public Command {
private:
    std::function<void()> action;
    std::function<void()> undo_action;
    std::string description;
    
public:
    SimpleCommand(std::function<void()> act, std::function<void()> undo, const std::string& desc)
        : action(act), undo_action(undo), description(desc) {}
    
    void execute() override {
        action();
    }
    
    void undo() override {
        undo_action();
    }
    
    std::string getDescription() const override {
        return description;
    }
};

// Command Invoker
class TextEditor {
private:
    std::string text;
    std::stack<std::unique_ptr<Command>> history;
    
public:
    TextEditor() : text("") {}
    
    void executeCommand(std::unique_ptr<Command> command) {
        command->execute();
        history.push(std::move(command));
    }
    
    void undo() {
        if (!history.empty()) {
            history.top()->undo();
            history.pop();
        }
    }
    
    void append(const std::string& str) {
        text += str;
    }
    
    void erase(int count) {
        if (count <= static_cast<int>(text.length())) {
            text.erase(text.length() - count);
        }
    }
    
    void setText(const std::string& new_text) {
        text = new_text;
    }
    
    std::string getText() const {
        return text;
    }
    
    void display() const {
        std::cout << "Current text: \"" << text << "\"" << std::endl;
    }
};

// Command Factory
class CommandFactory {
public:
    static std::unique_ptr<Command> createAppendCommand(TextEditor* editor, const std::string& text) {
        return std::make_unique<SimpleCommand>(
            [editor, text]() { editor->append(text); },
            [editor, text]() { editor->erase(text.length()); },
            "Append: " + text
        );
    }
    
    static std::unique_ptr<Command> createSetTextCommand(TextEditor* editor, const std::string& new_text) {
        std::string old_text = editor->getText();
        return std::make_unique<SimpleCommand>(
            [editor, new_text]() { editor->setText(new_text); },
            [editor, old_text]() { editor->setText(old_text); },
            "Set text: " + new_text
        );
    }
    
    static std::unique_ptr<Command> createEraseCommand(TextEditor* editor, int count) {
        return std::make_unique<SimpleCommand>(
            [editor, count]() { editor->erase(count); },
            [editor, count]() { 
                // Note: This is simplified - real implementation would store erased text
                editor->append("???"); 
            },
            "Erase " + std::to_string(count) + " characters"
        );
    }
};

int main() {
    std::cout << "=== Command Pattern Example ===" << std::endl;
    
    TextEditor editor;
    
    // Execute commands
    std::cout << "\n--- Executing Commands ---" << std::endl;
    
    auto cmd1 = CommandFactory::createAppendCommand(&editor, "Hello");
    cmd1->execute();
    editor.display();
    
    auto cmd2 = CommandFactory::createAppendCommand(&editor, " World");
    cmd2->execute();
    editor.display();
    
    auto cmd3 = CommandFactory::createSetTextCommand(&editor, "Goodbye");
    cmd3->execute();
    editor.display();
    
    auto cmd4 = CommandFactory::createAppendCommand(&editor, "!");
    cmd4->execute();
    editor.display();
    
    // Use command invoker with history
    TextEditor editor_with_history;
    
    std::cout << "\n--- Using Command Invoker ---" << std::endl;
    
    editor_with_history.executeCommand(CommandFactory::createAppendCommand(&editor_with_history, "Start"));
    editor_with_history.display();
    
    editor_with_history.executeCommand(CommandFactory::createAppendCommand(&editor_with_history, " Middle"));
    editor_with_history.display();
    
    editor_with_history.executeCommand(CommandFactory::createAppendCommand(&editor_with_history, " End"));
    editor_with_history.display();
    
    // Undo operations
    std::cout << "\n--- Undoing Operations ---" << std::endl;
    editor_with_history.undo();
    editor_with_history.display();
    
    editor_with_history.undo();
    editor_with_history.display();
    
    editor_with_history.undo();
    editor_with_history.display();
    
    return 0;
}
```

### Example 3: Strategy Pattern with std::function
```cpp
#include <iostream>
#include <functional>
#include <vector>
#include <algorithm>
#include <numeric>

class DataProcessor {
private:
    std::vector<int> data;
    
public:
    DataProcessor(const std::vector<int>& d) : data(d) {}
    
    // Strategy using std::function
    void process(std::function<std::vector<int>(const std::vector<int>&)> strategy) {
        data = strategy(data);
    }
    
    // Filter strategy
    void filter(std::function<bool(int)> predicate) {
        data.erase(
            std::remove_if(data.begin(), data.end(),
                          [predicate](int x) { return !predicate(x); }),
            data.end()
        );
    }
    
    // Transform strategy
    void transform(std::function<int(int)> transformer) {
        std::transform(data.begin(), data.end(), data.begin(), transformer);
    }
    
    // Aggregate strategy
    template<typename T>
    T aggregate(std::function<T(T, int)> aggregator, T initial) const {
        return std::accumulate(data.begin(), data.end(), initial, aggregator);
    }
    
    void display(const std::string& label) const {
        std::cout << label << ": ";
        for (int x : data) std::cout << x << " ";
        std::cout << std::endl;
    }
    
    size_t size() const { return data.size(); }
};

// Strategy functions
namespace strategies {
    // Remove even numbers
    std::vector<int> removeEven(const std::vector<int>& data) {
        std::vector<int> result;
        std::copy_if(data.begin(), data.end(), std::back_inserter(result),
                    [](int x) { return x % 2 != 0; });
        return result;
    }
    
    // Sort and remove duplicates
    std::vector<int> uniqueSorted(const std::vector<int>& data) {
        std::vector<int> result = data;
        std::sort(result.begin(), result.end());
        result.erase(std::unique(result.begin(), result.end()), result.end());
        return result;
    }
    
    // Keep only prime numbers
    std::vector<int> keepPrimes(const std::vector<int>& data) {
        std::vector<int> result;
        std::copy_if(data.begin(), data.end(), std::back_inserter(result),
                    [](int n) {
                        if (n < 2) return false;
                        for (int i = 2; i * i <= n; ++i) {
                            if (n % i == 0) return false;
                        }
                        return true;
                    });
        return result;
    }
    
    // Square all numbers
    std::vector<int> squareAll(const std::vector<int>& data) {
        std::vector<int> result;
        std::transform(data.begin(), data.end(), std::back_inserter(result),
                      [](int x) { return x * x; });
        return result;
    }
}

int main() {
    std::cout << "=== Strategy Pattern Example ===" << std::endl;
    
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 3, 1};
    DataProcessor processor(numbers);
    
    processor.display("Original data");
    
    // Apply different strategies
    std::cout << "\n--- Applying Different Strategies ---" << std::endl;
    
    // Strategy 1: Remove even numbers
    DataProcessor processor1(numbers);
    processor1.process(strategies::removeEven);
    processor1.display("After removing evens");
    
    // Strategy 2: Unique and sorted
    DataProcessor processor2(numbers);
    processor2.process(strategies::uniqueSorted);
    processor2.display("After unique sort");
    
    // Strategy 3: Keep primes
    DataProcessor processor3(numbers);
    processor3.process(strategies::keepPrimes);
    processor3.display("After keeping primes");
    
    // Strategy 4: Square all
    DataProcessor processor4(numbers);
    processor4.process(strategies::squareAll);
    processor4.display("After squaring all");
    
    // Chain strategies with lambdas
    std::cout << "\n--- Chaining Strategies ---" << std::endl;
    
    DataProcessor processor5(numbers);
    
    // Chain: remove evens, then square, then sort
    auto chain_strategy = [](const std::vector<int>& data) {
        auto step1 = strategies::removeEven(data);
        auto step2 = strategies::squareAll(step1);
        std::sort(step2.begin(), step2.end());
        return step2;
    };
    
    processor5.process(chain_strategy);
    processor5.display("After chaining strategies");
    
    // Using individual strategy methods
    std::cout << "\n--- Using Individual Strategy Methods ---" << std::endl;
    
    DataProcessor processor6(numbers);
    processor6.display("Start");
    
    // Filter strategy
    processor6.filter([](int x) { return x > 5; });
    processor6.display("After filter > 5");
    
    // Transform strategy
    processor6.transform([](int x) { return x * 2; });
    processor6.display("After transform * 2");
    
    // Aggregate strategy
    int sum = processor6.aggregate<int>([](int acc, int x) { return acc + x; }, 0);
    std::cout << "Sum of all elements: " << sum << std::endl;
    
    int product = processor6.aggregate<int>([](int acc, int x) { return acc * x; }, 1);
    std::cout << "Product of all elements: " << product << std::endl;
    
    return 0;
}
```

### Example 4: Functional Programming Utilities
```cpp
#include <iostream>
#include <functional>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>

class FunctionalUtils {
public:
    // Map function
    template<typename T, typename R>
    static std::vector<R> map(const std::vector<T>& vec, std::function<R(T)> func) {
        std::vector<R> result;
        std::transform(vec.begin(), vec.end(), std::back_inserter(result), func);
        return result;
    }
    
    // Filter function
    template<typename T>
    static std::vector<T> filter(const std::vector<T>& vec, std::function<bool(T)> predicate) {
        std::vector<T> result;
        std::copy_if(vec.begin(), vec.end(), std::back_inserter(result), predicate);
        return result;
    }
    
    // Reduce function
    template<typename T>
    static T reduce(const std::vector<T>& vec, std::function<T(T, T)> func, T initial) {
        return std::accumulate(vec.begin(), vec.end(), initial, func);
    }
    
    // Compose functions
    template<typename F, typename G>
    static auto compose(F f, G g) {
        return [f, g](auto x) { return f(g(x)); };
    }
    
    // Pipeline functions
    template<typename T, typename... Funcs>
    static auto pipeline(T value, Funcs... funcs) {
        return (value | ... | funcs);
    }
    
    // Curry function (simplified for binary functions)
    template<typename F, typename Arg1>
    static auto curry(F f, Arg1 arg1) {
        return [f, arg1](auto arg2) { return f(arg1, arg2); };
    }
    
    // Partial application
    template<typename F, typename... Args>
    static auto partial(F f, Args... args) {
        return [f, args...](auto... remaining_args) {
            return f(args..., remaining_args...);
        };
    }
};

int main() {
    std::cout << "=== Functional Programming Utilities ===" << std::endl;
    
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // Map examples
    std::cout << "\n--- Map Examples ---" << std::endl;
    
    auto doubled = FunctionalUtils::map<int, int>(numbers, [](int x) { return x * 2; });
    std::cout << "Doubled: ";
    for (int x : doubled) std::cout << x << " ";
    std::cout << std::endl;
    
    auto squared = FunctionalUtils::map<int, int>(numbers, [](int x) { return x * x; });
    std::cout << "Squared: ";
    for (int x : squared) std::cout << x << " ";
    std::cout << std::endl;
    
    auto as_strings = FunctionalUtils::map<int, std::string>(numbers, [](int x) { 
        return std::to_string(x); 
    });
    std::cout << "As strings: ";
    for (const auto& s : as_strings) std::cout << s << " ";
    std::cout << std::endl;
    
    // Filter examples
    std::cout << "\n--- Filter Examples ---" << std::endl;
    
    auto evens = FunctionalUtils::filter<int>(numbers, [](int x) { return x % 2 == 0; });
    std::cout << "Even numbers: ";
    for (int x : evens) std::cout << x << " ";
    std::cout << std::endl;
    
    auto greater_than_5 = FunctionalUtils::filter<int>(numbers, [](int x) { return x > 5; });
    std::cout << "Greater than 5: ";
    for (int x : greater_than_5) std::cout << x << " ";
    std::cout << std::endl;
    
    // Reduce examples
    std::cout << "\n--- Reduce Examples ---" << std::endl;
    
    int sum = FunctionalUtils::reduce<int>(numbers, [](int a, int b) { return a + b; }, 0);
    std::cout << "Sum: " << sum << std::endl;
    
    int product = FunctionalUtils::reduce<int>(numbers, [](int a, int b) { return a * b; }, 1);
    std::cout << "Product: " << product << std::endl;
    
    int maximum = FunctionalUtils::reduce<int>(numbers, [](int a, int b) { return std::max(a, b); }, numbers[0]);
    std::cout << "Maximum: " << maximum << std::endl;
    
    // Function composition
    std::cout << "\n--- Function Composition ---" << std::endl;
    
    auto add_one = [](int x) { return x + 1; };
    auto double_it = [](int x) { return x * 2; };
    auto square_it = [](int x) { return x * x; };
    
    auto add_then_double = FunctionalUtils::compose(double_it, add_one);
    auto double_then_square = FunctionalUtils::compose(square_it, double_it);
    auto composed = FunctionalUtils::compose(double_then_square, add_then_double);
    
    std::cout << "add_then_double(5) = " << add_then_double(5) << std::endl;
    std::cout << "double_then_square(5) = " << double_then_square(5) << std::endl;
    std::cout << "composed(5) = " << composed(5) << std::endl;
    
    // Currying
    std::cout << "\n--- Currying ---" << std::endl;
    
    auto add = [](int a, int b) { return a + b; };
    auto add_5 = FunctionalUtils::curry(add, 5);
    auto add_10 = FunctionalUtils::curry(add, 10);
    
    std::cout << "add_5(3) = " << add_5(3) << std::endl;
    std::cout << "add_10(7) = " << add_10(7) << std::endl;
    
    // Partial application
    std::cout << "\n--- Partial Application ---" << std::endl;
    
    auto multiply = [](int a, int b, int c) { return a * b * c; };
    auto multiply_by_2_3 = FunctionalUtils::partial(multiply, 2, 3);
    
    std::cout << "multiply_by_2_3(4) = " << multiply_by_2_3(4) << std::endl;
    
    // Chain operations
    std::cout << "\n--- Chained Operations ---" << std::endl;
    
    auto result = numbers;
    result = FunctionalUtils::filter<int>(result, [](int x) { return x % 2 == 0; });
    result = FunctionalUtils::map<int, int>(result, [](int x) { return x * x; });
    int final_sum = FunctionalUtils::reduce<int>(result, [](int a, int b) { return a + b; }, 0);
    
    std::cout << "Sum of squares of even numbers: " << final_sum << std::endl;
    
    return 0;
}
```

## 📊 Complete Function Reference

### Function Wrappers
| Function | Description | Template Parameters |
|----------|-------------|-------------------|
| `std::function<R(Args...)>` | Type-erased function wrapper | R: return type, Args: parameter types |

### Function Binding
| Function | Description | Notes |
|----------|-------------|-------|
| `std::bind(f, args...)` | Bind function arguments | Use `std::placeholders::_1, _2, ...` for unbound arguments |

### Standard Function Objects
| Function | Description | Category |
|----------|-------------|----------|
| `std::plus<T>` | Addition | Arithmetic |
| `std::minus<T>` | Subtraction | Arithmetic |
| `std::multiplies<T>` | Multiplication | Arithmetic |
| `std::divides<T>` | Division | Arithmetic |
| `std::modulus<T>` | Modulo | Arithmetic |
| `std::negate<T>` | Negation | Arithmetic |
| `std::equal_to<T>` | Equality | Comparison |
| `std::not_equal_to<T>` | Inequality | Comparison |
| `std::greater<T>` | Greater than | Comparison |
| `std::less<T>` | Less than | Comparison |
| `std::greater_equal<T>` | Greater or equal | Comparison |
| `std::less_equal<T>` | Less or equal | Comparison |
| `std::logical_and<T>` | Logical AND | Logical |
| `std::logical_or<T>` | Logical OR | Logical |
| `std::logical_not<T>` | Logical NOT | Logical |
| `std::bit_and<T>` | Bitwise AND | Bitwise |
| `std::bit_or<T>` | Bitwise OR | Bitwise |
| `std::bit_xor<T>` | Bitwise XOR | Bitwise |

### Negators
| Function | Description | C++ Version |
|----------|-------------|------------|
| `std::not_fn(f)` | Create negated predicate | C++17 |
| `std::not1(pred)` | Negate unary predicate | Pre-C++17 |
| `std::not2(pred)` | Negate binary predicate | Pre-C++17 |

### Reference Wrappers
| Function | Description | Notes |
|----------|-------------|-------|
| `std::ref(obj)` | Reference wrapper | Allows passing by reference |
| `std::cref(obj)` | Const reference wrapper | Const reference |

## ⚡ Performance Considerations

### std::function Overhead
```cpp
// Direct function call - fastest
void direct_call(int x) { /* ... */ }

// Function pointer - slight overhead
void (*func_ptr)(int) = direct_call;

// std::function - most overhead
std::function<void(int)> func = direct_call;
```

### Lambda vs std::bind
```cpp
// std::bind - more overhead
auto bound = std::bind(add, 5, std::placeholders::_1);

// Lambda - usually more efficient
auto lambda = [](int x) { return add(5, x); };
```

## 🎯 Common Patterns

### Pattern 1: Callback Registration
```cpp
class CallbackManager {
    std::vector<std::function<void()>> callbacks;
public:
    void registerCallback(std::function<void()> callback) {
        callbacks.push_back(callback);
    }
    
    void executeAll() {
        for (const auto& callback : callbacks) {
            callback();
        }
    }
};
```

### Pattern 2: Strategy Pattern
```cpp
class Context {
    std::function<int(int)> strategy;
public:
    void setStrategy(std::function<int(int)> s) { strategy = s; }
    int execute(int value) { return strategy(value); }
};
```

### Pattern 3: Command Pattern
```cpp
using Command = std::function<void()>;

std::vector<Command> commands;
commands.push_back([]() { /* do something */ });
commands.push_back([]() { /* do something else */ });

for (const auto& cmd : commands) {
    cmd();
}
```

## 🐛 Common Pitfalls & Solutions

### 1. std::function Type Mismatch
```cpp
// Problem - wrong signature
std::function<int()> func = [](int x) { return x; }; // Error!

// Solution - match signatures
std::function<int(int)> func = [](int x) { return x; }; // Correct
```

### 2. std::bind Placeholder Confusion
```cpp
// Problem - wrong placeholder order
auto func = std::bind(subtract, std::placeholders::_2, std::placeholders::_1);
func(3, 10); // Results in 10 - 3, not 3 - 10

// Solution - understand placeholder order
auto func = std::bind(subtract, std::placeholders::_1, std::placeholders::_2);
func(3, 10); // Results in 3 - 10
```

### 3. std::function Copy Cost
```cpp
// Problem - expensive copying
std::function<void()> heavy_func = [large_capture]() { /* ... */ };
std::vector<std::function<void()>> funcs;
funcs.push_back(heavy_func); // Copies capture

// Solution - use references or move
funcs.push_back(std::move(heavy_func)); // Move instead of copy
```

## 📚 Related Headers

- `algorithm.md` - Algorithms using function objects
- `memory.md` - Smart pointers for function management
- `iterator.md` - Iterator utilities
- `type_traits.md` - Type traits for template metaprogramming

## 🚀 Best Practices

1. **Prefer lambdas** over std::bind for new code
2. **Use std::function** only when type erasure is needed
3. **Consider auto** for lambda deduced types
4. **Use std::ref/std::cref** to avoid copies
5. **Be aware of std::function overhead** in performance-critical code
6. **Use std::not_fn** instead of deprecated negators
7. **Prefer standard function objects** over custom ones when possible

## 🎯 When to Use functional Utilities

✅ **Use when:**
- Implementing callback mechanisms
- Creating strategy patterns
- Working with STL algorithms
- Need type erasure for callables
- Implementing event systems
- Creating command patterns

❌ **Avoid when:**
- Simple function pointers suffice
- Performance-critical inner loops
- No need for type erasure
- Template functions can solve the problem
- Compile-time polymorphism is sufficient

---

**Examples in this file**: 4 complete programs  
**Key Components**: `std::function`, `std::bind`, standard function objects, `std::not_fn`  
**Performance**: Type erasure overhead vs direct calls  
**Flexibility**: Runtime polymorphism for callable objects
