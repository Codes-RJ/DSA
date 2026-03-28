I'll now start with the **Design Patterns** section. Let me begin with the theory file.

---

# 12_Design_Patterns/Theory.md

# Design Patterns in C++ - Complete Guide

## 📖 Overview

Design patterns are proven, reusable solutions to common software design problems. They represent best practices evolved over time by experienced developers. Design patterns help create more maintainable, flexible, and understandable code by providing a common vocabulary for discussing design solutions.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Design Pattern** | Reusable solution to a recurring problem |
| **Creational Patterns** | Object creation mechanisms |
| **Structural Patterns** | Class and object composition |
| **Behavioral Patterns** | Object interaction and responsibility |
| **Gang of Four (GoF)** | Authors of the seminal book on design patterns |

---

## 📊 Categories of Design Patterns

| Category | Purpose | Examples |
|----------|---------|----------|
| **Creational** | Object creation | Singleton, Factory, Builder, Prototype |
| **Structural** | Class composition | Adapter, Decorator, Facade, Proxy |
| **Behavioral** | Object interaction | Observer, Strategy, Command, State |

---

## 1. **Why Design Patterns?**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Without design patterns (tight coupling, difficult to extend)
class PaymentProcessor_Bad {
public:
    void processCreditCard(double amount) {
        cout << "Processing credit card: $" << amount << endl;
    }
    
    void processPayPal(double amount) {
        cout << "Processing PayPal: $" << amount << endl;
    }
    
    void processBankTransfer(double amount) {
        cout << "Processing bank transfer: $" << amount << endl;
    }
    
    // Adding new payment method requires modifying this class!
};

// With design patterns (Strategy Pattern - loose coupling)
class IPaymentStrategy {
public:
    virtual void process(double amount) = 0;
    virtual ~IPaymentStrategy() = default;
};

class CreditCardStrategy : public IPaymentStrategy {
public:
    void process(double amount) override {
        cout << "Processing credit card: $" << amount << endl;
    }
};

class PayPalStrategy : public IPaymentStrategy {
public:
    void process(double amount) override {
        cout << "Processing PayPal: $" << amount << endl;
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
    
    cout << "\n1. Without patterns (bad):" << endl;
    PaymentProcessor_Bad bad;
    bad.processCreditCard(100);
    bad.processPayPal(50);
    // Adding new method requires modifying class
    
    cout << "\n2. With patterns (good):" << endl;
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

## 2. **Creational Patterns Overview**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// ============ SINGLETON PATTERN ============
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
    
    static void destroy() {
        delete instance;
        instance = nullptr;
    }
};

Singleton* Singleton::instance = nullptr;

// ============ FACTORY PATTERN ============
class IProduct {
public:
    virtual void use() = 0;
    virtual ~IProduct() = default;
};

class ProductA : public IProduct {
public:
    void use() override { cout << "Using Product A" << endl; }
};

class ProductB : public IProduct {
public:
    void use() override { cout << "Using Product B" << endl; }
};

class SimpleFactory {
public:
    static IProduct* createProduct(const string& type) {
        if (type == "A") return new ProductA();
        if (type == "B") return new ProductB();
        return nullptr;
    }
};

// ============ BUILDER PATTERN ============
class Pizza {
private:
    string size;
    string crust;
    vector<string> toppings;
    bool cheese;
    
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
        
        Pizza build() { return pizza; }
    };
    
    void display() const {
        cout << "Pizza: " << size << " " << crust << " crust";
        if (cheese) cout << ", Extra cheese";
        if (!toppings.empty()) {
            cout << ", Toppings: ";
            for (const auto& t : toppings) cout << t << " ";
        }
        cout << endl;
    }
};

int main() {
    cout << "=== Creational Patterns Overview ===" << endl;
    
    cout << "\n1. Singleton Pattern:" << endl;
    Singleton* s1 = Singleton::getInstance();
    Singleton* s2 = Singleton::getInstance();
    s1->setData("Singleton Data");
    cout << "s1 data: " << s1->getData() << endl;
    cout << "s2 data: " << s2->getData() << endl;
    cout << "Same instance? " << (s1 == s2 ? "Yes" : "No") << endl;
    Singleton::destroy();
    
    cout << "\n2. Factory Pattern:" << endl;
    IProduct* p1 = SimpleFactory::createProduct("A");
    IProduct* p2 = SimpleFactory::createProduct("B");
    p1->use();
    p2->use();
    delete p1;
    delete p2;
    
    cout << "\n3. Builder Pattern:" << endl;
    Pizza pizza = Pizza::Builder()
        .setSize("Large")
        .setCrust("Thin")
        .addTopping("Pepperoni")
        .addTopping("Mushrooms")
        .addCheese()
        .build();
    pizza.display();
    
    return 0;
}
```

---

## 3. **Structural Patterns Overview**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// ============ ADAPTER PATTERN ============
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

// ============ DECORATOR PATTERN ============
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

// ============ FACADE PATTERN ============
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

int main() {
    cout << "=== Structural Patterns Overview ===" << endl;
    
    cout << "\n1. Adapter Pattern:" << endl;
    ILogger* logger = new LoggerAdapter();
    logger->log("Message through adapter");
    delete logger;
    
    cout << "\n2. Decorator Pattern:" << endl;
    ICoffee* coffee = new SimpleCoffee();
    cout << coffee->getDescription() << " $" << coffee->getCost() << endl;
    
    coffee = new MilkDecorator(coffee);
    cout << coffee->getDescription() << " $" << coffee->getCost() << endl;
    
    delete coffee;
    
    cout << "\n3. Facade Pattern:" << endl;
    ComputerFacade computer;
    computer.start();
    computer.shutdown();
    
    return 0;
}
```

---

## 4. **Behavioral Patterns Overview**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// ============ OBSERVER PATTERN ============
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
    unique_ptr<ISortStrategy> strategy;
    
public:
    void setStrategy(ISortStrategy* s) {
        strategy.reset(s);
    }
    
    void sort(vector<int>& data) {
        if (strategy) {
            strategy->sort(data);
            for (int val : data) cout << val << " ";
            cout << endl;
        }
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
    cout << "=== Behavioral Patterns Overview ===" << endl;
    
    cout << "\n1. Observer Pattern:" << endl;
    Subject subject;
    ConcreteObserver obs1("Observer1");
    ConcreteObserver obs2("Observer2");
    
    subject.attach(&obs1);
    subject.attach(&obs2);
    subject.setState("Event 1");
    subject.setState("Event 2");
    
    cout << "\n2. Strategy Pattern:" << endl;
    vector<int> data = {5, 2, 8, 1, 9, 3};
    Sorter sorter;
    
    sorter.setStrategy(new BubbleSort());
    sorter.sort(data);
    
    data = {5, 2, 8, 1, 9, 3};
    sorter.setStrategy(new QuickSort());
    sorter.sort(data);
    
    cout << "\n3. Command Pattern:" << endl;
    Light livingRoom;
    LightOnCommand onCmd(livingRoom);
    RemoteControl remote;
    
    remote.executeCommand(&onCmd);
    remote.undo();
    
    return 0;
}
```

---

## 📊 Design Pattern Categories Summary

| Category | Purpose | Common Patterns |
|----------|---------|-----------------|
| **Creational** | Object creation | Singleton, Factory, Builder, Prototype |
| **Structural** | Class composition | Adapter, Decorator, Facade, Proxy |
| **Behavioral** | Object interaction | Observer, Strategy, Command, State |

---

## ✅ Best Practices

1. **Understand the problem** before applying a pattern
2. **Don't force patterns** - use only when appropriate
3. **Prefer composition** over inheritance when possible
4. **Keep patterns simple** - don't over-engineer
5. **Document pattern usage** for maintainability
6. **Learn from examples** and adapt to your needs

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Overusing patterns** | Unnecessary complexity | Use only when needed |
| **Wrong pattern** | Doesn't solve problem | Understand problem first |
| **Pattern obsession** | Over-engineering | Keep it simple |
| **Ignoring language features** | Reinventing the wheel | Use language idioms |

---

## ✅ Key Takeaways

1. **Design patterns** are proven solutions to common problems
2. **Three categories**: Creational, Structural, Behavioral
3. **Singleton**: Single instance globally accessible
4. **Factory**: Centralized object creation
5. **Observer**: Event notification
6. **Strategy**: Interchangeable algorithms
7. **Patterns promote** loose coupling and high cohesion

---