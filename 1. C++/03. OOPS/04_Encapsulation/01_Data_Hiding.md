# 04_Encapsulation/01_Data_Hiding.md

# Data Hiding in C++ - Complete Guide

## 📖 Overview

Data hiding is a fundamental concept of encapsulation that restricts direct access to an object's internal data. It ensures that the internal representation of an object is hidden from the outside world, preventing unauthorized access and accidental modification. Data hiding is achieved primarily through the `private` and `protected` access specifiers.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Data Hiding** | Restricting direct access to internal data members |
| **Implementation Hiding** | Hiding how the class works internally |
| **Interface** | Public methods that provide controlled access |
| **Invariants** | Conditions that must hold true for valid object state |

---

## 1. **Basic Data Hiding**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Class with proper data hiding
class BankAccount {
private:
    string accountNumber;  // Hidden from outside
    double balance;        // Hidden from outside
    string pin;            // Hidden from outside
    bool isLocked;         // Hidden from outside
    
public:
    // Constructor
    BankAccount(string accNo, double initial, string p) 
        : accountNumber(accNo), balance(initial), pin(p), isLocked(false) {}
    
    // Public interface - only way to interact
    void deposit(double amount) {
        if (amount > 0 && !isLocked) {
            balance += amount;
            cout << "Deposited: $" << amount << endl;
        }
    }
    
    bool withdraw(double amount, string inputPin) {
        if (isLocked) {
            cout << "Account is locked!" << endl;
            return false;
        }
        
        if (inputPin != pin) {
            cout << "Invalid PIN!" << endl;
            return false;
        }
        
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            cout << "Withdrawn: $" << amount << endl;
            return true;
        }
        
        cout << "Insufficient funds!" << endl;
        return false;
    }
    
    double getBalance(string inputPin) const {
        if (inputPin == pin) {
            return balance;
        }
        return -1;  // Invalid PIN indicator
    }
    
    void lockAccount() {
        isLocked = true;
        cout << "Account locked" << endl;
    }
    
    void unlockAccount(string inputPin) {
        if (inputPin == pin) {
            isLocked = false;
            cout << "Account unlocked" << endl;
        }
    }
};

int main() {
    cout << "=== Basic Data Hiding ===" << endl;
    
    BankAccount account("12345678", 1000.0, "1234");
    
    // Cannot access private members directly
    // account.balance = 9999;        // Error! Private
    // account.pin = "9999";          // Error! Private
    // account.isLocked = true;        // Error! Private
    
    // Must use public interface
    cout << "Initial balance: $" << account.getBalance("1234") << endl;
    
    account.deposit(500);
    account.withdraw(200, "1234");
    
    cout << "Final balance: $" << account.getBalance("1234") << endl;
    
    // Wrong PIN - access denied
    cout << "\nAttempting with wrong PIN:" << endl;
    account.withdraw(100, "9999");
    cout << "Balance with wrong PIN: " << account.getBalance("9999") << endl;
    
    // Lock account
    cout << "\nLocking account:" << endl;
    account.lockAccount();
    account.withdraw(100, "1234");  // Should fail
    
    return 0;
}
```

**Output:**
```
=== Basic Data Hiding ===
Initial balance: $1000
Deposited: $500
Withdrawn: $200
Final balance: $1300

Attempting with wrong PIN:
Invalid PIN!
Balance with wrong PIN: -1

Locking account:
Account locked
Account is locked!
```

---

## 2. **Why Data Hiding Matters**

```cpp
#include <iostream>
#include <string>
using namespace std;

// BAD: No data hiding - vulnerable to corruption
class BadAccount {
public:
    string accountNumber;
    double balance;
    string pin;
    
    void display() {
        cout << "Account: " << accountNumber 
             << ", Balance: $" << balance << endl;
    }
};

// GOOD: Proper data hiding
class GoodAccount {
private:
    string accountNumber;
    double balance;
    string pin;
    
public:
    GoodAccount(string accNo, double initial, string p) 
        : accountNumber(accNo), balance(initial), pin(p) {}
    
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited: $" << amount << endl;
        }
    }
    
    bool withdraw(double amount, string inputPin) {
        if (inputPin != pin) {
            cout << "Invalid PIN!" << endl;
            return false;
        }
        
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            cout << "Withdrawn: $" << amount << endl;
            return true;
        }
        
        cout << "Insufficient funds!" << endl;
        return false;
    }
    
    double getBalance(string inputPin) const {
        return (inputPin == pin) ? balance : -1;
    }
    
    void display() const {
        cout << "Account: " << accountNumber 
             << ", Balance: $" << balance << endl;
    }
};

int main() {
    cout << "=== Why Data Hiding Matters ===" << endl;
    
    cout << "\n1. BAD: No data hiding - can be corrupted:" << endl;
    BadAccount bad;
    bad.accountNumber = "12345";
    bad.balance = 1000;
    bad.pin = "1234";
    
    cout << "Original: ";
    bad.display();
    
    // Direct modification - no validation!
    bad.balance = -5000;  // Negative balance! Invalid!
    bad.pin = "0000";      // PIN changed without verification!
    
    cout << "After corruption: ";
    bad.display();
    cout << "PIN changed to: " << bad.pin << " (without verification!)" << endl;
    
    cout << "\n2. GOOD: Proper data hiding - protected:" << endl;
    GoodAccount good("12345", 1000, "1234");
    good.display();
    
    // Cannot modify directly - compiler prevents it!
    // good.balance = -5000;  // Error! Private member
    // good.pin = "0000";      // Error! Private member
    
    // Must go through validated interface
    good.withdraw(2000, "1234");  // Fails due to insufficient funds
    good.withdraw(500, "9999");   // Fails due to wrong PIN
    good.withdraw(300, "1234");   // Success
    
    good.display();
    
    return 0;
}
```

**Output:**
```
=== Why Data Hiding Matters ===

1. BAD: No data hiding - can be corrupted:
Original: Account: 12345, Balance: $1000
After corruption: Account: 12345, Balance: $-5000
PIN changed to: 0000 (without verification!)

2. GOOD: Proper data hiding - protected:
Account: 12345, Balance: $1000
Insufficient funds!
Invalid PIN!
Withdrawn: $300
Account: 12345, Balance: $700
```

---

## 3. **Maintaining Invariants**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

class Rectangle {
private:
    double width;
    double height;
    
    // Invariant: width > 0, height > 0
    
    void validate() {
        if (width <= 0) width = 1;
        if (height <= 0) height = 1;
    }
    
public:
    Rectangle(double w, double h) : width(w), height(h) {
        validate();
    }
    
    void setWidth(double w) {
        if (w > 0) {
            width = w;
        } else {
            cout << "Invalid width! Using previous value." << endl;
        }
    }
    
    void setHeight(double h) {
        if (h > 0) {
            height = h;
        } else {
            cout << "Invalid height! Using previous value." << endl;
        }
    }
    
    double area() const {
        return width * height;
    }
    
    double perimeter() const {
        return 2 * (width + height);
    }
    
    void display() const {
        cout << "Rectangle: " << width << " x " << height 
             << ", Area: " << area() << ", Perimeter: " << perimeter() << endl;
    }
};

class Date {
private:
    int day, month, year;
    
    // Helper function to check if year is leap
    bool isLeapYear(int y) const {
        return (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);
    }
    
    // Get days in month
    int daysInMonth(int m, int y) const {
        switch (m) {
            case 2: return isLeapYear(y) ? 29 : 28;
            case 4: case 6: case 9: case 11: return 30;
            default: return 31;
        }
    }
    
    // Validate and normalize date
    void normalize() {
        if (year < 1) year = 1;
        if (month < 1) month = 1;
        if (month > 12) month = 12;
        
        int maxDay = daysInMonth(month, year);
        if (day < 1) day = 1;
        if (day > maxDay) day = maxDay;
    }
    
public:
    Date(int d, int m, int y) : day(d), month(m), year(y) {
        normalize();
    }
    
    void setDay(int d) {
        day = d;
        normalize();
    }
    
    void setMonth(int m) {
        month = m;
        normalize();
    }
    
    void setYear(int y) {
        year = y;
        normalize();
    }
    
    void addDays(int days) {
        day += days;
        while (day > daysInMonth(month, year)) {
            day -= daysInMonth(month, year);
            month++;
            if (month > 12) {
                month = 1;
                year++;
            }
        }
        while (day < 1) {
            month--;
            if (month < 1) {
                month = 12;
                year--;
            }
            day += daysInMonth(month, year);
        }
    }
    
    void display() const {
        cout << day << "/" << month << "/" << year << endl;
    }
};

int main() {
    cout << "=== Maintaining Invariants ===" << endl;
    
    cout << "\n1. Rectangle with invariant (width>0, height>0):" << endl;
    Rectangle r1(5, 3);
    r1.display();
    
    r1.setWidth(-2);  // Invalid - ignored
    r1.setHeight(0);  // Invalid - ignored
    r1.display();
    
    cout << "\n2. Date with invariant (valid date):" << endl;
    Date d1(31, 2, 2024);  // Feb 31 -> normalized to Feb 29 (leap year)
    d1.display();
    
    Date d2(31, 4, 2024);   // April 31 -> normalized to April 30
    d2.display();
    
    Date d3(15, 13, 2024);  // Month 13 -> normalized to December
    d3.display();
    
    cout << "\n3. Adding days maintains invariant:" << endl;
    Date d4(28, 2, 2024);
    cout << "Start: "; d4.display();
    d4.addDays(3);
    cout << "After +3 days: "; d4.display();
    
    return 0;
}
```

**Output:**
```
=== Maintaining Invariants ===

1. Rectangle with invariant (width>0, height>0):
Rectangle: 5 x 3, Area: 15, Perimeter: 16
Invalid width! Using previous value.
Invalid height! Using previous value.
Rectangle: 5 x 3, Area: 15, Perimeter: 16

2. Date with invariant (valid date):
29/2/2024
30/4/2024
15/12/2024

3. Adding days maintains invariant:
Start: 28/2/2024
After +3 days: 2/3/2024
```

---

## 4. **Data Hiding with Pointers and References**

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class StringBuffer {
private:
    char* data;
    size_t length;
    
public:
    // Constructor
    StringBuffer(const char* str = "") {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "Created: " << data << endl;
    }
    
    // Copy constructor (deep copy)
    StringBuffer(const StringBuffer& other) {
        length = other.length;
        data = new char[length + 1];
        strcpy(data, other.data);
        cout << "Copied: " << data << endl;
    }
    
    // Destructor
    ~StringBuffer() {
        if (data) {
            cout << "Destroyed: " << data << endl;
            delete[] data;
        }
    }
    
    // Getter returns const reference - prevents modification
    const char* getData() const {
        return data;
    }
    
    // Setter with validation
    void setData(const char* str) {
        if (str && strlen(str) > 0) {
            delete[] data;
            length = strlen(str);
            data = new char[length + 1];
            strcpy(data, str);
            cout << "Updated: " << data << endl;
        }
    }
    
    // Returns length (read-only)
    size_t getLength() const {
        return length;
    }
    
    // Safe character access with bounds checking
    char charAt(size_t index) const {
        if (index < length) {
            return data[index];
        }
        return '\0';
    }
};

class ConfigManager {
private:
    StringBuffer configPath;
    int* settings;      // Dynamic array
    int settingCount;
    
public:
    ConfigManager(const char* path, int count) 
        : configPath(path), settingCount(count) {
        settings = new int[count];
        for (int i = 0; i < count; i++) {
            settings[i] = 0;
        }
        cout << "ConfigManager created with " << count << " settings" << endl;
    }
    
    // Copy constructor (deep copy)
    ConfigManager(const ConfigManager& other) 
        : configPath(other.configPath), settingCount(other.settingCount) {
        settings = new int[settingCount];
        for (int i = 0; i < settingCount; i++) {
            settings[i] = other.settings[i];
        }
        cout << "ConfigManager copied" << endl;
    }
    
    // Destructor
    ~ConfigManager() {
        delete[] settings;
        cout << "ConfigManager destroyed" << endl;
    }
    
    // Getter returns const reference to internal data
    const StringBuffer& getConfigPath() const {
        return configPath;
    }
    
    // Getter returns copy (for primitive types)
    int getSetting(int index) const {
        if (index >= 0 && index < settingCount) {
            return settings[index];
        }
        return -1;
    }
    
    // Setter with validation
    void setSetting(int index, int value) {
        if (index >= 0 && index < settingCount) {
            if (value >= 0 && value <= 100) {  // Validate range
                settings[index] = value;
                cout << "Setting[" << index << "] = " << value << endl;
            }
        }
    }
    
    void display() const {
        cout << "Config Path: " << configPath.getData() << endl;
        cout << "Settings: ";
        for (int i = 0; i < settingCount; i++) {
            cout << settings[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    cout << "=== Data Hiding with Pointers and References ===" << endl;
    
    cout << "\n1. StringBuffer with deep copy:" << endl;
    StringBuffer s1("Hello");
    StringBuffer s2 = s1;  // Deep copy
    cout << "s1: " << s1.getData() << endl;
    cout << "s2: " << s2.getData() << endl;
    
    s1.setData("World");
    cout << "After modification:" << endl;
    cout << "s1: " << s1.getData() << endl;
    cout << "s2: " << s2.getData() << endl;  // Unchanged
    
    cout << "\n2. ConfigManager with dynamic allocation:" << endl;
    ConfigManager config1("/etc/config", 5);
    config1.setSetting(0, 50);
    config1.setSetting(1, 75);
    config1.display();
    
    ConfigManager config2 = config1;  // Deep copy
    config2.setSetting(0, 100);
    
    cout << "\nconfig1 after config2 modified:" << endl;
    config1.display();
    cout << "\nconfig2:" << endl;
    config2.display();
    
    return 0;
}
```

---

## 5. **Practical Example: Employee Management with Data Hiding**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <ctime>
using namespace std;

class Employee {
private:
    int id;
    string name;
    double salary;
    string department;
    time_t hireDate;
    bool active;
    static int nextId;
    
    // Private helper methods
    void validateSalary() {
        if (salary < 0) salary = 0;
    }
    
    void validateName() {
        if (name.empty()) name = "Unknown";
    }
    
    string formatDate(time_t t) const {
        struct tm* timeinfo = localtime(&t);
        char buffer[20];
        strftime(buffer, sizeof(buffer), "%Y-%m-%d", timeinfo);
        return string(buffer);
    }
    
public:
    // Constructor
    Employee(string n, string dept, double sal) 
        : name(n), department(dept), salary(sal), active(true) {
        id = nextId++;
        hireDate = time(nullptr);
        validateName();
        validateSalary();
        cout << "Employee created: " << name << " (ID: " << id << ")" << endl;
    }
    
    // Getters - controlled read access
    int getId() const { return id; }
    string getName() const { return name; }
    string getDepartment() const { return department; }
    string getHireDate() const { return formatDate(hireDate); }
    bool isActive() const { return active; }
    
    // Get salary with verification (manager access)
    double getSalary(const string& requesterRole) const {
        if (requesterRole == "Manager" || requesterRole == "HR") {
            return salary;
        }
        return -1;  // Access denied
    }
    
    // Setters with validation
    void setName(string n) {
        if (!n.empty()) {
            name = n;
            cout << "Name updated to: " << name << endl;
        }
    }
    
    void setDepartment(string dept) {
        if (dept == "Engineering" || dept == "Sales" || 
            dept == "HR" || dept == "Marketing") {
            department = dept;
            cout << "Department updated to: " << department << endl;
        }
    }
    
    void setSalary(double sal, string requesterRole) {
        if ((requesterRole == "Manager" || requesterRole == "HR") && sal >= 0) {
            double oldSalary = salary;
            salary = sal;
            cout << "Salary updated from $" << oldSalary 
                 << " to $" << salary << endl;
        } else {
            cout << "Unauthorized salary modification attempt!" << endl;
        }
    }
    
    // Business logic methods
    void giveRaise(double percent, string requesterRole) {
        if ((requesterRole == "Manager" || requesterRole == "HR") && percent > 0) {
            double oldSalary = salary;
            salary += salary * (percent / 100);
            cout << name << " received " << percent << "% raise. "
                 << "Salary: $" << oldSalary << " → $" << salary << endl;
        }
    }
    
    void terminate(string requesterRole) {
        if (requesterRole == "Manager" || requesterRole == "HR") {
            active = false;
            cout << name << " has been terminated." << endl;
        }
    }
    
    void display(string viewerRole) const {
        cout << "ID: " << setw(4) << id 
             << " | Name: " << setw(15) << name
             << " | Dept: " << setw(12) << department;
        
        if (viewerRole == "Manager" || viewerRole == "HR") {
            cout << " | Salary: $" << setw(8) << fixed << setprecision(2) << salary;
        } else {
            cout << " | Salary: [Confidential]";
        }
        
        cout << " | Active: " << (active ? "Yes" : "No")
             << " | Hired: " << getHireDate() << endl;
    }
};

int Employee::nextId = 1000;

class Department {
private:
    string name;
    vector<Employee*> employees;
    double budget;
    
public:
    Department(string n, double b) : name(n), budget(b) {
        cout << "Department created: " << name << " (Budget: $" << budget << ")" << endl;
    }
    
    void addEmployee(Employee* emp) {
        employees.push_back(emp);
        cout << emp->getName() << " added to " << name << " department" << endl;
    }
    
    void displayAll(string viewerRole) const {
        cout << "\n=== " << name << " Department (" << employees.size() << " employees) ===" << endl;
        for (const auto& emp : employees) {
            emp->display(viewerRole);
        }
    }
    
    double getTotalSalary(string requesterRole) const {
        if (requesterRole != "Manager" && requesterRole != "HR") {
            return -1;
        }
        
        double total = 0;
        for (const auto& emp : employees) {
            total += emp->getSalary(requesterRole);
        }
        return total;
    }
};

int main() {
    cout << "=== Employee Management with Data Hiding ===" << endl;
    
    cout << "\n1. Creating employees:" << endl;
    Employee e1("Alice Johnson", "Engineering", 85000);
    Employee e2("Bob Smith", "Sales", 65000);
    Employee e3("Charlie Brown", "Marketing", 70000);
    
    cout << "\n2. Department management:" << endl;
    Department engineering("Engineering", 500000);
    Department sales("Sales", 300000);
    
    engineering.addEmployee(&e1);
    sales.addEmployee(&e2);
    sales.addEmployee(&e3);
    
    cout << "\n3. Viewing as Employee (restricted access):" << endl;
    engineering.displayAll("Employee");
    sales.displayAll("Employee");
    
    cout << "\n4. Viewing as Manager (full access):" << endl;
    engineering.displayAll("Manager");
    sales.displayAll("Manager");
    
    cout << "\n5. Unauthorized access attempts:" << endl;
    e1.getSalary("Employee");  // Returns -1, but doesn't print
    e1.setSalary(90000, "Employee");  // Unauthorized
    e1.giveRaise(10, "Employee");  // Unauthorized
    
    cout << "\n6. Authorized actions:" << endl;
    e1.setSalary(90000, "Manager");
    e2.giveRaise(15, "HR");
    e3.terminate("Manager");
    
    cout << "\n7. Final employee list (Manager view):" << endl;
    engineering.displayAll("Manager");
    sales.displayAll("Manager");
    
    cout << "\nTotal Engineering Salary: $" 
         << engineering.getTotalSalary("Manager") << endl;
    
    return 0;
}
```

---

## 📊 Data Hiding Summary

| Level | Access | Purpose |
|-------|--------|---------|
| **Private** | Class only | Implementation details, invariants |
| **Protected** | Class + Derived | Base class internals for inheritance |
| **Public** | Everyone | Interface, controlled access |

---

## ✅ Best Practices

1. **Make data members private** by default
2. **Provide controlled access** through public methods
3. **Validate input** in setters to maintain invariants
4. **Use const getters** for read-only access
5. **Return copies or const references** to prevent modification
6. **Hide helper functions** as private methods
7. **Never expose internal pointers** unless necessary

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Public data members** | No control over modifications | Make private, add getters/setters |
| **Returning non-const references** | Bypasses encapsulation | Return const reference or copy |
| **No validation in setters** | Invalid state possible | Validate all inputs |
| **Exposing implementation** | Harder to change | Hide implementation details |
| **Too many getters/setters** | Anemic objects | Add business logic methods |

---

## ✅ Key Takeaways

1. **Data hiding** protects internal state from unauthorized access
2. **Private members** are only accessible within the class
3. **Public interface** provides controlled access to data
4. **Validation** ensures object invariants are maintained
5. **Benefits**: Security, maintainability, flexibility
6. **Rule of thumb**: Make data private, provide meaningful public interface

---