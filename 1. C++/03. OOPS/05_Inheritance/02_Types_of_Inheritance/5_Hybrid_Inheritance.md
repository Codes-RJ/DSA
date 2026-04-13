# Hybrid Inheritance in C++ - Complete Guide

## 📖 Overview

Hybrid inheritance is a combination of two or more types of inheritance (single, multiple, multilevel, hierarchical). It creates complex class hierarchies where a class may inherit from multiple base classes, and those base classes may themselves have their own inheritance chains. Hybrid inheritance often leads to the **diamond problem**, which requires virtual inheritance to resolve.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Hybrid Inheritance** | Combination of multiple inheritance types |
| **Diamond Problem** | Ambiguity when a class inherits from two classes that share a common base |
| **Virtual Inheritance** | Solution to the diamond problem |
| **Complex Hierarchy** | Can create intricate relationships |

---

## 1. **Basic Hybrid Inheritance (Without Virtual)**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Level 1 - Grandparent
class Person {
protected:
    string name;
    int age;
    
public:
    Person(string n, int a) : name(n), age(a) {
        cout << "Person constructor: " << name << endl;
    }
    
    void display() {
        cout << "Name: " << name << ", Age: " << age << endl;
    }
    
    virtual ~Person() {
        cout << "Person destructor: " << name << endl;
    }
};

// Level 2 - Employee (Single Inheritance)
class Employee : public Person {
protected:
    int employeeId;
    double salary;
    
public:
    Employee(string n, int a, int id, double sal) 
        : Person(n, a), employeeId(id), salary(sal) {
        cout << "  Employee constructor: ID=" << employeeId << endl;
    }
    
    void work() {
        cout << name << " is working" << endl;
    }
    
    void display() {
        Person::display();
        cout << "  ID: " << employeeId << ", Salary: $" << salary << endl;
    }
};

// Level 2 - Student (Single Inheritance)
class Student : public Person {
protected:
    int studentId;
    string major;
    
public:
    Student(string n, int a, int id, string m) 
        : Person(n, a), studentId(id), major(m) {
        cout << "  Student constructor: ID=" << studentId << endl;
    }
    
    void study() {
        cout << name << " is studying " << major << endl;
    }
    
    void display() {
        Person::display();
        cout << "  ID: " << studentId << ", Major: " << major << endl;
    }
};

// Level 3 - WorkingStudent (Multiple Inheritance from Employee and Student)
class WorkingStudent : public Employee, public Student {
private:
    int hoursPerWeek;
    
public:
    WorkingStudent(string n, int a, int empId, double sal, int stuId, string m, int hours)
        : Employee(n, a, empId, sal), Student(n, a, stuId, m), hoursPerWeek(hours) {
        cout << "    WorkingStudent constructor: " << hours << " hours/week" << endl;
    }
    
    void display() {
        // Ambiguity: which display() to call? Employee::display() or Student::display()?
        Employee::display();  // Need to specify which base class
        Student::display();
        cout << "  Hours: " << hoursPerWeek << " hours/week" << endl;
    }
    
    void workAndStudy() {
        work();   // From Employee
        study();  // From Student
        cout << name << " is working and studying" << endl;
    }
};

int main() {
    cout << "=== Hybrid Inheritance (Without Virtual) ===" << endl;
    
    cout << "\nCreating WorkingStudent:" << endl;
    WorkingStudent ws("Alice", 22, 1001, 50000, 2001, "Computer Science", 20);
    
    cout << "\n=== Displaying ===" << endl;
    ws.display();
    
    cout << "\n=== Actions ===" << endl;
    ws.workAndStudy();
    
    cout << "\nNote: Person class appears twice! (Diamond problem)" << endl;
    
    return 0;
}
```

**Output:**
```
=== Hybrid Inheritance (Without Virtual) ===

Creating WorkingStudent:
Person constructor: Alice
  Employee constructor: ID=1001
Person constructor: Alice
  Student constructor: ID=2001
    WorkingStudent constructor: 20 hours/week

=== Displaying ===
Name: Alice, Age: 22
  ID: 1001, Salary: $50000.00
Name: Alice, Age: 22
  ID: 2001, Major: Computer Science
  Hours: 20 hours/week

=== Actions ===
Alice is working
Alice is studying Computer Science
Alice is working and studying

Note: Person class appears twice! (Diamond problem)
```

---

## 2. **The Diamond Problem**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
protected:
    int value;
    
public:
    Base() : value(0) {
        cout << "Base constructor" << endl;
    }
    
    Base(int v) : value(v) {
        cout << "Base parameterized constructor: " << value << endl;
    }
    
    void show() {
        cout << "Base value: " << value << endl;
    }
    
    virtual ~Base() {
        cout << "Base destructor" << endl;
    }
};

class Derived1 : public Base {
public:
    Derived1() : Base() {
        cout << "Derived1 constructor" << endl;
    }
    
    Derived1(int v) : Base(v) {
        cout << "Derived1 parameterized: " << v << endl;
    }
    
    void feature1() {
        cout << "Derived1 feature" << endl;
    }
};

class Derived2 : public Base {
public:
    Derived2() : Base() {
        cout << "Derived2 constructor" << endl;
    }
    
    Derived2(int v) : Base(v) {
        cout << "Derived2 parameterized: " << v << endl;
    }
    
    void feature2() {
        cout << "Derived2 feature" << endl;
    }
};

// Multiple inheritance - Diamond problem!
class Diamond : public Derived1, public Derived2 {
public:
    Diamond() : Derived1(), Derived2() {
        cout << "Diamond constructor" << endl;
    }
    
    Diamond(int v1, int v2) : Derived1(v1), Derived2(v2) {
        cout << "Diamond parameterized constructor" << endl;
    }
    
    void showAll() {
        // Ambiguity: which value? Derived1::value or Derived2::value?
        cout << "Derived1 value: " << Derived1::value << endl;
        cout << "Derived2 value: " << Derived2::value << endl;
        // cout << "Base value: " << value;  // Error! Ambiguous
    }
};

int main() {
    cout << "=== Diamond Problem Demonstration ===" << endl;
    
    cout << "\n1. Creating Diamond object with default values:" << endl;
    Diamond d1;
    d1.showAll();
    
    cout << "\n2. Creating Diamond object with custom values:" << endl;
    Diamond d2(100, 200);
    d2.showAll();
    
    cout << "\n3. Memory layout issue:" << endl;
    cout << "Size of Base: " << sizeof(Base) << " bytes" << endl;
    cout << "Size of Derived1: " << sizeof(Derived1) << " bytes" << endl;
    cout << "Size of Derived2: " << sizeof(Derived2) << " bytes" << endl;
    cout << "Size of Diamond: " << sizeof(Diamond) << " bytes" << endl;
    cout << "Note: Diamond contains two copies of Base!" << endl;
    
    return 0;
}
```

**Output:**
```
=== Diamond Problem Demonstration ===

1. Creating Diamond object with default values:
Base constructor
Derived1 constructor
Base constructor
Derived2 constructor
Diamond constructor
Derived1 value: 0
Derived2 value: 0

2. Creating Diamond object with custom values:
Base parameterized constructor: 100
Derived1 parameterized: 100
Base parameterized constructor: 200
Derived2 parameterized: 200
Diamond parameterized constructor
Derived1 value: 100
Derived2 value: 200

3. Memory layout issue:
Size of Base: 4 bytes
Size of Derived1: 4 bytes
Size of Derived2: 4 bytes
Size of Diamond: 8 bytes
Note: Diamond contains two copies of Base!
```

---

## 3. **Solution: Virtual Inheritance**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Virtual base class to solve diamond problem
class VirtualBase {
protected:
    int value;
    
public:
    VirtualBase() : value(0) {
        cout << "VirtualBase constructor" << endl;
    }
    
    VirtualBase(int v) : value(v) {
        cout << "VirtualBase parameterized: " << value << endl;
    }
    
    void show() {
        cout << "VirtualBase value: " << value << endl;
    }
    
    virtual ~VirtualBase() {
        cout << "VirtualBase destructor" << endl;
    }
};

// Virtual inheritance
class VirtualDerived1 : virtual public VirtualBase {
public:
    VirtualDerived1() : VirtualBase() {
        cout << "VirtualDerived1 constructor" << endl;
    }
    
    VirtualDerived1(int v) : VirtualBase(v) {
        cout << "VirtualDerived1 parameterized: " << v << endl;
    }
    
    void feature1() {
        cout << "VirtualDerived1 feature" << endl;
    }
};

// Virtual inheritance
class VirtualDerived2 : virtual public VirtualBase {
public:
    VirtualDerived2() : VirtualBase() {
        cout << "VirtualDerived2 constructor" << endl;
    }
    
    VirtualDerived2(int v) : VirtualBase(v) {
        cout << "VirtualDerived2 parameterized: " << v << endl;
    }
    
    void feature2() {
        cout << "VirtualDerived2 feature" << endl;
    }
};

// Virtual Diamond - solves the problem
class VirtualDiamond : public VirtualDerived1, public VirtualDerived2 {
public:
    VirtualDiamond() : VirtualBase(), VirtualDerived1(), VirtualDerived2() {
        cout << "VirtualDiamond constructor" << endl;
    }
    
    VirtualDiamond(int v) : VirtualBase(v), VirtualDerived1(), VirtualDerived2() {
        cout << "VirtualDiamond parameterized: " << v << endl;
    }
    
    void showAll() {
        // No ambiguity now - only one copy of VirtualBase
        cout << "VirtualBase value: " << value << endl;
        show();  // Works fine
    }
};

int main() {
    cout << "=== Virtual Inheritance Solution ===" << endl;
    
    cout << "\n1. Creating VirtualDiamond with default:" << endl;
    VirtualDiamond vd1;
    vd1.showAll();
    vd1.feature1();
    vd1.feature2();
    
    cout << "\n2. Creating VirtualDiamond with custom value:" << endl;
    VirtualDiamond vd2(999);
    vd2.showAll();
    
    cout << "\n3. Memory layout improvement:" << endl;
    cout << "Size of VirtualBase: " << sizeof(VirtualBase) << " bytes" << endl;
    cout << "Size of VirtualDerived1: " << sizeof(VirtualDerived1) << " bytes" << endl;
    cout << "Size of VirtualDerived2: " << sizeof(VirtualDerived2) << " bytes" << endl;
    cout << "Size of VirtualDiamond: " << sizeof(VirtualDiamond) << " bytes" << endl;
    cout << "Note: Only one copy of VirtualBase now!" << endl;
    
    return 0;
}
```

---

## 4. **Practical Example: University Management System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

// Virtual Base Class
class Person {
protected:
    string name;
    int age;
    string email;
    
public:
    Person(string n, int a, string e) : name(n), age(a), email(e) {
        cout << "Person created: " << name << endl;
    }
    
    virtual void display() const {
        cout << "Name: " << name << ", Age: " << age << ", Email: " << email << endl;
    }
    
    virtual ~Person() {
        cout << "Person destroyed: " << name << endl;
    }
};

// Employee - inherits virtually from Person
class Employee : virtual public Person {
protected:
    int employeeId;
    double salary;
    static int nextEmpId;
    
public:
    Employee(string n, int a, string e, double sal) 
        : Person(n, a, e), employeeId(nextEmpId++), salary(sal) {
        cout << "  Employee: ID=" << employeeId << endl;
    }
    
    void work() const {
        cout << name << " is working" << endl;
    }
    
    void display() const override {
        Person::display();
        cout << "  Employee ID: " << employeeId << ", Salary: $" << salary << endl;
    }
};

int Employee::nextEmpId = 1000;

// Student - inherits virtually from Person
class Student : virtual public Person {
protected:
    int studentId;
    string major;
    double gpa;
    static int nextStuId;
    
public:
    Student(string n, int a, string e, string m, double g) 
        : Person(n, a, e), studentId(nextStuId++), major(m), gpa(g) {
        cout << "  Student: ID=" << studentId << ", Major=" << major << endl;
    }
    
    void study() const {
        cout << name << " is studying " << major << endl;
    }
    
    void display() const override {
        Person::display();
        cout << "  Student ID: " << studentId << ", Major: " << major 
             << ", GPA: " << fixed << setprecision(2) << gpa << endl;
    }
};

int Student::nextStuId = 2000;

// ResearchAssistant - Hybrid inheritance (Employee + Student)
class ResearchAssistant : public Employee, public Student {
private:
    string researchArea;
    int publications;
    double stipend;
    
public:
    ResearchAssistant(string n, int a, string e, double sal, string m, double g, 
                      string research, int pubs, double stip)
        : Person(n, a, e), 
          Employee(n, a, e, sal), 
          Student(n, a, e, m, g),
          researchArea(research), publications(pubs), stipend(stip) {
        cout << "    Research Assistant: " << researchArea << endl;
    }
    
    void doResearch() const {
        cout << name << " is researching " << researchArea << endl;
    }
    
    void publish() {
        publications++;
        cout << name << " published a paper! Total: " << publications << endl;
    }
    
    double getTotalCompensation() const {
        return salary + stipend;
    }
    
    void display() const override {
        Person::display();
        cout << "  Employee ID: " << employeeId << ", Salary: $" << salary << endl;
        cout << "  Student ID: " << studentId << ", Major: " << major 
             << ", GPA: " << gpa << endl;
        cout << "  Research: " << researchArea << ", Publications: " << publications
             << ", Stipend: $" << stipend << endl;
        cout << "  Total Compensation: $" << getTotalCompensation() << endl;
    }
};

// TeachingAssistant - Another hybrid
class TeachingAssistant : public Employee, public Student {
private:
    string course;
    int hoursPerWeek;
    double teachingStipend;
    
public:
    TeachingAssistant(string n, int a, string e, double sal, string m, double g,
                      string course, int hours, double stip)
        : Person(n, a, e),
          Employee(n, a, e, sal),
          Student(n, a, e, m, g),
          course(course), hoursPerWeek(hours), teachingStipend(stip) {
        cout << "    Teaching Assistant: " << course << endl;
    }
    
    void teach() const {
        cout << name << " is teaching " << course << endl;
    }
    
    void gradePapers() const {
        cout << name << " is grading papers for " << course << endl;
    }
    
    double getTotalCompensation() const {
        return salary + teachingStipend;
    }
    
    void display() const override {
        Person::display();
        cout << "  Employee ID: " << employeeId << ", Salary: $" << salary << endl;
        cout << "  Student ID: " << studentId << ", Major: " << major 
             << ", GPA: " << gpa << endl;
        cout << "  Teaching: " << course << ", Hours: " << hoursPerWeek
             << ", Stipend: $" << teachingStipend << endl;
        cout << "  Total Compensation: $" << getTotalCompensation() << endl;
    }
};

int main() {
    cout << "=== University Management System - Hybrid Inheritance ===" << endl;
    
    cout << "\n1. Creating Research Assistant:" << endl;
    ResearchAssistant ra("Alice Johnson", 28, "alice@univ.edu", 60000, 
                         "Computer Science", 3.8, "Machine Learning", 5, 15000);
    
    cout << "\n2. Creating Teaching Assistant:" << endl;
    TeachingAssistant ta("Bob Smith", 26, "bob@univ.edu", 55000,
                         "Mathematics", 3.9, "Calculus I", 10, 12000);
    
    cout << "\n3. Displaying Research Assistant:" << endl;
    ra.display();
    
    cout << "\n4. Displaying Teaching Assistant:" << endl;
    ta.display();
    
    cout << "\n5. Actions:" << endl;
    ra.work();
    ra.study();
    ra.doResearch();
    ra.publish();
    
    cout << endl;
    ta.work();
    ta.study();
    ta.teach();
    ta.gradePapers();
    
    cout << "\n6. Polymorphic container:" << endl;
    vector<Person*> people = {&ra, &ta};
    for (auto p : people) {
        p->display();
        cout << endl;
    }
    
    return 0;
}
```

---

## 5. **Constructor Order in Virtual Inheritance**

```cpp
#include <iostream>
#include <string>
using namespace std;

class VirtualBase {
public:
    VirtualBase() {
        cout << "VirtualBase constructor" << endl;
    }
    
    VirtualBase(int x) {
        cout << "VirtualBase parameterized: " << x << endl;
    }
    
    ~VirtualBase() {
        cout << "VirtualBase destructor" << endl;
    }
};

class Base1 : virtual public VirtualBase {
public:
    Base1() : VirtualBase() {
        cout << "  Base1 constructor" << endl;
    }
    
    Base1(int x) : VirtualBase(x) {
        cout << "  Base1 parameterized: " << x << endl;
    }
};

class Base2 : virtual public VirtualBase {
public:
    Base2() : VirtualBase() {
        cout << "  Base2 constructor" << endl;
    }
    
    Base2(int x) : VirtualBase(x) {
        cout << "  Base2 parameterized: " << x << endl;
    }
};

class Derived : public Base1, public Base2 {
public:
    Derived() : VirtualBase(), Base1(), Base2() {
        cout << "    Derived constructor" << endl;
    }
    
    Derived(int x) : VirtualBase(x), Base1(x), Base2(x) {
        cout << "    Derived parameterized: " << x << endl;
    }
};

int main() {
    cout << "=== Constructor Order in Virtual Inheritance ===" << endl;
    
    cout << "\n1. Default construction:" << endl;
    Derived d1;
    
    cout << "\n2. Parameterized construction:" << endl;
    Derived d2(42);
    
    cout << "\nConstructor order with virtual inheritance:" << endl;
    cout << "1. Virtual base class (only once!)" << endl;
    cout << "2. Non-virtual base classes (in order)" << endl;
    cout << "3. Derived class" << endl;
    
    return 0;
}
```

---

## 📊 Hybrid Inheritance Summary

| Aspect | Description |
|--------|-------------|
| **Definition** | Combination of multiple inheritance types |
| **Diamond Problem** | Ambiguity when two paths share a common base |
| **Virtual Inheritance** | Solution using `virtual` keyword |
| **Constructor Order** | Virtual base → Non-virtual bases → Derived |
| **Memory** | Virtual inheritance adds pointer overhead |

---

## ✅ Best Practices

1. **Use virtual inheritance** to solve diamond problem
2. **Minimize hybrid inheritance** complexity
3. **Prefer composition** over complex inheritance hierarchies
4. **Keep hierarchy shallow** when possible
5. **Document inheritance relationships** clearly
6. **Use pure virtual interfaces** for multiple inheritance

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Diamond problem** | Ambiguity, multiple base copies | Use virtual inheritance |
| **Constructor confusion** | Wrong initialization order | Explicitly call virtual base constructor |
| **Casting issues** | Difficulty casting | Use dynamic_cast |
| **Memory overhead** | Larger object size | Acceptable trade-off for correctness |
| **Complex debugging** | Hard to trace | Keep hierarchies simple |

---

## ✅ Key Takeaways

1. **Hybrid inheritance** combines multiple inheritance types
2. **Diamond problem** occurs with common ancestor
3. **Virtual inheritance** solves diamond problem
4. **Constructor order**: Virtual base → Non-virtual bases → Derived
5. **Use with caution** - can create complex hierarchies
6. **Composition** is often a better alternative

---

## Next Step

- Go to [Access Specifier in Inheritance](../03_Access_Specifiers_in_Inheritance.md) to understand the starting of Security in OOPS.
