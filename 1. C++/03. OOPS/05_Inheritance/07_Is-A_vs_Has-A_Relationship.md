# IS-A vs HAS-A Relationship in C++ - Complete Guide

## 📖 Overview

Understanding the difference between IS-A and HAS-A relationships is fundamental to good object-oriented design. **IS-A** represents inheritance (a specialized type of relationship), while **HAS-A** represents composition (a part-of relationship). Choosing the right relationship is crucial for creating maintainable, flexible, and correct class hierarchies.

---

## 🎯 Key Concepts

| Concept | Description | C++ Implementation |
|---------|-------------|-------------------|
| **IS-A** | "is a" relationship (inheritance) | Public inheritance |
| **HAS-A** | "has a" relationship (composition) | Member variables |
| **Liskov Substitution** | Derived must be substitutable for base | Follow for IS-A |
| **Composition** | Object contains other objects | Member objects or pointers |

---

## 1. **IS-A Relationship (Inheritance)**

### Definition
IS-A represents a specialization relationship. A derived class IS-A type of base class. All members of the base class are also members of the derived class.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Base class - general concept
class Animal {
protected:
    string name;
    int age;
    
public:
    Animal(string n, int a) : name(n), age(a) {}
    
    virtual void speak() const {
        cout << name << " makes a sound" << endl;
    }
    
    virtual void move() const {
        cout << name << " moves" << endl;
    }
    
    virtual ~Animal() {}
};

// Derived classes - specialized types
class Dog : public Animal {  // Dog IS-A Animal
public:
    Dog(string n, int a) : Animal(n, a) {}
    
    void speak() const override {
        cout << name << " barks: Woof!" << endl;
    }
    
    void move() const override {
        cout << name << " runs on four legs" << endl;
    }
    
    // Dog-specific behavior
    void wagTail() const {
        cout << name << " wags tail" << endl;
    }
};

class Bird : public Animal {  // Bird IS-A Animal
public:
    Bird(string n, int a) : Animal(n, a) {}
    
    void speak() const override {
        cout << name << " chirps: Tweet!" << endl;
    }
    
    void move() const override {
        cout << name << " flies" << endl;
    }
    
    // Bird-specific behavior
    void buildNest() const {
        cout << name << " builds a nest" << endl;
    }
};

int main() {
    cout << "=== IS-A Relationship ===" << endl;
    
    // Dog IS-A Animal
    Dog dog("Buddy", 3);
    dog.speak();    // Animal behavior
    dog.move();     // Animal behavior
    dog.wagTail();  // Dog-specific
    
    // Bird IS-A Animal
    Bird bird("Tweety", 1);
    bird.speak();     // Animal behavior
    bird.move();      // Animal behavior
    bird.buildNest(); // Bird-specific
    
    cout << "\nPolymorphic behavior (IS-A allows this):" << endl;
    Animal* animals[] = {&dog, &bird};
    for (auto animal : animals) {
        animal->speak();  // Calls appropriate derived method
        animal->move();   // Calls appropriate derived method
    }
    
    return 0;
}
```

**Output:**
```
=== IS-A Relationship ===
Buddy barks: Woof!
Buddy runs on four legs
Buddy wags tail
Tweety chirps: Tweet!
Tweety flies
Tweety builds a nest

Polymorphic behavior (IS-A allows this):
Buddy barks: Woof!
Buddy runs on four legs
Tweety chirps: Tweet!
Tweety flies
```

---

## 2. **HAS-A Relationship (Composition)**

### Definition
HAS-A represents a containment relationship. A class contains objects of other classes as members. This is also known as composition or aggregation.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Component classes
class Engine {
private:
    int horsepower;
    string type;
    
public:
    Engine(int hp, string t) : horsepower(hp), type(t) {
        cout << "  Engine created: " << horsepower << "hp " << type << endl;
    }
    
    void start() {
        cout << "  Engine starting..." << endl;
    }
    
    void stop() {
        cout << "  Engine stopping..." << endl;
    }
    
    ~Engine() {
        cout << "  Engine destroyed" << endl;
    }
};

class Wheel {
private:
    int size;
    string brand;
    
public:
    Wheel(int s, string b) : size(s), brand(b) {
        cout << "  Wheel created: " << size << " inch " << brand << endl;
    }
    
    void rotate() {
        cout << "  Wheel rotating" << endl;
    }
    
    ~Wheel() {
        cout << "  Wheel destroyed" << endl;
    }
};

class Transmission {
private:
    int gears;
    string type;
    
public:
    Transmission(int g, string t) : gears(g), type(t) {
        cout << "  Transmission created: " << gears << "-speed " << type << endl;
    }
    
    void shift(int gear) {
        cout << "  Shifting to gear " << gear << endl;
    }
    
    ~Transmission() {
        cout << "  Transmission destroyed" << endl;
    }
};

// Car HAS-A Engine, Wheels, Transmission
class Car {
private:
    string model;
    Engine engine;           // Composition - Car HAS-A Engine
    vector<Wheel> wheels;    // Composition - Car HAS-A Wheels
    Transmission* trans;     // Aggregation - Car HAS-A Transmission (can be shared)
    
public:
    Car(string m, int hp, string engineType, int wheelSize, string wheelBrand, int gears, string transType)
        : model(m), engine(hp, engineType) {
        
        cout << "Car constructor: " << model << endl;
        
        // Add wheels
        for (int i = 0; i < 4; i++) {
            wheels.emplace_back(wheelSize, wheelBrand);
        }
        
        // Transmission (could be shared with other cars)
        trans = new Transmission(gears, transType);
    }
    
    void start() {
        cout << model << " starting..." << endl;
        engine.start();
        for (auto& wheel : wheels) {
            wheel.rotate();
        }
        trans->shift(1);
    }
    
    void drive() {
        cout << model << " driving..." << endl;
        for (auto& wheel : wheels) {
            wheel.rotate();
        }
        trans->shift(2);
    }
    
    void stop() {
        cout << model << " stopping..." << endl;
        engine.stop();
        trans->shift(0);
    }
    
    ~Car() {
        cout << "Car destructor: " << model << endl;
        delete trans;
    }
};

int main() {
    cout << "=== HAS-A Relationship (Composition) ===" << endl;
    
    cout << "\nCreating Car (Car HAS-A Engine, Wheels, Transmission):" << endl;
    Car car("Tesla Model 3", 300, "Electric", 18, "Michelin", 1, "Single-speed");
    
    cout << "\nUsing Car:" << endl;
    car.start();
    car.drive();
    car.stop();
    
    cout << "\nDestruction order (reverse of construction):" << endl;
    // Destructor will be called automatically
    
    return 0;
}
```

---

## 3. **When to Use IS-A vs HAS-A**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Example 1: Employee Management
class Person {
protected:
    string name;
    int age;
    
public:
    Person(string n, int a) : name(n), age(a) {}
    virtual void display() const {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
    virtual ~Person() {}
};

// IS-A: Employee IS-A Person
class Employee : public Person {
private:
    int employeeId;
    double salary;
    
public:
    Employee(string n, int a, int id, double s) : Person(n, a), employeeId(id), salary(s) {}
    
    void display() const override {
        Person::display();
        cout << "  Employee ID: " << employeeId << ", Salary: $" << salary << endl;
    }
};

// HAS-A: Department HAS-A list of Employees
class Department {
private:
    string name;
    vector<Employee> employees;  // Composition
    
public:
    Department(string n) : name(n) {}
    
    void addEmployee(const Employee& emp) {
        employees.push_back(emp);
        cout << "Added to " << name << ": " << emp.getName() << endl;
    }
    
    void display() const {
        cout << "\nDepartment: " << name << " (" << employees.size() << " employees)" << endl;
        for (const auto& emp : employees) {
            emp.display();
        }
    }
};

// Example 2: Shape System
class Shape {
public:
    virtual double area() const = 0;
    virtual void draw() const = 0;
    virtual ~Shape() {}
};

// IS-A: Circle IS-A Shape
class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(double r) : radius(r) {}
    double area() const override { return 3.14159 * radius * radius; }
    void draw() const override { cout << "Drawing circle radius=" << radius << endl; }
};

// IS-A: Rectangle IS-A Shape
class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    double area() const override { return width * height; }
    void draw() const override { cout << "Drawing rectangle " << width << "x" << height << endl; }
};

// HAS-A: Drawing HAS-A list of Shapes
class Drawing {
private:
    vector<unique_ptr<Shape>> shapes;  // Composition
    
public:
    void addShape(Shape* shape) {
        shapes.emplace_back(shape);
    }
    
    void drawAll() const {
        cout << "\nDrawing all shapes:" << endl;
        for (const auto& shape : shapes) {
            shape->draw();
            cout << "  Area: " << shape->area() << endl;
        }
    }
};

int main() {
    cout << "=== When to Use IS-A vs HAS-A ===" << endl;
    
    cout << "\n1. IS-A Examples:" << endl;
    cout << "   - Employee IS-A Person ✓" << endl;
    cout << "   - Circle IS-A Shape ✓" << endl;
    cout << "   - Rectangle IS-A Shape ✓" << endl;
    cout << "   - Dog IS-A Animal ✓" << endl;
    
    cout << "\n2. HAS-A Examples:" << endl;
    cout << "   - Department HAS-A Employee ✓" << endl;
    cout << "   - Drawing HAS-A Shape ✓" << endl;
    cout << "   - Car HAS-A Engine ✓" << endl;
    cout << "   - Computer HAS-A CPU ✓" << endl;
    
    cout << "\n3. Wrong usage examples:" << endl;
    cout << "   - Car IS-A Engine ✗ (Car has an engine, not is an engine)" << endl;
    cout << "   - Department IS-A Employee ✗ (Department has employees)" << endl;
    cout << "   - Drawing IS-A Shape ✗ (Drawing contains shapes)" << endl;
    
    cout << "\n4. Demonstration:" << endl;
    
    // IS-A usage
    Circle circle(5);
    Rectangle rect(4, 6);
    cout << "Circle area: " << circle.area() << endl;
    cout << "Rectangle area: " << rect.area() << endl;
    
    // HAS-A usage
    Drawing drawing;
    drawing.addShape(new Circle(3));
    drawing.addShape(new Rectangle(2, 4));
    drawing.drawAll();
    
    return 0;
}
```

---

## 4. **Design Decision Guide**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Scenario 1: Logger - Should it be inherited or composed?

// Option A: Inheritance (IS-A)
class Logger {
public:
    virtual void log(const string& msg) {
        cout << "[LOG] " << msg << endl;
    }
};

class DatabaseLogger : public Logger {  // DatabaseLogger IS-A Logger?
public:
    void log(const string& msg) override {
        cout << "[DB] " << msg << endl;
    }
};

// Option B: Composition (HAS-A)
class Service {
private:
    Logger& logger;  // Service HAS-A Logger
    
public:
    Service(Logger& l) : logger(l) {}
    
    void process() {
        logger.log("Processing started");
        // ... do work
        logger.log("Processing completed");
    }
};

// Scenario 2: Computer components

// Correct: Composition
class CPU {
public:
    void process() { cout << "CPU processing" << endl; }
};

class Memory {
public:
    void load() { cout << "Memory loading" << endl; }
};

class Computer {
private:
    CPU cpu;      // HAS-A
    Memory memory; // HAS-A
    
public:
    void run() {
        cpu.process();
        memory.load();
        cout << "Computer running" << endl;
    }
};

// Wrong: Inheritance
class BadComputer : public CPU, public Memory {  // Computer IS-A CPU? NO!
public:
    void run() {
        process();  // From CPU
        load();     // From Memory
        cout << "Computer running" << endl;
    }
};

// Scenario 3: Vehicle types

// Correct: IS-A for specialization
class Vehicle {
public:
    virtual void move() = 0;
    virtual ~Vehicle() {}
};

class Car : public Vehicle {  // Car IS-A Vehicle ✓
public:
    void move() override { cout << "Car driving" << endl; }
};

class Boat : public Vehicle {  // Boat IS-A Vehicle ✓
public:
    void move() override { cout << "Boat sailing" << endl; }
};

// HAS-A for components
class AmphibiousVehicle : public Vehicle {
private:
    Car* car;    // HAS-A Car
    Boat* boat;  // HAS-A Boat
    
public:
    AmphibiousVehicle() : car(new Car()), boat(new Boat()) {}
    
    void move() override {
        cout << "Amphibious vehicle: ";
        car->move();
        boat->move();
    }
    
    ~AmphibiousVehicle() {
        delete car;
        delete boat;
    }
};

int main() {
    cout << "=== Design Decision Guide ===" << endl;
    
    cout << "\n1. IS-A (Inheritance) when:" << endl;
    cout << "   ✓ Specialization of existing class" << endl;
    cout << "   ✓ Need polymorphic behavior" << endl;
    cout << "   ✓ Liskov Substitution Principle holds" << endl;
    cout << "   ✓ Example: Car IS-A Vehicle" << endl;
    
    cout << "\n2. HAS-A (Composition) when:" << endl;
    cout << "   ✓ Object contains other objects" << endl;
    cout << "   ✓ Want to reuse functionality without inheritance" << endl;
    cout << "   ✓ More flexible (can change at runtime)" << endl;
    cout << "   ✓ Example: Computer HAS-A CPU" << endl;
    
    cout << "\n3. Decision tree:" << endl;
    cout << "   Does X logically belong to the same category as Y?" << endl;
    cout << "   ├── Yes → Consider IS-A (inheritance)" << endl;
    cout << "   └── No → Use HAS-A (composition)" << endl;
    
    cout << "\n4. Testing the decision:" << endl;
    
    // Test IS-A
    Car car;
    Vehicle* v = &car;  // Works because Car IS-A Vehicle
    v->move();
    
    // Test HAS-A
    Computer computer;
    computer.run();  // Computer uses CPU and Memory
    
    return 0;
}
```

---

## 5. **Practical Example: Library System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
using namespace std;

// IS-A relationships
class Person {
protected:
    string name;
    string email;
    
public:
    Person(string n, string e) : name(n), email(e) {}
    
    virtual void display() const {
        cout << "Name: " << name << ", Email: " << email << endl;
    }
    
    virtual ~Person() {}
};

// Member IS-A Person
class Member : public Person {
private:
    int memberId;
    static int nextId;
    
public:
    Member(string n, string e) : Person(n, e), memberId(nextId++) {}
    
    void display() const override {
        Person::display();
        cout << "  Member ID: " << memberId << endl;
    }
    
    int getId() const { return memberId; }
};

int Member::nextId = 1000;

// Librarian IS-A Person
class Librarian : public Person {
private:
    int employeeId;
    static int nextId;
    
public:
    Librarian(string n, string e) : Person(n, e), employeeId(nextId++) {}
    
    void display() const override {
        Person::display();
        cout << "  Employee ID: " << employeeId << endl;
    }
};

int Librarian::nextId = 500;

// Book (no inheritance - independent class)
class Book {
private:
    string isbn;
    string title;
    string author;
    bool available;
    
public:
    Book(string i, string t, string a) : isbn(i), title(t), author(a), available(true) {}
    
    void display() const {
        cout << "  ISBN: " << isbn << ", Title: " << title 
             << ", Author: " << author << endl;
        cout << "  Status: " << (available ? "Available" : "Borrowed") << endl;
    }
    
    string getISBN() const { return isbn; }
    string getTitle() const { return title; }
    bool isAvailable() const { return available; }
    void borrow() { available = false; }
    void returnBook() { available = true; }
};

// HAS-A relationships

// Library HAS-A Books
class Library {
private:
    string name;
    vector<Book> books;  // Composition
    
public:
    Library(string n) : name(n) {}
    
    void addBook(const Book& book) {
        books.push_back(book);
        cout << "Added to library: " << book.getTitle() << endl;
    }
    
    Book* findBook(const string& isbn) {
        for (auto& book : books) {
            if (book.getISBN() == isbn) {
                return &book;
            }
        }
        return nullptr;
    }
    
    void displayBooks() const {
        cout << "\nLibrary: " << name << " (" << books.size() << " books)" << endl;
        for (const auto& book : books) {
            book.display();
        }
    }
};

// BorrowingRecord HAS-A Book and Member
class BorrowingRecord {
private:
    Book* book;
    Member* member;
    string borrowDate;
    string dueDate;
    
public:
    BorrowingRecord(Book* b, Member* m, string borrow, string due)
        : book(b), member(m), borrowDate(borrow), dueDate(due) {}
    
    void display() const {
        cout << "  Book: " << book->getTitle() << endl;
        cout << "  Member ID: " << member->getId() << endl;
        cout << "  Borrowed: " << borrowDate << ", Due: " << dueDate << endl;
    }
    
    Book* getBook() const { return book; }
    Member* getMember() const { return member; }
};

// LibrarySystem HAS-A Library, Members, and Records
class LibrarySystem {
private:
    Library library;
    vector<Member> members;
    vector<BorrowingRecord> records;
    
public:
    LibrarySystem(string libName) : library(libName) {}
    
    void addBook(const Book& book) {
        library.addBook(book);
    }
    
    void addMember(const Member& member) {
        members.push_back(member);
        cout << "Member added: " << member.getName() << endl;
    }
    
    void borrowBook(int memberId, const string& isbn, string borrowDate, string dueDate) {
        // Find member
        Member* member = nullptr;
        for (auto& m : members) {
            if (m.getId() == memberId) {
                member = &m;
                break;
            }
        }
        
        if (!member) {
            cout << "Member not found!" << endl;
            return;
        }
        
        // Find book
        Book* book = library.findBook(isbn);
        if (!book) {
            cout << "Book not found!" << endl;
            return;
        }
        
        if (!book->isAvailable()) {
            cout << "Book not available!" << endl;
            return;
        }
        
        // Borrow the book
        book->borrow();
        records.emplace_back(book, member, borrowDate, dueDate);
        cout << "Book borrowed successfully!" << endl;
    }
    
    void returnBook(const string& isbn) {
        // Find borrowing record
        for (auto it = records.begin(); it != records.end(); ++it) {
            if (it->getBook()->getISBN() == isbn) {
                it->getBook()->returnBook();
                records.erase(it);
                cout << "Book returned successfully!" << endl;
                return;
            }
        }
        cout << "Borrowing record not found!" << endl;
    }
    
    void display() const {
        library.displayBooks();
        
        cout << "\nMembers (" << members.size() << "):" << endl;
        for (const auto& member : members) {
            member.display();
        }
        
        cout << "\nActive Borrowings (" << records.size() << "):" << endl;
        for (const auto& record : records) {
            record.display();
        }
    }
};

int main() {
    cout << "=== Library System - IS-A vs HAS-A ===" << endl;
    
    LibrarySystem libSys("City Library");
    
    cout << "\n1. Adding books (Library HAS-A Books):" << endl;
    libSys.addBook(Book("978-0-321-99278-9", "C++ Primer", "Lippman"));
    libSys.addBook(Book("978-0-201-63361-0", "Design Patterns", "Gamma"));
    libSys.addBook(Book("978-0-13-235088-4", "Clean Code", "Martin"));
    
    cout << "\n2. Adding members (Library HAS-A Members):" << endl;
    libSys.addMember(Member("Alice Johnson", "alice@email.com"));
    libSys.addMember(Member("Bob Smith", "bob@email.com"));
    
    cout << "\n3. Borrowing books:" << endl;
    libSys.borrowBook(1000, "978-0-321-99278-9", "2024-01-15", "2024-01-29");
    libSys.borrowBook(1001, "978-0-201-63361-0", "2024-01-16", "2024-01-30");
    
    cout << "\n4. Displaying system state:" << endl;
    libSys.display();
    
    cout << "\n5. Returning a book:" << endl;
    libSys.returnBook("978-0-321-99278-9");
    
    cout << "\n6. Final state:" << endl;
    libSys.display();
    
    cout << "\n7. Relationship Summary:" << endl;
    cout << "   - Member IS-A Person ✓" << endl;
    cout << "   - Librarian IS-A Person ✓" << endl;
    cout << "   - Library HAS-A Books ✓" << endl;
    cout << "   - LibrarySystem HAS-A Library ✓" << endl;
    cout << "   - LibrarySystem HAS-A Members ✓" << endl;
    cout << "   - BorrowingRecord HAS-A Book ✓" << endl;
    cout << "   - BorrowingRecord HAS-A Member ✓" << endl;
    
    return 0;
}
```

---

## 📊 IS-A vs HAS-A Summary

| Aspect | IS-A (Inheritance) | HAS-A (Composition) |
|--------|-------------------|---------------------|
| **Relationship** | "is a" specialization | "has a" containment |
| **C++ Implementation** | Public inheritance | Member variables |
| **Flexibility** | Static (compile-time) | Dynamic (runtime) |
| **Coupling** | Tight coupling | Loose coupling |
| **Reuse** | Code reuse | Functionality reuse |
| **Polymorphism** | Yes | No (needs interface) |
| **Example** | Dog IS-A Animal | Car HAS-A Engine |

---

## ✅ Best Practices

1. **Use IS-A** when class is a specialized version of another
2. **Use HAS-A** when class contains other objects
3. **Prefer composition over inheritance** when in doubt
4. **Follow Liskov Substitution Principle** for IS-A relationships
5. **Keep inheritance hierarchies shallow** for IS-A
6. **Use interfaces** (pure virtual) for shared behavior without inheritance

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Using inheritance for convenience** | Wrong relationship | Use composition |
| **Deep inheritance hierarchies** | Hard to maintain | Keep shallow, use composition |
| **Violating Liskov Substitution** | Broken polymorphism | Ensure derived is substitutable |
| **Overusing inheritance** | Tight coupling | Prefer composition |

---

## ✅ Key Takeaways

1. **IS-A**: Specialization (inheritance) - "Dog IS-A Animal"
2. **HAS-A**: Containment (composition) - "Car HAS-A Engine"
3. **Liskov Substitution**: Derived must be usable as base
4. **Prefer composition** over inheritance for flexibility
5. **Use inheritance** for polymorphic behavior and specialization
6. **Both have their place** in good OOP design

---