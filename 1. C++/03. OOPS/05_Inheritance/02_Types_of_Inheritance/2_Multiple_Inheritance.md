# Multiple Inheritance in C++ - Complete Guide

## 📖 Overview

Multiple inheritance allows a derived class to inherit from two or more base classes. This powerful feature enables a class to combine behaviors from multiple sources. However, it requires careful handling to avoid ambiguity and the diamond problem.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Multiple Inheritance** | A class inherits from multiple base classes |
| **Base Classes** | Multiple parent classes |
| **Derived Class** | Child that inherits from all bases |
| **Ambiguity** | Same member name from different bases |
| **Virtual Inheritance** | Solution to diamond problem |

---

## 1. **Basic Multiple Inheritance**

```cpp
#include <iostream>
#include <string>
using namespace std;

// First base class
class Printer {
protected:
    string model;
    
public:
    Printer(string m) : model(m) {
        cout << "Printer constructor: " << model << endl;
    }
    
    void print(const string& content) {
        cout << model << " printing: " << content << endl;
    }
    
    void calibrate() {
        cout << model << " printer calibrating..." << endl;
    }
    
    virtual ~Printer() {
        cout << "Printer destructor: " << model << endl;
    }
};

// Second base class
class Scanner {
protected:
    string resolution;
    
public:
    Scanner(string r) : resolution(r) {
        cout << "Scanner constructor: " << resolution << endl;
    }
    
    void scan() {
        cout << "Scanning at " << resolution << " DPI" << endl;
    }
    
    void calibrate() {
        cout << "Scanner calibrating..." << endl;
    }
    
    virtual ~Scanner() {
        cout << "Scanner destructor: " << resolution << endl;
    }
};

// Derived class - multiple inheritance
class MultiFunctionPrinter : public Printer, public Scanner {
private:
    string deviceName;
    
public:
    MultiFunctionPrinter(string m, string r, string name) 
        : Printer(m), Scanner(r), deviceName(name) {
        cout << "MFP constructor: " << deviceName << endl;
    }
    
    void copy() {
        cout << deviceName << " copying..." << endl;
    }
    
    void fax() {
        cout << deviceName << " sending fax..." << endl;
    }
    
    // Resolve ambiguity for calibrate()
    void calibrate() {
        Printer::calibrate();  // Call Printer's version
        Scanner::calibrate();  // Call Scanner's version
        cout << deviceName << " fully calibrated" << endl;
    }
    
    ~MultiFunctionPrinter() override {
        cout << "MFP destructor: " << deviceName << endl;
    }
};

int main() {
    cout << "=== Basic Multiple Inheritance ===" << endl;
    
    cout << "\nCreating MultiFunctionPrinter:" << endl;
    MultiFunctionPrinter mfp("HP LaserJet", "1200", "Office Pro");
    
    cout << "\n=== Using Inherited Features ===" << endl;
    mfp.print("Hello World");      // From Printer
    mfp.scan();                    // From Scanner
    mfp.copy();                    // MFP's own method
    mfp.fax();                     // MFP's own method
    mfp.calibrate();               // Resolved ambiguity
    
    return 0;
}
```

**Output:**
```
=== Basic Multiple Inheritance ===

Creating MultiFunctionPrinter:
Printer constructor: HP LaserJet
Scanner constructor: 1200
MFP constructor: Office Pro

=== Using Inherited Features ===
HP LaserJet printing: Hello World
Scanning at 1200 DPI
Office Pro copying...
Office Pro sending fax...
HP LaserJet printer calibrating...
Scanner calibrating...
Office Pro fully calibrated
MFP destructor: Office Pro
Scanner destructor: 1200
Printer destructor: HP LaserJet
```

---

## 2. **Ambiguity Resolution**

```cpp
#include <iostream>
#include <string>
using namespace std;

class BaseA {
public:
    void display() {
        cout << "BaseA::display()" << endl;
    }
    
    void common() {
        cout << "BaseA::common()" << endl;
    }
};

class BaseB {
public:
    void display() {
        cout << "BaseB::display()" << endl;
    }
    
    void common() {
        cout << "BaseB::common()" << endl;
    }
    
    void specific() {
        cout << "BaseB::specific()" << endl;
    }
};

class Derived : public BaseA, public BaseB {
public:
    // Resolve ambiguity by providing own version
    void display() {
        BaseA::display();  // Call specific base version
        BaseB::display();
        cout << "Derived::display()" << endl;
    }
    
    // Resolve ambiguity by selecting one
    void useCommonA() {
        BaseA::common();  // Explicitly call BaseA version
    }
    
    void useCommonB() {
        BaseB::common();  // Explicitly call BaseB version
    }
    
    // No ambiguity for unique method
    void callSpecific() {
        specific();  // OK - only in BaseB
    }
};

int main() {
    cout << "=== Ambiguity Resolution in Multiple Inheritance ===" << endl;
    
    Derived d;
    
    cout << "\n1. Ambiguous call (would cause error):" << endl;
    // d.display();  // Error! Ambiguous - both BaseA and BaseB have display()
    d.display();     // Now resolved - uses Derived's version
    
    cout << "\n2. Explicit base calls:" << endl;
    d.BaseA::display();
    d.BaseB::display();
    
    cout << "\n3. Resolving common method:" << endl;
    d.useCommonA();   // Calls BaseA::common()
    d.useCommonB();   // Calls BaseB::common()
    
    cout << "\n4. Unique method (no ambiguity):" << endl;
    d.callSpecific(); // Calls BaseB::specific()
    
    return 0;
}
```

**Output:**
```
=== Ambiguity Resolution in Multiple Inheritance ===

1. Ambiguous call (would cause error):
BaseA::display()
BaseB::display()
Derived::display()

2. Explicit base calls:
BaseA::display()
BaseB::display()

3. Resolving common method:
BaseA::common()
BaseB::common()

4. Unique method (no ambiguity):
BaseB::specific()
```

---

## 3. **Constructor and Destructor Order**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base1 {
private:
    string name;
    
public:
    Base1(string n) : name(n) {
        cout << "Base1 constructor: " << name << endl;
    }
    
    ~Base1() {
        cout << "Base1 destructor: " << name << endl;
    }
};

class Base2 {
private:
    string name;
    
public:
    Base2(string n) : name(n) {
        cout << "Base2 constructor: " << name << endl;
    }
    
    ~Base2() {
        cout << "Base2 destructor: " << name << endl;
    }
};

class Member1 {
private:
    string name;
    
public:
    Member1(string n) : name(n) {
        cout << "  Member1 constructor: " << name << endl;
    }
    
    ~Member1() {
        cout << "  Member1 destructor: " << name << endl;
    }
};

class Member2 {
private:
    string name;
    
public:
    Member2(string n) : name(n) {
        cout << "  Member2 constructor: " << name << endl;
    }
    
    ~Member2() {
        cout << "  Member2 destructor: " << name << endl;
    }
};

class Derived : public Base1, public Base2 {
private:
    Member1 m1;
    Member2 m2;
    
public:
    Derived(string b1Name, string b2Name, string m1Name, string m2Name) 
        : Base1(b1Name), Base2(b2Name), m2(m2Name), m1(m1Name) {
        cout << "Derived constructor body" << endl;
    }
    
    ~Derived() {
        cout << "Derived destructor body" << endl;
    }
};

int main() {
    cout << "=== Constructor/Destructor Order in Multiple Inheritance ===" << endl;
    cout << "\nConstruction order:" << endl;
    cout << "1. Base classes (in declaration order)" << endl;
    cout << "2. Member objects (in declaration order)" << endl;
    cout << "3. Derived class constructor body" << endl;
    cout << "\nDestruction order: REVERSE of construction\n" << endl;
    
    {
        Derived d("Base1Obj", "Base2Obj", "Member1Obj", "Member2Obj");
        cout << "\nObject created successfully" << endl;
    }  // Destructor called here
    
    return 0;
}
```

**Output:**
```
=== Constructor/Destructor Order in Multiple Inheritance ===

Construction order:
1. Base classes (in declaration order)
2. Member objects (in declaration order)
3. Derived class constructor body

Destruction order: REVERSE of construction

Base1 constructor: Base1Obj
Base2 constructor: Base2Obj
  Member1 constructor: Member1Obj
  Member2 constructor: Member2Obj
Derived constructor body

Object created successfully
Derived destructor body
  Member2 destructor: Member2Obj
  Member1 destructor: Member1Obj
Base2 destructor: Base2Obj
Base1 destructor: Base1Obj
```

---

## 4. **Practical Example: Smart Home Device**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <chrono>
#include <thread>
using namespace std;

// Base class 1: Connectivity
class WiFiDevice {
protected:
    string ssid;
    string ipAddress;
    bool connected;
    
public:
    WiFiDevice(string ssid) : ssid(ssid), connected(false), ipAddress("0.0.0.0") {
        cout << "WiFiDevice created" << endl;
    }
    
    void connect() {
        cout << "Connecting to WiFi: " << ssid << endl;
        this_thread::sleep_for(chrono::milliseconds(500));
        connected = true;
        ipAddress = "192.168.1." + to_string(rand() % 255);
        cout << "Connected! IP: " << ipAddress << endl;
    }
    
    void disconnect() {
        if (connected) {
            cout << "Disconnecting from WiFi..." << endl;
            connected = false;
            ipAddress = "0.0.0.0";
        }
    }
    
    void sendData(const string& data) {
        if (connected) {
            cout << "Sending: " << data << " via WiFi" << endl;
        } else {
            cout << "Not connected to WiFi!" << endl;
        }
    }
    
    virtual ~WiFiDevice() {
        disconnect();
        cout << "WiFiDevice destroyed" << endl;
    }
};

// Base class 2: Sensor
class Sensor {
protected:
    string sensorType;
    bool active;
    double lastReading;
    
public:
    Sensor(string type) : sensorType(type), active(false), lastReading(0) {
        cout << "Sensor created: " << sensorType << endl;
    }
    
    void activate() {
        active = true;
        cout << sensorType << " sensor activated" << endl;
    }
    
    void deactivate() {
        active = false;
        cout << sensorType << " sensor deactivated" << endl;
    }
    
    virtual double readValue() {
        if (active) {
            lastReading = rand() % 100;
            cout << sensorType << " reading: " << lastReading << endl;
            return lastReading;
        }
        cout << "Sensor not active!" << endl;
        return 0;
    }
    
    virtual ~Sensor() {
        deactivate();
        cout << "Sensor destroyed: " << sensorType << endl;
    }
};

// Derived class - Multiple Inheritance
class SmartSensor : public WiFiDevice, public Sensor {
private:
    string deviceName;
    int batteryLevel;
    vector<double> readingHistory;
    
public:
    SmartSensor(string name, string wifiSSID, string sensorType, int battery) 
        : WiFiDevice(wifiSSID), Sensor(sensorType), deviceName(name), batteryLevel(battery) {
        cout << "SmartSensor created: " << deviceName << endl;
    }
    
    void sendReading() {
        if (active && connected) {
            double reading = readValue();
            readingHistory.push_back(reading);
            string data = deviceName + ":" + sensorType + ":" + to_string(reading);
            sendData(data);
        } else {
            cout << "Cannot send reading - device not ready!" << endl;
        }
    }
    
    void checkBattery() {
        cout << deviceName << " battery: " << batteryLevel << "%" << endl;
        if (batteryLevel < 20) {
            cout << "Warning: Low battery!" << endl;
        }
    }
    
    void displayStats() {
        cout << "\n=== " << deviceName << " Statistics ===" << endl;
        cout << "Sensor Type: " << sensorType << endl;
        cout << "Battery: " << batteryLevel << "%" << endl;
        cout << "WiFi: " << (connected ? "Connected" : "Disconnected") << endl;
        cout << "Sensor: " << (active ? "Active" : "Inactive") << endl;
        cout << "Readings: " << readingHistory.size() << endl;
        if (!readingHistory.empty()) {
            double sum = 0;
            for (double r : readingHistory) sum += r;
            cout << "Average: " << sum / readingHistory.size() << endl;
        }
    }
    
    ~SmartSensor() override {
        cout << "SmartSensor destroyed: " << deviceName << endl;
    }
};

int main() {
    cout << "=== Smart Home Device - Multiple Inheritance ===" << endl;
    
    cout << "\n1. Creating SmartSensor:" << endl;
    SmartSensor sensor("Living Room Sensor", "HomeWiFi", "Temperature", 85);
    
    cout << "\n2. Setting up device:" << endl;
    sensor.connect();
    sensor.activate();
    
    cout << "\n3. Sending readings:" << endl;
    sensor.sendReading();
    sensor.sendReading();
    sensor.sendReading();
    
    cout << "\n4. Device status:" << endl;
    sensor.checkBattery();
    sensor.displayStats();
    
    cout << "\n5. Testing without WiFi:" << endl;
    sensor.disconnect();
    sensor.sendReading();
    
    cout << "\n6. Reconnecting:" << endl;
    sensor.connect();
    sensor.sendReading();
    
    cout << "\n7. Final status:" << endl;
    sensor.displayStats();
    
    return 0;
}
```

---

## 5. **Multiple Inheritance with Interfaces (Pure Virtual Classes)**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Interface 1: Drawable
class Drawable {
public:
    virtual void draw() const = 0;
    virtual void setColor(const string& color) = 0;
    virtual ~Drawable() = default;
};

// Interface 2: Resizable
class Resizable {
public:
    virtual void resize(double factor) = 0;
    virtual void scale(double factor) = 0;
    virtual ~Resizable() = default;
};

// Interface 3: Movable
class Movable {
public:
    virtual void move(int dx, int dy) = 0;
    virtual void moveTo(int x, int y) = 0;
    virtual ~Movable() = default;
};

// Class implementing multiple interfaces
class Shape : public Drawable, public Resizable, public Movable {
protected:
    string color;
    int x, y;
    
public:
    Shape(int xPos = 0, int yPos = 0, string c = "Black") 
        : x(xPos), y(yPos), color(c) {}
    
    // Drawable implementation
    void setColor(const string& c) override {
        color = c;
        cout << "Color set to " << color << endl;
    }
    
    // Movable implementation
    void move(int dx, int dy) override {
        x += dx;
        y += dy;
        cout << "Moved by (" << dx << ", " << dy << ") to (" << x << ", " << y << ")" << endl;
    }
    
    void moveTo(int newX, int newY) override {
        x = newX;
        y = newY;
        cout << "Moved to (" << x << ", " << y << ")" << endl;
    }
};

class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(double r, int xPos = 0, int yPos = 0, string c = "Black") 
        : Shape(xPos, yPos, c), radius(r) {}
    
    void draw() const override {
        cout << "Drawing Circle at (" << x << ", " << y 
             << ") radius=" << radius << ", color=" << color << endl;
    }
    
    void resize(double factor) override {
        radius *= factor;
        cout << "Circle resized: new radius=" << radius << endl;
    }
    
    void scale(double factor) override {
        resize(factor);
    }
};

class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(double w, double h, int xPos = 0, int yPos = 0, string c = "Black") 
        : Shape(xPos, yPos, c), width(w), height(h) {}
    
    void draw() const override {
        cout << "Drawing Rectangle at (" << x << ", " << y 
             << ") size=" << width << "x" << height << ", color=" << color << endl;
    }
    
    void resize(double factor) override {
        width *= factor;
        height *= factor;
        cout << "Rectangle resized: new size=" << width << "x" << height << endl;
    }
    
    void scale(double factor) override {
        resize(factor);
    }
};

int main() {
    cout << "=== Multiple Inheritance with Interfaces ===" << endl;
    
    cout << "\n1. Creating shapes:" << endl;
    Circle circle(5.0, 10, 20, "Red");
    Rectangle rect(4.0, 6.0, 30, 40, "Blue");
    
    cout << "\n2. Drawing shapes:" << endl;
    circle.draw();
    rect.draw();
    
    cout << "\n3. Moving and resizing Circle:" << endl;
    circle.move(5, 10);
    circle.resize(2.0);
    circle.setColor("Green");
    circle.draw();
    
    cout << "\n4. Moving and resizing Rectangle:" << endl;
    rect.moveTo(100, 100);
    rect.scale(1.5);
    rect.setColor("Yellow");
    rect.draw();
    
    cout << "\n5. Polymorphic container of interfaces:" << endl;
    vector<Drawable*> drawables = {&circle, &rect};
    for (auto d : drawables) {
        d->draw();
    }
    
    return 0;
}
```

---

## 📊 Multiple Inheritance Summary

| Aspect | Description |
|--------|-------------|
| **Syntax** | `class Derived : public Base1, public Base2` |
| **Ambiguity** | Can occur when same member exists in multiple bases |
| **Resolution** | Use scope resolution `Base::member` |
| **Constructor Order** | Base classes in declaration order |
| **Destructor Order** | Reverse of constructor order |
| **Virtual Inheritance** | Solves diamond problem |

---

## ✅ Best Practices

1. **Use multiple inheritance sparingly** - Can increase complexity
2. **Prefer interfaces** (pure virtual classes) for multiple inheritance
3. **Use virtual inheritance** to solve diamond problem
4. **Resolve ambiguity explicitly** using scope resolution
5. **Keep base classes focused** - Single Responsibility Principle
6. **Consider composition** as alternative to multiple inheritance

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Ambiguous member access** | Compiler error | Use scope resolution or override |
| **Diamond problem** | Duplicate base class copies | Use virtual inheritance |
| **Constructor confusion** | Wrong initialization order | Follow declaration order |
| **Slicing** | Loss of derived data | Use pointers/references |

---
---

## Next Step

- Go to [3_Multilevel_Inheritance.md](3_Multilevel_Inheritance.md) to continue with Multilevel Inheritance.
