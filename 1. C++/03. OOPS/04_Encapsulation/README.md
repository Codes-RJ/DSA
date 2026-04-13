Here is the `README.md` for the **04_Encapsulation** folder inside OOPS.

---

# README.md

## Encapsulation in C++ - Complete Guide

### Overview

Encapsulation is one of the four fundamental pillars of Object-Oriented Programming (along with Inheritance, Polymorphism, and Abstraction). It is the mechanism of bundling data (variables) and methods (functions) that operate on that data into a single unit (class), while restricting direct access to some of the object's internal components. Encapsulation protects the integrity of data by preventing unauthorized access and modification.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Data_Hiding.md](01_Data_Hiding.md) | understand Data Hiding |
| 2. | [02_Getters_and_Setters.md](02_Getters_and_Setters.md) | understand Getters and Setters |
| 3. | [03_Access_Control.md](03_Access_Control.md) | understand Access Control |
| 4. | [04_Practical_Examples.md](04_Practical_Examples.md) | understand Practical Examples of Encapsulation |
| 5. | [05_Best_Practices.md](05_Best_Practices.md) | understand Encapsulation Best Practices |
| 6. | [Theory.md](Theory.md) | understand Theoretical Foundations of Encapsulation |

---

## 1. Data Hiding

This topic explains the concept of hiding internal data from outside access.

**File:** [01_Data_Hiding.md](01_Data_Hiding.md)

**What you will learn:**
- What is data hiding
- Why data hiding is important
- Using `private` access specifier to hide data
- Difference between data hiding and abstraction
- Benefits of data hiding (security, integrity, decoupling)

**Key Concepts:**
- **Internal State** - Data that should not be directly accessible
- **Private Members** - Accessible only within the class
- **Integrity** - Prevents invalid state from outside modifications
- **Loose Coupling** - Internal changes don't affect external code

**Syntax:**
```cpp
class BankAccount {
private:
    double balance_;      // Hidden from outside
    string accountNumber_;
    int pin_;
    
public:
    void deposit(double amount) {
        if (amount > 0) {
            balance_ += amount;
        }
    }
    
    bool withdraw(double amount, int enteredPin) {
        if (enteredPin == pin_ && amount <= balance_) {
            balance_ -= amount;
            return true;
        }
        return false;
    }
};

// Outside code cannot directly access balance_, accountNumber_, or pin_
// They must use the public methods
```

---

## 2. Getters and Setters

This topic explains how to provide controlled access to private data members.

**File:** [02_Getters_and_Setters.md](02_Getters_and_Setters.md)

**What you will learn:**
- What are getters (accessors) and setters (mutators)
- Why use getters instead of public data members
- Read-only properties (getter without setter)
- Validation in setters
- Const-correctness with getters
- When to use and when to avoid getters/setters

**Key Concepts:**
- **Getter** - Public method that returns private data (read access)
- **Setter** - Public method that modifies private data (write access)
- **Validation** - Setters can validate data before assignment
- **Read-Only** - Provide getter without setter
- **Write-Only** - Provide setter without getter (rare)

**Syntax:**
```cpp
class Employee {
private:
    string name_;
    int age_;
    double salary_;
    
public:
    // Getter (read access)
    string getName() const { return name_; }
    int getAge() const { return age_; }
    double getSalary() const { return salary_; }
    
    // Setter (write access with validation)
    void setName(const string& name) {
        if (!name.empty()) {
            name_ = name;
        }
    }
    
    void setAge(int age) {
        if (age >= 18 && age <= 65) {
            age_ = age;
        }
    }
    
    void setSalary(double salary) {
        if (salary >= 0) {
            salary_ = salary;
        }
    }
};

// Usage
Employee emp;
emp.setName("John");      // Valid
emp.setAge(25);           // Valid
emp.setAge(150);          // Invalid - age unchanged
cout << emp.getName();    // Returns "John"
```

---

## 3. Access Control

This topic explains the three access specifiers in C++ and how they control visibility.

**File:** [03_Access_Control.md](03_Access_Control.md)

**What you will learn:**
- `public` - Accessible from anywhere
- `private` - Accessible only within the class
- `protected` - Accessible within class and derived classes
- Default access in class vs struct
- Access control in inheritance
- Friend functions and classes (bypassing access control)

**Key Concepts:**

| Specifier | Same Class | Derived Class | Outside Class |
|-----------|------------|---------------|---------------|
| **public** | Yes | Yes | Yes |
| **protected** | Yes | Yes | No |
| **private** | Yes | No | No |

**Syntax:**
```cpp
class AccessExample {
private:
    int privateVar_;      // Only AccessExample can access
    
protected:
    int protectedVar_;    // AccessExample and derived classes
    
public:
    int publicVar_;       // Anyone can access
    
    void publicMethod() {
        privateVar_ = 10;     // OK - inside class
        protectedVar_ = 20;   // OK - inside class
        publicVar_ = 30;      // OK - inside class
    }
};

class Derived : public AccessExample {
public:
    void derivedMethod() {
        // privateVar_ = 10;   // Error - cannot access private
        protectedVar_ = 20;    // OK - derived can access protected
        publicVar_ = 30;       // OK - public is accessible
    }
};

int main() {
    AccessExample obj;
    // obj.privateVar_ = 10;   // Error
    // obj.protectedVar_ = 20; // Error
    obj.publicVar_ = 30;        // OK
    obj.publicMethod();         // OK
}
```

---

## 4. Practical Examples

This topic provides real-world examples of encapsulation in action.

**File:** [04_Practical_Examples.md](04_Practical_Examples.md)

**What you will learn:**
- Encapsulation in banking systems
- Encapsulation in employee management
- Encapsulation in inventory systems
- Encapsulation in game development (health, score)
- Encapsulation in sensor data processing

**Key Concepts:**
- **Bank Account** - Balance hidden, accessed via deposit/withdraw
- **Student Record** - Grades hidden, accessed via validation
- **Thermostat** - Temperature hidden, accessed with bounds checking
- **Health System** - Patient data hidden, accessed with authorization

**Example: Bank Account**
```cpp
class BankAccount {
private:
    string accountNumber_;
    double balance_;
    string pin_;
    
public:
    BankAccount(string accNo, string pin) 
        : accountNumber_(accNo), balance_(0), pin_(pin) {}
    
    bool withdraw(double amount, string enteredPin) {
        if (enteredPin != pin_) {
            cout << "Invalid PIN" << endl;
            return false;
        }
        if (amount > balance_) {
            cout << "Insufficient funds" << endl;
            return false;
        }
        balance_ -= amount;
        return true;
    }
    
    void deposit(double amount) {
        if (amount > 0) {
            balance_ += amount;
        }
    }
    
    double getBalance(string enteredPin) const {
        if (enteredPin == pin_) {
            return balance_;
        }
        return -1;  // Invalid PIN
    }
};
```

---

## 5. Best Practices

This topic covers guidelines for effective encapsulation.

**File:** [05_Best_Practices.md](05_Best_Practices.md)

**What you will learn:**
- Keep data members private by default
- Provide public getters/setters only when necessary
- Validate data in setters
- Use const-correctness
- Avoid exposing internal data structures
- Prefer composition over getters that expose internals

**Key Concepts:**

| Practice | Description |
|----------|-------------|
| **Minimal Interface** | Expose only what is necessary |
| **Const Correctness** | Mark getters as `const` |
| **Validation** | Check data before modifying |
| **Return by Value** | Avoid returning references to internal data |
| **No Public Data** | Never make data members public |

**Syntax:**
```cpp
class BestPractice {
private:
    vector<int> data_;
    
public:
    // Good: Returns copy, not reference
    vector<int> getData() const {
        return data_;
    }
    
    // Good: Validation before modification
    void setData(const vector<int>& newData) {
        if (!newData.empty()) {
            data_ = newData;
        }
    }
    
    // Good: Provides specific functionality instead of exposing data
    int getSize() const {
        return data_.size();
    }
    
    // Good: Const-correct getter
    bool isEmpty() const {
        return data_.empty();
    }
};
```

---

## 6. Theoretical Foundations

This topic covers the theoretical concepts behind encapsulation.

**File:** [Theory.md](Theory.md)

**What you will learn:**
- History of encapsulation in OOP
- Information hiding principle (David Parnas)
- Encapsulation vs Abstraction
- Law of Demeter (principle of least knowledge)
- Encapsulation and modularity
- Encapsulation in large systems

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Information Hiding** | Hide design decisions that are likely to change |
| **Law of Demeter** | Only talk to immediate friends (don't chain calls) |
| **Modularity** | Encapsulation enables independent modules |
| **Maintainability** | Changes inside don't affect outside |

**Law of Demeter Example:**
```cpp
// Violates Law of Demeter (chained calls)
obj.getA().getB().getC().doSomething();

// Complies with Law of Demeter
obj.doSomething();  // Class handles the delegation internally
```

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - Variables, functions
- [02_Classes_and_Objects/README.md](../02_Classes_and_Objects/README.md) - Class basics
- [03_Constructors_and_Destructors/README.md](../03_Constructors_and_Destructors/README.md) - Object initialization

---

### Sample Encapsulation Example

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Student {
private:
    string name_;
    int rollNumber_;
    vector<int> marks_;
    static int totalStudents_;
    
public:
    // Constructor
    Student(string name, int roll) : name_(name), rollNumber_(roll) {
        totalStudents_++;
    }
    
    // Getter (read-only for name and roll)
    string getName() const { return name_; }
    int getRollNumber() const { return rollNumber_; }
    
    // Add mark with validation
    void addMark(int mark) {
        if (mark >= 0 && mark <= 100) {
            marks_.push_back(mark);
        } else {
            cout << "Invalid mark: " << mark << endl;
        }
    }
    
    // Get average (computed, not stored)
    double getAverage() const {
        if (marks_.empty()) return 0;
        int sum = 0;
        for (int m : marks_) {
            sum += m;
        }
        return static_cast<double>(sum) / marks_.size();
    }
    
    // Static getter
    static int getTotalStudents() { return totalStudents_; }
    
    // Display (controlled output)
    void display() const {
        cout << "Name: " << name_ << ", Roll: " << rollNumber_;
        cout << ", Average: " << getAverage() << endl;
    }
};

int Student::totalStudents_ = 0;

int main() {
    Student s1("Alice", 101);
    Student s2("Bob", 102);
    
    s1.addMark(85);
    s1.addMark(90);
    s1.addMark(78);
    
    s2.addMark(92);
    s2.addMark(88);
    
    s1.display();
    s2.display();
    
    cout << "Total students: " << Student::getTotalStudents() << endl;
    
    return 0;
}
```

---

### Learning Path

```
Level 1: Core Concepts
├── Data Hiding
├── Public vs Private
└── Access Control

Level 2: Controlled Access
├── Getters and Setters
├── Validation in Setters
└── Const-Correctness

Level 3: Advanced Topics
├── Friend Functions and Classes
├── Protected Access
└── Encapsulation in Inheritance

Level 4: Practical Application
├── Real-World Examples
├── Best Practices
└── Law of Demeter
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Making all data members public | Use private by default |
| Exposing internal data structures | Return copies, not references |
| Getters and setters for everything | Only provide what is necessary |
| Forgetting const on getters | Mark getters that don't modify as `const` |
| Returning pointers to internal data | Return by value or const reference |
| No validation in setters | Always validate before assignment |

---

### Practice Questions

After completing this section, you should be able to:

1. Explain what encapsulation is and why it is important
2. Differentiate between data hiding and abstraction
3. Write a class with private data members and public getters/setters
4. Implement validation in setters
5. Explain the difference between public, private, and protected
6. Use const-correctness with getters
7. Apply the Law of Demeter in class design
8. Identify and fix poor encapsulation in existing code

---

### Next Steps

- Go to [Theory](Theory.md) to understand basics.