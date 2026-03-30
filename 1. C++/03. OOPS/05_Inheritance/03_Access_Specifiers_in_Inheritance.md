# Access Specifiers in Inheritance - Complete Guide

## 📖 Overview

Access specifiers in inheritance determine how members of a base class are inherited by derived classes. The inheritance access specifier (public, protected, private) controls the visibility of base class members in the derived class and beyond. Understanding these rules is crucial for proper encapsulation and class design.

---

## 🎯 Key Concepts

| Specifier | Base Class Access | Derived Class Access | External Access |
|-----------|-------------------|---------------------|-----------------|
| **public inheritance** | public → public<br>protected → protected<br>private → inaccessible | public and protected remain as-is | public members accessible |
| **protected inheritance** | public → protected<br>protected → protected<br>private → inaccessible | all become protected | no members accessible |
| **private inheritance** | public → private<br>protected → private<br>private → inaccessible | all become private | no members accessible |

---

## 1. **Public Inheritance**

### Definition
Public inheritance is the most commonly used form. It models "is-a" relationships and preserves the access levels of base class members.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
private:
    int privateVar = 1;
    
protected:
    int protectedVar = 2;
    
public:
    int publicVar = 3;
    
    Base() {
        cout << "Base created" << endl;
    }
    
    void showBase() {
        cout << "Private: " << privateVar << endl;
        cout << "Protected: " << protectedVar << endl;
        cout << "Public: " << publicVar << endl;
    }
    
    int getPrivate() const { return privateVar; }
    void setPrivate(int val) { privateVar = val; }
};

// Public Inheritance
class PublicDerived : public Base {
public:
    void showDerived() {
        // cout << privateVar << endl;  // Error! Private not accessible
        cout << "Protected: " << protectedVar << endl;  // OK - becomes protected
        cout << "Public: " << publicVar << endl;        // OK - remains public
        cout << "Private via getter: " << getPrivate() << endl;
    }
    
    void modify() {
        protectedVar = 20;    // OK - can modify protected
        publicVar = 30;       // OK - can modify public
        setPrivate(10);       // OK - via public method
    }
};

int main() {
    cout << "=== Public Inheritance ===" << endl;
    
    PublicDerived derived;
    
    cout << "\n1. Derived class accessing base members:" << endl;
    derived.showDerived();
    
    cout << "\n2. External access:" << endl;
    derived.publicVar = 100;  // OK - public
    // derived.protectedVar = 200;  // Error! Protected
    // derived.privateVar = 300;    // Error! Private
    
    cout << "\n3. After modifications:" << endl;
    derived.showDerived();
    
    return 0;
}
```

**Output:**
```
=== Public Inheritance ===

1. Derived class accessing base members:
Protected: 2
Public: 3
Private via getter: 1

2. External access:

3. After modifications:
Protected: 20
Public: 30
Private via getter: 10
```

---

## 2. **Protected Inheritance**

### Definition
Protected inheritance makes all public and protected members of the base class protected in the derived class. This is used when you want to further restrict access in the inheritance chain.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
protected:
    int protectedVar = 2;
    
public:
    int publicVar = 3;
    
    void showBase() {
        cout << "Protected: " << protectedVar << endl;
        cout << "Public: " << publicVar << endl;
    }
};

// Protected Inheritance
class ProtectedDerived : protected Base {
public:
    void showDerived() {
        // Both become protected in derived
        cout << "Protected: " << protectedVar << endl;  // OK
        cout << "Public: " << publicVar << endl;        // OK - now protected
    }
    
    void modify() {
        protectedVar = 20;
        publicVar = 30;
    }
};

// Further inheritance
class FurtherDerived : public ProtectedDerived {
public:
    void showFurther() {
        // Can access because they are protected in ProtectedDerived
        cout << "Protected from Base: " << protectedVar << endl;  // OK
        cout << "Public from Base (now protected): " << publicVar << endl;  // OK
    }
};

int main() {
    cout << "=== Protected Inheritance ===" << endl;
    
    ProtectedDerived derived;
    
    cout << "\n1. Derived class access:" << endl;
    derived.showDerived();
    
    cout << "\n2. External access:" << endl;
    // derived.publicVar = 100;   // Error! Now protected
    // derived.protectedVar = 200; // Error! Protected
    
    cout << "\n3. Further derived class access:" << endl;
    FurtherDerived further;
    further.showFurther();
    
    return 0;
}
```

---

## 3. **Private Inheritance**

### Definition
Private inheritance makes all base class members private in the derived class. This is used to implement "has-a" relationships (implementation inheritance) rather than "is-a" relationships.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
protected:
    int protectedVar = 2;
    
public:
    int publicVar = 3;
    
    void showBase() {
        cout << "Protected: " << protectedVar << endl;
        cout << "Public: " << publicVar << endl;
    }
};

// Private Inheritance
class PrivateDerived : private Base {
public:
    void showDerived() {
        // Both become private in derived
        cout << "Protected: " << protectedVar << endl;  // OK
        cout << "Public: " << publicVar << endl;        // OK - now private
    }
    
    void modify() {
        protectedVar = 20;
        publicVar = 30;
    }
    
    // To expose base functionality selectively
    void showBasePublic() {
        showBase();  // Call base method (now private in derived)
    }
};

// Cannot access base members in further derived classes
class FurtherDerived : public PrivateDerived {
public:
    void showFurther() {
        // cout << protectedVar << endl;  // Error! Not accessible
        // cout << publicVar << endl;     // Error! Not accessible
        showBasePublic();  // OK - public method of PrivateDerived
    }
};

int main() {
    cout << "=== Private Inheritance ===" << endl;
    
    PrivateDerived derived;
    
    cout << "\n1. Derived class access:" << endl;
    derived.showDerived();
    
    cout << "\n2. External access:" << endl;
    // derived.publicVar = 100;    // Error! Now private
    // derived.protectedVar = 200;  // Error! Private
    
    cout << "\n3. Exposing base functionality:" << endl;
    derived.showBasePublic();
    
    cout << "\n4. Further derived class access:" << endl;
    FurtherDerived further;
    further.showFurther();
    
    return 0;
}
```

---

## 4. **Comparison Table**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
private:
    int privateVar = 1;
protected:
    int protectedVar = 2;
public:
    int publicVar = 3;
    
    void display() {
        cout << "Private: " << privateVar << endl;
        cout << "Protected: " << protectedVar << endl;
        cout << "Public: " << publicVar << endl;
    }
};

// Different inheritance types
class PublicDerived : public Base {
public:
    void show() {
        // cout << privateVar << endl;  // Not accessible
        cout << "PublicDerived - protectedVar: " << protectedVar << endl;
        cout << "PublicDerived - publicVar: " << publicVar << endl;
    }
};

class ProtectedDerived : protected Base {
public:
    void show() {
        cout << "ProtectedDerived - protectedVar: " << protectedVar << endl;
        cout << "ProtectedDerived - publicVar: " << publicVar << endl;
    }
};

class PrivateDerived : private Base {
public:
    void show() {
        cout << "PrivateDerived - protectedVar: " << protectedVar << endl;
        cout << "PrivateDerived - publicVar: " << publicVar << endl;
    }
};

int main() {
    cout << "=== Access Specifiers Comparison ===" << endl;
    
    cout << "\n1. Public Inheritance:" << endl;
    PublicDerived pub;
    pub.show();
    pub.publicVar = 100;  // OK - public
    // pub.protectedVar = 200;  // Error
    
    cout << "\n2. Protected Inheritance:" << endl;
    ProtectedDerived prot;
    prot.show();
    // prot.publicVar = 100;  // Error - now protected
    // prot.protectedVar = 200; // Error
    
    cout << "\n3. Private Inheritance:" << endl;
    PrivateDerived priv;
    priv.show();
    // priv.publicVar = 100;  // Error - now private
    // priv.protectedVar = 200; // Error
    
    cout << "\n4. Summary Table:" << endl;
    cout << "Inheritance Type | Base public | Base protected | Base private" << endl;
    cout << "Public           | public      | protected      | inaccessible" << endl;
    cout << "Protected        | protected   | protected      | inaccessible" << endl;
    cout << "Private          | private     | private        | inaccessible" << endl;
    
    return 0;
}
```

---

## 5. **Practical Example: Different Inheritance Levels**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Base class with various access levels
class DataStore {
private:
    string privateData = "Private Data";
    
protected:
    string protectedData = "Protected Data";
    
public:
    string publicData = "Public Data";
    
    virtual void display() {
        cout << "  Private: " << privateData << endl;
        cout << "  Protected: " << protectedData << endl;
        cout << "  Public: " << publicData << endl;
    }
    
    string getPrivate() const { return privateData; }
    void setPrivate(const string& val) { privateData = val; }
};

// Public inheritance - preserves access levels
class PublicStore : public DataStore {
public:
    void accessData() {
        // cout << privateData << endl;  // Error
        cout << "Protected: " << protectedData << endl;  // OK
        cout << "Public: " << publicData << endl;        // OK
        cout << "Private via getter: " << getPrivate() << endl;
    }
    
    void modifyData() {
        protectedData = "Modified Protected";
        publicData = "Modified Public";
        setPrivate("Modified Private");
    }
};

// Protected inheritance - everything becomes protected
class ProtectedStore : protected DataStore {
public:
    void accessData() {
        cout << "Protected: " << protectedData << endl;
        cout << "Public (now protected): " << publicData << endl;
        cout << "Private via getter: " << getPrivate() << endl;
    }
    
    void modifyData() {
        protectedData = "Modified Protected";
        publicData = "Modified Public";
        setPrivate("Modified Private");
    }
};

// Private inheritance - everything becomes private
class PrivateStore : private DataStore {
public:
    void accessData() {
        cout << "Protected (now private): " << protectedData << endl;
        cout << "Public (now private): " << publicData << endl;
        cout << "Private via getter: " << getPrivate() << endl;
    }
    
    void modifyData() {
        protectedData = "Modified Protected";
        publicData = "Modified Public";
        setPrivate("Modified Private");
    }
    
    // Expose selected functionality
    void showData() {
        display();  // Now private, but accessible here
    }
};

class ExtendedPublic : public PublicStore {
public:
    void extendedAccess() {
        // Can access protected and public from PublicStore
        cout << "Protected from PublicStore: " << protectedData << endl;
        cout << "Public from PublicStore: " << publicData << endl;
        // cout << privateData << endl;  // Still not accessible
    }
};

class ExtendedProtected : public ProtectedStore {
public:
    void extendedAccess() {
        // Can access protected members (now protected in ProtectedStore)
        cout << "Protected from ProtectedStore: " << protectedData << endl;
        // cout << publicData << endl;  // Error - now protected, but accessible? Actually protected
        // Actually protected members are accessible in derived classes
        // The publicData is now protected, so accessible
        cout << "Public (now protected): " << publicData << endl;
    }
};

class ExtendedPrivate : public PrivateStore {
public:
    void extendedAccess() {
        // Cannot access any base members - they are all private
        // cout << protectedData << endl;  // Error
        // cout << publicData << endl;     // Error
        // Must use public interface of PrivateStore
        showData();  // OK - public method
    }
};

int main() {
    cout << "=== Different Inheritance Levels - Practical Example ===" << endl;
    
    cout << "\n1. Public Inheritance:" << endl;
    PublicStore pub;
    pub.accessData();
    pub.modifyData();
    cout << "\nAfter modification:" << endl;
    pub.accessData();
    pub.publicData = "Direct Modification";  // OK - public
    // pub.protectedData = "Direct";  // Error - protected
    
    cout << "\n2. Protected Inheritance:" << endl;
    ProtectedStore prot;
    prot.accessData();
    // prot.publicData = "Direct";  // Error - now protected
    
    cout << "\n3. Private Inheritance:" << endl;
    PrivateStore priv;
    priv.accessData();
    priv.showData();  // Exposed functionality
    // priv.publicData = "Direct";  // Error - now private
    
    cout << "\n4. Extended Inheritance Chains:" << endl;
    ExtendedPublic extPub;
    extPub.extendedAccess();
    
    ExtendedProtected extProt;
    extProt.extendedAccess();
    
    ExtendedPrivate extPriv;
    extPriv.extendedAccess();
    
    return 0;
}
```

---

## 6. **Choosing the Right Inheritance Type**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// Example 1: Public Inheritance - IS-A relationship
class Animal {
public:
    virtual void speak() = 0;
    virtual ~Animal() {}
};

class Dog : public Animal {  // Dog IS-A Animal
public:
    void speak() override {
        cout << "Woof!" << endl;
    }
};

// Example 2: Private Inheritance - HAS-A / Implemented-in-terms-of
class Timer {
public:
    void start() { cout << "Timer started" << endl; }
    void stop() { cout << "Timer stopped" << endl; }
    double elapsed() { return 0.0; }
};

class StopWatch : private Timer {  // StopWatch implemented using Timer
public:
    void begin() { start(); }
    void end() { stop(); }
    double duration() { return elapsed(); }
};

// Example 3: Protected Inheritance - Limited extension
class BaseAlgorithm {
protected:
    void step1() { cout << "Step 1" << endl; }
    void step2() { cout << "Step 2" << endl; }
    void step3() { cout << "Step 3" << endl; }
};

class CustomAlgorithm : protected BaseAlgorithm {
public:
    void run() {
        step1();
        step2();
        step3();
    }
};

// Example 4: Using composition vs private inheritance
class Logger {
public:
    void log(const string& msg) {
        cout << "[LOG] " << msg << endl;
    }
};

// Option 1: Private inheritance
class ServiceA : private Logger {
public:
    void process() {
        log("Processing in ServiceA");
    }
};

// Option 2: Composition (often preferred)
class ServiceB {
private:
    Logger logger;  // Composition
public:
    void process() {
        logger.log("Processing in ServiceB");
    }
};

int main() {
    cout << "=== Choosing the Right Inheritance Type ===" << endl;
    
    cout << "\n1. Public Inheritance (IS-A):" << endl;
    Dog dog;
    dog.speak();
    
    cout << "\n2. Private Inheritance (Implemented-in-terms-of):" << endl;
    StopWatch watch;
    watch.begin();
    watch.end();
    cout << "Duration: " << watch.duration() << endl;
    
    cout << "\n3. Protected Inheritance (Limited extension):" << endl;
    CustomAlgorithm algo;
    algo.run();
    
    cout << "\n4. Composition vs Private Inheritance:" << endl;
    ServiceA svcA;
    svcA.process();
    
    ServiceB svcB;
    svcB.process();
    
    cout << "\nGuidelines:" << endl;
    cout << "✓ Public: Use for IS-A relationships" << endl;
    cout << "✓ Protected: Use when base should only be extended, not used" << endl;
    cout << "✓ Private: Use for implementation details (prefer composition)" << endl;
    
    return 0;
}
```

---

## 📊 Access Specifiers Summary Table

| Base Member Access | Public Inheritance | Protected Inheritance | Private Inheritance |
|-------------------|-------------------|----------------------|--------------------|
| **public** | public | protected | private |
| **protected** | protected | protected | private |
| **private** | inaccessible | inaccessible | inaccessible |

---

## ✅ Best Practices

1. **Use public inheritance** for "is-a" relationships
2. **Use private inheritance** for "implemented-in-terms-of" (prefer composition)
3. **Use protected inheritance** rarely (mostly for framework design)
4. **Keep base class interface clean** - what should be inherited vs hidden
5. **Document inheritance type** in class comments
6. **Consider composition** over private/protected inheritance

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Using private inheritance unnecessarily** | Harder to maintain | Use composition instead |
| **Wrong inheritance type** | Exposing too much or too little | Choose based on relationship |
| **Forgetting access rules** | Compilation errors | Understand inheritance access |
| **Protected data members** | Tight coupling | Keep data private, provide protected methods |

---

## ✅ Key Takeaways

1. **Public inheritance**: Preserves access levels (most common)
2. **Protected inheritance**: Makes everything protected
3. **Private inheritance**: Makes everything private
4. **IS-A relationship**: Use public inheritance
5. **HAS-A/Implemented-in-terms-of**: Prefer composition over private inheritance
6. **Access levels**: public > protected > private in terms of visibility

---