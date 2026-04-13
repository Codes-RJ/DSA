# Template Specialization

## 📖 Overview

Template specialization allows you to define custom implementations of templates for specific types. When the general template implementation doesn't work well for a particular type or requires special handling, you can provide a specialized version that overrides the generic behavior.

---

## 🎯 Key Concepts

- **Full Specialization**: Complete replacement for a specific type
- **Partial Specialization**: Specialization for some template parameters
- **Explicit Specialization**: Using `template <>` syntax
- **Function Template Specialization**: Special behavior for specific types
- **Class Template Specialization**: Custom class implementation

---

## 💻 Syntax Overview

### Full Specialization
```cpp
template <>
class ClassName<SpecificType> {
    // Specialized implementation
};
```

### Partial Specialization
```cpp
template <typename T>
class ClassName<T, SpecificType> {
    // Partially specialized implementation
};
```

---

## 🔍 Detailed Explanation

### 1. **Function Template Specialization**

```cpp
#include <iostream>
#include <cstring>
using namespace std;

// Generic function template
template <typename T>
T add(T a, T b) {
    cout << "Generic add: ";
    return a + b;
}

// Full specialization for const char*
template <>
const char* add<const char*>(const char* a, const char* b) {
    cout << "String specialization: ";
    static char result[100];
    strcpy(result, a);
    strcat(result, b);
    return result;
}

// Generic compare function
template <typename T>
bool compare(T a, T b) {
    cout << "Generic compare: ";
    return a == b;
}

// Specialization for double (with epsilon)
template <>
bool compare<double>(double a, double b) {
    cout << "Double specialization: ";
    const double epsilon = 1e-10;
    return abs(a - b) < epsilon;
}

// Generic print function
template <typename T>
void print(T value) {
    cout << "Generic print: " << value << endl;
}

// Specialization for bool
template <>
void print<bool>(bool value) {
    cout << "Bool specialization: " << (value ? "TRUE" : "FALSE") << endl;
}

// Specialization for pointers
template <typename T>
void print<T*>(T* ptr) {
    cout << "Pointer specialization: " << ptr << " -> " << *ptr << endl;
}

int main() {
    cout << "=== Function Template Specialization ===" << endl;
    
    // Generic add
    cout << add(5, 3) << endl;
    cout << add(3.14, 2.86) << endl;
    
    // Specialized string add
    cout << add("Hello", " World") << endl;
    
    cout << endl;
    
    // Generic compare
    cout << "5 == 5: " << compare(5, 5) << endl;
    cout << "5.0 == 5.0000000001: " << compare(5.0, 5.0000000001) << endl;
    
    cout << endl;
    
    // Generic print
    print(42);
    print(3.14);
    print("Hello");
    
    // Specialized print
    print(true);
    print(false);
    
    // Pointer specialization
    int x = 100;
    print(&x);
    
    return 0;
}
```

### 2. **Class Template Full Specialization**

```cpp
#include <iostream>
#include <cstring>
using namespace std;

// Generic Calculator class template
template <typename T>
class Calculator {
public:
    T add(T a, T b) {
        cout << "Generic add: ";
        return a + b;
    }
    
    T multiply(T a, T b) {
        cout << "Generic multiply: ";
        return a * b;
    }
    
    T divide(T a, T b) {
        cout << "Generic divide: ";
        if (b == 0) {
            throw runtime_error("Division by zero");
        }
        return a / b;
    }
    
    void display(T value) {
        cout << "Result: " << value << endl;
    }
};

// Full specialization for const char*
template <>
class Calculator<const char*> {
public:
    const char* add(const char* a, const char* b) {
        cout << "String add: ";
        static char result[100];
        strcpy(result, a);
        strcat(result, b);
        return result;
    }
    
    const char* multiply(const char* a, const char* b) {
        cout << "String multiply (concatenation): ";
        return add(a, b); // Reuse add functionality
    }
    
    const char* divide(const char* a, const char* b) {
        cout << "String divide (not supported): ";
        return "Cannot divide strings";
    }
    
    void display(const char* value) {
        cout << "String result: " << value << endl;
    }
};

// Full specialization for bool
template <>
class Calculator<bool> {
public:
    bool add(bool a, bool b) {
        cout << "Boolean add (OR): ";
        return a || b;
    }
    
    bool multiply(bool a, bool b) {
        cout << "Boolean multiply (AND): ";
        return a && b;
    }
    
    bool divide(bool a, bool b) {
        cout << "Boolean divide (not supported): ";
        return false;
    }
    
    void display(bool value) {
        cout << "Boolean result: " << (value ? "TRUE" : "FALSE") << endl;
    }
};

int main() {
    cout << "=== Class Template Full Specialization ===" << endl;
    
    // Generic calculator
    Calculator<int> intCalc;
    cout << intCalc.add(5, 3) << endl;
    cout << intCalc.multiply(4, 6) << endl;
    intCalc.display(intCalc.divide(10, 2));
    
    cout << endl;
    
    // String calculator (specialized)
    Calculator<const char*> stringCalc;
    cout << stringCalc.add("Hello", " World") << endl;
    cout << stringCalc.multiply("Hi", " There") << endl;
    stringCalc.display(stringCalc.divide("A", "B"));
    
    cout << endl;
    
    // Boolean calculator (specialized)
    Calculator<bool> boolCalc;
    cout << boolCalc.add(true, false) << endl;
    cout << boolCalc.multiply(true, true) << endl;
    cout << boolCalc.multiply(true, false) << endl;
    
    return 0;
}
```

### 3. **Class Template Partial Specialization**

```cpp
#include <iostream>
using namespace std;

// Generic template with two parameters
template <typename T, typename U>
class Pair {
private:
    T first;
    U second;
    
public:
    Pair(T f, U s) : first(f), second(s) {}
    
    void display() {
        cout << "Generic Pair[" << first << ", " << second << "]" << endl;
    }
    
    T getFirst() { return first; }
    U getSecond() { return second; }
};

// Partial specialization for same types
template <typename T>
class Pair<T, T> {
private:
    T first;
    T second;
    
public:
    Pair(T f, T s) : first(f), second(s) {}
    
    void display() {
        cout << "Same-type Pair[" << first << ", " << second << "]" << endl;
        cout << "Both elements are of the same type!" << endl;
    }
    
    T getFirst() { return first; }
    T getSecond() { return second; }
    
    // Additional method for same-type pairs
    T getSum() {
        return first + second;
    }
};

// Partial specialization for pointer types
template <typename T>
class Pair<T*, T*> {
private:
    T* first;
    T* second;
    
public:
    Pair(T* f, T* s) : first(f), second(s) {}
    
    void display() {
        cout << "Pointer Pair[" << first << ", " << second << "]" << endl;
        cout << "Values: [" << *first << ", " << *second << "]" << endl;
    }
    
    T* getFirst() { return first; }
    T* getSecond() { return second; }
    
    // Swap the pointed values
    void swapValues() {
        T temp = *first;
        *first = *second;
        *second = temp;
    }
};

// Template with three parameters
template <typename T, typename U, typename V>
class Triple {
private:
    T first;
    U second;
    V third;
    
public:
    Triple(T f, U s, V t) : first(f), second(s), third(t) {}
    
    void display() {
        cout << "Generic Triple[" << first << ", " << second << ", " << third << "]" << endl;
    }
};

// Partial specialization for all same types
template <typename T>
class Triple<T, T, T> {
private:
    T first, second, third;
    
public:
    Triple(T f, T s, T t) : first(f), second(s), third(t) {}
    
    void display() {
        cout << "Uniform Triple[" << first << ", " << second << ", " << third << "]" << endl;
        cout << "All elements are the same type!" << endl;
    }
    
    T getSum() {
        return first + second + third;
    }
};

int main() {
    cout << "=== Class Template Partial Specialization ===" << endl;
    
    // Generic pairs
    Pair<int, string> p1(42, "Answer");
    p1.display();
    
    Pair<double, bool> p2(3.14, true);
    p2.display();
    
    cout << endl;
    
    // Same-type pairs (partial specialization)
    Pair<int, int> p3(10, 20);
    p3.display();
    cout << "Sum: " << p3.getSum() << endl;
    
    Pair<string, string> p4("Hello", "World");
    p4.display();
    cout << "Sum: " << p4.getSum() << endl;
    
    cout << endl;
    
    // Pointer pairs (partial specialization)
    int x = 100, y = 200;
    Pair<int*, int*> p5(&x, &y);
    p5.display();
    
    cout << "Before swap: x=" << x << ", y=" << y << endl;
    p5.swapValues();
    cout << "After swap: x=" << x << ", y=" << y << endl;
    
    cout << endl;
    
    // Triple examples
    Triple<int, string, double> t1(1, "Two", 3.0);
    t1.display();
    
    Triple<int, int, int> t2(1, 2, 3);
    t2.display();
    cout << "Sum: " << t2.getSum() << endl;
    
    return 0;
}
```

### 4. **Advanced Specialization Techniques**

```cpp
#include <iostream>
#include <type_traits>
using namespace std;

// Template with conditionally enabled members
template <typename T>
class Container {
private:
    T data;
    
public:
    Container(T value) : data(value) {}
    
    // Method enabled only for arithmetic types
    template <typename U = T>
    typename enable_if<is_arithmetic<U>::value, U>::type
    multiply(U factor) {
        cout << "Arithmetic multiply: ";
        return data * factor;
    }
    
    // Method enabled only for string types
    template <typename U = T>
    typename enable_if<is_same<U, string>::value, U>::type
    repeat(int times) {
        cout << "String repeat: ";
        string result;
        for (int i = 0; i < times; i++) {
            result += data;
        }
        return result;
    }
    
    void display() {
        cout << "Container holds: " << data << endl;
    }
};

// Specialization for arrays
template <typename T, size_t N>
class Container<T[N]> {
private:
    T data[N];
    
public:
    Container(const T (&arr)[N]) {
        for (size_t i = 0; i < N; i++) {
            data[i] = arr[i];
        }
    }
    
    T& operator[](size_t index) {
        return data[index];
    }
    
    const T& operator[](size_t index) const {
        return data[index];
    }
    
    size_t size() const { return N; }
    
    void display() {
        cout << "Array Container [";
        for (size_t i = 0; i < N; i++) {
            cout << data[i];
            if (i < N - 1) cout << ", ";
        }
        cout << "]" << endl;
    }
};

// Template class with specialization based on type properties
template <typename T>
class TypeInfo {
public:
    static void printInfo() {
        cout << "Generic type information" << endl;
        cout << "Size: " << sizeof(T) << " bytes" << endl;
    }
};

// Partial specialization for pointers
template <typename T>
class TypeInfo<T*> {
public:
    static void printInfo() {
        cout << "Pointer type information" << endl;
        cout << "Pointer size: " << sizeof(T*) << " bytes" << endl;
        cout << "Pointed type size: " << sizeof(T) << " bytes" << endl;
    }
};

// Partial specialization for arrays
template <typename T, size_t N>
class TypeInfo<T[N]> {
public:
    static void printInfo() {
        cout << "Array type information" << endl;
        cout << "Array size: " << N << " elements" << endl;
        cout << "Total size: " << sizeof(T[N]) << " bytes" << endl;
        cout << "Element size: " << sizeof(T) << " bytes" << endl;
    }
};

int main() {
    cout << "=== Advanced Specialization Techniques ===" << endl;
    
    // Container with conditional methods
    Container<int> intContainer(42);
    intContainer.display();
    cout << "Multiplied by 3: " << intContainer.multiply(3) << endl;
    
    Container<string> stringContainer("Hello");
    stringContainer.display();
    cout << "Repeated 3 times: " << stringContainer.repeat(3) << endl;
    
    cout << endl;
    
    // Array container specialization
    int arr[] = {1, 2, 3, 4, 5};
    Container<int[5]> arrayContainer(arr);
    arrayContainer.display();
    cout << "Element at index 2: " << arrayContainer[2] << endl;
    
    cout << endl;
    
    // Type information with specializations
    cout << "Type information:" << endl;
    TypeInfo<int>::printInfo();
    cout << endl;
    
    TypeInfo<int*>::printInfo();
    cout << endl;
    
    TypeInfo<double[10]>::printInfo();
    
    return 0;
}
```

### 5. **Specialization with Inheritance**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Base template class
template <typename T>
class Shape {
protected:
    T data;
    
public:
    Shape(T d) : data(d) {}
    
    virtual void draw() {
        cout << "Drawing generic shape with data: " << data << endl;
    }
    
    virtual double getArea() {
        cout << "Generic area calculation: ";
        return 0.0;
    }
    
    virtual ~Shape() {}
};

// Specialization for Circle
template <>
class Shape<double> {
protected:
    double radius;
    
public:
    Shape(double r) : radius(r) {}
    
    void draw() {
        cout << "Drawing circle with radius: " << radius << endl;
    }
    
    double getArea() {
        cout << "Circle area calculation: ";
        return 3.14159 * radius * radius;
    }
};

// Template class inheriting from specialized template
template <typename T>
class ColoredShape : public Shape<T> {
private:
    string color;
    
public:
    ColoredShape(T data, string c) : Shape<T>(data), color(c) {}
    
    void draw() override {
        cout << "Drawing colored " << color << " shape" << endl;
        Shape<T>::draw();
    }
};

// Specialization for Rectangle (using composition)
template <>
class Shape<pair<double, double>> {
protected:
    pair<double, double> dimensions; // width, height
    
public:
    Shape(pair<double, double> dims) : dimensions(dims) {}
    
    void draw() {
        cout << "Drawing rectangle " << dimensions.first << "x" << dimensions.second << endl;
    }
    
    double getArea() {
        cout << "Rectangle area calculation: ";
        return dimensions.first * dimensions.second;
    }
};

int main() {
    cout << "=== Specialization with Inheritance ===" << endl;
    
    // Generic shape
    Shape<string> genericShape("Generic Data");
    genericShape.draw();
    cout << "Area: " << genericShape.getArea() << endl;
    
    cout << endl;
    
    // Specialized circle
    Shape<double> circle(5.0);
    circle.draw();
    cout << "Area: " << circle.getArea() << endl;
    
    cout << endl;
    
    // Colored shape inheriting from generic
    ColoredShape<int> coloredIntShape(42, "red");
    coloredIntShape.draw();
    
    cout << endl;
    
    // Specialized rectangle
    Shape<pair<double, double>> rectangle({4.0, 6.0});
    rectangle.draw();
    cout << "Area: " << rectangle.getArea() << endl;
    
    return 0;
}
```

---

## 🎮 Complete Example: Smart Pointer Specializations

```cpp
#include <iostream>
#include <memory>
#include <type_traits>
using namespace std;

// Generic smart pointer template
template <typename T>
class SmartPointer {
private:
    T* ptr;
    
public:
    explicit SmartPointer(T* p = nullptr) : ptr(p) {}
    
    ~SmartPointer() {
        delete ptr;
    }
    
    // Copy semantics (deleted)
    SmartPointer(const SmartPointer&) = delete;
    SmartPointer& operator=(const SmartPointer&) = delete;
    
    // Move semantics
    SmartPointer(SmartPointer&& other) noexcept : ptr(other.ptr) {
        other.ptr = nullptr;
    }
    
    SmartPointer& operator=(SmartPointer&& other) noexcept {
        if (this != &other) {
            delete ptr;
            ptr = other.ptr;
            other.ptr = nullptr;
        }
        return *this;
    }
    
    T& operator*() const { return *ptr; }
    T* operator->() const { return ptr; }
    T* get() const { return ptr; }
    
    explicit operator bool() const { return ptr != nullptr; }
    
    void reset(T* p = nullptr) {
        delete ptr;
        ptr = p;
    }
    
    void displayInfo() const {
        cout << "Generic SmartPointer managing: " << typeid(T).name() << endl;
        if (ptr) {
            cout << "  Value: " << *ptr << endl;
        } else {
            cout << "  Value: nullptr" << endl;
        }
    }
};

// Specialization for arrays
template <typename T>
class SmartPointer<T[]> {
private:
    T* ptr;
    size_t size;
    
public:
    SmartPointer(T* p = nullptr, size_t s = 0) : ptr(p), size(s) {}
    
    ~SmartPointer() {
        delete[] ptr;
    }
    
    // Delete copy operations
    SmartPointer(const SmartPointer&) = delete;
    SmartPointer& operator=(const SmartPointer&) = delete;
    
    // Move operations
    SmartPointer(SmartPointer&& other) noexcept : ptr(other.ptr), size(other.size) {
        other.ptr = nullptr;
        other.size = 0;
    }
    
    SmartPointer& operator=(SmartPointer&& other) noexcept {
        if (this != &other) {
            delete[] ptr;
            ptr = other.ptr;
            size = other.size;
            other.ptr = nullptr;
            other.size = 0;
        }
        return *this;
    }
    
    T& operator[](size_t index) const {
        if (!ptr || index >= size) {
            throw out_of_range("Array index out of bounds");
        }
        return ptr[index];
    }
    
    T* get() const { return ptr; }
    size_t getSize() const { return size; }
    
    explicit operator bool() const { return ptr != nullptr; }
    
    void displayInfo() const {
        cout << "Array SmartPointer managing: " << typeid(T).name() << "[" << size << "]" << endl;
        if (ptr) {
            cout << "  Values: [";
            for (size_t i = 0; i < size; i++) {
                cout << ptr[i];
                if (i < size - 1) cout << ", ";
            }
            cout << "]" << endl;
        } else {
            cout << "  Values: nullptr" << endl;
        }
    }
};

// Specialization for FILE handles
template <>
class SmartPointer<FILE> {
private:
    FILE* file;
    
public:
    explicit SmartPointer(FILE* f = nullptr) : file(f) {}
    
    ~SmartPointer() {
        if (file) {
            fclose(file);
        }
    }
    
    // Delete copy operations
    SmartPointer(const SmartPointer&) = delete;
    SmartPointer& operator=(const SmartPointer&) = delete;
    
    // Move operations
    SmartPointer(SmartPointer&& other) noexcept : file(other.file) {
        other.file = nullptr;
    }
    
    SmartPointer& operator=(SmartPointer&& other) noexcept {
        if (this != &other) {
            if (file) fclose(file);
            file = other.file;
            other.file = nullptr;
        }
        return *this;
    }
    
    FILE* get() const { return file; }
    
    explicit operator bool() const { return file != nullptr; }
    
    // File-specific operations
    int write(const string& text) {
        if (!file) return -1;
        return fwrite(text.c_str(), 1, text.length(), file);
    }
    
    string readLine() {
        if (!file) return "";
        
        char buffer[256];
        if (fgets(buffer, sizeof(buffer), file)) {
            return string(buffer);
        }
        return "";
    }
    
    void displayInfo() const {
        cout << "FILE SmartPointer managing: ";
        if (file) {
            cout << "open file handle" << endl;
        } else {
            cout << "nullptr" << endl;
        }
    }
};

int main() {
    cout << "=== Smart Pointer Specializations Demo ===" << endl;
    
    // Generic smart pointer
    {
        SmartPointer<int> intPtr(new int(42));
        intPtr.displayInfo();
        cout << "Value: " << *intPtr << endl;
        
        // Move semantics
        SmartPointer<int> movedPtr = move(intPtr);
        movedPtr.displayInfo();
        cout << "Original valid: " << (intPtr ? "Yes" : "No") << endl;
    }
    
    cout << endl;
    
    // Array smart pointer specialization
    {
        SmartPointer<int[]> arrPtr(new int[5]{1, 2, 3, 4, 5}, 5);
        arrPtr.displayInfo();
        
        cout << "Array elements: ";
        for (size_t i = 0; i < arrPtr.getSize(); i++) {
            cout << arrPtr[i] << " ";
        }
        cout << endl;
    }
    
    cout << endl;
    
    // FILE smart pointer specialization
    {
        SmartPointer<FILE> filePtr(fopen("test.txt", "w"));
        filePtr.displayInfo();
        
        if (filePtr) {
            filePtr.write("Hello from specialized smart pointer!");
            cout << "Wrote to file successfully" << endl;
        }
        
        // File automatically closed when filePtr goes out of scope
    }
    
    cout << endl;
    
    // Read from file
    {
        SmartPointer<FILE> filePtr(fopen("test.txt", "r"));
        if (filePtr) {
            string content = filePtr.readLine();
            cout << "Read from file: " << content << endl;
        }
    }
    
    return 0;
}
```

---

## ⚡ Performance Considerations

### Advantages
- ✅ **Optimized for Specific Types**: Specialized implementations can be more efficient
- ✅ **Type-Specific Behavior**: Handle edge cases and special requirements
- ✅ **Compile-Time Selection**: No runtime overhead for choosing implementation

### Considerations
- ⚠️ **Code Maintenance**: Multiple versions to maintain
- ⚠️ **Compilation Time**: More templates to instantiate
- ⚠️ **Code Bloat**: Additional specialized code

---

## 🐛 Common Pitfalls

| Problem | Solution |
|---------|----------|
| **Specialization not found** | Ensure specialization syntax is correct |
| **Ambiguous specialization** | Be specific about which parameters to specialize |
| **Partial specialization order** | Most specific specialization is chosen |
| **Function specialization conflicts** | Use overloads instead of function specialization |

---

## ✅ Best Practices

1. **Specialize only when necessary** - prefer generic implementations
2. **Document specialization reasons** - explain why special behavior is needed
3. **Keep specializations consistent** - maintain similar interfaces
4. **Test all specializations** - ensure they work correctly
5. **Use concepts (C++20)** instead of specialization when possible
6. **Consider overloads** for function templates instead of specialization

---

## 📚 Related Topics

- [Function Templates](01_Function_Templates.md)
- [Class Templates](02_Class_Templates.md)
- [Variadic Templates](04_Variadic_Templates.md)
- [Template Metaprogramming](05_Template_Metaprogramming.md)

---

## 🚀 Next Steps

Continue learning about:
- **Variadic Templates**: Variable number of template arguments
- **Template Metaprogramming**: Compile-time computation
- **C++20 Concepts**: Modern template constraints
- **Advanced Template Techniques**: SFINAE, tag dispatch, and more

---
---

## Next Step

- Go to [04_Variadic_Templates.md](04_Variadic_Templates.md) to continue with Variadic Templates.
