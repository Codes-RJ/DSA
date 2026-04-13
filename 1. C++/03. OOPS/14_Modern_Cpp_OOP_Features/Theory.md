# Modern C++ OOP Features - Complete Guide

## 📖 Overview

Modern C++ (C++11 and later) introduced numerous features that enhance Object-Oriented Programming. These features improve type safety, performance, code clarity, and maintainability. Understanding modern C++ features is essential for writing efficient and elegant object-oriented code.

---

## 🎯 Key Modern C++ Features

| Feature | Version | Description |
|---------|---------|-------------|
| **auto** | C++11 | Type inference |
| **decltype** | C++11 | Declare type of expression |
| **Range-based for** | C++11 | Simplified iteration |
| **Lambda Expressions** | C++11 | Anonymous functions |
| **Smart Pointers** | C++11 | Automatic memory management |
| **Move Semantics** | C++11 | Efficient resource transfer |
| **Initializer Lists** | C++11 | Uniform initialization |
| **Delegating Constructors** | C++11 | Constructor chaining |
| **Inheriting Constructors** | C++11 | Inherit base constructors |
| **override/final** | C++11 | Virtual function control |
| **Concepts** | C++20 | Template constraints |

---

## 1. **auto and decltype (Type Inference)**

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;

class Widget {
public:
    static auto create() {
        return Widget();
    }
    
    void process() {
        cout << "Widget processing" << endl;
    }
};

auto add(int a, int b) -> int {  // Trailing return type
    return a + b;
}

template<typename T, typename U>
auto multiply(T a, U b) -> decltype(a * b) {
    return a * b;
}

int main() {
    cout << "=== auto and decltype ===" << endl;
    
    // Basic auto usage
    auto i = 42;           // int
    auto d = 3.14;         // double
    auto s = "Hello";      // const char*
    auto v = vector<int>{1, 2, 3};
    
    // auto with iterators
    map<string, int> scores = {{"Alice", 95}, {"Bob", 87}};
    for (auto it = scores.begin(); it != scores.end(); ++it) {
        cout << it->first << ": " << it->second << endl;
    }
    
    // Range-based for with auto
    for (const auto& [name, score] : scores) {
        cout << name << ": " << score << endl;
    }
    
    // decltype example
    int x = 10;
    decltype(x) y = 20;  // y is int
    decltype((x)) z = x; // z is int& (reference)
    
    // auto with functions
    auto result = add(5, 3);
    cout << "add(5, 3) = " << result << endl;
    
    auto product = multiply(5, 3.14);
    cout << "multiply(5, 3.14) = " << product << endl;
    
    // auto with factory method
    auto widget = Widget::create();
    widget.process();
    
    return 0;
}
```

---

## 2. **Range-Based For Loops**

```cpp
#include <iostream>
#include <vector>
#include <array>
#include <string>
#include <map>
using namespace std;

class Collection {
private:
    vector<int> data_ = {1, 2, 3, 4, 5};
    
public:
    auto begin() { return data_.begin(); }
    auto end() { return data_.end(); }
    auto begin() const { return data_.begin(); }
    auto end() const { return data_.end(); }
};

int main() {
    cout << "=== Range-Based For Loops ===" << endl;
    
    // Basic array
    int arr[] = {1, 2, 3, 4, 5};
    cout << "Array: ";
    for (int x : arr) {
        cout << x << " ";
    }
    cout << endl;
    
    // Vector
    vector<string> words = {"Hello", "World", "C++"};
    cout << "Vector: ";
    for (const auto& word : words) {
        cout << word << " ";
    }
    cout << endl;
    
    // Modifying elements
    vector<int> numbers = {1, 2, 3, 4, 5};
    for (auto& n : numbers) {
        n *= 2;
    }
    cout << "Doubled: ";
    for (int n : numbers) {
        cout << n << " ";
    }
    cout << endl;
    
    // Map with structured bindings (C++17)
    map<string, int> scores = {{"Alice", 95}, {"Bob", 87}, {"Charlie", 92}};
    cout << "Scores:" << endl;
    for (const auto& [name, score] : scores) {
        cout << "  " << name << ": " << score << endl;
    }
    
    // Custom container
    Collection col;
    cout << "Custom collection: ";
    for (int x : col) {
        cout << x << " ";
    }
    cout << endl;
    
    return 0;
}
```

---

## 3. **Lambda Expressions**

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <memory>
using namespace std;

class Processor {
private:
    int multiplier_ = 2;
    
public:
    void process(vector<int>& data) {
        // Lambda capturing this
        for_each(data.begin(), data.end(), [this](int& x) {
            x *= multiplier_;
        });
    }
    
    auto getMultiplier() const { return multiplier_; }
};

int main() {
    cout << "=== Lambda Expressions ===" << endl;
    
    // Basic lambda
    auto add = [](int a, int b) { return a + b; };
    cout << "add(5, 3) = " << add(5, 3) << endl;
    
    // Lambda with capture
    int factor = 2;
    auto multiply = [factor](int x) { return x * factor; };
    cout << "multiply(5) = " << multiply(5) << endl;
    
    // Mutable lambda
    int counter = 0;
    auto increment = [counter]() mutable {
        return ++counter;
    };
    cout << "Counter: " << increment() << ", " << increment() << endl;
    
    // Lambda with STL algorithms
    vector<int> numbers = {1, 2, 3, 4, 5};
    
    // Transform
    vector<int> squares(numbers.size());
    transform(numbers.begin(), numbers.end(), squares.begin(), 
              [](int x) { return x * x; });
    cout << "Squares: ";
    for (int x : squares) cout << x << " ";
    cout << endl;
    
    // Filter
    auto it = remove_if(numbers.begin(), numbers.end(), 
                        [](int x) { return x % 2 == 0; });
    numbers.erase(it, numbers.end());
    cout << "Odd numbers: ";
    for (int x : numbers) cout << x << " ";
    cout << endl;
    
    // Lambda capturing this
    Processor proc;
    vector<int> data = {1, 2, 3, 4, 5};
    proc.process(data);
    cout << "Processed data: ";
    for (int x : data) cout << x << " ";
    cout << endl;
    
    // Generic lambda (C++14)
    auto generic_add = [](auto a, auto b) { return a + b; };
    cout << "generic_add(5, 3) = " << generic_add(5, 3) << endl;
    cout << "generic_add(3.14, 2.71) = " << generic_add(3.14, 2.71) << endl;
    
    // Lambda as function object
    function<int(int, int)> func = [](int a, int b) { return a + b; };
    cout << "function: " << func(10, 20) << endl;
    
    return 0;
}
```

---

## 4. **Smart Pointers**

```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <string>
using namespace std;

class Resource {
private:
    string name_;
    static int count_;
    
public:
    Resource(string name) : name_(name) {
        count_++;
        cout << "Resource '" << name_ << "' created (total: " << count_ << ")" << endl;
    }
    
    ~Resource() {
        count_--;
        cout << "Resource '" << name_ << "' destroyed (remaining: " << count_ << ")" << endl;
    }
    
    void use() const {
        cout << "Using resource: " << name_ << endl;
    }
    
    string getName() const { return name_; }
};

int Resource::count_ = 0;

// unique_ptr - exclusive ownership
void uniquePtrExample() {
    cout << "\n--- unique_ptr ---" << endl;
    
    unique_ptr<Resource> u1 = make_unique<Resource>("Unique1");
    unique_ptr<Resource> u2 = make_unique<Resource>("Unique2");
    
    u1->use();
    
    // Transfer ownership
    unique_ptr<Resource> u3 = move(u1);
    if (!u1) cout << "u1 is now empty" << endl;
    u3->use();
}

// shared_ptr - shared ownership
void sharedPtrExample() {
    cout << "\n--- shared_ptr ---" << endl;
    
    shared_ptr<Resource> s1 = make_shared<Resource>("Shared1");
    {
        shared_ptr<Resource> s2 = s1;  // Reference count: 2
        shared_ptr<Resource> s3 = s2;  // Reference count: 3
        cout << "Reference count: " << s1.use_count() << endl;
        s2->use();
    }  // s2 and s3 destroyed, count becomes 1
    cout << "Reference count: " << s1.use_count() << endl;
}

// weak_ptr - non-owning observer
void weakPtrExample() {
    cout << "\n--- weak_ptr ---" << endl;
    
    shared_ptr<Resource> s = make_shared<Resource>("Shared");
    weak_ptr<Resource> w = s;
    
    cout << "Reference count: " << s.use_count() << endl;
    
    if (auto locked = w.lock()) {
        locked->use();
        cout << "Weak pointer valid" << endl;
    }
    
    s.reset();  // Destroy the object
    
    if (auto locked = w.lock()) {
        locked->use();
    } else {
        cout << "Weak pointer expired" << endl;
    }
}

// Custom deleter
void customDeleterExample() {
    cout << "\n--- Custom Deleter ---" << endl;
    
    auto deleter = [](Resource* r) {
        cout << "Custom deleting: " << r->getName() << endl;
        delete r;
    };
    
    unique_ptr<Resource, decltype(deleter)> u(new Resource("Custom"), deleter);
    u->use();
}

int main() {
    cout << "=== Smart Pointers ===" << endl;
    
    uniquePtrExample();
    sharedPtrExample();
    weakPtrExample();
    customDeleterExample();
    
    cout << "\nAll resources automatically managed!" << endl;
    
    return 0;
}
```

---

## 5. **Move Semantics**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <chrono>
using namespace std;

class StringBuffer {
private:
    char* data_;
    size_t size_;
    
public:
    // Constructor
    StringBuffer(const char* str = "") {
        size_ = strlen(str);
        data_ = new char[size_ + 1];
        strcpy(data_, str);
        cout << "Constructed: " << data_ << endl;
    }
    
    // Copy constructor (expensive)
    StringBuffer(const StringBuffer& other) {
        size_ = other.size_;
        data_ = new char[size_ + 1];
        strcpy(data_, other.data_);
        cout << "Copied: " << data_ << endl;
    }
    
    // Move constructor (efficient)
    StringBuffer(StringBuffer&& other) noexcept
        : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr;
        other.size_ = 0;
        cout << "Moved: " << data_ << endl;
    }
    
    // Copy assignment
    StringBuffer& operator=(const StringBuffer& other) {
        if (this != &other) {
            delete[] data_;
            size_ = other.size_;
            data_ = new char[size_ + 1];
            strcpy(data_, other.data_);
            cout << "Copy assigned: " << data_ << endl;
        }
        return *this;
    }
    
    // Move assignment
    StringBuffer& operator=(StringBuffer&& other) noexcept {
        if (this != &other) {
            delete[] data_;
            data_ = other.data_;
            size_ = other.size_;
            other.data_ = nullptr;
            other.size_ = 0;
            cout << "Move assigned: " << data_ << endl;
        }
        return *this;
    }
    
    ~StringBuffer() {
        if (data_) {
            cout << "Destroyed: " << data_ << endl;
            delete[] data_;
        }
    }
    
    void display() const {
        if (data_) cout << "String: " << data_ << endl;
        else cout << "String: (empty)" << endl;
    }
};

StringBuffer createBuffer() {
    StringBuffer temp("Temporary");
    return temp;  // Move or RVO
}

int main() {
    cout << "=== Move Semantics ===" << endl;
    
    cout << "\n1. Copy vs Move:" << endl;
    StringBuffer s1("Hello");
    StringBuffer s2 = s1;           // Copy
    StringBuffer s3 = move(s1);     // Move
    cout << "s1 after move: ";
    s1.display();
    cout << "s2: ";
    s2.display();
    cout << "s3: ";
    s3.display();
    
    cout << "\n2. Returning from function:" << endl;
    StringBuffer s4 = createBuffer();  // Move or RVO
    s4.display();
    
    cout << "\n3. Move with vector:" << endl;
    vector<StringBuffer> vec;
    vec.push_back(StringBuffer("First"));   // Move
    vec.push_back(StringBuffer("Second"));  // Move
    vec.push_back(StringBuffer("Third"));   // Move
    
    return 0;
}
```

---

## 6. **override and final Specifiers**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <vector>
using namespace std;

// Base class
class Shape {
public:
    virtual void draw() const {
        cout << "Drawing shape" << endl;
    }
    
    virtual double area() const = 0;
    
    virtual void scale(double factor) {
        cout << "Scaling shape" << endl;
    }
    
    virtual ~Shape() = default;
};

// override ensures correct overriding
class Circle : public Shape {
private:
    double radius_;
    
public:
    Circle(double r) : radius_(r) {}
    
    void draw() const override {
        cout << "Drawing circle with radius " << radius_ << endl;
    }
    
    double area() const override {
        return 3.14159 * radius_ * radius_;
    }
    
    // final prevents further overriding
    void scale(double factor) override final {
        radius_ *= factor;
        cout << "Circle scaled to radius " << radius_ << endl;
    }
};

// Cannot override final function
class BigCircle : public Circle {
public:
    BigCircle(double r) : Circle(r) {}
    
    // void scale(double factor) override { }  // Error! final function
    
    void draw() const override {
        cout << "Drawing big circle" << endl;
    }
};

// final class - cannot be inherited
class FinalShape final : public Shape {
public:
    double area() const override { return 0; }
    void draw() const override { cout << "Drawing final shape" << endl; }
};

// class InvalidShape : public FinalShape { };  // Error! FinalShape is final

int main() {
    cout << "=== override and final Specifiers ===" << endl;
    
    Circle circle(5.0);
    BigCircle bigCircle(10.0);
    
    cout << "\n1. Virtual function calls:" << endl;
    circle.draw();
    circle.scale(2.0);
    
    cout << "\n2. Polymorphic container:" << endl;
    vector<unique_ptr<Shape>> shapes;
    shapes.push_back(make_unique<Circle>(3.0));
    shapes.push_back(make_unique<BigCircle>(7.0));
    
    for (const auto& shape : shapes) {
        shape->draw();
        cout << "Area: " << shape->area() << endl;
    }
    
    cout << "\n3. final class:" << endl;
    FinalShape fs;
    fs.draw();
    
    return 0;
}
```

---

## 📊 Modern C++ Features Summary

| Feature | Purpose | Best Practice |
|---------|---------|---------------|
| **auto** | Type deduction | Use for complex types, avoid for simple types |
| **decltype** | Expression type | Use in templates and trailing returns |
| **Range-for** | Simplified iteration | Use for all container iteration |
| **Lambda** | Anonymous functions | Capture by value for small data, by reference for large |
| **Smart Pointers** | Automatic memory | unique_ptr for exclusive, shared_ptr for shared |
| **Move Semantics** | Efficient transfer | Use for large objects, implement move operations |
| **override** | Virtual override safety | Always use when overriding virtual functions |
| **final** | Prevent overriding | Use for leaf classes and final overrides |

---

## ✅ Key Takeaways

1. **auto** simplifies code but use judiciously
2. **Range-based for** makes iteration cleaner
3. **Lambdas** enable functional programming patterns
4. **Smart pointers** eliminate manual memory management
5. **Move semantics** dramatically improve performance
6. **override** prevents subtle bugs in inheritance
7. **final** documents design intent
8. **Modern C++** is safer and more expressive

---
---

## Next Step

- Go to [README.md](README.md) to continue.
