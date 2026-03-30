# Access Specifiers in C++ - Complete Guide

## 📖 Overview

Access specifiers (also called access modifiers) control the visibility and accessibility of class members (data and functions). They are fundamental to **encapsulation**, one of the core principles of Object-Oriented Programming. C++ provides three access specifiers: `public`, `private`, and `protected`.

---

## 🎯 The Three Access Specifiers

| Specifier | Class Access | Derived Class Access | External Access | Purpose |
|-----------|--------------|---------------------|-----------------|---------|
| **public** | ✓ Yes | ✓ Yes | ✓ Yes | Interface for users |
| **private** | ✓ Yes | ✗ No | ✗ No | Implementation details, data hiding |
| **protected** | ✓ Yes | ✓ Yes | ✗ No | For inheritance hierarchies |

---

## 1. **Public Access Specifier**

### Definition
Members declared as `public` are accessible from anywhere in the program. They form the **interface** of the class.

```cpp
#include <iostream>
#include <string>
using namespace std;

class PublicExample {
public:
    // Public data members (generally not recommended)
    string name;
    int age;
    
    // Public member functions
    void display() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
    
    void setName(string n) {
        name = n;
    }
    
    void setAge(int a) {
        if (a >= 0 && a <= 150) {
            age = a;
        }
    }
};

int main() {
    PublicExample obj;
    
    // Accessible from anywhere
    obj.name = "Alice";
    obj.age = 25;
    obj.display();
    
    obj.setName("Bob");
    obj.setAge(30);
    obj.display();
    
    return 0;
}
```

**Output:**
```
Name: Alice, Age: 25
Name: Bob, Age: 30
```

---

## 2. **Private Access Specifier**

### Definition
Members declared as `private` are accessible only within the class itself. They cannot be accessed from outside the class or from derived classes. This is the default access for class members.

```cpp
#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
    // Private data members - hidden from outside
    string accountNumber;
    double balance;
    string pin;
    
    // Private helper function
    bool validatePin(string inputPin) {
        return pin == inputPin;
    }
    
public:
    // Public interface
    BankAccount(string accNo, double initial, string p) {
        accountNumber = accNo;
        balance = initial;
        pin = p;
    }
    
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited: $" << amount << endl;
        }
    }
    
    bool withdraw(double amount, string inputPin) {
        if (!validatePin(inputPin)) {
            cout << "Invalid PIN!" << endl;
            return false;
        }
        
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            cout << "Withdrawn: $" << amount << endl;
            return true;
        }
        cout << "Insufficient funds!" << endl;
        return false;
    }
    
    double getBalance(string inputPin) {
        if (validatePin(inputPin)) {
            return balance;
        }
        return -1;
    }
};

int main() {
    BankAccount account("12345678", 1000, "1234");
    
    // Cannot access private members directly
    // account.balance = 9999;        // Error!
    // account.pin = "9999";          // Error!
    // account.validatePin("1234");   // Error!
    
    // Must use public interface
    account.deposit(500);
    account.withdraw(200, "1234");
    cout << "Balance: $" << account.getBalance("1234") << endl;
    
    // Wrong PIN - access denied
    account.withdraw(100, "9999");
    
    return 0;
}
```

**Output:**
```
Deposited: $500
Withdrawn: $200
Balance: $1300
Invalid PIN!
```

---

## 3. **Protected Access Specifier**

### Definition
Members declared as `protected` are accessible within the class itself and in derived classes, but not from outside the class hierarchy.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Base class
class Animal {
protected:
    // Protected data members - accessible in derived classes
    string name;
    int age;
    
public:
    Animal(string n, int a) : name(n), age(a) {}
    
    void display() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

// Derived class
class Dog : public Animal {
private:
    string breed;
    
public:
    Dog(string n, int a, string b) : Animal(n, a), breed(b) {}
    
    void bark() {
        cout << name << " says: Woof!" << endl;  // Can access protected 'name'
        // age is also accessible here
    }
    
    void display() {
        Animal::display();
        cout << "Breed: " << breed << endl;
    }
};

int main() {
    Dog dog("Buddy", 3, "Golden Retriever");
    
    dog.display();
    dog.bark();
    
    // Cannot access protected members directly
    // dog.name = "Max";     // Error! Protected member not accessible outside class hierarchy
    // dog.age = 5;          // Error! Protected member not accessible
    
    return 0;
}
```

**Output:**
```
Name: Buddy, Age: 3
Breed: Golden Retriever
Buddy says: Woof!
```

---

## 📊 Comparison with Examples

### Complete Example Showing All Three

```cpp
#include <iostream>
#include <string>
using namespace std;

class AccessDemo {
private:
    int privateVar;
    
protected:
    int protectedVar;
    
public:
    int publicVar;
    
    // Constructor
    AccessDemo() : privateVar(10), protectedVar(20), publicVar(30) {}
    
    // Public methods to demonstrate access
    void showAccess() {
        cout << "Inside class:" << endl;
        cout << "  privateVar = " << privateVar << endl;    // ✓ Accessible
        cout << "  protectedVar = " << protectedVar << endl; // ✓ Accessible
        cout << "  publicVar = " << publicVar << endl;       // ✓ Accessible
    }
    
    void modifyPrivate(int value) {
        privateVar = value;  // ✓ Can modify private members
    }
    
    int getPrivate() {
        return privateVar;   // ✓ Can access private members
    }
};

class Derived : public AccessDemo {
public:
    void showDerivedAccess() {
        cout << "Inside derived class:" << endl;
        // cout << "  privateVar = " << privateVar << endl;  // ✗ Error! Not accessible
        cout << "  protectedVar = " << protectedVar << endl; // ✓ Accessible (inherited)
        cout << "  publicVar = " << publicVar << endl;       // ✓ Accessible
    }
    
    void modifyProtected(int value) {
        protectedVar = value;  // ✓ Can modify protected members
    }
    
    int getProtected() {
        return protectedVar;   // ✓ Can access protected members
    }
};

int main() {
    AccessDemo obj;
    Derived derived;
    
    cout << "=== Access from main (outside class) ===\n";
    // cout << obj.privateVar << endl;    // ✗ Error: private
    // cout << obj.protectedVar << endl;  // ✗ Error: protected
    cout << "obj.publicVar = " << obj.publicVar << endl;  // ✓ OK
    
    cout << "\n=== Access through public interface ===\n";
    obj.showAccess();
    obj.modifyPrivate(100);
    cout << "Modified privateVar = " << obj.getPrivate() << endl;
    
    cout << "\n=== Access from derived class ===\n";
    derived.showDerivedAccess();
    derived.modifyProtected(200);
    cout << "Modified protectedVar (via getter) = " << derived.getProtected() << endl;
    derived.publicVar = 300;
    cout << "Modified publicVar = " << derived.publicVar << endl;
    
    return 0;
}
```

**Output:**
```
=== Access from main (outside class) ===
obj.publicVar = 30

=== Access through public interface ===
Inside class:
  privateVar = 10
  protectedVar = 20
  publicVar = 30
Modified privateVar = 100

=== Access from derived class ===
Inside derived class:
  protectedVar = 20
  publicVar = 30
Modified protectedVar (via getter) = 200
Modified publicVar = 300
```

---

## 🏗️ Class Default Access

### Struct vs Class Defaults

```cpp
#include <iostream>
using namespace std;

// struct: default access is public
struct PointStruct {
    int x;      // public by default
    int y;      // public by default
    
    void display() {  // public by default
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

// class: default access is private
class PointClass {
    int x;      // private by default
    int y;      // private by default
    
    void display() {  // private by default
        cout << "(" << x << ", " << y << ")" << endl;
    }
    
public:
    void setX(int val) { x = val; }
    void setY(int val) { y = val; }
    void show() { display(); }
};

int main() {
    PointStruct ps;
    ps.x = 10;      // ✓ OK - public
    ps.y = 20;      // ✓ OK - public
    ps.display();   // ✓ OK - public
    
    PointClass pc;
    // pc.x = 10;   // ✗ Error - private
    // pc.display(); // ✗ Error - private
    pc.setX(10);    // ✓ OK - public method
    pc.setY(20);    // ✓ OK - public method
    pc.show();      // ✓ OK - public method
    
    return 0;
}
```

---

## 🔧 Access Specifiers in Inheritance

### Public, Protected, and Private Inheritance

```cpp
#include <iostream>
using namespace std;

class Base {
private:
    int privateMember = 1;
protected:
    int protectedMember = 2;
public:
    int publicMember = 3;
    
    void showBase() {
        cout << "Base: private=" << privateMember 
             << ", protected=" << protectedMember 
             << ", public=" << publicMember << endl;
    }
};

// Public Inheritance
class PublicDerived : public Base {
public:
    void show() {
        // cout << privateMember << endl;  // ✗ Error: private not accessible
        cout << "PublicDerived - protectedMember: " << protectedMember << endl;  // ✓ Accessible
        cout << "PublicDerived - publicMember: " << publicMember << endl;         // ✓ Accessible
    }
};

// Protected Inheritance
class ProtectedDerived : protected Base {
public:
    void show() {
        cout << "ProtectedDerived - protectedMember: " << protectedMember << endl;
        cout << "ProtectedDerived - publicMember: " << publicMember << endl;
    }
};

// Private Inheritance
class PrivateDerived : private Base {
public:
    void show() {
        cout << "PrivateDerived - protectedMember: " << protectedMember << endl;
        cout << "PrivateDerived - publicMember: " << publicMember << endl;
    }
};

int main() {
    PublicDerived pub;
    pub.show();
    pub.publicMember = 100;     // ✓ OK - public in derived
    // pub.protectedMember = 200;  // ✗ Error - protected in derived
    
    ProtectedDerived prot;
    prot.show();
    // prot.publicMember = 100;    // ✗ Error - now protected in derived
    
    PrivateDerived priv;
    priv.show();
    // priv.publicMember = 100;     // ✗ Error - now private in derived
    
    return 0;
}
```

---

## 📊 Access Specifier Summary Table

| Where Accessed | public | protected | private |
|----------------|--------|-----------|---------|
| Same class | ✓ Yes | ✓ Yes | ✓ Yes |
| Derived class | ✓ Yes | ✓ Yes | ✗ No |
| Outside class | ✓ Yes | ✗ No | ✗ No |
| Friends | ✓ Yes | ✓ Yes | ✓ Yes |

---

## 🎯 Best Practices

### 1. **Keep Data Private**
```cpp
class Employee {
private:
    string name;      // ✓ Good: private data
    double salary;    // ✓ Good: private data
    
public:
    // ✓ Good: public interface
    void setName(string n) { name = n; }
    string getName() const { return name; }
    
    void setSalary(double s) {
        if (s >= 0) salary = s;  // Validation
    }
    
    double getSalary() const { return salary; }
};
```

### 2. **Use Protected for Inheritance**
```cpp
class Shape {
protected:
    int x, y;  // ✓ Good: accessible to derived classes
    
public:
    virtual double area() const = 0;
    virtual void draw() const = 0;
};

class Circle : public Shape {
private:
    double radius;  // ✓ Good: private to Circle
    
public:
    double area() const override {
        return 3.14159 * radius * radius;
    }
};
```

### 3. **Interface Should Be Public**
```cpp
class Database {
public:
    // ✓ Good: public interface for users
    void connect();
    void disconnect();
    void executeQuery(const string& query);
    
private:
    // ✓ Good: implementation details hidden
    void establishConnection();
    void closeConnection();
    string connectionString;
    bool isConnected;
};
```

---

## 🐛 Common Pitfalls

| Pitfall | Example | Solution |
|---------|---------|----------|
| **Public data members** | `public: int age;` | Make private, use getters/setters |
| **Overly restrictive access** | Making everything private | Use protected for inheritance |
| **Overly permissive access** | Making everything public | Encapsulate, hide implementation |
| **Forgetting default access** | `class MyClass { int x; };` | Be explicit with access specifiers |
| **Incorrect inheritance access** | `class Derived : Base` (private by default) | Specify `public`, `protected`, or `private` |

---

## ✅ Key Takeaways

1. **`public`**: Interface for users, accessible everywhere
2. **`private`**: Implementation details, accessible only within class
3. **`protected`**: For inheritance, accessible in derived classes
4. **Encapsulation**: Hide data, expose interface
5. **Default access**: `struct` = public, `class` = private
6. **Inheritance access**: Specifies how base members are inherited

---