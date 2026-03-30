# Hierarchical Inheritance in C++ - Complete Guide

## 📖 Overview

Hierarchical inheritance occurs when multiple derived classes inherit from a single base class. This creates a tree-like structure where one base class serves as the parent for several specialized child classes. This is one of the most common and useful forms of inheritance.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Hierarchical Inheritance** | Multiple derived classes from one base class |
| **Base Class** | Common parent providing shared functionality |
| **Derived Classes** | Specialized children with unique features |
| **Code Reuse** | Base class code is reused across all derived classes |
| **Specialization** | Each derived class adds specific functionality |

---

## 1. **Basic Hierarchical Inheritance**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// Base class - common to all shapes
class Shape {
protected:
    string color;
    
public:
    Shape(string c) : color(c) {
        cout << "Shape constructor: " << color << endl;
    }
    
    virtual double area() const = 0;
    virtual double perimeter() const = 0;
    
    void setColor(string c) { color = c; }
    string getColor() const { return color; }
    
    virtual void display() const {
        cout << "Shape color: " << color << endl;
    }
    
    virtual ~Shape() {
        cout << "Shape destructor: " << color << endl;
    }
};

// Derived class 1 - Circle
class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(string c, double r) : Shape(c), radius(r) {
        cout << "  Circle constructor: radius=" << radius << endl;
    }
    
    double area() const override {
        return M_PI * radius * radius;
    }
    
    double perimeter() const override {
        return 2 * M_PI * radius;
    }
    
    void display() const override {
        Shape::display();
        cout << "  Circle: radius=" << radius 
             << ", area=" << area() 
             << ", circumference=" << perimeter() << endl;
    }
    
    ~Circle() override {
        cout << "  Circle destructor: radius=" << radius << endl;
    }
};

// Derived class 2 - Rectangle
class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(string c, double w, double h) : Shape(c), width(w), height(h) {
        cout << "  Rectangle constructor: " << width << "x" << height << endl;
    }
    
    double area() const override {
        return width * height;
    }
    
    double perimeter() const override {
        return 2 * (width + height);
    }
    
    void display() const override {
        Shape::display();
        cout << "  Rectangle: " << width << "x" << height 
             << ", area=" << area() 
             << ", perimeter=" << perimeter() << endl;
    }
    
    ~Rectangle() override {
        cout << "  Rectangle destructor: " << width << "x" << height << endl;
    }
};

// Derived class 3 - Triangle
class Triangle : public Shape {
private:
    double side1, side2, side3;
    
public:
    Triangle(string c, double s1, double s2, double s3) 
        : Shape(c), side1(s1), side2(s2), side3(s3) {
        cout << "  Triangle constructor: " << side1 << "," << side2 << "," << side3 << endl;
    }
    
    double area() const override {
        double s = (side1 + side2 + side3) / 2;
        return sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }
    
    double perimeter() const override {
        return side1 + side2 + side3;
    }
    
    void display() const override {
        Shape::display();
        cout << "  Triangle: sides=" << side1 << "," << side2 << "," << side3
             << ", area=" << area() 
             << ", perimeter=" << perimeter() << endl;
    }
    
    ~Triangle() override {
        cout << "  Triangle destructor" << endl;
    }
};

int main() {
    cout << "=== Hierarchical Inheritance Demo ===" << endl;
    
    cout << "\nCreating shapes:" << endl;
    Circle circle("Red", 5.0);
    Rectangle rect("Blue", 4.0, 6.0);
    Triangle triangle("Green", 3.0, 4.0, 5.0);
    
    cout << "\n=== Displaying Shapes ===" << endl;
    circle.display();
    cout << endl;
    rect.display();
    cout << endl;
    triangle.display();
    
    cout << "\n=== Polymorphic Behavior ===" << endl;
    Shape* shapes[] = {&circle, &rect, &triangle};
    
    for (auto shape : shapes) {
        cout << "Area: " << shape->area() 
             << ", Perimeter: " << shape->perimeter() << endl;
    }
    
    return 0;
}
```

**Output:**
```
=== Hierarchical Inheritance Demo ===

Creating shapes:
Shape constructor: Red
  Circle constructor: radius=5
Shape constructor: Blue
  Rectangle constructor: 4x6
Shape constructor: Green
  Triangle constructor: 3,4,5

=== Displaying Shapes ===
Shape color: Red
  Circle: radius=5, area=78.5398, circumference=31.4159

Shape color: Blue
  Rectangle: 4x6, area=24, perimeter=20

Shape color: Green
  Triangle: sides=3,4,5, area=6, perimeter=12

=== Polymorphic Behavior ===
Area: 78.5398, Perimeter: 31.4159
Area: 24, Perimeter: 20
Area: 6, Perimeter: 12
Shape destructor: Green
  Triangle destructor
Shape destructor: Blue
  Rectangle destructor: 4x6
Shape destructor: Red
  Circle destructor: radius=5
```

---

## 2. **Common Base Class Features**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Base class with common functionality
class Logger {
protected:
    string name;
    static int totalLogs;
    
public:
    Logger(string n) : name(n) {
        totalLogs++;
        cout << "Logger created: " << name << " (Total: " << totalLogs << ")" << endl;
    }
    
    virtual void log(const string& message) {
        cout << "[" << name << "] " << message << endl;
    }
    
    virtual void error(const string& message) {
        cout << "[" << name << "] ERROR: " << message << endl;
    }
    
    static int getTotalLogs() { return totalLogs; }
    
    virtual ~Logger() {
        totalLogs--;
        cout << "Logger destroyed: " << name << " (Remaining: " << totalLogs << ")" << endl;
    }
};

int Logger::totalLogs = 0;

// File logger
class FileLogger : public Logger {
private:
    string filename;
    
public:
    FileLogger(string n, string file) : Logger(n), filename(file) {
        cout << "  FileLogger: writing to " << filename << endl;
    }
    
    void log(const string& message) override {
        cout << "[" << name << "] Writing to file " << filename << ": " << message << endl;
    }
    
    void error(const string& message) override {
        cout << "[" << name << "] ERROR in file " << filename << ": " << message << endl;
    }
};

// Console logger
class ConsoleLogger : public Logger {
private:
    string color;
    
public:
    ConsoleLogger(string n, string c) : Logger(n), color(c) {
        cout << "  ConsoleLogger: color=" << color << endl;
    }
    
    void log(const string& message) override {
        cout << "[" << color << "][" << name << "] " << message << " [RESET]" << endl;
    }
    
    void error(const string& message) override {
        cout << "[RED][" << name << "] ERROR: " << message << " [RESET]" << endl;
    }
};

// Database logger
class DatabaseLogger : public Logger {
private:
    string connectionString;
    bool connected;
    
public:
    DatabaseLogger(string n, string conn) : Logger(n), connectionString(conn), connected(false) {
        cout << "  DatabaseLogger: connecting to " << connectionString << endl;
        connected = true;
    }
    
    void log(const string& message) override {
        if (connected) {
            cout << "[" << name << "] DB INSERT: " << message << endl;
        }
    }
    
    void error(const string& message) override {
        if (connected) {
            cout << "[" << name << "] DB ERROR: " << message << endl;
        }
    }
    
    ~DatabaseLogger() {
        cout << "  DatabaseLogger: disconnecting from " << connectionString << endl;
    }
};

int main() {
    cout << "=== Common Base Class Features ===" << endl;
    
    cout << "\n1. Creating loggers:" << endl;
    FileLogger fileLog("FileLog", "app.log");
    ConsoleLogger consoleLog("Console", "GREEN");
    DatabaseLogger dbLog("DBLog", "postgresql://localhost/logs");
    
    cout << "\n2. Using loggers:" << endl;
    fileLog.log("Application started");
    consoleLog.log("User logged in");
    dbLog.log("Transaction completed");
    
    cout << "\n3. Error logging:" << endl;
    fileLog.error("File not found");
    consoleLog.error("Invalid input");
    dbLog.error("Connection timeout");
    
    cout << "\n4. Total loggers created: " << Logger::getTotalLogs() << endl;
    
    cout << "\n5. Polymorphic container:" << endl;
    vector<Logger*> loggers = {&fileLog, &consoleLog, &dbLog};
    for (auto logger : loggers) {
        logger->log("Test message");
    }
    
    return 0;
}
```

---

## 3. **Specialization with Additional Features**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Base class: Employee
class Employee {
protected:
    string name;
    int id;
    double baseSalary;
    static int nextId;
    
public:
    Employee(string n, double salary) : name(n), baseSalary(salary) {
        id = nextId++;
        cout << "Employee created: " << name << " (ID: " << id << ")" << endl;
    }
    
    virtual double calculateSalary() const {
        return baseSalary;
    }
    
    virtual void work() const {
        cout << name << " is working" << endl;
    }
    
    virtual void display() const {
        cout << "ID: " << id << ", Name: " << name 
             << ", Base Salary: $" << baseSalary << endl;
    }
    
    virtual ~Employee() {
        cout << "Employee destroyed: " << name << endl;
    }
};

int Employee::nextId = 1000;

// Developer - specialization
class Developer : public Employee {
private:
    string programmingLanguage;
    vector<string> skills;
    
public:
    Developer(string n, double salary, string lang) 
        : Employee(n, salary), programmingLanguage(lang) {
        cout << "  Developer: " << lang << " programmer" << endl;
    }
    
    void addSkill(const string& skill) {
        skills.push_back(skill);
        cout << name << " learned " << skill << endl;
    }
    
    double calculateSalary() const override {
        // Developers get bonus based on skills
        return baseSalary + (skills.size() * 2000);
    }
    
    void work() const override {
        cout << name << " is writing " << programmingLanguage << " code" << endl;
    }
    
    void display() const override {
        Employee::display();
        cout << "  Language: " << programmingLanguage << endl;
        cout << "  Skills: ";
        for (const auto& s : skills) cout << s << " ";
        cout << endl;
    }
};

// Manager - specialization
class Manager : public Employee {
private:
    int teamSize;
    vector<string> teamMembers;
    double bonus;
    
public:
    Manager(string n, double salary, int size) 
        : Employee(n, salary), teamSize(size), bonus(0) {
        cout << "  Manager: leading " << teamSize << " people" << endl;
    }
    
    void addTeamMember(const string& member) {
        teamMembers.push_back(member);
        cout << member << " joined " << name << "'s team" << endl;
    }
    
    void setBonus(double b) {
        bonus = b;
        cout << name << " received bonus of $" << bonus << endl;
    }
    
    double calculateSalary() const override {
        return baseSalary + bonus;
    }
    
    void work() const override {
        cout << name << " is managing a team of " << teamSize << " people" << endl;
    }
    
    void display() const override {
        Employee::display();
        cout << "  Team Size: " << teamSize << ", Bonus: $" << bonus << endl;
        if (!teamMembers.empty()) {
            cout << "  Team Members: ";
            for (const auto& m : teamMembers) cout << m << " ";
            cout << endl;
        }
    }
};

// Intern - specialization
class Intern : public Employee {
private:
    int hoursWorked;
    double hourlyRate;
    string mentor;
    
public:
    Intern(string n, double rate, string mentor) 
        : Employee(n, 0), hourlyRate(rate), mentor(mentor), hoursWorked(0) {
        cout << "  Intern: mentored by " << mentor << endl;
    }
    
    void addHours(int hours) {
        hoursWorked += hours;
        cout << name << " worked " << hours << " more hours" << endl;
    }
    
    double calculateSalary() const override {
        return hoursWorked * hourlyRate;
    }
    
    void work() const override {
        cout << name << " is learning from " << mentor << endl;
    }
    
    void display() const override {
        cout << "ID: " << id << ", Name: " << name 
             << ", Hours: " << hoursWorked 
             << ", Rate: $" << hourlyRate
             << ", Mentor: " << mentor
             << ", Total: $" << calculateSalary() << endl;
    }
};

int main() {
    cout << "=== Hierarchical Inheritance with Specialization ===" << endl;
    
    cout << "\n1. Creating employees:" << endl;
    Developer dev("Alice", 70000, "C++");
    Manager mgr("Bob", 90000, 5);
    Intern intern("Charlie", 20, "Alice");
    
    cout << "\n2. Adding specializations:" << endl;
    dev.addSkill("Python");
    dev.addSkill("SQL");
    dev.addSkill("JavaScript");
    
    mgr.addTeamMember("Alice");
    mgr.addTeamMember("David");
    mgr.setBonus(10000);
    
    intern.addHours(40);
    intern.addHours(35);
    
    cout << "\n3. Working behaviors:" << endl;
    dev.work();
    mgr.work();
    intern.work();
    
    cout << "\n4. Salary calculations:" << endl;
    cout << "Developer salary: $" << dev.calculateSalary() << endl;
    cout << "Manager salary: $" << mgr.calculateSalary() << endl;
    cout << "Intern salary: $" << intern.calculateSalary() << endl;
    
    cout << "\n5. Displaying all employees:" << endl;
    dev.display();
    cout << endl;
    mgr.display();
    cout << endl;
    intern.display();
    
    return 0;
}
```

---

## 4. **Virtual Functions in Hierarchical Inheritance**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Payment {
protected:
    double amount;
    string currency;
    
public:
    Payment(double amt, string curr) : amount(amt), currency(curr) {}
    
    virtual void process() {
        cout << "Processing payment of " << amount << " " << currency << endl;
    }
    
    virtual double calculateFee() const {
        return amount * 0.02;  // 2% base fee
    }
    
    virtual void display() const {
        cout << "Payment: " << amount << " " << currency 
             << ", Fee: " << calculateFee() << endl;
    }
    
    virtual ~Payment() {}
};

class CreditCardPayment : public Payment {
private:
    string cardNumber;
    string cardHolder;
    string expiryDate;
    
public:
    CreditCardPayment(double amt, string curr, string card, string holder, string expiry)
        : Payment(amt, curr), cardNumber(card), cardHolder(holder), expiryDate(expiry) {}
    
    void process() override {
        cout << "Processing credit card payment for " << cardHolder << endl;
        cout << "  Card: ****" << cardNumber.substr(cardNumber.length() - 4) << endl;
        cout << "  Amount: " << amount << " " << currency << endl;
    }
    
    double calculateFee() const override {
        return amount * 0.03;  // 3% credit card fee
    }
    
    void display() const override {
        Payment::display();
        cout << "  Card: ****" << cardNumber.substr(cardNumber.length() - 4)
             << ", Holder: " << cardHolder << endl;
    }
};

class PayPalPayment : public Payment {
private:
    string email;
    string transactionId;
    
public:
    PayPalPayment(double amt, string curr, string em)
        : Payment(amt, curr), email(em), transactionId("") {}
    
    void process() override {
        transactionId = "PP-" + to_string(rand() % 10000);
        cout << "Processing PayPal payment for " << email << endl;
        cout << "  Transaction ID: " << transactionId << endl;
        cout << "  Amount: " << amount << " " << currency << endl;
    }
    
    double calculateFee() const override {
        return amount * 0.025;  // 2.5% PayPal fee
    }
    
    void display() const override {
        Payment::display();
        cout << "  Email: " << email << ", Transaction: " << transactionId << endl;
    }
};

class BankTransferPayment : public Payment {
private:
    string accountNumber;
    string bankCode;
    string reference;
    
public:
    BankTransferPayment(double amt, string curr, string account, string bank)
        : Payment(amt, curr), accountNumber(account), bankCode(bank), reference("") {}
    
    void process() override {
        reference = "REF-" + to_string(rand() % 10000);
        cout << "Processing bank transfer to account " << accountNumber << endl;
        cout << "  Bank: " << bankCode << ", Reference: " << reference << endl;
        cout << "  Amount: " << amount << " " << currency << endl;
    }
    
    double calculateFee() const override {
        return 5.0;  // Flat fee for bank transfers
    }
    
    void display() const override {
        Payment::display();
        cout << "  Account: ****" << accountNumber.substr(accountNumber.length() - 4)
             << ", Bank: " << bankCode << endl;
    }
};

int main() {
    cout << "=== Virtual Functions in Hierarchical Inheritance ===" << endl;
    
    cout << "\n1. Creating payments:" << endl;
    CreditCardPayment cc(100.0, "USD", "4111111111111111", "John Doe", "12/25");
    PayPalPayment pp(75.50, "EUR", "john@example.com");
    BankTransferPayment bt(500.0, "GBP", "12345678", "BANK123");
    
    cout << "\n2. Processing payments:" << endl;
    cc.process();
    cout << endl;
    pp.process();
    cout << endl;
    bt.process();
    
    cout << "\n3. Fee calculations:" << endl;
    cout << "Credit Card fee: $" << cc.calculateFee() << endl;
    cout << "PayPal fee: $" << pp.calculateFee() << endl;
    cout << "Bank Transfer fee: $" << bt.calculateFee() << endl;
    
    cout << "\n4. Polymorphic container:" << endl;
    vector<Payment*> payments = {&cc, &pp, &bt};
    
    for (auto payment : payments) {
        payment->display();
        payment->process();
        cout << endl;
    }
    
    return 0;
}
```

---

## 5. **Practical Example: Notification System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <chrono>
#include <ctime>
using namespace std;

// Base class: Notification
class Notification {
protected:
    string recipient;
    string message;
    time_t timestamp;
    
public:
    Notification(string to, string msg) 
        : recipient(to), message(msg) {
        timestamp = time(nullptr);
        cout << "Notification created for: " << recipient << endl;
    }
    
    virtual void send() = 0;
    virtual string getType() const = 0;
    
    void display() const {
        cout << "Type: " << getType() << endl;
        cout << "To: " << recipient << endl;
        cout << "Message: " << message << endl;
        cout << "Time: " << ctime(&timestamp);
    }
    
    virtual ~Notification() {}
};

// Email notification
class EmailNotification : public Notification {
private:
    string subject;
    string from;
    bool isHTML;
    
public:
    EmailNotification(string to, string subj, string msg, string fromAddr, bool html = false)
        : Notification(to, msg), subject(subj), from(fromAddr), isHTML(html) {}
    
    void send() override {
        cout << "\n[Sending Email]" << endl;
        cout << "From: " << from << endl;
        cout << "To: " << recipient << endl;
        cout << "Subject: " << subject << endl;
        cout << "Format: " << (isHTML ? "HTML" : "Plain Text") << endl;
        cout << "Body: " << message << endl;
        cout << "Email sent successfully!" << endl;
    }
    
    string getType() const override {
        return "Email";
    }
};

// SMS notification
class SMSNotification : public Notification {
private:
    string phoneNumber;
    string carrier;
    
public:
    SMSNotification(string number, string msg, string carrierName)
        : Notification(number, msg), phoneNumber(number), carrier(carrierName) {}
    
    void send() override {
        cout << "\n[Sending SMS]" << endl;
        cout << "To: " << phoneNumber << " (" << carrier << ")" << endl;
        cout << "Message: " << message << endl;
        cout << "SMS sent successfully!" << endl;
    }
    
    string getType() const override {
        return "SMS";
    }
};

// Push notification
class PushNotification : public Notification {
private:
    string deviceId;
    string appName;
    int priority;
    
public:
    PushNotification(string device, string app, string msg, int prio = 1)
        : Notification(device, msg), deviceId(device), appName(app), priority(prio) {}
    
    void send() override {
        cout << "\n[Sending Push Notification]" << endl;
        cout << "App: " << appName << endl;
        cout << "Device: " << deviceId << endl;
        cout << "Priority: " << priority << endl;
        cout << "Message: " << message << endl;
        cout << "Push notification sent!" << endl;
    }
    
    string getType() const override {
        return "Push";
    }
};

// Slack notification
class SlackNotification : public Notification {
private:
    string channel;
    string webhookUrl;
    bool mentionUser;
    
public:
    SlackNotification(string channel, string webhook, string msg, bool mention = false)
        : Notification(channel, msg), channel(channel), webhookUrl(webhook), mentionUser(mention) {}
    
    void send() override {
        cout << "\n[Sending Slack Message]" << endl;
        cout << "Channel: #" << channel << endl;
        cout << "Webhook: " << webhookUrl << endl;
        cout << "Mention: " << (mentionUser ? "Yes" : "No") << endl;
        cout << "Message: " << message << endl;
        cout << "Slack message sent!" << endl;
    }
    
    string getType() const override {
        return "Slack";
    }
};

class NotificationService {
private:
    vector<Notification*> notifications;
    
public:
    void addNotification(Notification* n) {
        notifications.push_back(n);
    }
    
    void sendAll() {
        cout << "\n=== Sending All Notifications ===" << endl;
        for (auto n : notifications) {
            n->send();
        }
    }
    
    void displayAll() {
        cout << "\n=== All Notifications ===" << endl;
        for (auto n : notifications) {
            n->display();
            cout << endl;
        }
    }
    
    ~NotificationService() {
        for (auto n : notifications) {
            delete n;
        }
    }
};

int main() {
    cout << "=== Notification System - Hierarchical Inheritance ===" << endl;
    
    NotificationService service;
    
    cout << "\n1. Creating notifications:" << endl;
    service.addNotification(new EmailNotification("user@example.com", "Welcome!", 
        "Thank you for joining!", "noreply@company.com", false));
    
    service.addNotification(new SMSNotification("+1234567890", 
        "Your verification code is 123456", "AT&T"));
    
    service.addNotification(new PushNotification("device_123", "MyApp",
        "You have a new message!", 2));
    
    service.addNotification(new SlackNotification("general", 
        "https://hooks.slack.com/xxx", "New deployment completed", true));
    
    cout << "\n2. Displaying notifications:" << endl;
    service.displayAll();
    
    cout << "\n3. Sending notifications:" << endl;
    service.sendAll();
    
    return 0;
}
```

---

## 📊 Hierarchical Inheritance Summary

| Aspect | Description |
|--------|-------------|
| **Structure** | One base class, multiple derived classes |
| **Code Reuse** | Base class code shared across all derived classes |
| **Specialization** | Each derived class adds unique features |
| **Polymorphism** | Base class pointers can refer to any derived object |
| **Use Case** | Multiple specialized types sharing common functionality |

---

## ✅ Best Practices

1. **Identify common functionality** in base class
2. **Keep base class focused** on shared features
3. **Use pure virtual functions** for abstract base classes
4. **Add specialized features** only in derived classes
5. **Use virtual destructors** for proper cleanup
6. **Consider interface segregation** when derived classes need different subsets

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Bloated base class** | Too many features not needed by all | Split into multiple base classes |
| **Incomplete abstraction** | Derived classes override everything | Add pure virtual functions |
| **Missing virtual destructor** | Memory leaks | Always make base destructor virtual |
| **Code duplication** | Similar code in multiple derived | Move common code to base class |

---

## ✅ Key Takeaways

1. **Hierarchical inheritance** creates a tree structure
2. **Base class** provides common functionality
3. **Derived classes** add specialized features
4. **Code reuse** is maximized through shared base
5. **Polymorphism** works seamlessly across all derived types
6. **Common use cases**: shapes, employees, notifications, payments

---