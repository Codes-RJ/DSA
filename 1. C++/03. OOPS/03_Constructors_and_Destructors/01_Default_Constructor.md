# Default Constructor in C++ - Complete Guide

## 📖 Overview

A default constructor is a constructor that can be called with no arguments. It initializes objects when no initial values are provided. If no constructor is defined, the compiler generates an implicit default constructor. Understanding default constructors is essential for proper object initialization.

---

## 🎯 Types of Default Constructors

| Type | Description | Example |
|------|-------------|---------|
| **Compiler-Generated** | Created automatically when no constructor defined | `ClassName obj;` |
| **User-Defined Default** | Explicitly defined with no parameters | `ClassName() { }` |
| **Defaulted Default (C++11)** | Explicitly request compiler-generated version | `ClassName() = default;` |
| **Deleted Default (C++11)** | Prevent default construction | `ClassName() = delete;` |

---

## 1. **Compiler-Generated Default Constructor**

### Definition
If no constructor is defined, the compiler automatically generates a default constructor that:
- Calls default constructors of base classes
- Calls default constructors of member objects
- Does NOT initialize fundamental types (they have indeterminate values)

```cpp
#include <iostream>
#include <string>
using namespace std;

class NoConstructor {
public:
    int value;           // Will be uninitialized
    string text;         // Will be default-initialized (empty string)
    
    // No constructor defined - compiler generates one
};

class WithMembers {
private:
    int* ptr;            // Will be uninitialized (dangerous!)
    string name;         // Will be default-initialized (empty)
    
public:
    // No constructor - compiler generates
    void display() const {
        cout << "Name: '" << name << "'" << endl;
        cout << "Ptr: " << ptr << " (uninitialized!)" << endl;
    }
};

class Base {
public:
    Base() {
        cout << "Base default constructor called" << endl;
    }
};

class Member {
public:
    Member() {
        cout << "Member default constructor called" << endl;
    }
};

class Derived : public Base {
private:
    Member m;
    int x;               // Uninitialized
    string s;            // Default-initialized
    
public:
    // Compiler-generated default constructor calls Base() and Member()
    void display() const {
        cout << "x = " << x << " (uninitialized!)" << endl;
        cout << "s = '" << s << "'" << endl;
    }
};

int main() {
    cout << "=== Compiler-Generated Default Constructor ===" << endl;
    
    cout << "\n1. Simple class:" << endl;
    NoConstructor obj1;
    cout << "obj1.value = " << obj1.value << " (uninitialized!)" << endl;
    cout << "obj1.text = '" << obj1.text << "'" << endl;
    
    cout << "\n2. Class with members:" << endl;
    WithMembers obj2;
    obj2.display();
    
    cout << "\n3. Inheritance and composition:" << endl;
    Derived d;
    d.display();
    
    return 0;
}
```

**Output:**
```
=== Compiler-Generated Default Constructor ===

1. Simple class:
obj1.value = 0 (uninitialized!)
obj1.text = ''

2. Class with members:
Name: ''
Ptr: 0x7ffc12345678 (uninitialized!)

3. Inheritance and composition:
Base default constructor called
Member default constructor called
x = 0 (uninitialized!)
s = ''
```

---

## 2. **User-Defined Default Constructor**

### Definition
A default constructor explicitly defined by the programmer. It can initialize members to specific values.

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Point {
private:
    double x, y;
    
public:
    // User-defined default constructor
    Point() : x(0.0), y(0.0) {
        cout << "Point default constructor: (" << x << ", " << y << ")" << endl;
    }
    
    // Parameterized constructor
    Point(double xVal, double yVal) : x(xVal), y(yVal) {
        cout << "Point parameterized: (" << x << ", " << y << ")" << endl;
    }
    
    void display() const {
        cout << "(" << x << ", " << y << ")" << endl;
    }
    
    double distanceFromOrigin() const {
        return sqrt(x * x + y * y);
    }
};

class Student {
private:
    string name;
    int rollNumber;
    double marks;
    bool isActive;
    
public:
    // User-defined default constructor
    Student() {
        name = "Unknown";
        rollNumber = 0;
        marks = 0.0;
        isActive = true;
        cout << "Student default constructor called" << endl;
    }
    
    // Parameterized constructor
    Student(string n, int r, double m) {
        name = n;
        rollNumber = r;
        marks = m;
        isActive = true;
        cout << "Student parameterized: " << name << endl;
    }
    
    void display() const {
        cout << "Name: " << name << endl;
        cout << "Roll: " << rollNumber << endl;
        cout << "Marks: " << marks << endl;
        cout << "Active: " << (isActive ? "Yes" : "No") << endl;
    }
};

class Timer {
private:
    int hours;
    int minutes;
    int seconds;
    
public:
    // Default constructor with member initializer list
    Timer() : hours(0), minutes(0), seconds(0) {
        cout << "Timer default: 00:00:00" << endl;
    }
    
    // Parameterized constructor
    Timer(int h, int m, int s) : hours(h), minutes(m), seconds(s) {
        cout << "Timer: " << h << ":" << m << ":" << s << endl;
    }
    
    void display() const {
        cout << hours << ":" << minutes << ":" << seconds << endl;
    }
};

int main() {
    cout << "=== User-Defined Default Constructor ===" << endl;
    
    cout << "\n1. Point class:" << endl;
    Point p1;                    // Default constructor
    Point p2(3, 4);              // Parameterized constructor
    cout << "p1: "; p1.display();
    cout << "p2: "; p2.display();
    cout << "Distance p1: " << p1.distanceFromOrigin() << endl;
    
    cout << "\n2. Student class:" << endl;
    Student s1;                  // Default constructor
    Student s2("Alice", 101, 85.5);  // Parameterized
    s1.display();
    cout << endl;
    s2.display();
    
    cout << "\n3. Timer class:" << endl;
    Timer t1;                    // Default constructor
    Timer t2(10, 30, 45);        // Parameterized
    
    return 0;
}
```

**Output:**
```
=== User-Defined Default Constructor ===

1. Point class:
Point default constructor: (0, 0)
Point parameterized: (3, 4)
p1: (0, 0)
p2: (3, 4)
Distance p1: 0

2. Student class:
Student default constructor called
Student parameterized: Alice
Name: Unknown
Roll: 0
Marks: 0
Active: Yes

Name: Alice
Roll: 101
Marks: 85.5
Active: Yes

3. Timer class:
Timer default: 00:00:00
Timer: 10:30:45
```

---

## 3. **Defaulted Default Constructor (C++11)**

### Definition
The `= default` syntax explicitly requests the compiler to generate the default constructor. Useful when you need the compiler-generated version but have defined other constructors.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Simple {
public:
    int x;
    string s;
    
    // Defaulted default constructor
    Simple() = default;
    
    // Parameterized constructor
    Simple(int val, string str) : x(val), s(str) {}
    
    void display() const {
        cout << "x=" << x << ", s='" << s << "'" << endl;
    }
};

class Resource {
private:
    int* data;
    size_t size;
    
public:
    // Default constructor - initialize to empty state
    Resource() : data(nullptr), size(0) {
        cout << "Resource default: empty" << endl;
    }
    
    // Parameterized constructor
    Resource(size_t n) : size(n) {
        data = new int[size];
        cout << "Resource parameterized: allocated " << size << " ints" << endl;
    }
    
    // Defaulted copy constructor
    Resource(const Resource&) = default;
    
    // Defaulted destructor
    ~Resource() = default;
    
    void display() const {
        cout << "Resource: size=" << size << ", data=" << data << endl;
    }
};

class Logger {
private:
    string prefix;
    static int instanceCount;
    
public:
    // Defaulted default constructor
    Logger() = default;
    
    // Parameterized constructor
    Logger(string p) : prefix(p) {
        instanceCount++;
    }
    
    // Defaulted copy constructor
    Logger(const Logger&) = default;
    
    void log(const string& msg) const {
        if (!prefix.empty()) {
            cout << "[" << prefix << "] " << msg << endl;
        } else {
            cout << msg << endl;
        }
    }
    
    static int getCount() { return instanceCount; }
};

int Logger::instanceCount = 0;

class NonCopyable {
public:
    NonCopyable() = default;
    
    // Delete copy constructor
    NonCopyable(const NonCopyable&) = delete;
    
    // Delete copy assignment
    NonCopyable& operator=(const NonCopyable&) = delete;
    
    // Move constructor is still available
    NonCopyable(NonCopyable&&) = default;
};

int main() {
    cout << "=== Defaulted Default Constructor (C++11) ===" << endl;
    
    cout << "\n1. Simple class with =default:" << endl;
    Simple s1;                    // Uses defaulted constructor
    Simple s2(42, "Hello");       // Parameterized
    cout << "s1: "; s1.display();  // x is uninitialized, s is empty
    cout << "s2: "; s2.display();
    
    cout << "\n2. Resource class with mixed constructors:" << endl;
    Resource r1;                   // Default constructor
    Resource r2(100);              // Parameterized
    r1.display();
    r2.display();
    
    cout << "\n3. Logger with defaulted constructor:" << endl;
    Logger l1;                     // Defaulted default
    Logger l2("App");              // Parameterized
    l1.log("No prefix message");
    l2.log("Application starting");
    cout << "Logger instances: " << Logger::getCount() << endl;
    
    cout << "\n4. Non-copyable class:" << endl;
    NonCopyable nc1;
    // NonCopyable nc2 = nc1;      // Error! Copy constructor deleted
    NonCopyable nc3 = move(nc1);   // OK - move constructor exists
    
    return 0;
}
```

---

## 4. **Deleted Default Constructor (C++11)**

### Definition
The `= delete` syntax prevents default construction of a class. Useful for utility classes that should never be instantiated.

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// Utility class that should never be instantiated
class MathUtils {
public:
    // Delete default constructor
    MathUtils() = delete;
    
    // Only static methods
    static double pi() { return 3.141592653589793; }
    static double square(double x) { return x * x; }
    static double cube(double x) { return x * x * x; }
    static int factorial(int n) {
        if (n <= 1) return 1;
        return n * factorial(n - 1);
    }
};

class Singleton {
private:
    static Singleton* instance;
    string data;
    
    // Private constructor - prevents external instantiation
    Singleton() : data("Singleton Data") {
        cout << "Singleton instance created" << endl;
    }
    
    // Delete copy constructor and assignment
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;
    
public:
    static Singleton* getInstance() {
        if (!instance) {
            instance = new Singleton();
        }
        return instance;
    }
    
    void display() const {
        cout << "Singleton: " << data << endl;
    }
    
    static void destroy() {
        delete instance;
        instance = nullptr;
    }
};

Singleton* Singleton::instance = nullptr;

class AbstractShape {
public:
    // Pure virtual destructor makes class abstract
    virtual ~AbstractShape() = 0;
    
    // Deleted default constructor
    AbstractShape() = delete;
    
    // Parameterized constructor
    AbstractShape(string color) : color(color) {}
    
    virtual double area() const = 0;
    virtual void display() const = 0;
    
protected:
    string color;
};

AbstractShape::~AbstractShape() {}

class Circle : public AbstractShape {
private:
    double radius;
    
public:
    Circle(double r, string c) : AbstractShape(c), radius(r) {}
    
    double area() const override {
        return MathUtils::pi() * radius * radius;
    }
    
    void display() const override {
        cout << "Circle: radius=" << radius << ", color=" << color 
             << ", area=" << area() << endl;
    }
};

class Rectangle : public AbstractShape {
private:
    double width, height;
    
public:
    Rectangle(double w, double h, string c) : AbstractShape(c), width(w), height(h) {}
    
    double area() const override {
        return width * height;
    }
    
    void display() const override {
        cout << "Rectangle: " << width << "x" << height << ", color=" << color 
             << ", area=" << area() << endl;
    }
};

int main() {
    cout << "=== Deleted Default Constructor ===" << endl;
    
    cout << "\n1. MathUtils - cannot be instantiated:" << endl;
    // MathUtils utils;  // Error! Constructor is deleted
    cout << "PI = " << MathUtils::pi() << endl;
    cout << "Square of 5 = " << MathUtils::square(5) << endl;
    cout << "Factorial of 5 = " << MathUtils::factorial(5) << endl;
    
    cout << "\n2. Singleton - private constructor:" << endl;
    // Singleton s;      // Error! Constructor is private
    Singleton* s1 = Singleton::getInstance();
    Singleton* s2 = Singleton::getInstance();
    s1->display();
    cout << "Same instance? " << (s1 == s2 ? "Yes" : "No") << endl;
    Singleton::destroy();
    
    cout << "\n3. Abstract class with deleted default constructor:" << endl;
    // AbstractShape shape;  // Error! Abstract class and deleted constructor
    Circle circle(5, "Red");
    Rectangle rect(4, 6, "Blue");
    circle.display();
    rect.display();
    
    return 0;
}
```

---

## 5. **Default Constructor and Arrays**

### Definition
When creating arrays of objects, each element must be default constructible (unless using aggregate initialization).

```cpp
#include <iostream>
#include <string>
using namespace std;

class DefaultConstructible {
private:
    int id;
    string name;
    
public:
    // Default constructor
    DefaultConstructible() : id(0), name("Default") {
        cout << "DefaultConstructible created: " << name << endl;
    }
    
    // Parameterized constructor
    DefaultConstructible(int i, string n) : id(i), name(n) {
        cout << "Parameterized: " << name << endl;
    }
    
    void display() const {
        cout << "ID: " << id << ", Name: " << name << endl;
    }
};

class NoDefault {
private:
    int value;
    
public:
    // No default constructor - only parameterized
    NoDefault(int v) : value(v) {
        cout << "NoDefault: " << value << endl;
    }
    
    void display() const {
        cout << "Value: " << value << endl;
    }
};

class Container {
private:
    static const int SIZE = 3;
    DefaultConstructible arr1[SIZE];     // OK - default constructor exists
    // NoDefault arr2[SIZE];             // Error! No default constructor
    
public:
    Container() {
        cout << "Container created" << endl;
    }
    
    void display() {
        for (int i = 0; i < SIZE; i++) {
            arr1[i].display();
        }
    }
};

int main() {
    cout << "=== Default Constructor and Arrays ===" << endl;
    
    cout << "\n1. Array of default-constructible objects:" << endl;
    DefaultConstructible arr1[3];  // Each element default constructed
    for (int i = 0; i < 3; i++) {
        arr1[i].display();
    }
    
    cout << "\n2. Array with initialization:" << endl;
    DefaultConstructible arr2[3] = {
        DefaultConstructible(1, "First"),
        DefaultConstructible(2, "Second"),
        DefaultConstructible(3, "Third")
    };
    for (int i = 0; i < 3; i++) {
        arr2[i].display();
    }
    
    cout << "\n3. Container class with array member:" << endl;
    Container c;
    c.display();
    
    cout << "\n4. Dynamic array of objects:" << endl;
    DefaultConstructible* dynArr = new DefaultConstructible[3];
    for (int i = 0; i < 3; i++) {
        dynArr[i].display();
    }
    delete[] dynArr;
    
    cout << "\n5. Vector of objects:" << endl;
    vector<DefaultConstructible> vec(2);  // Creates 2 default objects
    vec.push_back(DefaultConstructible(4, "Fourth"));
    for (const auto& obj : vec) {
        obj.display();
    }
    
    return 0;
}
```

---

## 6. **When Default Constructor is Required**

```cpp
#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Required {
private:
    int data;
    
public:
    // Default constructor
    Required() : data(0) {
        cout << "Default constructor" << endl;
    }
    
    Required(int d) : data(d) {
        cout << "Parameterized: " << d << endl;
    }
    
    void display() const {
        cout << "Data: " << data << endl;
    }
};

class NoDefaultClass {
private:
    int value;
    
public:
    NoDefaultClass(int v) : value(v) {}
    
    void display() const { cout << "Value: " << value << endl; }
};

int main() {
    cout << "=== When Default Constructor is Required ===" << endl;
    
    cout << "\n1. Array allocation:" << endl;
    Required arr1[3];      // Requires default constructor
    // NoDefaultClass arr2[3];  // Error! No default constructor
    
    cout << "\n2. Vector with size:" << endl;
    vector<Required> vec1(3);   // Requires default constructor
    // vector<NoDefaultClass> vec2(3);  // Error! No default constructor
    
    cout << "\n3. Map operator[]:" << endl;
    map<int, Required> m;
    m[1] = Required(100);   // operator[] requires default constructible value
    // map<int, NoDefaultClass> m2;  // operator[] would fail
    
    cout << "\n4. Static array in class:" << endl;
    struct Container {
        Required arr[2];     // Requires default constructor
        // NoDefaultClass arr2[2];  // Error!
    };
    
    cout << "\n5. new[] operator:" << endl;
    Required* dyn = new Required[2];  // Requires default constructor
    delete[] dyn;
    
    cout << "\n6. Templates requiring default construction:" << endl;
    template<typename T>
    class Wrapper {
        T obj;              // Requires default constructor if not initialized
    public:
        Wrapper() : obj() {}  // Default construction required
    };
    
    Wrapper<Required> w1;    // OK
    // Wrapper<NoDefaultClass> w2;  // Error! No default constructor
    
    return 0;
}
```

---

## 📊 Default Constructor Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Initialize objects without arguments |
| **Syntax** | `ClassName();` or `ClassName() = default;` |
| **Compiler Generation** | Generated if no constructor defined |
| **When Required** | Arrays, containers, operator[], templates |
| **Default Initialization** | Leaves fundamental types uninitialized |
| **Zero Initialization** | For static/global objects |

---

## ✅ Best Practices

1. **Always initialize members** in default constructor
2. **Use `= default`** when compiler-generated version is sufficient
3. **Use `= delete`** to prevent default construction when appropriate
4. **Provide default constructor** for classes used in containers
5. **Consider `explicit`** for single-argument constructors
6. **Initialize pointers to nullptr** in default constructor

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Uninitialized members** | Indeterminate values | Initialize all members |
| **Missing default constructor** | Cannot use in arrays/vectors | Provide default constructor |
| **Compiler-generated for pointers** | Dangling pointers | Initialize to nullptr |
| **Implicit conversions** | Unexpected behavior | Use `explicit` keyword |

---

## ✅ Key Takeaways

1. **Default constructor** initializes objects with no arguments
2. **Compiler-generated**: Creates if no constructor defined
3. **User-defined**: Explicitly defined by programmer
4. **`= default`**: Requests compiler-generated version
5. **`= delete`**: Prevents default construction
6. **Required for**: Arrays, vectors, maps, templates
7. **Always initialize**: All members to prevent undefined behavior

---