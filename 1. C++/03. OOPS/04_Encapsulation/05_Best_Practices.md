# 04_Encapsulation/05_Best_Practices.md

# Encapsulation Best Practices

## 📖 Overview

Encapsulation is one of the most important principles of Object-Oriented Programming. Following best practices ensures that your classes are well-designed, maintainable, and secure. This guide provides comprehensive guidelines for effective encapsulation in C++.

---

## 🎯 Core Principles

| Principle | Description |
|-----------|-------------|
| **Data Hiding** | Keep data members private |
| **Interface Segregation** | Provide minimal, focused public interface |
| **Invariant Maintenance** | Ensure object state is always valid |
| **Const Correctness** | Mark methods that don't modify state as const |
| **Resource Management** | Use RAII for resource acquisition |

---

## 1. **Keep Data Members Private**

### ✅ Good: Private Data with Public Interface

```cpp
class Employee {
private:
    string name;        // Private - hidden
    double salary;      // Private - hidden
    int id;             // Private - hidden
    
public:
    // Public interface only
    Employee(string n, double s) : name(n), salary(s), id(generateId()) {}
    
    string getName() const { return name; }
    double getSalary() const { return salary; }
    
    void giveRaise(double percent) {
        if (percent > 0) {
            salary += salary * (percent / 100);
        }
    }
};
```

### ❌ Bad: Public Data Members

```cpp
class Employee {
public:
    string name;        // Public - anyone can modify
    double salary;      // Public - no validation
    int id;             // Public - no control
    
    // No encapsulation - data exposed directly
};
```

---

## 2. **Validate Input in Setters**

### ✅ Good: Validation Ensures Invariants

```cpp
class BankAccount {
private:
    double balance;
    string accountNumber;
    
public:
    void deposit(double amount) {
        if (amount > 0) {           // ✓ Validate input
            balance += amount;
        } else {
            throw invalid_argument("Deposit amount must be positive");
        }
    }
    
    bool withdraw(double amount) {
        if (amount <= 0) {          // ✓ Validate input
            return false;
        }
        if (amount <= balance) {    // ✓ Check invariants
            balance -= amount;
            return true;
        }
        return false;
    }
    
    void setAccountNumber(const string& number) {
        if (number.length() == 10 && isdigit(number[0])) {  // ✓ Validate format
            accountNumber = number;
        } else {
            throw invalid_argument("Invalid account number format");
        }
    }
};
```

### ❌ Bad: No Validation

```cpp
class BankAccount {
public:
    double balance;                 // No validation
    string accountNumber;           // No format check
    
    void deposit(double amount) {
        balance += amount;          // No validation - could be negative!
    }
};
```

---

## 3. **Return by Value or Const Reference**

### ✅ Good: Safe Return Types

```cpp
class Database {
private:
    vector<string> records;
    string name;
    
public:
    // Return by value - safe copy
    string getName() const {
        return name;
    }
    
    // Return const reference - read-only access, no copy
    const vector<string>& getRecords() const {
        return records;
    }
    
    // Return by value for primitives
    int getRecordCount() const {
        return records.size();
    }
};
```

### ❌ Bad: Exposing Internal References

```cpp
class Database {
private:
    vector<string> records;
    
public:
    // Bad: Returns non-const reference - allows modification!
    vector<string>& getRecords() {
        return records;     // Caller can modify internal data!
    }
    
    // Bad: Returns pointer to internal data
    string* getData() {
        return records.data();  // Dangerous!
    }
};
```

---

## 4. **Use Const Correctness**

### ✅ Good: Const Methods for Read-Only Operations

```cpp
class Rectangle {
private:
    double width, height;
    
public:
    // Const methods - don't modify object
    double area() const { return width * height; }
    double perimeter() const { return 2 * (width + height); }
    double getWidth() const { return width; }
    double getHeight() const { return height; }
    
    // Non-const methods - modify object
    void setWidth(double w) { width = w; }
    void setHeight(double h) { height = h; }
    void scale(double factor) {
        width *= factor;
        height *= factor;
    }
};

void processRectangle(const Rectangle& rect) {
    // Can only call const methods on const reference
    cout << "Area: " << rect.area() << endl;
    // rect.setWidth(10);  // Error! Cannot call non-const on const
}
```

---

## 5. **Follow the Rule of Zero/Three/Five**

### ✅ Good: Rule of Zero (Use RAII Types)

```cpp
class Employee {
private:
    string name;          // std::string manages memory
    vector<string> skills; // std::vector manages memory
    unique_ptr<int> bonus; // smart pointer manages memory
    
public:
    // No need to write destructor, copy, or move
    // Compiler-generated versions work correctly
    Employee(string n) : name(n) {}
    
    void addSkill(const string& s) { skills.push_back(s); }
};
```

### ✅ Good: Rule of Five (When Managing Resources)

```cpp
class StringBuffer {
private:
    char* data;
    size_t size;
    
public:
    // Constructor
    StringBuffer(const char* str) {
        size = strlen(str);
        data = new char[size + 1];
        strcpy(data, str);
    }
    
    // Destructor
    ~StringBuffer() {
        delete[] data;
    }
    
    // Copy constructor
    StringBuffer(const StringBuffer& other) {
        size = other.size;
        data = new char[size + 1];
        strcpy(data, other.data);
    }
    
    // Copy assignment
    StringBuffer& operator=(const StringBuffer& other) {
        if (this != &other) {
            delete[] data;
            size = other.size;
            data = new char[size + 1];
            strcpy(data, other.data);
        }
        return *this;
    }
    
    // Move constructor
    StringBuffer(StringBuffer&& other) noexcept
        : data(other.data), size(other.size) {
        other.data = nullptr;
        other.size = 0;
    }
    
    // Move assignment
    StringBuffer& operator=(StringBuffer&& other) noexcept {
        if (this != &other) {
            delete[] data;
            data = other.data;
            size = other.size;
            other.data = nullptr;
            other.size = 0;
        }
        return *this;
    }
};
```

---

## 6. **Provide Minimal Interface**

### ✅ Good: Focused, Cohesive Interface

```cpp
class Temperature {
private:
    double celsius;
    
public:
    // Minimal, focused interface
    void setCelsius(double c) {
        if (c >= -273.15) celsius = c;
    }
    
    void setFahrenheit(double f) {
        setCelsius((f - 32) * 5.0 / 9.0);
    }
    
    double getCelsius() const { return celsius; }
    double getFahrenheit() const { return celsius * 9.0 / 5.0 + 32; }
};
```

### ❌ Bad: Exposing Internal Details

```cpp
class Temperature {
public:
    double celsius;      // Exposed - can set invalid values
    double fahrenheit;   // Redundant - derived from celsius
    
    // Too many ways to do the same thing
    void setC(double c) { celsius = c; }
    void setF(double f) { celsius = (f - 32) * 5.0 / 9.0; }
    void update(double c) { celsius = c; }
    void modify(double f) { celsius = (f - 32) * 5.0 / 9.0; }
};
```

---

## 7. **Use Private Helper Functions**

### ✅ Good: Hide Complex Implementation

```cpp
class Date {
private:
    int day, month, year;
    
    // Private helpers - hidden from users
    bool isLeapYear() const {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }
    
    int daysInMonth() const {
        switch (month) {
            case 2: return isLeapYear() ? 29 : 28;
            case 4: case 6: case 9: case 11: return 30;
            default: return 31;
        }
    }
    
    void normalize() {
        while (day > daysInMonth()) {
            day -= daysInMonth();
            month++;
            if (month > 12) {
                month = 1;
                year++;
            }
        }
    }
    
public:
    Date(int d, int m, int y) : day(d), month(m), year(y) {
        normalize();  // Call private helper
    }
    
    void addDays(int days) {
        day += days;
        normalize();  // Reuse helper
    }
};
```

---

## 8. **Prefer Composition over Inheritance for Code Reuse**

### ✅ Good: Composition

```cpp
class Engine {
public:
    void start() { cout << "Engine started" << endl; }
    void stop() { cout << "Engine stopped" << endl; }
};

class Wheels {
public:
    void rotate() { cout << "Wheels rotating" << endl; }
};

class Car {
private:
    Engine engine;      // Composition
    Wheels wheels[4];   // Composition
    
public:
    void start() {
        engine.start();
        for (auto& w : wheels) w.rotate();
    }
};
```

### ❌ Bad: Overusing Inheritance

```cpp
class Car : public Engine, public Wheels {  // Inheritance for code reuse
    // This creates a confusing "is-a" relationship
    // A Car is not an Engine or a Wheel
};
```

---

## 9. **Use `explicit` for Single-Parameter Constructors**

### ✅ Good: Prevent Implicit Conversions

```cpp
class String {
private:
    char* data;
    
public:
    // explicit prevents implicit conversion
    explicit String(const char* str) {
        data = new char[strlen(str) + 1];
        strcpy(data, str);
    }
};

void printString(const String& s) {
    // Function implementation
}

int main() {
    String s1("Hello");     // OK - explicit
    // String s2 = "World"; // Error! Implicit conversion prevented
    // printString("Hello"); // Error! Implicit conversion prevented
    printString(String("Hello")); // OK - explicit conversion
}
```

---

## 10. **Use `mutable` for Caching and Logging**

### ✅ Good: Mutable for Internal State

```cpp
class ExpensiveCalculator {
private:
    int value;
    mutable int cacheCount;      // Can be modified in const methods
    mutable double cachedResult; // Can be modified in const methods
    mutable bool cacheValid;     // Can be modified in const methods
    
    double expensiveCalculation() const {
        cacheCount++;
        return sqrt(value) * sin(value) * cos(value);
    }
    
public:
    ExpensiveCalculator(int v) : value(v), cacheCount(0), cacheValid(false) {}
    
    double getResult() const {
        if (!cacheValid) {
            cachedResult = expensiveCalculation();
            cacheValid = true;
        }
        return cachedResult;
    }
    
    int getCacheCount() const { return cacheCount; }
    
    void setValue(int v) {
        value = v;
        cacheValid = false;  // Invalidate cache
    }
};
```

---

## 11. **Design for Extension, Not Modification**

### ✅ Good: Open/Closed Principle

```cpp
// Base class - open for extension
class Shape {
public:
    virtual double area() const = 0;
    virtual ~Shape() = default;
};

// Closed for modification - add new shapes by extending, not modifying
class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r) : radius(r) {}
    double area() const override { return 3.14159 * radius * radius; }
};

class Rectangle : public Shape {
private:
    double width, height;
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    double area() const override { return width * height; }
};

// Client code doesn't need to change when new shapes are added
void printArea(const Shape& shape) {
    cout << "Area: " << shape.area() << endl;
}
```

---

## 12. **Document the Interface**

### ✅ Good: Clear Documentation

```cpp
/**
 * @class BankAccount
 * @brief Represents a bank account with deposit and withdrawal capabilities
 * 
 * This class provides a safe interface for bank account operations.
 * All transactions are validated to maintain account integrity.
 */
class BankAccount {
private:
    double balance;  ///< Current account balance (always >= 0)
    
public:
    /**
     * @brief Deposits money into the account
     * @param amount Amount to deposit (must be positive)
     * @throws std::invalid_argument if amount <= 0
     */
    void deposit(double amount);
    
    /**
     * @brief Withdraws money from the account
     * @param amount Amount to withdraw (must be positive)
     * @return true if withdrawal successful, false if insufficient funds
     */
    bool withdraw(double amount);
    
    /**
     * @brief Gets current balance
     * @return Current account balance
     */
    double getBalance() const;
};
```

---

## 📊 Best Practices Checklist

| Practice | Status |
|----------|--------|
| Data members are private | ☐ |
| Setters include validation | ☐ |
| Getters are const | ☐ |
| Return const references for large objects | ☐ |
| Follow Rule of Zero/Three/Five | ☐ |
| Provide minimal interface | ☐ |
| Use private helper functions | ☐ |
| Prefer composition over inheritance | ☐ |
| Use explicit for single-arg constructors | ☐ |
| Document public interface | ☐ |
| Mark methods that don't modify as const | ☐ |
| Use RAII for resource management | ☐ |

---

## ✅ Key Takeaways

1. **Keep data private** - Expose only through controlled interface
2. **Validate input** - Maintain invariants in setters
3. **Return safely** - Prefer values or const references
4. **Const correctness** - Mark read-only methods as const
5. **Follow resource rules** - Rule of Zero/Three/Five
6. **Minimal interface** - Expose only what's necessary
7. **Hide complexity** - Use private helpers
8. **Prefer composition** - Over inheritance for code reuse
9. **Prevent implicit conversions** - Use explicit keyword
10. **Document clearly** - Explain interface and usage

---