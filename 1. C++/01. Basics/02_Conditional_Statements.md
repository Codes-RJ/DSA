# C++ Conditional Statements

## Overview

Conditional statements allow programs to make decisions and execute different code paths based on specific conditions. C++ provides several conditional constructs that enable branching logic, which is fundamental to algorithm implementation and problem-solving.

## if Statement

### Basic if Statement
```cpp
#include <iostream>

void basicIfStatement() {
    int age = 18;
    
    // Simple if statement
    if (age >= 18) {
        std::cout << "You are eligible to vote\n";
    }
    
    // if with compound condition
    int score = 85;
    if (score >= 90) {
        std::cout << "Grade: A\n";
    } else if (score >= 80) {
        std::cout << "Grade: B\n";
    } else if (score >= 70) {
        std::cout << "Grade: C\n";
    } else {
        std::cout << "Grade: F\n";
    }
    
    // Nested if statements
    int temperature = 25;
    bool isRaining = false;
    
    if (temperature > 20) {
        std::cout << "Warm weather\n";
        if (isRaining) {
            std::cout << "But it's raining\n";
        } else {
            std::cout << "Perfect weather for a walk\n";
        }
    }
}
```

### Complex Conditions
```cpp
#include <iostream>
#include <string>

void complexConditions() {
    int age = 25;
    bool hasLicense = true;
    bool hasCar = false;
    std::string country = "USA";
    
    // Multiple conditions with AND (&&)
    if (age >= 18 && hasLicense && hasCar) {
        std::cout << "You can drive\n";
    } else {
        std::cout << "You cannot drive\n";
    }
    
    // Multiple conditions with OR (||)
    if (age >= 18 || (country == "USA" && age >= 16)) {
        std::cout << "You can get a license\n";
    }
    
    // Combining AND and OR (use parentheses for clarity)
    if ((age >= 18 && hasLicense) || (age >= 16 && country == "USA")) {
        std::cout << "Driving eligible\n";
    }
    
    // NOT operator (!)
    if (!hasCar) {
        std::cout << "You don't have a car\n";
    }
    
    // Complex boolean logic
    bool canDrive = (age >= 18 && hasLicense) || 
                    (age >= 16 && hasLicense && country == "USA");
    
    if (canDrive && hasCar) {
        std::cout << "You can drive your car\n";
    } else if (canDrive && !hasCar) {
        std::cout << "You can drive but need a car\n";
    } else {
        std::cout << "You cannot drive\n";
    }
}
```

### Ternary Operator
```cpp
#include <iostream>
#include <string>

void ternaryOperator() {
    int age = 20;
    std::string status;
    
    // Basic ternary operator
    status = (age >= 18) ? "Adult" : "Minor";
    std::cout << "Status: " << status << "\n";
    
    // Nested ternary (avoid for readability)
    int score = 75;
    std::string grade = (score >= 90) ? "A" : 
                       (score >= 80) ? "B" : 
                       (score >= 70) ? "C" : "F";
    std::cout << "Grade: " << grade << "\n";
    
    // Ternary in expressions
    int max = (age > score) ? age : score;
    std::cout << "Maximum: " << max << "\n";
    
    // Function calls with ternary
    auto printMessage = [](const std::string& msg) {
        std::cout << msg << "\n";
    };
    
    (age >= 18) ? printMessage("Welcome, adult!") : printMessage("Hello, minor!");
    
    // Note: For complex conditions, prefer if-else for readability
}
```

## switch Statement

### Basic switch Statement
```cpp
#include <iostream>

void basicSwitchStatement() {
    int day = 3;
    
    switch (day) {
        case 1:
            std::cout << "Monday\n";
            break;
        case 2:
            std::cout << "Tuesday\n";
            break;
        case 3:
            std::cout << "Wednesday\n";
            break;
        case 4:
            std::cout << "Thursday\n";
            break;
        case 5:
            std::cout << "Friday\n";
            break;
        case 6:
            std::cout << "Saturday\n";
            break;
        case 7:
            std::cout << "Sunday\n";
            break;
        default:
            std::cout << "Invalid day\n";
            break;
    }
    
    // Switch without breaks (fall-through)
    int grade = 'B';
    std::cout << "Grade interpretation: ";
    switch (grade) {
        case 'A':
            std::cout << "Excellent";
            break;
        case 'B':
            std::cout << "Good";
            break;
        case 'C':
        case 'D':
            std::cout << "Average";
            break;
        case 'F':
            std::cout << "Poor";
            break;
        default:
            std::cout << "Invalid grade";
    }
    std::cout << "\n";
}
```

### Advanced switch Features
```cpp
#include <iostream>
#include <string>

void advancedSwitch() {
    // Switch with string (C++ doesn't support directly, use if-else)
    std::string color = "red";
    
    if (color == "red") {
        std::cout << "Stop\n";
    } else if (color == "yellow") {
        std::cout << "Caution\n";
    } else if (color == "green") {
        std::cout << "Go\n";
    } else {
        std::cout << "Invalid signal\n";
    }
    
    // Switch with enum (recommended)
    enum class Color { RED, YELLOW, GREEN, UNKNOWN };
    
    Color signal = Color::GREEN;
    switch (signal) {
        case Color::RED:
            std::cout << "Stop\n";
            break;
        case Color::YELLOW:
            std::cout << "Caution\n";
            break;
        case Color::GREEN:
            std::cout << "Go\n";
            break;
        default:
            std::cout << "Unknown signal\n";
            break;
    }
    
    // Switch with initialization (C++17)
    switch (int value = 42; value % 10) {
        case 0:
            std::cout << "Ends with 0\n";
            break;
        case 2:
            std::cout << "Ends with 2\n";
            break;
        default:
            std::cout << "Ends with other digit\n";
            break;
    }
}
```

## Modern C++ Conditional Features

### if with Initializer (C++17)
```cpp
#include <iostream>
#include <map>
#include <string>

void ifWithInitializer() {
    // Traditional approach
    std::map<std::string, int> scores = {{"Alice", 95}, {"Bob", 87}};
    auto it = scores.find("Alice");
    if (it != scores.end()) {
        std::cout << it->first << ": " << it->second << "\n";
    }
    
    // C++17 approach with initializer
    if (auto it2 = scores.find("Bob"); it2 != scores.end()) {
        std::cout << it2->first << ": " << it2->second << "\n";
    }
    
    // With else
    if (auto it3 = scores.find("Charlie"); it3 != scores.end()) {
        std::cout << it3->first << ": " << it3->second << "\n";
    } else {
        std::cout << "Charlie not found\n";
    }
    
    // Complex initialization
    if (int x = 10, y = 20; x + y > 25) {
        std::cout << "Sum is greater than 25\n";
    }
    
    // With switch
    switch (int choice = 2; choice) {
        case 1:
            std::cout << "Option 1\n";
            break;
        case 2:
            std::cout << "Option 2\n";
            break;
        default:
            std::cout << "Invalid option\n";
            break;
    }
}
```

### constexpr if (C++17)
```cpp
#include <iostream>
#include <type_traits>

template<typename T>
void printTypeInfo(const T& value) {
    if constexpr (std::is_integral_v<T>) {
        std::cout << "Integral type: " << value << "\n";
    } else if constexpr (std::is_floating_point_v<T>) {
        std::cout << "Floating point type: " << value << "\n";
    } else if constexpr (std::is_same_v<T, std::string>) {
        std::cout << "String type: " << value << "\n";
    } else {
        std::cout << "Other type\n";
    }
}

void constexprIfExample() {
    printTypeInfo(42);
    printTypeInfo(3.14);
    printTypeInfo(std::string("Hello"));
    
    // Compile-time branching
    if constexpr (sizeof(int) == 4) {
        std::cout << "int is 4 bytes\n";
    } else {
        std::cout << "int is not 4 bytes\n";
    }
}
```

## Conditional Expressions with Data Structures

### Vector Operations
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

void vectorConditionals() {
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // Conditional operations
    std::vector<int> evens, odds;
    
    for (int num : numbers) {
        if (num % 2 == 0) {
            evens.push_back(num);
        } else {
            odds.push_back(num);
        }
    }
    
    std::cout << "Even numbers: ";
    for (int num : evens) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    std::cout << "Odd numbers: ";
    for (int num : odds) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Using algorithms with conditions
    std::vector<int> filtered;
    std::copy_if(numbers.begin(), numbers.end(), std::back_inserter(filtered),
                [](int n) { return n > 5; });
    
    std::cout << "Numbers > 5: ";
    for (int num : filtered) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Conditional sorting
    bool ascending = false;
    if (ascending) {
        std::sort(numbers.begin(), numbers.end());
    } else {
        std::sort(numbers.begin(), numbers.end(), std::greater<int>());
    }
    
    std::cout << "Sorted " << (ascending ? "ascending" : "descending") << ": ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}
```

### Map Operations
```cpp
#include <iostream>
#include <map>
#include <string>

void mapConditionals() {
    std::map<std::string, int> scores = {
        {"Alice", 95},
        {"Bob", 87},
        {"Charlie", 92},
        {"David", 78},
        {"Eve", 88}
    };
    
    // Conditional processing
    std::map<std::string, std::string> grades;
    
    for (const auto& [name, score] : scores) {
        if (score >= 90) {
            grades[name] = "A";
        } else if (score >= 80) {
            grades[name] = "B";
        } else if (score >= 70) {
            grades[name] = "C";
        } else {
            grades[name] = "F";
        }
    }
    
    std::cout << "Grades:\n";
    for (const auto& [name, grade] : grades) {
        std::cout << name << ": " << grade << "\n";
    }
    
    // Conditional search
    std::string search_name = "Bob";
    auto it = scores.find(search_name);
    
    if (it != scores.end()) {
        int score = it->second;
        std::string comment = (score >= 90) ? "Excellent!" :
                             (score >= 80) ? "Good job!" :
                             (score >= 70) ? "Keep trying!" : "Needs improvement!";
        
        std::cout << search_name << " scored " << score << ". " << comment << "\n";
    } else {
        std::cout << search_name << " not found\n";
    }
}
```

### Set Operations
```cpp
#include <iostream>
#include <set>
#include <vector>

void setConditionals() {
    std::set<int> numbers = {1, 3, 5, 7, 9, 11, 13, 15};
    
    // Conditional processing
    std::vector<int> primes, composites;
    
    for (int num : numbers) {
        if (num == 2 || num == 3 || num == 5 || num == 7 || num == 11 || num == 13) {
            primes.push_back(num);
        } else {
            composites.push_back(num);
        }
    }
    
    std::cout << "Primes: ";
    for (int num : primes) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    std::cout << "Composites: ";
    for (int num : composites) {
        std::cout << num << " ";
    }
    std::cout << "\n";
    
    // Conditional insertion
    std::set<int> filtered_numbers;
    for (int num : numbers) {
        if (num % 3 == 0 || num % 5 == 0) {
            filtered_numbers.insert(num);
        }
    }
    
    std::cout << "Divisible by 3 or 5: ";
    for (int num : filtered_numbers) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}
```

## Advanced Conditional Patterns

### Strategy Pattern with Conditionals
```cpp
#include <iostream>
#include <functional>
#include <map>
#include <string>

class Calculator {
private:
    std::map<std::string, std::function<int(int, int)>> operations;
    
public:
    Calculator() {
        operations["+"] = [](int a, int b) { return a + b; };
        operations["-"] = [](int a, int b) { return a - b; };
        operations["*"] = [](int a, int b) { return a * b; };
        operations["/"] = [](int a, int b) { 
            return b != 0 ? a / b : 0; 
        };
    }
    
    int calculate(const std::string& op, int a, int b) {
        auto it = operations.find(op);
        if (it != operations.end()) {
            return it->second(a, b);
        }
        return 0; // Default case
    }
};

void strategyPattern() {
    Calculator calc;
    std::string operation = "+";
    int x = 10, y = 5;
    
    int result = calc.calculate(operation, x, y);
    std::cout << x << " " << operation << " " << y << " = " << result << "\n";
    
    // Alternative approach with function pointers
    using Operation = int(*)(int, int);
    
    std::map<std::string, Operation> ops = {
        {"add", [](int a, int b) { return a + b; }},
        {"sub", [](int a, int b) { return a - b; }},
        {"mul", [](int a, int b) { return a * b; }}
    };
    
    std::string op_name = "add";
    if (ops.count(op_name)) {
        result = ops[op_name](x, y);
        std::cout << "Result: " << result << "\n";
    }
}
```

### State Machine with Conditionals
```cpp
#include <iostream>
#include <string>

enum class State { IDLE, STARTED, RUNNING, PAUSED, STOPPED };

class TrafficLight {
private:
    State current_state = State::IDLE;
    
public:
    void transition(const std::string& event) {
        switch (current_state) {
            case State::IDLE:
                if (event == "start") {
                    current_state = State::STARTED;
                    std::cout << "Light started\n";
                }
                break;
                
            case State::STARTED:
                if (event == "run") {
                    current_state = State::RUNNING;
                    std::cout << "Light running (green)\n";
                } else if (event == "stop") {
                    current_state = State::STOPPED;
                    std::cout << "Light stopped\n";
                }
                break;
                
            case State::RUNNING:
                if (event == "pause") {
                    current_state = State::PAUSED;
                    std::cout << "Light paused (yellow)\n";
                } else if (event == "stop") {
                    current_state = State::STOPPED;
                    std::cout << "Light stopped\n";
                }
                break;
                
            case State::PAUSED:
                if (event == "resume") {
                    current_state = State::RUNNING;
                    std::cout << "Light resumed (green)\n";
                } else if (event == "stop") {
                    current_state = State::STOPPED;
                    std::cout << "Light stopped\n";
                }
                break;
                
            case State::STOPPED:
                if (event == "start") {
                    current_state = State::STARTED;
                    std::cout << "Light restarted\n";
                }
                break;
        }
    }
    
    std::string getStateString() const {
        switch (current_state) {
            case State::IDLE: return "IDLE";
            case State::STARTED: return "STARTED";
            case State::RUNNING: return "RUNNING";
            case State::PAUSED: return "PAUSED";
            case State::STOPPED: return "STOPPED";
            default: return "UNKNOWN";
        }
    }
};

void stateMachineExample() {
    TrafficLight light;
    
    light.transition("start");
    light.transition("run");
    light.transition("pause");
    light.transition("resume");
    light.transition("stop");
    
    std::cout << "Final state: " << light.getStateString() << "\n";
}
```

## Performance Considerations

### Branch Prediction
```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <algorithm>

void branchPrediction() {
    // Sorted data (predictable branches)
    std::vector<int> sorted_data(100000);
    for (size_t i = 0; i < sorted_data.size(); i++) {
        sorted_data[i] = i;
    }
    
    // Random data (unpredictable branches)
    std::vector<int> random_data = sorted_data;
    std::random_shuffle(random_data.begin(), random_data.end());
    
    auto conditionalSum = [](const std::vector<int>& data) {
        long long sum = 0;
        for (int num : data) {
            if (num < 50000) {  // Branch condition
                sum += num;
            }
        }
        return sum;
    };
    
    auto branchlessSum = [](const std::vector<int>& data) {
        long long sum = 0;
        for (int num : data) {
            sum += (num < 50000) * num;  // Branchless using multiplication
        }
        return sum;
    };
    
    // Test with sorted data
    auto start = std::chrono::high_resolution_clock::now();
    long long result1 = conditionalSum(sorted_data);
    auto end = std::chrono::high_resolution_clock::now();
    auto duration1 = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    // Test with random data
    start = std::chrono::high_resolution_clock::now();
    long long result2 = conditionalSum(random_data);
    end = std::chrono::high_resolution_clock::now();
    auto duration2 = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    // Test branchless with random data
    start = std::chrono::high_resolution_clock::now();
    long long result3 = branchlessSum(random_data);
    end = std::chrono::high_resolution_clock::now();
    auto duration3 = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    std::cout << "Conditional sum (sorted): " << duration1.count() << " μs\n";
    std::cout << "Conditional sum (random): " << duration2.count() << " μs\n";
    std::cout << "Branchless sum (random): " << duration3.count() << " μs\n";
    
    std::cout << "Results equal: " << (result2 == result3) << "\n";
}
```

### Lookup Tables vs Conditionals
```cpp
#include <iostream>
#include <array>
#include <chrono>

void lookupTableVsConditional() {
    // Conditional approach
    auto conditionalAbs = [](int x) {
        if (x >= 0) return x;
        else return -x;
    };
    
    // Lookup table approach (for small range)
    std::array<int, 21> lookup_table;
    for (int i = -10; i <= 10; i++) {
        lookup_table[i + 10] = (i >= 0) ? i : -i;
    }
    
    auto lookupAbs = [&lookup_table](int x) {
        if (x >= -10 && x <= 10) {
            return lookup_table[x + 10];
        }
        return conditionalAbs(x);  // Fallback
    };
    
    // Performance test
    std::vector<int> test_data;
    for (int i = -1000; i <= 1000; i++) {
        test_data.push_back(i);
    }
    
    auto start = std::chrono::high_resolution_clock::now();
    long long sum1 = 0;
    for (int x : test_data) {
        sum1 += conditionalAbs(x);
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto duration1 = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    start = std::chrono::high_resolution_clock::now();
    long long sum2 = 0;
    for (int x : test_data) {
        sum2 += lookupAbs(x);
    }
    end = std::chrono::high_resolution_clock::now();
    auto duration2 = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    std::cout << "Conditional: " << duration1.count() << " μs\n";
    std::cout << "Lookup table: " << duration2.count() << " μs\n";
    std::cout << "Results equal: " << (sum1 == sum2) << "\n";
}
```

## Common Conditional Patterns

### Input Validation
```cpp
#include <iostream>
#include <string>
#include <limits>

void inputValidation() {
    int age;
    std::cout << "Enter your age: ";
    
    // Validate input
    while (!(std::cin >> age)) {
        std::cout << "Invalid input. Please enter a number: ";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
    
    // Validate range
    if (age < 0) {
        std::cout << "Age cannot be negative\n";
    } else if (age > 120) {
        std::cout << "Age seems unrealistic\n";
    } else if (age < 18) {
        std::cout << "You are a minor\n";
    } else if (age < 65) {
        std::cout << "You are an adult\n";
    } else {
        std::cout << "You are a senior citizen\n";
    }
    
    // String validation
    std::string password;
    std::cout << "Enter password: ";
    std::cin >> password;
    
    bool has_upper = false, has_lower = false, has_digit = false, has_special = false;
    
    for (char c : password) {
        if (c >= 'A' && c <= 'Z') has_upper = true;
        else if (c >= 'a' && c <= 'z') has_lower = true;
        else if (c >= '0' && c <= '9') has_digit = true;
        else if (c == '!' || c == '@' || c == '#' || c == '$') has_special = true;
    }
    
    if (password.length() < 8) {
        std::cout << "Password too short\n";
    } else if (!has_upper) {
        std::cout << "Password needs uppercase letter\n";
    } else if (!has_lower) {
        std::cout << "Password needs lowercase letter\n";
    } else if (!has_digit) {
        std::cout << "Password needs digit\n";
    } else if (!has_special) {
        std::cout << "Password needs special character\n";
    } else {
        std::cout << "Password is strong\n";
    }
}
```

### Error Handling with Conditionals
```cpp
#include <iostream>
#include <fstream>
#include <string>

void errorHandling() {
    std::string filename = "example.txt";
    std::ifstream file(filename);
    
    // Check if file opened successfully
    if (!file.is_open()) {
        std::cout << "Error: Could not open file " << filename << "\n";
        return;
    }
    
    std::string line;
    int line_number = 0;
    
    while (std::getline(file, line)) {
        line_number++;
        
        // Validate line content
        if (line.empty()) {
            std::cout << "Warning: Empty line at line " << line_number << "\n";
            continue;
        }
        
        // Check for specific patterns
        if (line.find("error") != std::string::npos) {
            std::cout << "Found error keyword at line " << line_number << "\n";
        } else if (line.find("warning") != std::string::npos) {
            std::cout << "Found warning at line " << line_number << "\n";
        }
        
        // Process valid line
        std::cout << "Processing line " << line_number << ": " << line.substr(0, 50) << "\n";
    }
    
    // Check if read completed successfully
    if (file.bad()) {
        std::cout << "Error: I/O error while reading\n";
    } else if (!file.eof()) {
        std::cout << "Error: Format error while reading\n";
    } else {
        std::cout << "File read successfully\n";
    }
}
```

## Best Practices

1. **Use clear and simple conditions** that are easy to understand
2. **Prefer if-else** for complex conditions over nested ternary operators
3. **Use switch** when testing multiple values of the same variable
4. **Use enum classes** with switch for type safety
5. **Use modern C++ features** like if with initializers (C++17)
6. **Consider branch prediction** in performance-critical code
7. **Validate inputs** before processing
8. **Handle edge cases** explicitly
9. **Use meaningful variable names** in conditions
10. **Keep conditionals short** and move complex logic to functions

## Conclusion

Conditional statements are fundamental to programming logic and decision-making in C++. Understanding the various conditional constructs, their performance implications, and best practices enables writing clear, efficient, and maintainable code. Modern C++ continues to enhance conditional programming with features like if-initializers and constexpr if, providing more expressive and type-safe ways to implement branching logic.

---

## Next Step

- Go to [03_Loops_and_Iteration.md](03_Loops_and_Iteration.md) to continue with Loops and Iteration.
