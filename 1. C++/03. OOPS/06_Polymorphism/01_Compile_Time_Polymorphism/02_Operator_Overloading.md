# Operator Overloading in C++ - Complete Guide

## 📖 Overview

Operator overloading allows user-defined types (classes) to define custom behavior for built-in operators (+, -, *, /, ==, etc.). It makes user-defined types behave like built-in types, enabling intuitive syntax and natural expressions. Operator overloading is a form of compile-time polymorphism that enhances code readability and maintainability.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Operator Overloading** | Defining custom behavior for operators on user-defined types |
| **Syntax** | `return_type operator@(parameters)` |
| **Operators** | Can overload most operators (except ::, ., .*, ?:) |
| **Member vs Non-member** | Operators can be member functions or friend functions |

---

## 1. **Basic Operator Overloading (Arithmetic)**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Complex {
private:
    double real;
    double imag;
    
public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}
    
    // Overload + operator
    Complex operator+(const Complex& other) const {
        return Complex(real + other.real, imag + other.imag);
    }
    
    // Overload - operator
    Complex operator-(const Complex& other) const {
        return Complex(real - other.real, imag - other.imag);
    }
    
    // Overload * operator
    Complex operator*(const Complex& other) const {
        return Complex(
            real * other.real - imag * other.imag,
            real * other.imag + imag * other.real
        );
    }
    
    // Overload / operator
    Complex operator/(const Complex& other) const {
        double denominator = other.real * other.real + other.imag * other.imag;
        return Complex(
            (real * other.real + imag * other.imag) / denominator,
            (imag * other.real - real * other.imag) / denominator
        );
    }
    
    // Overload unary - operator
    Complex operator-() const {
        return Complex(-real, -imag);
    }
    
    void display() const {
        cout << real;
        if (imag >= 0) cout << " + " << imag << "i";
        else cout << " - " << -imag << "i";
    }
};

int main() {
    cout << "=== Basic Operator Overloading ===" << endl;
    
    Complex c1(3, 4);
    Complex c2(1, -2);
    
    cout << "c1 = "; c1.display(); cout << endl;
    cout << "c2 = "; c2.display(); cout << endl;
    
    Complex sum = c1 + c2;
    cout << "c1 + c2 = "; sum.display(); cout << endl;
    
    Complex diff = c1 - c2;
    cout << "c1 - c2 = "; diff.display(); cout << endl;
    
    Complex prod = c1 * c2;
    cout << "c1 * c2 = "; prod.display(); cout << endl;
    
    Complex quot = c1 / c2;
    cout << "c1 / c2 = "; quot.display(); cout << endl;
    
    Complex neg = -c1;
    cout << "-c1 = "; neg.display(); cout << endl;
    
    return 0;
}
```

**Output:**
```
=== Basic Operator Overloading ===
c1 = 3 + 4i
c2 = 1 - 2i
c1 + c2 = 4 + 2i
c1 - c2 = 2 + 6i
c1 * c2 = 11 - 2i
c1 / c2 = -1 + 2i
-c1 = -3 - 4i
```

---

## 2. **Comparison Operators**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Point {
private:
    int x, y;
    
public:
    Point(int xVal = 0, int yVal = 0) : x(xVal), y(yVal) {}
    
    // Equality operators
    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
    
    bool operator!=(const Point& other) const {
        return !(*this == other);
    }
    
    // Relational operators
    bool operator<(const Point& other) const {
        if (x != other.x) return x < other.x;
        return y < other.y;
    }
    
    bool operator<=(const Point& other) const {
        return *this < other || *this == other;
    }
    
    bool operator>(const Point& other) const {
        return !(*this <= other);
    }
    
    bool operator>=(const Point& other) const {
        return !(*this < other);
    }
    
    void display() const {
        cout << "(" << x << ", " << y << ")";
    }
};

class String {
private:
    string data;
    
public:
    String(const string& str = "") : data(str) {}
    
    // Comparison operators
    bool operator==(const String& other) const {
        return data == other.data;
    }
    
    bool operator!=(const String& other) const {
        return data != other.data;
    }
    
    bool operator<(const String& other) const {
        return data < other.data;
    }
    
    bool operator>(const String& other) const {
        return data > other.data;
    }
    
    // Concatenation
    String operator+(const String& other) const {
        return String(data + other.data);
    }
    
    void display() const {
        cout << "\"" << data << "\"";
    }
};

int main() {
    cout << "=== Comparison Operators ===" << endl;
    
    cout << "\n1. Point comparison:" << endl;
    Point p1(3, 4);
    Point p2(3, 4);
    Point p3(5, 1);
    
    cout << "p1 = "; p1.display(); cout << endl;
    cout << "p2 = "; p2.display(); cout << endl;
    cout << "p3 = "; p3.display(); cout << endl;
    
    cout << "p1 == p2: " << (p1 == p2 ? "true" : "false") << endl;
    cout << "p1 != p3: " << (p1 != p3 ? "true" : "false") << endl;
    cout << "p1 < p3: " << (p1 < p3 ? "true" : "false") << endl;
    cout << "p3 > p1: " << (p3 > p1 ? "true" : "false") << endl;
    
    cout << "\n2. String comparison:" << endl;
    String s1("Apple");
    String s2("Apple");
    String s3("Banana");
    
    cout << "s1 = "; s1.display(); cout << endl;
    cout << "s2 = "; s2.display(); cout << endl;
    cout << "s3 = "; s3.display(); cout << endl;
    
    cout << "s1 == s2: " << (s1 == s2 ? "true" : "false") << endl;
    cout << "s1 != s3: " << (s1 != s3 ? "true" : "false") << endl;
    cout << "s1 < s3: " << (s1 < s3 ? "true" : "false") << endl;
    
    String s4 = s1 + s3;
    cout << "s1 + s3 = "; s4.display(); cout << endl;
    
    return 0;
}
```

---

## 3. **Assignment Operators**

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class StringBuffer {
private:
    char* data;
    size_t length;
    
public:
    // Constructor
    StringBuffer(const char* str = "") {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "Created: " << data << endl;
    }
    
    // Copy constructor
    StringBuffer(const StringBuffer& other) {
        length = other.length;
        data = new char[length + 1];
        strcpy(data, other.data);
        cout << "Copied: " << data << endl;
    }
    
    // Destructor
    ~StringBuffer() {
        cout << "Destroyed: " << data << endl;
        delete[] data;
    }
    
    // Copy assignment operator
    StringBuffer& operator=(const StringBuffer& other) {
        if (this != &other) {
            cout << "Assigning: " << data << " = " << other.data << endl;
            delete[] data;
            length = other.length;
            data = new char[length + 1];
            strcpy(data, other.data);
        }
        return *this;
    }
    
    // Move assignment operator (C++11)
    StringBuffer& operator=(StringBuffer&& other) noexcept {
        if (this != &other) {
            cout << "Move assigning: " << data << " = " << other.data << endl;
            delete[] data;
            data = other.data;
            length = other.length;
            other.data = nullptr;
            other.length = 0;
        }
        return *this;
    }
    
    // Compound assignment operators
    StringBuffer& operator+=(const StringBuffer& other) {
        char* newData = new char[length + other.length + 1];
        strcpy(newData, data);
        strcat(newData, other.data);
        delete[] data;
        data = newData;
        length += other.length;
        return *this;
    }
    
    void display() const {
        cout << "String: " << data << " (length=" << length << ")" << endl;
    }
};

int main() {
    cout << "=== Assignment Operators ===" << endl;
    
    StringBuffer s1("Hello");
    StringBuffer s2("World");
    StringBuffer s3("Temp");
    
    cout << "\n1. Copy assignment:" << endl;
    s3 = s1;  // Copy assignment
    
    cout << "\n2. Move assignment:" << endl;
    s2 = move(s3);  // Move assignment
    
    cout << "\n3. Compound assignment (+=):" << endl;
    s1 += s2;
    
    cout << "\n4. Final strings:" << endl;
    s1.display();
    s2.display();
    
    return 0;
}
```

---

## 4. **Increment/Decrement Operators**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Counter {
private:
    int value;
    
public:
    Counter(int v = 0) : value(v) {}
    
    // Prefix increment (++c)
    Counter& operator++() {
        ++value;
        return *this;
    }
    
    // Postfix increment (c++)
    Counter operator++(int) {
        Counter temp = *this;
        ++value;
        return temp;
    }
    
    // Prefix decrement (--c)
    Counter& operator--() {
        --value;
        return *this;
    }
    
    // Postfix decrement (c--)
    Counter operator--(int) {
        Counter temp = *this;
        --value;
        return temp;
    }
    
    int getValue() const { return value; }
    
    void display() const {
        cout << "Counter: " << value << endl;
    }
};

class Iterator {
private:
    int* ptr;
    int index;
    
public:
    Iterator(int* p, int i) : ptr(p), index(i) {}
    
    // Dereference operator
    int& operator*() {
        return ptr[index];
    }
    
    const int& operator*() const {
        return ptr[index];
    }
    
    // Arrow operator
    int* operator->() {
        return &ptr[index];
    }
    
    // Prefix increment (++iter)
    Iterator& operator++() {
        ++index;
        return *this;
    }
    
    // Postfix increment (iter++)
    Iterator operator++(int) {
        Iterator temp = *this;
        ++index;
        return temp;
    }
    
    // Equality
    bool operator==(const Iterator& other) const {
        return ptr == other.ptr && index == other.index;
    }
    
    bool operator!=(const Iterator& other) const {
        return !(*this == other);
    }
    
    int getIndex() const { return index; }
};

int main() {
    cout << "=== Increment/Decrement Operators ===" << endl;
    
    cout << "\n1. Counter with prefix/postfix:" << endl;
    Counter c(10);
    cout << "Initial: "; c.display();
    
    cout << "Prefix ++c: "; (++c).display();
    cout << "After prefix: "; c.display();
    
    cout << "Postfix c++: "; (c++).display();
    cout << "After postfix: "; c.display();
    
    cout << "\n2. Iterator for array:" << endl;
    int arr[] = {10, 20, 30, 40, 50};
    Iterator it(arr, 0);
    Iterator end(arr, 5);
    
    cout << "Iterating: ";
    while (it != end) {
        cout << *it << " ";
        ++it;
    }
    cout << endl;
    
    return 0;
}
```

---

## 5. **Stream Insertion/Extraction Operators**

```cpp
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

class Date {
private:
    int day, month, year;
    
public:
    Date(int d = 1, int m = 1, int y = 2000) : day(d), month(m), year(y) {}
    
    // Friend functions for stream operators
    friend ostream& operator<<(ostream& os, const Date& d);
    friend istream& operator>>(istream& is, Date& d);
    
    bool isValid() const {
        if (year < 1900 || year > 2100) return false;
        if (month < 1 || month > 12) return false;
        
        int daysInMonth[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if (month == 2 && ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))) {
            daysInMonth[1] = 29;
        }
        return (day >= 1 && day <= daysInMonth[month - 1]);
    }
};

ostream& operator<<(ostream& os, const Date& d) {
    os << setfill('0') << setw(2) << d.day << "/"
       << setw(2) << d.month << "/"
       << d.year;
    return os;
}

istream& operator>>(istream& is, Date& d) {
    char slash1, slash2;
    is >> d.day >> slash1 >> d.month >> slash2 >> d.year;
    
    if (slash1 != '/' || slash2 != '/') {
        is.setstate(ios::failbit);
    }
    
    if (!d.isValid()) {
        is.setstate(ios::failbit);
    }
    
    return is;
}

class Vector3D {
private:
    double x, y, z;
    
public:
    Vector3D(double xVal = 0, double yVal = 0, double zVal = 0) 
        : x(xVal), y(yVal), z(zVal) {}
    
    friend ostream& operator<<(ostream& os, const Vector3D& v);
    friend istream& operator>>(istream& is, Vector3D& v);
    
    Vector3D operator+(const Vector3D& other) const {
        return Vector3D(x + other.x, y + other.y, z + other.z);
    }
};

ostream& operator<<(ostream& os, const Vector3D& v) {
    os << "(" << v.x << ", " << v.y << ", " << v.z << ")";
    return os;
}

istream& operator>>(istream& is, Vector3D& v) {
    char open, comma1, comma2, close;
    is >> open >> v.x >> comma1 >> v.y >> comma2 >> v.z >> close;
    
    if (open != '(' || comma1 != ',' || comma2 != ',' || close != ')') {
        is.setstate(ios::failbit);
    }
    
    return is;
}

int main() {
    cout << "=== Stream Insertion/Extraction Operators ===" << endl;
    
    cout << "\n1. Date I/O:" << endl;
    Date d1(15, 3, 2024);
    cout << "Date: " << d1 << endl;
    
    Date d2;
    cout << "Enter a date (dd/mm/yyyy): ";
    // cin >> d2;  // Uncomment for interactive input
    // cout << "You entered: " << d2 << endl;
    
    cout << "\n2. Vector3D I/O:" << endl;
    Vector3D v1(3, 4, 5);
    cout << "Vector: " << v1 << endl;
    
    Vector3D v2;
    cout << "Enter a vector (x, y, z): ";
    // cin >> v2;  // Uncomment for interactive input
    // cout << "You entered: " << v2 << endl;
    
    Vector3D v3 = v1 + Vector3D(1, 2, 3);
    cout << "v1 + (1,2,3) = " << v3 << endl;
    
    return 0;
}
```

---

## 6. **Subscript and Function Call Operators**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <stdexcept>
using namespace std;

class Array {
private:
    int* data;
    size_t size;
    
public:
    Array(size_t s) : size(s) {
        data = new int[size];
        for (size_t i = 0; i < size; i++) {
            data[i] = 0;
        }
    }
    
    ~Array() {
        delete[] data;
    }
    
    // Subscript operator (non-const)
    int& operator[](size_t index) {
        if (index >= size) {
            throw out_of_range("Index out of bounds");
        }
        return data[index];
    }
    
    // Subscript operator (const)
    const int& operator[](size_t index) const {
        if (index >= size) {
            throw out_of_range("Index out of bounds");
        }
        return data[index];
    }
    
    size_t getSize() const { return size; }
};

class Matrix {
private:
    vector<vector<int>> data;
    size_t rows, cols;
    
public:
    Matrix(size_t r, size_t c) : rows(r), cols(c) {
        data.resize(rows, vector<int>(cols, 0));
    }
    
    // Double subscript operator (returns proxy)
    vector<int>& operator[](size_t row) {
        if (row >= rows) {
            throw out_of_range("Row index out of bounds");
        }
        return data[row];
    }
    
    const vector<int>& operator[](size_t row) const {
        if (row >= rows) {
            throw out_of_range("Row index out of bounds");
        }
        return data[row];
    }
    
    size_t getRows() const { return rows; }
    size_t getCols() const { return cols; }
};

class Multiplier {
private:
    int factor;
    
public:
    Multiplier(int f) : factor(f) {}
    
    // Function call operator (functor)
    int operator()(int x) const {
        return x * factor;
    }
    
    int operator()(int x, int y) const {
        return x * y * factor;
    }
};

class Accumulator {
private:
    int sum;
    
public:
    Accumulator() : sum(0) {}
    
    // Function call operator
    int operator()(int x) {
        sum += x;
        return sum;
    }
    
    int getSum() const { return sum; }
    void reset() { sum = 0; }
};

int main() {
    cout << "=== Subscript and Function Call Operators ===" << endl;
    
    cout << "\n1. Array subscript operator:" << endl;
    Array arr(5);
    for (size_t i = 0; i < arr.getSize(); i++) {
        arr[i] = i * 10;
    }
    cout << "Array contents: ";
    for (size_t i = 0; i < arr.getSize(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    cout << "\n2. Matrix double subscript:" << endl;
    Matrix mat(3, 3);
    for (size_t i = 0; i < mat.getRows(); i++) {
        for (size_t j = 0; j < mat.getCols(); j++) {
            mat[i][j] = i * mat.getCols() + j + 1;
        }
    }
    
    cout << "Matrix:" << endl;
    for (size_t i = 0; i < mat.getRows(); i++) {
        for (size_t j = 0; j < mat.getCols(); j++) {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
    
    cout << "\n3. Function call operator (functor):" << endl;
    Multiplier times2(2);
    cout << "times2(5) = " << times2(5) << endl;
    cout << "times2(3, 4) = " << times2(3, 4) << endl;
    
    cout << "\n4. Accumulator functor:" << endl;
    Accumulator acc;
    cout << "acc(10) = " << acc(10) << endl;
    cout << "acc(20) = " << acc(20) << endl;
    cout << "acc(30) = " << acc(30) << endl;
    cout << "Total sum: " << acc.getSum() << endl;
    
    return 0;
}
```

---

## 7. **Practical Example: Rational Number Class**

```cpp
#include <iostream>
#include <string>
#include <numeric>
using namespace std;

class Rational {
private:
    int numerator;
    int denominator;
    
    void simplify() {
        int gcd_val = gcd(abs(numerator), abs(denominator));
        numerator /= gcd_val;
        denominator /= gcd_val;
        
        if (denominator < 0) {
            numerator = -numerator;
            denominator = -denominator;
        }
    }
    
public:
    Rational(int num = 0, int den = 1) : numerator(num), denominator(den) {
        if (denominator == 0) {
            throw invalid_argument("Denominator cannot be zero");
        }
        simplify();
    }
    
    // Arithmetic operators
    Rational operator+(const Rational& other) const {
        return Rational(
            numerator * other.denominator + other.numerator * denominator,
            denominator * other.denominator
        );
    }
    
    Rational operator-(const Rational& other) const {
        return Rational(
            numerator * other.denominator - other.numerator * denominator,
            denominator * other.denominator
        );
    }
    
    Rational operator*(const Rational& other) const {
        return Rational(
            numerator * other.numerator,
            denominator * other.denominator
        );
    }
    
    Rational operator/(const Rational& other) const {
        return Rational(
            numerator * other.denominator,
            denominator * other.numerator
        );
    }
    
    // Comparison operators
    bool operator==(const Rational& other) const {
        return numerator == other.numerator && denominator == other.denominator;
    }
    
    bool operator<(const Rational& other) const {
        return numerator * other.denominator < other.numerator * denominator;
    }
    
    bool operator<=(const Rational& other) const {
        return *this < other || *this == other;
    }
    
    bool operator>(const Rational& other) const {
        return !(*this <= other);
    }
    
    bool operator>=(const Rational& other) const {
        return !(*this < other);
    }
    
    // Unary operators
    Rational operator-() const {
        return Rational(-numerator, denominator);
    }
    
    // Compound assignment
    Rational& operator+=(const Rational& other) {
        *this = *this + other;
        return *this;
    }
    
    Rational& operator-=(const Rational& other) {
        *this = *this - other;
        return *this;
    }
    
    Rational& operator*=(const Rational& other) {
        *this = *this * other;
        return *this;
    }
    
    Rational& operator/=(const Rational& other) {
        *this = *this / other;
        return *this;
    }
    
    // Conversion to double
    explicit operator double() const {
        return static_cast<double>(numerator) / denominator;
    }
    
    // Stream operators
    friend ostream& operator<<(ostream& os, const Rational& r);
    friend istream& operator>>(istream& is, Rational& r);
};

ostream& operator<<(ostream& os, const Rational& r) {
    if (r.denominator == 1) {
        os << r.numerator;
    } else {
        os << r.numerator << "/" << r.denominator;
    }
    return os;
}

istream& operator>>(istream& is, Rational& r) {
    int num, den;
    char slash;
    is >> num;
    
    if (is.peek() == '/') {
        is >> slash >> den;
        if (slash != '/') {
            is.setstate(ios::failbit);
        }
    } else {
        den = 1;
    }
    
    if (den == 0) {
        is.setstate(ios::failbit);
    } else {
        r = Rational(num, den);
    }
    
    return is;
}

int main() {
    cout << "=== Rational Number Class ===" << endl;
    
    Rational r1(3, 4);
    Rational r2(1, 2);
    Rational r3(2, 3);
    
    cout << "r1 = " << r1 << endl;
    cout << "r2 = " << r2 << endl;
    cout << "r3 = " << r3 << endl;
    
    cout << "\nArithmetic:" << endl;
    cout << "r1 + r2 = " << (r1 + r2) << endl;
    cout << "r1 - r2 = " << (r1 - r2) << endl;
    cout << "r1 * r2 = " << (r1 * r2) << endl;
    cout << "r1 / r2 = " << (r1 / r2) << endl;
    
    cout << "\nComparisons:" << endl;
    cout << "r1 == r2: " << (r1 == r2 ? "true" : "false") << endl;
    cout << "r1 < r2: " << (r1 < r2 ? "true" : "false") << endl;
    cout << "r1 > r2: " << (r1 > r2 ? "true" : "false") << endl;
    
    cout << "\nCompound assignment:" << endl;
    Rational r4 = r1;
    r4 += r2;
    cout << "r1 += r2 = " << r4 << endl;
    
    cout << "\nConversion to double:" << endl;
    cout << "r1 as double: " << static_cast<double>(r1) << endl;
    
    return 0;
}
```

---

## 📊 Operator Overloading Summary

| Operator Category | Examples | Common Usage |
|-------------------|----------|--------------|
| **Arithmetic** | `+`, `-`, `*`, `/`, `%` | Mathematical operations |
| **Comparison** | `==`, `!=`, `<`, `>`, `<=`, `>=` | Ordering and equality |
| **Assignment** | `=`, `+=`, `-=`, `*=`, `/=` | Assignment and compound ops |
| **Increment/Decrement** | `++`, `--` | Iterators, counters |
| **Subscript** | `[]` | Container access |
| **Function Call** | `()` | Functors, accumulators |
| **Stream** | `<<`, `>>` | I/O operations |

---

## ✅ Best Practices

1. **Maintain natural semantics** - Operators should behave as expected
2. **Return references for assignment** - Enable chaining (`a = b = c`)
3. **Implement comparison operators** together for consistency
4. **Use friend functions** for symmetric operators (like `+`)
5. **Provide both member and non-member** versions when appropriate
6. **Mark appropriate operators as `const`** when they don't modify object

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Not returning `*this`** | Cannot chain assignments | Return `*this` from assignment |
| **Forgetting const** | Cannot use on const objects | Add `const` where appropriate |
| **Ambiguous operators** | Compiler errors | Choose member vs non-member carefully |
| **Not handling self-assignment** | Memory corruption | Check `if (this != &other)` |

---

## ✅ Key Takeaways

1. **Operator overloading** makes user-defined types behave like built-ins
2. **Member vs non-member** - choose based on symmetry requirements
3. **Return references** for assignment operators to enable chaining
4. **Use `const`** for operators that don't modify objects
5. **Follow natural semantics** - overloaded operators should be intuitive

---
---

## Next Step

- Go to [03_Overloading_Rules.md](03_Overloading_Rules.md) to continue with Overloading Rules.
