# Visitor Pattern in C++

> **Minimum standard:** C++17
>
> **Canonical location:** Behavioral design patterns.

## Visitor — Operations on an Object Hierarchy
```cpp
#include <iostream>
#include <vector>
#include <memory>
#include <string>

// Forward declarations
class Circle; class Rectangle; class Triangle;

class ShapeVisitor {
public:
    virtual ~ShapeVisitor() = default;
    virtual void visit(const Circle&)    = 0;
    virtual void visit(const Rectangle&) = 0;
    virtual void visit(const Triangle&)  = 0;
};

class Shape {
public:
    virtual ~Shape() = default;
    virtual void accept(ShapeVisitor& v) const = 0;
};

class Circle : public Shape {
public:
    double radius;
    Circle(double r) : radius(r) {}
    void accept(ShapeVisitor& v) const override { v.visit(*this); }
};

class Rectangle : public Shape {
public:
    double w, h;
    Rectangle(double w, double h) : w(w), h(h) {}
    void accept(ShapeVisitor& v) const override { v.visit(*this); }
};

class Triangle : public Shape {
public:
    double base, height;
    Triangle(double b, double h) : base(b), height(h) {}
    void accept(ShapeVisitor& v) const override { v.visit(*this); }
};

// Area computing visitor
class AreaVisitor : public ShapeVisitor {
public:
    double total = 0;
    void visit(const Circle& c)    override { total += 3.14159 * c.radius * c.radius; }
    void visit(const Rectangle& r) override { total += r.w * r.h; }
    void visit(const Triangle& t)  override { total += 0.5 * t.base * t.height; }
};

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>(5));
    shapes.push_back(std::make_unique<Rectangle>(4, 6));
    shapes.push_back(std::make_unique<Triangle>(3, 8));

    AreaVisitor areaCalc;
    for (const auto& s : shapes) s->accept(areaCalc);
    std::cout << "Total area: " << areaCalc.total << "\n";
    return 0;
}
```

## Next Step

Return to the parent section README and continue along the canonical [C++ and DSA learning path](../../../LEARNING_PATH.md).

