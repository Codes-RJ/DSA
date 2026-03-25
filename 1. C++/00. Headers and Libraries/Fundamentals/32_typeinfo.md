# typeinfo - Runtime Type Information (RTTI)

The `typeinfo` header provides access to runtime type metadata through the `typeid` operator and the `std::type_info` class, allowing programs to query the actual type of an object at runtime.

## 📖 Overview

C++ is a statically-typed language, but with polymorphism, the *dynamic* (runtime) type of an object can differ from its *static* (compile-time) type. RTTI gives you a safe, standardised way to inspect that dynamic type.

Two mechanisms together form RTTI:
- **`typeid`** — returns a `std::type_info` reference describing the type
- **`dynamic_cast`** — safely downcasts through a polymorphic hierarchy (from `<typeinfo>` implicitly)

> **Note:** RTTI applies to *polymorphic types* (classes with at least one `virtual` function). For non-polymorphic types, `typeid` returns the static type only.

## 🎯 Key Components

### `std::type_info`
A class that holds metadata about a type. You cannot construct it directly — you get references from `typeid`.

| Member | Description |
|--------|-------------|
| `name()` | Returns an implementation-defined name string |
| `operator==` | True if two `type_info` objects describe the same type |
| `operator!=` | True if types differ |
| `hash_code()` | Returns a hash suitable for use in `unordered_map` (C++11) |
| `before(other)` | Ordering (for use in sorted containers) |

### `typeid` Operator
```cpp
typeid(expression)  // returns std::type_info const&
typeid(TypeName)    // also accepts a type directly
```

### `dynamic_cast`
```cpp
dynamic_cast<Derived*>(base_ptr)  // returns nullptr if cast fails
dynamic_cast<Derived&>(base_ref)  // throws std::bad_cast if cast fails
```

## 🔧 Basic Operations

### Querying the Type of a Variable
```cpp
#include <typeinfo>
#include <iostream>

int main() {
    int    i = 42;
    double d = 3.14;
    float  f = 1.0f;

    std::cout << typeid(i).name() << "\n"; // int (or 'i' on GCC)
    std::cout << typeid(d).name() << "\n"; // double (or 'd')
    std::cout << typeid(f).name() << "\n"; // float (or 'f')

    // Compare types
    if (typeid(i) == typeid(int)) {
        std::cout << "i is an int\n";
    }

    return 0;
}
```

### RTTI with Polymorphic Types
```cpp
#include <typeinfo>
#include <iostream>

class Animal {
public:
    virtual ~Animal() = default;  // virtual destructor enables RTTI
    virtual void speak() const = 0;
};

class Dog : public Animal {
public:
    void speak() const override { std::cout << "Woof!\n"; }
};

class Cat : public Animal {
public:
    void speak() const override { std::cout << "Meow!\n"; }
};

int main() {
    Animal* a1 = new Dog();
    Animal* a2 = new Cat();

    // typeid on pointer gives STATIC type (Animal)
    std::cout << typeid(a1).name() << "\n"; // pointer to Animal

    // typeid on DEREFERENCED pointer gives DYNAMIC type
    std::cout << typeid(*a1).name() << "\n"; // Dog
    std::cout << typeid(*a2).name() << "\n"; // Cat

    // Compare at runtime
    if (typeid(*a1) == typeid(Dog)) {
        std::cout << "a1 is a Dog\n";
    }

    delete a1;
    delete a2;
    return 0;
}
```

### `dynamic_cast` — Safe Downcast
```cpp
#include <typeinfo>
#include <iostream>

class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
};

class Circle : public Shape {
public:
    double radius;
    Circle(double r) : radius(r) {}
    double area() const override { return 3.14159 * radius * radius; }
};

class Rectangle : public Shape {
public:
    double w, h;
    Rectangle(double w, double h) : w(w), h(h) {}
    double area() const override { return w * h; }
};

void process(Shape* s) {
    if (Circle* c = dynamic_cast<Circle*>(s)) {
        std::cout << "Circle with radius " << c->radius << "\n";
    } else if (Rectangle* r = dynamic_cast<Rectangle*>(s)) {
        std::cout << "Rectangle " << r->w << "x" << r->h << "\n";
    } else {
        std::cout << "Unknown shape\n";
    }
}

int main() {
    Shape* s1 = new Circle(5.0);
    Shape* s2 = new Rectangle(3.0, 4.0);

    process(s1);
    process(s2);

    delete s1;
    delete s2;
    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Type Dispatcher
```cpp
#include <typeinfo>
#include <iostream>
#include <vector>
#include <memory>

class Event { public: virtual ~Event() = default; };
class ClickEvent  : public Event { public: int x, y; ClickEvent(int x, int y): x(x), y(y) {} };
class KeyEvent    : public Event { public: char key;  KeyEvent(char k): key(k) {} };
class ResizeEvent : public Event { public: int w, h;  ResizeEvent(int w, int h): w(w), h(h) {} };

void dispatch(const Event& e) {
    if (const auto* c = dynamic_cast<const ClickEvent*>(&e))
        std::cout << "Click at (" << c->x << ", " << c->y << ")\n";
    else if (const auto* k = dynamic_cast<const KeyEvent*>(&e))
        std::cout << "Key pressed: '" << k->key << "'\n";
    else if (const auto* r = dynamic_cast<const ResizeEvent*>(&e))
        std::cout << "Resized to " << r->w << "x" << r->h << "\n";
    else
        std::cout << "Unknown event\n";
}

int main() {
    std::vector<std::unique_ptr<Event>> events;
    events.push_back(std::make_unique<ClickEvent>(100, 200));
    events.push_back(std::make_unique<KeyEvent>('Q'));
    events.push_back(std::make_unique<ResizeEvent>(1920, 1080));

    for (const auto& e : events)
        dispatch(*e);

    return 0;
}
```

### Example 2: Type Name Registry
```cpp
#include <typeinfo>
#include <iostream>
#include <unordered_map>
#include <string>
#include <typeindex>  // std::type_index — hashable wrapper for type_info

class TypeRegistry {
    std::unordered_map<std::type_index, std::string> names_;

public:
    template <typename T>
    void registerType(const std::string& name) {
        names_[std::type_index(typeid(T))] = name;
    }

    template <typename T>
    std::string lookup(const T& obj) const {
        auto it = names_.find(std::type_index(typeid(obj)));
        return it != names_.end() ? it->second : typeid(obj).name();
    }
};

struct Dog {};
struct Cat {};
struct Bird {};

int main() {
    TypeRegistry reg;
    reg.registerType<Dog>("Domestic Dog");
    reg.registerType<Cat>("House Cat");

    Dog d; Cat c; Bird b;
    std::cout << reg.lookup(d) << "\n"; // Domestic Dog
    std::cout << reg.lookup(c) << "\n"; // House Cat
    std::cout << reg.lookup(b) << "\n"; // fallback: mangled name

    return 0;
}
```

### Example 3: Catching `std::bad_cast`
```cpp
#include <typeinfo>
#include <iostream>

class Base { public: virtual ~Base() = default; };
class Derived : public Base {};

int main() {
    Base b;

    try {
        // dynamic_cast on a reference throws bad_cast on failure
        Derived& d = dynamic_cast<Derived&>(b);
        std::cout << "Cast succeeded\n";
    } catch (const std::bad_cast& e) {
        std::cerr << "bad_cast: " << e.what() << "\n";
    }

    return 0;
}
```

### Example 4: Using `type_index` in a Map
```cpp
#include <typeinfo>
#include <typeindex>
#include <iostream>
#include <unordered_map>
#include <functional>

class Handler {
    std::unordered_map<std::type_index, std::function<void()>> handlers_;

public:
    template <typename T>
    void on(std::function<void()> fn) {
        handlers_[std::type_index(typeid(T))] = fn;
    }

    template <typename T>
    void trigger() {
        auto it = handlers_.find(std::type_index(typeid(T)));
        if (it != handlers_.end()) it->second();
        else std::cout << "No handler for " << typeid(T).name() << "\n";
    }
};

struct StartEvent {};
struct StopEvent {};

int main() {
    Handler h;
    h.on<StartEvent>([]{ std::cout << "Application started!\n"; });
    h.on<StopEvent> ([]{ std::cout << "Application stopped!\n"; });

    h.trigger<StartEvent>();
    h.trigger<StopEvent>();

    return 0;
}
```

## ⚡ Performance Tips

### `dynamic_cast` Has a Runtime Cost
```cpp
// Prefer virtual dispatch (design with polymorphism) over dynamic_cast in hot paths
// dynamic_cast traverses the class hierarchy — O(depth) for deep hierarchies

// Fast: virtual function (vtable lookup = constant time)
shape->area();

// Slower: dynamic_cast checks hierarchy at runtime
if (Circle* c = dynamic_cast<Circle*>(shape)) { ... }
```

### Use `std::type_index` for Containers
```cpp
// type_info cannot be copied or used as a map key directly
// Use std::type_index — a copyable, hashable wrapper
#include <typeindex>
std::unordered_map<std::type_index, int> typeCounters;
typeCounters[std::type_index(typeid(int))]++;
```

## 🐛 Common Pitfalls & Solutions

### 1. `typeid` on a Non-Polymorphic Type Gives Static Type
```cpp
struct Plain {}; // no virtual functions
struct Child : Plain {};

Plain* p = new Child();
// typeid(*p) gives Plain, NOT Child — no RTTI without virtual
std::cout << typeid(*p).name() << "\n"; // "Plain"
```

### 2. `typeid` on a Null Pointer Throws `std::bad_typeid`
```cpp
Animal* a = nullptr;
try {
    std::cout << typeid(*a).name(); // throws bad_typeid
} catch (const std::bad_typeid& e) {
    std::cerr << e.what() << "\n";
}
```

### 3. `name()` Returns Implementation-Defined Mangled Names
```cpp
std::cout << typeid(int).name(); // "i" on GCC, "int" on MSVC
// Use a demangler or maintain your own name registry for readable names
```

### 4. Overusing `dynamic_cast` (Design Smell)
```cpp
// If you find yourself casting frequently, refactor to use virtual functions
// Prefer polymorphic dispatch over tangled if/else dynamic_cast chains
```

## 🎯 Best Practices

1. **Add `virtual` destructors** to base classes to enable RTTI
2. **Prefer virtual dispatch** over `dynamic_cast` for performance-critical code
3. **Use `dynamic_cast` on pointers** to get a null check rather than an exception
4. **Use `std::type_index`** when you need type as a map key
5. **Don't rely on `name()`** for stable, human-readable output across compilers
6. **Treat heavy use of `dynamic_cast` as a design smell** — refactor with the Visitor pattern instead

## 📚 Related Headers

- [`exception.md`](31_exception.md) — `std::bad_cast`, `std::bad_typeid`
- [`type_traits.md`](33_type_traits.md) — Compile-time type inspection (prefer over RTTI when possible)
- [`memory.md`](22_memory.md) — Smart pointers that pair with polymorphic hierarchies

## 🚀 Next Steps

1. Experiment with `typeid` on your own class hierarchy and observe name mangling
2. Rewrite a `dynamic_cast`-heavy code path using the Visitor design pattern
3. Build a simple factory that uses `std::type_index` to map types to creator functions
4. Learn about `std::any` (C++17) — a type-erased container that uses RTTI internally

---

**Examples in this file**: 4 complete programs  
**Key Types**: `std::type_info`, `std::type_index`, `std::bad_cast`, `std::bad_typeid`  
**Key Operators**: `typeid`, `dynamic_cast`  
**Common Use Cases**: Event dispatching, type registries, safe downcasting, plugin systems
