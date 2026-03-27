# 01_Introduction/04_Basic_Terminology.md

# Object-Oriented Programming: Basic Terminology

## 📖 Overview

Understanding OOP requires mastering its fundamental terminology. This guide provides comprehensive definitions, examples, and practical applications of all essential OOP terms. Master these concepts to build a solid foundation in object-oriented programming.

---

## 🎯 Core Terminology

### 1. **Class**

**Definition:** A class is a blueprint or template for creating objects. It defines the structure (data members) and behavior (member functions) that objects of that type will have.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Class definition - blueprint for creating objects
class Car {
private:
    string brand;      // Data member
    string model;      // Data member
    int year;          // Data member
    int speed;         // Data member
    
public:
    // Constructor
    Car(string b, string m, int y) {
        brand = b;
        model = m;
        year = y;
        speed = 0;
    }
    
    // Member functions (methods)
    void accelerate(int amount) {
        speed += amount;
    }
    
    void brake(int amount) {
        speed = max(0, speed - amount);
    }
    
    void display() {
        cout << brand << " " << model << " (" << year << ") - " << speed << " km/h" << endl;
    }
};

int main() {
    // Creating objects from the Car class
    Car myCar("Toyota", "Camry", 2022);
    myCar.display();
    
    return 0;
}
```

**Key Points:**
- Classes don't occupy memory until objects are created
- A class can have multiple objects
- Classes support access specifiers (public, private, protected)
- Classes can contain data members and member functions

---

### 2. **Object**

**Definition:** An object is an instance of a class. It represents a real-world entity with its own state (data) and behavior (methods).

```cpp
class Student {
public:
    string name;
    int rollNumber;
    float marks;
};

int main() {
    // Objects - instances of the Student class
    Student student1;  // Object 1
    Student student2;  // Object 2
    Student student3;  // Object 3
    
    // Each object has its own data
    student1.name = "Alice";
    student1.rollNumber = 101;
    student1.marks = 85.5;
    
    student2.name = "Bob";
    student2.rollNumber = 102;
    student2.marks = 78.0;
    
    student3.name = "Charlie";
    student3.rollNumber = 103;
    student3.marks = 92.5;
    
    // Each object's state is independent
    cout << student1.name << "'s marks: " << student1.marks << endl;
    cout << student2.name << "'s marks: " << student2.marks << endl;
    cout << student3.name << "'s marks: " << student3.marks << endl;
    
    return 0;
}
```

**Object Characteristics:**
- **Identity**: Each object has a unique identity (memory address)
- **State**: Attributes/data that define the object's condition
- **Behavior**: Methods that define what the object can do

---

### 3. **Data Member (Attribute/Property)**

**Definition:** Data members are variables declared within a class that hold the state of an object. They are also called attributes, properties, or fields.

```cpp
class Employee {
private:
    // Data members (attributes)
    int employeeID;           // Numeric attribute
    string name;              // String attribute
    double salary;            // Double attribute
    bool isActive;            // Boolean attribute
    static int totalEmployees; // Static data member (shared by all objects)
    
public:
    // Member functions to access/modify data members
    void setDetails(int id, string n, double s) {
        employeeID = id;
        name = n;
        salary = s;
        isActive = true;
    }
    
    void display() {
        cout << "ID: " << employeeID << endl;
        cout << "Name: " << name << endl;
        cout << "Salary: $" << salary << endl;
        cout << "Active: " << (isActive ? "Yes" : "No") << endl;
    }
};

int Employee::totalEmployees = 0;  // Initialize static member
```

**Types of Data Members:**
- **Instance variables**: Each object has its own copy
- **Static variables**: Shared across all objects of the class
- **Constant members**: Cannot be modified after initialization
- **Reference members**: References to other objects

---

### 4. **Member Function (Method)**

**Definition:** Member functions are functions declared within a class that define the behavior of objects. They can access and modify the object's data members.

```cpp
class Calculator {
private:
    double result;
    
public:
    // Member functions (methods)
    void add(double value) {
        result += value;
    }
    
    void subtract(double value) {
        result -= value;
    }
    
    void multiply(double value) {
        result *= value;
    }
    
    void divide(double value) {
        if (value != 0) {
            result /= value;
        }
    }
    
    void clear() {
        result = 0;
    }
    
    double getResult() const {  // Const member function (doesn't modify object)
        return result;
    }
    
    static void showInstructions() {  // Static member function
        cout << "Use: add, subtract, multiply, divide" << endl;
    }
};

int main() {
    Calculator calc;
    
    calc.add(10);
    calc.multiply(5);
    calc.subtract(20);
    calc.divide(2);
    
    cout << "Result: " << calc.getResult() << endl;  // 15
    
    Calculator::showInstructions();  // Call static method without object
    
    return 0;
}
```

**Types of Member Functions:**
- **Instance methods**: Operate on specific objects
- **Static methods**: Belong to the class, not individual objects
- **Const methods**: Promise not to modify the object
- **Virtual methods**: Can be overridden in derived classes
- **Inline methods**: Expanded at compile time for performance

---

### 5. **Constructor**

**Definition:** A constructor is a special member function automatically called when an object is created. It initializes the object's data members.

```cpp
class Book {
private:
    string title;
    string author;
    int pages;
    double price;
    
public:
    // Default constructor
    Book() {
        title = "Unknown";
        author = "Unknown";
        pages = 0;
        price = 0.0;
        cout << "Default constructor called" << endl;
    }
    
    // Parameterized constructor
    Book(string t, string a, int p, double pr) {
        title = t;
        author = a;
        pages = p;
        price = pr;
        cout << "Parameterized constructor called" << endl;
    }
    
    // Copy constructor
    Book(const Book& other) {
        title = other.title;
        author = other.author;
        pages = other.pages;
        price = other.price;
        cout << "Copy constructor called" << endl;
    }
    
    // Constructor with initialization list (more efficient)
    Book(string t, string a) : title(t), author(a), pages(0), price(0.0) {
        cout << "Initialization list constructor called" << endl;
    }
    
    void display() {
        cout << title << " by " << author << " - " << pages << " pages, $" << price << endl;
    }
};

int main() {
    Book book1;                                    // Default constructor
    Book book2("C++ Programming", "Bjarne", 1000, 59.99);  // Parameterized
    Book book3(book2);                             // Copy constructor
    Book book4("The Lord of the Rings", "Tolkien"); // Initialization list
    
    book1.display();
    book2.display();
    book3.display();
    book4.display();
    
    return 0;
}
```

**Constructor Types:**
- **Default constructor**: No parameters, initializes with default values
- **Parameterized constructor**: Takes arguments to initialize with specific values
- **Copy constructor**: Creates a new object as a copy of an existing object
- **Move constructor** (C++11): Transfers resources from a temporary object
- **Delegating constructor** (C++11): Calls another constructor from the same class

---

### 6. **Destructor**

**Definition:** A destructor is a special member function automatically called when an object goes out of scope or is deleted. It releases resources allocated by the object.

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class String {
private:
    char* data;
    int length;
    
public:
    // Constructor
    String(const char* str) {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "Constructor: Created \"" << data << "\"" << endl;
    }
    
    // Destructor
    ~String() {
        cout << "Destructor: Deleting \"" << data << "\"" << endl;
        delete[] data;  // Release allocated memory
        data = nullptr;
    }
    
    void display() {
        cout << "String: " << data << " (Length: " << length << ")" << endl;
    }
};

int main() {
    {
        String s1("Hello");
        String s2("World");
        
        s1.display();
        s2.display();
        
        // Objects will be destroyed when they go out of scope
    }  // Destructors called automatically here
    
    cout << "Objects destroyed!" << endl;
    
    return 0;
}
```

**Destructor Characteristics:**
- Same name as class with tilde (~) prefix
- No parameters and no return type
- Cannot be overloaded (only one destructor per class)
- Called automatically when object is destroyed
- Used to release dynamic memory, close files, release locks

---

### 7. **Access Specifiers**

**Definition:** Access specifiers control the visibility and accessibility of class members (data and functions).

```cpp
#include <iostream>
using namespace std;

class AccessDemo {
private:
    // Private: Accessible only within this class
    int privateVar;
    
    void privateMethod() {
        cout << "Private method" << endl;
    }
    
protected:
    // Protected: Accessible within this class and derived classes
    int protectedVar;
    
    void protectedMethod() {
        cout << "Protected method" << endl;
    }
    
public:
    // Public: Accessible from anywhere
    int publicVar;
    
    void publicMethod() {
        cout << "Public method" << endl;
        
        // Can access private and protected members within the class
        privateVar = 10;
        protectedVar = 20;
        privateMethod();
        protectedMethod();
    }
    
    // Getter and setter for private members
    void setPrivateVar(int value) {
        privateVar = value;
    }
    
    int getPrivateVar() {
        return privateVar;
    }
};

class Derived : public AccessDemo {
public:
    void derivedMethod() {
        // Can access public and protected members
        publicVar = 100;
        protectedVar = 200;  // Accessible in derived class
        publicMethod();
        protectedMethod();
        
        // Cannot access private members
        // privateVar = 300;  // Error! Private member not accessible
    }
};

int main() {
    AccessDemo obj;
    
    // Public members accessible from main
    obj.publicVar = 50;
    obj.publicMethod();
    
    // Cannot access private/protected members directly
    // obj.privateVar = 10;   // Error!
    // obj.protectedVar = 20;  // Error!
    
    // Use public interface to access private data
    obj.setPrivateVar(99);
    cout << "Private var: " << obj.getPrivateVar() << endl;
    
    Derived derived;
    derived.derivedMethod();  // Can access protected members
    
    return 0;
}
```

**Access Specifier Summary:**

| Specifier | Class Access | Derived Class Access | External Access |
|-----------|--------------|---------------------|-----------------|
| **private** | ✓ Yes | ✗ No | ✗ No |
| **protected** | ✓ Yes | ✓ Yes | ✗ No |
| **public** | ✓ Yes | ✓ Yes | ✓ Yes |

---

### 8. **Inheritance**

**Definition:** Inheritance is a mechanism where a new class (derived class) acquires the properties and behaviors of an existing class (base class).

```cpp
#include <iostream>
#include <string>
using namespace std;

// Base class
class Animal {
protected:
    string name;
    int age;
    
public:
    Animal(string n, int a) : name(n), age(a) {}
    
    void eat() {
        cout << name << " is eating" << endl;
    }
    
    void sleep() {
        cout << name << " is sleeping" << endl;
    }
    
    virtual void sound() {
        cout << name << " makes a sound" << endl;
    }
    
    void display() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

// Derived class (inherits from Animal)
class Dog : public Animal {
private:
    string breed;
    
public:
    Dog(string n, int a, string b) : Animal(n, a), breed(b) {}
    
    // Override base class method
    void sound() override {
        cout << name << " barks: Woof! Woof!" << endl;
    }
    
    void wagTail() {
        cout << name << " is wagging tail" << endl;
    }
    
    void display() {
        Animal::display();
        cout << "Breed: " << breed << endl;
    }
};

// Another derived class
class Cat : public Animal {
public:
    Cat(string n, int a) : Animal(n, a) {}
    
    void sound() override {
        cout << name << " meows: Meow! Meow!" << endl;
    }
    
    void climb() {
        cout << name << " is climbing" << endl;
    }
};

int main() {
    Dog dog("Buddy", 3, "Golden Retriever");
    Cat cat("Whiskers", 2);
    
    dog.display();
    dog.eat();
    dog.sound();
    dog.wagTail();
    
    cout << endl;
    
    cat.display();
    cat.eat();
    cat.sound();
    cat.climb();
    
    return 0;
}
```

**Inheritance Types:**
- **Single inheritance**: One base class, one derived class
- **Multiple inheritance**: Multiple base classes (C++ specific)
- **Multilevel inheritance**: Chain of inheritance
- **Hierarchical inheritance**: Multiple derived classes from one base
- **Hybrid inheritance**: Combination of multiple inheritance types

---

### 9. **Polymorphism**

**Definition:** Polymorphism allows objects of different classes to be treated as objects of a common base class, with the appropriate method being called based on the actual object type.

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Base class
class Shape {
public:
    virtual double area() const = 0;  // Pure virtual function
    virtual void draw() const {
        cout << "Drawing a shape" << endl;
    }
    virtual ~Shape() {}
};

// Derived class 1
class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(double r) : radius(r) {}
    
    double area() const override {
        return 3.14159 * radius * radius;
    }
    
    void draw() const override {
        cout << "Drawing a circle with radius " << radius << endl;
    }
};

// Derived class 2
class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    
    double area() const override {
        return width * height;
    }
    
    void draw() const override {
        cout << "Drawing a rectangle " << width << "x" << height << endl;
    }
};

// Derived class 3
class Triangle : public Shape {
private:
    double base, height;
    
public:
    Triangle(double b, double h) : base(b), height(h) {}
    
    double area() const override {
        return 0.5 * base * height;
    }
    
    void draw() const override {
        cout << "Drawing a triangle with base " << base << " and height " << height << endl;
    }
};

// Function demonstrating polymorphism
void processShape(const Shape& shape) {
    shape.draw();
    cout << "Area: " << shape.area() << endl;
}

int main() {
    // Polymorphism through base class pointers/references
    vector<Shape*> shapes;
    shapes.push_back(new Circle(5));
    shapes.push_back(new Rectangle(4, 6));
    shapes.push_back(new Triangle(3, 4));
    
    // Same code works for all shapes
    for (const auto& shape : shapes) {
        processShape(*shape);
        cout << endl;
    }
    
    // Clean up
    for (auto shape : shapes) {
        delete shape;
    }
    
    return 0;
}
```

**Types of Polymorphism:**
- **Compile-time polymorphism**: Function overloading, operator overloading
- **Run-time polymorphism**: Virtual functions, inheritance

---

### 10. **Abstraction**

**Definition:** Abstraction is the concept of hiding complex implementation details and showing only the essential features to the user.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Abstract class (interface)
class Database {
public:
    // Abstract methods (pure virtual functions)
    virtual void connect() = 0;
    virtual void executeQuery(const string& query) = 0;
    virtual void disconnect() = 0;
    virtual ~Database() {}
};

// Concrete implementation 1
class MySQLDatabase : public Database {
private:
    string connectionString;
    bool isConnected;
    
    // Hidden implementation details
    void establishConnection() {
        cout << "Establishing MySQL connection..." << endl;
        // Complex connection logic
        isConnected = true;
    }
    
    void closeConnection() {
        cout << "Closing MySQL connection..." << endl;
        isConnected = false;
    }
    
public:
    MySQLDatabase(string conn) : connectionString(conn), isConnected(false) {}
    
    void connect() override {
        if (!isConnected) {
            establishConnection();
            cout << "Connected to MySQL database: " << connectionString << endl;
        }
    }
    
    void executeQuery(const string& query) override {
        if (!isConnected) {
            cout << "Not connected to database!" << endl;
            return;
        }
        cout << "Executing MySQL query: " << query << endl;
        // Complex query execution logic
    }
    
    void disconnect() override {
        if (isConnected) {
            closeConnection();
            cout << "Disconnected from MySQL database" << endl;
        }
    }
};

// Concrete implementation 2
class PostgreSQLDatabase : public Database {
private:
    string host;
    string database;
    
    void openConnection() {
        cout << "Opening PostgreSQL connection..." << endl;
    }
    
    void closeConnection() {
        cout << "Closing PostgreSQL connection..." << endl;
    }
    
public:
    PostgreSQLDatabase(string h, string db) : host(h), database(db) {}
    
    void connect() override {
        openConnection();
        cout << "Connected to PostgreSQL database: " << host << "/" << database << endl;
    }
    
    void executeQuery(const string& query) override {
        cout << "Executing PostgreSQL query: " << query << endl;
    }
    
    void disconnect() override {
        closeConnection();
        cout << "Disconnected from PostgreSQL database" << endl;
    }
};

int main() {
    // User only sees the simple interface, not the complexity
    Database* db1 = new MySQLDatabase("localhost:3306/mydb");
    Database* db2 = new PostgreSQLDatabase("localhost", "mydb");
    
    db1->connect();
    db1->executeQuery("SELECT * FROM users");
    db1->disconnect();
    
    cout << endl;
    
    db2->connect();
    db2->executeQuery("SELECT * FROM products");
    db2->disconnect();
    
    delete db1;
    delete db2;
    
    return 0;
}
```

---

## 📚 OOP Terminology Glossary

| Term | Definition |
|------|------------|
| **Class** | Blueprint for creating objects |
| **Object** | Instance of a class |
| **Instance** | Another name for an object |
| **Method** | Function defined within a class |
| **Attribute** | Data member/variable in a class |
| **Constructor** | Special method called when object is created |
| **Destructor** | Special method called when object is destroyed |
| **Encapsulation** | Bundling data and methods, hiding internal state |
| **Inheritance** | Creating new classes from existing ones |
| **Polymorphism** | Same interface, different implementations |
| **Abstraction** | Hiding complex implementation details |
| **Interface** | Set of public methods a class provides |
| **Base Class** | Parent class being inherited from |
| **Derived Class** | Child class that inherits from base |
| **Override** | Redefining a base class method in derived class |
| **Overload** | Multiple methods with same name, different parameters |
| **Virtual Function** | Function that can be overridden in derived classes |
| **Pure Virtual** | Abstract function that must be overridden |
| **Static Member** | Member shared by all objects of a class |
| **Const Member** | Member that doesn't modify the object |

---

## ✅ Key Takeaways

1. **Class vs Object**: Class is blueprint, object is instance
2. **Data Members**: Store object state
3. **Member Functions**: Define object behavior
4. **Constructors**: Initialize objects automatically
5. **Destructors**: Clean up resources automatically
6. **Access Specifiers**: Control visibility (public, private, protected)
7. **Inheritance**: Code reuse through "is-a" relationships
8. **Polymorphism**: Same interface, different implementations
9. **Abstraction**: Hide complexity, show essentials

---