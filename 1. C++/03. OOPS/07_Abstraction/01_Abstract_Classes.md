# Abstract Classes in C++ - Complete Guide

## 📖 Overview

Abstract classes are classes that cannot be instantiated and are designed to serve as base classes for other classes. They contain at least one pure virtual function and provide a common interface that derived classes must implement. Abstract classes are fundamental to achieving abstraction in C++.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Abstract Class** | Class with at least one pure virtual function |
| **Pure Virtual Function** | Virtual function with `= 0` syntax |
| **Concrete Class** | Class that overrides all pure virtual functions |
| **Interface** | Abstract class with only pure virtual functions |
| **Partial Implementation** | Abstract class with some implemented methods |

---

## 1. **Basic Abstract Class**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// Abstract class - cannot be instantiated
class Shape {
protected:
    string color;
    
public:
    Shape(string c) : color(c) {}
    
    // Pure virtual functions - must be overridden
    virtual double area() const = 0;
    virtual double perimeter() const = 0;
    virtual void draw() const = 0;
    
    // Concrete method - can be used by derived classes
    string getColor() const { return color; }
    void setColor(string c) { color = c; }
    
    // Virtual destructor
    virtual ~Shape() {
        cout << "Shape destructor" << endl;
    }
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
    cout << "=== Basic Abstract Class ===" << endl;
    
    // Shape s("Red");  // Error! Cannot instantiate abstract class
    
    Circle circle("Red", 5.0);
    Rectangle rect("Blue", 4.0, 6.0);
    
    cout << "\n1. Using concrete objects:" << endl;
    circle.draw();
    cout << "Area: " << circle.area() << ", Perimeter: " << circle.perimeter() << endl;
    
    rect.draw();
    cout << "Area: " << rect.area() << ", Perimeter: " << rect.perimeter() << endl;
    
    cout << "\n2. Polymorphic behavior:" << endl;
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
=== Basic Abstract Class ===

1. Using concrete objects:
Drawing Red circle with radius 5
Area: 78.5398, Perimeter: 31.4159
Drawing Blue rectangle 4x6
Area: 24, Perimeter: 20

2. Polymorphic behavior:
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

## 2. **Abstract Class with Partial Implementation**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Abstract class with partial implementation
class Animal {
protected:
    string name;
    int age;
    
public:
    Animal(string n, int a) : name(n), age(a) {}
    
    // Pure virtual functions - must be overridden
    virtual void speak() const = 0;
    virtual void move() const = 0;
    
    // Concrete methods - common to all animals
    void eat() const {
        cout << name << " is eating" << endl;
    }
    
    void sleep() const {
        cout << name << " is sleeping" << endl;
    }
    
    // Template method pattern - uses pure virtual functions
    void performDailyRoutine() const {
        wakeUp();
        eat();
        move();
        speak();
        sleep();
    }
    
    virtual void wakeUp() const {
        cout << name << " wakes up" << endl;
    }
    
    virtual ~Animal() {
        cout << "Animal destructor: " << name << endl;
    }
};

class Dog : public Animal {
private:
    string breed;
    
public:
    Dog(string n, int a, string b) : Animal(n, a), breed(b) {}
    
    void speak() const override {
        cout << name << " barks: Woof! Woof!" << endl;
    }
    
    void move() const override {
        cout << name << " runs on four legs" << endl;
    }
    
    void wakeUp() const override {
        cout << name << " jumps out of bed excitedly" << endl;
    }
    
    ~Dog() override {
        cout << "Dog destructor: " << name << endl;
    }
};

class Cat : public Animal {
public:
    Cat(string n, int a) : Animal(n, a) {}
    
    void speak() const override {
        cout << name << " meows: Meow! Meow!" << endl;
    }
    
    void move() const override {
        cout << name << " walks silently" << endl;
    }
    
    void wakeUp() const override {
        cout << name << " stretches lazily" << endl;
    }
    
    ~Cat() override {
        cout << "Cat destructor: " << name << endl;
    }
};

int main() {
    cout << "=== Abstract Class with Partial Implementation ===" << endl;
    
    Dog dog("Buddy", 3, "Golden Retriever");
    Cat cat("Whiskers", 2);
    
    cout << "\n1. Dog's daily routine:" << endl;
    dog.performDailyRoutine();
    
    cout << "\n2. Cat's daily routine:" << endl;
    cat.performDailyRoutine();
    
    cout << "\n3. Polymorphic container:" << endl;
    Animal* animals[] = {&dog, &cat};
    
    for (auto animal : animals) {
        animal->speak();
        animal->move();
    }
    
    return 0;
}
```

**Output:**
```
=== Abstract Class with Partial Implementation ===

1. Dog's daily routine:
Buddy jumps out of bed excitedly
Buddy is eating
Buddy runs on four legs
Buddy barks: Woof! Woof!
Buddy is sleeping

2. Cat's daily routine:
Whiskers stretches lazily
Whiskers is eating
Whiskers walks silently
Whiskers meows: Meow! Meow!
Whiskers is sleeping

3. Polymorphic container:
Buddy barks: Woof! Woof!
Buddy runs on four legs
Whiskers meows: Meow! Meow!
Whiskers walks silently
Dog destructor: Buddy
Animal destructor: Buddy
Cat destructor: Whiskers
Animal destructor: Whiskers
```

---

## 3. **Abstract Class with Pure Virtual Destructor**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// Abstract class with pure virtual destructor
class Resource {
public:
    virtual void use() = 0;
    
    // Pure virtual destructor - makes class abstract
    virtual ~Resource() = 0;
};

// Pure virtual destructor MUST have a body
Resource::~Resource() {
    cout << "Resource base destructor" << endl;
}

class FileResource : public Resource {
private:
    string filename;
    
public:
    FileResource(string name) : filename(name) {
        cout << "FileResource created: " << filename << endl;
    }
    
    void use() override {
        cout << "Using file: " << filename << endl;
    }
    
    ~FileResource() override {
        cout << "FileResource destroyed: " << filename << endl;
    }
};

class MemoryResource : public Resource {
private:
    size_t size;
    
public:
    MemoryResource(size_t s) : size(s) {
        cout << "MemoryResource allocated: " << size << " bytes" << endl;
    }
    
    void use() override {
        cout << "Using memory block of " << size << " bytes" << endl;
    }
    
    ~MemoryResource() override {
        cout << "MemoryResource freed: " << size << " bytes" << endl;
    }
};

int main() {
    cout << "=== Abstract Class with Pure Virtual Destructor ===" << endl;
    
    // Resource r;  // Error! Cannot instantiate abstract class
    
    {
        unique_ptr<Resource> r1 = make_unique<FileResource>("data.txt");
        unique_ptr<Resource> r2 = make_unique<MemoryResource>(1024);
        
        cout << "\nUsing resources:" << endl;
        r1->use();
        r2->use();
        
        cout << "\nResources will be destroyed automatically:" << endl;
    }  // Destructors called here
    
    cout << "\nNote: Pure virtual destructor requires a body!" << endl;
    
    return 0;
}
```

**Output:**
```
=== Abstract Class with Pure Virtual Destructor ===
FileResource created: data.txt
MemoryResource allocated: 1024 bytes

Using resources:
Using file: data.txt
Using memory block of 1024 bytes

Resources will be destroyed automatically:
FileResource destroyed: data.txt
Resource base destructor
MemoryResource freed: 1024 bytes
Resource base destructor

Note: Pure virtual destructor requires a body!
```

---

## 4. **Abstract Class with Factory Method**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <map>
using namespace std;

// Abstract product
class Document {
protected:
    string title;
    string content;
    
public:
    Document(string t) : title(t), content("") {}
    
    virtual void addContent(const string& text) = 0;
    virtual void display() const = 0;
    virtual void save() const = 0;
    virtual ~Document() = default;
    
    string getTitle() const { return title; }
};

// Concrete product 1
class TextDocument : public Document {
public:
    TextDocument(string t) : Document(t) {}
    
    void addContent(const string& text) override {
        content += text;
        cout << "Added text to " << title << endl;
    }
    
    void display() const override {
        cout << "\n=== Text Document: " << title << " ===" << endl;
        cout << content << endl;
    }
    
    void save() const override {
        cout << "Saving text document: " << title << ".txt" << endl;
    }
};

// Concrete product 2
class HTMLDocument : public Document {
public:
    HTMLDocument(string t) : Document(t) {}
    
    void addContent(const string& text) override {
        content += "<p>" + text + "</p>\n";
        cout << "Added HTML paragraph to " << title << endl;
    }
    
    void display() const override {
        cout << "\n=== HTML Document: " << title << " ===" << endl;
        cout << "<html><body>\n" << content << "</body></html>" << endl;
    }
    
    void save() const override {
        cout << "Saving HTML document: " << title << ".html" << endl;
    }
};

// Abstract factory
class DocumentFactory {
public:
    virtual unique_ptr<Document> createDocument(const string& title) = 0;
    virtual ~DocumentFactory() = default;
};

// Concrete factory 1
class TextDocumentFactory : public DocumentFactory {
public:
    unique_ptr<Document> createDocument(const string& title) override {
        return make_unique<TextDocument>(title);
    }
};

// Concrete factory 2
class HTMLDocumentFactory : public DocumentFactory {
public:
    unique_ptr<Document> createDocument(const string& title) override {
        return make_unique<HTMLDocument>(title);
    }
};

class DocumentEditor {
private:
    unique_ptr<Document> doc;
    
public:
    DocumentEditor(DocumentFactory& factory, const string& title) {
        doc = factory.createDocument(title);
        cout << "Created new document: " << title << endl;
    }
    
    void edit(const string& text) {
        doc->addContent(text);
    }
    
    void display() const {
        doc->display();
    }
    
    void save() const {
        doc->save();
    }
};

int main() {
    cout << "=== Abstract Class with Factory Method ===" << endl;
    
    TextDocumentFactory textFactory;
    HTMLDocumentFactory htmlFactory;
    
    cout << "\n1. Creating Text Document:" << endl;
    DocumentEditor textEditor(textFactory, "MyNotes");
    textEditor.edit("This is my first note.");
    textEditor.edit("Object-Oriented Programming is great!");
    textEditor.display();
    textEditor.save();
    
    cout << "\n2. Creating HTML Document:" << endl;
    DocumentEditor htmlEditor(htmlFactory, "WebPage");
    htmlEditor.edit("Welcome to my website");
    htmlEditor.edit("Learn C++ programming");
    htmlEditor.display();
    htmlEditor.save();
    
    return 0;
}
```

---

## 5. **Abstract Class with Multiple Levels**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Level 1: Abstract base class
class Vehicle {
protected:
    string brand;
    int year;
    
public:
    Vehicle(string b, int y) : brand(b), year(y) {}
    
    virtual void start() = 0;
    virtual void stop() = 0;
    virtual void display() const = 0;
    
    virtual ~Vehicle() = default;
    
    string getBrand() const { return brand; }
};

// Level 2: Partially abstract class
class MotorVehicle : public Vehicle {
protected:
    int engineCC;
    string fuelType;
    
public:
    MotorVehicle(string b, int y, int cc, string fuel) 
        : Vehicle(b, y), engineCC(cc), fuelType(fuel) {}
    
    // start() is still pure virtual (not overridden)
    // stop() is still pure virtual (not overridden)
    
    virtual void refuel() = 0;
    
    void display() const override {
        cout << "Brand: " << brand << ", Year: " << year 
             << ", Engine: " << engineCC << "cc, Fuel: " << fuelType << endl;
    }
};

// Level 3: Concrete class
class Car : public MotorVehicle {
private:
    int doors;
    string transmission;
    
public:
    Car(string b, int y, int cc, string fuel, int d, string trans)
        : MotorVehicle(b, y, cc, fuel), doors(d), transmission(trans) {}
    
    void start() override {
        cout << brand << " car starting with ignition key" << endl;
    }
    
    void stop() override {
        cout << brand << " car applying brakes" << endl;
    }
    
    void refuel() override {
        cout << brand << " car refueling with " << fuelType << endl;
    }
    
    void display() const override {
        MotorVehicle::display();
        cout << "  Doors: " << doors << ", Transmission: " << transmission << endl;
    }
    
    void honk() {
        cout << brand << " car honks: Beep! Beep!" << endl;
    }
};

// Level 3: Another concrete class
class Motorcycle : public MotorVehicle {
private:
    bool hasSidecar;
    
public:
    Motorcycle(string b, int y, int cc, string fuel, bool sidecar)
        : MotorVehicle(b, y, cc, fuel), hasSidecar(sidecar) {}
    
    void start() override {
        cout << brand << " motorcycle kick-starting" << endl;
    }
    
    void stop() override {
        cout << brand << " motorcycle applying hand brakes" << endl;
    }
    
    void refuel() override {
        cout << brand << " motorcycle refueling with " << fuelType << endl;
    }
    
    void display() const override {
        MotorVehicle::display();
        cout << "  Sidecar: " << (hasSidecar ? "Yes" : "No") << endl;
    }
    
    void wheelie() {
        cout << brand << " motorcycle doing a wheelie!" << endl;
    }
};

int main() {
    cout << "=== Abstract Class with Multiple Levels ===" << endl;
    
    Car car("Toyota", 2022, 2000, "Petrol", 4, "Automatic");
    Motorcycle bike("Harley", 2021, 1200, "Petrol", false);
    
    cout << "\n1. Car behavior:" << endl;
    car.display();
    car.start();
    car.refuel();
    car.honk();
    car.stop();
    
    cout << "\n2. Motorcycle behavior:" << endl;
    bike.display();
    bike.start();
    bike.refuel();
    bike.wheelie();
    bike.stop();
    
    cout << "\n3. Polymorphic container:" << endl;
    vector<unique_ptr<Vehicle>> vehicles;
    vehicles.push_back(make_unique<Car>(car));
    vehicles.push_back(make_unique<Motorcycle>(bike));
    
    for (const auto& v : vehicles) {
        v->display();
        v->start();
        v->stop();
        cout << endl;
    }
    
    return 0;
}
```

---

## 📊 Abstract Classes Summary

| Aspect | Description |
|--------|-------------|
| **Definition** | Class with at least one pure virtual function |
| **Instantiation** | Cannot be instantiated directly |
| **Purpose** | Provide interface, partial implementation, or base for derivation |
| **Pure Virtual Functions** | Must be overridden in derived classes |
| **Concrete Derived** | Must override all pure virtual functions |
| **Virtual Destructor** | Essential for proper cleanup |

---

## ✅ Best Practices

1. **Use abstract classes** to define interfaces
2. **Make destructor virtual** in abstract classes
3. **Provide default implementations** when appropriate
4. **Use pure virtual functions** for required behaviors
5. **Keep abstract classes focused** on single responsibility
6. **Document** which functions must be overridden

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Instantiating abstract class** | Compilation error | Only instantiate concrete derived classes |
| **Missing override** | Class remains abstract | Override all pure virtual functions |
| **Non-virtual destructor** | Memory leak | Make destructor virtual |
| **Forgetting pure virtual syntax** | Compilation error | Use `= 0` syntax |
| **Pure virtual destructor without body** | Linker error | Provide body even for pure virtual destructor |

---

## ✅ Key Takeaways

1. **Abstract classes** cannot be instantiated
2. **Pure virtual functions** define required behaviors
3. **Concrete derived classes** must override all pure virtual functions
4. **Interfaces** are abstract classes with only pure virtual functions
5. **Partial implementation** can be provided in abstract classes
6. **Template method pattern** uses abstract classes effectively
7. **Factory pattern** often uses abstract classes for products

---
---

## Next Step

- Go to [02_Interfaces_in_Cpp.md](02_Interfaces_in_Cpp.md) to continue with Interfaces in Cpp.
