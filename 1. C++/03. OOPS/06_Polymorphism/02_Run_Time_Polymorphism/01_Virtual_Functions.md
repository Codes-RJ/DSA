# Virtual Functions in C++ - Complete Guide

## 📖 Overview

Virtual functions are the foundation of run-time polymorphism in C++. They allow derived classes to override base class functions, enabling dynamic dispatch where the appropriate function is called based on the actual object type at run time. This is essential for implementing polymorphic behavior and designing extensible systems.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Virtual Function** | Function that can be overridden in derived classes |
| **Dynamic Dispatch** | Function call resolved at run time based on object type |
| **vtable** | Virtual table containing function pointers |
| **vptr** | Virtual pointer pointing to vtable |
| **Override** | Derived class provides its own implementation |

---

## 1. **Basic Virtual Functions**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

class Animal {
protected:
    string name;
    
public:
    Animal(string n) : name(n) {}
    
    // Virtual function - can be overridden
    virtual void speak() const {
        cout << name << " makes a sound" << endl;
    }
    
    // Virtual function with default implementation
    virtual void move() const {
        cout << name << " moves" << endl;
    }
    
    // Non-virtual function - cannot be overridden effectively
    void eat() const {
        cout << name << " eats" << endl;
    }
    
    virtual ~Animal() {
        cout << "Animal destructor: " << name << endl;
    }
};

class Dog : public Animal {
public:
    Dog(string n) : Animal(n) {}
    
    // Override virtual function
    void speak() const override {
        cout << name << " barks: Woof! Woof!" << endl;
    }
    
    void move() const override {
        cout << name << " runs on four legs" << endl;
    }
    
    // Dog-specific method
    void wagTail() const {
        cout << name << " wags tail" << endl;
    }
    
    ~Dog() override {
        cout << "Dog destructor: " << name << endl;
    }
};

class Bird : public Animal {
public:
    Bird(string n) : Animal(n) {}
    
    void speak() const override {
        cout << name << " chirps: Tweet! Tweet!" << endl;
    }
    
    void move() const override {
        cout << name << " flies in the sky" << endl;
    }
    
    ~Bird() override {
        cout << "Bird destructor: " << name << endl;
    }
};

class Fish : public Animal {
public:
    Fish(string n) : Animal(n) {}
    
    void speak() const override {
        cout << name << " says: ... (silence)" << endl;
    }
    
    void move() const override {
        cout << name << " swims in water" << endl;
    }
    
    ~Fish() override {
        cout << "Fish destructor: " << name << endl;
    }
};

int main() {
    cout << "=== Basic Virtual Functions ===" << endl;
    
    // Polymorphic behavior
    vector<unique_ptr<Animal>> animals;
    animals.push_back(make_unique<Dog>("Buddy"));
    animals.push_back(make_unique<Bird>("Tweety"));
    animals.push_back(make_unique<Fish>("Nemo"));
    
    cout << "\nPolymorphic behavior:" << endl;
    for (const auto& animal : animals) {
        animal->speak();   // Virtual - calls derived version
        animal->move();    // Virtual - calls derived version
        animal->eat();     // Non-virtual - calls base version
        cout << endl;
    }
    
    // Demonstrating virtual destructor
    cout << "\nDestructors (virtual):" << endl;
    // Destructors called automatically when unique_ptr goes out of scope
    
    return 0;
}
```

**Output:**
```
=== Basic Virtual Functions ===

Polymorphic behavior:
Buddy barks: Woof! Woof!
Buddy runs on four legs
Buddy eats

Tweety chirps: Tweet! Tweet!
Tweety flies in the sky
Tweety eats

Nemo says: ... (silence)
Nemo swims in water
Nemo eats

Destructors (virtual):
Fish destructor: Nemo
Animal destructor: Nemo
Bird destructor: Tweety
Animal destructor: Tweety
Dog destructor: Buddy
Animal destructor: Buddy
```

---

## 2. **How Virtual Functions Work (vtable)**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
public:
    virtual void func1() {
        cout << "Base::func1()" << endl;
    }
    
    virtual void func2() {
        cout << "Base::func2()" << endl;
    }
    
    void func3() {
        cout << "Base::func3() (non-virtual)" << endl;
    }
    
    virtual ~Base() {}
};

class Derived : public Base {
public:
    void func1() override {
        cout << "Derived::func1()" << endl;
    }
    
    virtual void func4() {
        cout << "Derived::func4()" << endl;
    }
};

int main() {
    cout << "=== How Virtual Functions Work (vtable) ===" << endl;
    
    Base b;
    Derived d;
    Base* ptr = &d;
    
    cout << "\n1. Object sizes:" << endl;
    cout << "Size of Base: " << sizeof(Base) << " bytes" << endl;
    cout << "Size of Derived: " << sizeof(Derived) << " bytes" << endl;
    cout << "Note: vptr (virtual pointer) adds 8 bytes on 64-bit system" << endl;
    
    cout << "\n2. Virtual function calls (dynamic dispatch):" << endl;
    ptr->func1();   // Calls Derived::func1() via vtable
    ptr->func2();   // Calls Base::func2() via vtable
    ptr->func3();   // Calls Base::func3() (non-virtual, static binding)
    
    cout << "\n3. Direct calls (static binding):" << endl;
    d.func1();      // Calls Derived::func1()
    d.func2();      // Calls Base::func2()
    d.func4();      // Calls Derived::func4()
    
    cout << "\n4. vtable layout:" << endl;
    cout << "   Each object contains a vptr pointing to vtable" << endl;
    cout << "   vtable contains pointers to virtual functions" << endl;
    cout << "   Virtual calls: obj->vptr[index]()" << endl;
    
    return 0;
}
```

---

## 3. **Virtual Functions in Inheritance Chains**

```cpp
#include <iostream>
#include <string>
using namespace std;

class GrandParent {
public:
    virtual void show() {
        cout << "GrandParent::show()" << endl;
    }
    
    virtual void display() {
        cout << "GrandParent::display()" << endl;
    }
    
    virtual ~GrandParent() {}
};

class Parent : public GrandParent {
public:
    void show() override {
        cout << "Parent::show()" << endl;
    }
    
    // display() not overridden - uses GrandParent version
    
    virtual void specific() {
        cout << "Parent::specific()" << endl;
    }
};

class Child : public Parent {
public:
    void show() override {
        cout << "Child::show()" << endl;
    }
    
    void display() override {
        cout << "Child::display()" << endl;
    }
    
    void specific() override {
        cout << "Child::specific()" << endl;
    }
};

int main() {
    cout << "=== Virtual Functions in Inheritance Chains ===" << endl;
    
    GrandParent* gp = new GrandParent();
    GrandParent* p = new Parent();
    GrandParent* c = new Child();
    
    cout << "\n1. Calls through GrandParent pointers:" << endl;
    gp->show();     // GrandParent::show()
    gp->display();  // GrandParent::display()
    
    cout << "\n2. Calls through Parent pointer (as GrandParent):" << endl;
    p->show();      // Parent::show()
    p->display();   // GrandParent::display()
    
    cout << "\n3. Calls through Child pointer (as GrandParent):" << endl;
    c->show();      // Child::show()
    c->display();   // Child::display()
    
    cout << "\n4. Virtual function table chain:" << endl;
    cout << "   GrandParent vtable: show() → GrandParent::show, display() → GrandParent::display" << endl;
    cout << "   Parent vtable: show() → Parent::show, display() → GrandParent::display, specific() → Parent::specific" << endl;
    cout << "   Child vtable: show() → Child::show, display() → Child::display, specific() → Child::specific" << endl;
    
    delete gp;
    delete p;
    delete c;
    
    return 0;
}
```

---

## 4. **Virtual Functions in Constructors and Destructors**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
public:
    Base() {
        cout << "Base constructor" << endl;
        callVirtual();  // Warning: virtual call in constructor!
    }
    
    virtual void callVirtual() {
        cout << "Base::callVirtual()" << endl;
    }
    
    virtual ~Base() {
        cout << "Base destructor" << endl;
        callVirtual();  // Warning: virtual call in destructor!
    }
};

class Derived : public Base {
public:
    Derived() {
        cout << "Derived constructor" << endl;
    }
    
    void callVirtual() override {
        cout << "Derived::callVirtual()" << endl;
    }
    
    ~Derived() override {
        cout << "Derived destructor" << endl;
    }
};

int main() {
    cout << "=== Virtual Functions in Constructors and Destructors ===" << endl;
    
    cout << "\n1. Creating Derived object:" << endl;
    Derived d;
    
    cout << "\n2. Note: Virtual calls in constructor/destructor don't work as expected!" << endl;
    cout << "   During Base construction, Derived part doesn't exist yet." << endl;
    cout << "   So Base::callVirtual() is called, not Derived::callVirtual()." << endl;
    cout << "   Same applies during destruction (Derived part destroyed first)." << endl;
    
    cout << "\n3. Rule: Never call virtual functions in constructor or destructor!" << endl;
    
    return 0;
}
```

---

## 5. **Pure Virtual Functions and Abstract Classes**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// Abstract base class (interface)
class Shape {
public:
    // Pure virtual functions - must be overridden
    virtual double area() const = 0;
    virtual double perimeter() const = 0;
    virtual void draw() const = 0;
    
    // Virtual destructor with default implementation
    virtual ~Shape() = default;
};

class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(double r) : radius(r) {}
    
    double area() const override {
        return M_PI * radius * radius;
    }
    
    double perimeter() const override {
        return 2 * M_PI * radius;
    }
    
    void draw() const override {
        cout << "Drawing circle with radius " << radius << endl;
    }
};

class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    
    double area() const override {
        return width * height;
    }
    
    double perimeter() const override {
        return 2 * (width + height);
    }
    
    void draw() const override {
        cout << "Drawing rectangle " << width << "x" << height << endl;
    }
};

class Triangle : public Shape {
private:
    double a, b, c;
    
public:
    Triangle(double s1, double s2, double s3) : a(s1), b(s2), c(s3) {}
    
    double area() const override {
        double s = (a + b + c) / 2;
        return sqrt(s * (s - a) * (s - b) * (s - c));
    }
    
    double perimeter() const override {
        return a + b + c;
    }
    
    void draw() const override {
        cout << "Drawing triangle with sides " << a << ", " << b << ", " << c << endl;
    }
};

int main() {
    cout << "=== Pure Virtual Functions and Abstract Classes ===" << endl;
    
    // Shape s;  // Error! Cannot instantiate abstract class
    
    Shape* shapes[] = {
        new Circle(5),
        new Rectangle(4, 6),
        new Triangle(3, 4, 5)
    };
    
    cout << "\nPolymorphic behavior with abstract base class:" << endl;
    for (auto shape : shapes) {
        shape->draw();
        cout << "Area: " << shape->area() << endl;
        cout << "Perimeter: " << shape->perimeter() << endl;
        cout << endl;
    }
    
    // Cleanup
    for (auto shape : shapes) {
        delete shape;
    }
    
    return 0;
}
```

---

## 6. **Practical Example: Game Character System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <cmath>
using namespace std;

// Abstract base class
class Character {
protected:
    string name;
    int health;
    int mana;
    int level;
    
public:
    Character(string n, int h, int m, int l) 
        : name(n), health(h), mana(m), level(l) {}
    
    // Pure virtual functions
    virtual void attack() const = 0;
    virtual void defend() const = 0;
    virtual void specialAbility() const = 0;
    virtual void displayStats() const = 0;
    
    // Virtual function with default implementation
    virtual void takeDamage(int damage) {
        health -= damage;
        cout << name << " takes " << damage << " damage! Health: " << health << endl;
        if (health <= 0) {
            cout << name << " has been defeated!" << endl;
        }
    }
    
    virtual void heal(int amount) {
        health += amount;
        cout << name << " heals for " << amount << "! Health: " << health << endl;
    }
    
    virtual ~Character() = default;
    
    string getName() const { return name; }
    bool isAlive() const { return health > 0; }
};

class Warrior : public Character {
private:
    int strength;
    
public:
    Warrior(string n, int h, int m, int l, int s) 
        : Character(n, h, m, l), strength(s) {}
    
    void attack() const override {
        cout << name << " swings a mighty sword! Damage: " << strength * 2 << endl;
    }
    
    void defend() const override {
        cout << name << " raises shield, reducing incoming damage!" << endl;
    }
    
    void specialAbility() const override {
        cout << name << " performs Whirlwind Attack! All enemies take " 
             << strength * 3 << " damage!" << endl;
    }
    
    void displayStats() const override {
        cout << "=== Warrior: " << name << " ===" << endl;
        cout << "Level: " << level << ", Health: " << health << ", Mana: " << mana << endl;
        cout << "Strength: " << strength << endl;
    }
};

class Mage : public Character {
private:
    int intelligence;
    
public:
    Mage(string n, int h, int m, int l, int i) 
        : Character(n, h, m, l), intelligence(i) {}
    
    void attack() const override {
        cout << name << " casts Fireball! Damage: " << intelligence * 2 << endl;
    }
    
    void defend() const override {
        cout << name << " creates a magical barrier!" << endl;
    }
    
    void specialAbility() const override {
        cout << name << " summons Meteor Shower! Damage: " 
             << intelligence * 4 << endl;
    }
    
    void displayStats() const override {
        cout << "=== Mage: " << name << " ===" << endl;
        cout << "Level: " << level << ", Health: " << health << ", Mana: " << mana << endl;
        cout << "Intelligence: " << intelligence << endl;
    }
    
    void heal(int amount) override {
        // Mages heal more effectively
        int bonus = intelligence / 10;
        Character::heal(amount + bonus);
    }
};

class Archer : public Character {
private:
    int dexterity;
    
public:
    Archer(string n, int h, int m, int l, int d) 
        : Character(n, h, m, l), dexterity(d) {}
    
    void attack() const override {
        cout << name << " shoots an arrow! Damage: " << dexterity * 1.5 << endl;
    }
    
    void defend() const override {
        cout << name << " dodges the attack!" << endl;
    }
    
    void specialAbility() const override {
        cout << name << " fires a volley of arrows! Damage: " 
             << dexterity * 2.5 << endl;
    }
    
    void displayStats() const override {
        cout << "=== Archer: " << name << " ===" << endl;
        cout << "Level: " << level << ", Health: " << health << ", Mana: " << mana << endl;
        cout << "Dexterity: " << dexterity << endl;
    }
};

class Battle {
private:
    vector<unique_ptr<Character>> party;
    vector<unique_ptr<Character>> enemies;
    
public:
    void addPartyMember(Character* c) {
        party.emplace_back(c);
    }
    
    void addEnemy(Character* e) {
        enemies.emplace_back(e);
    }
    
    void displayStatus() const {
        cout << "\n=== Party ===" << endl;
        for (const auto& c : party) {
            c->displayStats();
        }
        
        cout << "\n=== Enemies ===" << endl;
        for (const auto& e : enemies) {
            e->displayStats();
        }
    }
    
    void simulateBattle() {
        cout << "\n=== Battle Begins! ===" << endl;
        
        while (!party.empty() && !enemies.empty()) {
            displayStatus();
            
            // Party attacks
            for (auto& attacker : party) {
                if (attacker->isAlive() && !enemies.empty()) {
                    cout << "\n" << attacker->getName() << " attacks!" << endl;
                    attacker->attack();
                    
                    // First enemy takes damage
                    enemies[0]->takeDamage(20);
                    if (!enemies[0]->isAlive()) {
                        cout << enemies[0]->getName() << " defeated!" << endl;
                        enemies.erase(enemies.begin());
                    }
                }
            }
            
            // Enemies attack
            for (auto& attacker : enemies) {
                if (attacker->isAlive() && !party.empty()) {
                    cout << "\n" << attacker->getName() << " attacks!" << endl;
                    attacker->attack();
                    
                    party[0]->takeDamage(15);
                    if (!party[0]->isAlive()) {
                        cout << party[0]->getName() << " defeated!" << endl;
                        party.erase(party.begin());
                    }
                }
            }
        }
        
        if (!party.empty()) {
            cout << "\n=== Victory! Party wins! ===" << endl;
        } else {
            cout << "\n=== Defeat! Party is defeated! ===" << endl;
        }
    }
};

int main() {
    cout << "=== Game Character System with Virtual Functions ===" << endl;
    
    Battle battle;
    
    // Create party
    battle.addPartyMember(new Warrior("Conan", 120, 50, 5, 25));
    battle.addPartyMember(new Mage("Gandalf", 80, 100, 5, 30));
    battle.addPartyMember(new Archer("Legolas", 90, 60, 5, 28));
    
    // Create enemies
    battle.addEnemy(new Warrior("Orc Chieftain", 100, 30, 4, 20));
    battle.addEnemy(new Mage("Dark Wizard", 70, 80, 4, 25));
    
    battle.simulateBattle();
    
    return 0;
}
```

---

## 📊 Virtual Functions Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Enable run-time polymorphism |
| **Syntax** | `virtual returnType functionName(params);` |
| **Override** | `override` keyword (C++11) explicitly marks overrides |
| **vtable** | Virtual table containing function pointers |
| **vptr** | Virtual pointer in each object |
| **Cost** | Memory (vptr) and slight runtime overhead |

---

## ✅ Best Practices

1. **Make base destructors virtual** for polymorphic classes
2. **Use `override` keyword** to explicitly mark overridden functions
3. **Use `final` keyword** to prevent further overriding
4. **Never call virtual functions** in constructor or destructor
5. **Prefer pure virtual functions** for interfaces
6. **Use smart pointers** for polymorphic objects

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Missing virtual destructor** | Memory leak in polymorphism | Make base destructor virtual |
| **Calling virtual in constructor** | Wrong function called | Avoid virtual calls in constructor |
| **Forgetting `override`** | Hard to maintain | Use `override` keyword |
| **Object slicing** | Loss of derived data | Use pointers/references |
| **Not using `virtual` in base** | No polymorphism | Declare functions virtual in base |

---

## ✅ Key Takeaways

1. **Virtual functions** enable run-time polymorphism
2. **Dynamic dispatch** uses vtable and vptr
3. **Pure virtual functions** make class abstract
4. **Virtual destructor** is essential for polymorphic base classes
5. **`override` keyword** ensures correct overriding
6. **Never call virtual** in constructor or destructor

---
---

## Next Step

- Go to [02_Override_Specifier.md](02_Override_Specifier.md) to continue with Override Specifier.
