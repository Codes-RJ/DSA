# Design Patterns Introduction in C++ - Complete Guide

## 📖 Overview

Design patterns are proven, reusable solutions to common software design problems. They represent best practices evolved over time by experienced developers. Understanding design patterns helps create more maintainable, flexible, and understandable code. Abstraction is a key principle underlying many design patterns.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Design Pattern** | Reusable solution to a common problem |
| **Creational Patterns** | Object creation mechanisms |
| **Structural Patterns** | Class and object composition |
| **Behavioral Patterns** | Object interaction and responsibility |
| **Abstraction Role** | Separates interface from implementation |

---

## 1. **Why Design Patterns?**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Without design patterns (tight coupling, difficult to extend)
class PaymentProcessor_NoPattern {
public:
    void processCreditCard(double amount) {
        cout << "Processing credit card payment: $" << amount << endl;
        // Complex credit card logic
    }
    
    void processPayPal(double amount) {
        cout << "Processing PayPal payment: $" << amount << endl;
        // Complex PayPal logic
    }
    
    void processBankTransfer(double amount) {
        cout << "Processing bank transfer: $" << amount << endl;
        // Complex bank transfer logic
    }
};

// With design pattern (Strategy Pattern - loose coupling, easy to extend)
class IPaymentStrategy {
public:
    virtual void process(double amount) = 0;
    virtual ~IPaymentStrategy() = default;
};

class CreditCardStrategy : public IPaymentStrategy {
public:
    void process(double amount) override {
        cout << "Processing credit card payment: $" << amount << endl;
    }
};

class PayPalStrategy : public IPaymentStrategy {
public:
    void process(double amount) override {
        cout << "Processing PayPal payment: $" << amount << endl;
    }
};

class BankTransferStrategy : public IPaymentStrategy {
public:
    void process(double amount) override {
        cout << "Processing bank transfer: $" << amount << endl;
    }
};

class PaymentProcessor {
private:
    unique_ptr<IPaymentStrategy> strategy;
    
public:
    void setStrategy(IPaymentStrategy* s) {
        strategy.reset(s);
    }
    
    void process(double amount) {
        if (strategy) {
            strategy->process(amount);
        } else {
            cout << "No payment strategy set!" << endl;
        }
    }
};

int main() {
    cout << "=== Why Design Patterns? ===" << endl;
    
    cout << "\nWithout patterns (bad):" << endl;
    PaymentProcessor_NoPattern proc;
    proc.processCreditCard(100);
    proc.processPayPal(50);
    // Adding new payment method requires modifying the class
    
    cout << "\nWith patterns (good):" << endl;
    PaymentProcessor processor;
    
    processor.setStrategy(new CreditCardStrategy());
    processor.process(100);
    
    processor.setStrategy(new PayPalStrategy());
    processor.process(50);
    
    processor.setStrategy(new BankTransferStrategy());
    processor.process(200);
    
    cout << "\nBenefits of design patterns:" << endl;
    cout << "  ✓ Open/Closed Principle - open for extension, closed for modification" << endl;
    cout << "  ✓ Loose coupling between components" << endl;
    cout << "  ✓ Easy to add new payment methods" << endl;
    cout << "  ✓ Code reuse and maintainability" << endl;
    
    return 0;
}
```

---

## 2. **Categories of Design Patterns**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <map>
using namespace std;

// ============ CREATIONAL PATTERN: Singleton ============
class Singleton {
private:
    static Singleton* instance;
    string data;
    
    Singleton() : data("Default") {}
    
public:
    static Singleton* getInstance() {
        if (!instance) {
            instance = new Singleton();
        }
        return instance;
    }
    
    void setData(const string& d) { data = d; }
    string getData() const { return data; }
};

Singleton* Singleton::instance = nullptr;

// ============ STRUCTURAL PATTERN: Adapter ============
// Existing class (incompatible interface)
class OldLogger {
public:
    void writeMessage(const string& msg) {
        cout << "[OLD] " << msg << endl;
    }
};

// Target interface
class ILogger {
public:
    virtual void log(const string& message) = 0;
    virtual ~ILogger() = default;
};

// Adapter
class LoggerAdapter : public ILogger {
private:
    OldLogger oldLogger;
    
public:
    void log(const string& message) override {
        oldLogger.writeMessage(message);
    }
};

// ============ BEHAVIORAL PATTERN: Observer ============
class IObserver {
public:
    virtual void update(const string& message) = 0;
    virtual ~IObserver() = default;
};

class Subject {
private:
    vector<IObserver*> observers;
    string state;
    
public:
    void attach(IObserver* observer) {
        observers.push_back(observer);
    }
    
    void detach(IObserver* observer) {
        // Remove observer (simplified)
    }
    
    void setState(const string& s) {
        state = s;
        notify();
    }
    
    void notify() {
        for (auto observer : observers) {
            observer->update(state);
        }
    }
};

class ConcreteObserver : public IObserver {
private:
    string name;
    
public:
    ConcreteObserver(string n) : name(n) {}
    
    void update(const string& message) override {
        cout << "Observer " << name << " received: " << message << endl;
    }
};

int main() {
    cout << "=== Categories of Design Patterns ===" << endl;
    
    cout << "\n1. CREATIONAL PATTERN - Singleton:" << endl;
    Singleton* s1 = Singleton::getInstance();
    Singleton* s2 = Singleton::getInstance();
    s1->setData("Singleton Data");
    cout << "s1 data: " << s1->getData() << endl;
    cout << "s2 data: " << s2->getData() << endl;
    cout << "Same instance? " << (s1 == s2 ? "Yes" : "No") << endl;
    
    cout << "\n2. STRUCTURAL PATTERN - Adapter:" << endl;
    ILogger* logger = new LoggerAdapter();
    logger->log("This message goes through adapter");
    delete logger;
    
    cout << "\n3. BEHAVIORAL PATTERN - Observer:" << endl;
    Subject subject;
    ConcreteObserver obs1("Observer1");
    ConcreteObserver obs2("Observer2");
    
    subject.attach(&obs1);
    subject.attach(&obs2);
    
    subject.setState("Event 1");
    subject.setState("Event 2");
    
    cout << "\nPattern Categories Summary:" << endl;
    cout << "  Creational:   Object creation (Singleton, Factory, Builder)" << endl;
    cout << "  Structural:   Class composition (Adapter, Decorator, Facade)" << endl;
    cout << "  Behavioral:   Object interaction (Observer, Strategy, Command)" << endl;
    
    return 0;
}
```

---

## 3. **Common Design Patterns**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <functional>
#include <map>
using namespace std;

// ============ STRATEGY PATTERN ============
class ISortStrategy {
public:
    virtual void sort(vector<int>& data) = 0;
    virtual ~ISortStrategy() = default;
};

class BubbleSort : public ISortStrategy {
public:
    void sort(vector<int>& data) override {
        cout << "Using Bubble Sort: ";
        // Bubble sort implementation
        for (size_t i = 0; i < data.size(); i++) {
            for (size_t j = 0; j < data.size() - i - 1; j++) {
                if (data[j] > data[j + 1]) {
                    swap(data[j], data[j + 1]);
                }
            }
        }
    }
};

class QuickSort : public ISortStrategy {
public:
    void sort(vector<int>& data) override {
        cout << "Using Quick Sort: ";
        // Quick sort implementation (simplified)
        sort(data, 0, data.size() - 1);
    }
    
private:
    void sort(vector<int>& data, int left, int right) {
        if (left < right) {
            int pivot = partition(data, left, right);
            sort(data, left, pivot - 1);
            sort(data, pivot + 1, right);
        }
    }
    
    int partition(vector<int>& data, int left, int right) {
        int pivot = data[right];
        int i = left - 1;
        for (int j = left; j < right; j++) {
            if (data[j] <= pivot) {
                i++;
                swap(data[i], data[j]);
            }
        }
        swap(data[i + 1], data[right]);
        return i + 1;
    }
};

class Sorter {
private:
    ISortStrategy* strategy;
    
public:
    Sorter(ISortStrategy* s) : strategy(s) {}
    
    void setStrategy(ISortStrategy* s) {
        strategy = s;
    }
    
    void sort(vector<int>& data) {
        strategy->sort(data);
        for (int val : data) {
            cout << val << " ";
        }
        cout << endl;
    }
};

// ============ FACTORY PATTERN ============
class IProduct {
public:
    virtual void use() = 0;
    virtual ~IProduct() = default;
};

class ProductA : public IProduct {
public:
    void use() override {
        cout << "Using Product A" << endl;
    }
};

class ProductB : public IProduct {
public:
    void use() override {
        cout << "Using Product B" << endl;
    }
};

class ProductC : public IProduct {
public:
    void use() override {
        cout << "Using Product C" << endl;
    }
};

class Factory {
public:
    static IProduct* createProduct(const string& type) {
        if (type == "A") return new ProductA();
        if (type == "B") return new ProductB();
        if (type == "C") return new ProductC();
        return nullptr;
    }
};

// ============ COMMAND PATTERN ============
class ICommand {
public:
    virtual void execute() = 0;
    virtual void undo() = 0;
    virtual ~ICommand() = default;
};

class Light {
public:
    void turnOn() { cout << "Light is ON" << endl; }
    void turnOff() { cout << "Light is OFF" << endl; }
};

class LightOnCommand : public ICommand {
private:
    Light& light;
    
public:
    LightOnCommand(Light& l) : light(l) {}
    
    void execute() override {
        light.turnOn();
    }
    
    void undo() override {
        light.turnOff();
    }
};

class LightOffCommand : public ICommand {
private:
    Light& light;
    
public:
    LightOffCommand(Light& l) : light(l) {}
    
    void execute() override {
        light.turnOff();
    }
    
    void undo() override {
        light.turnOn();
    }
};

class RemoteControl {
private:
    vector<ICommand*> history;
    
public:
    void executeCommand(ICommand* cmd) {
        cmd->execute();
        history.push_back(cmd);
    }
    
    void undo() {
        if (!history.empty()) {
            history.back()->undo();
            history.pop_back();
        }
    }
};

int main() {
    cout << "=== Common Design Patterns ===" << endl;
    
    cout << "\n1. Strategy Pattern:" << endl;
    vector<int> data = {5, 2, 8, 1, 9, 3};
    Sorter sorter(new BubbleSort());
    sorter.sort(data);
    
    data = {5, 2, 8, 1, 9, 3};
    sorter.setStrategy(new QuickSort());
    sorter.sort(data);
    
    cout << "\n2. Factory Pattern:" << endl;
    IProduct* p1 = Factory::createProduct("A");
    IProduct* p2 = Factory::createProduct("B");
    IProduct* p3 = Factory::createProduct("C");
    
    p1->use();
    p2->use();
    p3->use();
    
    delete p1;
    delete p2;
    delete p3;
    
    cout << "\n3. Command Pattern:" << endl;
    Light livingRoom;
    LightOnCommand onCmd(livingRoom);
    LightOffCommand offCmd(livingRoom);
    RemoteControl remote;
    
    remote.executeCommand(&onCmd);
    remote.executeCommand(&offCmd);
    remote.undo();
    
    return 0;
}
```

---

## 4. **Pattern Selection Guide**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

// Problem: Need to create objects with many optional parameters
// Solution: Builder Pattern
class Pizza {
private:
    string size;
    string crust;
    vector<string> toppings;
    bool cheese;
    bool sauce;
    
public:
    class Builder {
    private:
        Pizza pizza;
        
    public:
        Builder& setSize(const string& s) {
            pizza.size = s;
            return *this;
        }
        
        Builder& setCrust(const string& c) {
            pizza.crust = c;
            return *this;
        }
        
        Builder& addTopping(const string& t) {
            pizza.toppings.push_back(t);
            return *this;
        }
        
        Builder& addCheese() {
            pizza.cheese = true;
            return *this;
        }
        
        Builder& addSauce() {
            pizza.sauce = true;
            return *this;
        }
        
        Pizza build() {
            return pizza;
        }
    };
    
    void display() const {
        cout << "Pizza: " << size << " " << crust << " crust";
        if (cheese) cout << ", Extra cheese";
        if (sauce) cout << ", Extra sauce";
        if (!toppings.empty()) {
            cout << ", Toppings: ";
            for (const auto& t : toppings) cout << t << " ";
        }
        cout << endl;
    }
};

// Problem: Need to provide a simplified interface to a complex subsystem
// Solution: Facade Pattern
class CPU {
public:
    void start() { cout << "CPU starting" << endl; }
    void execute() { cout << "CPU executing" << endl; }
    void shutdown() { cout << "CPU shutting down" << endl; }
};

class Memory {
public:
    void load() { cout << "Memory loading" << endl; }
    void clear() { cout << "Memory clearing" << endl; }
};

class HardDrive {
public:
    void read() { cout << "HardDrive reading" << endl; }
    void write() { cout << "HardDrive writing" << endl; }
};

class ComputerFacade {
private:
    CPU cpu;
    Memory memory;
    HardDrive hardDrive;
    
public:
    void start() {
        cout << "\nStarting computer..." << endl;
        cpu.start();
        memory.load();
        hardDrive.read();
        cpu.execute();
        cout << "Computer ready" << endl;
    }
    
    void shutdown() {
        cout << "\nShutting down computer..." << endl;
        cpu.shutdown();
        memory.clear();
        hardDrive.write();
        cout << "Computer off" << endl;
    }
};

// Problem: Need to add responsibilities to objects dynamically
// Solution: Decorator Pattern
class ICoffee {
public:
    virtual string getDescription() const = 0;
    virtual double getCost() const = 0;
    virtual ~ICoffee() = default;
};

class SimpleCoffee : public ICoffee {
public:
    string getDescription() const override {
        return "Simple Coffee";
    }
    
    double getCost() const override {
        return 2.0;
    }
};

class MilkDecorator : public ICoffee {
private:
    ICoffee* coffee;
    
public:
    MilkDecorator(ICoffee* c) : coffee(c) {}
    
    string getDescription() const override {
        return coffee->getDescription() + ", Milk";
    }
    
    double getCost() const override {
        return coffee->getCost() + 0.5;
    }
};

class SugarDecorator : public ICoffee {
private:
    ICoffee* coffee;
    
public:
    SugarDecorator(ICoffee* c) : coffee(c) {}
    
    string getDescription() const override {
        return coffee->getDescription() + ", Sugar";
    }
    
    double getCost() const override {
        return coffee->getCost() + 0.2;
    }
};

int main() {
    cout << "=== Pattern Selection Guide ===" << endl;
    
    cout << "\n1. Builder Pattern (complex object creation):" << endl;
    Pizza pizza = Pizza::Builder()
        .setSize("Large")
        .setCrust("Thin")
        .addTopping("Pepperoni")
        .addTopping("Mushrooms")
        .addCheese()
        .build();
    pizza.display();
    
    cout << "\n2. Facade Pattern (simplify complex subsystem):" << endl;
    ComputerFacade computer;
    computer.start();
    computer.shutdown();
    
    cout << "\n3. Decorator Pattern (dynamic behavior addition):" << endl;
    ICoffee* coffee = new SimpleCoffee();
    cout << coffee->getDescription() << " $" << coffee->getCost() << endl;
    
    coffee = new MilkDecorator(coffee);
    cout << coffee->getDescription() << " $" << coffee->getCost() << endl;
    
    coffee = new SugarDecorator(coffee);
    cout << coffee->getDescription() << " $" << coffee->getCost() << endl;
    
    delete coffee;
    
    cout << "\nWhen to use which pattern?" << endl;
    cout << "  Builder:   Complex object creation with many parameters" << endl;
    cout << "  Facade:    Simplify complex subsystem interface" << endl;
    cout << "  Decorator: Add responsibilities dynamically" << endl;
    cout << "  Strategy:  Family of algorithms, interchangeable" << endl;
    cout << "  Observer:  One-to-many dependency notification" << endl;
    cout << "  Singleton: Ensure single instance of a class" << endl;
    
    return 0;
}
```

---

## 📊 Design Patterns Summary

| Category | Pattern | Purpose |
|----------|---------|---------|
| **Creational** | Singleton | Single instance |
| **Creational** | Factory | Object creation |
| **Creational** | Builder | Complex object construction |
| **Structural** | Adapter | Interface conversion |
| **Structural** | Decorator | Dynamic behavior addition |
| **Structural** | Facade | Simplified interface |
| **Behavioral** | Strategy | Interchangeable algorithms |
| **Behavioral** | Observer | Event notification |
| **Behavioral** | Command | Request encapsulation |

---

## ✅ Key Takeaways

1. **Design patterns** are reusable solutions to common problems
2. **Three categories**: Creational, Structural, Behavioral
3. **Abstraction** is key to many design patterns
4. **Patterns promote** loose coupling and high cohesion
5. **Learn patterns** by understanding problems they solve
6. **Don't force patterns** - use when appropriate

---