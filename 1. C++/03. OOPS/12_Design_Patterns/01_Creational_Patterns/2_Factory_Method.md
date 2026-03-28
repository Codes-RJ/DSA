# 12_Design_Patterns/01_Creational_Patterns/Factory_Method.md

# Factory Method Pattern in C++ - Complete Guide

## 📖 Overview

The Factory Method pattern defines an interface for creating objects but lets subclasses decide which class to instantiate. It promotes loose coupling by eliminating the need to bind application-specific classes into the code. This pattern is particularly useful when the exact type of object to create isn't known until runtime.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Creator** | Abstract class that declares the factory method |
| **Concrete Creator** | Overrides the factory method to return a concrete product |
| **Product** | Abstract interface for objects created by the factory |
| **Concrete Product** | Specific implementation of the product |

---

## 1. **Basic Factory Method**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// Product interface
class Document {
public:
    virtual void open() = 0;
    virtual void save() = 0;
    virtual void close() = 0;
    virtual ~Document() = default;
};

// Concrete Products
class TextDocument : public Document {
private:
    string name;
    
public:
    TextDocument(string n) : name(n) {}
    
    void open() override {
        cout << "Opening text document: " << name << ".txt" << endl;
    }
    
    void save() override {
        cout << "Saving text document: " << name << ".txt" << endl;
    }
    
    void close() override {
        cout << "Closing text document: " << name << ".txt" << endl;
    }
};

class PDFDocument : public Document {
private:
    string name;
    
public:
    PDFDocument(string n) : name(n) {}
    
    void open() override {
        cout << "Opening PDF document: " << name << ".pdf" << endl;
    }
    
    void save() override {
        cout << "Saving PDF document: " << name << ".pdf" << endl;
    }
    
    void close() override {
        cout << "Closing PDF document: " << name << ".pdf" << endl;
    }
};

class SpreadsheetDocument : public Document {
private:
    string name;
    
public:
    SpreadsheetDocument(string n) : name(n) {}
    
    void open() override {
        cout << "Opening spreadsheet: " << name << ".xlsx" << endl;
    }
    
    void save() override {
        cout << "Saving spreadsheet: " << name << ".xlsx" << endl;
    }
    
    void close() override {
        cout << "Closing spreadsheet: " << name << ".xlsx" << endl;
    }
};

// Creator (Abstract Factory)
class Application {
public:
    virtual ~Application() = default;
    
    // Factory method
    virtual unique_ptr<Document> createDocument(const string& name) = 0;
    
    // Template method
    void newDocument(const string& name) {
        cout << "\nCreating new document: " << name << endl;
        auto doc = createDocument(name);
        doc->open();
        doc->save();
        doc->close();
    }
};

// Concrete Creators
class TextEditor : public Application {
public:
    unique_ptr<Document> createDocument(const string& name) override {
        return make_unique<TextDocument>(name);
    }
};

class PDFViewer : public Application {
public:
    unique_ptr<Document> createDocument(const string& name) override {
        return make_unique<PDFDocument>(name);
    }
};

class SpreadsheetApp : public Application {
public:
    unique_ptr<Document> createDocument(const string& name) override {
        return make_unique<SpreadsheetDocument>(name);
    }
};

int main() {
    cout << "=== Basic Factory Method ===" << endl;
    
    unique_ptr<Application> apps[] = {
        make_unique<TextEditor>(),
        make_unique<PDFViewer>(),
        make_unique<SpreadsheetApp>()
    };
    
    string documents[] = {"Report", "Invoice", "Budget"};
    
    for (int i = 0; i < 3; i++) {
        apps[i]->newDocument(documents[i]);
    }
    
    return 0;
}
```

**Output:**
```
=== Basic Factory Method ===

Creating new document: Report
Opening text document: Report.txt
Saving text document: Report.txt
Closing text document: Report.txt

Creating new document: Invoice
Opening PDF document: Invoice.pdf
Saving PDF document: Invoice.pdf
Closing PDF document: Invoice.pdf

Creating new document: Budget
Opening spreadsheet: Budget.xlsx
Saving spreadsheet: Budget.xlsx
Closing spreadsheet: Budget.xlsx
```

---

## 2. **Parameterized Factory Method**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <map>
using namespace std;

// Product interface
class Shape {
public:
    virtual void draw() = 0;
    virtual string getType() const = 0;
    virtual ~Shape() = default;
};

// Concrete Products
class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(double r) : radius(r) {}
    
    void draw() override {
        cout << "Drawing circle with radius " << radius << endl;
    }
    
    string getType() const override {
        return "Circle";
    }
};

class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    
    void draw() override {
        cout << "Drawing rectangle " << width << "x" << height << endl;
    }
    
    string getType() const override {
        return "Rectangle";
    }
};

class Triangle : public Shape {
private:
    double base, height;
    
public:
    Triangle(double b, double h) : base(b), height(h) {}
    
    void draw() override {
        cout << "Drawing triangle with base " << base << " and height " << height << endl;
    }
    
    string getType() const override {
        return "Triangle";
    }
};

// Factory with parameterized creation
class ShapeFactory {
public:
    static unique_ptr<Shape> createShape(const string& type, double param1, double param2 = 0) {
        if (type == "circle") {
            return make_unique<Circle>(param1);
        } else if (type == "rectangle") {
            return make_unique<Rectangle>(param1, param2);
        } else if (type == "triangle") {
            return make_unique<Triangle>(param1, param2);
        }
        return nullptr;
    }
};

class ShapeFactoryWithRegistry {
private:
    using Creator = function<unique_ptr<Shape>(const vector<double>&)>;
    map<string, Creator> registry;
    
public:
    void registerShape(const string& type, Creator creator) {
        registry[type] = creator;
    }
    
    unique_ptr<Shape> createShape(const string& type, const vector<double>& params) {
        auto it = registry.find(type);
        if (it != registry.end()) {
            return it->second(params);
        }
        return nullptr;
    }
};

int main() {
    cout << "=== Parameterized Factory Method ===" << endl;
    
    cout << "\n1. Simple parameterized factory:" << endl;
    auto circle = ShapeFactory::createShape("circle", 5.0);
    auto rectangle = ShapeFactory::createShape("rectangle", 4.0, 6.0);
    auto triangle = ShapeFactory::createShape("triangle", 3.0, 4.0);
    
    circle->draw();
    rectangle->draw();
    triangle->draw();
    
    cout << "\n2. Factory with registry (extensible):" << endl;
    ShapeFactoryWithRegistry factory;
    
    // Register shape creators
    factory.registerShape("circle", [](const vector<double>& params) {
        return make_unique<Circle>(params[0]);
    });
    
    factory.registerShape("rectangle", [](const vector<double>& params) {
        return make_unique<Rectangle>(params[0], params[1]);
    });
    
    factory.registerShape("triangle", [](const vector<double>& params) {
        return make_unique<Triangle>(params[0], params[1]);
    });
    
    // Create shapes dynamically
    auto circle2 = factory.createShape("circle", {7.0});
    auto rect2 = factory.createShape("rectangle", {5.0, 8.0});
    
    circle2->draw();
    rect2->draw();
    
    return 0;
}
```

---

## 3. **Factory Method with Multiple Products**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <vector>
using namespace std;

// Product interfaces
class IButton {
public:
    virtual void render() = 0;
    virtual void onClick() = 0;
    virtual ~IButton() = default;
};

class ICheckbox {
public:
    virtual void render() = 0;
    virtual void toggle() = 0;
    virtual ~ICheckbox() = default;
};

// Concrete products for Windows
class WindowsButton : public IButton {
public:
    void render() override {
        cout << "Rendering Windows button" << endl;
    }
    
    void onClick() override {
        cout << "Windows button clicked" << endl;
    }
};

class WindowsCheckbox : public ICheckbox {
public:
    void render() override {
        cout << "Rendering Windows checkbox" << endl;
    }
    
    void toggle() override {
        cout << "Windows checkbox toggled" << endl;
    }
};

// Concrete products for Mac
class MacButton : public IButton {
public:
    void render() override {
        cout << "Rendering Mac button" << endl;
    }
    
    void onClick() override {
        cout << "Mac button clicked" << endl;
    }
};

class MacCheckbox : public ICheckbox {
public:
    void render() override {
        cout << "Rendering Mac checkbox" << endl;
    }
    
    void toggle() override {
        cout << "Mac checkbox toggled" << endl;
    }
};

// Abstract Factory
class GUIFactory {
public:
    virtual unique_ptr<IButton> createButton() = 0;
    virtual unique_ptr<ICheckbox> createCheckbox() = 0;
    virtual ~GUIFactory() = default;
};

// Concrete Factory for Windows
class WindowsFactory : public GUIFactory {
public:
    unique_ptr<IButton> createButton() override {
        return make_unique<WindowsButton>();
    }
    
    unique_ptr<ICheckbox> createCheckbox() override {
        return make_unique<WindowsCheckbox>();
    }
};

// Concrete Factory for Mac
class MacFactory : public GUIFactory {
public:
    unique_ptr<IButton> createButton() override {
        return make_unique<MacButton>();
    }
    
    unique_ptr<ICheckbox> createCheckbox() override {
        return make_unique<MacCheckbox>();
    }
};

class Application {
private:
    unique_ptr<GUIFactory> factory;
    vector<unique_ptr<IButton>> buttons;
    vector<unique_ptr<ICheckbox>> checkboxes;
    
public:
    Application(unique_ptr<GUIFactory> f) : factory(move(f)) {}
    
    void createUI() {
        buttons.push_back(factory->createButton());
        checkboxes.push_back(factory->createCheckbox());
        buttons.push_back(factory->createButton());
    }
    
    void render() {
        cout << "\nRendering UI:" << endl;
        for (auto& btn : buttons) {
            btn->render();
        }
        for (auto& cb : checkboxes) {
            cb->render();
        }
    }
};

int main() {
    cout << "=== Factory Method with Multiple Products ===" << endl;
    
    cout << "\n1. Windows Application:" << endl;
    Application winApp(make_unique<WindowsFactory>());
    winApp.createUI();
    winApp.render();
    
    cout << "\n2. Mac Application:" << endl;
    Application macApp(make_unique<MacFactory>());
    macApp.createUI();
    macApp.render();
    
    return 0;
}
```

---

## 4. **Factory Method with Object Pool**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <stack>
#include <vector>
using namespace std;

class DatabaseConnection {
private:
    int id;
    string url;
    bool inUse;
    static int nextId;
    
public:
    DatabaseConnection(string u) : id(nextId++), url(u), inUse(false) {
        cout << "Connection " << id << " created for " << url << endl;
    }
    
    ~DatabaseConnection() {
        cout << "Connection " << id << " destroyed" << endl;
    }
    
    void connect() {
        inUse = true;
        cout << "Connection " << id << " connected" << endl;
    }
    
    void disconnect() {
        inUse = false;
        cout << "Connection " << id << " disconnected" << endl;
    }
    
    void execute(const string& query) {
        if (inUse) {
            cout << "Connection " << id << " executing: " << query << endl;
        }
    }
    
    bool isInUse() const { return inUse; }
    int getId() const { return id; }
};

int DatabaseConnection::nextId = 1;

class ConnectionPool {
private:
    stack<unique_ptr<DatabaseConnection>> available;
    vector<unique_ptr<DatabaseConnection>> all;
    string url;
    size_t maxSize;
    
public:
    ConnectionPool(string u, size_t max) : url(u), maxSize(max) {
        cout << "Connection pool created for " << url << " (max=" << max << ")" << endl;
    }
    
    // Factory method with pooling
    DatabaseConnection* getConnection() {
        if (!available.empty()) {
            DatabaseConnection* conn = available.top().get();
            available.pop();
            conn->connect();
            return conn;
        }
        
        if (all.size() < maxSize) {
            auto conn = make_unique<DatabaseConnection>(url);
            DatabaseConnection* ptr = conn.get();
            all.push_back(move(conn));
            ptr->connect();
            return ptr;
        }
        
        cout << "No available connections!" << endl;
        return nullptr;
    }
    
    void releaseConnection(DatabaseConnection* conn) {
        conn->disconnect();
        for (auto& c : all) {
            if (c.get() == conn) {
                available.push(move(c));
                break;
            }
        }
    }
    
    size_t availableCount() const {
        return available.size();
    }
    
    size_t usedCount() const {
        return all.size() - available.size();
    }
};

int main() {
    cout << "=== Factory Method with Object Pool ===" << endl;
    
    ConnectionPool pool("postgresql://localhost/mydb", 3);
    
    cout << "\n1. Getting connections:" << endl;
    auto conn1 = pool.getConnection();
    auto conn2 = pool.getConnection();
    auto conn3 = pool.getConnection();
    auto conn4 = pool.getConnection();  // Should fail
    
    cout << "\n2. Using connections:" << endl;
    conn1->execute("SELECT * FROM users");
    conn2->execute("INSERT INTO logs VALUES('test')");
    conn3->execute("UPDATE products SET price=99");
    
    cout << "\n3. Releasing connections:" << endl;
    pool.releaseConnection(conn1);
    pool.releaseConnection(conn2);
    
    cout << "\n4. Getting connections again (reusing):" << endl;
    auto conn5 = pool.getConnection();
    auto conn6 = pool.getConnection();
    
    conn5->execute("SELECT * FROM products");
    conn6->execute("INSERT INTO audit VALUES('action')");
    
    cout << "\n5. Statistics:" << endl;
    cout << "Available: " << pool.availableCount() << endl;
    cout << "Used: " << pool.usedCount() << endl;
    
    return 0;
}
```

---

## 5. **Practical Example: Logging System**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <fstream>
#include <chrono>
#include <iomanip>
#include <map>
using namespace std;

// Product interface
class ILogger {
public:
    virtual void log(const string& message, int level = 1) = 0;
    virtual void setLevel(int level) = 0;
    virtual ~ILogger() = default;
};

// Concrete products
class ConsoleLogger : public ILogger {
private:
    int level;
    
public:
    ConsoleLogger() : level(1) {}
    
    void setLevel(int l) override {
        level = l;
    }
    
    void log(const string& message, int msgLevel = 1) override {
        if (msgLevel >= level) {
            auto now = chrono::system_clock::now();
            auto time = chrono::system_clock::to_time_t(now);
            cout << put_time(localtime(&time), "[%H:%M:%S] ") << message << endl;
        }
    }
};

class FileLogger : public ILogger {
private:
    ofstream file;
    int level;
    
public:
    FileLogger(const string& filename) : level(1) {
        file.open(filename, ios::app);
        if (!file.is_open()) {
            throw runtime_error("Cannot open log file");
        }
    }
    
    ~FileLogger() {
        if (file.is_open()) {
            file.close();
        }
    }
    
    void setLevel(int l) override {
        level = l;
    }
    
    void log(const string& message, int msgLevel = 1) override {
        if (msgLevel >= level && file.is_open()) {
            auto now = chrono::system_clock::now();
            auto time = chrono::system_clock::to_time_t(now);
            file << put_time(localtime(&time), "[%H:%M:%S] ") << message << endl;
        }
    }
};

class DatabaseLogger : public ILogger {
private:
    string connection;
    int level;
    
public:
    DatabaseLogger(const string& conn) : connection(conn), level(1) {
        cout << "Connecting to database: " << connection << endl;
    }
    
    void setLevel(int l) override {
        level = l;
    }
    
    void log(const string& message, int msgLevel = 1) override {
        if (msgLevel >= level) {
            cout << "[DB:" << connection << "] " << message << endl;
        }
    }
};

// Factory with configuration
class LoggerFactory {
private:
    static map<string, function<unique_ptr<ILogger>()>> factories;
    
public:
    static void registerLogger(const string& type, function<unique_ptr<ILogger>()> factory) {
        factories[type] = factory;
    }
    
    static unique_ptr<ILogger> createLogger(const string& type) {
        auto it = factories.find(type);
        if (it != factories.end()) {
            return it->second();
        }
        return nullptr;
    }
    
    static unique_ptr<ILogger> createConfiguredLogger(const string& type, const string& config) {
        if (type == "console") {
            return make_unique<ConsoleLogger>();
        } else if (type == "file") {
            return make_unique<FileLogger>(config);
        } else if (type == "database") {
            return make_unique<DatabaseLogger>(config);
        }
        return nullptr;
    }
};

map<string, function<unique_ptr<ILogger>()>> LoggerFactory::factories;

// Initialize logger factory
struct LoggerInitializer {
    LoggerInitializer() {
        LoggerFactory::registerLogger("console", []() { return make_unique<ConsoleLogger>(); });
        LoggerFactory::registerLogger("file", []() { return make_unique<FileLogger>("app.log"); });
        LoggerFactory::registerLogger("database", []() { return make_unique<DatabaseLogger>("postgresql://localhost/logs"); });
    }
};

LoggerInitializer initializer;

class Application {
private:
    unique_ptr<ILogger> logger;
    
public:
    Application(const string& loggerType, const string& config = "") {
        logger = LoggerFactory::createConfiguredLogger(loggerType, config);
        if (!logger) {
            logger = make_unique<ConsoleLogger>();
        }
        logger->log("Application created", 1);
    }
    
    void run() {
        logger->log("Application running", 1);
        logger->log("Processing data", 2);
        logger->log("Debug info", 3);
    }
    
    ~Application() {
        logger->log("Application shutting down", 1);
    }
};

int main() {
    cout << "=== Factory Method: Logging System ===" << endl;
    
    cout << "\n1. Console Logger:" << endl;
    Application app1("console");
    app1.run();
    
    cout << "\n2. File Logger:" << endl;
    Application app2("file", "app.log");
    app2.run();
    
    cout << "\n3. Database Logger:" << endl;
    Application app3("database", "postgresql://localhost/logs");
    app3.run();
    
    return 0;
}
```

---

## 📊 Factory Method Summary

| Variant | Description | Use Case |
|---------|-------------|----------|
| **Basic** | Single factory method | Simple object creation |
| **Parameterized** | Factory with parameters | Creation based on input |
| **Abstract Factory** | Multiple factory methods | Families of related objects |
| **Registry** | Dynamically registered factories | Extensible systems |
| **Pooling** | Factory with object reuse | Performance optimization |

---

## ✅ Best Practices

1. **Use factory method** when object creation is complex
2. **Parameterize factory** for flexible creation
3. **Register factories** for extensibility
4. **Use smart pointers** for automatic memory management
5. **Separate creation from usage** for loose coupling

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Over-engineering** | Unnecessary abstraction | Use only when needed |
| **Leaky abstraction** | Client knows too much | Keep interface simple |
| **Memory leaks** | Raw pointers | Use smart pointers |
| **Not extensible** | Hard to add new types | Use registry pattern |

---

## ✅ Key Takeaways

1. **Factory Method** delegates object creation to subclasses
2. **Promotes loose coupling** between client and product classes
3. **Supports Open/Closed Principle** - easy to add new product types
4. **Parameterized factories** provide flexible creation
5. **Registry pattern** enables dynamic factory registration
6. **Object pooling** can be combined with factory pattern

---