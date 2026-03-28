# 08_Advanced_OOP/01_Friend_Functions_and_Classes.md

# Friend Functions and Classes in C++ - Complete Guide

## 📖 Overview

Friend functions and classes are a powerful feature in C++ that allow external functions or classes to access the private and protected members of a class. While this breaks encapsulation, it is sometimes necessary for certain design patterns, operator overloading, and when two classes need to work closely together.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Friend Function** | Non-member function that can access private/protected members |
| **Friend Class** | Class whose all member functions can access private/protected members |
| **Friend Member Function** | Specific member function of another class granted friendship |
| **Encapsulation** | Friendship breaks encapsulation - use sparingly |

---

## 1. **Friend Functions**

```cpp
#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    double balance;
    string pin;
    
public:
    BankAccount(string acc, double bal, string p) 
        : accountNumber(acc), balance(bal), pin(p) {}
    
    // Friend function declaration
    friend void displayAccount(const BankAccount& acc);
    friend void transfer(BankAccount& from, BankAccount& to, double amount);
    
    double getBalance() const { return balance; }
};

// Friend function definitions - can access private members
void displayAccount(const BankAccount& acc) {
    cout << "Account: " << acc.accountNumber << endl;
    cout << "Balance: $" << acc.balance << endl;
    // Can also access PIN if needed, but shouldn't expose it
}

void transfer(BankAccount& from, BankAccount& to, double amount) {
    if (amount > 0 && amount <= from.balance) {
        from.balance -= amount;
        to.balance += amount;
        cout << "Transferred $" << amount << " from " 
             << from.accountNumber << " to " << to.accountNumber << endl;
    } else {
        cout << "Transfer failed: Insufficient funds!" << endl;
    }
}

class Complex {
private:
    double real, imag;
    
public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}
    
    // Friend function for operator overloading
    friend Complex operator+(const Complex& a, const Complex& b);
    friend ostream& operator<<(ostream& os, const Complex& c);
};

Complex operator+(const Complex& a, const Complex& b) {
    return Complex(a.real + b.real, a.imag + b.imag);
}

ostream& operator<<(ostream& os, const Complex& c) {
    os << c.real;
    if (c.imag >= 0) os << " + " << c.imag << "i";
    else os << " - " << -c.imag << "i";
    return os;
}

int main() {
    cout << "=== Friend Functions ===" << endl;
    
    BankAccount acc1("12345678", 1000, "1234");
    BankAccount acc2("87654321", 500, "5678");
    
    cout << "\n1. Friend function accessing private members:" << endl;
    displayAccount(acc1);
    displayAccount(acc2);
    
    cout << "\n2. Friend function modifying private members:" << endl;
    transfer(acc1, acc2, 300);
    
    cout << "\nAfter transfer:" << endl;
    displayAccount(acc1);
    displayAccount(acc2);
    
    cout << "\n3. Friend function for operator overloading:" << endl;
    Complex c1(3, 4);
    Complex c2(1, -2);
    Complex c3 = c1 + c2;
    cout << c1 << " + " << c2 << " = " << c3 << endl;
    
    return 0;
}
```

**Output:**
```
=== Friend Functions ===

1. Friend function accessing private members:
Account: 12345678
Balance: $1000
Account: 87654321
Balance: $500

2. Friend function modifying private members:
Transferred $300 from 12345678 to 87654321

After transfer:
Account: 12345678
Balance: $700
Account: 87654321
Balance: $800

3. Friend function for operator overloading:
3 + 4i + 1 - 2i = 4 + 2i
```

---

## 2. **Friend Classes**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Engine {
private:
    int horsepower;
    string type;
    bool running;
    
public:
    Engine(int hp, string t) : horsepower(hp), type(t), running(false) {}
    
    void start() { running = true; }
    void stop() { running = false; }
    
    friend class Car;  // Car can access Engine's private members
};

class Car {
private:
    string model;
    Engine engine;
    vector<string> features;
    
public:
    Car(string m, int hp, string engineType) 
        : model(m), engine(hp, engineType) {}
    
    // Can access Engine's private members
    void start() {
        engine.start();
        cout << model << " with " << engine.horsepower << "hp "
             << engine.type << " engine started" << endl;
    }
    
    void stop() {
        engine.stop();
        cout << model << " stopped" << endl;
    }
    
    void addFeature(const string& feature) {
        features.push_back(feature);
    }
    
    // Friend class declaration
    friend class Mechanic;
};

class Mechanic {
public:
    // Can access Car's private members
    void inspect(const Car& car) {
        cout << "Inspecting " << car.model << ":" << endl;
        cout << "  Engine: " << car.engine.horsepower << "hp "
             << car.engine.type << endl;
        cout << "  Features: ";
        for (const auto& f : car.features) {
            cout << f << " ";
        }
        cout << endl;
    }
    
    void modifyEngine(Car& car, int newHorsepower) {
        car.engine.horsepower = newHorsepower;
        cout << "Engine horsepower upgraded to " << newHorsepower << endl;
    }
};

int main() {
    cout << "=== Friend Classes ===" << endl;
    
    Car myCar("Tesla Model 3", 300, "Electric");
    myCar.addFeature("Autopilot");
    myCar.addFeature("Heated Seats");
    
    cout << "\n1. Starting the car:" << endl;
    myCar.start();
    
    cout << "\n2. Mechanic inspection (friend class):" << endl;
    Mechanic mechanic;
    mechanic.inspect(myCar);
    
    cout << "\n3. Mechanic modifying engine (private member):" << endl;
    mechanic.modifyEngine(myCar, 350);
    
    cout << "\n4. Starting upgraded car:" << endl;
    myCar.start();
    myCar.stop();
    
    return 0;
}
```

---

## 3. **Friend Member Functions**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Forward declaration
class Container;

class Iterator {
private:
    int index;
    
public:
    Iterator() : index(0) {}
    
    // Declaration of friend member function
    void reset(Container& c);
    void next(Container& c);
    bool hasNext(const Container& c);
    int getCurrent(const Container& c);
};

class Container {
private:
    int data[10];
    int size;
    
public:
    Container() : size(0) {
        for (int i = 0; i < 10; i++) data[i] = 0;
    }
    
    void add(int value) {
        if (size < 10) {
            data[size++] = value;
        }
    }
    
    // Grant friendship to specific member functions
    friend void Iterator::reset(Container& c);
    friend void Iterator::next(Container& c);
    friend bool Iterator::hasNext(const Container& c);
    friend int Iterator::getCurrent(const Container& c);
};

// Iterator member function definitions (can access Container's private members)
void Iterator::reset(Container& c) {
    index = 0;
}

void Iterator::next(Container& c) {
    if (index < c.size) {
        index++;
    }
}

bool Iterator::hasNext(const Container& c) {
    return index < c.size;
}

int Iterator::getCurrent(const Container& c) {
    if (index < c.size) {
        return c.data[index];
    }
    return -1;
}

class DataProcessor;

class DataStore {
private:
    int values[100];
    int count;
    
public:
    DataStore() : count(0) {}
    
    void add(int val) {
        if (count < 100) {
            values[count++] = val;
        }
    }
    
    // Friend class
    friend class DataProcessor;
};

class DataProcessor {
public:
    // Can access all private members of DataStore
    int sum(const DataStore& ds) {
        int total = 0;
        for (int i = 0; i < ds.count; i++) {
            total += ds.values[i];
        }
        return total;
    }
    
    double average(const DataStore& ds) {
        if (ds.count == 0) return 0;
        return static_cast<double>(sum(ds)) / ds.count;
    }
    
    int max(const DataStore& ds) {
        if (ds.count == 0) return 0;
        int maxVal = ds.values[0];
        for (int i = 1; i < ds.count; i++) {
            if (ds.values[i] > maxVal) maxVal = ds.values[i];
        }
        return maxVal;
    }
};

int main() {
    cout << "=== Friend Member Functions ===" << endl;
    
    Container container;
    container.add(10);
    container.add(20);
    container.add(30);
    container.add(40);
    container.add(50);
    
    Iterator iter;
    
    cout << "\n1. Iterating through container:" << endl;
    iter.reset(container);
    while (iter.hasNext(container)) {
        cout << iter.getCurrent(container) << " ";
        iter.next(container);
    }
    cout << endl;
    
    cout << "\n2. DataStore and DataProcessor (friend class):" << endl;
    DataStore store;
    store.add(5);
    store.add(15);
    store.add(25);
    store.add(35);
    store.add(45);
    
    DataProcessor processor;
    cout << "Sum: " << processor.sum(store) << endl;
    cout << "Average: " << processor.average(store) << endl;
    cout << "Max: " << processor.max(store) << endl;
    
    return 0;
}
```

---

## 4. **Friend Functions in Multiple Classes**

```cpp
#include <iostream>
#include <string>
using namespace std;

class A;
class B;

class A {
private:
    int valueA;
    
public:
    A(int v) : valueA(v) {}
    
    // Friend function that accesses both A and B
    friend void exchange(A& a, B& b);
    friend void displayBoth(const A& a, const B& b);
    
    int getValue() const { return valueA; }
};

class B {
private:
    int valueB;
    
public:
    B(int v) : valueB(v) {}
    
    // Friend function that accesses both A and B
    friend void exchange(A& a, B& b);
    friend void displayBoth(const A& a, const B& b);
    
    int getValue() const { return valueB; }
};

// Friend function that can access private members of both A and B
void exchange(A& a, B& b) {
    int temp = a.valueA;
    a.valueA = b.valueB;
    b.valueB = temp;
    cout << "Values exchanged!" << endl;
}

void displayBoth(const A& a, const B& b) {
    cout << "A value: " << a.valueA << ", B value: " << b.valueB << endl;
}

class Matrix;
class Vector;

class Matrix {
private:
    int data[3][3];
    
public:
    Matrix() {
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                data[i][j] = (i == j) ? 1 : 0;  // Identity matrix
    }
    
    void set(int i, int j, int val) { data[i][j] = val; }
    
    friend Vector operator*(const Matrix& m, const Vector& v);
};

class Vector {
private:
    int data[3];
    
public:
    Vector(int x = 0, int y = 0, int z = 0) {
        data[0] = x;
        data[1] = y;
        data[2] = z;
    }
    
    friend Vector operator*(const Matrix& m, const Vector& v);
    
    void display() const {
        cout << "(" << data[0] << ", " << data[1] << ", " << data[2] << ")" << endl;
    }
};

// Friend function multiplying matrix and vector
Vector operator*(const Matrix& m, const Vector& v) {
    Vector result;
    for (int i = 0; i < 3; i++) {
        result.data[i] = 0;
        for (int j = 0; j < 3; j++) {
            result.data[i] += m.data[i][j] * v.data[j];
        }
    }
    return result;
}

int main() {
    cout << "=== Friend Functions in Multiple Classes ===" << endl;
    
    cout << "\n1. Exchange values between A and B:" << endl;
    A a(10);
    B b(20);
    
    displayBoth(a, b);
    exchange(a, b);
    displayBoth(a, b);
    
    cout << "\n2. Matrix-Vector multiplication:" << endl;
    Matrix m;
    m.set(0, 0, 2);
    m.set(1, 1, 3);
    m.set(2, 2, 4);
    
    Vector v(1, 2, 3);
    
    Vector result = m * v;
    cout << "Matrix * Vector = ";
    result.display();
    
    return 0;
}
```

---

## 5. **When to Use Friends**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Example 1: Operator overloading (good use of friends)
class Rational {
private:
    int numerator;
    int denominator;
    
    void simplify() {
        int gcd = 1;
        for (int i = 2; i <= abs(numerator) && i <= abs(denominator); i++) {
            if (numerator % i == 0 && denominator % i == 0) {
                gcd = i;
            }
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
    
    // Friend operators for symmetric operations
    friend Rational operator+(const Rational& a, const Rational& b);
    friend ostream& operator<<(ostream& os, const Rational& r);
};

Rational operator+(const Rational& a, const Rational& b) {
    return Rational(
        a.numerator * b.denominator + b.numerator * a.denominator,
        a.denominator * b.denominator
    );
}

ostream& operator<<(ostream& os, const Rational& r) {
    if (r.denominator == 1) {
        os << r.numerator;
    } else {
        os << r.numerator << "/" << r.denominator;
    }
    return os;
}

// Example 2: Two closely coupled classes (acceptable use)
class Node;
class LinkedList {
private:
    Node* head;
    
public:
    LinkedList() : head(nullptr) {}
    ~LinkedList();
    
    void add(int value);
    void display();
    
    friend class Node;  // Node needs to access LinkedList's head? Actually not needed
};

class Node {
private:
    int data;
    Node* next;
    
public:
    Node(int val) : data(val), next(nullptr) {}
    
    friend class LinkedList;  // LinkedList needs to access Node's private members
};

LinkedList::~LinkedList() {
    Node* current = head;
    while (current) {
        Node* next = current->next;
        delete current;
        current = next;
    }
}

void LinkedList::add(int value) {
    Node* newNode = new Node(value);
    newNode->next = head;
    head = newNode;  // Can access Node's next because of friendship
}

void LinkedList::display() {
    Node* current = head;
    while (current) {
        cout << current->data << " ";  // Can access Node's data
        current = current->next;
    }
    cout << endl;
}

// Example 3: Test/Diagnostic class (good use)
class Database {
private:
    string connectionString;
    bool connected;
    int queryCount;
    
public:
    Database(string conn) : connectionString(conn), connected(false), queryCount(0) {}
    
    void connect() {
        connected = true;
        cout << "Connected to " << connectionString << endl;
    }
    
    void query(const string& sql) {
        if (connected) {
            queryCount++;
            cout << "Executing: " << sql << endl;
        }
    }
    
    // Friend for testing/debugging
    friend class DatabaseTester;
};

class DatabaseTester {
public:
    static void testConnection(Database& db) {
        cout << "Testing database: " << db.connectionString << endl;
        cout << "Connected: " << (db.connected ? "Yes" : "No") << endl;
        cout << "Query count: " << db.queryCount << endl;
    }
    
    static void forceConnect(Database& db) {
        db.connected = true;
        cout << "Forced connection" << endl;
    }
};

int main() {
    cout << "=== When to Use Friends ===" << endl;
    
    cout << "\n1. Operator overloading (good use):" << endl;
    Rational r1(1, 2);
    Rational r2(1, 3);
    cout << r1 << " + " << r2 << " = " << (r1 + r2) << endl;
    
    cout << "\n2. Closely coupled classes (LinkedList/Node):" << endl;
    LinkedList list;
    list.add(10);
    list.add(20);
    list.add(30);
    list.display();
    
    cout << "\n3. Testing/Diagnostic classes (good use):" << endl;
    Database db("postgresql://localhost/mydb");
    DatabaseTester::testConnection(db);
    db.connect();
    db.query("SELECT * FROM users");
    DatabaseTester::testConnection(db);
    
    cout << "\nGuidelines for using friends:" << endl;
    cout << "  ✓ Use for operator overloading (symmetry)" << endl;
    cout << "  ✓ Use for closely coupled classes (container/element)" << endl;
    cout << "  ✓ Use for testing/diagnostic classes" << endl;
    cout << "  ✗ Avoid for convenience when getters/setters work" << endl;
    cout << "  ✗ Avoid overuse - breaks encapsulation" << endl;
    
    return 0;
}
```

---

## 📊 Friend Functions and Classes Summary

| Type | Declaration | Scope | Use Case |
|------|-------------|-------|----------|
| **Friend Function** | `friend void func();` | Non-member | Operator overloading, helpers |
| **Friend Class** | `friend class ClassName;` | All members | Tight coupling, container/element |
| **Friend Member** | `friend void Class::func();` | Specific member | Limited access |

---

## ✅ Best Practices

1. **Use friends sparingly** - They break encapsulation
2. **Prefer getters/setters** when possible
3. **Use for operator overloading** (symmetry requirement)
4. **Use for testing/diagnostics** (legitimate use)
5. **Document friendship** in class comments
6. **Consider alternatives** (public interfaces, design patterns)

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Overusing friends** | Tight coupling | Use public interface when possible |
| **Circular friendship** | A needs B, B needs A | Redesign to avoid |
| **Friend in header** | Exposes implementation | Keep minimal |
| **Not forward declaring** | Compilation errors | Proper forward declarations |

---

## ✅ Key Takeaways

1. **Friend functions** access private members from outside
2. **Friend classes** give all members access to another class
3. **Use for operator overloading** when left operand is not class type
4. **Use for closely coupled classes** (container/element)
5. **Use for testing** to access internal state
6. **Break encapsulation deliberately** - use with caution

---