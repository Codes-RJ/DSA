# 02_Class_Templates.md

## Class Templates in C++

### Overview

Class templates allow creating a single class definition that works with multiple data types. Instead of writing separate classes for `int`, `double`, `string`, etc., you write one template class, and the compiler generates the appropriate version for each type used. Class templates are the foundation of container classes like `vector`, `list`, `map`, and `stack` in the C++ Standard Library.

---

### What is a Class Template?

A class template is a blueprint for creating classes. It defines a family of classes that differ only by the types of their data members or the types they operate on. When you instantiate a class template, the compiler generates a concrete class for the specified type.

**Syntax:**
```cpp
template <typename T>
class ClassName {
private:
    T data_;
    
public:
    ClassName(T value);
    T getData() const;
    void setData(T value);
};
```

**Key Components:**

| Component | Description | Example |
|-----------|-------------|---------|
| `template <typename T>` | Template parameter declaration | `template <typename T>` |
| `typename` or `class` | Keyword indicating a type parameter | `typename T` or `class T` |
| `T` | Template parameter name (placeholder for type) | Any valid identifier |
| Class body | Uses `T` as a regular type | `T data_;` |

---

### Basic Class Template Example

This example demonstrates a simple class template that stores a value of any type.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Class template definition
template <typename T>
class Box {
private:
    T content_;
    
public:
    // Constructor
    Box(T content) : content_(content) {
        cout << "Box created with content of type: " << typeid(T).name() << endl;
    }
    
    // Getter
    T getContent() const {
        return content_;
    }
    
    // Setter
    void setContent(T content) {
        content_ = content;
    }
    
    // Display function
    void display() const {
        cout << "Box contains: " << content_ << endl;
    }
};

int main() {
    // Box for integers
    Box<int> intBox(42);
    intBox.display();
    cout << "Value: " << intBox.getContent() << endl;
    
    // Box for doubles
    Box<double> doubleBox(3.14159);
    doubleBox.display();
    
    // Box for strings
    Box<string> stringBox("Hello, World!");
    stringBox.display();
    
    // Box for char
    Box<char> charBox('A');
    charBox.display();
    
    // Modifying content
    intBox.setContent(100);
    cout << "After modification: ";
    intBox.display();
    
    return 0;
}
```

**Output:**
```
Box created with content of type: i
Box contains: 42
Value: 42
Box created with content of type: d
Box contains: 3.14159
Box created with content of type: NSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
Box contains: Hello, World!
Box created with content of type: c
Box contains: A
After modification: Box contains: 100
```

---

### Member Function Definitions Outside the Class

Member functions of a class template can be defined outside the class body.

```cpp
#include <iostream>
using namespace std;

template <typename T>
class Calculator {
private:
    T value_;
    
public:
    // Constructor
    Calculator(T value);
    
    // Member functions declared inside, defined outside
    T add(T other) const;
    T subtract(T other) const;
    T multiply(T other) const;
    T divide(T other) const;
    void display() const;
};

// Member function definitions outside the class
template <typename T>
Calculator<T>::Calculator(T value) : value_(value) { }

template <typename T>
T Calculator<T>::add(T other) const {
    return value_ + other;
}

template <typename T>
T Calculator<T>::subtract(T other) const {
    return value_ - other;
}

template <typename T>
T Calculator<T>::multiply(T other) const {
    return value_ * other;
}

template <typename T>
T Calculator<T>::divide(T other) const {
    if (other != 0) {
        return value_ / other;
    }
    cout << "Error: Division by zero!" << endl;
    return 0;
}

template <typename T>
void Calculator<T>::display() const {
    cout << "Calculator value: " << value_ << endl;
}

int main() {
    Calculator<int> intCalc(10);
    intCalc.display();
    cout << "Add 5: " << intCalc.add(5) << endl;
    cout << "Subtract 3: " << intCalc.subtract(3) << endl;
    cout << "Multiply by 2: " << intCalc.multiply(2) << endl;
    cout << "Divide by 4: " << intCalc.divide(4) << endl;
    
    Calculator<double> doubleCalc(3.14);
    doubleCalc.display();
    cout << "Add 2.71: " << doubleCalc.add(2.71) << endl;
    
    return 0;
}
```

**Output:**
```
Calculator value: 10
Add 5: 15
Subtract 3: 7
Multiply by 2: 20
Divide by 4: 2
Calculator value: 3.14
Add 2.71: 5.85
```

---

### Class Template with Multiple Type Parameters

Class templates can have multiple type parameters.

```cpp
#include <iostream>
#include <utility>
using namespace std;

// Class template with two type parameters
template <typename T1, typename T2>
class Pair {
private:
    T1 first_;
    T2 second_;
    
public:
    Pair(T1 first, T2 second) : first_(first), second_(second) { }
    
    T1 getFirst() const { return first_; }
    T2 getSecond() const { return second_; }
    
    void setFirst(T1 first) { first_ = first; }
    void setSecond(T2 second) { second_ = second; }
    
    void display() const {
        cout << "(" << first_ << ", " << second_ << ")" << endl;
    }
    
    // Swap the pair (swap first and second)
    Pair<T2, T1> swap() const {
        return Pair<T2, T1>(second_, first_);
    }
};

int main() {
    // Different type combinations
    Pair<int, double> p1(10, 3.14);
    cout << "Integer-Double pair: ";
    p1.display();
    
    Pair<string, int> p2("Age", 25);
    cout << "String-Integer pair: ";
    p2.display();
    
    Pair<char, bool> p3('A', true);
    cout << "Character-Boolean pair: ";
    p3.display();
    
    // Using the swap function
    Pair<double, int> swapped = p1.swap();
    cout << "Swapped pair: ";
    swapped.display();
    
    return 0;
}
```

**Output:**
```
Integer-Double pair: (10, 3.14)
String-Integer pair: (Age, 25)
Character-Boolean pair: (A, 1)
Swapped pair: (3.14, 10)
```

---

### Non-Type Template Parameters in Classes

Class templates can also accept non-type parameters (compile-time constants).

```cpp
#include <iostream>
using namespace std;

// Class template with non-type parameter
template <typename T, int capacity>
class StaticArray {
private:
    T data_[capacity];
    int size_;
    
public:
    StaticArray() : size_(0) { }
    
    bool push(const T& value) {
        if (size_ < capacity) {
            data_[size_++] = value;
            return true;
        }
        return false;
    }
    
    T pop() {
        if (size_ > 0) {
            return data_[--size_];
        }
        throw out_of_range("Array is empty");
    }
    
    T get(int index) const {
        if (index >= 0 && index < size_) {
            return data_[index];
        }
        throw out_of_range("Index out of bounds");
    }
    
    int size() const { return size_; }
    int capacity() const { return capacity; }
    
    void display() const {
        cout << "[";
        for (int i = 0; i < size_; i++) {
            cout << data_[i];
            if (i < size_ - 1) cout << ", ";
        }
        cout << "]" << endl;
    }
};

int main() {
    // Different capacities create different types
    StaticArray<int, 5> smallArray;
    StaticArray<int, 10> largeArray;
    
    cout << "smallArray capacity: " << smallArray.capacity() << endl;
    cout << "largeArray capacity: " << largeArray.capacity() << endl;
    
    // Using smallArray
    for (int i = 1; i <= 5; i++) {
        smallArray.push(i * 10);
    }
    cout << "smallArray: ";
    smallArray.display();
    
    // Attempt to push beyond capacity
    if (!smallArray.push(60)) {
        cout << "Cannot push to smallArray (full)" << endl;
    }
    
    // Using different type with non-type parameter
    StaticArray<string, 3> stringArray;
    stringArray.push("Apple");
    stringArray.push("Banana");
    stringArray.push("Cherry");
    cout << "stringArray: ";
    stringArray.display();
    
    return 0;
}
```

**Output:**
```
smallArray capacity: 5
largeArray capacity: 10
smallArray: [10, 20, 30, 40, 50]
Cannot push to smallArray (full)
stringArray: [Apple, Banana, Cherry]
```

---

### Default Template Parameters

Class templates can have default values for template parameters (C++11 and later).

```cpp
#include <iostream>
#include <string>
using namespace std;

// Class template with default type parameter
template <typename T = int>
class SimpleContainer {
private:
    T value_;
    
public:
    SimpleContainer(T value = T()) : value_(value) { }
    
    T getValue() const { return value_; }
    void setValue(T value) { value_ = value; }
};

// Class template with multiple defaults
template <typename T = double, int size = 10>
class FixedArray {
private:
    T data_[size];
    int count_;
    
public:
    FixedArray() : count_(0) { }
    
    void add(const T& value) {
        if (count_ < size) {
            data_[count_++] = value;
        }
    }
    
    void display() const {
        cout << "Array (size=" << size << ", type=" << typeid(T).name() << "): ";
        for (int i = 0; i < count_; i++) {
            cout << data_[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    // Using default template parameter (int)
    SimpleContainer<> defaultContainer;
    cout << "Default container value: " << defaultContainer.getValue() << endl;
    
    // Explicit type
    SimpleContainer<string> stringContainer("Hello");
    cout << "String container value: " << stringContainer.getValue() << endl;
    
    // FixedArray with defaults (double, size=10)
    FixedArray<> defaultArray;
    defaultArray.add(3.14);
    defaultArray.add(2.71);
    defaultArray.display();
    
    // FixedArray with custom type and default size
    FixedArray<int> intArray;
    intArray.add(10);
    intArray.add(20);
    intArray.add(30);
    intArray.display();
    
    // FixedArray with custom type and custom size
    FixedArray<char, 5> charArray;
    charArray.add('A');
    charArray.add('B');
    charArray.add('C');
    charArray.display();
    
    return 0;
}
```

**Output:**
```
Default container value: 0
String container value: Hello
Array (size=10, type=d): 3.14 2.71 
Array (size=10, type=i): 10 20 30 
Array (size=5, type=c): A B C 
```

---

### Template Template Parameters

A template parameter can itself be a template (advanced feature).

```cpp
#include <iostream>
#include <vector>
#include <list>
using namespace std;

// Template template parameter
template <typename T, template <typename> class Container>
class Wrapper {
private:
    Container<T> container_;
    
public:
    void add(const T& value) {
        container_.push_back(value);
    }
    
    void display() const {
        for (const auto& item : container_) {
            cout << item << " ";
        }
        cout << endl;
    }
};

// Note: std::vector and std::list have two template parameters (type, allocator)
// Simplified example for demonstration
template <typename T>
class SimpleVector {
private:
    T data_[100];
    int size_;
    
public:
    SimpleVector() : size_(0) { }
    
    void push_back(const T& value) {
        if (size_ < 100) {
            data_[size_++] = value;
        }
    }
    
    T* begin() { return data_; }
    T* end() { return data_ + size_; }
    const T* begin() const { return data_; }
    const T* end() const { return data_ + size_; }
};

template <typename T>
class SimpleList {
    // Simplified list implementation
};

int main() {
    Wrapper<int, SimpleVector> intVector;
    intVector.add(10);
    intVector.add(20);
    intVector.add(30);
    cout << "SimpleVector contents: ";
    intVector.display();
    
    return 0;
}
```

---

### Common Class Template Examples

#### 1. Stack Class Template

```cpp
template <typename T, int maxSize = 100>
class Stack {
private:
    T data_[maxSize];
    int top_;
    
public:
    Stack() : top_(-1) { }
    
    void push(const T& value) {
        if (top_ < maxSize - 1) {
            data_[++top_] = value;
        } else {
            throw overflow_error("Stack overflow");
        }
    }
    
    T pop() {
        if (top_ >= 0) {
            return data_[top_--];
        } else {
            throw underflow_error("Stack underflow");
        }
    }
    
    T peek() const {
        if (top_ >= 0) {
            return data_[top_];
        }
        throw underflow_error("Stack is empty");
    }
    
    bool isEmpty() const { return top_ == -1; }
    bool isFull() const { return top_ == maxSize - 1; }
    int size() const { return top_ + 1; }
};
```

#### 2. Queue Class Template

```cpp
template <typename T, int maxSize = 100>
class Queue {
private:
    T data_[maxSize];
    int front_;
    int rear_;
    int count_;
    
public:
    Queue() : front_(0), rear_(-1), count_(0) { }
    
    void enqueue(const T& value) {
        if (count_ < maxSize) {
            rear_ = (rear_ + 1) % maxSize;
            data_[rear_] = value;
            count_++;
        } else {
            throw overflow_error("Queue overflow");
        }
    }
    
    T dequeue() {
        if (count_ > 0) {
            T value = data_[front_];
            front_ = (front_ + 1) % maxSize;
            count_--;
            return value;
        } else {
            throw underflow_error("Queue underflow");
        }
    }
    
    bool isEmpty() const { return count_ == 0; }
    bool isFull() const { return count_ == maxSize; }
    int size() const { return count_; }
};
```

#### 3. Pair Class Template (Like std::pair)

```cpp
template <typename T1, typename T2>
class Pair {
public:
    T1 first;
    T2 second;
    
    Pair() : first(T1()), second(T2()) { }
    Pair(const T1& a, const T2& b) : first(a), second(b) { }
    
    bool operator==(const Pair& other) const {
        return first == other.first && second == other.second;
    }
    
    bool operator<(const Pair& other) const {
        if (first != other.first) return first < other.first;
        return second < other.second;
    }
};
```

---

### Summary

| Concept | Key Point |
|---------|-----------|
| **Class Template** | Blueprint for creating classes for different types |
| **Template Parameter** | Placeholder for a type (or value) |
| **Member Function Definition** | Can be defined inside or outside the class |
| **Multiple Parameters** | Class templates can have multiple type parameters |
| **Non-Type Parameters** | Compile-time constants as template arguments |
| **Default Parameters** | Default values for template arguments (C++11) |
| **Template Template Parameters** | Templates as parameters to other templates |

---

### Key Takeaways

1. **Class templates** enable creating type-independent containers and data structures
2. **Member functions** defined outside require `template <typename T>` prefix
3. **Multiple type parameters** allow creating pairs, tuples, and complex containers
4. **Non-type parameters** enable compile-time fixed-size arrays and buffers
5. **Default template parameters** simplify usage for common cases
6. **Class templates are defined in headers** (not .cpp files)
7. **Template code is generated** at compile time for each type used

---

### Next Steps

- Go to [03_Template_Specialization.md](03_Template_Specialization.md) to understand Template Specialization.