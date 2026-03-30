# Copy Constructor in C++ - Complete Guide

## 📖 Overview

A copy constructor is a special constructor that creates a new object as a copy of an existing object. It defines how objects of a class are copied, which is crucial for proper resource management. Understanding copy constructors is essential for preventing shallow copy issues and implementing deep copy when needed.

---

## 🎯 Key Concepts

| Aspect | Description |
|--------|-------------|
| **Purpose** | Create a new object as a copy of an existing object |
| **Syntax** | `ClassName(const ClassName& other);` |
| **When Called** | Passing by value, returning by value, explicit copy |
| **Default** | Compiler generates shallow copy if not provided |
| **Deep Copy** | Required for classes managing dynamic memory |

---

## 1. **When Copy Constructor is Called**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Demo {
private:
    string name;
    int value;
    
public:
    // Constructor
    Demo(string n, int v) : name(n), value(v) {
        cout << "Constructor: " << name << endl;
    }
    
    // Copy constructor
    Demo(const Demo& other) : name(other.name + "_copy"), value(other.value) {
        cout << "Copy constructor: copying " << other.name << " to " << name << endl;
    }
    
    // Destructor
    ~Demo() {
        cout << "Destructor: " << name << endl;
    }
    
    void display() const {
        cout << name << ": " << value << endl;
    }
};

// Function that takes parameter by value (triggers copy)
void functionByValue(Demo d) {
    cout << "Inside functionByValue" << endl;
    d.display();
}

// Function that returns by value (triggers copy)
Demo functionByReturn() {
    Demo temp("Temporary", 999);
    return temp;  // Copy constructor may be called (or RVO)
}

int main() {
    cout << "=== Copy Constructor Call Scenarios ===" << endl;
    
    cout << "\n1. Direct initialization:" << endl;
    Demo d1("Original", 100);
    Demo d2 = d1;  // Copy constructor
    
    cout << "\n2. Passing by value to function:" << endl;
    functionByValue(d1);
    
    cout << "\n3. Returning by value from function:" << endl;
    Demo d3 = functionByReturn();
    
    cout << "\n4. Explicit copy:" << endl;
    Demo d4(d1);  // Explicit copy constructor call
    
    cout << "\n--- End of main ---" << endl;
    return 0;
}
```

**Output:**
```
=== Copy Constructor Call Scenarios ===

1. Direct initialization:
Constructor: Original
Copy constructor: copying Original to Original_copy

2. Passing by value to function:
Copy constructor: copying Original to Original_copy
Inside functionByValue
Original_copy: 100
Destructor: Original_copy

3. Returning by value from function:
Constructor: Temporary
Destructor: Temporary

4. Explicit copy:
Copy constructor: copying Original to Original_copy

--- End of main ---
Destructor: Original_copy
Destructor: Original_copy
Destructor: Original
Destructor: Original_copy
```

---

## 2. **Shallow Copy vs Deep Copy**

### Shallow Copy (Default)
Copies only the pointer, not the pointed data. Dangerous for classes managing dynamic memory.

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class ShallowString {
private:
    char* data;
    
public:
    // Constructor
    ShallowString(const char* str) {
        data = new char[strlen(str) + 1];
        strcpy(data, str);
        cout << "Created: " << data << endl;
    }
    
    // Default copy constructor (shallow) - DANGEROUS!
    // ShallowString(const ShallowString& other) = default;
    
    // Destructor
    ~ShallowString() {
        cout << "Destroying: " << (data ? data : "null") << endl;
        delete[] data;
    }
    
    void setChar(size_t index, char c) {
        if (index < strlen(data)) {
            data[index] = c;
        }
    }
    
    void display() const {
        cout << "Data: " << (data ? data : "null") << endl;
    }
};

class DeepString {
private:
    char* data;
    
public:
    // Constructor
    DeepString(const char* str) {
        data = new char[strlen(str) + 1];
        strcpy(data, str);
        cout << "Created: " << data << endl;
    }
    
    // Deep copy constructor - PROPER
    DeepString(const DeepString& other) {
        data = new char[strlen(other.data) + 1];
        strcpy(data, other.data);
        cout << "Deep copy: " << data << endl;
    }
    
    // Destructor
    ~DeepString() {
        cout << "Destroying: " << (data ? data : "null") << endl;
        delete[] data;
    }
    
    void setChar(size_t index, char c) {
        if (index < strlen(data)) {
            data[index] = c;
        }
    }
    
    void display() const {
        cout << "Data: " << (data ? data : "null") << endl;
    }
};

int main() {
    cout << "=== Shallow Copy vs Deep Copy ===" << endl;
    
    cout << "\n1. Shallow Copy (DANGEROUS):" << endl;
    ShallowString s1("Hello");
    ShallowString s2 = s1;  // Shallow copy - both point to same memory!
    
    cout << "Original: ";
    s1.display();
    cout << "Copy: ";
    s2.display();
    
    cout << "\nModifying original..." << endl;
    s1.setChar(0, 'J');
    cout << "Original after modification: ";
    s1.display();
    cout << "Copy after modification: ";
    s2.display();  // Copy also changed! (shared memory)
    
    cout << "\n2. Deep Copy (CORRECT):" << endl;
    DeepString d1("World");
    DeepString d2 = d1;  // Deep copy - separate memory
    
    cout << "Original: ";
    d1.display();
    cout << "Copy: ";
    d2.display();
    
    cout << "\nModifying original..." << endl;
    d1.setChar(0, 'J');
    cout << "Original after modification: ";
    d1.display();
    cout << "Copy after modification: ";
    d2.display();  // Copy unchanged! (separate memory)
    
    cout << "\n--- End of main ---" << endl;
    return 0;
}
```

**Output:**
```
=== Shallow Copy vs Deep Copy ===

1. Shallow Copy (DANGEROUS):
Created: Hello
Destroying: Hello
Destroying: Hello

2. Deep Copy (CORRECT):
Created: World
Deep copy: World
Original: Data: World
Copy: Data: World

Modifying original...
Original after modification: Data: Jorld
Copy after modification: Data: World

--- End of main ---
Destroying: Jorld
Destroying: World
```

---

## 3. **Copy Constructor with Dynamic Memory**

Proper implementation of copy constructor for classes managing dynamic memory.

```cpp
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

class StringBuffer {
private:
    char* buffer;
    size_t size;
    static int objectCount;
    
public:
    // Constructor
    StringBuffer(const char* str = "") {
        size = strlen(str);
        buffer = new char[size + 1];
        strcpy(buffer, str);
        objectCount++;
        cout << "Constructor: " << buffer << " (Object #" << objectCount << ")" << endl;
    }
    
    // Deep copy constructor
    StringBuffer(const StringBuffer& other) {
        size = other.size;
        buffer = new char[size + 1];
        strcpy(buffer, other.buffer);
        objectCount++;
        cout << "Copy Constructor: copying '" << other.buffer << "' to '" 
             << buffer << "' (Object #" << objectCount << ")" << endl;
    }
    
    // Destructor
    ~StringBuffer() {
        cout << "Destructor: " << buffer << " (Object #" << objectCount << ")" << endl;
        delete[] buffer;
        objectCount--;
    }
    
    // Assignment operator (for completeness)
    StringBuffer& operator=(const StringBuffer& other) {
        if (this != &other) {
            delete[] buffer;
            size = other.size;
            buffer = new char[size + 1];
            strcpy(buffer, other.buffer);
            cout << "Assignment: " << buffer << endl;
        }
        return *this;
    }
    
    void append(const char* str) {
        size_t newSize = size + strlen(str);
        char* newBuffer = new char[newSize + 1];
        strcpy(newBuffer, buffer);
        strcat(newBuffer, str);
        delete[] buffer;
        buffer = newBuffer;
        size = newSize;
    }
    
    void display() const {
        cout << "Buffer: '" << buffer << "' (size: " << size << ")" << endl;
    }
    
    static int getCount() { return objectCount; }
};

int StringBuffer::objectCount = 0;

class ResourceManager {
private:
    int* data;
    size_t size;
    
public:
    // Constructor
    ResourceManager(size_t n) : size(n) {
        data = new int[size];
        for (size_t i = 0; i < size; i++) {
            data[i] = i;
        }
        cout << "ResourceManager created with " << size << " elements" << endl;
    }
    
    // Deep copy constructor
    ResourceManager(const ResourceManager& other) : size(other.size) {
        data = new int[size];
        for (size_t i = 0; i < size; i++) {
            data[i] = other.data[i];
        }
        cout << "ResourceManager copied (" << size << " elements)" << endl;
    }
    
    // Destructor
    ~ResourceManager() {
        cout << "ResourceManager destroyed (" << size << " elements)" << endl;
        delete[] data;
    }
    
    void setValue(size_t index, int value) {
        if (index < size) data[index] = value;
    }
    
    int getValue(size_t index) const {
        return (index < size) ? data[index] : -1;
    }
    
    void display() const {
        cout << "Data: ";
        for (size_t i = 0; i < size; i++) {
            cout << data[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    cout << "=== Copy Constructor with Dynamic Memory ===" << endl;
    
    cout << "\n1. StringBuffer (deep copy):" << endl;
    StringBuffer sb1("Hello");
    StringBuffer sb2 = sb1;  // Deep copy
    sb1.append(" World");
    cout << "sb1: ";
    sb1.display();
    cout << "sb2: ";
    sb2.display();  // Unchanged
    
    cout << "\n2. ResourceManager (deep copy):" << endl;
    ResourceManager rm1(5);
    ResourceManager rm2 = rm1;  // Deep copy
    
    cout << "rm1: ";
    rm1.display();
    cout << "rm2: ";
    rm2.display();
    
    cout << "\nModifying rm1..." << endl;
    rm1.setValue(2, 999);
    cout << "rm1 after modification: ";
    rm1.display();
    cout << "rm2 after modification: ";
    rm2.display();  // Unchanged
    
    cout << "\n--- End of main ---" << endl;
    return 0;
}
```

---

## 4. **Copy Constructor with Inheritance**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Base {
protected:
    int baseValue;
    
public:
    Base(int v) : baseValue(v) {
        cout << "Base constructor: " << baseValue << endl;
    }
    
    // Base copy constructor
    Base(const Base& other) : baseValue(other.baseValue) {
        cout << "Base copy constructor: " << baseValue << endl;
    }
    
    virtual ~Base() {
        cout << "Base destructor: " << baseValue << endl;
    }
    
    virtual void display() const {
        cout << "Base value: " << baseValue << endl;
    }
};

class Derived : public Base {
private:
    string name;
    int* data;
    
public:
    // Constructor
    Derived(int v, string n, int d) : Base(v), name(n) {
        data = new int(d);
        cout << "Derived constructor: " << name << endl;
    }
    
    // Derived copy constructor - must call Base copy constructor
    Derived(const Derived& other) 
        : Base(other),           // Call base copy constructor
          name(other.name + "_copy"),
          data(new int(*other.data))  // Deep copy
    {
        cout << "Derived copy constructor: " << name << endl;
    }
    
    // Destructor
    ~Derived() {
        cout << "Derived destructor: " << name << endl;
        delete data;
    }
    
    void display() const override {
        Base::display();
        cout << "Name: " << name << ", Data: " << *data << endl;
    }
    
    void modifyData(int newValue) {
        *data = newValue;
    }
};

int main() {
    cout << "=== Copy Constructor with Inheritance ===" << endl;
    
    cout << "\n1. Creating original object:" << endl;
    Derived d1(100, "Original", 999);
    d1.display();
    
    cout << "\n2. Copy constructor (deep copy):" << endl;
    Derived d2 = d1;  // Calls Base and Derived copy constructors
    d2.display();
    
    cout << "\n3. Modifying original's data:" << endl;
    d1.modifyData(777);
    cout << "Original after modification: ";
    d1.display();
    cout << "Copy after modification: ";
    d2.display();  // Unchanged (deep copy)
    
    cout << "\n--- End of main ---" << endl;
    return 0;
}
```

**Output:**
```
=== Copy Constructor with Inheritance ===

1. Creating original object:
Base constructor: 100
Derived constructor: Original
Base value: 100
Name: Original, Data: 999

2. Copy constructor (deep copy):
Base copy constructor: 100
Derived copy constructor: Original_copy
Base value: 100
Name: Original_copy, Data: 999

3. Modifying original's data:
Original after modification: Base value: 100
Name: Original, Data: 777
Copy after modification: Base value: 100
Name: Original_copy, Data: 999

--- End of main ---
Derived destructor: Original_copy
Base destructor: 100
Derived destructor: Original
Base destructor: 100
```

---

## 5. **Disabling Copy Constructor (Non-Copyable Classes)**

```cpp
#include <iostream>
#include <memory>
using namespace std;

// C++11 style: delete copy constructor
class NonCopyable1 {
private:
    int value;
    
public:
    NonCopyable1(int v) : value(v) {}
    
    // Delete copy constructor and copy assignment
    NonCopyable1(const NonCopyable1&) = delete;
    NonCopyable1& operator=(const NonCopyable1&) = delete;
    
    // Move constructor is still allowed
    NonCopyable1(NonCopyable1&&) = default;
    
    void display() const { cout << "Value: " << value << endl; }
};

// Traditional style: make copy constructor private
class NonCopyable2 {
private:
    int value;
    
    // Private copy constructor (no implementation)
    NonCopyable2(const NonCopyable2&);
    NonCopyable2& operator=(const NonCopyable2&);
    
public:
    NonCopyable2(int v) : value(v) {}
    
    void display() const { cout << "Value: " << value << endl; }
};

class UniqueResource {
private:
    int* data;
    
public:
    UniqueResource(int val) {
        data = new int(val);
        cout << "Resource created: " << *data << endl;
    }
    
    // Delete copy constructor - prevents copying
    UniqueResource(const UniqueResource&) = delete;
    UniqueResource& operator=(const UniqueResource&) = delete;
    
    // Move constructor - allows transferring ownership
    UniqueResource(UniqueResource&& other) noexcept : data(other.data) {
        other.data = nullptr;
        cout << "Resource moved" << endl;
    }
    
    ~UniqueResource() {
        if (data) {
            cout << "Resource destroyed: " << *data << endl;
            delete data;
        } else {
            cout << "Resource already moved" << endl;
        }
    }
    
    void display() const {
        if (data) {
            cout << "Resource value: " << *data << endl;
        } else {
            cout << "Resource is empty" << endl;
        }
    }
};

int main() {
    cout << "=== Non-Copyable Classes ===" << endl;
    
    cout << "\n1. NonCopyable1 (deleted copy):" << endl;
    NonCopyable1 n1(42);
    // NonCopyable1 n2 = n1;  // Error! Copy constructor deleted
    n1.display();
    
    cout << "\n2. UniqueResource (move-only):" << endl;
    UniqueResource u1(100);
    // UniqueResource u2 = u1;  // Error! Copy constructor deleted
    
    UniqueResource u2 = move(u1);  // OK - move constructor
    cout << "After move:" << endl;
    u1.display();
    u2.display();
    
    cout << "\n--- End of main ---" << endl;
    return 0;
}
```

---

## 6. **Practical Example: Image Class**

```cpp
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

class Image {
private:
    int width;
    int height;
    unsigned char* pixels;
    string filename;
    static int imageCount;
    
public:
    // Constructor
    Image(int w, int h, const string& name) : width(w), height(h), filename(name) {
        pixels = new unsigned char[width * height];
        memset(pixels, 0, width * height);
        imageCount++;
        cout << "Image created: " << filename << " (" << width << "x" << height << ")" << endl;
    }
    
    // Deep copy constructor
    Image(const Image& other) 
        : width(other.width), height(other.height), 
          filename(other.filename + "_copy") {
        pixels = new unsigned char[width * height];
        memcpy(pixels, other.pixels, width * height);
        imageCount++;
        cout << "Image copied: " << filename << endl;
    }
    
    // Destructor
    ~Image() {
        cout << "Image destroyed: " << filename << endl;
        delete[] pixels;
        imageCount--;
    }
    
    void setPixel(int x, int y, unsigned char value) {
        if (x >= 0 && x < width && y >= 0 && y < height) {
            pixels[y * width + x] = value;
        }
    }
    
    unsigned char getPixel(int x, int y) const {
        if (x >= 0 && x < width && y >= 0 && y < height) {
            return pixels[y * width + x];
        }
        return 0;
    }
    
    void fill(unsigned char value) {
        memset(pixels, value, width * height);
    }
    
    void display() const {
        cout << "Image: " << filename << " (" << width << "x" << height << ")" << endl;
        cout << "First row: ";
        for (int x = 0; x < min(10, width); x++) {
            cout << (int)pixels[x] << " ";
        }
        cout << "..." << endl;
    }
    
    static int getCount() { return imageCount; }
};

int Image::imageCount = 0;

class ImageProcessor {
private:
    vector<Image> images;
    
public:
    void addImage(const Image& img) {
        images.push_back(img);  // Calls copy constructor
        cout << "Added to processor" << endl;
    }
    
    void process() {
        cout << "\nProcessing " << images.size() << " images..." << endl;
        for (auto& img : images) {
            img.fill(128);  // Apply grayscale effect
            img.display();
        }
    }
};

int main() {
    cout << "=== Image Processing Example ===" << endl;
    
    cout << "\n1. Creating original images:" << endl;
    Image img1(1920, 1080, "landscape.jpg");
    Image img2(800, 600, "portrait.png");
    
    img1.fill(255);  // White
    img2.fill(100);  // Dark
    
    img1.display();
    img2.display();
    
    cout << "\n2. Copying images (deep copy):" << endl;
    Image img3 = img1;  // Copy constructor
    img3.display();
    
    cout << "\n3. Modifying original:" << endl;
    img1.fill(0);  // Black
    cout << "Original after modification: ";
    img1.display();
    cout << "Copy after modification: ";
    img3.display();  // Unchanged
    
    cout << "\n4. Image processor with vector:" << endl;
    ImageProcessor processor;
    processor.addImage(img1);
    processor.addImage(img2);
    processor.addImage(img3);
    processor.process();
    
    cout << "\nTotal images alive: " << Image::getCount() << endl;
    cout << "\n--- End of main ---" << endl;
    return 0;
}
```

---

## 📊 Copy Constructor Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Create copy of existing object |
| **Syntax** | `ClassName(const ClassName& other);` |
| **When Called** | Pass by value, return by value, explicit copy |
| **Default** | Member-wise copy (shallow) |
| **Deep Copy** | Required for dynamic resources |
| **Inheritance** | Must call base copy constructor |

---

## ✅ Best Practices

1. **Implement deep copy** for classes with dynamic memory
2. **Follow Rule of Three** if you need custom destructor or copy constructor
3. **Use `= delete`** to disable copying when appropriate
4. **Call base copy constructor** in derived classes
5. **Prefer `const` reference** parameter to avoid infinite recursion
6. **Initialize all members** in copy constructor

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Shallow copy** | Double deletion, data corruption | Implement deep copy |
| **Missing base copy** | Incomplete copy | Call base copy constructor |
| **Infinite recursion** | Passing by value in copy constructor | Use const reference |
| **Self-assignment** | Not handled in assignment | Check `this != &other` |
| **Resource leak** | Old resources not freed | Delete before copying |

---

## ✅ Key Takeaways

1. **Copy constructor** creates new object as copy of existing
2. **Default copy** is shallow - copies pointers, not data
3. **Deep copy** needed for dynamic memory management
4. **Called** during pass by value, return by value, explicit copy
5. **Rule of Three**: Destructor, copy constructor, copy assignment
6. **Disable copying** with `= delete` for move-only types
7. **Inheritance** requires calling base copy constructor

---