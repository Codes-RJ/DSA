# 13_Best_Practices/Theory.md

# C++ OOP Best Practices - Complete Guide

## 📖 Overview

Best practices in Object-Oriented Programming are guidelines that have emerged from years of experience in software development. Following these practices leads to code that is more maintainable, readable, reusable, and less prone to bugs. This guide covers essential OOP best practices for C++ development.

---

## 🎯 Key Areas of Best Practices

| Area | Description |
|------|-------------|
| **Coding Standards** | Naming, formatting, documentation |
| **Const Correctness** | Using const to prevent unintended modifications |
| **RAII** | Resource Acquisition Is Initialization |
| **Rule of Zero/Three/Five** | Proper resource management |
| **SOLID Principles** | Five fundamental design principles |
| **Common Pitfalls** | Mistakes to avoid |

---

## 1. **Coding Standards**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Good: Naming conventions
class EmployeeManager {                    // PascalCase for classes
public:
    static constexpr int MAX_EMPLOYEES = 100;  // UPPER_SNAKE_CASE for constants
    
    EmployeeManager() = default;            // Constructor
    
    void addEmployee(const string& name, int id) {  // camelCase for methods
        employees_.push_back(make_unique<Employee>(name, id));
    }
    
    const vector<unique_ptr<Employee>>& getEmployees() const {  // Getter
        return employees_;
    }
    
private:
    vector<unique_ptr<Employee>> employees_;  // Trailing underscore for members
};

// Good: Single responsibility
class Employee {
private:
    string name_;
    int id_;
    
public:
    Employee(string name, int id) : name_(move(name)), id_(id) {}
    
    string getName() const { return name_; }
    int getId() const { return id_; }
};

// Bad: Poor naming and formatting
class empMgr {
public:
    static const int max = 100;
    void add(string n, int i) {
        v.push_back(make_unique<emp>(n, i));
    }
    vector<unique_ptr<emp>> v;
};

class emp {
public:
    string n;
    int i;
    emp(string name, int id) : n(name), i(id) {}
};

int main() {
    cout << "=== Coding Standards ===" << endl;
    
    EmployeeManager manager;
    manager.addEmployee("Alice", 1001);
    manager.addEmployee("Bob", 1002);
    
    for (const auto& emp : manager.getEmployees()) {
        cout << "Employee: " << emp->getName() << " (ID: " << emp->getId() << ")" << endl;
    }
    
    return 0;
}
```

---

## 2. **Const Correctness**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class BankAccount {
private:
    string accountNumber_;
    double balance_;
    
public:
    BankAccount(string number, double balance) 
        : accountNumber_(move(number)), balance_(balance) {}
    
    // Const methods - promise not to modify object
    string getAccountNumber() const { return accountNumber_; }
    double getBalance() const { return balance_; }
    
    // Non-const methods - can modify
    void deposit(double amount) { balance_ += amount; }
    bool withdraw(double amount) {
        if (amount <= balance_) {
            balance_ -= amount;
            return true;
        }
        return false;
    }
};

class DataProcessor {
private:
    vector<int> data_;
    
public:
    void addData(int value) { data_.push_back(value); }
    
    // Const method - only reads
    int sum() const {
        int total = 0;
        for (int val : data_) total += val;
        return total;
    }
    
    // Const overload and non-const overload
    int& operator[](size_t index) { return data_[index]; }
    const int& operator[](size_t index) const { return data_[index]; }
};

// Function taking const reference - promises not to modify
void printAccount(const BankAccount& account) {
    cout << "Account: " << account.getAccountNumber() 
         << ", Balance: $" << account.getBalance() << endl;
    // account.deposit(100);  // Error! Cannot call non-const on const reference
}

int main() {
    cout << "=== Const Correctness ===" << endl;
    
    BankAccount account("123456", 1000);
    printAccount(account);
    
    // Const object can only call const methods
    const BankAccount constAccount("654321", 500);
    cout << "Const account balance: " << constAccount.getBalance() << endl;
    // constAccount.deposit(100);  // Error! Cannot call non-const
    
    DataProcessor processor;
    processor.addData(10);
    processor.addData(20);
    processor.addData(30);
    
    cout << "Sum: " << processor.sum() << endl;
    
    // Const reference to processor
    const DataProcessor& constProcessor = processor;
    cout << "Const processor sum: " << constProcessor.sum() << endl;
    // constProcessor.addData(40);  // Error! Cannot call non-const
    
    return 0;
}
```

---

## 3. **RAII (Resource Acquisition Is Initialization)**

```cpp
#include <iostream>
#include <fstream>
#include <mutex>
#include <thread>
#include <vector>
#include <stdexcept>
using namespace std;

// RAII for file handling
class FileHandler {
private:
    FILE* file_;
    string filename_;
    
public:
    FileHandler(const string& filename, const string& mode) 
        : filename_(filename) {
        file_ = fopen(filename.c_str(), mode.c_str());
        if (!file_) {
            throw runtime_error("Cannot open file: " + filename);
        }
        cout << "File opened: " << filename << endl;
    }
    
    ~FileHandler() {
        if (file_) {
            fclose(file_);
            cout << "File closed: " << filename_ << endl;
        }
    }
    
    void write(const string& data) {
        if (file_) {
            fprintf(file_, "%s\n", data.c_str());
        }
    }
    
    // Prevent copying
    FileHandler(const FileHandler&) = delete;
    FileHandler& operator=(const FileHandler&) = delete;
};

// RAII for mutex locking
class MutexGuard {
private:
    mutex& mtx_;
    
public:
    explicit MutexGuard(mutex& mtx) : mtx_(mtx) {
        mtx_.lock();
        cout << "Mutex locked" << endl;
    }
    
    ~MutexGuard() {
        mtx_.unlock();
        cout << "Mutex unlocked" << endl;
    }
    
    MutexGuard(const MutexGuard&) = delete;
    MutexGuard& operator=(const MutexGuard&) = delete;
};

class Counter {
private:
    int value_;
    mutex mtx_;
    
public:
    Counter() : value_(0) {}
    
    void increment() {
        MutexGuard lock(mtx_);  // RAII lock
        value_++;
    }
    
    int getValue() const {
        MutexGuard lock(mtx_);
        return value_;
    }
};

void worker(Counter& counter, int iterations) {
    for (int i = 0; i < iterations; i++) {
        counter.increment();
    }
}

int main() {
    cout << "=== RAII (Resource Acquisition Is Initialization) ===" << endl;
    
    cout << "\n1. File handling with RAII:" << endl;
    try {
        FileHandler file("test.txt", "w");
        file.write("Hello, RAII!");
        // File automatically closed when file goes out of scope
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    cout << "\n2. Mutex with RAII:" << endl;
    Counter counter;
    const int THREADS = 4;
    const int ITERATIONS = 100000;
    vector<thread> threads;
    
    for (int i = 0; i < THREADS; i++) {
        threads.emplace_back(worker, ref(counter), ITERATIONS);
    }
    
    for (auto& t : threads) {
        t.join();
    }
    
    cout << "Final count: " << counter.getValue() << endl;
    cout << "Expected: " << (THREADS * ITERATIONS) << endl;
    
    return 0;
}
```

---

## 4. **Rule of Zero/Three/Five**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <cstring>
using namespace std;

// Rule of Zero: Use RAII types, no custom destructor needed
class Employee {
private:
    string name_;           // std::string manages memory
    vector<string> skills_; // std::vector manages memory
    unique_ptr<int> bonus_; // smart pointer manages memory
    
public:
    Employee(string name) : name_(move(name)) {
        bonus_ = make_unique<int>(0);
    }
    
    void addSkill(const string& skill) {
        skills_.push_back(skill);
    }
    
    void setBonus(int bonus) { *bonus_ = bonus; }
    
    // No destructor, copy, move needed - Rule of Zero
};

// Rule of Three: Manual resource management (old style)
class StringBuffer {
private:
    char* data_;
    size_t size_;
    
public:
    StringBuffer(const char* str = "") {
        size_ = strlen(str);
        data_ = new char[size_ + 1];
        strcpy(data_, str);
    }
    
    // Destructor
    ~StringBuffer() {
        delete[] data_;
    }
    
    // Copy constructor
    StringBuffer(const StringBuffer& other) {
        size_ = other.size_;
        data_ = new char[size_ + 1];
        strcpy(data_, other.data_);
    }
    
    // Copy assignment
    StringBuffer& operator=(const StringBuffer& other) {
        if (this != &other) {
            delete[] data_;
            size_ = other.size_;
            data_ = new char[size_ + 1];
            strcpy(data_, other.data_);
        }
        return *this;
    }
    
    const char* c_str() const { return data_; }
};

// Rule of Five: Add move operations (modern C++)
class ModernStringBuffer {
private:
    char* data_;
    size_t size_;
    
public:
    ModernStringBuffer(const char* str = "") {
        size_ = strlen(str);
        data_ = new char[size_ + 1];
        strcpy(data_, str);
    }
    
    ~ModernStringBuffer() {
        delete[] data_;
    }
    
    // Copy constructor
    ModernStringBuffer(const ModernStringBuffer& other) {
        size_ = other.size_;
        data_ = new char[size_ + 1];
        strcpy(data_, other.data_);
    }
    
    // Copy assignment
    ModernStringBuffer& operator=(const ModernStringBuffer& other) {
        if (this != &other) {
            delete[] data_;
            size_ = other.size_;
            data_ = new char[size_ + 1];
            strcpy(data_, other.data_);
        }
        return *this;
    }
    
    // Move constructor
    ModernStringBuffer(ModernStringBuffer&& other) noexcept
        : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr;
        other.size_ = 0;
    }
    
    // Move assignment
    ModernStringBuffer& operator=(ModernStringBuffer&& other) noexcept {
        if (this != &other) {
            delete[] data_;
            data_ = other.data_;
            size_ = other.size_;
            other.data_ = nullptr;
            other.size_ = 0;
        }
        return *this;
    }
    
    const char* c_str() const { return data_; }
};

int main() {
    cout << "=== Rule of Zero/Three/Five ===" << endl;
    
    cout << "\n1. Rule of Zero (preferred):" << endl;
    Employee emp("Alice");
    emp.addSkill("C++");
    emp.addSkill("Python");
    emp.setBonus(5000);
    // No manual cleanup needed
    
    cout << "\n2. Rule of Three (manual management):" << endl;
    StringBuffer sb1("Hello");
    StringBuffer sb2 = sb1;  // Copy constructor
    cout << "sb1: " << sb1.c_str() << endl;
    cout << "sb2: " << sb2.c_str() << endl;
    
    cout << "\n3. Rule of Five (with move semantics):" << endl;
    ModernStringBuffer msb1("World");
    ModernStringBuffer msb2 = move(msb1);  // Move constructor
    cout << "msb2: " << msb2.c_str() << endl;
    // msb1 is now in valid but unspecified state
    
    return 0;
}
```

---

## 5. **SOLID Principles**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <cmath>
using namespace std;

// ============ S: Single Responsibility ============
// Bad: Class with multiple responsibilities
class BadReport {
    string data;
public:
    void calculate() { /* ... */ }
    void print() { /* ... */ }
    void save() { /* ... */ }
};

// Good: Separate classes for each responsibility
class ReportData {
    string data_;
public:
    void calculate() { /* ... */ }
    string getData() const { return data_; }
};

class ReportPrinter {
public:
    void print(const ReportData& data) { /* ... */ }
};

class ReportSaver {
public:
    void save(const ReportData& data) { /* ... */ }
};

// ============ O: Open/Closed ============
// Bad: Modifying existing class to add new shapes
class BadAreaCalculator {
public:
    double calculateArea(const string& shape, double param1, double param2 = 0) {
        if (shape == "circle") return 3.14159 * param1 * param1;
        if (shape == "rectangle") return param1 * param2;
        return 0;
    }
};

// Good: Open for extension, closed for modification
class Shape {
public:
    virtual double area() const = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape {
    double radius_;
public:
    Circle(double r) : radius_(r) {}
    double area() const override { return 3.14159 * radius_ * radius_; }
};

class Rectangle : public Shape {
    double width_, height_;
public:
    Rectangle(double w, double h) : width_(w), height_(h) {}
    double area() const override { return width_ * height_; }
};

class AreaCalculator {
public:
    double calculateTotal(const vector<unique_ptr<Shape>>& shapes) {
        double total = 0;
        for (const auto& shape : shapes) {
            total += shape->area();
        }
        return total;
    }
};

// ============ L: Liskov Substitution ============
class Bird {
public:
    virtual void move() { cout << "Flying" << endl; }
    virtual ~Bird() = default;
};

// Bad: Penguin can't fly, violates LSP
class Penguin : public Bird {
public:
    void move() override { cout << "Walking" << endl; }
};

// Good: Better design
class FlyingBird : public Bird {
public:
    void move() override { cout << "Flying" << endl; }
};

class WalkingBird {
public:
    void move() { cout << "Walking" << endl; }
};

// ============ I: Interface Segregation ============
// Bad: Fat interface
class IMachine {
public:
    virtual void print() = 0;
    virtual void scan() = 0;
    virtual void fax() = 0;
    virtual ~IMachine() = default;
};

// Good: Segregated interfaces
class IPrinter {
public:
    virtual void print() = 0;
    virtual ~IPrinter() = default;
};

class IScanner {
public:
    virtual void scan() = 0;
    virtual ~IScanner() = default;
};

class IFax {
public:
    virtual void fax() = 0;
    virtual ~IFax() = default;
};

// ============ D: Dependency Inversion ============
// Bad: High-level module depends on low-level module
class BadKeyboard {
public:
    string read() { return "key pressed"; }
};

class BadComputer {
    BadKeyboard keyboard_;
public:
    string getInput() { return keyboard_.read(); }
};

// Good: Depend on abstractions
class IInputDevice {
public:
    virtual string read() = 0;
    virtual ~IInputDevice() = default;
};

class Keyboard : public IInputDevice {
public:
    string read() override { return "key pressed"; }
};

class Mouse : public IInputDevice {
public:
    string read() override { return "mouse clicked"; }
};

class Computer {
    IInputDevice& inputDevice_;
public:
    Computer(IInputDevice& device) : inputDevice_(device) {}
    string getInput() { return inputDevice_.read(); }
};

int main() {
    cout << "=== SOLID Principles ===" << endl;
    
    cout << "\n1. Open/Closed Principle:" << endl;
    vector<unique_ptr<Shape>> shapes;
    shapes.push_back(make_unique<Circle>(5));
    shapes.push_back(make_unique<Rectangle>(4, 6));
    
    AreaCalculator calc;
    cout << "Total area: " << calc.calculateTotal(shapes) << endl;
    
    cout << "\n2. Dependency Inversion:" << endl;
    Keyboard keyboard;
    Computer computer(keyboard);
    cout << "Input: " << computer.getInput() << endl;
    
    return 0;
}
```

---

## 6. **Common Pitfalls to Avoid**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Pitfall 1: Object Slicing
class Base {
public:
    virtual void speak() { cout << "Base" << endl; }
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void speak() override { cout << "Derived" << endl; }
    void derivedOnly() { cout << "Derived only" << endl; }
};

void slicingExample() {
    Derived d;
    Base b = d;  // Slicing! Derived part lost
    b.speak();   // Calls Base::speak()
    
    Base& ref = d;  // No slicing
    ref.speak();    // Calls Derived::speak()
}

// Pitfall 2: Memory Leak
void memoryLeakExample() {
    int* ptr = new int(42);
    // Missing delete - memory leak!
}

// Pitfall 3: Dangling Pointer
void danglingPointerExample() {
    int* ptr = new int(42);
    delete ptr;
    // ptr is now dangling
    // *ptr = 100;  // Undefined behavior!
    ptr = nullptr;  // Good practice
}

// Pitfall 4: Double Delete
void doubleDeleteExample() {
    int* ptr = new int(42);
    delete ptr;
    // delete ptr;  // Undefined behavior - double delete!
}

// Pitfall 5: Not Using Virtual Destructor
class BaseNoVirtual {
public:
    ~BaseNoVirtual() { cout << "Base destructor" << endl; }
};

class DerivedNoVirtual : public BaseNoVirtual {
    int* data_;
public:
    DerivedNoVirtual() : data_(new int(42)) {}
    ~DerivedNoVirtual() { delete data_; cout << "Derived destructor" << endl; }
};

void virtualDestructorExample() {
    BaseNoVirtual* ptr = new DerivedNoVirtual();
    delete ptr;  // Only Base destructor called! Memory leak!
}

// Pitfall 6: Copying Raw Pointers
class BadCopy {
    int* data_;
public:
    BadCopy() : data_(new int(42)) {}
    ~BadCopy() { delete data_; }
    // No copy constructor - shallow copy causes double delete!
};

class GoodCopy {
    unique_ptr<int> data_;
public:
    GoodCopy() : data_(make_unique<int>(42)) {}
    // No need for explicit destructor - unique_ptr handles it
};

int main() {
    cout << "=== Common Pitfalls to Avoid ===" << endl;
    
    cout << "\n1. Object Slicing:" << endl;
    slicingExample();
    
    cout << "\n2. Always use virtual destructor for polymorphic classes" << endl;
    // virtualDestructorExample();  // Uncomment to see issue
    
    cout << "\n3. Use smart pointers instead of raw pointers" << endl;
    cout << "   unique_ptr, shared_ptr, weak_ptr" << endl;
    
    cout << "\n4. Follow Rule of Zero/Three/Five" << endl;
    
    cout << "\n5. Use RAII for resource management" << endl;
    
    cout << "\n6. Initialize all variables" << endl;
    
    return 0;
}
```

---

## 📊 Best Practices Summary

| Area | Key Practice |
|------|--------------|
| **Naming** | PascalCase for classes, camelCase for methods, UPPER_CASE for constants |
| **Const** | Mark methods const when they don't modify object |
| **RAII** | Acquire resources in constructor, release in destructor |
| **Rule of Zero** | Prefer RAII types over manual resource management |
| **SOLID** | Apply five principles for maintainable design |
| **Smart Pointers** | Use instead of raw pointers for ownership |

---

## ✅ Key Takeaways

1. **Follow consistent naming conventions**
2. **Use const correctness** to prevent unintended modifications
3. **Apply RAII** for all resource management
4. **Prefer Rule of Zero** - use RAII types
5. **Apply SOLID principles** for maintainable design
6. **Use smart pointers** instead of raw pointers
7. **Make destructors virtual** for polymorphic classes
8. **Initialize all variables** before use

---