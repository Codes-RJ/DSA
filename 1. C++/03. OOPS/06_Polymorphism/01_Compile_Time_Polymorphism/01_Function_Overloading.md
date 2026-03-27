# 06_Polymorphism/01_Compile_Time_Polymorphism/01_Function_Overloading.md

# Function Overloading in C++ - Complete Guide

## 📖 Overview

Function overloading is a form of compile-time polymorphism that allows multiple functions with the same name but different parameters. The compiler determines which function to call based on the number, types, and order of arguments. This enables intuitive and consistent interfaces for operations that work with different data types.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Function Overloading** | Multiple functions with same name, different parameters |
| **Signature** | Function name + parameter list (types, order, count) |
| **Return Type** | Not part of signature (cannot overload on return type alone) |
| **Resolution** | Compiler selects best match at compile time |

---

## 1. **Basic Function Overloading**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Multiple print functions with same name
void print(int value) {
    cout << "Integer: " << value << endl;
}

void print(double value) {
    cout << "Double: " << value << endl;
}

void print(const string& value) {
    cout << "String: " << value << endl;
}

void print(bool value) {
    cout << "Boolean: " << (value ? "true" : "false") << endl;
}

class Calculator {
public:
    // Overloaded add functions
    int add(int a, int b) {
        cout << "int add(int, int): ";
        return a + b;
    }
    
    double add(double a, double b) {
        cout << "double add(double, double): ";
        return a + b;
    }
    
    int add(int a, int b, int c) {
        cout << "int add(int, int, int): ";
        return a + b + c;
    }
    
    string add(const string& a, const string& b) {
        cout << "string add(string, string): ";
        return a + b;
    }
};

int main() {
    cout << "=== Basic Function Overloading ===" << endl;
    
    cout << "\n1. Overloaded print functions:" << endl;
    print(42);
    print(3.14159);
    print("Hello World");
    print(true);
    
    cout << "\n2. Overloaded Calculator methods:" << endl;
    Calculator calc;
    cout << calc.add(5, 3) << endl;
    cout << calc.add(5.5, 3.2) << endl;
    cout << calc.add(1, 2, 3) << endl;
    cout << calc.add("Hello", " World") << endl;
    
    return 0;
}
```

**Output:**
```
=== Basic Function Overloading ===

1. Overloaded print functions:
Integer: 42
Double: 3.14159
String: Hello World
Boolean: true

2. Overloaded Calculator methods:
int add(int, int): 8
double add(double, double): 8.7
int add(int, int, int): 6
string add(string, string): Hello World
```

---

## 2. **Overloading with Different Parameter Types**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

class AreaCalculator {
public:
    // Overloaded area functions for different shapes
    double area(double radius) {  // Circle
        cout << "Circle: ";
        return M_PI * radius * radius;
    }
    
    double area(double length, double width) {  // Rectangle
        cout << "Rectangle: ";
        return length * width;
    }
    
    double area(double base, double height, bool isTriangle) {  // Triangle
        cout << "Triangle: ";
        return 0.5 * base * height;
    }
    
    double area(int side) {  // Square (int parameter)
        cout << "Square: ";
        return side * side;
    }
    
    // Overloading with different parameter order
    void display(int x, int y) {
        cout << "Point: (" << x << ", " << y << ")" << endl;
    }
    
    void display(int x, int y, int z) {
        cout << "3D Point: (" << x << ", " << y << ", " << z << ")" << endl;
    }
    
    void display(double x, double y) {
        cout << "Floating Point: (" << x << ", " << y << ")" << endl;
    }
};

int main() {
    cout << "=== Overloading with Different Parameter Types ===" << endl;
    
    AreaCalculator area;
    
    cout << "\n1. Different shape calculations:" << endl;
    cout << area.area(5.0) << endl;                    // Circle
    cout << area.area(4.0, 6.0) << endl;              // Rectangle
    cout << area.area(3.0, 4.0, true) << endl;        // Triangle
    cout << area.area(5) << endl;                     // Square (int)
    
    cout << "\n2. Different parameter counts:" << endl;
    area.display(10, 20);
    area.display(10, 20, 30);
    
    cout << "\n3. Different parameter types:" << endl;
    area.display(5.5, 3.2);
    
    return 0;
}
```

---

## 3. **Overloading with References and Pointers**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Processor {
public:
    // Overload by value
    void process(int value) {
        cout << "process(int): " << value << endl;
    }
    
    // Overload by reference
    void process(int& value) {
        cout << "process(int&): " << value << endl;
        value *= 2;
    }
    
    // Overload by const reference
    void process(const int& value) {
        cout << "process(const int&): " << value << endl;
        // value = 10;  // Error! Cannot modify const
    }
    
    // Overload by pointer
    void process(int* value) {
        cout << "process(int*): " << *value << endl;
        *value *= 2;
    }
    
    // Overload by const pointer
    void process(const int* value) {
        cout << "process(const int*): " << *value << endl;
        // *value = 10;  // Error! Cannot modify const
    }
    
    // Overload by array
    void process(int arr[], int size) {
        cout << "process(int[], int): ";
        for (int i = 0; i < size; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    cout << "=== Overloading with References and Pointers ===" << endl;
    
    Processor proc;
    
    int value = 10;
    const int constValue = 20;
    
    cout << "\n1. By value:" << endl;
    proc.process(5);
    
    cout << "\n2. By reference:" << endl;
    cout << "Before: " << value << endl;
    proc.process(value);
    cout << "After: " << value << endl;
    
    cout << "\n3. By const reference:" << endl;
    proc.process(constValue);
    
    cout << "\n4. By pointer:" << endl;
    value = 30;
    cout << "Before: " << value << endl;
    proc.process(&value);
    cout << "After: " << value << endl;
    
    cout << "\n5. By const pointer:" << endl;
    proc.process(&constValue);
    
    cout << "\n6. By array:" << endl;
    int arr[] = {1, 2, 3, 4, 5};
    proc.process(arr, 5);
    
    return 0;
}
```

---

## 4. **Overloading with Default Arguments**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Logger {
public:
    // Overloaded with default arguments
    void log(const string& message) {
        cout << "[INFO] " << message << endl;
    }
    
    void log(const string& message, int level) {
        string prefix;
        switch(level) {
            case 0: prefix = "DEBUG"; break;
            case 1: prefix = "INFO"; break;
            case 2: prefix = "WARN"; break;
            case 3: prefix = "ERROR"; break;
            default: prefix = "UNKNOWN";
        }
        cout << "[" << prefix << "] " << message << endl;
    }
    
    void log(const string& message, int level, const string& module) {
        string prefix;
        switch(level) {
            case 0: prefix = "DEBUG"; break;
            case 1: prefix = "INFO"; break;
            case 2: prefix = "WARN"; break;
            case 3: prefix = "ERROR"; break;
            default: prefix = "UNKNOWN";
        }
        cout << "[" << prefix << "][" << module << "] " << message << endl;
    }
    
    // NOT allowed: cannot overload only by default arguments
    // void log(const string& message, int level = 1) { }
    // void log(const string& message) { }  // Ambiguous with default argument version
};

class Connection {
public:
    void connect(const string& host) {
        cout << "Connecting to " << host << " (default port)" << endl;
    }
    
    void connect(const string& host, int port) {
        cout << "Connecting to " << host << ":" << port << endl;
    }
    
    void connect(const string& host, int port, const string& user) {
        cout << "Connecting to " << host << ":" << port << " as " << user << endl;
    }
};

int main() {
    cout << "=== Overloading with Default Arguments ===" << endl;
    
    cout << "\n1. Logger with different parameter counts:" << endl;
    Logger logger;
    logger.log("Application started");
    logger.log("Database connection failed", 3);
    logger.log("User logged in", 1, "Auth");
    
    cout << "\n2. Connection with different parameters:" << endl;
    Connection conn;
    conn.connect("localhost");
    conn.connect("localhost", 3306);
    conn.connect("localhost", 3306, "admin");
    
    cout << "\n3. Note on overloading with default arguments:" << endl;
    cout << "   Cannot overload functions that would be ambiguous with default arguments." << endl;
    
    return 0;
}
```

---

## 5. **Overloading and Type Conversion**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Converter {
public:
    void convert(int value) {
        cout << "convert(int): " << value << endl;
    }
    
    void convert(double value) {
        cout << "convert(double): " << value << endl;
    }
    
    void convert(long value) {
        cout << "convert(long): " << value << endl;
    }
    
    void convert(float value) {
        cout << "convert(float): " << value << endl;
    }
    
    void convert(char value) {
        cout << "convert(char): '" << value << "'" << endl;
    }
    
    void convert(bool value) {
        cout << "convert(bool): " << (value ? "true" : "false") << endl;
    }
};

class AmbiguityDemo {
public:
    void display(int a, int b) {
        cout << "display(int, int): " << a << ", " << b << endl;
    }
    
    void display(double a, double b) {
        cout << "display(double, double): " << a << ", " << b << endl;
    }
    
    // Ambiguous overloads
    // void display(int a, double b) { }
    // void display(double a, int b) { }  // Would cause ambiguity with (int,int) and (double,double)
};

int main() {
    cout << "=== Overloading and Type Conversion ===" << endl;
    
    Converter conv;
    
    cout << "\n1. Exact matches:" << endl;
    conv.convert(42);           // int
    conv.convert(3.14);         // double
    conv.convert(100L);         // long
    conv.convert(3.14f);        // float
    conv.convert('A');          // char
    conv.convert(true);         // bool
    
    cout << "\n2. Type promotion and conversion:" << endl;
    conv.convert(10);           // int (exact match)
    conv.convert(10L);          // long (exact match)
    conv.convert(10.5f);        // float (exact match)
    
    cout << "\n3. Ambiguity examples:" << endl;
    AmbiguityDemo amb;
    amb.display(10, 20);        // int, int
    amb.display(10.5, 20.5);    // double, double
    // amb.display(10, 20.5);   // Ambiguous! Could be (int,int) with conversion or (double,double)
    // amb.display(10.5, 20);   // Ambiguous! Same issue
    
    cout << "\n4. Overload resolution rules:" << endl;
    cout << "   1. Exact match" << endl;
    cout << "   2. Promotion (char → int, float → double)" << endl;
    cout << "   3. Standard conversion (int → double)" << endl;
    cout << "   4. User-defined conversion" << endl;
    cout << "   5. Ambiguous if multiple equally good matches" << endl;
    
    return 0;
}
```

---

## 6. **Practical Example: String Formatter**

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
using namespace std;

class Formatter {
public:
    // Format integer
    string format(int value) {
        return to_string(value);
    }
    
    // Format double with precision
    string format(double value, int precision = 2) {
        stringstream ss;
        ss << fixed << setprecision(precision) << value;
        return ss.str();
    }
    
    // Format boolean
    string format(bool value) {
        return value ? "true" : "false";
    }
    
    // Format string (wrap in quotes)
    string format(const string& value) {
        return "\"" + value + "\"";
    }
    
    // Format date (day, month, year)
    string format(int day, int month, int year) {
        stringstream ss;
        ss << setfill('0') << setw(2) << day << "/"
           << setw(2) << month << "/"
           << year;
        return ss.str();
    }
    
    // Format time (hour, minute, second)
    string format(int hour, int minute, int second) {
        stringstream ss;
        ss << setfill('0') << setw(2) << hour << ":"
           << setw(2) << minute << ":"
           << setw(2) << second;
        return ss.str();
    }
    
    // Format with custom prefix/suffix
    string format(const string& value, const string& prefix, const string& suffix) {
        return prefix + value + suffix;
    }
};

class DataProcessor {
public:
    // Process different data types
    void process(int data) {
        cout << "Processing integer: " << data << endl;
    }
    
    void process(double data) {
        cout << "Processing double: " << data << endl;
    }
    
    void process(const string& data) {
        cout << "Processing string: " << data << endl;
    }
    
    void process(const vector<int>& data) {
        cout << "Processing vector of " << data.size() << " integers: ";
        for (int v : data) cout << v << " ";
        cout << endl;
    }
    
    void process(const vector<double>& data) {
        cout << "Processing vector of " << data.size() << " doubles: ";
        for (double v : data) cout << v << " ";
        cout << endl;
    }
    
    void process(const vector<string>& data) {
        cout << "Processing vector of " << data.size() << " strings: ";
        for (const auto& v : data) cout << v << " ";
        cout << endl;
    }
};

int main() {
    cout << "=== Practical Example: String Formatter ===" << endl;
    
    Formatter fmt;
    
    cout << "\n1. Basic formatting:" << endl;
    cout << "Integer: " << fmt.format(42) << endl;
    cout << "Double: " << fmt.format(3.14159265) << endl;
    cout << "Double with precision 4: " << fmt.format(3.14159265, 4) << endl;
    cout << "Boolean: " << fmt.format(true) << endl;
    cout << "String: " << fmt.format("Hello World") << endl;
    
    cout << "\n2. Date and time formatting:" << endl;
    cout << "Date: " << fmt.format(15, 3, 2024) << endl;
    cout << "Time: " << fmt.format(14, 30, 45) << endl;
    
    cout << "\n3. Custom formatting:" << endl;
    cout << fmt.format("ERROR", "[", "]") << endl;
    cout << fmt.format("Success", "✓ ", "") << endl;
    
    cout << "\n4. Data processing with overloads:" << endl;
    DataProcessor processor;
    processor.process(100);
    processor.process(3.14);
    processor.process("Sample text");
    processor.process(vector<int>{1, 2, 3, 4, 5});
    processor.process(vector<double>{1.1, 2.2, 3.3});
    processor.process(vector<string>{"apple", "banana", "cherry"});
    
    return 0;
}
```

---

## 📊 Function Overloading Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Multiple functions with same name, different parameters |
| **Signature** | Function name + parameter list (types, count, order) |
| **Return Type** | Not part of signature |
| **Resolution** | Compile-time based on argument types |
| **Ambiguity** | Occurs when multiple overloads are equally good matches |

---

## ✅ Best Practices

1. **Use meaningful overloads** that perform logically similar operations
2. **Avoid ambiguous overloads** that could confuse the compiler
3. **Document overloaded functions** clearly
4. **Use consistent parameter order** across overloads
5. **Consider default arguments** as alternative to overloading
6. **Be aware of type conversions** that may cause unexpected matches

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Overloading by return type only** | Not allowed | Use different parameter types |
| **Ambiguous overloads** | Compiler error | Ensure distinct signatures |
| **Default arguments conflict** | Ambiguity | Avoid mixing defaults with overloads |
| **Type promotion confusion** | Unexpected function called | Be explicit with types |

---

## ✅ Key Takeaways

1. **Function overloading** enables multiple functions with same name
2. **Signature** includes name + parameter list (not return type)
3. **Compiler resolves** at compile time based on arguments
4. **Common uses**: Different data types, parameter counts
5. **Best for**: Logically similar operations on different types
6. **Avoid ambiguity** with careful design

---