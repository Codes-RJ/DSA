# 02_Classes_and_Objects/05_Member_Functions.md

# Member Functions in C++ - Complete Guide

## 📖 Overview

Member functions (also called methods) are functions declared within a class that define the behavior of objects. They operate on the data members of the class and can access both private and protected members. Member functions are fundamental to encapsulation and define what operations can be performed on objects.

---

## 🎯 Types of Member Functions

| Type | Description | Access | Example |
|------|-------------|--------|---------|
| **Instance Methods** | Operate on specific objects | Via object | `obj.method()` |
| **Static Methods** | Belong to class, not objects | Via class name | `Class::method()` |
| **Const Methods** | Promise not to modify object | Via const object | `obj.constMethod()` |
| **Virtual Methods** | Support polymorphism | Via base pointer | `base->virtualMethod()` |
| **Inline Methods** | Expanded at compile time | Same as normal | Small functions in header |

---

## 1. **Instance Member Functions**

### Definition
Instance member functions operate on a specific object and have access to the `this` pointer. They can access and modify the object's data members.

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Circle {
private:
    double radius;
    string color;
    
public:
    // Constructor
    Circle(double r, string c) : radius(r), color(c) {}
    
    // Instance member functions
    double area() const {
        return 3.14159 * radius * radius;
    }
    
    double circumference() const {
        return 2 * 3.14159 * radius;
    }
    
    void setRadius(double r) {
        if (r > 0) {
            radius = r;
        }
    }
    
    void setColor(string c) {
        color = c;
    }
    
    void display() const {
        cout << "Circle: radius=" << radius 
             << ", color=" << color 
             << ", area=" << area() 
             << ", circumference=" << circumference() << endl;
    }
    
    // Function returning reference for chaining
    Circle& scale(double factor) {
        radius *= factor;
        return *this;  // Return reference to current object
    }
};

int main() {
    Circle c1(5.0, "Red");
    Circle c2(3.0, "Blue");
    
    c1.display();
    c2.display();
    
    c1.setRadius(7.0);
    c1.setColor("Green");
    c1.display();
    
    // Method chaining (using returned reference)
    c2.scale(2.0).setColor("Purple");
    c2.display();
    
    return 0;
}
```

**Output:**
```
Circle: radius=5, color=Red, area=78.5398, circumference=31.4159
Circle: radius=3, color=Blue, area=28.2743, circumference=18.8496
Circle: radius=7, color=Green, area=153.938, circumference=43.9823
Circle: radius=6, color=Purple, area=113.097, circumference=37.6991
```

---

## 2. **The `this` Pointer**

### Definition
`this` is an implicit pointer available in every non-static member function. It points to the current object and is used to resolve name conflicts and enable method chaining.

```cpp
#include <iostream>
using namespace std;

class Employee {
private:
    string name;
    int id;
    double salary;
    
public:
    // Using 'this' to resolve parameter-member name conflict
    Employee(string name, int id, double salary) {
        this->name = name;      // this->name refers to member, 'name' is parameter
        this->id = id;
        this->salary = salary;
    }
    
    // Returning *this for chaining
    Employee& setName(string name) {
        this->name = name;
        return *this;
    }
    
    Employee& setId(int id) {
        this->id = id;
        return *this;
    }
    
    Employee& setSalary(double salary) {
        this->salary = salary;
        return *this;
    }
    
    // Passing current object to another function
    void compare(const Employee& other) const {
        cout << "Comparing " << this->name << " with " << other.name << endl;
        if (this->salary > other.salary) {
            cout << this->name << " has higher salary" << endl;
        } else if (this->salary < other.salary) {
            cout << other.name << " has higher salary" << endl;
        } else {
            cout << "Equal salaries" << endl;
        }
    }
    
    void display() const {
        cout << "ID: " << id << ", Name: " << name << ", Salary: $" << salary << endl;
    }
};

int main() {
    Employee e1("Alice", 101, 75000);
    Employee e2("Bob", 102, 85000);
    
    e1.display();
    e2.display();
    
    e1.compare(e2);
    
    // Method chaining using returned *this
    e1.setName("Alicia").setSalary(80000);
    e1.display();
    
    return 0;
}
```

**Output:**
```
ID: 101, Name: Alice, Salary: $75000
ID: 102, Name: Bob, Salary: $85000
Comparing Alice with Bob
Bob has higher salary
ID: 101, Name: Alicia, Salary: $80000
```

---

## 3. **Const Member Functions**

### Definition
Const member functions promise not to modify the object's data members. They can be called on const objects and are essential for const correctness.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Rectangle {
private:
    double width;
    double height;
    mutable int accessCount;  // mutable: can be modified in const functions
    
public:
    Rectangle(double w, double h) : width(w), height(h), accessCount(0) {}
    
    // Const member functions - cannot modify non-mutable members
    double area() const {
        accessCount++;  // ✓ OK - mutable member
        // width = 10;  // ✗ Error - cannot modify in const function
        return width * height;
    }
    
    double perimeter() const {
        return 2 * (width + height);
    }
    
    double getWidth() const { return width; }
    double getHeight() const { return height; }
    
    int getAccessCount() const { return accessCount; }
    
    // Non-const member function - can modify
    void scale(double factor) {
        width *= factor;
        height *= factor;
    }
    
    void setWidth(double w) {
        width = w;
    }
    
    void display() const {
        cout << "Rectangle: " << width << " x " << height 
             << ", Area: " << area() << ", Perimeter: " << perimeter() << endl;
    }
};

int main() {
    Rectangle rect1(10, 5);
    const Rectangle rect2(7, 3);  // Const object
    
    // Both can call const member functions
    rect1.display();
    rect2.display();
    
    cout << "rect1 area: " << rect1.area() << endl;
    cout << "rect2 area: " << rect2.area() << endl;
    
    // Non-const object can call non-const functions
    rect1.scale(2);
    rect1.setWidth(20);
    rect1.display();
    
    // Const object cannot call non-const functions
    // rect2.scale(2);    // ✗ Error!
    // rect2.setWidth(15); // ✗ Error!
    
    cout << "Access count for rect1: " << rect1.getAccessCount() << endl;
    cout << "Access count for rect2: " << rect2.getAccessCount() << endl;
    
    return 0;
}
```

**Output:**
```
Rectangle: 10 x 5, Area: 50, Perimeter: 30
Rectangle: 7 x 3, Area: 21, Perimeter: 20
rect1 area: 50
rect2 area: 21
Rectangle: 20 x 10, Area: 200, Perimeter: 60
Access count for rect1: 3
Access count for rect2: 2
```

---

## 4. **Inline Member Functions**

### Definition
Inline functions are expanded at the point of call, potentially eliminating function call overhead. They are defined inside the class definition or with the `inline` keyword.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Vector {
private:
    double x, y;
    
public:
    // Inline member functions (defined inside class)
    Vector(double x = 0, double y = 0) : x(x), y(y) {}
    
    // Inline getters - defined inside class
    double getX() const { return x; }
    double getY() const { return y; }
    
    // Inline operators
    Vector operator+(const Vector& other) const {
        return Vector(x + other.x, y + other.y);
    }
    
    // Inline function for simple operations
    double magnitude() const {
        return sqrt(x * x + y * y);
    }
};

// Inline function defined outside class
inline double dotProduct(const Vector& a, const Vector& b) {
    return a.getX() * b.getX() + a.getY() * b.getY();
}

class MathUtils {
public:
    // Large function - not inline (defined outside)
    static double complexCalculation(double x);
    
    // Small function - inline
    static inline int square(int x) { return x * x; }
    
    // Inline with default behavior
    static inline int cube(int x) { return x * x * x; }
};

// Non-inline function definition
double MathUtils::complexCalculation(double x) {
    // Complex calculations that shouldn't be inlined
    double result = 0;
    for (int i = 0; i < 1000; i++) {
        result += sin(x * i) * cos(x * i);
    }
    return result;
}

int main() {
    Vector v1(3, 4);
    Vector v2(1, 2);
    
    // Inline function calls
    cout << "v1 magnitude: " << v1.magnitude() << endl;
    cout << "v1 + v2: (" << (v1 + v2).getX() << ", " << (v1 + v2).getY() << ")" << endl;
    cout << "Dot product: " << dotProduct(v1, v2) << endl;
    
    cout << "Square of 5: " << MathUtils::square(5) << endl;
    cout << "Cube of 3: " << MathUtils::cube(3) << endl;
    
    return 0;
}
```

---

## 5. **Static Member Functions**

### Definition
Static member functions belong to the class rather than individual objects. They can only access static data members and cannot use the `this` pointer.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Student {
private:
    string name;
    int rollNumber;
    double marks;
    
    static int totalStudents;      // Static data member
    static double totalMarks;      // Static data member
    static vector<Student*> allStudents;  // Static container
    
public:
    Student(string n, double m) : name(n), marks(m) {
        rollNumber = ++totalStudents;
        totalMarks += marks;
        allStudents.push_back(this);
        cout << "Student " << name << " enrolled. Roll No: " << rollNumber << endl;
    }
    
    ~Student() {
        totalMarks -= marks;
        totalStudents--;
        // Remove from vector (simplified - not removing from vector here)
        cout << "Student " << name << " removed." << endl;
    }
    
    // Static member functions
    static int getTotalStudents() {
        return totalStudents;
    }
    
    static double getAverageMarks() {
        if (totalStudents == 0) return 0;
        return totalMarks / totalStudents;
    }
    
    static void displayStatistics() {
        cout << "\n=== Statistics ===" << endl;
        cout << "Total Students: " << totalStudents << endl;
        cout << "Total Marks: " << totalMarks << endl;
        cout << "Average Marks: " << getAverageMarks() << endl;
    }
    
    static Student* findStudent(int rollNumber) {
        for (Student* s : allStudents) {
            if (s->rollNumber == rollNumber) {
                return s;
            }
        }
        return nullptr;
    }
    
    // Instance method
    void display() const {
        cout << "Roll No: " << rollNumber << ", Name: " << name << ", Marks: " << marks << endl;
    }
};

// Initialize static members
int Student::totalStudents = 0;
double Student::totalMarks = 0;
vector<Student*> Student::allStudents;

int main() {
    // Static methods called without object
    Student::displayStatistics();
    
    Student s1("Alice", 85.5);
    Student s2("Bob", 92.0);
    Student s3("Charlie", 78.5);
    Student s4("Diana", 95.0);
    
    Student::displayStatistics();
    
    // Find student by roll number
    Student* found = Student::findStudent(3);
    if (found) {
        cout << "\nFound student: ";
        found->display();
    }
    
    return 0;
}
```

**Output:**
```
=== Statistics ===
Total Students: 0
Total Marks: 0
Average Marks: 0
Student Alice enrolled. Roll No: 1
Student Bob enrolled. Roll No: 2
Student Charlie enrolled. Roll No: 3
Student Diana enrolled. Roll No: 4

=== Statistics ===
Total Students: 4
Total Marks: 351
Average Marks: 87.75

Found student: Roll No: 3, Name: Charlie, Marks: 78.5
Student Diana removed.
Student Charlie removed.
Student Bob removed.
Student Alice removed.
```

---

## 6. **Virtual Member Functions**

### Definition
Virtual functions enable runtime polymorphism. They allow derived classes to override base class implementations. (Detailed in Polymorphism section)

```cpp
#include <iostream>
#include <vector>
#include <memory>
using namespace std;

// Base class
class Animal {
protected:
    string name;
    
public:
    Animal(string n) : name(n) {}
    
    // Virtual destructor - essential for polymorphic deletion
    virtual ~Animal() {}
    
    // Virtual function
    virtual void speak() const {
        cout << name << " makes a sound" << endl;
    }
    
    // Pure virtual function (makes Animal abstract)
    virtual void move() const = 0;
    
    void display() const {
        cout << "Animal: " << name << endl;
    }
};

// Derived class 1
class Dog : public Animal {
private:
    string breed;
    
public:
    Dog(string n, string b) : Animal(n), breed(b) {}
    
    // Override virtual function
    void speak() const override {
        cout << name << " says: Woof! Woof!" << endl;
    }
    
    void move() const override {
        cout << name << " runs on four legs" << endl;
    }
    
    void wagTail() const {
        cout << name << " wags tail" << endl;
    }
};

// Derived class 2
class Bird : public Animal {
public:
    Bird(string n) : Animal(n) {}
    
    void speak() const override {
        cout << name << " says: Chirp! Chirp!" << endl;
    }
    
    void move() const override {
        cout << name << " flies in the sky" << endl;
    }
};

// Derived class 3
class Fish : public Animal {
public:
    Fish(string n) : Animal(n) {}
    
    void speak() const override {
        cout << name << " says: ... (silence)" << endl;
    }
    
    void move() const override {
        cout << name << " swims in water" << endl;
    }
};

int main() {
    // Polymorphic container
    vector<unique_ptr<Animal>> animals;
    
    animals.push_back(make_unique<Dog>("Buddy", "Golden Retriever"));
    animals.push_back(make_unique<Bird>("Tweety"));
    animals.push_back(make_unique<Fish>("Nemo"));
    
    // Polymorphic behavior
    for (const auto& animal : animals) {
        animal->speak();    // Calls appropriate derived class method
        animal->move();     // Calls appropriate derived class method
        cout << endl;
    }
    
    // Can't create Animal object (pure virtual function)
    // Animal a("Unknown");  // Error! Abstract class
    
    return 0;
}
```

**Output:**
```
Buddy says: Woof! Woof!
Buddy runs on four legs

Tweety says: Chirp! Chirp!
Tweety flies in the sky

Nemo says: ... (silence)
Nemo swims in water
```

---

## 7. **Friend Functions**

### Definition
Friend functions are not member functions but can access private and protected members of a class. They are declared with the `friend` keyword.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Complex {
private:
    double real;
    double imag;
    
public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}
    
    void display() const {
        cout << real << " + " << imag << "i" << endl;
    }
    
    // Friend function declarations
    friend Complex operator+(const Complex& a, const Complex& b);
    friend ostream& operator<<(ostream& os, const Complex& c);
    friend class ComplexCalculator;  // Friend class
};

// Friend function definition
Complex operator+(const Complex& a, const Complex& b) {
    // Can access private members
    return Complex(a.real + b.real, a.imag + b.imag);
}

// Friend function for output streaming
ostream& operator<<(ostream& os, const Complex& c) {
    os << c.real;
    if (c.imag >= 0) os << " + " << c.imag << "i";
    else os << " - " << -c.imag << "i";
    return os;
}

// Friend class
class ComplexCalculator {
public:
    static Complex multiply(const Complex& a, const Complex& b) {
        // Can access private members of Complex
        return Complex(
            a.real * b.real - a.imag * b.imag,
            a.real * b.imag + a.imag * b.real
        );
    }
    
    static double magnitude(const Complex& c) {
        return sqrt(c.real * c.real + c.imag * c.imag);
    }
};

class Box {
private:
    double length, width, height;
    
public:
    Box(double l, double w, double h) : length(l), width(w), height(h) {}
    
    // Friend function - can access private members
    friend double calculateVolume(const Box& b);
    
    // Friend function - can be declared in multiple classes
    friend bool operator==(const Box& a, const Box& b);
};

double calculateVolume(const Box& b) {
    return b.length * b.width * b.height;
}

bool operator==(const Box& a, const Box& b) {
    return a.length == b.length && a.width == b.width && a.height == b.height;
}

int main() {
    Complex c1(3, 4);
    Complex c2(1, -2);
    
    // Using friend operators
    Complex c3 = c1 + c2;
    cout << "c1: " << c1 << endl;
    cout << "c2: " << c2 << endl;
    cout << "c1 + c2: " << c3 << endl;
    
    // Using friend class
    Complex c4 = ComplexCalculator::multiply(c1, c2);
    cout << "c1 * c2: " << c4 << endl;
    cout << "|c1|: " << ComplexCalculator::magnitude(c1) << endl;
    
    // Using friend function
    Box box1(10, 5, 3);
    Box box2(10, 5, 3);
    Box box3(8, 6, 4);
    
    cout << "Volume of box1: " << calculateVolume(box1) << endl;
    cout << "box1 == box2: " << (box1 == box2 ? "Yes" : "No") << endl;
    cout << "box1 == box3: " << (box1 == box3 ? "Yes" : "No") << endl;
    
    return 0;
}
```

**Output:**
```
c1: 3 + 4i
c2: 1 - 2i
c1 + c2: 4 + 2i
c1 * c2: 11 - 2i
|c1|: 5
Volume of box1: 150
box1 == box2: Yes
box1 == box3: No
```

---

## 📊 Member Functions Summary

| Type | Declaration | Access | `this` | Static | Overridable |
|------|-------------|--------|--------|--------|-------------|
| Instance | `void func();` | Via object | Yes | No | Yes (virtual) |
| Static | `static void func();` | Via class | No | Yes | No |
| Const | `void func() const;` | Via const object | Const pointer | No | Yes |
| Virtual | `virtual void func();` | Via pointer | Yes | No | Yes |
| Inline | `inline void func();` | Same as instance | Yes | No | Yes |
| Friend | `friend void func();` | Direct | No | No | No |

---

## ✅ Best Practices

### 1. **Keep Member Functions Small and Focused**
```cpp
class Good {
public:
    void setName(string n) { name = n; }  // ✓ Single responsibility
    void setAge(int a) { age = a; }       // ✓ Single responsibility
    void display() const;                 // ✓ Single responsibility
};
```

### 2. **Use Const Correctness**
```cpp
class Data {
private:
    int value;
    
public:
    int getValue() const { return value; }     // ✓ Doesn't modify
    void setValue(int v) { value = v; }        // ✓ Modifies
    void update() { value++; }                 // ✓ Modifies
};
```

### 3. **Prefer Inline for Small Functions**
```cpp
class Point {
public:
    // ✓ Good for small, frequently called functions
    int getX() const { return x; }
    int getY() const { return y; }
    
    // ✗ Avoid inline for large functions
    void complexAlgorithm();  // Define in .cpp file
};
```

### 4. **Return *this for Method Chaining**
```cpp
class Builder {
public:
    Builder& setOption1(int val) {
        opt1 = val;
        return *this;  // Enable chaining
    }
    
    Builder& setOption2(string val) {
        opt2 = val;
        return *this;
    }
};

// Usage
Builder b;
b.setOption1(10).setOption2("test");
```

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Forgetting const** | Can't call on const objects | Mark methods that don't modify as const |
| **Modifying in const method** | Compiler error | Use `mutable` for cache/logging |
| **Calling virtual in constructor** | Unexpected behavior | Avoid virtual calls in constructor/destructor |
| **Static function accessing non-static** | Compiler error | Static functions can only access static members |
| **Friend overuse** | Breaks encapsulation | Use sparingly for operators, streams |

---

## ✅ Key Takeaways

1. **Instance methods**: Operate on objects, have `this` pointer
2. **Const methods**: Promise not to modify object, callable on const objects
3. **Static methods**: Belong to class, no `this`, access only static members
4. **Virtual methods**: Enable polymorphism, overridden in derived classes
5. **Inline methods**: Reduce call overhead, best for small functions
6. **Friend functions**: Access private members, use sparingly
7. **Method chaining**: Return `*this` for fluent interfaces

---