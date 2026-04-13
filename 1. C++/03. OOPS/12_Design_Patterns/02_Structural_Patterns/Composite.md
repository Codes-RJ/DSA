# Composite Pattern in C++ - Complete Guide

## 📖 Overview

The Composite pattern composes objects into tree structures to represent part-whole hierarchies. It allows clients to treat individual objects and compositions of objects uniformly. This pattern is particularly useful for representing hierarchical structures like file systems, organizational charts, or UI components.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Component** | Abstract interface for all objects in the composition |
| **Leaf** | Primitive object that has no children |
| **Composite** | Container object that can contain other components |
| **Uniformity** | Clients treat leaves and composites the same way |

---

## 1. **Basic Composite Pattern**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
using namespace std;

// Component interface
class Graphic {
public:
    virtual void draw() const = 0;
    virtual void add(Graphic* g) {}
    virtual void remove(Graphic* g) {}
    virtual Graphic* getChild(int index) { return nullptr; }
    virtual ~Graphic() = default;
};

// Leaf
class Circle : public Graphic {
private:
    int id;
    static int nextId;
    
public:
    Circle() : id(nextId++) {}
    
    void draw() const override {
        cout << "  Circle " << id << " drawn" << endl;
    }
};

int Circle::nextId = 1;

// Leaf
class Rectangle : public Graphic {
private:
    int id;
    static int nextId;
    
public:
    Rectangle() : id(nextId++) {}
    
    void draw() const override {
        cout << "  Rectangle " << id << " drawn" << endl;
    }
};

int Rectangle::nextId = 1;

// Composite
class CompositeGraphic : public Graphic {
private:
    vector<unique_ptr<Graphic>> children;
    
public:
    void add(Graphic* g) override {
        children.emplace_back(g);
    }
    
    void draw() const override {
        cout << "Composite Graphic drawing:" << endl;
        for (const auto& child : children) {
            child->draw();
        }
    }
    
    Graphic* getChild(int index) override {
        if (index >= 0 && index < children.size()) {
            return children[index].get();
        }
        return nullptr;
    }
};

int main() {
    cout << "=== Basic Composite Pattern ===" << endl;
    
    // Create leaves
    Circle* c1 = new Circle();
    Circle* c2 = new Circle();
    Rectangle* r1 = new Rectangle();
    
    // Create composite
    CompositeGraphic* composite = new CompositeGraphic();
    composite->add(c1);
    composite->add(r1);
    
    // Create another composite
    CompositeGraphic* root = new CompositeGraphic();
    root->add(c2);
    root->add(composite);
    
    // Draw everything (uniform treatment)
    cout << "Drawing root composite:" << endl;
    root->draw();
    
    delete root;
    
    return 0;
}
```

**Output:**
```
=== Basic Composite Pattern ===
Drawing root composite:
Composite Graphic drawing:
  Circle 2 drawn
Composite Graphic drawing:
  Circle 1 drawn
  Rectangle 1 drawn
```

---

## 2. **File System Example**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
#include <iomanip>
using namespace std;

// Component
class FileSystemNode {
protected:
    string name;
    
public:
    FileSystemNode(const string& n) : name(n) {}
    
    virtual void display(int depth = 0) const = 0;
    virtual int getSize() const = 0;
    virtual bool isDirectory() const = 0;
    virtual ~FileSystemNode() = default;
    
    string getName() const { return name; }
};

// Leaf: File
class File : public FileSystemNode {
private:
    int size;
    
public:
    File(const string& n, int s) : FileSystemNode(n), size(s) {}
    
    void display(int depth = 0) const override {
        cout << string(depth * 2, ' ') << "📄 " << name 
             << " (" << size << " bytes)" << endl;
    }
    
    int getSize() const override {
        return size;
    }
    
    bool isDirectory() const override {
        return false;
    }
};

// Composite: Directory
class Directory : public FileSystemNode {
private:
    vector<unique_ptr<FileSystemNode>> children;
    
public:
    Directory(const string& n) : FileSystemNode(n) {}
    
    void add(FileSystemNode* node) {
        children.emplace_back(node);
    }
    
    void remove(const string& name) {
        auto it = find_if(children.begin(), children.end(),
            [&](const auto& node) { return node->getName() == name; });
        if (it != children.end()) {
            children.erase(it);
        }
    }
    
    FileSystemNode* getChild(const string& name) {
        auto it = find_if(children.begin(), children.end(),
            [&](const auto& node) { return node->getName() == name; });
        if (it != children.end()) {
            return it->get();
        }
        return nullptr;
    }
    
    void display(int depth = 0) const override {
        cout << string(depth * 2, ' ') << "📁 " << name << "/" << endl;
        for (const auto& child : children) {
            child->display(depth + 1);
        }
    }
    
    int getSize() const override {
        int total = 0;
        for (const auto& child : children) {
            total += child->getSize();
        }
        return total;
    }
    
    bool isDirectory() const override {
        return true;
    }
};

int main() {
    cout << "=== File System Example ===" << endl;
    
    // Create files
    File* file1 = new File("document.txt", 1024);
    File* file2 = new File("image.jpg", 2048);
    File* file3 = new File("data.csv", 512);
    File* file4 = new File("config.ini", 128);
    
    // Create directories
    Directory* root = new Directory("root");
    Directory* documents = new Directory("documents");
    Directory* pictures = new Directory("pictures");
    Directory* data = new Directory("data");
    
    // Build tree
    root->add(documents);
    root->add(pictures);
    root->add(data);
    
    documents->add(file1);
    documents->add(file4);
    
    pictures->add(file2);
    
    data->add(file3);
    
    // Display file system
    cout << "\nFile System Structure:" << endl;
    root->display();
    
    cout << "\nTotal size: " << root->getSize() << " bytes" << endl;
    
    delete root;
    
    return 0;
}
```

---

## 3. **Company Organization Example**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <iomanip>
using namespace std;

// Component
class Employee {
protected:
    string name;
    string position;
    double salary;
    
public:
    Employee(const string& n, const string& p, double s) 
        : name(n), position(p), salary(s) {}
    
    virtual void display(int depth = 0) const = 0;
    virtual double getTotalSalary() const = 0;
    virtual int getEmployeeCount() const = 0;
    virtual ~Employee() = default;
    
    string getName() const { return name; }
    string getPosition() const { return position; }
};

// Leaf: Individual Employee
class IndividualEmployee : public Employee {
public:
    IndividualEmployee(const string& n, const string& p, double s) 
        : Employee(n, p, s) {}
    
    void display(int depth = 0) const override {
        cout << string(depth * 2, ' ') << "👤 " << name 
             << " (" << position << ") - $" << fixed << setprecision(2) << salary << endl;
    }
    
    double getTotalSalary() const override {
        return salary;
    }
    
    int getEmployeeCount() const override {
        return 1;
    }
};

// Composite: Department
class Department : public Employee {
private:
    vector<unique_ptr<Employee>> employees;
    
public:
    Department(const string& n, const string& p) 
        : Employee(n, p, 0) {}
    
    void add(Employee* emp) {
        employees.emplace_back(emp);
    }
    
    void remove(const string& name) {
        auto it = find_if(employees.begin(), employees.end(),
            [&](const auto& emp) { return emp->getName() == name; });
        if (it != employees.end()) {
            employees.erase(it);
        }
    }
    
    void display(int depth = 0) const override {
        cout << string(depth * 2, ' ') << "🏢 " << name 
             << " (" << position << ")" << endl;
        for (const auto& emp : employees) {
            emp->display(depth + 1);
        }
    }
    
    double getTotalSalary() const override {
        double total = 0;
        for (const auto& emp : employees) {
            total += emp->getTotalSalary();
        }
        return total;
    }
    
    int getEmployeeCount() const override {
        int count = 0;
        for (const auto& emp : employees) {
            count += emp->getEmployeeCount();
        }
        return count;
    }
};

int main() {
    cout << "=== Company Organization Example ===" << endl;
    
    // Create individual employees
    IndividualEmployee* ceo = new IndividualEmployee("John Smith", "CEO", 300000);
    IndividualEmployee* vp1 = new IndividualEmployee("Alice Johnson", "VP Engineering", 200000);
    IndividualEmployee* vp2 = new IndividualEmployee("Bob Williams", "VP Sales", 200000);
    IndividualEmployee* manager1 = new IndividualEmployee("Charlie Brown", "Engineering Manager", 150000);
    IndividualEmployee* manager2 = new IndividualEmployee("Diana Prince", "Sales Manager", 150000);
    IndividualEmployee* dev1 = new IndividualEmployee("Eve Wilson", "Senior Developer", 120000);
    IndividualEmployee* dev2 = new IndividualEmployee("Frank Castle", "Developer", 90000);
    IndividualEmployee* dev3 = new IndividualEmployee("Grace Hopper", "Developer", 95000);
    IndividualEmployee* sales1 = new IndividualEmployee("Henry Ford", "Sales Rep", 80000);
    IndividualEmployee* sales2 = new IndividualEmployee("Irene Adler", "Sales Rep", 85000);
    
    // Create departments
    Department* engineering = new Department("Engineering Department", "Department");
    Department* sales = new Department("Sales Department", "Department");
    Department* company = new Department("Tech Corp", "Company");
    
    // Build hierarchy
    engineering->add(manager1);
    engineering->add(dev1);
    engineering->add(dev2);
    engineering->add(dev3);
    
    sales->add(manager2);
    sales->add(sales1);
    sales->add(sales2);
    
    company->add(ceo);
    company->add(vp1);
    company->add(vp2);
    company->add(engineering);
    company->add(sales);
    
    // Display organization
    cout << "\nOrganization Structure:" << endl;
    company->display();
    
    cout << "\nTotal Employees: " << company->getEmployeeCount() << endl;
    cout << "Total Salary Budget: $" << fixed << setprecision(2) 
         << company->getTotalSalary() << endl;
    
    delete company;
    
    return 0;
}
```

---

## 4. **Menu System Example**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <functional>
using namespace std;

// Component
class MenuComponent {
protected:
    string name;
    
public:
    MenuComponent(const string& n) : name(n) {}
    
    virtual void display(int depth = 0) const = 0;
    virtual void execute() const = 0;
    virtual void add(MenuComponent* component) {}
    virtual void remove(MenuComponent* component) {}
    virtual MenuComponent* getChild(int index) { return nullptr; }
    virtual ~MenuComponent() = default;
    
    string getName() const { return name; }
};

// Leaf: Menu Item
class MenuItem : public MenuComponent {
private:
    function<void()> action;
    
public:
    MenuItem(const string& n, function<void()> a) 
        : MenuComponent(n), action(a) {}
    
    void display(int depth = 0) const override {
        cout << string(depth * 2, ' ') << "📄 " << name << endl;
    }
    
    void execute() const override {
        cout << "Executing: " << name << endl;
        if (action) {
            action();
        }
    }
};

// Composite: Submenu
class Submenu : public MenuComponent {
private:
    vector<unique_ptr<MenuComponent>> children;
    
public:
    Submenu(const string& n) : MenuComponent(n) {}
    
    void add(MenuComponent* component) override {
        children.emplace_back(component);
    }
    
    void remove(MenuComponent* component) override {
        auto it = find_if(children.begin(), children.end(),
            [component](const auto& c) { return c.get() == component; });
        if (it != children.end()) {
            children.erase(it);
        }
    }
    
    MenuComponent* getChild(int index) override {
        if (index >= 0 && index < children.size()) {
            return children[index].get();
        }
        return nullptr;
    }
    
    void display(int depth = 0) const override {
        cout << string(depth * 2, ' ') << "📁 " << name << endl;
        for (const auto& child : children) {
            child->display(depth + 1);
        }
    }
    
    void execute() const override {
        cout << "Opening menu: " << name << endl;
        // Submenu doesn't have its own action
    }
};

class MenuBar {
private:
    vector<unique_ptr<MenuComponent>> menus;
    
public:
    void addMenu(MenuComponent* menu) {
        menus.emplace_back(menu);
    }
    
    void display() const {
        cout << "\n=== Menu Bar ===" << endl;
        for (const auto& menu : menus) {
            menu->display();
        }
    }
    
    MenuComponent* findMenu(const string& name) {
        for (auto& menu : menus) {
            if (menu->getName() == name) {
                return menu.get();
            }
        }
        return nullptr;
    }
};

int main() {
    cout << "=== Menu System Example ===" << endl;
    
    // Create actions
    auto newFileAction = []() { cout << "  Creating new file..." << endl; };
    auto openFileAction = []() { cout << "  Opening file..." << endl; };
    auto saveFileAction = []() { cout << "  Saving file..." << endl; };
    auto exitAction = []() { cout << "  Exiting application..." << endl; };
    auto cutAction = []() { cout << "  Cutting text..." << endl; };
    auto copyAction = []() { cout << "  Copying text..." << endl; };
    auto pasteAction = []() { cout << "  Pasting text..." << endl; };
    auto aboutAction = []() { cout << "  About dialog shown" << endl; };
    
    // Build File menu
    Submenu* fileMenu = new Submenu("File");
    fileMenu->add(new MenuItem("New", newFileAction));
    fileMenu->add(new MenuItem("Open", openFileAction));
    fileMenu->add(new MenuItem("Save", saveFileAction));
    fileMenu->add(new MenuItem("Exit", exitAction));
    
    // Build Edit menu
    Submenu* editMenu = new Submenu("Edit");
    editMenu->add(new MenuItem("Cut", cutAction));
    editMenu->add(new MenuItem("Copy", copyAction));
    editMenu->add(new MenuItem("Paste", pasteAction));
    
    // Build Help menu
    Submenu* helpMenu = new Submenu("Help");
    helpMenu->add(new MenuItem("About", aboutAction));
    
    // Create menu bar
    MenuBar menuBar;
    menuBar.addMenu(fileMenu);
    menuBar.addMenu(editMenu);
    menuBar.addMenu(helpMenu);
    
    // Display menu bar
    menuBar.display();
    
    // Simulate user actions
    cout << "\n=== User Actions ===" << endl;
    
    auto file = menuBar.findMenu("File");
    if (file) {
        auto child = file->getChild(0);
        if (child) child->execute();
        child = file->getChild(2);
        if (child) child->execute();
        child = file->getChild(3);
        if (child) child->execute();
    }
    
    auto edit = menuBar.findMenu("Edit");
    if (edit) {
        auto child = edit->getChild(1);
        if (child) child->execute();
        child = edit->getChild(2);
        if (child) child->execute();
    }
    
    auto help = menuBar.findMenu("Help");
    if (help) {
        auto child = help->getChild(0);
        if (child) child->execute();
    }
    
    delete fileMenu;
    delete editMenu;
    delete helpMenu;
    
    return 0;
}
```

---

## 5. **Practical Example: Graphic Design Tool**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <cmath>
using namespace std;

// Component
class GraphicElement {
protected:
    string name;
    double x, y;
    
public:
    GraphicElement(const string& n, double xPos, double yPos) 
        : name(n), x(xPos), y(yPos) {}
    
    virtual void draw() const = 0;
    virtual void move(double dx, double dy) {
        x += dx;
        y += dy;
    }
    
    virtual double getArea() const = 0;
    virtual void add(GraphicElement* g) {}
    virtual void remove(GraphicElement* g) {}
    virtual GraphicElement* getChild(int index) { return nullptr; }
    virtual ~GraphicElement() = default;
    
    string getName() const { return name; }
};

// Leaf: Circle
class CircleElement : public GraphicElement {
private:
    double radius;
    
public:
    CircleElement(const string& n, double xPos, double yPos, double r) 
        : GraphicElement(n, xPos, yPos), radius(r) {}
    
    void draw() const override {
        cout << "  Circle '" << name << "' at (" << x << ", " << y 
             << ") radius=" << radius << endl;
    }
    
    double getArea() const override {
        return M_PI * radius * radius;
    }
};

// Leaf: Rectangle
class RectangleElement : public GraphicElement {
private:
    double width, height;
    
public:
    RectangleElement(const string& n, double xPos, double yPos, double w, double h) 
        : GraphicElement(n, xPos, yPos), width(w), height(h) {}
    
    void draw() const override {
        cout << "  Rectangle '" << name << "' at (" << x << ", " << y 
             << ") size=" << width << "x" << height << endl;
    }
    
    double getArea() const override {
        return width * height;
    }
};

// Leaf: Text
class TextElement : public GraphicElement {
private:
    string text;
    
public:
    TextElement(const string& n, double xPos, double yPos, const string& txt) 
        : GraphicElement(n, xPos, yPos), text(txt) {}
    
    void draw() const override {
        cout << "  Text '" << name << "' at (" << x << ", " << y 
             << ") content='" << text << "'" << endl;
    }
    
    double getArea() const override {
        return text.length() * 10; // Approximate area
    }
};

// Composite: Group
class GroupElement : public GraphicElement {
private:
    vector<unique_ptr<GraphicElement>> children;
    
public:
    GroupElement(const string& n, double xPos, double yPos) 
        : GraphicElement(n, xPos, yPos) {}
    
    void add(GraphicElement* g) override {
        children.emplace_back(g);
    }
    
    void remove(GraphicElement* g) override {
        auto it = find_if(children.begin(), children.end(),
            [g](const auto& c) { return c.get() == g; });
        if (it != children.end()) {
            children.erase(it);
        }
    }
    
    GraphicElement* getChild(int index) override {
        if (index >= 0 && index < children.size()) {
            return children[index].get();
        }
        return nullptr;
    }
    
    void draw() const override {
        cout << "Group '" << name << "' at (" << x << ", " << y << "):" << endl;
        for (const auto& child : children) {
            child->draw();
        }
    }
    
    void move(double dx, double dy) override {
        GraphicElement::move(dx, dy);
        for (auto& child : children) {
            child->move(dx, dy);
        }
    }
    
    double getArea() const override {
        double total = 0;
        for (const auto& child : children) {
            total += child->getArea();
        }
        return total;
    }
};

class Drawing {
private:
    vector<unique_ptr<GraphicElement>> elements;
    
public:
    void addElement(GraphicElement* elem) {
        elements.emplace_back(elem);
    }
    
    void drawAll() const {
        cout << "\n=== Drawing Contents ===" << endl;
        for (const auto& elem : elements) {
            elem->draw();
        }
    }
    
    double getTotalArea() const {
        double total = 0;
        for (const auto& elem : elements) {
            total += elem->getArea();
        }
        return total;
    }
};

int main() {
    cout << "=== Graphic Design Tool ===" << endl;
    
    Drawing drawing;
    
    // Create individual elements
    CircleElement* circle1 = new CircleElement("Sun", 100, 100, 50);
    RectangleElement* rect1 = new RectangleElement("Building", 200, 150, 80, 120);
    TextElement* text1 = new TextElement("Label", 50, 200, "Hello World");
    
    // Create a group for background elements
    GroupElement* background = new GroupElement("Background", 0, 0);
    CircleElement* sky = new CircleElement("Sky", 400, 300, 200);
    RectangleElement* ground = new RectangleElement("Ground", 0, 400, 800, 200);
    background->add(sky);
    background->add(ground);
    
    // Create a group for foreground elements
    GroupElement* foreground = new GroupElement("Foreground", 0, 0);
    foreground->add(circle1);
    foreground->add(rect1);
    foreground->add(text1);
    
    // Add all to drawing
    drawing.addElement(background);
    drawing.addElement(foreground);
    
    // Draw everything
    drawing.drawAll();
    
    cout << "\nTotal area: " << drawing.getTotalArea() << endl;
    
    // Move entire foreground group
    cout << "\nMoving foreground group..." << endl;
    foreground->move(50, 30);
    drawing.drawAll();
    
    delete background;
    delete foreground;
    
    return 0;
}
```

---

## 📊 Composite Pattern Summary

| Component | Description | Responsibilities |
|-----------|-------------|-----------------|
| **Component** | Abstract interface | Declares common operations |
| **Leaf** | Primitive object | Implements operations, has no children |
| **Composite** | Container object | Implements child management operations |

---

## ✅ Best Practices

1. **Use Composite** when you need tree structures
2. **Make Component interface** as simple as possible
3. **Provide default implementations** for child management (throw or do nothing)
4. **Consider using Flyweight** for shared leaf objects
5. **Implement caching** for expensive operations (like area calculation)

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Unclear component interface** | Some operations don't make sense for leaves | Provide default implementations |
| **Performance issues** | Deep tree traversal can be slow | Cache results when possible |
| **Memory management** | Complex ownership | Use smart pointers |

---

## ✅ Key Takeaways

1. **Composite pattern** creates tree structures
2. **Leaves and composites** are treated uniformly
3. **Recursive composition** enables complex hierarchies
4. **Useful for** file systems, UI components, organizational charts
5. **Follows** Open/Closed Principle
6. **Simplifies** client code by treating objects uniformly

---
---

## Next Step

- Go to [Decorator.md](Decorator.md) to continue with Decorator.
