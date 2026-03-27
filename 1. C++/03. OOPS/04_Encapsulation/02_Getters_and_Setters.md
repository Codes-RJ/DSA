# 04_Encapsulation/02_Getters_and_Setters.md

# Getters and Setters in C++ - Complete Guide

## 📖 Overview

Getters (accessors) and setters (mutators) are public methods that provide controlled access to private data members. They form the interface of a class, allowing external code to interact with an object's data while maintaining encapsulation. Getters allow reading data, while setters allow modifying data with validation.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Getter** | Public method that returns the value of a private data member |
| **Setter** | Public method that modifies the value of a private data member |
| **Accessor** | Another term for getter |
| **Mutator** | Another term for setter |
| **Validation** | Logic in setters to ensure data integrity |

---

## 1. **Basic Getters and Setters**

```cpp
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

class Student {
private:
    string name;
    int rollNumber;
    double marks;
    char grade;
    
public:
    // Constructor
    Student(string n, int r, double m) : name(n), rollNumber(r), marks(m) {
        calculateGrade();
    }
    
    // Getters (accessors)
    string getName() const { return name; }
    int getRollNumber() const { return rollNumber; }
    double getMarks() const { return marks; }
    char getGrade() const { return grade; }
    
    // Setters (mutators) with validation
    void setName(string n) {
        if (!n.empty()) {
            name = n;
        } else {
            cout << "Invalid name!" << endl;
        }
    }
    
    void setRollNumber(int r) {
        if (r > 0) {
            rollNumber = r;
        } else {
            cout << "Roll number must be positive!" << endl;
        }
    }
    
    void setMarks(double m) {
        if (m >= 0 && m <= 100) {
            marks = m;
            calculateGrade();  // Update grade when marks change
        } else {
            cout << "Marks must be between 0 and 100!" << endl;
        }
    }
    
    // Private helper to calculate grade
    void calculateGrade() {
        if (marks >= 90) grade = 'A';
        else if (marks >= 80) grade = 'B';
        else if (marks >= 70) grade = 'C';
        else if (marks >= 60) grade = 'D';
        else grade = 'F';
    }
    
    void display() const {
        cout << "Name: " << name << ", Roll: " << rollNumber
             << ", Marks: " << marks << ", Grade: " << grade << endl;
    }
};

int main() {
    cout << "=== Basic Getters and Setters ===" << endl;
    
    Student s1("Alice", 101, 85.5);
    s1.display();
    
    cout << "\nUsing getters:" << endl;
    cout << "Name: " << s1.getName() << endl;
    cout << "Roll Number: " << s1.getRollNumber() << endl;
    cout << "Marks: " << s1.getMarks() << endl;
    cout << "Grade: " << s1.getGrade() << endl;
    
    cout << "\nUsing setters:" << endl;
    s1.setName("Alicia");
    s1.setMarks(92.0);
    s1.setRollNumber(102);
    
    cout << "\nAfter modifications:" << endl;
    s1.display();
    
    cout << "\nInvalid attempts:" << endl;
    s1.setName("");        // Invalid
    s1.setMarks(150);      // Invalid
    s1.setRollNumber(-5);  // Invalid
    
    return 0;
}
```

**Output:**
```
=== Basic Getters and Setters ===
Name: Alice, Roll: 101, Marks: 85.5, Grade: B

Using getters:
Name: Alice
Roll Number: 101
Marks: 85.5
Grade: B

Using setters:

After modifications:
Name: Alicia, Roll: 102, Marks: 92, Grade: A

Invalid attempts:
Invalid name!
Marks must be between 0 and 100!
Roll number must be positive!
```

---

## 2. **Getter and Setter Variations**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Config {
private:
    string serverName;
    int port;
    bool debugMode;
    vector<string> allowedIPs;
    static int instanceCount;
    
public:
    Config() : serverName("localhost"), port(8080), debugMode(false) {
        instanceCount++;
    }
    
    // 1. Basic getter (by value)
    string getServerName() const { return serverName; }
    
    // 2. Getter returning const reference (avoids copying)
    const string& getServerNameRef() const { return serverName; }
    
    // 3. Getter returning reference (allows modification - careful!)
    string& getServerNameRefMod() { return serverName; }
    
    // 4. Getter with default value for missing data
    int getPort(int defaultPort = 8080) const {
        return (port > 0) ? port : defaultPort;
    }
    
    // 5. Getter for vector - return const reference
    const vector<string>& getAllowedIPs() const { return allowedIPs; }
    
    // 6. Getter returning copy (safe but expensive)
    vector<string> getAllowedIPsCopy() const { return allowedIPs; }
    
    // 7. Basic setter with validation
    void setServerName(const string& name) {
        if (!name.empty()) {
            serverName = name;
        }
    }
    
    // 8. Setter with range validation
    void setPort(int p) {
        if (p >= 1 && p <= 65535) {
            port = p;
        } else {
            cout << "Invalid port! Must be 1-65535" << endl;
        }
    }
    
    // 9. Setter with flag
    void setDebugMode(bool enabled) {
        debugMode = enabled;
        cout << "Debug mode " << (enabled ? "enabled" : "disabled") << endl;
    }
    
    // 10. Add to collection (not a simple setter)
    void addAllowedIP(const string& ip) {
        // Validate IP format (simplified)
        if (ip.find('.') != string::npos) {
            allowedIPs.push_back(ip);
        } else {
            cout << "Invalid IP format!" << endl;
        }
    }
    
    // 11. Remove from collection
    void removeAllowedIP(const string& ip) {
        for (auto it = allowedIPs.begin(); it != allowedIPs.end(); ++it) {
            if (*it == ip) {
                allowedIPs.erase(it);
                break;
            }
        }
    }
    
    // 12. Boolean getter (is/has prefix)
    bool isDebugMode() const { return debugMode; }
    
    // 13. Static getter
    static int getInstanceCount() { return instanceCount; }
    
    void display() const {
        cout << "Server: " << serverName << ":" << port << endl;
        cout << "Debug: " << (debugMode ? "ON" : "OFF") << endl;
        cout << "Allowed IPs: ";
        for (const auto& ip : allowedIPs) {
            cout << ip << " ";
        }
        cout << endl;
    }
};

int Config::instanceCount = 0;

int main() {
    cout << "=== Getter and Setter Variations ===" << endl;
    
    Config cfg;
    cfg.display();
    
    cout << "\n1. Basic getter (by value): " << cfg.getServerName() << endl;
    cout << "2. Getter returning const ref: " << cfg.getServerNameRef() << endl;
    
    cout << "\n3. Getter with default value: " << cfg.getPort(9090) << endl;
    
    cout << "\n4. Setting values:" << endl;
    cfg.setServerName("production.example.com");
    cfg.setPort(443);
    cfg.setDebugMode(true);
    cfg.addAllowedIP("192.168.1.1");
    cfg.addAllowedIP("10.0.0.1");
    
    cfg.display();
    
    cout << "\n5. Boolean getter (isDebugMode): " << cfg.isDebugMode() << endl;
    cout << "6. Static getter: " << Config::getInstanceCount() << endl;
    
    cout << "\n7. Const reference getter for vector:" << endl;
    const auto& ips = cfg.getAllowedIPs();
    for (const auto& ip : ips) {
        cout << "  " << ip << endl;
    }
    
    return 0;
}
```

---

## 3. **Getter/Setter with Computed Properties**

```cpp
#include <iostream>
#include <string>
#include <cmath>
#include <vector>
using namespace std;

class Circle {
private:
    double radius;
    
public:
    Circle(double r = 0) : radius(r) {}
    
    // Getter for radius
    double getRadius() const { return radius; }
    
    // Setter for radius
    void setRadius(double r) {
        if (r >= 0) {
            radius = r;
        }
    }
    
    // Computed properties (not stored, calculated on demand)
    double getDiameter() const {
        return 2 * radius;
    }
    
    double getCircumference() const {
        return 2 * M_PI * radius;
    }
    
    double getArea() const {
        return M_PI * radius * radius;
    }
    
    void display() const {
        cout << "Circle: radius=" << radius 
             << ", diameter=" << getDiameter()
             << ", circumference=" << getCircumference()
             << ", area=" << getArea() << endl;
    }
};

class Rectangle {
private:
    double width;
    double height;
    
public:
    Rectangle(double w = 0, double h = 0) : width(w), height(h) {}
    
    // Getters
    double getWidth() const { return width; }
    double getHeight() const { return height; }
    
    // Setters
    void setWidth(double w) {
        if (w >= 0) width = w;
    }
    
    void setHeight(double h) {
        if (h >= 0) height = h;
    }
    
    // Computed properties
    double getArea() const {
        return width * height;
    }
    
    double getPerimeter() const {
        return 2 * (width + height);
    }
    
    double getDiagonal() const {
        return sqrt(width * width + height * height);
    }
    
    bool isSquare() const {
        return width == height;
    }
    
    void display() const {
        cout << "Rectangle: " << width << " x " << height
             << ", area=" << getArea()
             << ", perimeter=" << getPerimeter()
             << ", diagonal=" << getDiagonal()
             << (isSquare() ? " (square)" : "") << endl;
    }
};

class BankAccount {
private:
    double balance;
    vector<double> transactions;
    
public:
    BankAccount(double initial = 0) : balance(initial) {
        if (initial > 0) transactions.push_back(initial);
    }
    
    // Simple getters
    double getBalance() const { return balance; }
    
    // Setter with business logic
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            transactions.push_back(amount);
        }
    }
    
    bool withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            transactions.push_back(-amount);
            return true;
        }
        return false;
    }
    
    // Computed properties
    double getTotalDeposits() const {
        double total = 0;
        for (double t : transactions) {
            if (t > 0) total += t;
        }
        return total;
    }
    
    double getTotalWithdrawals() const {
        double total = 0;
        for (double t : transactions) {
            if (t < 0) total += -t;
        }
        return total;
    }
    
    int getTransactionCount() const {
        return transactions.size();
    }
    
    double getAverageTransaction() const {
        if (transactions.empty()) return 0;
        double sum = 0;
        for (double t : transactions) {
            sum += (t > 0 ? t : -t);
        }
        return sum / transactions.size();
    }
    
    void display() const {
        cout << "Balance: $" << balance << endl;
        cout << "Total Deposits: $" << getTotalDeposits() << endl;
        cout << "Total Withdrawals: $" << getTotalWithdrawals() << endl;
        cout << "Transactions: " << getTransactionCount() << endl;
        cout << "Average Transaction: $" << getAverageTransaction() << endl;
    }
};

int main() {
    cout << "=== Getter/Setter with Computed Properties ===" << endl;
    
    cout << "\n1. Circle - computed from radius:" << endl;
    Circle c(5);
    c.display();
    c.setRadius(10);
    cout << "After setting radius to 10:" << endl;
    c.display();
    
    cout << "\n2. Rectangle - computed from dimensions:" << endl;
    Rectangle r(4, 6);
    r.display();
    r.setWidth(5);
    r.setHeight(5);
    cout << "After setting to 5x5:" << endl;
    r.display();
    
    cout << "\n3. BankAccount - computed from transactions:" << endl;
    BankAccount acc(1000);
    acc.deposit(500);
    acc.withdraw(200);
    acc.deposit(300);
    acc.withdraw(100);
    acc.display();
    
    return 0;
}
```

---

## 4. **Const Correctness in Getters**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class DataContainer {
private:
    vector<int> data;
    mutable int accessCount;  // mutable - can be modified in const methods
    string name;
    
public:
    DataContainer(string n) : name(n), accessCount(0) {}
    
    // Const getter - returns const reference
    const vector<int>& getData() const {
        accessCount++;  // OK - mutable member
        return data;
    }
    
    // Non-const getter - returns reference for modification
    vector<int>& getData() {
        return data;
    }
    
    // Const getter with copying
    vector<int> getDataCopy() const {
        accessCount++;
        return data;  // Returns a copy
    }
    
    // Const getter for name
    string getName() const {
        return name;
    }
    
    // Non-const setter
    void setName(const string& n) {
        name = n;
    }
    
    int getAccessCount() const {
        return accessCount;
    }
    
    void addData(int value) {
        data.push_back(value);
    }
};

class ReadOnlyWrapper {
private:
    const DataContainer& container;
    
public:
    ReadOnlyWrapper(const DataContainer& c) : container(c) {}
    
    // Only const methods available
    void display() const {
        cout << "Container: " << container.getName() << endl;
        cout << "Data: ";
        for (int val : container.getData()) {
            cout << val << " ";
        }
        cout << endl;
        cout << "Access count: " << container.getAccessCount() << endl;
    }
};

int main() {
    cout << "=== Const Correctness in Getters ===" << endl;
    
    DataContainer dc("MyData");
    dc.addData(10);
    dc.addData(20);
    dc.addData(30);
    
    cout << "\n1. Non-const access (can modify):" << endl;
    auto& dataRef = dc.getData();
    dataRef.push_back(40);  // Modifies original
    
    cout << "Data after modification: ";
    for (int val : dc.getData()) {
        cout << val << " ";
    }
    cout << endl;
    
    cout << "\n2. Const access (read-only):" << endl;
    const DataContainer& constRef = dc;
    const auto& constData = constRef.getData();
    // constData.push_back(50);  // Error! Can't modify const reference
    
    cout << "Const access data: ";
    for (int val : constData) {
        cout << val << " ";
    }
    cout << endl;
    
    cout << "\n3. Read-only wrapper:" << endl;
    ReadOnlyWrapper wrapper(dc);
    wrapper.display();
    
    cout << "\n4. Copy getter (doesn't affect original):" << endl;
    vector<int> copy = dc.getDataCopy();
    copy.push_back(100);
    cout << "Original after copy modification: ";
    for (int val : dc.getData()) {
        cout << val << " ";
    }
    cout << endl;
    
    cout << "Access count: " << dc.getAccessCount() << endl;
    
    return 0;
}
```

---

## 5. **Getter/Setter Design Patterns**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

// Pattern 1: Property with validation
class Temperature {
private:
    double celsius;
    
public:
    // Setter with unit conversion
    void setCelsius(double c) {
        if (c >= -273.15) {
            celsius = c;
        }
    }
    
    void setFahrenheit(double f) {
        setCelsius((f - 32) * 5.0 / 9.0);
    }
    
    // Getters with unit conversion
    double getCelsius() const { return celsius; }
    double getFahrenheit() const { return celsius * 9.0 / 5.0 + 32; }
};

// Pattern 2: Lazy initialization
class ExpensiveResource {
private:
    vector<int> data;
    mutable bool loaded;
    
    void load() const {
        if (!loaded) {
            cout << "Loading expensive resource..." << endl;
            // Simulate expensive operation
            for (int i = 0; i < 1000000; i++) {
                const_cast<vector<int>&>(data).push_back(i);
            }
            const_cast<bool&>(loaded) = true;
        }
    }
    
public:
    ExpensiveResource() : loaded(false) {}
    
    const vector<int>& getData() const {
        load();  // Lazy load on first access
        return data;
    }
};

// Pattern 3: Read-only property with private setter
class Person {
private:
    string name;
    int age;
    
public:
    Person(string n, int a) : name(n), age(a) {}
    
    // Read-only getter (no public setter)
    string getName() const { return name; }
    
    // Getter with derived value
    int getAge() const { return age; }
    
    // Business logic method (instead of direct setter)
    void haveBirthday() {
        age++;
        cout << name << " is now " << age << " years old!" << endl;
    }
};

// Pattern 4: Range validation
class Score {
private:
    int value;
    
public:
    void setValue(int v) {
        if (v >= 0 && v <= 100) {
            value = v;
        } else {
            throw out_of_range("Score must be between 0 and 100");
        }
    }
    
    int getValue() const { return value; }
};

// Pattern 5: Computed property with caching
class RectangleCache {
private:
    double width, height;
    mutable double cachedArea;
    mutable bool areaValid;
    
    void updateCache() const {
        if (!areaValid) {
            cachedArea = width * height;
            areaValid = true;
        }
    }
    
public:
    RectangleCache(double w, double h) : width(w), height(h), areaValid(false) {}
    
    void setWidth(double w) {
        width = w;
        areaValid = false;  // Invalidate cache
    }
    
    void setHeight(double h) {
        height = h;
        areaValid = false;  // Invalidate cache
    }
    
    double getArea() const {
        updateCache();  // Recalculate if needed
        return cachedArea;
    }
};

int main() {
    cout << "=== Getter/Setter Design Patterns ===" << endl;
    
    cout << "\n1. Property with unit conversion:" << endl;
    Temperature temp;
    temp.setCelsius(25);
    cout << "Celsius: " << temp.getCelsius() << endl;
    cout << "Fahrenheit: " << temp.getFahrenheit() << endl;
    temp.setFahrenheit(98.6);
    cout << "After setting 98.6°F: " << temp.getCelsius() << "°C" << endl;
    
    cout << "\n2. Lazy initialization:" << endl;
    ExpensiveResource res;
    cout << "Resource created, not loaded yet" << endl;
    cout << "First access: " << res.getData().size() << " elements" << endl;
    cout << "Second access: " << res.getData().size() << " elements (cached)" << endl;
    
    cout << "\n3. Read-only property:" << endl;
    Person p("Alice", 25);
    cout << "Name: " << p.getName() << endl;
    cout << "Age: " << p.getAge() << endl;
    p.haveBirthday();
    
    cout << "\n4. Range validation:" << endl;
    Score score;
    try {
        score.setValue(85);
        cout << "Score: " << score.getValue() << endl;
        score.setValue(150);  // Will throw
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    cout << "\n5. Cached computed property:" << endl;
    RectangleCache rc(10, 5);
    cout << "Area: " << rc.getArea() << endl;
    rc.setWidth(20);
    cout << "After changing width: " << rc.getArea() << endl;
    
    return 0;
}
```

---

## 6. **Practical Example: User Profile Management**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <regex>
#include <chrono>
#include <iomanip>
using namespace std;

class UserProfile {
private:
    string username;
    string email;
    string passwordHash;
    int age;
    vector<string> interests;
    chrono::system_clock::time_point createdAt;
    bool isActive;
    
    // Private helper methods
    string hashPassword(const string& password) {
        // Simplified hash simulation
        string hash;
        for (char c : password) {
            hash += to_string((int)c);
        }
        return hash;
    }
    
    bool validateEmail(const string& email) {
        regex emailRegex(R"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})");
        return regex_match(email, emailRegex);
    }
    
    bool validateAge(int a) {
        return a >= 13 && a <= 120;
    }
    
    bool validateUsername(const string& name) {
        regex usernameRegex(R"([a-zA-Z0-9_]{3,20})");
        return regex_match(name, usernameRegex);
    }
    
public:
    // Constructor
    UserProfile(string uname, string emailAddr, string pwd, int a) 
        : username(uname), email(emailAddr), age(a), isActive(true) {
        
        if (!validateUsername(uname)) {
            throw invalid_argument("Invalid username");
        }
        
        if (!validateEmail(emailAddr)) {
            throw invalid_argument("Invalid email");
        }
        
        if (!validateAge(a)) {
            throw invalid_argument("Invalid age");
        }
        
        passwordHash = hashPassword(pwd);
        createdAt = chrono::system_clock::now();
        cout << "User created: " << username << endl;
    }
    
    // Getters - read-only access
    string getUsername() const { return username; }
    string getEmail() const { return email; }
    int getAge() const { return age; }
    vector<string> getInterests() const { return interests; }
    bool isUserActive() const { return isActive; }
    
    string getCreatedDate() const {
        auto time = chrono::system_clock::to_time_t(createdAt);
        return ctime(&time);
    }
    
    // Setters with validation
    void setEmail(const string& newEmail) {
        if (validateEmail(newEmail)) {
            email = newEmail;
            cout << "Email updated to: " << email << endl;
        } else {
            cout << "Invalid email format!" << endl;
        }
    }
    
    void setAge(int newAge) {
        if (validateAge(newAge)) {
            age = newAge;
            cout << "Age updated to: " << age << endl;
        } else {
            cout << "Invalid age! Must be 13-120." << endl;
        }
    }
    
    // Business logic methods
    bool authenticate(const string& password) {
        return passwordHash == hashPassword(password);
    }
    
    void addInterest(const string& interest) {
        if (!interest.empty()) {
            interests.push_back(interest);
            cout << "Interest added: " << interest << endl;
        }
    }
    
    void removeInterest(const string& interest) {
        auto it = find(interests.begin(), interests.end(), interest);
        if (it != interests.end()) {
            interests.erase(it);
            cout << "Interest removed: " << interest << endl;
        }
    }
    
    void deactivate() {
        isActive = false;
        cout << "Account deactivated: " << username << endl;
    }
    
    void activate() {
        isActive = true;
        cout << "Account activated: " << username << endl;
    }
    
    void display() const {
        cout << "\n=== User Profile ===" << endl;
        cout << "Username: " << username << endl;
        cout << "Email: " << email << endl;
        cout << "Age: " << age << endl;
        cout << "Status: " << (isActive ? "Active" : "Inactive") << endl;
        cout << "Created: " << getCreatedDate();
        cout << "Interests: ";
        if (interests.empty()) {
            cout << "None" << endl;
        } else {
            for (const auto& i : interests) {
                cout << i << " ";
            }
            cout << endl;
        }
    }
};

class UserManager {
private:
    vector<UserProfile> users;
    
public:
    void registerUser(const string& username, const string& email, 
                      const string& password, int age) {
        try {
            users.emplace_back(username, email, password, age);
        } catch (const exception& e) {
            cout << "Registration failed: " << e.what() << endl;
        }
    }
    
    UserProfile* findUser(const string& username) {
        for (auto& user : users) {
            if (user.getUsername() == username) {
                return &user;
            }
        }
        return nullptr;
    }
    
    void displayAll() const {
        cout << "\n=== All Users (" << users.size() << ") ===" << endl;
        for (const auto& user : users) {
            user.display();
        }
    }
};

int main() {
    cout << "=== User Profile Management ===" << endl;
    
    UserManager manager;
    
    cout << "\n1. Registering users:" << endl;
    manager.registerUser("alice123", "alice@email.com", "pass123", 25);
    manager.registerUser("bob_dev", "bob@dev.com", "secure456", 30);
    manager.registerUser("invalid", "not-an-email", "pwd", 15);  // Will fail
    
    cout << "\n2. Finding and modifying user:" << endl;
    UserProfile* user = manager.findUser("alice123");
    if (user) {
        user->addInterest("Programming");
        user->addInterest("Reading");
        user->setEmail("alice_new@email.com");
        user->setAge(26);
        
        cout << "\nAuthentication test:" << endl;
        cout << "Correct password: " << (user->authenticate("pass123") ? "Success" : "Failed") << endl;
        cout << "Wrong password: " << (user->authenticate("wrong") ? "Success" : "Failed") << endl;
    }
    
    cout << "\n3. Removing interest:" << endl;
    if (user) {
        user->removeInterest("Reading");
    }
    
    cout << "\n4. Deactivating account:" << endl;
    if (user) {
        user->deactivate();
    }
    
    cout << "\n5. Displaying all users:" << endl;
    manager.displayAll();
    
    return 0;
}
```

---

## 📊 Getter/Setter Summary

| Type | Syntax | Use Case |
|------|--------|----------|
| **Basic Getter** | `Type getX() const` | Simple read access |
| **Const Reference Getter** | `const Type& getX() const` | Avoid copying large objects |
| **Reference Getter** | `Type& getX()` | Allow modification (use carefully) |
| **Copy Getter** | `Type getX() const` | Safe but expensive |
| **Boolean Getter** | `bool isX() const` | Boolean properties |
| **Computed Getter** | `Type getX() const` | Calculated from other data |
| **Basic Setter** | `void setX(Type value)` | Simple assignment |
| **Setter with Validation** | `void setX(Type value)` | Validate before assignment |
| **Setter with Logic** | `void setX(Type value)` | Trigger side effects |

---

## ✅ Best Practices

1. **Make getters `const`** - They shouldn't modify the object
2. **Return `const` references** for large objects to avoid copying
3. **Validate input** in setters to maintain invariants
4. **Use meaningful names** - `getX()` for simple getters, `isX()` for booleans
5. **Don't expose internal collections directly** - return const references or copies
6. **Consider computed properties** instead of storing derived data
7. **Use private setters** for read-only properties

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Returning non-const reference** | Bypasses encapsulation | Return const reference or value |
| **Setter without validation** | Invalid state possible | Always validate |
| **Getter returning internal pointer** | Can lead to dangling pointers | Return by value or const reference |
| **Exposing collections directly** | Outside code can modify | Return const reference or copy |
| **Too many getters/setters** | Anemic objects | Add business logic methods |

---

## ✅ Key Takeaways

1. **Getters** provide controlled read access to private data
2. **Setters** provide controlled write access with validation
3. **Const correctness** ensures getters don't modify objects
4. **Validation** in setters maintains object invariants
5. **Computed properties** can replace stored derived data
6. **Return const references** for large objects to avoid copying

---