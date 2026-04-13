# Interfaces in C++ - Complete Guide

## 📖 Overview

An interface in C++ is a class that contains only pure virtual functions and no data members. It defines a contract that derived classes must fulfill. Interfaces enable loose coupling, multiple inheritance of behavior, and design patterns like Strategy, Observer, and Command.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Interface** | Class with only pure virtual functions |
| **Contract** | Set of methods that implementing classes must provide |
| **Multiple Interface Inheritance** | A class can implement multiple interfaces |
| **Loose Coupling** | Clients depend on interfaces, not concrete implementations |
| **Dependency Inversion** | High-level modules depend on abstractions |

---

## 1. **Basic Interface**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Interface definition (pure abstract class)
class IDrawable {
public:
    virtual void draw() const = 0;
    virtual void setColor(const string& color) = 0;
    virtual string getColor() const = 0;
    virtual ~IDrawable() = default;
};

// Implementing the interface
class Circle : public IDrawable {
private:
    string color;
    double radius;
    
public:
    Circle(double r, string c) : radius(r), color(c) {}
    
    void draw() const override {
        cout << "Drawing " << color << " circle with radius " << radius << endl;
    }
    
    void setColor(const string& c) override {
        color = c;
    }
    
    string getColor() const override {
        return color;
    }
};

class Rectangle : public IDrawable {
private:
    string color;
    double width, height;
    
public:
    Rectangle(double w, double h, string c) : width(w), height(h), color(c) {}
    
    void draw() const override {
        cout << "Drawing " << color << " rectangle " << width << "x" << height << endl;
    }
    
    void setColor(const string& c) override {
        color = c;
    }
    
    string getColor() const override {
        return color;
    }
};

int main() {
    cout << "=== Basic Interface ===" << endl;
    
    // Using interface pointers
    vector<unique_ptr<IDrawable>> shapes;
    shapes.push_back(make_unique<Circle>(5.0, "Red"));
    shapes.push_back(make_unique<Rectangle>(4.0, 6.0, "Blue"));
    
    cout << "\nDrawing all shapes:" << endl;
    for (const auto& shape : shapes) {
        shape->draw();
    }
    
    cout << "\nChanging colors:" << endl;
    shapes[0]->setColor("Green");
    shapes[1]->setColor("Yellow");
    
    for (const auto& shape : shapes) {
        shape->draw();
    }
    
    return 0;
}
```

**Output:**
```
=== Basic Interface ===

Drawing all shapes:
Drawing Red circle with radius 5
Drawing Blue rectangle 4x6

Changing colors:
Drawing Green circle with radius 5
Drawing Yellow rectangle 4x6
```

---

## 2. **Multiple Interface Inheritance**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// Multiple interfaces
class IDrawable {
public:
    virtual void draw() const = 0;
    virtual ~IDrawable() = default;
};

class IResizable {
public:
    virtual void resize(double factor) = 0;
    virtual ~IResizable() = default;
};

class IMovable {
public:
    virtual void move(int dx, int dy) = 0;
    virtual void moveTo(int x, int y) = 0;
    virtual ~IMovable() = default;
};

class ISerializable {
public:
    virtual void serialize(ostream& os) const = 0;
    virtual void deserialize(istream& is) = 0;
    virtual ~ISerializable() = default;
};

// Class implementing multiple interfaces
class Shape : public IDrawable, public IResizable, public IMovable, public ISerializable {
private:
    string name;
    int x, y;
    double width, height;
    
public:
    Shape(string n, int xPos, int yPos, double w, double h)
        : name(n), x(xPos), y(yPos), width(w), height(h) {}
    
    // IDrawable implementation
    void draw() const override {
        cout << "Drawing " << name << " at (" << x << ", " << y 
             << ") size " << width << "x" << height << endl;
    }
    
    // IResizable implementation
    void resize(double factor) override {
        width *= factor;
        height *= factor;
        cout << name << " resized to " << width << "x" << height << endl;
    }
    
    // IMovable implementation
    void move(int dx, int dy) override {
        x += dx;
        y += dy;
        cout << name << " moved to (" << x << ", " << y << ")" << endl;
    }
    
    void moveTo(int xPos, int yPos) override {
        x = xPos;
        y = yPos;
        cout << name << " moved to (" << x << ", " << y << ")" << endl;
    }
    
    // ISerializable implementation
    void serialize(ostream& os) const override {
        os << name << "," << x << "," << y << "," << width << "," << height << endl;
    }
    
    void deserialize(istream& is) override {
        string line;
        getline(is, line);
        // Simplified parsing
        cout << "Deserializing: " << line << endl;
    }
};

int main() {
    cout << "=== Multiple Interface Inheritance ===" << endl;
    
    Shape shape("Rectangle", 10, 20, 100, 50);
    
    cout << "\n1. Using IDrawable interface:" << endl;
    IDrawable* d = &shape;
    d->draw();
    
    cout << "\n2. Using IResizable interface:" << endl;
    IResizable* r = &shape;
    r->resize(2.0);
    
    cout << "\n3. Using IMovable interface:" << endl;
    IMovable* m = &shape;
    m->move(5, 10);
    m->moveTo(100, 200);
    
    cout << "\n4. Using ISerializable interface:" << endl;
    ISerializable* s = &shape;
    s->serialize(cout);
    
    cout << "\n5. Final state:" << endl;
    shape.draw();
    
    return 0;
}
```

---

## 3. **Interface Segregation Principle**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Bad: Fat interface (violates Interface Segregation Principle)
class IWorker_Bad {
public:
    virtual void work() = 0;
    virtual void eat() = 0;
    virtual void sleep() = 0;
    virtual void code() = 0;
    virtual void design() = 0;
    virtual void test() = 0;
    virtual ~IWorker_Bad() = default;
};

// Good: Segregated interfaces
class IWorkable {
public:
    virtual void work() = 0;
    virtual ~IWorkable() = default;
};

class IEatable {
public:
    virtual void eat() = 0;
    virtual ~IEatable() = default;
};

class ISleepable {
public:
    virtual void sleep() = 0;
    virtual ~ISleepable() = default;
};

class ICoder {
public:
    virtual void code() = 0;
    virtual ~ICoder() = default;
};

class IDesigner {
public:
    virtual void design() = 0;
    virtual ~IDesigner() = default;
};

class ITester {
public:
    virtual void test() = 0;
    virtual ~ITester() = default;
};

// Human implements multiple interfaces
class Human : public IWorkable, public IEatable, public ISleepable {
public:
    void work() override {
        cout << "Human is working" << endl;
    }
    
    void eat() override {
        cout << "Human is eating" << endl;
    }
    
    void sleep() override {
        cout << "Human is sleeping" << endl;
    }
};

// Developer implements specific interfaces
class Developer : public IWorkable, public IEatable, public ISleepable, public ICoder {
public:
    void work() override {
        cout << "Developer is working" << endl;
    }
    
    void eat() override {
        cout << "Developer is eating" << endl;
    }
    
    void sleep() override {
        cout << "Developer is sleeping" << endl;
    }
    
    void code() override {
        cout << "Developer is writing code" << endl;
    }
};

// Designer implements specific interfaces
class Designer : public IWorkable, public IEatable, public ISleepable, public IDesigner {
public:
    void work() override {
        cout << "Designer is working" << endl;
    }
    
    void eat() override {
        cout << "Designer is eating" << endl;
    }
    
    void sleep() override {
        cout << "Designer is sleeping" << endl;
    }
    
    void design() override {
        cout << "Designer is creating designs" << endl;
    }
};

// Tester implements specific interfaces
class Tester : public IWorkable, public IEatable, public ISleepable, public ITester {
public:
    void work() override {
        cout << "Tester is working" << endl;
    }
    
    void eat() override {
        cout << "Tester is eating" << endl;
    }
    
    void sleep() override {
        cout << "Tester is sleeping" << endl;
    }
    
    void test() override {
        cout << "Tester is testing" << endl;
    }
};

int main() {
    cout << "=== Interface Segregation Principle ===" << endl;
    
    Developer dev;
    Designer des;
    Tester test;
    Human human;
    
    cout << "\n1. Developer capabilities:" << endl;
    dev.work();
    dev.code();
    dev.eat();
    dev.sleep();
    
    cout << "\n2. Designer capabilities:" << endl;
    des.work();
    des.design();
    des.eat();
    des.sleep();
    
    cout << "\n3. Tester capabilities:" << endl;
    test.work();
    test.test();
    test.eat();
    test.sleep();
    
    cout << "\n4. Human capabilities:" << endl;
    human.work();
    human.eat();
    human.sleep();
    
    cout << "\nBenefits of interface segregation:" << endl;
    cout << "  ✓ Classes only implement what they need" << endl;
    cout << "  ✓ No dummy implementations" << endl;
    cout << "  ✓ Easier to understand and maintain" << endl;
    
    return 0;
}
```

---

## 4. **Interface as a Contract**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <stdexcept>
using namespace std;

// Interface defining contract for data sources
class IDataSource {
public:
    virtual bool open() = 0;
    virtual void close() = 0;
    virtual string read() = 0;
    virtual bool write(const string& data) = 0;
    virtual bool isOpen() const = 0;
    virtual ~IDataSource() = default;
};

// File implementation
class FileDataSource : public IDataSource {
private:
    string filename;
    FILE* file;
    bool opened;
    
public:
    FileDataSource(string name) : filename(name), file(nullptr), opened(false) {}
    
    bool open() override {
        file = fopen(filename.c_str(), "r+");
        if (file) {
            opened = true;
            cout << "File opened: " << filename << endl;
            return true;
        }
        return false;
    }
    
    void close() override {
        if (file) {
            fclose(file);
            file = nullptr;
            opened = false;
            cout << "File closed: " << filename << endl;
        }
    }
    
    string read() override {
        if (!opened) throw runtime_error("File not open");
        char buffer[1024];
        if (fgets(buffer, sizeof(buffer), file)) {
            return string(buffer);
        }
        return "";
    }
    
    bool write(const string& data) override {
        if (!opened) return false;
        return fputs(data.c_str(), file) != EOF;
    }
    
    bool isOpen() const override {
        return opened;
    }
};

// Memory implementation
class MemoryDataSource : public IDataSource {
private:
    string data;
    bool opened;
    
public:
    MemoryDataSource() : data(""), opened(false) {}
    
    bool open() override {
        opened = true;
        cout << "Memory data source opened" << endl;
        return true;
    }
    
    void close() override {
        opened = false;
        cout << "Memory data source closed" << endl;
    }
    
    string read() override {
        if (!opened) throw runtime_error("Data source not open");
        return data;
    }
    
    bool write(const string& d) override {
        if (!opened) return false;
        data = d;
        return true;
    }
    
    bool isOpen() const override {
        return opened;
    }
};

// Network implementation
class NetworkDataSource : public IDataSource {
private:
    string url;
    bool connected;
    
public:
    NetworkDataSource(string u) : url(u), connected(false) {}
    
    bool open() override {
        cout << "Connecting to: " << url << endl;
        connected = true;
        return true;
    }
    
    void close() override {
        cout << "Disconnecting from: " << url << endl;
        connected = false;
    }
    
    string read() override {
        if (!connected) throw runtime_error("Not connected");
        return "Data from " + url;
    }
    
    bool write(const string& data) override {
        if (!connected) return false;
        cout << "Sending to " << url << ": " << data << endl;
        return true;
    }
    
    bool isOpen() const override {
        return connected;
    }
};

class DataProcessor {
private:
    unique_ptr<IDataSource> source;
    
public:
    DataProcessor(IDataSource* src) : source(src) {}
    
    void process() {
        if (!source->isOpen()) {
            source->open();
        }
        
        string data = source->read();
        cout << "Processing: " << data << endl;
        
        string result = "Processed: " + data;
        source->write(result);
        
        source->close();
    }
};

int main() {
    cout << "=== Interface as a Contract ===" << endl;
    
    cout << "\n1. Using FileDataSource:" << endl;
    FileDataSource file("test.txt");
    DataProcessor fileProcessor(&file);
    fileProcessor.process();
    
    cout << "\n2. Using MemoryDataSource:" << endl;
    MemoryDataSource memory;
    DataProcessor memoryProcessor(&memory);
    memoryProcessor.process();
    
    cout << "\n3. Using NetworkDataSource:" << endl;
    NetworkDataSource network("http://api.example.com/data");
    DataProcessor networkProcessor(&network);
    networkProcessor.process();
    
    cout << "\nAll implementations follow the same contract!" << endl;
    
    return 0;
}
```

---

## 5. **Practical Example: Plugin System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <memory>
#include <functional>
using namespace std;

// Plugin interfaces
class IPlugin {
public:
    virtual bool initialize() = 0;
    virtual void execute() = 0;
    virtual void shutdown() = 0;
    virtual string getName() const = 0;
    virtual string getVersion() const = 0;
    virtual ~IPlugin() = default;
};

class IConfigurable {
public:
    virtual void configure(const map<string, string>& config) = 0;
    virtual ~IConfigurable() = default;
};

class ILoggable {
public:
    virtual void setLogLevel(int level) = 0;
    virtual ~ILoggable() = default;
};

// Logger plugin
class LoggerPlugin : public IPlugin, public IConfigurable, public ILoggable {
private:
    string name;
    string version;
    int logLevel;
    map<string, string> config;
    bool active;
    
public:
    LoggerPlugin() : name("Logger"), version("1.0"), logLevel(1), active(false) {}
    
    bool initialize() override {
        active = true;
        cout << "LoggerPlugin initialized (level=" << logLevel << ")" << endl;
        return true;
    }
    
    void execute() override {
        if (active) {
            cout << "LoggerPlugin: logging at level " << logLevel << endl;
        }
    }
    
    void shutdown() override {
        active = false;
        cout << "LoggerPlugin shutdown" << endl;
    }
    
    string getName() const override { return name; }
    string getVersion() const override { return version; }
    
    void configure(const map<string, string>& cfg) override {
        config = cfg;
        auto it = cfg.find("logLevel");
        if (it != cfg.end()) {
            logLevel = stoi(it->second);
            cout << "LoggerPlugin configured: logLevel=" << logLevel << endl;
        }
    }
    
    void setLogLevel(int level) override {
        logLevel = level;
        cout << "LoggerPlugin log level set to " << level << endl;
    }
};

// DataProcessor plugin
class DataProcessorPlugin : public IPlugin, public IConfigurable {
private:
    string name;
    string version;
    int batchSize;
    bool active;
    
public:
    DataProcessorPlugin() : name("DataProcessor"), version("2.1"), batchSize(100), active(false) {}
    
    bool initialize() override {
        active = true;
        cout << "DataProcessorPlugin initialized (batchSize=" << batchSize << ")" << endl;
        return true;
    }
    
    void execute() override {
        if (active) {
            cout << "DataProcessorPlugin: processing " << batchSize << " items" << endl;
        }
    }
    
    void shutdown() override {
        active = false;
        cout << "DataProcessorPlugin shutdown" << endl;
    }
    
    string getName() const override { return name; }
    string getVersion() const override { return version; }
    
    void configure(const map<string, string>& cfg) override {
        auto it = cfg.find("batchSize");
        if (it != cfg.end()) {
            batchSize = stoi(it->second);
            cout << "DataProcessorPlugin configured: batchSize=" << batchSize << endl;
        }
    }
};

// Security plugin
class SecurityPlugin : public IPlugin, public ILoggable {
private:
    string name;
    string version;
    int securityLevel;
    bool active;
    
public:
    SecurityPlugin() : name("Security"), version("1.5"), securityLevel(2), active(false) {}
    
    bool initialize() override {
        active = true;
        cout << "SecurityPlugin initialized (level=" << securityLevel << ")" << endl;
        return true;
    }
    
    void execute() override {
        if (active) {
            cout << "SecurityPlugin: checking security at level " << securityLevel << endl;
        }
    }
    
    void shutdown() override {
        active = false;
        cout << "SecurityPlugin shutdown" << endl;
    }
    
    string getName() const override { return name; }
    string getVersion() const override { return version; }
    
    void setLogLevel(int level) override {
        securityLevel = level;
        cout << "SecurityPlugin security level set to " << level << endl;
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
    
    void configurePlugin(const string& name, const map<string, string>& config) {
        auto* configurable = dynamic_cast<IConfigurable*>(pluginMap[name]);
        if (configurable) {
            configurable->configure(config);
        }
    }
};

int main() {
    cout << "=== Plugin System with Interfaces ===" << endl;
    
    PluginManager manager;
    
    cout << "\n1. Registering plugins:" << endl;
    manager.registerPlugin(new LoggerPlugin());
    manager.registerPlugin(new DataProcessorPlugin());
    manager.registerPlugin(new SecurityPlugin());
    
    cout << "\n2. Configuring plugins:" << endl;
    manager.configurePlugin("Logger", {{"logLevel", "3"}});
    manager.configurePlugin("DataProcessor", {{"batchSize", "500"}});
    
    cout << "\n3. Initializing plugins:" << endl;
    manager.initializeAll();
    
    cout << "\n4. Executing plugins:" << endl;
    manager.executeAll();
    
    cout << "\n5. Using specific plugin interfaces:" << endl;
    auto logger = manager.getPlugin<ILoggable>("Logger");
    if (logger) {
        logger->setLogLevel(5);
    }
    
    cout << "\n6. Shutting down plugins:" << endl;
    manager.shutdownAll();
    
    return 0;
}
```

---

## 📊 Interfaces Summary

| Aspect | Description |
|--------|-------------|
| **Definition** | Class with only pure virtual functions |
| **Purpose** | Define contract that derived classes must fulfill |
| **Data Members** | None (only pure virtual functions) |
| **Multiple Inheritance** | A class can implement multiple interfaces |
| **Loose Coupling** | Clients depend on interfaces, not implementations |
| **Design Patterns** | Strategy, Observer, Command, etc. |

---

## ✅ Best Practices

1. **Use interfaces** to define contracts
2. **Keep interfaces focused** (Interface Segregation Principle)
3. **Use pure virtual destructor** with default implementation
4. **Prefer multiple interfaces** over large monolithic ones
5. **Name interfaces** with `I` prefix (e.g., `IDrawable`)
6. **Use `override` keyword** when implementing interface methods

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Including data members** | Not a pure interface | Keep only pure virtual functions |
| **Missing virtual destructor** | Memory leak | Add virtual destructor |
| **Forgetting `= 0`** | Not pure virtual | Add `= 0` syntax |
| **Large interfaces** | Classes implement unnecessary methods | Segregate interfaces |

---

## ✅ Key Takeaways

1. **Interfaces** define contracts without implementation
2. **Pure virtual functions** define required behaviors
3. **Multiple inheritance** allows implementing multiple interfaces
4. **Interface Segregation Principle** keeps interfaces focused
5. **Loose coupling** achieved through interface dependencies
6. **Design patterns** heavily rely on interfaces
7. **Virtual destructor** ensures proper cleanup

---
---

## Next Step

- Go to [03_Abstract_vs_Concrete.md](03_Abstract_vs_Concrete.md) to continue with Abstract vs Concrete.
