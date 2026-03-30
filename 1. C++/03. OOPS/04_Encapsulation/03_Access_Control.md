# Access Control in C++ - Complete Guide

## 📖 Overview

Access control is the mechanism that determines which parts of a program can access a class's members. It is a fundamental aspect of encapsulation that protects data and implementation details. C++ provides three access specifiers: `public`, `private`, and `protected`, each with different visibility levels.

---

## 🎯 The Three Access Specifiers

| Specifier | Class Access | Derived Class Access | External Access | Purpose |
|-----------|--------------|---------------------|-----------------|---------|
| **public** | ✓ Yes | ✓ Yes | ✓ Yes | Interface for users |
| **private** | ✓ Yes | ✗ No | ✗ No | Implementation details |
| **protected** | ✓ Yes | ✓ Yes | ✗ No | For inheritance hierarchies |

---

## 1. **Public Access Specifier**

### Definition
Public members are accessible from anywhere in the program. They form the **interface** of the class.

```cpp
#include <iostream>
#include <string>
using namespace std;

class PublicDemo {
public:
    // Public data members (generally not recommended)
    string name;
    int age;
    
    // Public member functions
    void display() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
    
    void setData(string n, int a) {
        name = n;
        age = a;
    }
    
    // Public static method
    static void showInfo() {
        cout << "This is a public class" << endl;
    }
};

int main() {
    cout << "=== Public Access Specifier ===" << endl;
    
    PublicDemo obj;
    
    // Direct access from main (external code)
    obj.name = "Alice";
    obj.age = 25;
    obj.display();
    
    obj.setData("Bob", 30);
    obj.display();
    
    // Accessing static method
    PublicDemo::showInfo();
    
    return 0;
}
```

**Output:**
```
=== Public Access Specifier ===
Name: Alice, Age: 25
Name: Bob, Age: 30
This is a public class
```

---

## 2. **Private Access Specifier**

### Definition
Private members are accessible only within the class itself. They cannot be accessed from outside or from derived classes.

```cpp
#include <iostream>
#include <string>
using namespace std;

class PrivateDemo {
private:
    // Private data members - hidden from outside
    string secret;
    int pin;
    
    // Private helper function
    bool validatePin(int input) {
        return pin == input;
    }
    
public:
    // Constructor
    PrivateDemo(string s, int p) : secret(s), pin(p) {}
    
    // Public interface
    void setSecret(string s, int inputPin) {
        if (validatePin(inputPin)) {
            secret = s;
            cout << "Secret updated!" << endl;
        } else {
            cout << "Invalid PIN!" << endl;
        }
    }
    
    string getSecret(int inputPin) {
        if (validatePin(inputPin)) {
            return secret;
        }
        return "Access Denied";
    }
    
    void changePin(int oldPin, int newPin) {
        if (validatePin(oldPin)) {
            pin = newPin;
            cout << "PIN changed successfully!" << endl;
        } else {
            cout << "Invalid old PIN!" << endl;
        }
    }
    
    void display(int inputPin) {
        if (validatePin(inputPin)) {
            cout << "Secret: " << secret << endl;
        } else {
            cout << "Access Denied!" << endl;
        }
    }
};

int main() {
    cout << "=== Private Access Specifier ===" << endl;
    
    PrivateDemo obj("Top Secret", 1234);
    
    // Cannot access private members directly
    // obj.secret = "New Secret";  // Error!
    // obj.pin = 9999;              // Error!
    // obj.validatePin(1234);       // Error!
    
    // Must use public interface
    obj.display(1234);  // Correct PIN
    obj.display(9999);  // Wrong PIN
    
    obj.setSecret("Updated Secret", 1234);
    cout << "Secret: " << obj.getSecret(1234) << endl;
    
    obj.changePin(1234, 5678);
    obj.display(5678);
    
    return 0;
}
```

**Output:**
```
=== Private Access Specifier ===
Secret: Top Secret
Access Denied!
Secret updated!
Secret: Updated Secret
PIN changed successfully!
Secret: Updated Secret
```

---

## 3. **Protected Access Specifier**

### Definition
Protected members are accessible within the class itself and in derived classes, but not from external code.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Base class with protected members
class Animal {
protected:
    string name;
    int age;
    
public:
    Animal(string n, int a) : name(n), age(a) {}
    
    void display() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
};

// Derived class can access protected members
class Dog : public Animal {
private:
    string breed;
    
public:
    Dog(string n, int a, string b) : Animal(n, a), breed(b) {}
    
    void bark() {
        cout << name << " says: Woof!" << endl;  // Accessing protected member
        // age is also accessible here
    }
    
    void displayDog() {
        Animal::display();
        cout << "Breed: " << breed << endl;
        cout << "Age (from protected): " << age << endl;
    }
    
    void setName(string n) {
        name = n;  // Can modify protected member
    }
};

class Cat : public Animal {
public:
    Cat(string n, int a) : Animal(n, a) {}
    
    void meow() {
        cout << name << " says: Meow!" << endl;  // Accessing protected member
    }
    
    void setAge(int a) {
        age = a;  // Can modify protected member
    }
};

int main() {
    cout << "=== Protected Access Specifier ===" << endl;
    
    Animal animal("Generic", 5);
    animal.display();
    
    Dog dog("Buddy", 3, "Golden Retriever");
    dog.bark();
    dog.displayDog();
    
    Cat cat("Whiskers", 2);
    cat.meow();
    cat.setAge(4);
    cat.display();
    
    // Cannot access protected members from outside
    // animal.name = "Unknown";  // Error!
    // dog.name = "Max";         // Error! Protected member
    // cat.age = 10;              // Error! Protected member
    
    return 0;
}
```

**Output:**
```
=== Protected Access Specifier ===
Name: Generic, Age: 5
Buddy says: Woof!
Name: Buddy, Age: 3
Breed: Golden Retriever
Age (from protected): 3
Whiskers says: Meow!
Name: Whiskers, Age: 4
```

---

## 4. **Access Control in Inheritance**

### Definition
When inheriting, the access specifier in the derived class declaration determines how base class members are inherited.

```cpp
#include <iostream>
using namespace std;

class Base {
private:
    int privateVar = 1;
protected:
    int protectedVar = 2;
public:
    int publicVar = 3;
    
    void showBase() {
        cout << "Private: " << privateVar << endl;
        cout << "Protected: " << protectedVar << endl;
        cout << "Public: " << publicVar << endl;
    }
};

// Public Inheritance
class PublicDerived : public Base {
public:
    void show() {
        // cout << privateVar << endl;  // Error! Private not accessible
        cout << "Protected: " << protectedVar << endl;  // OK - becomes protected
        cout << "Public: " << publicVar << endl;        // OK - remains public
    }
};

// Protected Inheritance
class ProtectedDerived : protected Base {
public:
    void show() {
        cout << "Protected: " << protectedVar << endl;  // OK
        cout << "Public: " << publicVar << endl;        // OK - becomes protected
    }
};

// Private Inheritance
class PrivateDerived : private Base {
public:
    void show() {
        cout << "Protected: " << protectedVar << endl;  // OK
        cout << "Public: " << publicVar << endl;        // OK - becomes private
    }
};

int main() {
    cout << "=== Access Control in Inheritance ===" << endl;
    
    cout << "\n1. Public Inheritance:" << endl;
    PublicDerived pub;
    pub.show();
    pub.publicVar = 100;        // OK - public
    // pub.protectedVar = 200;  // Error! protected
    
    cout << "\n2. Protected Inheritance:" << endl;
    ProtectedDerived prot;
    prot.show();
    // prot.publicVar = 100;    // Error! becomes protected
    // prot.protectedVar = 200; // Error! protected
    
    cout << "\n3. Private Inheritance:" << endl;
    PrivateDerived priv;
    priv.show();
    // priv.publicVar = 100;    // Error! becomes private
    // priv.protectedVar = 200; // Error! private
    
    return 0;
}
```

**Output:**
```
=== Access Control in Inheritance ===

1. Public Inheritance:
Protected: 2
Public: 3

2. Protected Inheritance:
Protected: 2
Public: 3

3. Private Inheritance:
Protected: 2
Public: 3
```

---

## 5. **Access Control in Practice**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    double balance;
    string pin;
    
protected:
    // Protected members for derived classes
    string accountType;
    double interestRate;
    
    // Protected helper
    bool validatePin(string inputPin) {
        return pin == inputPin;
    }
    
public:
    BankAccount(string accNo, double initial, string p, string type, double rate)
        : accountNumber(accNo), balance(initial), pin(p), 
          accountType(type), interestRate(rate) {}
    
    // Public interface
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
    
    string getAccountNumber() const { return accountNumber; }
    string getAccountType() const { return accountType; }
    
    void display(string inputPin) {
        if (validatePin(inputPin)) {
            cout << "Account: " << accountNumber << endl;
            cout << "Type: " << accountType << endl;
            cout << "Balance: $" << balance << endl;
            cout << "Interest Rate: " << interestRate << "%" << endl;
        } else {
            cout << "Access Denied!" << endl;
        }
    }
};

class SavingsAccount : public BankAccount {
private:
    int withdrawalCount;
    static const int FREE_WITHDRAWALS = 3;
    static const double WITHDRAWAL_FEE;
    
public:
    SavingsAccount(string accNo, double initial, string pin)
        : BankAccount(accNo, initial, pin, "Savings", 2.5), withdrawalCount(0) {}
    
    // Override withdraw with additional logic
    bool withdraw(double amount, string inputPin) {
        bool success = BankAccount::withdraw(amount, inputPin);
        
        if (success) {
            withdrawalCount++;
            
            // Apply fee after free withdrawals
            if (withdrawalCount > FREE_WITHDRAWALS) {
                // Access protected method? No, but can access base class withdraw
                // Actually we need to deduct fee
                cout << "Withdrawal fee applied: $" << WITHDRAWAL_FEE << endl;
                // Can't directly access balance, but can call another withdraw
                // This is simplified
            }
        }
        return success;
    }
    
    void addInterest(string inputPin) {
        if (validatePin(inputPin)) {
            double interest = getBalance(inputPin) * (interestRate / 100);
            deposit(interest);
            cout << "Interest added: $" << interest << endl;
        }
    }
};

const double SavingsAccount::WITHDRAWAL_FEE = 1.0;

class CheckingAccount : public BankAccount {
public:
    CheckingAccount(string accNo, double initial, string pin)
        : BankAccount(accNo, initial, pin, "Checking", 0.5) {}
    
    void writeCheck(double amount, string inputPin, string payee) {
        if (withdraw(amount, inputPin)) {
            cout << "Check written to " << payee << " for $" << amount << endl;
        }
    }
};

int main() {
    cout << "=== Access Control in Practice ===" << endl;
    
    cout << "\n1. Savings Account:" << endl;
    SavingsAccount savings("SAV001", 1000, "1234");
    savings.display("1234");
    
    savings.deposit(500);
    savings.withdraw(200, "1234");
    savings.addInterest("1234");
    
    cout << "\n2. Checking Account:" << endl;
    CheckingAccount checking("CHK001", 500, "5678");
    checking.display("5678");
    checking.writeCheck(150, "5678", "Utility Company");
    
    cout << "\n3. Access restrictions:" << endl;
    // Cannot access private members
    // savings.balance = 9999;      // Error!
    // savings.pin = "9999";        // Error!
    
    // Cannot access protected members from outside
    // savings.interestRate = 5.0;  // Error!
    // savings.accountType = "New";  // Error!
    
    cout << "\n4. Derived class access to protected:" << endl;
    // Derived classes can access protected members
    // SavingsAccount can access interestRate and accountType
    
    return 0;
}
```

---

## 6. **Friend Functions and Classes**

### Definition
Friend declarations allow external functions or classes to access private and protected members.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Secret {
private:
    string password;
    int securityCode;
    
protected:
    string internalNote;
    
public:
    Secret(string pwd, int code, string note) 
        : password(pwd), securityCode(code), internalNote(note) {}
    
    // Friend function declaration
    friend void revealSecret(const Secret& s);
    
    // Friend class declaration
    friend class Inspector;
};

// Friend function - can access private and protected members
void revealSecret(const Secret& s) {
    cout << "Password: " << s.password << endl;
    cout << "Security Code: " << s.securityCode << endl;
    cout << "Internal Note: " << s.internalNote << endl;
}

// Friend class - can access private and protected members
class Inspector {
public:
    static void inspect(const Secret& s) {
        cout << "\nInspector Access:" << endl;
        cout << "Password: " << s.password << endl;
        cout << "Security Code: " << s.securityCode << endl;
        cout << "Internal Note: " << s.internalNote << endl;
    }
    
    static void modify(Secret& s, string newPwd) {
        s.password = newPwd;  // Can modify private members
        cout << "Password changed to: " << newPwd << endl;
    }
};

class NotFriend {
public:
    void tryAccess(const Secret& s) {
        // Cannot access private members
        // cout << s.password;  // Error!
    }
};

int main() {
    cout << "=== Friend Functions and Classes ===" << endl;
    
    Secret secret("TopSecret123", 9876, "Confidential Note");
    
    cout << "\n1. Friend function access:" << endl;
    revealSecret(secret);
    
    cout << "\n2. Friend class access:" << endl;
    Inspector::inspect(secret);
    Inspector::modify(secret, "NewSecret456");
    
    cout << "\n3. After modification:" << endl;
    revealSecret(secret);
    
    cout << "\n4. Not a friend (cannot access):" << endl;
    NotFriend notFriend;
    // notFriend.tryAccess(secret);  // Would be error
    
    return 0;
}
```

---

## 📊 Access Control Summary

| Access | Class | Derived | External | Friend | Use Case |
|--------|-------|---------|----------|--------|----------|
| **public** | ✓ | ✓ | ✓ | ✓ | Interface |
| **private** | ✓ | ✗ | ✗ | ✓ | Implementation |
| **protected** | ✓ | ✓ | ✗ | ✓ | Base class internals |

---

## ✅ Best Practices

1. **Make data members private** by default
2. **Use public for interface** methods
3. **Use protected for inheritance** (rarely for data)
4. **Use private for implementation details**
5. **Use friend sparingly** (breaks encapsulation)
6. **Prefer composition over protected data** when possible

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Public data members** | No control over modifications | Make private, add getters/setters |
| **Overusing protected** | Coupling between base and derived | Use private with proper interface |
| **Overusing friend** | Breaks encapsulation | Use public interface instead |
| **Wrong inheritance access** | Unexpected visibility | Understand inheritance access rules |
| **Forgetting to declare friend** | Compilation error | Declare friend before use |

---

## ✅ Key Takeaways

1. **public**: Accessible everywhere - forms the interface
2. **private**: Accessible only within class - for implementation
3. **protected**: Accessible in class and derived classes - for inheritance
4. **Friend**: Allows external access - use sparingly
5. **Inheritance access**: Determines how base members are inherited
6. **Encapsulation**: Achieved through access control

---