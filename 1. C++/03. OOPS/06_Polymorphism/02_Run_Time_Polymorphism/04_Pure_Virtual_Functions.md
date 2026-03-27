# 06_Polymorphism/02_Run_Time_Polymorphism/04_Pure_Virtual_Functions.md

# Pure Virtual Functions in C++ - Complete Guide

## 📖 Overview

Pure virtual functions are virtual functions that have no implementation in the base class. They make a class abstract, meaning it cannot be instantiated. Derived classes must override pure virtual functions to become concrete (instantiable). Pure virtual functions are the foundation for creating interfaces and abstract base classes in C++.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Pure Virtual Function** | Virtual function with `= 0` syntax, no implementation in base class |
| **Abstract Class** | Class with at least one pure virtual function, cannot be instantiated |
| **Concrete Class** | Class that overrides all pure virtual functions |
| **Interface** | Class with only pure virtual functions (and virtual destructor) |

---

## 1. **Basic Pure Virtual Functions**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// Abstract base class (cannot be instantiated)
class Shape {
protected:
    string color;
    
public:
    Shape(string c) : color(c) {}
    
    // Pure virtual functions - must be overridden
    virtual double area() const = 0;
    virtual double perimeter() const = 0;
    virtual void draw() const = 0;
    
    // Virtual destructor (can have implementation)
    virtual ~Shape() {
        cout << "Shape destructor" << endl;
    }
    
    // Non-virtual function (concrete)
    string getColor() const { return color; }
    void setColor(string c) { color = c; }
};

// Concrete class - overrides all pure virtual functions
class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(string c, double r) : Shape(c), radius(r) {}
    
    double area() const override {
        return M_PI * radius * radius;
    }
    
    double perimeter() const override {
        return 2 * M_PI * radius;
    }
    
    void draw() const override {
        cout << "Drawing " << color << " circle with radius " << radius << endl;
    }
    
    ~Circle() override {
        cout << "Circle destructor" << endl;
    }
};

class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(string c, double w, double h) : Shape(c), width(w), height(h) {}
    
    double area() const override {
        return width * height;
    }
    
    double perimeter() const override {
        return 2 * (width + height);
    }
    
    void draw() const override {
        cout << "Drawing " << color << " rectangle " << width << "x" << height << endl;
    }
    
    ~Rectangle() override {
        cout << "Rectangle destructor" << endl;
    }
};

int main() {
    cout << "=== Pure Virtual Functions ===" << endl;
    
    // Shape s("Red");  // Error! Cannot instantiate abstract class
    
    Circle circle("Red", 5.0);
    Rectangle rect("Blue", 4.0, 6.0);
    
    cout << "\n1. Using concrete objects:" << endl;
    circle.draw();
    cout << "Area: " << circle.area() << ", Perimeter: " << circle.perimeter() << endl;
    
    rect.draw();
    cout << "Area: " << rect.area() << ", Perimeter: " << rect.perimeter() << endl;
    
    cout << "\n2. Polymorphic container:" << endl;
    Shape* shapes[] = {&circle, &rect};
    
    for (auto shape : shapes) {
        shape->draw();
        cout << "Area: " << shape->area() << endl;
    }
    
    return 0;
}
```

**Output:**
```
=== Pure Virtual Functions ===

1. Using concrete objects:
Drawing Red circle with radius 5
Area: 78.5398, Perimeter: 31.4159
Drawing Blue rectangle 4x6
Area: 24, Perimeter: 20

2. Polymorphic container:
Drawing Red circle with radius 5
Area: 78.5398
Drawing Blue rectangle 4x6
Area: 24
Circle destructor
Rectangle destructor
Shape destructor
Shape destructor
```

---

## 2. **Pure Virtual Destructor**

```cpp
#include <iostream>
#include <string>
using namespace std;

class AbstractBase {
public:
    // Pure virtual destructor - class becomes abstract
    virtual ~AbstractBase() = 0;
    
    // Pure virtual function
    virtual void show() const = 0;
};

// Pure virtual destructor MUST have a body
AbstractBase::~AbstractBase() {
    cout << "AbstractBase destructor" << endl;
}

class Concrete : public AbstractBase {
public:
    ~Concrete() override {
        cout << "Concrete destructor" << endl;
    }
    
    void show() const override {
        cout << "Concrete::show()" << endl;
    }
};

int main() {
    cout << "=== Pure Virtual Destructor ===" << endl;
    
    // AbstractBase ab;  // Error! Cannot instantiate abstract class
    
    Concrete c;
    c.show();
    
    cout << "\nDestructor order:" << endl;
    // Destructors called automatically
    
    cout << "\nWhy pure virtual destructor?" << endl;
    cout << "✓ Makes class abstract without other pure virtual functions" << endl;
    cout << "✓ Still must provide a body for the destructor" << endl;
    cout << "✓ Ensures proper cleanup in inheritance hierarchies" << endl;
    
    return 0;
}
```

---

## 3. **Abstract Class as Interface**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Interface (pure abstract class)
class Drawable {
public:
    virtual void draw() const = 0;
    virtual void setColor(const string& color) = 0;
    virtual string getColor() const = 0;
    virtual ~Drawable() = default;
};

// Interface for resizeable objects
class Resizeable {
public:
    virtual void resize(double factor) = 0;
    virtual void scale(double factor) = 0;
    virtual ~Resizeable() = default;
};

// Interface for movable objects
class Movable {
public:
    virtual void move(int dx, int dy) = 0;
    virtual void moveTo(int x, int y) = 0;
    virtual ~Movable() = default;
};

// Concrete class implementing multiple interfaces
class Shape : public Drawable, public Resizeable, public Movable {
private:
    string color;
    int x, y;
    double width, height;
    
public:
    Shape(string c, int xPos, int yPos, double w, double h)
        : color(c), x(xPos), y(yPos), width(w), height(h) {}
    
    // Drawable implementation
    void draw() const override {
        cout << "Shape at (" << x << ", " << y << ") size " 
             << width << "x" << height << " color " << color << endl;
    }
    
    void setColor(const string& c) override {
        color = c;
    }
    
    string getColor() const override {
        return color;
    }
    
    // Resizeable implementation
    void resize(double factor) override {
        width *= factor;
        height *= factor;
    }
    
    void scale(double factor) override {
        resize(factor);
    }
    
    // Movable implementation
    void move(int dx, int dy) override {
        x += dx;
        y += dy;
    }
    
    void moveTo(int xPos, int yPos) override {
        x = xPos;
        y = yPos;
    }
    
    double area() const {
        return width * height;
    }
};

class Circle : public Drawable, public Movable {
private:
    string color;
    int x, y;
    double radius;
    
public:
    Circle(string c, int xPos, int yPos, double r)
        : color(c), x(xPos), y(yPos), radius(r) {}
    
    void draw() const override {
        cout << "Circle at (" << x << ", " << y << ") radius " 
             << radius << " color " << color << endl;
    }
    
    void setColor(const string& c) override {
        color = c;
    }
    
    string getColor() const override {
        return color;
    }
    
    void move(int dx, int dy) override {
        x += dx;
        y += dy;
    }
    
    void moveTo(int xPos, int yPos) override {
        x = xPos;
        y = yPos;
    }
    
    double area() const {
        return 3.14159 * radius * radius;
    }
};

int main() {
    cout << "=== Abstract Class as Interface ===" << endl;
    
    Shape rect("Red", 10, 20, 100, 50);
    Circle circle("Blue", 30, 40, 25);
    
    cout << "\n1. Using Drawable interface:" << endl;
    Drawable* d1 = &rect;
    Drawable* d2 = &circle;
    
    d1->draw();
    d2->draw();
    
    cout << "\n2. Using Movable interface:" << endl;
    Movable* m1 = &rect;
    Movable* m2 = &circle;
    
    m1->move(5, 10);
    m2->move(-10, -5);
    
    cout << "\n3. After moving:" << endl;
    d1->draw();
    d2->draw();
    
    cout << "\n4. Using Resizeable interface (only Shape):" << endl;
    Resizeable* r = &rect;
    r->resize(2.0);
    d1->draw();
    cout << "Area: " << rect.area() << endl;
    
    return 0;
}
```

---

## 4. **Partial Implementation in Abstract Class**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Abstract class with partial implementation
class Database {
protected:
    string connectionString;
    bool connected;
    
public:
    Database(string conn) : connectionString(conn), connected(false) {}
    
    // Pure virtual - must be implemented by derived classes
    virtual void connect() = 0;
    virtual void disconnect() = 0;
    virtual void executeQuery(const string& query) = 0;
    
    // Concrete method - shared implementation
    bool isConnected() const {
        return connected;
    }
    
    string getConnectionString() const {
        return connectionString;
    }
    
    // Template method pattern - uses pure virtual functions
    void runTransaction(const string& query1, const string& query2) {
        if (!connected) {
            connect();
        }
        
        cout << "Starting transaction..." << endl;
        executeQuery(query1);
        executeQuery(query2);
        cout << "Committing transaction..." << endl;
    }
    
    virtual ~Database() {
        if (connected) {
            disconnect();
        }
    }
};

class MySQLDatabase : public Database {
public:
    MySQLDatabase(string conn) : Database(conn) {}
    
    void connect() override {
        cout << "Connecting to MySQL: " << connectionString << endl;
        connected = true;
    }
    
    void disconnect() override {
        cout << "Disconnecting from MySQL" << endl;
        connected = false;
    }
    
    void executeQuery(const string& query) override {
        cout << "MySQL executing: " << query << endl;
    }
};

class PostgreSQLDatabase : public Database {
public:
    PostgreSQLDatabase(string conn) : Database(conn) {}
    
    void connect() override {
        cout << "Connecting to PostgreSQL: " << connectionString << endl;
        connected = true;
    }
    
    void disconnect() override {
        cout << "Disconnecting from PostgreSQL" << endl;
        connected = false;
    }
    
    void executeQuery(const string& query) override {
        cout << "PostgreSQL executing: " << query << endl;
    }
};

int main() {
    cout << "=== Partial Implementation in Abstract Class ===" << endl;
    
    MySQLDatabase mysql("mysql://localhost:3306/mydb");
    PostgreSQLDatabase pg("postgresql://localhost:5432/mydb");
    
    cout << "\n1. MySQL operations:" << endl;
    mysql.runTransaction("INSERT INTO users VALUES('Alice')", 
                         "UPDATE logs SET count=count+1");
    
    cout << "\n2. PostgreSQL operations:" << endl;
    pg.runTransaction("SELECT * FROM products", 
                      "INSERT INTO audit VALUES('query')");
    
    cout << "\n3. Checking connection status:" << endl;
    cout << "MySQL connected: " << (mysql.isConnected() ? "Yes" : "No") << endl;
    cout << "PostgreSQL connected: " << (pg.isConnected() ? "Yes" : "No") << endl;
    
    return 0;
}
```

---

## 5. **Pure Virtual Functions with Default Arguments**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Shape {
public:
    // Pure virtual function with default argument
    virtual void draw(string color = "Black") const = 0;
    
    // Regular virtual function with default argument
    virtual void setSize(double size = 1.0) {
        cout << "Shape::setSize(" << size << ")" << endl;
    }
    
    virtual ~Shape() = default;
};

class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(double r) : radius(r) {}
    
    // Default argument is taken from base class declaration
    void draw(string color = "Red") const override {
        cout << "Drawing " << color << " circle with radius " << radius << endl;
    }
    
    void setSize(double size = 2.0) override {
        radius = size;
        cout << "Circle::setSize(" << size << ")" << endl;
    }
};

int main() {
    cout << "=== Pure Virtual Functions with Default Arguments ===" << endl;
    
    Circle circle(5.0);
    Shape* ptr = &circle;
    
    cout << "\n1. Direct call to Circle::draw():" << endl;
    circle.draw();           // Uses Circle's default "Red"
    circle.draw("Blue");     // Explicit argument
    
    cout << "\n2. Call through base pointer:" << endl;
    ptr->draw();             // Uses Base's default "Black"!
    ptr->draw("Green");      // Explicit argument
    
    cout << "\n3. Default arguments are statically bound:" << endl;
    cout << "   Base pointer uses Base's default arguments" << endl;
    cout << "   Derived object uses Derived's default arguments" << endl;
    
    cout << "\n4. Virtual functions with default arguments:" << endl;
    ptr->setSize();          // Uses Base's default 1.0? Actually dynamic binding for function, static for default
    // Note: setSize is virtual, but default arguments are determined at compile time
    
    return 0;
}
```

---

## 6. **Practical Example: Plugin Architecture**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <map>
using namespace std;

// Plugin interface (pure abstract class)
class IPlugin {
protected:
    string name;
    string version;
    
public:
    IPlugin(string n, string v) : name(n), version(v) {}
    
    // Pure virtual interface
    virtual bool initialize() = 0;
    virtual void execute() = 0;
    virtual void shutdown() = 0;
    virtual string getDescription() const = 0;
    
    // Concrete methods
    string getName() const { return name; }
    string getVersion() const { return version; }
    
    virtual ~IPlugin() = default;
};

// Abstract plugin with common functionality
class BasePlugin : public IPlugin {
protected:
    bool isActive;
    
public:
    BasePlugin(string n, string v) : IPlugin(n, v), isActive(false) {}
    
    bool initialize() override {
        isActive = true;
        cout << "  " << name << " v" << version << " initialized" << endl;
        return true;
    }
    
    void shutdown() override {
        if (isActive) {
            cout << "  " << name << " v" << version << " shutdown" << endl;
            isActive = false;
        }
    }
    
    bool isActive() const { return isActive; }
};

// Concrete plugin 1
class LoggerPlugin : public BasePlugin {
private:
    vector<string> logs;
    
public:
    LoggerPlugin() : BasePlugin("Logger", "1.0") {}
    
    void execute() override {
        if (isActive) {
            logs.push_back("Log entry at " + to_string(time(nullptr)));
            cout << "  Logger: recorded log entry (" << logs.size() << " total)" << endl;
        }
    }
    
    string getDescription() const override {
        return "Logs system events to internal storage";
    }
    
    void showLogs() const {
        cout << "  Logger logs (" << logs.size() << " entries):" << endl;
        for (const auto& log : logs) {
            cout << "    " << log << endl;
        }
    }
};

// Concrete plugin 2
class DataProcessorPlugin : public BasePlugin {
private:
    int processedCount;
    
public:
    DataProcessorPlugin() : BasePlugin("DataProcessor", "2.1"), processedCount(0) {}
    
    void execute() override {
        if (isActive) {
            processedCount++;
            cout << "  DataProcessor: processed " << processedCount << " items" << endl;
        }
    }
    
    string getDescription() const override {
        return "Processes data streams with high performance";
    }
    
    int getProcessedCount() const { return processedCount; }
};

// Concrete plugin 3
class SecurityPlugin : public BasePlugin {
private:
    int authAttempts;
    int failedAttempts;
    
public:
    SecurityPlugin() : BasePlugin("Security", "1.5"), authAttempts(0), failedAttempts(0) {}
    
    void execute() override {
        if (isActive) {
            cout << "  Security: performing security check" << endl;
        }
    }
    
    string getDescription() const override {
        return "Provides authentication and authorization services";
    }
    
    bool authenticate(const string& user, const string& pass) {
        if (isActive) {
            authAttempts++;
            bool success = (user == "admin" && pass == "secret");
            if (!success) failedAttempts++;
            cout << "  Security: auth for " << user << " - " 
                 << (success ? "SUCCESS" : "FAILED") << endl;
            return success;
        }
        return false;
    }
    
    void showStats() const {
        cout << "  Security stats: " << authAttempts << " attempts, "
             << failedAttempts << " failed" << endl;
    }
};

class PluginManager {
private:
    vector<unique_ptr<IPlugin>> plugins;
    map<string, IPlugin*> pluginMap;
    
public:
    void registerPlugin(IPlugin* plugin) {
        plugins.emplace_back(plugin);
        pluginMap[plugin->getName()] = plugin;
        cout << "Registered: " << plugin->getName() << " v" << plugin->getVersion() << endl;
    }
    
    void initializeAll() {
        cout << "\n=== Initializing Plugins ===" << endl;
        for (auto& plugin : plugins) {
            plugin->initialize();
        }
    }
    
    void executeAll() {
        cout << "\n=== Executing Plugins ===" << endl;
        for (auto& plugin : plugins) {
            plugin->execute();
        }
    }
    
    void shutdownAll() {
        cout << "\n=== Shutting Down Plugins ===" << endl;
        for (auto& plugin : plugins) {
            plugin->shutdown();
        }
    }
    
    template<typename T>
    T* getPlugin(const string& name) {
        auto it = pluginMap.find(name);
        if (it != pluginMap.end()) {
            return dynamic_cast<T*>(it->second);
        }
        return nullptr;
    }
    
    void showInfo() const {
        cout << "\n=== Plugin Information ===" << endl;
        for (const auto& plugin : plugins) {
            cout << "  " << plugin->getName() << " v" << plugin->getVersion() << endl;
            cout << "    " << plugin->getDescription() << endl;
        }
    }
};

int main() {
    cout << "=== Plugin Architecture with Pure Virtual Functions ===" << endl;
    
    PluginManager manager;
    
    cout << "\n1. Registering plugins:" << endl;
    manager.registerPlugin(new LoggerPlugin());
    manager.registerPlugin(new DataProcessorPlugin());
    manager.registerPlugin(new SecurityPlugin());
    
    manager.showInfo();
    
    cout << "\n2. Initializing plugins:" << endl;
    manager.initializeAll();
    
    cout << "\n3. Executing plugins:" << endl;
    manager.executeAll();
    manager.executeAll();  // Second execution
    
    cout << "\n4. Using specific plugins:" << endl;
    auto logger = manager.getPlugin<LoggerPlugin>("Logger");
    if (logger) {
        logger->showLogs();
    }
    
    auto security = manager.getPlugin<SecurityPlugin>("Security");
    if (security) {
        security->authenticate("admin", "secret");
        security->authenticate("user", "wrong");
        security->showStats();
    }
    
    auto processor = manager.getPlugin<DataProcessorPlugin>("DataProcessor");
    if (processor) {
        cout << "  DataProcessor processed: " << processor->getProcessedCount() << " items" << endl;
    }
    
    cout << "\n5. Shutting down plugins:" << endl;
    manager.shutdownAll();
    
    return 0;
}
```

---

## 📊 Pure Virtual Functions Summary

| Aspect | Description |
|--------|-------------|
| **Syntax** | `virtual returnType functionName(params) = 0;` |
| **Purpose** | Define abstract classes, create interfaces |
| **Abstract Class** | Class with at least one pure virtual function |
| **Concrete Class** | Class that overrides all pure virtual functions |
| **Pure Virtual Destructor** | Makes class abstract, must have body |
| **Interface** | Class with only pure virtual functions |

---

## ✅ Best Practices

1. **Use pure virtual functions** to define interfaces
2. **Make destructor virtual** (pure or regular) in abstract classes
3. **Provide default implementations** when appropriate
4. **Use abstract classes** to prevent instantiation of incomplete types
5. **Separate interface from implementation** using abstract classes
6. **Document** which functions must be overridden

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Missing override** | Class remains abstract | Override all pure virtual functions |
| **Pure virtual destructor without body** | Linker error | Provide body even for pure virtual destructor |
| **Instantiating abstract class** | Compilation error | Don't try to instantiate |
| **Not making destructor virtual** | Memory leak | Always make destructor virtual in abstract classes |

---

## ✅ Key Takeaways

1. **Pure virtual functions** make classes abstract
2. **Abstract classes** cannot be instantiated
3. **Derived classes** must override all pure virtual functions to become concrete
4. **Pure virtual destructor** must have a body
5. **Interfaces** are classes with only pure virtual functions
6. **Template method pattern** uses pure virtual functions for customizable steps

---