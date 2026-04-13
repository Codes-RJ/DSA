# Static Members in C++ - Complete Guide

## 📖 Overview

Static members belong to the class itself rather than to individual objects. They are shared across all instances of the class and exist even before any object is created. Static members are useful for maintaining class-level data, implementing singleton patterns, and managing shared resources.

---

## 🎯 Types of Static Members

| Type | Declaration | Storage | Lifetime | Access |
|------|-------------|---------|----------|--------|
| **Static Data Member** | `static int count;` | Class scope | Program lifetime | Via class or object |
| **Static Member Function** | `static void func();` | Class scope | Program lifetime | Via class or object |

---

## 1. **Static Data Members**

### Definition
Static data members are shared across all objects of a class. They are stored in a single memory location and are initialized only once.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Employee {
private:
    string name;
    int id;
    static int nextId;           // Static data member
    static int totalEmployees;   // Static data member
    static const int MAX_ID = 9999;  // Static const integral member (C++98)
    static inline double bonus = 1000.0; // Static inline member (C++17)
    
public:
    Employee(string n) : name(n) {
        if (nextId > MAX_ID) {
            throw runtime_error("Maximum employee limit reached!");
        }
        id = nextId++;
        totalEmployees++;
        cout << "Employee " << name << " created with ID: " << id << endl;
    }
    
    ~Employee() {
        totalEmployees--;
        cout << "Employee " << name << " (ID: " << id << ") removed" << endl;
    }
    
    void display() const {
        cout << "ID: " << id << ", Name: " << name << endl;
    }
    
    // Static member functions to access static data
    static int getTotalEmployees() { return totalEmployees; }
    static int getNextId() { return nextId; }
    static double getBonus() { return bonus; }
    static void setBonus(double b) { bonus = b; }
};

// Definition and initialization of static members
int Employee::nextId = 1000;
int Employee::totalEmployees = 0;
// const int Employee::MAX_ID;  // Already initialized in-class
// double Employee::bonus;      // Already initialized inline (C++17)

int main() {
    cout << "Initial total employees: " << Employee::getTotalEmployees() << endl;
    cout << "Next available ID: " << Employee::getNextId() << endl;
    cout << "Bonus amount: $" << Employee::getBonus() << endl;
    
    cout << "\n--- Creating employees ---\n";
    Employee e1("Alice");
    Employee e2("Bob");
    Employee e3("Charlie");
    
    cout << "\n--- Current status ---\n";
    cout << "Total employees: " << Employee::getTotalEmployees() << endl;
    cout << "Next available ID: " << Employee::getNextId() << endl;
    
    // Changing static member affects all objects
    Employee::setBonus(1500.0);
    cout << "Updated bonus: $" << Employee::getBonus() << endl;
    
    cout << "\n--- Employee details ---\n";
    e1.display();
    e2.display();
    e3.display();
    
    return 0;
}
```

**Output:**
```
Initial total employees: 0
Next available ID: 1000
Bonus amount: $1000

--- Creating employees ---
Employee Alice created with ID: 1000
Employee Bob created with ID: 1001
Employee Charlie created with ID: 1002

--- Current status ---
Total employees: 3
Next available ID: 1003
Updated bonus: $1500

--- Employee details ---
ID: 1000, Name: Alice
ID: 1001, Name: Bob
ID: 1002, Name: Charlie
Employee Charlie (ID: 1002) removed
Employee Bob (ID: 1001) removed
Employee Alice (ID: 1000) removed
```

---

## 2. **Static Member Functions**

### Definition
Static member functions belong to the class and can be called without an object. They can only access static data members and other static functions.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Product {
private:
    int id;
    string name;
    double price;
    
    static vector<Product*> inventory;
    static int nextId;
    static int totalProducts;
    static double totalValue;
    
public:
    Product(string n, double p) : name(n), price(p) {
        id = nextId++;
        totalProducts++;
        totalValue += price;
        inventory.push_back(this);
        cout << "Product " << name << " added (ID: " << id << ")" << endl;
    }
    
    ~Product() {
        totalProducts--;
        totalValue -= price;
        // Remove from inventory
        auto it = find(inventory.begin(), inventory.end(), this);
        if (it != inventory.end()) {
            inventory.erase(it);
        }
        cout << "Product " << name << " removed (ID: " << id << ")" << endl;
    }
    
    void display() const {
        cout << "ID: " << id << ", Name: " << name << ", Price: $" << price << endl;
    }
    
    // Static member functions
    static int getTotalProducts() { return totalProducts; }
    static double getTotalValue() { return totalValue; }
    static double getAveragePrice() {
        if (totalProducts == 0) return 0;
        return totalValue / totalProducts;
    }
    
    static Product* findProduct(int id) {
        for (Product* p : inventory) {
            if (p->id == id) return p;
        }
        return nullptr;
    }
    
    static void displayInventory() {
        cout << "\n=== Inventory ===" << endl;
        cout << "Total Products: " << totalProducts << endl;
        cout << "Total Value: $" << totalValue << endl;
        cout << "Average Price: $" << getAveragePrice() << endl;
        cout << "Products:" << endl;
        for (Product* p : inventory) {
            cout << "  ";
            p->display();
        }
    }
    
    static Product* createProduct(string name, double price) {
        return new Product(name, price);
    }
    
    static void cleanup() {
        for (Product* p : inventory) {
            delete p;
        }
        inventory.clear();
    }
};

// Initialize static members
vector<Product*> Product::inventory;
int Product::nextId = 1;
int Product::totalProducts = 0;
double Product::totalValue = 0.0;

int main() {
    // Static functions called without objects
    cout << "=== Initial State ===" << endl;
    Product::displayInventory();
    
    cout << "\n=== Adding Products ===" << endl;
    Product* p1 = Product::createProduct("Laptop", 999.99);
    Product* p2 = Product::createProduct("Mouse", 29.99);
    Product* p3 = Product::createProduct("Keyboard", 79.99);
    
    Product::displayInventory();
    
    cout << "\n=== Searching ===" << endl;
    Product* found = Product::findProduct(2);
    if (found) {
        cout << "Found: ";
        found->display();
    } else {
        cout << "Product not found" << endl;
    }
    
    cout << "\n=== Cleanup ===" << endl;
    Product::cleanup();
    Product::displayInventory();
    
    return 0;
}
```

**Output:**
```
=== Initial State ===

=== Inventory ===
Total Products: 0
Total Value: $0
Average Price: $0
Products:

=== Adding Products ===
Product Laptop added (ID: 1)
Product Mouse added (ID: 2)
Product Keyboard added (ID: 3)

=== Inventory ===
Total Products: 3
Total Value: $1109.97
Average Price: $369.99
Products:
  ID: 1, Name: Laptop, Price: $999.99
  ID: 2, Name: Mouse, Price: $29.99
  ID: 3, Name: Keyboard, Price: $79.99

=== Searching ===
Found: ID: 2, Name: Mouse, Price: $29.99

=== Cleanup ===
Product Laptop removed (ID: 1)
Product Mouse removed (ID: 2)
Product Keyboard removed (ID: 3)

=== Inventory ===
Total Products: 0
Total Value: $0
Average Price: $0
Products:
```

---

## 3. **Static Const Members**

### Definition
Static const members are compile-time constants that can be initialized inside the class definition for integral types.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

class MathConstants {
public:
    // Static const integral types - can be initialized in-class
    static const int MAX_VALUE = 1000;
    static const int MIN_VALUE = 0;
    static const int DEFAULT_PRECISION = 6;
    
    // Static constexpr (C++11) - more flexible
    static constexpr double PI = 3.14159265358979323846;
    static constexpr double E = 2.71828182845904523536;
    static constexpr double GOLDEN_RATIO = 1.6180339887498948482;
    
    // Static const member - must be defined outside if not integral
    static const string VERSION;
    static const string AUTHOR;
    
    // Static member functions using const members
    static double degreesToRadians(double degrees) {
        return degrees * PI / 180.0;
    }
    
    static double radiansToDegrees(double radians) {
        return radians * 180.0 / PI;
    }
    
    static double circleArea(double radius) {
        return PI * radius * radius;
    }
    
    static double circleCircumference(double radius) {
        return 2 * PI * radius;
    }
    
    static double exponential(double x) {
        return pow(E, x);
    }
};

// Definition of non-integral static const members
const string MathConstants::VERSION = "1.0.0";
const string MathConstants::AUTHOR = "C++ Programmer";

class UnitConverter {
private:
    static constexpr double INCH_TO_CM = 2.54;
    static constexpr double POUND_TO_KG = 0.453592;
    static constexpr double FAHRENHEIT_TO_CELSIUS_OFFSET = 32.0;
    static constexpr double FAHRENHEIT_TO_CELSIUS_RATIO = 5.0 / 9.0;
    
public:
    static double inchesToCm(double inches) {
        return inches * INCH_TO_CM;
    }
    
    static double cmToInches(double cm) {
        return cm / INCH_TO_CM;
    }
    
    static double poundsToKg(double pounds) {
        return pounds * POUND_TO_KG;
    }
    
    static double kgToPounds(double kg) {
        return kg / POUND_TO_KG;
    }
    
    static double fahrenheitToCelsius(double f) {
        return (f - FAHRENHEIT_TO_CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_RATIO;
    }
    
    static double celsiusToFahrenheit(double c) {
        return c / FAHRENHEIT_TO_CELSIUS_RATIO + FAHRENHEIT_TO_CELSIUS_OFFSET;
    }
};

int main() {
    cout << "=== Math Constants ===" << endl;
    cout << "PI = " << MathConstants::PI << endl;
    cout << "E = " << MathConstants::E << endl;
    cout << "Golden Ratio = " << MathConstants::GOLDEN_RATIO << endl;
    cout << "Version: " << MathConstants::VERSION << endl;
    cout << "Author: " << MathConstants::AUTHOR << endl;
    
    cout << "\n=== Circle Calculations ===" << endl;
    double radius = 5.0;
    cout << "Radius = " << radius << endl;
    cout << "Area = " << MathConstants::circleArea(radius) << endl;
    cout << "Circumference = " << MathConstants::circleCircumference(radius) << endl;
    
    cout << "\n=== Angle Conversion ===" << endl;
    double angle = 45.0;
    cout << angle << " degrees = " << MathConstants::degreesToRadians(angle) << " radians" << endl;
    cout << MathConstants::degreesToRadians(angle) << " radians = " 
         << MathConstants::radiansToDegrees(MathConstants::degreesToRadians(angle)) << " degrees" << endl;
    
    cout << "\n=== Unit Conversion ===" << endl;
    cout << "10 inches = " << UnitConverter::inchesToCm(10) << " cm" << endl;
    cout << "20 cm = " << UnitConverter::cmToInches(20) << " inches" << endl;
    cout << "150 pounds = " << UnitConverter::poundsToKg(150) << " kg" << endl;
    cout << "68 kg = " << UnitConverter::kgToPounds(68) << " pounds" << endl;
    cout << "98.6°F = " << UnitConverter::fahrenheitToCelsius(98.6) << "°C" << endl;
    cout << "37°C = " << UnitConverter::celsiusToFahrenheit(37) << "°F" << endl;
    
    return 0;
}
```

**Output:**
```
=== Math Constants ===
PI = 3.14159
E = 2.71828
Golden Ratio = 1.61803
Version: 1.0.0
Author: C++ Programmer

=== Circle Calculations ===
Radius = 5
Area = 78.5398
Circumference = 31.4159

=== Angle Conversion ===
45 degrees = 0.785398 radians
0.785398 radians = 45 degrees

=== Unit Conversion ===
10 inches = 25.4 cm
20 cm = 7.87402 inches
150 pounds = 68.0388 kg
68 kg = 149.914 pounds
98.6°F = 37°C
37°C = 98.6°F
```

---

## 4. **Singleton Pattern Using Static Members**

### Definition
The Singleton pattern ensures a class has only one instance and provides a global access point to it.

```cpp
#include <iostream>
#include <string>
#include <mutex>
using namespace std;

class Logger {
private:
    // Private constructor - prevents direct instantiation
    Logger() {
        cout << "Logger instance created" << endl;
    }
    
    // Private destructor
    ~Logger() {
        cout << "Logger instance destroyed" << endl;
    }
    
    // Delete copy constructor and assignment
    Logger(const Logger&) = delete;
    Logger& operator=(const Logger&) = delete;
    
    // Static pointer to the single instance
    static Logger* instance;
    static mutex mtx;
    
    // Log level
    string logLevel = "INFO";
    
public:
    // Static method to get the single instance
    static Logger* getInstance() {
        if (instance == nullptr) {
            lock_guard<mutex> lock(mtx);
            if (instance == nullptr) {
                instance = new Logger();
            }
        }
        return instance;
    }
    
    // Static method to destroy the instance
    static void destroyInstance() {
        lock_guard<mutex> lock(mtx);
        delete instance;
        instance = nullptr;
    }
    
    // Instance methods
    void setLogLevel(string level) {
        logLevel = level;
    }
    
    void log(const string& message) {
        cout << "[" << logLevel << "] " << message << endl;
    }
    
    void info(const string& message) {
        cout << "[INFO] " << message << endl;
    }
    
    void error(const string& message) {
        cout << "[ERROR] " << message << endl;
    }
    
    void debug(const string& message) {
        if (logLevel == "DEBUG") {
            cout << "[DEBUG] " << message << endl;
        }
    }
};

// Initialize static members
Logger* Logger::instance = nullptr;
mutex Logger::mtx;

class Configuration {
private:
    // Private constructor
    Configuration() {
        cout << "Configuration loaded" << endl;
        loadConfig();
    }
    
    ~Configuration() {
        cout << "Configuration saved" << endl;
        saveConfig();
    }
    
    Configuration(const Configuration&) = delete;
    Configuration& operator=(const Configuration&) = delete;
    
    static Configuration* instance;
    
    string serverAddress = "localhost";
    int port = 8080;
    string databaseUrl = "postgresql://localhost/mydb";
    
    void loadConfig() {
        // Simulate loading from file
        cout << "Loading configuration..." << endl;
    }
    
    void saveConfig() {
        // Simulate saving to file
        cout << "Saving configuration..." << endl;
    }
    
public:
    static Configuration* getInstance() {
        if (instance == nullptr) {
            instance = new Configuration();
        }
        return instance;
    }
    
    static void destroyInstance() {
        delete instance;
        instance = nullptr;
    }
    
    // Getters
    string getServerAddress() const { return serverAddress; }
    int getPort() const { return port; }
    string getDatabaseUrl() const { return databaseUrl; }
    
    // Setters
    void setServerAddress(string addr) { serverAddress = addr; }
    void setPort(int p) { port = p; }
    void setDatabaseUrl(string url) { databaseUrl = url; }
    
    void display() const {
        cout << "Configuration:" << endl;
        cout << "  Server: " << serverAddress << ":" << port << endl;
        cout << "  Database: " << databaseUrl << endl;
    }
};

Configuration* Configuration::instance = nullptr;

int main() {
    // Get logger instance
    Logger* logger = Logger::getInstance();
    logger->info("Application starting");
    
    // Get configuration instance
    Configuration* config = Configuration::getInstance();
    config->display();
    
    // Modify configuration
    config->setPort(9090);
    config->setServerAddress("production.example.com");
    
    logger->info("Configuration updated");
    config->display();
    
    // Set log level
    logger->setLogLevel("DEBUG");
    logger->debug("This is a debug message");
    
    logger->info("Application shutting down");
    
    // Clean up
    Configuration::destroyInstance();
    Logger::destroyInstance();
    
    return 0;
}
```

**Output:**
```
[INFO] Application starting
Configuration loaded
Loading configuration...
Configuration:
  Server: localhost:8080
  Database: postgresql://localhost/mydb
[INFO] Configuration updated
Configuration:
  Server: production.example.com:9090
  Database: postgresql://localhost/mydb
[DEBUG] This is a debug message
[INFO] Application shutting down
Saving configuration...
Configuration saved
Logger instance destroyed
```

---

## 5. **Static Members with Templates**

```cpp
#include <iostream>
#include <string>
using namespace std;

template<typename T>
class Factory {
private:
    static int objectCount;
    static string typeName;
    
public:
    Factory() {
        objectCount++;
        cout << "Created " << typeName << " object #" << objectCount << endl;
    }
    
    ~Factory() {
        cout << "Destroyed " << typeName << " object #" << objectCount << endl;
        objectCount--;
    }
    
    static int getCount() { return objectCount; }
    static void setTypeName(string name) { typeName = name; }
};

// Static member definitions for each template instantiation
template<typename T>
int Factory<T>::objectCount = 0;

template<typename T>
string Factory<T>::typeName = "Unknown";

// Specialization for int
template<>
string Factory<int>::typeName = "Integer";

// Specialization for double
template<>
string Factory<double>::typeName = "Double";

// Specialization for string
template<>
string Factory<string>::typeName = "String";

class Widget {};
class Gadget {};

int main() {
    cout << "=== Integer Factory ===" << endl;
    Factory<int>::setTypeName("Integer");
    Factory<int> i1, i2, i3;
    cout << "Integer count: " << Factory<int>::getCount() << endl;
    
    cout << "\n=== Double Factory ===" << endl;
    Factory<double> d1, d2;
    cout << "Double count: " << Factory<double>::getCount() << endl;
    
    cout << "\n=== String Factory ===" << endl;
    Factory<string> s1, s2, s3, s4;
    cout << "String count: " << Factory<string>::getCount() << endl;
    
    cout << "\n=== Widget Factory ===" << endl;
    Factory<Widget>::setTypeName("Widget");
    Factory<Widget> w1, w2;
    cout << "Widget count: " << Factory<Widget>::getCount() << endl;
    
    cout << "\n=== Gadget Factory ===" << endl;
    Factory<Gadget>::setTypeName("Gadget");
    Factory<Gadget> g1, g2, g3;
    cout << "Gadget count: " << Factory<Gadget>::getCount() << endl;
    
    cout << "\n=== Cleanup (objects destroyed in reverse order) ===" << endl;
    
    return 0;
}
```

---

## 📊 Static Members Summary

| Feature | Static Data Member | Static Member Function |
|---------|-------------------|----------------------|
| **Storage** | One copy for all objects | One copy for all objects |
| **Access** | Class::member or object.member | Class::function() or object.function() |
| **`this` Pointer** | N/A | No `this` pointer |
| **Access to non-static** | No | No |
| **Access to static** | Yes | Yes |
| **Initialization** | Must be defined outside class | No initialization needed |
| **Memory** | Program lifetime | Program lifetime |

---

## ✅ Best Practices

### 1. **Initialize Static Members Properly**
```cpp
class Good {
    static int count;           // Declaration
    static const int MAX = 100; // OK for integral types
    static inline double rate = 0.05; // C++17: inline initialization
};

int Good::count = 0;            // Definition (required)
```

### 2. **Use Static for Class-Level Data**
```cpp
class Logger {
    static ofstream logFile;    // Shared across all instances
    static mutex logMutex;      // Synchronization for all
};
```

### 3. **Use Static Methods for Utilities**
```cpp
class MathUtils {
public:
    static double sin(double x);    // No need for object
    static double cos(double x);
    static double sqrt(double x);
};
```

### 4. **Singleton Pattern with Static Members**
```cpp
class Singleton {
private:
    static Singleton* instance;     // Single instance pointer
    
public:
    static Singleton* getInstance() {
        if (!instance) instance = new Singleton();
        return instance;
    }
};
```

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Not defining static member** | Linker error | Define in .cpp file: `int Class::member = 0;` |
| **Accessing non-static in static** | Compiler error | Static functions only access static members |
| **Static member in header** | Multiple definitions | Use `inline` (C++17) or define in .cpp |
| **Using `this` in static** | Compiler error | `this` not available in static functions |
| **Virtual static functions** | Not possible | Static functions cannot be virtual |

---

## ✅ Key Takeaways

1. **Static data members**: Shared across all objects, initialized once
2. **Static member functions**: Called without objects, no `this` pointer
3. **Static const members**: Compile-time constants (integral types can be initialized in-class)
4. **Singleton pattern**: Common use of static members
5. **Template static members**: Separate instances for each template specialization
6. **Thread safety**: Consider synchronization for static members in multithreaded code

---
---

## Next Step

- Go to [07_Const_Members.md](07_Const_Members.md) to continue with Const Members.
