# Type Conversion in OOP - Complete Guide

## 📖 Overview

Type conversion (also called type casting) in Object-Oriented Programming allows objects of one type to be treated as another type. C++ provides several casting operators for different conversion scenarios, each with specific purposes and safety guarantees. Understanding these conversions is essential for writing robust polymorphic code.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Upcasting** | Converting derived to base (always safe) |
| **Downcasting** | Converting base to derived (needs check) |
| **static_cast** | Compile-time checked conversion |
| **dynamic_cast** | Runtime checked conversion for polymorphic types |
| **reinterpret_cast** | Low-level bitwise conversion |
| **const_cast** | Adding/removing const qualifier |

---

## 1. **Upcasting (Derived to Base)**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Animal {
protected:
    string name;
    
public:
    Animal(string n) : name(n) {}
    
    virtual void speak() const {
        cout << name << " makes a sound" << endl;
    }
    
    virtual ~Animal() {}
};

class Dog : public Animal {
private:
    string breed;
    
public:
    Dog(string n, string b) : Animal(n), breed(b) {}
    
    void speak() const override {
        cout << name << " barks: Woof! (" << breed << ")" << endl;
    }
    
    void wagTail() const {
        cout << name << " wags tail" << endl;
    }
};

class Cat : public Animal {
public:
    Cat(string n) : Animal(n) {}
    
    void speak() const override {
        cout << name << " meows: Meow!" << endl;
    }
    
    void purr() const {
        cout << name << " purrs" << endl;
    }
};

int main() {
    cout << "=== Upcasting (Derived to Base) ===" << endl;
    
    Dog dog("Buddy", "Golden Retriever");
    Cat cat("Whiskers");
    
    cout << "\n1. Implicit upcasting (safe):" << endl;
    Animal* a1 = &dog;  // Implicit conversion
    Animal* a2 = &cat;  // Implicit conversion
    
    a1->speak();  // Virtual call works
    a2->speak();
    
    cout << "\n2. Explicit upcasting with static_cast:" << endl;
    Animal* a3 = static_cast<Animal*>(&dog);
    a3->speak();
    
    cout << "\n3. Upcasting in containers:" << endl;
    vector<Animal*> animals;
    animals.push_back(&dog);
    animals.push_back(&cat);
    
    for (auto a : animals) {
        a->speak();  // Polymorphic behavior
    }
    
    return 0;
}
```

**Output:**
```
=== Upcasting (Derived to Base) ===

1. Implicit upcasting (safe):
Buddy barks: Woof! (Golden Retriever)
Whiskers meows: Meow!

2. Explicit upcasting with static_cast:
Buddy barks: Woof! (Golden Retriever)

3. Upcasting in containers:
Buddy barks: Woof! (Golden Retriever)
Whiskers meows: Meow!
```

---

## 2. **Downcasting (Base to Derived)**

```cpp
#include <iostream>
#include <string>
#include <typeinfo>
using namespace std;

class Shape {
public:
    virtual void draw() const {
        cout << "Drawing shape" << endl;
    }
    virtual ~Shape() {}
};

class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(double r) : radius(r) {}
    
    void draw() const override {
        cout << "Drawing circle with radius " << radius << endl;
    }
    
    void setRadius(double r) { radius = r; }
    double getRadius() const { return radius; }
};

class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    
    void draw() const override {
        cout << "Drawing rectangle " << width << "x" << height << endl;
    }
    
    double getArea() const { return width * height; }
};

void processShape(Shape* shape) {
    shape->draw();
    
    // Downcasting with dynamic_cast (safe)
    Circle* circle = dynamic_cast<Circle*>(shape);
    if (circle) {
        cout << "  It's a circle! Radius: " << circle->getRadius() << endl;
    }
    
    Rectangle* rect = dynamic_cast<Rectangle*>(shape);
    if (rect) {
        cout << "  It's a rectangle! Area: " << rect->getArea() << endl;
    }
}

int main() {
    cout << "=== Downcasting (Base to Derived) ===" << endl;
    
    Circle circle(5.0);
    Rectangle rect(4.0, 6.0);
    
    cout << "\n1. Using dynamic_cast (safe):" << endl;
    Shape* s1 = &circle;
    Shape* s2 = &rect;
    
    Circle* c = dynamic_cast<Circle*>(s1);
    if (c) {
        cout << "Cast successful: radius = " << c->getRadius() << endl;
    }
    
    Rectangle* r = dynamic_cast<Rectangle*>(s2);
    if (r) {
        cout << "Cast successful: area = " << r->getArea() << endl;
    }
    
    cout << "\n2. Wrong cast (returns nullptr):" << endl;
    Circle* wrong = dynamic_cast<Circle*>(s2);
    if (!wrong) {
        cout << "Cannot cast Rectangle to Circle" << endl;
    }
    
    cout << "\n3. Using dynamic_cast with references:" << endl;
    try {
        Circle& cRef = dynamic_cast<Circle&>(*s1);
        cout << "Reference cast successful: radius = " << cRef.getRadius() << endl;
        
        // This will throw
        Circle& badRef = dynamic_cast<Circle&>(*s2);
    } catch (const bad_cast& e) {
        cout << "Bad cast: " << e.what() << endl;
    }
    
    cout << "\n4. Using in function:" << endl;
    processShape(&circle);
    processShape(&rect);
    
    return 0;
}
```

---

## 3. **static_cast vs dynamic_cast**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
public:
    virtual void show() { cout << "Base::show()" << endl; }
    virtual ~Base() {}
};

class Derived : public Base {
public:
    void show() override { cout << "Derived::show()" << endl; }
    void derivedOnly() { cout << "Derived::derivedOnly()" << endl; }
};

class Other {
public:
    void other() { cout << "Other::other()" << endl; }
};

int main() {
    cout << "=== static_cast vs dynamic_cast ===" << endl;
    
    Derived d;
    Base* basePtr = &d;
    
    cout << "\n1. Upcast (both work):" << endl;
    Base* b1 = static_cast<Base*>(&d);
    Base* b2 = dynamic_cast<Base*>(&d);
    b1->show();
    b2->show();
    
    cout << "\n2. Downcast (dynamic_cast safe):" << endl;
    
    // static_cast - no runtime check (dangerous)
    Derived* d1 = static_cast<Derived*>(basePtr);
    d1->derivedOnly();  // OK in this case
    
    // dynamic_cast - runtime check (safe)
    Derived* d2 = dynamic_cast<Derived*>(basePtr);
    if (d2) {
        d2->derivedOnly();
    }
    
    cout << "\n3. Wrong cast (static_cast dangerous):" << endl;
    Base base;
    Base* basePtr2 = &base;
    
    // static_cast - compiles, but undefined behavior
    Derived* d3 = static_cast<Derived*>(basePtr2);
    // d3->derivedOnly();  // Undefined behavior!
    
    // dynamic_cast - returns nullptr
    Derived* d4 = dynamic_cast<Derived*>(basePtr2);
    if (!d4) {
        cout << "dynamic_cast failed (safe)" << endl;
    }
    
    cout << "\n4. Cast between unrelated types:" << endl;
    Other* o = reinterpret_cast<Other*>(basePtr);
    // o->other();  // Dangerous! Only use with reinterpret_cast
    
    cout << "\nWhen to use:" << endl;
    cout << "  static_cast:   Upcast, well-defined conversions" << endl;
    cout << "  dynamic_cast:  Safe downcast for polymorphic types" << endl;
    cout << "  reinterpret_cast: Low-level bit casting (avoid)" << endl;
    cout << "  const_cast:    Remove const (avoid unless necessary)" << endl;
    
    return 0;
}
```

---

## 4. **const_cast for Const Removal**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Data {
private:
    string value;
    
public:
    Data(string v) : value(v) {}
    
    const string& getValue() const { return value; }
    
    void setValue(const string& v) { value = v; }
    
    void display() const { cout << "Value: " << value << endl; }
};

void modifyData(const Data& d) {
    // d.setValue("Modified");  // Error! Cannot call non-const on const
    
    // const_cast to remove const (use with caution!)
    Data& mutableData = const_cast<Data&>(d);
    mutableData.setValue("Modified via const_cast");
    cout << "Modified via const_cast" << endl;
}

class Logger {
private:
    mutable int logCount;  // Better: use mutable instead of const_cast
    
public:
    void log(const string& msg) const {
        // const_cast<int&>(logCount)++;  // Bad: use mutable instead
        logCount++;  // OK with mutable
        cout << "[LOG] " << msg << " (" << logCount << ")" << endl;
    }
    
    int getLogCount() const { return logCount; }
    
    Logger() : logCount(0) {}
};

int main() {
    cout << "=== const_cast for Const Removal ===" << endl;
    
    cout << "\n1. Modifying const object:" << endl;
    Data d("Original");
    d.display();
    
    modifyData(d);
    d.display();
    
    cout << "\n2. Better approach with mutable:" << endl;
    const Logger logger;
    logger.log("Message 1");
    logger.log("Message 2");
    logger.log("Message 3");
    cout << "Total logs: " << logger.getLogCount() << endl;
    
    cout << "\n3. When to use const_cast:" << endl;
    cout << "  ✓ Legacy APIs that take non-const but don't modify" << endl;
    cout << "  ✓ Rare cases where const-correctness is external" << endl;
    cout << "  ✗ Avoid for regular data modification" << endl;
    cout << "  ✗ Better to use mutable when possible" << endl;
    
    return 0;
}
```

---

## 5. **User-Defined Conversions**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Rational {
private:
    int numerator;
    int denominator;
    
    void simplify() {
        int gcd = 1;
        for (int i = 2; i <= abs(numerator) && i <= abs(denominator); i++) {
            if (numerator % i == 0 && denominator % i == 0) gcd = i;
        }
        numerator /= gcd;
        denominator /= gcd;
        
        if (denominator < 0) {
            numerator = -numerator;
            denominator = -denominator;
        }
    }
    
public:
    Rational(int num = 0, int den = 1) : numerator(num), denominator(den) {
        if (denominator == 0) throw invalid_argument("Denominator cannot be zero");
        simplify();
    }
    
    // Conversion to double
    operator double() const {
        return static_cast<double>(numerator) / denominator;
    }
    
    // Conversion to int (explicit to avoid accidental conversion)
    explicit operator int() const {
        return numerator / denominator;
    }
    
    void display() const {
        cout << numerator << "/" << denominator;
    }
};

class Complex {
private:
    double real, imag;
    
public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}
    
    // Conversion from Rational
    Complex(const Rational& r) : real(static_cast<double>(r)), imag(0) {}
    
    // Conversion to string
    operator string() const {
        string result = to_string(real);
        if (imag >= 0) result += " + " + to_string(imag) + "i";
        else result += " - " + to_string(-imag) + "i";
        return result;
    }
    
    void display() const {
        cout << real;
        if (imag >= 0) cout << " + " << imag << "i";
        else cout << " - " << -imag << "i";
    }
};

int main() {
    cout << "=== User-Defined Conversions ===" << endl;
    
    cout << "\n1. Rational to double (implicit):" << endl;
    Rational r(3, 4);
    double d = r;  // Implicit conversion
    cout << "r = "; r.display();
    cout << " converted to double: " << d << endl;
    
    cout << "\n2. Rational to int (explicit):" << endl;
    Rational r2(7, 2);
    // int i = r2;  // Error! Conversion is explicit
    int i = static_cast<int>(r2);
    cout << "r2 = "; r2.display();
    cout << " converted to int: " << i << endl;
    
    cout << "\n3. Rational to Complex (implicit):" << endl;
    Complex c = r;  // Implicit conversion
    cout << "Complex from rational: ";
    c.display();
    cout << endl;
    
    cout << "\n4. Complex to string (explicit):" << endl;
    Complex c2(3, 4);
    // string s = c2;  // Error! Conversion is explicit
    string s = static_cast<string>(c2);
    cout << "Complex as string: " << s << endl;
    
    cout << "\n5. Mixed operations:" << endl;
    double result = r + 0.5;  // Rational converted to double
    cout << "r + 0.5 = " << result << endl;
    
    return 0;
}
```

---

## 6. **Practical Example: Safe Type Conversions**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <typeinfo>
using namespace std;

class IPlugin {
public:
    virtual void execute() = 0;
    virtual string getName() const = 0;
    virtual ~IPlugin() = default;
};

class LoggerPlugin : public IPlugin {
public:
    void execute() override {
        cout << "Logger: Logging information" << endl;
    }
    
    string getName() const override {
        return "Logger";
    }
    
    void writeLog(const string& msg) {
        cout << "[LOG] " << msg << endl;
    }
};

class DataPlugin : public IPlugin {
public:
    void execute() override {
        cout << "DataPlugin: Processing data" << endl;
    }
    
    string getName() const override {
        return "DataProcessor";
    }
    
    void process(const string& data) {
        cout << "Processing: " << data << endl;
    }
};

class SecurityPlugin : public IPlugin {
public:
    void execute() override {
        cout << "Security: Checking permissions" << endl;
    }
    
    string getName() const override {
        return "Security";
    }
    
    bool authenticate(const string& user, const string& pass) {
        cout << "Authenticating " << user << endl;
        return user == "admin" && pass == "secret";
    }
};

class PluginManager {
private:
    vector<unique_ptr<IPlugin>> plugins;
    
public:
    void addPlugin(IPlugin* plugin) {
        plugins.emplace_back(plugin);
    }
    
    void executeAll() {
        for (auto& plugin : plugins) {
            plugin->execute();
        }
    }
    
    template<typename T>
    T* getPlugin(const string& name) {
        for (auto& plugin : plugins) {
            if (plugin->getName() == name) {
                // Safe downcasting with dynamic_cast
                return dynamic_cast<T*>(plugin.get());
            }
        }
        return nullptr;
    }
    
    void usePlugin(const string& name) {
        IPlugin* plugin = nullptr;
        for (auto& p : plugins) {
            if (p->getName() == name) {
                plugin = p.get();
                break;
            }
        }
        
        if (!plugin) return;
        
        // Type-safe handling with dynamic_cast
        if (auto logger = dynamic_cast<LoggerPlugin*>(plugin)) {
            logger->writeLog("Using logger plugin");
        } else if (auto data = dynamic_cast<DataPlugin*>(plugin)) {
            data->process("Sample data");
        } else if (auto security = dynamic_cast<SecurityPlugin*>(plugin)) {
            security->authenticate("admin", "secret");
        } else {
            cout << "Unknown plugin type" << endl;
        }
    }
};

int main() {
    cout << "=== Safe Type Conversions in Practice ===" << endl;
    
    PluginManager manager;
    manager.addPlugin(new LoggerPlugin());
    manager.addPlugin(new DataPlugin());
    manager.addPlugin(new SecurityPlugin());
    
    cout << "\n1. Executing all plugins:" << endl;
    manager.executeAll();
    
    cout << "\n2. Type-safe plugin access:" << endl;
    auto logger = manager.getPlugin<LoggerPlugin>("Logger");
    if (logger) {
        logger->writeLog("Accessing via safe downcast");
    }
    
    auto data = manager.getPlugin<DataPlugin>("DataProcessor");
    if (data) {
        data->process("Custom data");
    }
    
    auto security = manager.getPlugin<SecurityPlugin>("Security");
    if (security) {
        bool auth = security->authenticate("admin", "secret");
        cout << "Authentication result: " << (auth ? "Success" : "Failed") << endl;
    }
    
    cout << "\n3. Using plugin with runtime type checking:" << endl;
    manager.usePlugin("Logger");
    manager.usePlugin("DataProcessor");
    manager.usePlugin("Security");
    
    return 0;
}
```

---

## 📊 Type Conversion Summary

| Cast Type | Purpose | Safety | Runtime Cost |
|-----------|---------|--------|--------------|
| **static_cast** | Upcast, numeric conversions | Compile-time | None |
| **dynamic_cast** | Safe downcast (polymorphic) | Runtime | Moderate |
| **const_cast** | Add/remove const | Compile-time | None |
| **reinterpret_cast** | Low-level bit casting | None | None |
| **Implicit** | Built-in conversions | Compile-time | None |

---

## ✅ Best Practices

1. **Prefer static_cast** for upcasting and well-defined conversions
2. **Use dynamic_cast** for safe downcasting of polymorphic types
3. **Always check dynamic_cast result** for pointers (catch for references)
4. **Avoid const_cast** except for legacy APIs
5. **Never use reinterpret_cast** unless absolutely necessary
6. **Use virtual functions** instead of type switching when possible

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **C-style casts** | Hard to find, unsafe | Use C++ casts |
| **Unchecked downcast** | Undefined behavior | Use dynamic_cast and check |
| **const_cast misuse** | Undefined behavior | Use mutable or redesign |
| **reinterpret_cast overuse** | Portability issues | Avoid when possible |

---

## ✅ Key Takeaways

1. **Upcasting** is always safe (derived → base)
2. **Downcasting** needs runtime check for safety
3. **static_cast** for compile-time safe conversions
4. **dynamic_cast** for runtime-checked downcasting
5. **const_cast** for removing const (use sparingly)
6. **reinterpret_cast** for low-level bit casting (avoid)
7. **User-defined conversions** provide type flexibility

---
---

## Next Step

- Go to [09_Templates_and_Generic_Programming](../09_Templates_and_Generic_Programming/README.md) to understand theoretical foundations of Templates and Generic Programming.
