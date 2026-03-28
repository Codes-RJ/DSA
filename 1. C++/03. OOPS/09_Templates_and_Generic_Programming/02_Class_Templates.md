# Class Templates

## 📖 Overview

Class templates allow you to create generic classes that can work with any data type. Just like function templates, class templates provide a blueprint for creating classes with type parameters, enabling code reuse and type safety without sacrificing performance.

---

## 🎯 Key Concepts

- **Template Class**: A class with one or more template parameters
- **Instantiation**: Creating a concrete class from a template
- **Type Parameters**: Placeholders for data types (`typename T`)
- **Non-type Parameters**: Compile-time constants (`int SIZE`)
- **Default Template Arguments**: Fallback types for template parameters

---

## 💻 Basic Syntax

```cpp
template <typename T>
class ClassName {
    // Class members using T
};
```

### With Multiple Parameters
```cpp
template <typename T, typename U, int N>
class ClassName {
    // Class members using T, U, and N
};
```

---

## 🔍 Detailed Explanation

### 1. **Simple Class Template**

```cpp
#include <iostream>
using namespace std;

// Basic Box class template
template <typename T>
class Box {
private:
    T content;
    
public:
    // Constructor
    Box(T value) : content(value) {}
    
    // Getter
    T getContent() const { return content; }
    
    // Setter
    void setContent(T value) { content = value; }
    
    // Display method
    void display() const {
        cout << "Box contains: " << content << endl;
    }
};

int main() {
    // Create boxes with different types
    Box<int> intBox(42);
    Box<string> stringBox("Hello Templates");
    Box<double> doubleBox(3.14159);
    
    // Use the boxes
    intBox.display();
    stringBox.display();
    doubleBox.display();
    
    // Modify content
    intBox.setContent(100);
    stringBox.setContent("Modified Content");
    
    cout << "\nAfter modification:" << endl;
    intBox.display();
    stringBox.display();
    
    return 0;
}
```

### 2. **Class Template with Multiple Type Parameters**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Pair class template with two type parameters
template <typename T, typename U>
class Pair {
private:
    T first;
    U second;
    
public:
    Pair(T f, U s) : first(f), second(s) {}
    
    T getFirst() const { return first; }
    U getSecond() const { return second; }
    
    void setFirst(T f) { first = f; }
    void setSecond(U s) { second = s; }
    
    void display() const {
        cout << "Pair[" << first << ", " << second << "]" << endl;
    }
};

// Triple class template with three type parameters
template <typename T, typename U, typename V>
class Triple {
private:
    T first;
    U second;
    V third;
    
public:
    Triple(T f, U s, V t) : first(f), second(s), third(t) {}
    
    void display() const {
        cout << "Triple[" << first << ", " << second << ", " << third << "]" << endl;
    }
    
    // Method returning a pair
    Pair<T, U> getFirstTwo() const {
        return Pair<T, U>(first, second);
    }
};

int main() {
    // Pair with different type combinations
    Pair<int, string> p1(42, "Answer");
    Pair<string, double> p2("Pi", 3.14159);
    Pair<char, bool> p3('A', true);
    
    p1.display();
    p2.display();
    p3.display();
    
    cout << endl;
    
    // Triple example
    Triple<int, string, double> t1(100, "Hundred", 100.0);
    t1.display();
    
    Pair<int, string> firstTwo = t1.getFirstTwo();
    cout << "First two: ";
    firstTwo.display();
    
    return 0;
}
```

### 3. **Class Template with Non-type Parameters**

```cpp
#include <iostream>
#include <stdexcept>
using namespace std;

// Array class template with non-type parameter
template <typename T, int SIZE>
class FixedArray {
private:
    T data[SIZE];
    
public:
    // Default constructor
    FixedArray() {
        for (int i = 0; i < SIZE; i++) {
            data[i] = T{};
        }
    }
    
    // Constructor with initial value
    FixedArray(const T& initialValue) {
        for (int i = 0; i < SIZE; i++) {
            data[i] = initialValue;
        }
    }
    
    // Subscript operator
    T& operator[](int index) {
        if (index < 0 || index >= SIZE) {
            throw out_of_range("Index out of bounds");
        }
        return data[index];
    }
    
    // Const version of subscript operator
    const T& operator[](int index) const {
        if (index < 0 || index >= SIZE) {
            throw out_of_range("Index out of bounds");
        }
        return data[index];
    }
    
    // Get size
    int getSize() const { return SIZE; }
    
    // Display array
    void display() const {
        cout << "[";
        for (int i = 0; i < SIZE; i++) {
            cout << data[i];
            if (i < SIZE - 1) cout << ", ";
        }
        cout << "]" << endl;
    }
    
    // Fill array with value
    void fill(const T& value) {
        for (int i = 0; i < SIZE; i++) {
            data[i] = value;
        }
    }
};

// Matrix class template with two non-type parameters
template <typename T, int ROWS, int COLS>
class Matrix {
private:
    T data[ROWS][COLS];
    
public:
    Matrix() {
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                data[i][j] = T{};
            }
        }
    }
    
    T& operator()(int row, int col) {
        if (row < 0 || row >= ROWS || col < 0 || col >= COLS) {
            throw out_of_range("Matrix index out of bounds");
        }
        return data[row][col];
    }
    
    const T& operator()(int row, int col) const {
        if (row < 0 || row >= ROWS || col < 0 || col >= COLS) {
            throw out_of_range("Matrix index out of bounds");
        }
        return data[row][col];
    }
    
    void display() const {
        for (int i = 0; i < ROWS; i++) {
            cout << "[";
            for (int j = 0; j < COLS; j++) {
                cout << data[i][j];
                if (j < COLS - 1) cout << ", ";
            }
            cout << "]" << endl;
        }
    }
    
    int getRows() const { return ROWS; }
    int getCols() const { return COLS; }
};

int main() {
    // FixedArray with different sizes and types
    FixedArray<int, 5> intArray;
    FixedArray<string, 3> strArray("Empty");
    
    // Set values
    for (int i = 0; i < 5; i++) {
        intArray[i] = i * 10;
    }
    
    strArray[0] = "First";
    strArray[1] = "Second";
    strArray[2] = "Third";
    
    cout << "Integer array (size 5): ";
    intArray.display();
    
    cout << "String array (size 3): ";
    strArray.display();
    
    cout << endl;
    
    // Matrix example
    Matrix<int, 3, 3> intMatrix;
    
    // Fill matrix with values
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            intMatrix(i, j) = i * 3 + j + 1;
        }
    }
    
    cout << "3x3 Integer Matrix:" << endl;
    intMatrix.display();
    
    // Access specific element
    cout << "Element at (1,2): " << intMatrix(1, 2) << endl;
    
    return 0;
}
```

### 4. **Stack Class Template**

```cpp
#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;

// Generic Stack class template
template <typename T>
class Stack {
private:
    vector<T> items;
    
public:
    // Push item onto stack
    void push(const T& item) {
        items.push_back(item);
    }
    
    // Push item using move semantics
    void push(T&& item) {
        items.push_back(move(item));
    }
    
    // Pop item from stack
    T pop() {
        if (isEmpty()) {
            throw runtime_error("Stack is empty");
        }
        T top = items.back();
        items.pop_back();
        return top;
    }
    
    // Get top item without removing
    T& top() {
        if (isEmpty()) {
            throw runtime_error("Stack is empty");
        }
        return items.back();
    }
    
    // Get top item (const version)
    const T& top() const {
        if (isEmpty()) {
            throw runtime_error("Stack is empty");
        }
        return items.back();
    }
    
    // Check if stack is empty
    bool isEmpty() const {
        return items.empty();
    }
    
    // Get stack size
    size_t size() const {
        return items.size();
    }
    
    // Clear stack
    void clear() {
        items.clear();
    }
    
    // Display stack contents
    void display() const {
        if (isEmpty()) {
            cout << "Stack is empty" << endl;
            return;
        }
        
        cout << "Stack (top -> bottom): ";
        for (auto it = items.rbegin(); it != items.rend(); ++it) {
            cout << *it;
            if (it + 1 != items.rend()) cout << " -> ";
        }
        cout << endl;
    }
};

int main() {
    cout << "=== Stack Template Demo ===" << endl;
    
    // Stack with integers
    Stack<int> intStack;
    intStack.push(10);
    intStack.push(20);
    intStack.push(30);
    
    cout << "Integer stack:" << endl;
    intStack.display();
    cout << "Top element: " << intStack.top() << endl;
    cout << "Stack size: " << intStack.size() << endl;
    
    cout << "\nPopping elements:" << endl;
    while (!intStack.isEmpty()) {
        cout << "Popped: " << intStack.pop() << endl;
    }
    
    cout << "\n";
    
    // Stack with strings
    Stack<string> stringStack;
    stringStack.push("First");
    stringStack.push("Second");
    stringStack.push("Third");
    
    cout << "String stack:" << endl;
    stringStack.display();
    
    cout << "\nPopping: " << stringStack.pop() << endl;
    cout << "New top: " << stringStack.top() << endl;
    
    cout << "\n";
    
    // Stack with custom objects
    Stack<pair<int, string>> pairStack;
    pairStack.push({1, "One"});
    pairStack.push({2, "Two"});
    pairStack.push({3, "Three"});
    
    cout << "Pair stack:" << endl;
    pairStack.display();
    
    return 0;
}
```

### 5. **Template Class with Default Parameters**

```cpp
#include <iostream>
#include <memory>
using namespace std;

// Smart pointer class template with default deleter
template <typename T, typename Deleter = default_delete<T>>
class SmartPointer {
private:
    T* ptr;
    Deleter deleter;
    
public:
    // Constructor
    explicit SmartPointer(T* p = nullptr) : ptr(p) {}
    
    // Destructor
    ~SmartPointer() {
        if (ptr) {
            deleter(ptr);
        }
    }
    
    // Copy constructor (deleted for unique ownership)
    SmartPointer(const SmartPointer&) = delete;
    SmartPointer& operator=(const SmartPointer&) = delete;
    
    // Move constructor
    SmartPointer(SmartPointer&& other) noexcept : ptr(other.ptr), deleter(move(other.deleter)) {
        other.ptr = nullptr;
    }
    
    // Move assignment
    SmartPointer& operator=(SmartPointer&& other) noexcept {
        if (this != &other) {
            if (ptr) {
                deleter(ptr);
            }
            ptr = other.ptr;
            deleter = move(other.deleter);
            other.ptr = nullptr;
        }
        return *this;
    }
    
    // Dereference operators
    T& operator*() const { return *ptr; }
    T* operator->() const { return ptr; }
    
    // Get raw pointer
    T* get() const { return ptr; }
    
    // Check if pointer is valid
    explicit operator bool() const { return ptr != nullptr; }
    
    // Reset pointer
    void reset(T* p = nullptr) {
        if (ptr) {
            deleter(ptr);
        }
        ptr = p;
    }
    
    // Release ownership
    T* release() {
        T* temp = ptr;
        ptr = nullptr;
        return temp;
    }
};

// Custom deleter for arrays
template <typename T>
class ArrayDeleter {
public:
    void operator()(T* ptr) const {
        delete[] ptr;
    }
};

int main() {
    cout << "=== Smart Pointer Template Demo ===" << endl;
    
    // Using default deleter
    {
        SmartPointer<int> ptr1(new int(42));
        cout << "Value: " << *ptr1 << endl;
        cout << "Pointer valid: " << (ptr1 ? "Yes" : "No") << endl;
    } // ptr1 automatically deleted here
    
    // Using custom array deleter
    {
        SmartPointer<int, ArrayDeleter<int>> arrPtr(new int[5]{1, 2, 3, 4, 5});
        cout << "Array values: ";
        for (int i = 0; i < 5; i++) {
            cout << arrPtr.get()[i] << " ";
        }
        cout << endl;
    } // array automatically deleted here
    
    // Move semantics
    {
        SmartPointer<string> strPtr(new string("Hello Templates"));
        SmartPointer<string> movedPtr = move(strPtr);
        
        cout << "Moved pointer value: " << *movedPtr << endl;
        cout << "Original pointer valid: " << (strPtr ? "Yes" : "No") << endl;
        cout << "Moved pointer valid: " << (movedPtr ? "Yes" : "No") << endl;
    }
    
    return 0;
}
```

---

## 🎮 Complete Example: Generic Container Library

```cpp
#include <iostream>
#include <stdexcept>
#include <algorithm>
using namespace std;

// Generic List class template
template <typename T>
class List {
private:
    struct Node {
        T data;
        Node* next;
        Node(const T& value) : data(value), next(nullptr) {}
    };
    
    Node* head;
    Node* tail;
    size_t count;
    
public:
    List() : head(nullptr), tail(nullptr), count(0) {}
    
    ~List() {
        clear();
    }
    
    // Copy constructor
    List(const List& other) : head(nullptr), tail(nullptr), count(0) {
        Node* current = other.head;
        while (current) {
            pushBack(current->data);
            current = current->next;
        }
    }
    
    // Assignment operator
    List& operator=(const List& other) {
        if (this != &other) {
            clear();
            Node* current = other.head;
            while (current) {
                pushBack(current->data);
                current = current->next;
            }
        }
        return *this;
    }
    
    void pushFront(const T& value) {
        Node* newNode = new Node(value);
        if (!head) {
            head = tail = newNode;
        } else {
            newNode->next = head;
            head = newNode;
        }
        count++;
    }
    
    void pushBack(const T& value) {
        Node* newNode = new Node(value);
        if (!head) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
        count++;
    }
    
    T popFront() {
        if (!head) {
            throw runtime_error("List is empty");
        }
        
        Node* temp = head;
        T value = temp->data;
        head = head->next;
        
        if (!head) {
            tail = nullptr;
        }
        
        delete temp;
        count--;
        return value;
    }
    
    T popBack() {
        if (!head) {
            throw runtime_error("List is empty");
        }
        
        T value;
        if (head == tail) {
            value = head->data;
            delete head;
            head = tail = nullptr;
        } else {
            Node* current = head;
            while (current->next != tail) {
                current = current->next;
            }
            value = tail->data;
            delete tail;
            tail = current;
            tail->next = nullptr;
        }
        
        count--;
        return value;
    }
    
    bool isEmpty() const { return count == 0; }
    size_t size() const { return count; }
    
    void clear() {
        while (!isEmpty()) {
            popFront();
        }
    }
    
    void display() const {
        if (isEmpty()) {
            cout << "List is empty" << endl;
            return;
        }
        
        cout << "List: ";
        Node* current = head;
        while (current) {
            cout << current->data;
            if (current->next) cout << " -> ";
            current = current->next;
        }
        cout << endl;
    }
    
    // Iterator class for range-based for loops
    class Iterator {
    private:
        Node* current;
        
    public:
        Iterator(Node* node) : current(node) {}
        
        T& operator*() { return current->data; }
        const T& operator*() const { return current->data; }
        
        Iterator& operator++() {
            current = current->next;
            return *this;
        }
        
        bool operator!=(const Iterator& other) const {
            return current != other.current;
        }
    };
    
    Iterator begin() { return Iterator(head); }
    Iterator end() { return Iterator(nullptr); }
};

int main() {
    cout << "=== Generic List Container Demo ===" << endl;
    
    // List with integers
    List<int> intList;
    intList.pushBack(10);
    intList.pushBack(20);
    intList.pushBack(30);
    intList.pushFront(5);
    
    cout << "Integer list:" << endl;
    intList.display();
    cout << "Size: " << intList.size() << endl;
    
    cout << "\nPopping from front: " << intList.popFront() << endl;
    intList.display();
    
    cout << "\nPopping from back: " << intList.popBack() << endl;
    intList.display();
    
    // Range-based for loop
    cout << "\nUsing range-based for loop:" << endl;
    for (int value : intList) {
        cout << value << " ";
    }
    cout << endl;
    
    cout << "\n";
    
    // List with strings
    List<string> stringList;
    stringList.pushBack("First");
    stringList.pushBack("Second");
    stringList.pushBack("Third");
    stringList.pushFront("Zero");
    
    cout << "String list:" << endl;
    stringList.display();
    
    // Copy constructor test
    List<string> copyList = stringList;
    cout << "\nCopied list:" << endl;
    copyList.display();
    
    // Modify original
    stringList.popFront();
    cout << "\nOriginal after pop:" << endl;
    stringList.display();
    cout << "Copy remains unchanged:" << endl;
    copyList.display();
    
    return 0;
}
```

---

## ⚡ Performance Considerations

### Advantages
- ✅ **Zero Runtime Overhead**: Templates generate optimized code
- ✅ **Type Safety**: Compile-time type checking
- ✅ **Code Reuse**: Single implementation for multiple types
- ✅ **Inlining**: Template methods are often inlined

### Considerations
- ⚠️ **Code Bloat**: Each instantiation generates separate code
- ⚠️ **Compilation Time**: Longer build times
- ⚠️ **Binary Size**: Increased executable size

---

## 🐛 Common Pitfalls

| Problem | Solution |
|---------|----------|
| **Template definition in .cpp file** | Move definition to header file |
| **Missing template arguments** | Provide default template parameters |
| **Linker errors** | Ensure template is visible to all translation units |
| **Circular dependencies** | Use forward declarations and proper includes |

---

## ✅ Best Practices

1. **Use meaningful template parameter names**
2. **Provide default template arguments** when appropriate
3. **Implement rule of three/five/zero** for template classes
4. **Use `const` correctness** throughout the class
5. **Consider move semantics** for performance
6. **Document template requirements** and constraints
7. **Use `static_assert`** for better error messages

---

## 📚 Related Topics

- [Function Templates](01_Function_Templates.md)
- [Template Specialization](03_Template_Specialization.md)
- [Variadic Templates](04_Variadic_Templates.md)
- [STL Containers](../11_Memory_Management_in_OOP/05_Smart_Pointers_Intro.md)

---

## 🚀 Next Steps

Continue learning about:
- **Template Specialization**: Custom behavior for specific types
- **Variadic Templates**: Variable number of template arguments
- **Template Metaprogramming**: Compile-time computation
- **Advanced Template Techniques**: SFINAE, concepts, and more

---
