# Abstract Classes in C++ - Complete Guide

## 📖 Overview

An abstract class is a class that cannot be instantiated and is designed to be used as a base class. It contains at least one pure virtual function and serves as an interface or a partially implemented foundation for derived classes. Abstract classes are fundamental to designing extensible and maintainable class hierarchies.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Abstract Class** | Class with at least one pure virtual function, cannot be instantiated |
| **Concrete Class** | Class that overrides all pure virtual functions, can be instantiated |
| **Pure Virtual Function** | Virtual function with `= 0` syntax |
| **Interface** | Abstract class with only pure virtual functions |
| **Partial Implementation** | Abstract class with some implemented methods |

---

## 1. **Basic Abstract Class**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// Abstract class (cannot be instantiated)
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
    
    // Pure virtual functions
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

---

## 3. **Interface (Pure Abstract Class)**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Interface 1 - Drawable
class IDrawable {
public:
    virtual void draw() const = 0;
    virtual void setColor(const string& color) = 0;
    virtual string getColor() const = 0;
    virtual ~IDrawable() = default;
};

// Interface 2 - Resizable
class IResizable {
public:
    virtual void resize(double factor) = 0;
    virtual void scale(double factor) = 0;
    virtual ~IResizable() = default;
};

// Interface 3 - Movable
class IMovable {
public:
    virtual void move(int dx, int dy) = 0;
    virtual void moveTo(int x, int y) = 0;
    virtual ~IMovable() = default;
};

// Concrete class implementing multiple interfaces
class Shape : public IDrawable, public IResizable, public IMovable {
private:
    string color;
    int x, y;
    double width, height;
    
public:
    Shape(string c, int xPos, int yPos, double w, double h)
        : color(c), x(xPos), y(yPos), width(w), height(h) {}
    
    // IDrawable implementation
    void draw() const override {
        cout << "Shape at (" << x << ", " << y << ") size " 
             << width << "x" << height << " color " << color << endl;
    }
    
    void setColor(const string& c) override {
        color = c;
        cout << "Color changed to " << color << endl;
    }
    
    string getColor() const override {
        return color;
    }
    
    // IResizable implementation
    void resize(double factor) override {
        width *= factor;
        height *= factor;
        cout << "Resized to " << width << "x" << height << endl;
    }
    
    void scale(double factor) override {
        resize(factor);
    }
    
    // IMovable implementation
    void move(int dx, int dy) override {
        x += dx;
        y += dy;
        cout << "Moved to (" << x << ", " << y << ")" << endl;
    }
    
    void moveTo(int xPos, int yPos) override {
        x = xPos;
        y = yPos;
        cout << "Moved to (" << x << ", " << y << ")" << endl;
    }
    
    double area() const {
        return width * height;
    }
};

// Class implementing only some interfaces
class Point : public IDrawable, public IMovable {
private:
    string color;
    int x, y;
    
public:
    Point(string c, int xPos, int yPos) : color(c), x(xPos), y(yPos) {}
    
    void draw() const override {
        cout << "Point at (" << x << ", " << y << ") color " << color << endl;
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
};

int main() {
    cout << "=== Interface (Pure Abstract Class) ===" << endl;
    
    Shape rect("Red", 10, 20, 100, 50);
    Point pt("Blue", 30, 40);
    
    cout << "\n1. Using IDrawable interface:" << endl;
    IDrawable* d1 = &rect;
    IDrawable* d2 = &pt;
    
    d1->draw();
    d2->draw();
    d1->setColor("Green");
    d1->draw();
    
    cout << "\n2. Using IResizable interface (only Shape):" << endl;
    IResizable* r = &rect;
    r->resize(2.0);
    
    cout << "\n3. Using IMovable interface:" << endl;
    IMovable* m1 = &rect;
    IMovable* m2 = &pt;
    
    m1->move(5, 10);
    m2->move(-10, -5);
    
    cout << "\n4. Final state:" << endl;
    rect.draw();
    pt.draw();
    
    return 0;
}
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

## 6. **Practical Example: Payment System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <iomanip>
#include <ctime>
using namespace std;

// Abstract Payment class
class Payment {
protected:
    double amount;
    string currency;
    time_t timestamp;
    bool processed;
    
public:
    Payment(double amt, string curr) : amount(amt), currency(curr), processed(false) {
        timestamp = time(nullptr);
    }
    
    virtual bool process() = 0;
    virtual void validate() = 0;
    virtual void receipt() const = 0;
    
    virtual double calculateFee() const = 0;
    virtual string getPaymentType() const = 0;
    
    bool isProcessed() const { return processed; }
    double getAmount() const { return amount; }
    
    void displayInfo() const {
        cout << fixed << setprecision(2);
        cout << "Type: " << getPaymentType() << endl;
        cout << "Amount: " << amount << " " << currency << endl;
        cout << "Fee: " << calculateFee() << " " << currency << endl;
        cout << "Total: " << (amount + calculateFee()) << " " << currency << endl;
        cout << "Status: " << (processed ? "Processed" : "Pending") << endl;
    }
    
    virtual ~Payment() = default;
};

// Credit Card Payment
class CreditCardPayment : public Payment {
private:
    string cardNumber;
    string cardHolder;
    string expiryDate;
    string cvv;
    
public:
    CreditCardPayment(double amt, string curr, string card, string holder, string expiry, string c)
        : Payment(amt, curr), cardNumber(card), cardHolder(holder), expiryDate(expiry), cvv(c) {}
    
    void validate() override {
        cout << "Validating credit card..." << endl;
        // Simplified validation
        if (cardNumber.length() >= 13 && cardNumber.length() <= 19) {
            cout << "  Card number valid" << endl;
        } else {
            throw runtime_error("Invalid card number");
        }
        
        // Check expiry (simplified)
        if (expiryDate > "2024") {
            cout << "  Card not expired" << endl;
        } else {
            throw runtime_error("Card expired");
        }
    }
    
    bool process() override {
        try {
            validate();
            cout << "Processing credit card payment..." << endl;
            cout << "  Charging " << amount << " " << currency << " to card ****" 
                 << cardNumber.substr(cardNumber.length() - 4) << endl;
            processed = true;
            return true;
        } catch (const exception& e) {
            cout << "Payment failed: " << e.what() << endl;
            return false;
        }
    }
    
    double calculateFee() const override {
        return amount * 0.025;  // 2.5% fee
    }
    
    string getPaymentType() const override {
        return "Credit Card";
    }
    
    void receipt() const override {
        cout << "\n=== Credit Card Receipt ===" << endl;
        cout << "Card Holder: " << cardHolder << endl;
        cout << "Card: ****" << cardNumber.substr(cardNumber.length() - 4) << endl;
        displayInfo();
    }
};

// PayPal Payment
class PayPalPayment : public Payment {
private:
    string email;
    string transactionId;
    
public:
    PayPalPayment(double amt, string curr, string em)
        : Payment(amt, curr), email(em), transactionId("") {}
    
    void validate() override {
        cout << "Validating PayPal account..." << endl;
        if (email.find('@') != string::npos) {
            cout << "  Email valid" << endl;
        } else {
            throw runtime_error("Invalid email address");
        }
    }
    
    bool process() override {
        try {
            validate();
            transactionId = "PP-" + to_string(rand() % 10000);
            cout << "Processing PayPal payment..." << endl;
            cout << "  Transaction ID: " << transactionId << endl;
            processed = true;
            return true;
        } catch (const exception& e) {
            cout << "Payment failed: " << e.what() << endl;
            return false;
        }
    }
    
    double calculateFee() const override {
        return amount * 0.03;  // 3% fee
    }
    
    string getPaymentType() const override {
        return "PayPal";
    }
    
    void receipt() const override {
        cout << "\n=== PayPal Receipt ===" << endl;
        cout << "Email: " << email << endl;
        cout << "Transaction: " << transactionId << endl;
        displayInfo();
    }
};

// Bank Transfer Payment
class BankTransferPayment : public Payment {
private:
    string accountNumber;
    string bankCode;
    string reference;
    
public:
    BankTransferPayment(double amt, string curr, string account, string bank)
        : Payment(amt, curr), accountNumber(account), bankCode(bank), reference("") {}
    
    void validate() override {
        cout << "Validating bank account..." << endl;
        if (accountNumber.length() >= 8 && accountNumber.length() <= 20) {
            cout << "  Account number valid" << endl;
        } else {
            throw runtime_error("Invalid account number");
        }
    }
    
    bool process() override {
        try {
            validate();
            reference = "TRF-" + to_string(rand() % 10000);
            cout << "Processing bank transfer..." << endl;
            cout << "  Reference: " << reference << endl;
            processed = true;
            return true;
        } catch (const exception& e) {
            cout << "Payment failed: " << e.what() << endl;
            return false;
        }
    }
    
    double calculateFee() const override {
        return 5.0;  // Flat fee
    }
    
    string getPaymentType() const override {
        return "Bank Transfer";
    }
    
    void receipt() const override {
        cout << "\n=== Bank Transfer Receipt ===" << endl;
        cout << "Account: ****" << accountNumber.substr(accountNumber.length() - 4) << endl;
        cout << "Bank: " << bankCode << endl;
        cout << "Reference: " << reference << endl;
        displayInfo();
    }
};

class PaymentProcessor {
private:
    vector<unique_ptr<Payment>> payments;
    
public:
    void addPayment(Payment* payment) {
        payments.emplace_back(payment);
    }
    
    void processAll() {
        cout << "\n=== Processing Payments ===" << endl;
        for (auto& payment : payments) {
            cout << "\nProcessing " << payment->getPaymentType() << "..." << endl;
            payment->process();
        }
    }
    
    void printReceipts() const {
        cout << "\n=== Payment Receipts ===" << endl;
        for (const auto& payment : payments) {
            if (payment->isProcessed()) {
                payment->receipt();
            }
        }
    }
    
    double getTotalAmount() const {
        double total = 0;
        for (const auto& payment : payments) {
            if (payment->isProcessed()) {
                total += payment->getAmount() + payment->calculateFee();
            }
        }
        return total;
    }
};

int main() {
    cout << "=== Payment System with Abstract Classes ===" << endl;
    
    PaymentProcessor processor;
    
    cout << "\n1. Adding payments:" << endl;
    processor.addPayment(new CreditCardPayment(100.0, "USD", "4111111111111111", 
                                               "John Doe", "12/25", "123"));
    processor.addPayment(new PayPalPayment(75.50, "EUR", "john@example.com"));
    processor.addPayment(new BankTransferPayment(500.0, "GBP", "12345678", "BANK123"));
    
    cout << "\n2. Processing payments:" << endl;
    processor.processAll();
    
    cout << "\n3. Generating receipts:" << endl;
    processor.printReceipts();
    
    cout << "\n4. Total collected: $" << fixed << setprecision(2) 
         << processor.getTotalAmount() << endl;
    
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