# 04_Encapsulation/Theory.md

# Encapsulation in C++ - Complete Guide

## 📖 Overview

Encapsulation is one of the four fundamental principles of Object-Oriented Programming (along with inheritance, polymorphism, and abstraction). It is the mechanism of bundling data (attributes) and methods (functions) that operate on that data within a single unit (class), while restricting direct access to some of an object's components. Encapsulation protects data integrity and hides implementation details from the outside world.

---

## 🎯 Core Concepts

| Concept | Description |
|---------|-------------|
| **Data Hiding** | Making data members private to prevent direct access |
| **Information Hiding** | Hiding implementation details behind a public interface |
| **Access Control** | Using access specifiers (public, private, protected) |
| **Interface** | Public methods that provide controlled access to data |

---

## 📊 Benefits of Encapsulation

| Benefit | Description |
|---------|-------------|
| **Data Protection** | Prevents unauthorized access and accidental modification |
| **Flexibility** | Implementation can change without affecting users |
| **Maintainability** | Changes are isolated to the class |
| **Reusability** | Well-encapsulated classes are easier to reuse |
| **Testability** | Clear interfaces make testing easier |
| **Security** | Sensitive data can be hidden from external access |

---

## 🔧 How Encapsulation Works in C++

### Access Specifiers

```cpp
class Encapsulated {
private:
    // Private: Accessible only within this class
    int privateData;
    void privateMethod() { }
    
protected:
    // Protected: Accessible within this class and derived classes
    int protectedData;
    void protectedMethod() { }
    
public:
    // Public: Accessible from anywhere
    int publicData;
    void publicMethod() { }
    
    // Getter and Setter for private data
    int getPrivateData() const { return privateData; }
    void setPrivateData(int value) { 
        // Validation can be added here
        if (value >= 0) {
            privateData = value;
        }
    }
};
```

---

## 🏗️ Levels of Encapsulation

### 1. **Complete Encapsulation**
All data members are private; access is only through public methods.

```cpp
class BankAccount {
private:
    double balance;           // Hidden from outside
    string accountNumber;     // Hidden from outside
    
public:
    void deposit(double amount);   // Controlled access
    bool withdraw(double amount);  // Controlled access
    double getBalance() const;     // Read-only access
};
```

### 2. **Partial Encapsulation**
Some data members are public, others are protected/private.

```cpp
class Employee {
public:
    string name;              // Public - can be accessed directly
    int id;                   // Public - can be accessed directly
    
private:
    double salary;            // Private - must use getters/setters
    string ssn;               // Private - sensitive data
    
public:
    double getSalary() const { return salary; }
    void setSalary(double s) {
        if (s >= 0) salary = s;
    }
};
```

### 3. **No Encapsulation (Struct-like)**
All members are public (typically used for simple data aggregates).

```cpp
struct Point {
    int x;      // Public
    int y;      // Public
    // No methods, just data
};
```

---

## 💡 Getters and Setters (Accessors and Mutators)

### Why Use Getters and Setters?

```cpp
class Temperature {
private:
    double value;
    string unit;  // "C" or "F"
    
public:
    // Getter - provides read-only access
    double getValue() const { return value; }
    string getUnit() const { return unit; }
    
    // Setter with validation
    void setValue(double v) {
        // Validate temperature (absolute zero check)
        if (unit == "C" && v >= -273.15) {
            value = v;
        } else if (unit == "F" && v >= -459.67) {
            value = v;
        }
    }
    
    void setUnit(string u) {
        if (u == "C" || u == "F") {
            // Convert temperature if unit changes
            if (u != unit) {
                if (u == "C") {
                    value = (value - 32) * 5.0 / 9.0;
                } else {
                    value = (value * 9.0 / 5.0) + 32;
                }
            }
            unit = u;
        }
    }
};
```

### Benefits of Getters/Setters

```cpp
class Product {
private:
    string name;
    double price;
    int quantity;
    
public:
    // Getter: Simple read access
    string getName() const { return name; }
    double getPrice() const { return price; }
    int getQuantity() const { return quantity; }
    
    // Setter with validation
    void setName(const string& n) {
        if (!n.empty()) name = n;
    }
    
    void setPrice(double p) {
        if (p >= 0) price = p;  // Validate
    }
    
    void setQuantity(int q) {
        if (q >= 0) quantity = q;  // Validate
    }
    
    // Calculated property (not a direct data member)
    double getTotalValue() const {
        return price * quantity;
    }
    
    // Business logic
    bool reduceStock(int amount) {
        if (amount <= quantity) {
            quantity -= amount;
            return true;
        }
        return false;
    }
};
```

---

## 🔒 Encapsulation in Practice

### Example: Safe Integer Class

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

class SafeInt {
private:
    int value;
    
public:
    // Constructor with validation
    SafeInt(int v = 0) : value(v) {}
    
    // Getter
    int getValue() const { return value; }
    
    // Setter with range validation
    void setValue(int v) {
        if (v >= -100 && v <= 100) {
            value = v;
        } else {
            throw out_of_range("Value must be between -100 and 100");
        }
    }
    
    // Arithmetic operations with bounds checking
    SafeInt add(const SafeInt& other) const {
        int result = value + other.value;
        if (result < -100 || result > 100) {
            throw overflow_error("Addition would exceed bounds");
        }
        return SafeInt(result);
    }
    
    SafeInt subtract(const SafeInt& other) const {
        int result = value - other.value;
        if (result < -100 || result > 100) {
            throw overflow_error("Subtraction would exceed bounds");
        }
        return SafeInt(result);
    }
    
    SafeInt multiply(const SafeInt& other) const {
        int result = value * other.value;
        if (result < -100 || result > 100) {
            throw overflow_error("Multiplication would exceed bounds");
        }
        return SafeInt(result);
    }
    
    // Display
    void display() const {
        cout << "Value: " << value << endl;
    }
};

int main() {
    cout << "=== SafeInt - Encapsulation Example ===" << endl;
    
    try {
        SafeInt a(50);
        SafeInt b(30);
        
        cout << "a: "; a.display();
        cout << "b: "; b.display();
        
        SafeInt sum = a.add(b);
        cout << "a + b: "; sum.display();
        
        SafeInt diff = a.subtract(b);
        cout << "a - b: "; diff.display();
        
        SafeInt product = a.multiply(b);
        cout << "a * b: "; product.display();
        
        // This would throw exception
        // SafeInt c(150);  // Would throw if validation added
        // SafeInt d(60);
        // SafeInt invalid = a.add(d);
        
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    return 0;
}
```

---

## 🏗️ Encapsulation in Inheritance

### How Access Specifiers Affect Derived Classes

```cpp
#include <iostream>
using namespace std;

class Base {
private:
    int privateVar = 1;      // Not accessible in derived class
    
protected:
    int protectedVar = 2;    // Accessible in derived class
    
public:
    int publicVar = 3;       // Accessible everywhere
    
    // Public interface to access private members
    int getPrivate() const { return privateVar; }
};

class Derived : public Base {
public:
    void showAccess() {
        // cout << privateVar;  // Error! Cannot access private
        cout << "Protected: " << protectedVar << endl;  // OK
        cout << "Public: " << publicVar << endl;        // OK
        cout << "Private via getter: " << getPrivate() << endl;  // OK
    }
};

int main() {
    Base b;
    Derived d;
    
    // Access from main
    // cout << b.privateVar;  // Error!
    // cout << b.protectedVar; // Error!
    cout << "Base public: " << b.publicVar << endl;      // OK
    
    d.showAccess();
    
    return 0;
}
```

---

## 📊 Encapsulation Best Practices

### 1. **Keep Data Private**
```cpp
class Good {
private:
    int data;  // ✓ Private data
    
public:
    int getData() const { return data; }  // Public getter
    void setData(int d) { data = d; }     // Public setter
};
```

### 2. **Use Const for Read-Only Access**
```cpp
class Data {
private:
    int value;
    
public:
    int getValue() const { return value; }  // ✓ Const - won't modify
    void setValue(int v) { value = v; }     // Non-const - modifies
};
```

### 3. **Validate Input in Setters**
```cpp
void setAge(int a) {
    if (a >= 0 && a <= 150) {  // ✓ Validation
        age = a;
    } else {
        throw invalid_argument("Invalid age");
    }
}
```

### 4. **Provide Meaningful Interface**
```cpp
class Account {
private:
    double balance;
    
public:
    // ✓ Good: Business-logic methods
    void deposit(double amount);
    bool withdraw(double amount);
    double getBalance() const;
    
    // ✗ Avoid: Exposing implementation
    // void setBalance(double b);  // Would break invariants
};
```

---

## 🐛 Common Encapsulation Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| **Public data members** | No control over modifications | Make data private, add getters/setters |
| **Getter returns reference** | Allows bypassing setter | Return by value or const reference |
| **Setter without validation** | Invalid data can be stored | Add validation in setters |
| **Exposing internal collections** | Outside code can modify | Return const reference or copy |
| **God class** | Too many responsibilities | Split into smaller classes |

---

## ✅ Key Takeaways

1. **Encapsulation** bundles data and methods, hiding implementation
2. **Access specifiers** (public, private, protected) control visibility
3. **Getters and setters** provide controlled access to private data
4. **Data hiding** prevents accidental modification and maintains invariants
5. **Benefits**: Security, maintainability, flexibility, reusability
6. **Rule of thumb**: Make data private, provide public interface

---