# README.md

## Polymorphism in C++ - Complete Guide

### Overview

Polymorphism is one of the four fundamental pillars of Object-Oriented Programming. The term comes from Greek words "poly" (many) and "morph" (forms), meaning "many forms". Polymorphism allows objects of different classes to be treated as objects of a common base class, and the same function call can produce different behaviors depending on the actual type of the object.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Compile_Time_Polymorphism](01_Compile_Time_Polymorphism/README.md) | understand Compile-Time Polymorphism |
| 2. | [02_Run_Time_Polymorphism](02_Run_Time_Polymorphism/README.md) | understand Run-Time Polymorphism |
| 3. | [Theory.md](Theory.md) | understand Theoretical Foundations of Polymorphism |

---

## 1. Compile-Time Polymorphism

This topic explains polymorphism that is resolved during compilation. It includes function overloading and operator overloading.

**File:** [01_Compile_Time_Polymorphism/README.md](01_Compile_Time_Polymorphism/README.md)

**What you will learn:**
- Definition of compile-time polymorphism (static polymorphism)
- Function overloading - multiple functions with same name
- Operator overloading - defining behavior for operators
- How compiler resolves overloaded functions
- Benefits and limitations of compile-time polymorphism

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **Function Overloading** | Same function name, different parameters | `void print(int); void print(double);` |
| **Operator Overloading** | Defining behavior for operators | `Vector operator+(const Vector&);` |
| **Early Binding** | Function call resolved at compile time | Compiler knows which function to call |
| **Performance** | No runtime overhead | Faster than runtime polymorphism |

**Syntax - Function Overloading:**
```cpp
class Calculator {
public:
    int add(int a, int b) {
        return a + b;
    }
    
    double add(double a, double b) {
        return a + b;
    }
    
    int add(int a, int b, int c) {
        return a + b + c;
    }
};

// Usage
Calculator calc;
cout << calc.add(5, 10);        // Calls int version
cout << calc.add(5.5, 10.5);    // Calls double version
cout << calc.add(5, 10, 15);    // Calls three-parameter version
```

**Syntax - Operator Overloading:**
```cpp
class Complex {
private:
    double real, imag;
public:
    Complex(double r, double i) : real(r), imag(i) {}
    
    // Overload + operator
    Complex operator+(const Complex& other) {
        return Complex(real + other.real, imag + other.imag);
    }
    
    // Overload == operator
    bool operator==(const Complex& other) {
        return (real == other.real && imag == other.imag);
    }
};

// Usage
Complex c1(3, 4), c2(1, 2);
Complex c3 = c1 + c2;  // Calls operator+
```

---

## 2. Run-Time Polymorphism

This topic explains polymorphism that is resolved during program execution using virtual functions.

**File:** [02_Run_Time_Polymorphism/README.md](02_Run_Time_Polymorphism/README.md)

**What you will learn:**
- Definition of run-time polymorphism (dynamic polymorphism)
- Virtual functions and function overriding
- Virtual table (vtable) and virtual pointer (vptr)
- Pure virtual functions and abstract classes
- Late binding (dynamic dispatch)
- Benefits of run-time polymorphism

**Key Concepts:**

| Concept | Description | Example |
|---------|-------------|---------|
| **Virtual Function** | Function that can be overridden in derived class | `virtual void draw() { }` |
| **Function Overriding** | Derived class provides its own implementation | `void draw() override { }` |
| **Late Binding** | Function call resolved at runtime | Based on actual object type |
| **Abstract Class** | Class with at least one pure virtual function | `virtual void draw() = 0;` |
| **VTable** | Table of function pointers for virtual functions | Created by compiler |

**Syntax:**
```cpp
// Base class with virtual function
class Shape {
public:
    virtual void draw() {
        cout << "Drawing Shape" << endl;
    }
    
    virtual double getArea() = 0;  // Pure virtual function
    virtual ~Shape() { }           // Virtual destructor
};

// Derived class overriding virtual function
class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r) : radius(r) {}
    
    void draw() override {
        cout << "Drawing Circle" << endl;
    }
    
    double getArea() override {
        return 3.14159 * radius * radius;
    }
};

class Rectangle : public Shape {
private:
    double length, width;
public:
    Rectangle(double l, double w) : length(l), width(w) {}
    
    void draw() override {
        cout << "Drawing Rectangle" << endl;
    }
    
    double getArea() override {
        return length * width;
    }
};

// Polymorphic usage
int main() {
    Shape* shapes[2];
    shapes[0] = new Circle(5);
    shapes[1] = new Rectangle(4, 6);
    
    for (int i = 0; i < 2; i++) {
        shapes[i]->draw();      // Calls appropriate draw()
        cout << "Area: " << shapes[i]->getArea() << endl;
    }
    
    // Cleanup
    for (int i = 0; i < 2; i++) {
        delete shapes[i];
    }
}
```

---

### Compile-Time vs Run-Time Polymorphism

| Aspect | Compile-Time Polymorphism | Run-Time Polymorphism |
|--------|--------------------------|----------------------|
| **Also Known As** | Static polymorphism, Early binding | Dynamic polymorphism, Late binding |
| **Resolved At** | Compile time | Run time |
| **Achieved By** | Function overloading, Operator overloading | Virtual functions, Function overriding |
| **Speed** | Faster (no runtime overhead) | Slower (vtable lookup) |
| **Flexibility** | Less flexible | More flexible |
| **Memory** | No extra memory | VTable per class, VPtr per object |
| **Function Call** | Direct call | Indirect call via vtable |

---

## 3. Theoretical Foundations

This topic covers the theoretical concepts behind polymorphism.

**File:** [Theory.md](Theory.md)

**What you will learn:**
- Subtype polymorphism (inclusion polymorphism)
- Parametric polymorphism (templates)
- Ad-hoc polymorphism (overloading)
- Liskov Substitution Principle (LSP)
- Open/Closed Principle (OCP)
- Dynamic dispatch mechanism
- Virtual table implementation details

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Subtype Polymorphism** | Using derived class through base class pointer/reference |
| **Parametric Polymorphism** | Templates - same code works with different types |
| **Ad-hoc Polymorphism** | Overloading - same name, different implementations |
| **Co-variant Return Types** | Overriding function can return derived type |
| **Liskov Substitution** | Derived class must be substitutable for base class |

**Liskov Substitution Principle Example:**
```cpp
// Good - follows LSP
class Bird {
public:
    virtual void move() { cout << "Moving" << endl; }
};

class Sparrow : public Bird {
public:
    void move() override { cout << "Flying" << endl; }
};

class Penguin : public Bird {
public:
    void move() override { cout << "Swimming" << endl; }
};

// Bad - violates LSP
class Bird2 {
public:
    virtual void fly() { cout << "Flying" << endl; }
};

class Penguin2 : public Bird2 {
    void fly() override {
        // Penguins can't fly - violates LSP
        throw "Cannot fly";
    }
};
```

---

### Virtual Function Mechanism

**How Virtual Functions Work:**

```
1. Compiler creates a virtual table (vtable) for each class with virtual functions
2. Vtable contains pointers to actual function implementations
3. Each object gets a hidden virtual pointer (vptr) pointing to its class's vtable
4. When virtual function is called, program:
   a. Follows object's vptr to the vtable
   b. Looks up function address in vtable
   c. Calls the function through the pointer

Memory Layout:
    Object
    ┌─────────┐
    │  vptr   │ ──→ Class VTable
    ├─────────┤     ┌──────────────┐
    │  data   │     │ func1 ptr    │ ──→ actual func1
    └─────────┘     ├──────────────┤
                    │ func2 ptr    │ ──→ actual func2
                    └──────────────┘
```

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - Functions, pointers
- [02_Classes_and_Objects/README.md](../02_Classes_and_Objects/README.md) - Class basics
- [03_Constructors_and_Destructors/README.md](../03_Constructors_and_Destructors/README.md) - Object lifecycle
- [05_Inheritance/README.md](../05_Inheritance/README.md) - Inheritance concepts

---

### Sample Polymorphism Example

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Abstract base class
class MediaFile {
protected:
    string filename_;
    double size_;  // in MB
    
public:
    MediaFile(string name, double size) : filename_(name), size_(size) {}
    
    virtual ~MediaFile() { }
    
    // Pure virtual functions
    virtual void play() = 0;
    virtual void displayInfo() const = 0;
    
    // Common function (not virtual - not overridden)
    string getFilename() const { return filename_; }
};

class AudioFile : public MediaFile {
private:
    int bitrate_;  // kbps
    
public:
    AudioFile(string name, double size, int bitrate)
        : MediaFile(name, size), bitrate_(bitrate) {}
    
    void play() override {
        cout << "Playing audio: " << filename_ << " at " << bitrate_ << " kbps" << endl;
    }
    
    void displayInfo() const override {
        cout << "Audio: " << filename_ << " | Size: " << size_ << " MB | Bitrate: " << bitrate_ << endl;
    }
};

class VideoFile : public MediaFile {
private:
    int resolution_;  // 720, 1080, 2160
    int duration_;    // seconds
    
public:
    VideoFile(string name, double size, int resolution, int duration)
        : MediaFile(name, size), resolution_(resolution), duration_(duration) {}
    
    void play() override {
        cout << "Playing video: " << filename_ << " at " << resolution_ << "p" << endl;
    }
    
    void displayInfo() const override {
        cout << "Video: " << filename_ << " | Size: " << size_ << " MB | Resolution: " 
             << resolution_ << "p | Duration: " << duration_ << "s" << endl;
    }
};

class ImageFile : public MediaFile {
private:
    int width_, height_;
    
public:
    ImageFile(string name, double size, int width, int height)
        : MediaFile(name, size), width_(width), height_(height) {}
    
    void play() override {
        cout << "Displaying image: " << filename_ << " (" << width_ << "x" << height_ << ")" << endl;
    }
    
    void displayInfo() const override {
        cout << "Image: " << filename_ << " | Size: " << size_ << " MB | Dimensions: " 
             << width_ << "x" << height_ << endl;
    }
};

// Function demonstrating polymorphism
void processMedia(MediaFile* media) {
    media->play();
    media->displayInfo();
    cout << "---" << endl;
}

int main() {
    // Polymorphic container
    vector<MediaFile*> library;
    
    library.push_back(new AudioFile("song.mp3", 4.5, 320));
    library.push_back(new VideoFile("movie.mp4", 850.0, 1080, 5400));
    library.push_back(new ImageFile("photo.jpg", 2.3, 1920, 1080));
    
    cout << "=== Media Library ===" << endl;
    
    for (MediaFile* media : library) {
        processMedia(media);
    }
    
    // Cleanup
    for (MediaFile* media : library) {
        delete media;
    }
    
    return 0;
}
```

---

### Learning Path

```
Level 1: Compile-Time Polymorphism
├── Function Overloading
├── Operator Overloading
└── Default Arguments

Level 2: Run-Time Polymorphism Basics
├── Virtual Functions
├── Function Overriding
└── Base Class Pointers/References

Level 3: Advanced Run-Time Polymorphism
├── Pure Virtual Functions
├── Abstract Classes
├── Virtual Destructors
└── Virtual Table Mechanism

Level 4: Design with Polymorphism
├── Liskov Substitution Principle
├── Open/Closed Principle
├── Interface Segregation
└── Template Method Pattern
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Forgetting `virtual` keyword in base class | Mark functions as `virtual` if intended to override |
| Not using `override` specifier | Use `override` to catch signature mismatches |
| Non-virtual destructor in base class | Always make base destructor virtual |
| Slicing objects | Use pointers or references, not pass by value |
| Calling virtual function in constructor/destructor | Avoid - doesn't work as expected |
| Confusing overloading with overriding | Overloading = same name, different parameters; Overriding = same signature, different class |

---

### Practice Questions

After completing this section, you should be able to:

1. Define polymorphism and explain its two types
2. Differentiate between compile-time and run-time polymorphism
3. Implement function overloading with different parameter types
4. Implement operator overloading for a custom class
5. Create a class hierarchy with virtual functions
6. Explain the vtable and vptr mechanism
7. Create an abstract class with pure virtual functions
8. Apply the Liskov Substitution Principle in class design

---

## Next Steps

- Visit [Theory.md](Theory.md) to learn about the theoretical foundations of Polymorphism.