# Prototype Pattern in C++ - Complete Guide

## 📖 Overview

The Prototype pattern creates new objects by cloning existing objects, rather than calling constructors. This pattern is useful when object creation is expensive, or when objects need to be created with the same state as existing objects. Prototype reduces the need for subclasses and provides a way to create objects with dynamic types.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Prototype** | Interface for cloning itself |
| **Concrete Prototype** | Implements cloning method |
| **Clone** | Creates a copy of the object |
| **Deep Copy** | Copies all member data, including dynamically allocated memory |
| **Shallow Copy** | Copies only member values (pointers are copied, not the data) |

---

## 1. **Basic Prototype Pattern**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <cstring>
using namespace std;

// Prototype interface
class Shape {
protected:
    string color;
    int x, y;
    
public:
    Shape(string c, int xPos, int yPos) : color(c), x(xPos), y(yPos) {}
    
    virtual unique_ptr<Shape> clone() const = 0;
    virtual void draw() const = 0;
    
    virtual ~Shape() = default;
    
    void move(int dx, int dy) {
        x += dx;
        y += dy;
    }
};

// Concrete prototype 1
class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(string c, int xPos, int yPos, double r) 
        : Shape(c, xPos, yPos), radius(r) {}
    
    unique_ptr<Shape> clone() const override {
        return make_unique<Circle>(*this);
    }
    
    void draw() const override {
        cout << "Circle: " << color << " at (" << x << ", " << y 
             << ") radius=" << radius << endl;
    }
    
    void setRadius(double r) { radius = r; }
};

// Concrete prototype 2
class Rectangle : public Shape {
private:
    double width, height;
    
public:
    Rectangle(string c, int xPos, int yPos, double w, double h) 
        : Shape(c, xPos, yPos), width(w), height(h) {}
    
    unique_ptr<Shape> clone() const override {
        return make_unique<Rectangle>(*this);
    }
    
    void draw() const override {
        cout << "Rectangle: " << color << " at (" << x << ", " << y 
             << ") size=" << width << "x" << height << endl;
    }
    
    void setSize(double w, double h) {
        width = w;
        height = h;
    }
};

int main() {
    cout << "=== Basic Prototype Pattern ===" << endl;
    
    // Create original objects
    Circle originalCircle("Red", 10, 20, 5.0);
    Rectangle originalRect("Blue", 30, 40, 10.0, 6.0);
    
    cout << "\n1. Original objects:" << endl;
    originalCircle.draw();
    originalRect.draw();
    
    // Clone objects
    auto clonedCircle = originalCircle.clone();
    auto clonedRect = originalRect.clone();
    
    cout << "\n2. Cloned objects (same as originals):" << endl;
    clonedCircle->draw();
    clonedRect->draw();
    
    // Modify clones
    clonedCircle->move(5, 10);
    clonedCircle->setRadius(7.0);
    clonedRect->move(-10, -5);
    clonedRect->setSize(15.0, 8.0);
    
    cout << "\n3. Modified clones:" << endl;
    clonedCircle->draw();
    clonedRect->draw();
    
    cout << "\n4. Originals unchanged:" << endl;
    originalCircle.draw();
    originalRect.draw();
    
    return 0;
}
```

**Output:**
```
=== Basic Prototype Pattern ===

1. Original objects:
Circle: Red at (10, 20) radius=5
Rectangle: Blue at (30, 40) size=10x6

2. Cloned objects (same as originals):
Circle: Red at (10, 20) radius=5
Rectangle: Blue at (30, 40) size=10x6

3. Modified clones:
Circle: Red at (15, 30) radius=7
Rectangle: Blue at (20, 35) size=15x8

4. Originals unchanged:
Circle: Red at (10, 20) radius=5
Rectangle: Blue at (30, 40) size=10x6
```

---

## 2. **Deep Copy vs Shallow Copy**

```cpp
#include <iostream>
#include <string>
#include <cstring>
#include <memory>
using namespace std;

// Bad: Shallow copy (dangerous)
class ShallowDocument {
private:
    char* content;
    int length;
    
public:
    ShallowDocument(const char* text) {
        length = strlen(text);
        content = new char[length + 1];
        strcpy(content, text);
        cout << "Created: " << content << endl;
    }
    
    // Shallow copy (default copy constructor) - DANGEROUS!
    ShallowDocument(const ShallowDocument& other) 
        : content(other.content), length(other.length) {
        cout << "Shallow copy: " << content << endl;
    }
    
    ~ShallowDocument() {
        if (content) {
            cout << "Destroying: " << content << endl;
            delete[] content;
        }
    }
    
    void modify(const char* text) {
        delete[] content;
        length = strlen(text);
        content = new char[length + 1];
        strcpy(content, text);
    }
    
    void display() const {
        cout << "Content: " << content << endl;
    }
};

// Good: Deep copy (safe)
class DeepDocument {
private:
    char* content;
    int length;
    
public:
    DeepDocument(const char* text) {
        length = strlen(text);
        content = new char[length + 1];
        strcpy(content, text);
        cout << "Created: " << content << endl;
    }
    
    // Deep copy (safe)
    DeepDocument(const DeepDocument& other) {
        length = other.length;
        content = new char[length + 1];
        strcpy(content, other.content);
        cout << "Deep copy: " << content << endl;
    }
    
    ~DeepDocument() {
        if (content) {
            cout << "Destroying: " << content << endl;
            delete[] content;
        }
    }
    
    void modify(const char* text) {
        delete[] content;
        length = strlen(text);
        content = new char[length + 1];
        strcpy(content, text);
    }
    
    void display() const {
        cout << "Content: " << content << endl;
    }
};

int main() {
    cout << "=== Deep Copy vs Shallow Copy ===" << endl;
    
    cout << "\n1. Shallow Copy (DANGEROUS):" << endl;
    ShallowDocument doc1("Original");
    ShallowDocument doc2 = doc1;  // Shallow copy - shares same pointer!
    
    cout << "Before modification:" << endl;
    doc1.display();
    doc2.display();
    
    cout << "Modifying doc1..." << endl;
    doc1.modify("Modified");
    
    cout << "After modification:" << endl;
    doc1.display();
    doc2.display();  // doc2 also changed! (shared memory)
    
    cout << "\n2. Deep Copy (SAFE):" << endl;
    DeepDocument deep1("Original");
    DeepDocument deep2 = deep1;  // Deep copy - separate memory
    
    cout << "Before modification:" << endl;
    deep1.display();
    deep2.display();
    
    cout << "Modifying deep1..." << endl;
    deep1.modify("Modified");
    
    cout << "After modification:" << endl;
    deep1.display();
    deep2.display();  // deep2 unchanged!
    
    return 0;
}
```

---

## 3. **Prototype Registry**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <unordered_map>
using namespace std;

// Prototype interface
class Enemy {
protected:
    string type;
    int health;
    int damage;
    
public:
    Enemy(string t, int h, int d) : type(t), health(h), damage(d) {}
    
    virtual unique_ptr<Enemy> clone() const = 0;
    virtual void display() const = 0;
    virtual ~Enemy() = default;
    
    string getType() const { return type; }
};

// Concrete prototypes
class Goblin : public Enemy {
public:
    Goblin() : Enemy("Goblin", 30, 5) {}
    
    unique_ptr<Enemy> clone() const override {
        return make_unique<Goblin>(*this);
    }
    
    void display() const override {
        cout << "Goblin: Health=" << health << ", Damage=" << damage << endl;
    }
};

class Orc : public Enemy {
public:
    Orc() : Enemy("Orc", 80, 15) {}
    
    unique_ptr<Enemy> clone() const override {
        return make_unique<Orc>(*this);
    }
    
    void display() const override {
        cout << "Orc: Health=" << health << ", Damage=" << damage << endl;
    }
};

class Dragon : public Enemy {
public:
    Dragon() : Enemy("Dragon", 200, 40) {}
    
    unique_ptr<Enemy> clone() const override {
        return make_unique<Dragon>(*this);
    }
    
    void display() const override {
        cout << "Dragon: Health=" << health << ", Damage=" << damage << endl;
    }
};

// Prototype Registry
class EnemyRegistry {
private:
    unordered_map<string, unique_ptr<Enemy>> prototypes;
    
public:
    void registerEnemy(const string& key, unique_ptr<Enemy> prototype) {
        prototypes[key] = move(prototype);
        cout << "Registered: " << key << endl;
    }
    
    unique_ptr<Enemy> createEnemy(const string& key) {
        auto it = prototypes.find(key);
        if (it != prototypes.end()) {
            return it->second->clone();
        }
        return nullptr;
    }
};

int main() {
    cout << "=== Prototype Registry ===" << endl;
    
    EnemyRegistry registry;
    
    // Register prototypes
    registry.registerEnemy("goblin", make_unique<Goblin>());
    registry.registerEnemy("orc", make_unique<Orc>());
    registry.registerEnemy("dragon", make_unique<Dragon>());
    
    cout << "\n1. Creating enemies from registry:" << endl;
    auto goblin1 = registry.createEnemy("goblin");
    auto goblin2 = registry.createEnemy("goblin");
    auto orc1 = registry.createEnemy("orc");
    auto dragon1 = registry.createEnemy("dragon");
    
    goblin1->display();
    goblin2->display();
    orc1->display();
    dragon1->display();
    
    cout << "\n2. Creating non-existent enemy:" << endl;
    auto unknown = registry.createEnemy("unknown");
    if (!unknown) {
        cout << "Enemy type not registered!" << endl;
    }
    
    return 0;
}
```

---

## 4. **Prototype with Complex Objects**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
using namespace std;

class Property {
public:
    string key;
    string value;
    
    Property(string k, string v) : key(k), value(v) {}
    
    Property* clone() const {
        return new Property(key, value);
    }
};

class GameObject {
private:
    string name;
    vector<Property*> properties;
    int* id;
    
public:
    GameObject(string n, int i) : name(n) {
        id = new int(i);
        cout << "GameObject created: " << name << " (ID: " << *id << ")" << endl;
    }
    
    // Deep copy constructor
    GameObject(const GameObject& other) {
        name = other.name;
        id = new int(*other.id);
        
        // Deep copy properties
        for (auto prop : other.properties) {
            properties.push_back(prop->clone());
        }
        
        cout << "GameObject cloned: " << name << " (ID: " << *id << ")" << endl;
    }
    
    ~GameObject() {
        delete id;
        for (auto prop : properties) {
            delete prop;
        }
        cout << "GameObject destroyed: " << name << endl;
    }
    
    void addProperty(const string& key, const string& value) {
        properties.push_back(new Property(key, value));
    }
    
    void setID(int i) { *id = i; }
    
    void display() const {
        cout << "GameObject: " << name << " (ID: " << *id << ")" << endl;
        cout << "  Properties:" << endl;
        for (auto prop : properties) {
            cout << "    " << prop->key << " = " << prop->value << endl;
        }
    }
    
    GameObject* clone() const {
        return new GameObject(*this);
    }
};

int main() {
    cout << "=== Prototype with Complex Objects ===" << endl;
    
    // Create original object
    GameObject* original = new GameObject("Player", 1001);
    original->addProperty("health", "100");
    original->addProperty("mana", "50");
    original->addProperty("level", "5");
    
    cout << "\n1. Original object:" << endl;
    original->display();
    
    // Clone the object
    GameObject* clone = original->clone();
    
    cout << "\n2. Cloned object (same data):" << endl;
    clone->display();
    
    // Modify clone
    clone->setID(1002);
    clone->addProperty("experience", "2500");
    
    cout << "\n3. Modified clone:" << endl;
    clone->display();
    
    cout << "\n4. Original unchanged:" << endl;
    original->display();
    
    delete original;
    delete clone;
    
    return 0;
}
```

---

## 5. **Practical Example: Document Template System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <map>
using namespace std;

// Prototype
class Document {
protected:
    string title;
    string author;
    string content;
    vector<string> tags;
    
public:
    Document(string t, string a) : title(t), author(a) {}
    
    virtual unique_ptr<Document> clone() const = 0;
    virtual void render() const = 0;
    
    void addTag(const string& tag) {
        tags.push_back(tag);
    }
    
    void setContent(const string& c) {
        content = c;
    }
    
    void setTitle(const string& t) {
        title = t;
    }
    
    void setAuthor(const string& a) {
        author = a;
    }
    
    virtual ~Document() = default;
    
protected:
    void renderCommon() const {
        cout << "Title: " << title << endl;
        cout << "Author: " << author << endl;
        if (!tags.empty()) {
            cout << "Tags: ";
            for (const auto& t : tags) cout << t << " ";
            cout << endl;
        }
    }
};

// Concrete prototypes
class ReportDocument : public Document {
public:
    ReportDocument() : Document("Untitled Report", "Unknown") {}
    
    unique_ptr<Document> clone() const override {
        return make_unique<ReportDocument>(*this);
    }
    
    void render() const override {
        cout << "\n=== REPORT ===" << endl;
        renderCommon();
        cout << "Report Content:\n" << content << endl;
    }
};

class InvoiceDocument : public Document {
private:
    double amount;
    string customer;
    
public:
    InvoiceDocument() : Document("Untitled Invoice", "Unknown"), amount(0), customer("") {}
    
    unique_ptr<Document> clone() const override {
        return make_unique<InvoiceDocument>(*this);
    }
    
    void setAmount(double a) { amount = a; }
    void setCustomer(const string& c) { customer = c; }
    
    void render() const override {
        cout << "\n=== INVOICE ===" << endl;
        renderCommon();
        cout << "Customer: " << customer << endl;
        cout << "Amount: $" << amount << endl;
        cout << "Invoice Content:\n" << content << endl;
    }
};

class LetterDocument : public Document {
private:
    string recipient;
    string sender;
    
public:
    LetterDocument() : Document("Untitled Letter", "Unknown"), recipient(""), sender("") {}
    
    unique_ptr<Document> clone() const override {
        return make_unique<LetterDocument>(*this);
    }
    
    void setRecipient(const string& r) { recipient = r; }
    void setSender(const string& s) { sender = s; }
    
    void render() const override {
        cout << "\n=== LETTER ===" << endl;
        cout << "From: " << sender << endl;
        cout << "To: " << recipient << endl;
        renderCommon();
        cout << "Letter Content:\n" << content << endl;
    }
};

class DocumentTemplateManager {
private:
    map<string, unique_ptr<Document>> templates;
    
public:
    void registerTemplate(const string& name, unique_ptr<Document> doc) {
        templates[name] = move(doc);
        cout << "Template registered: " << name << endl;
    }
    
    unique_ptr<Document> createDocument(const string& name) {
        auto it = templates.find(name);
        if (it != templates.end()) {
            return it->second->clone();
        }
        return nullptr;
    }
};

int main() {
    cout << "=== Document Template System ===" << endl;
    
    DocumentTemplateManager manager;
    
    // Register templates
    manager.registerTemplate("report", make_unique<ReportDocument>());
    manager.registerTemplate("invoice", make_unique<InvoiceDocument>());
    manager.registerTemplate("letter", make_unique<LetterDocument>());
    
    cout << "\n1. Creating documents from templates:" << endl;
    
    auto report = manager.createDocument("report");
    report->setTitle("Annual Sales Report");
    report->setAuthor("Sales Team");
    report->addTag("sales");
    report->addTag("annual");
    report->setContent("Sales increased by 25% this year...");
    report->render();
    
    auto invoice = manager.createDocument("invoice");
    invoice->setTitle("Invoice #INV-2024-001");
    invoice->setAuthor("Billing Dept");
    invoice->setContent("Product: Premium Subscription\nQuantity: 1\nPrice: $299.99");
    dynamic_cast<InvoiceDocument*>(invoice.get())->setAmount(299.99);
    dynamic_cast<InvoiceDocument*>(invoice.get())->setCustomer("Acme Corp");
    invoice->render();
    
    auto letter = manager.createDocument("letter");
    letter->setTitle("Welcome Letter");
    letter->setAuthor("HR Department");
    letter->setContent("Welcome to the team! We're excited to have you aboard.");
    dynamic_cast<LetterDocument*>(letter.get())->setRecipient("John Doe");
    dynamic_cast<LetterDocument*>(letter.get())->setSender("HR Team");
    letter->render();
    
    cout << "\n2. Creating another report (clone of template):" << endl;
    auto report2 = manager.createDocument("report");
    report2->setTitle("Q1 Performance Review");
    report2->setAuthor("Manager");
    report2->render();
    
    return 0;
}
```

---

## 📊 Prototype Pattern Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Create objects by cloning existing ones |
| **Clone Method** | Returns a copy of the object |
| **Deep Copy** | Copies all data, including dynamically allocated memory |
| **Registry** | Stores and retrieves prototypes by key |

---

## ✅ Best Practices

1. **Implement deep copy** for objects with dynamic memory
2. **Use smart pointers** for automatic memory management
3. **Make clone method virtual** for polymorphic cloning
4. **Consider using registry** for managing prototypes
5. **Protect against self-assignment** in copy constructors
6. **Use `make_unique`/`make_shared`** for creating clones

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Shallow copy** | Shared pointers cause double delete | Implement deep copy |
| **Forgetting virtual destructor** | Memory leak | Make destructor virtual |
| **Incomplete clone** | Missing members in copy | Copy all members |
| **Circular references** | Infinite recursion | Handle with care or use weak_ptr |

---

## ✅ Key Takeaways

1. **Prototype pattern** creates objects by cloning
2. **Useful when** object creation is expensive
3. **Deep copy** is essential for objects with dynamic memory
4. **Registry pattern** complements prototype
5. **Reduces subclassing** - no need for factory classes
6. **Supports** dynamic object creation at runtime

---
---

## Next Step

- Go to [02_Structural_Patterns](../02_Structural_Patterns/README.md) to continue.
