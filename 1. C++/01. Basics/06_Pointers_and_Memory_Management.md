# Pointers and Memory Management

## Overview
Pointers are one of C++'s most powerful features, providing direct memory access and enabling dynamic memory management. Understanding pointers is crucial for effective C++ programming and data structure implementation.

## Pointer Fundamentals

### 1. Basic Pointer Concepts

#### Pointer Declaration and Initialization
```cpp
int main() {
    int variable = 42;
    int* ptr;           // Declare pointer
    ptr = &variable;    // Initialize with address
    
    std::cout << "Variable value: " << variable << std::endl;
    std::cout << "Variable address: " << &variable << std::endl;
    std::cout << "Pointer value: " << ptr << std::endl;
    std::cout << "Pointer address: " << &ptr << std::endl;
    std::cout << "Dereferenced pointer: " << *ptr << std::endl;
    
    return 0;
}
```

#### Pointer Types and Size
```cpp
int main() {
    int* intPtr;
    double* doublePtr;
    char* charPtr;
    void* voidPtr;
    
    std::cout << "Size of int pointer: " << sizeof(intPtr) << " bytes" << std::endl;
    std::cout << "Size of double pointer: " << sizeof(doublePtr) << " bytes" << std::endl;
    std::cout << "Size of char pointer: " << sizeof(charPtr) << " bytes" << std::endl;
    std::cout << "Size of void pointer: " << sizeof(voidPtr) << " bytes" << std::endl;
    
    // All pointers have the same size on a given architecture
    return 0;
}
```

### 2. Pointer Operations

#### Dereferencing and Assignment
```cpp
void demonstrateOperations() {
    int a = 10, b = 20;
    int* ptr = &a;
    
    // Dereferencing
    std::cout << "*ptr = " << *ptr << std::endl;  // 10
    
    // Modifying through pointer
    *ptr = 15;
    std::cout << "a = " << a << std::endl;  // 15
    
    // Pointer reassignment
    ptr = &b;
    std::cout << "*ptr = " << *ptr << std::endl;  // 20
    
    // Pointer arithmetic
    ptr++;  // Moves to next memory location (dangerous here)
}
```

#### Pointer Arithmetic
```cpp
void pointerArithmetic() {
    int arr[] = {10, 20, 30, 40, 50};
    int* ptr = arr;
    
    std::cout << "First element: " << *ptr << std::endl;      // 10
    std::cout << "Second element: " << *(ptr + 1) << std::endl; // 20
    
    ptr += 2;  // Move pointer by 2 elements
    std::cout << "Third element: " << *ptr << std::endl;      // 30
    
    // Pointer difference
    int* start = arr;
    int* end = arr + 5;
    std::cout << "Array size: " << (end - start) << std::endl; // 5
}
```

## Dynamic Memory Management

### 1. new and delete Operators

#### Single Object Allocation
```cpp
void singleObjectAllocation() {
    // Allocate single integer
    int* ptr = new int(42);
    std::cout << "Value: " << *ptr << std::endl;
    
    // Don't forget to deallocate
    delete ptr;
    ptr = nullptr;  // Avoid dangling pointer
    
    // Allocate without initialization
    int* ptr2 = new int;
    *ptr2 = 100;
    std::cout << "Value: " << *ptr2 << std::endl;
    delete ptr2;
    ptr2 = nullptr;
}
```

#### Array Allocation
```cpp
void arrayAllocation() {
    // Allocate array of integers
    int size = 5;
    int* arr = new int[size];
    
    // Initialize array
    for (int i = 0; i < size; i++) {
        arr[i] = i * 10;
    }
    
    // Print array
    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    
    // Deallocate array
    delete[] arr;
    arr = nullptr;
}
```

### 2. Memory Allocation Examples

#### Dynamic 2D Array
```cpp
int** create2DArray(int rows, int cols) {
    // Allocate array of pointers
    int** matrix = new int*[rows];
    
    // Allocate each row
    for (int i = 0; i < rows; i++) {
        matrix[i] = new int[cols];
    }
    
    // Initialize
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = i * cols + j;
        }
    }
    
    return matrix;
}

void delete2DArray(int** matrix, int rows) {
    // Delete each row
    for (int i = 0; i < rows; i++) {
        delete[] matrix[i];
    }
    
    // Delete array of pointers
    delete[] matrix;
}

void demonstrate2DArray() {
    int rows = 3, cols = 4;
    int** matrix = create2DArray(rows, cols);
    
    // Print matrix
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
    
    delete2DArray(matrix, rows);
}
```

## Smart Pointers (C++11 and later)

### 1. unique_ptr

#### Basic Usage
```cpp
#include <memory>

void uniquePtrExample() {
    // Create unique_ptr
    std::unique_ptr<int> ptr = std::make_unique<int>(42);
    std::cout << "Value: " << *ptr << std::endl;
    
    // Automatic cleanup when ptr goes out of scope
    
    // unique_ptr with custom deleter
    auto deleter = [](int* p) {
        std::cout << "Custom deleter called" << std::endl;
        delete p;
    };
    
    std::unique_ptr<int, decltype(deleter)> customPtr(new int(100), deleter);
}
```

#### unique_ptr with Arrays
```cpp
void uniquePtrArray() {
    // Create unique_ptr for array
    std::unique_ptr<int[]> arr = std::make_unique<int[]>(5);
    
    // Initialize array
    for (int i = 0; i < 5; i++) {
        arr[i] = i * 10;
    }
    
    // Print array
    for (int i = 0; i < 5; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    
    // Automatic cleanup
}
```

### 2. shared_ptr

#### Basic Usage
```cpp
void sharedPtrExample() {
    // Create shared_ptr
    std::shared_ptr<int> ptr1 = std::make_shared<int>(42);
    std::cout << "Value: " << *ptr1 << std::endl;
    std::cout << "Use count: " << ptr1.use_count() << std::endl; // 1
    
    {
        std::shared_ptr<int> ptr2 = ptr1;  // Share ownership
        std::cout << "Use count: " << ptr1.use_count() << std::endl; // 2
        std::cout << "Use count: " << ptr2.use_count() << std::endl; // 2
    }
    
    std::cout << "Use count after ptr2 destruction: " << ptr1.use_count() << std::endl; // 1
}
```

#### shared_ptr with Custom Objects
```cpp
class MyClass {
private:
    std::string name;
public:
    MyClass(const std::string& n) : name(n) {
        std::cout << "Constructor: " << name << std::endl;
    }
    
    ~MyClass() {
        std::cout << "Destructor: " << name << std::endl;
    }
    
    void sayHello() {
        std::cout << "Hello from " << name << std::endl;
    }
};

void sharedPtrWithObjects() {
    auto obj1 = std::make_shared<MyClass>("Object1");
    auto obj2 = std::make_shared<MyClass>("Object2");
    
    obj1->sayHello();
    obj2->sayHello();
    
    // Objects are automatically destroyed when last shared_ptr is destroyed
}
```

### 3. weak_ptr

#### Breaking Circular References
```cpp
class Node {
public:
    std::string name;
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;  // Use weak_ptr to avoid circular reference
    
    Node(const std::string& n) : name(n) {
        std::cout << "Node created: " << name << std::endl;
    }
    
    ~Node() {
        std::cout << "Node destroyed: " << name << std::endl;
    }
};

void weakPtrExample() {
    auto node1 = std::make_shared<Node>("Node1");
    auto node2 = std::make_shared<Node>("Node2");
    
    node1->next = node2;
    node2->prev = node1;  // weak_ptr doesn't increase reference count
    
    std::cout << "Node1 use count: " << node1.use_count() << std::endl; // 1
    std::cout << "Node2 use count: " << node2.use_count() << std::endl; // 2
    
    // Check if weak_ptr is still valid
    if (auto locked = node2->prev.lock()) {
        std::cout << "Previous node: " << locked->name << std::endl;
    }
}
```

## References

### 1. L-value References

#### Basic Reference Usage
```cpp
void referenceExample() {
    int value = 42;
    int& ref = value;  // Reference to value
    
    std::cout << "Value: " << value << std::endl;    // 42
    std::cout << "Reference: " << ref << std::endl;  // 42
    
    ref = 100;  // Modifies original value
    std::cout << "Value after modification: " << value << std::endl; // 100
    
    int& anotherRef = ref;  // Reference to reference (still refers to value)
    anotherRef = 200;
    std::cout << "Value: " << value << std::endl;    // 200
}
```

#### References as Function Parameters
```cpp
void swapValues(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

void modifyValue(int& value) {
    value *= 2;  // Modifies original variable
}

void referenceParameters() {
    int x = 10, y = 20;
    std::cout << "Before swap: x=" << x << ", y=" << y << std::endl;
    swapValues(x, y);
    std::cout << "After swap: x=" << x << ", y=" << y << std::endl;
    
    int num = 5;
    std::cout << "Before modification: " << num << std::endl;
    modifyValue(num);
    std::cout << "After modification: " << num << std::endl;
}
```

### 2. const References

#### const Reference Parameters
```cpp
void printValue(const int& value) {
    std::cout << "Value: " << value << std::endl;
    // value = 100;  // Error: cannot modify const reference
}

void processLargeObject(const std::vector<int>& largeVec) {
    std::cout << "Vector size: " << largeVec.size() << std::endl;
    // Efficient: no copy made
}

void constReferenceExample() {
    int value = 42;
    printValue(value);
    
    std::vector<int> largeVector(1000000, 42);
    processLargeObject(largeVector);
}
```

### 3. R-value References (C++11)

#### Move Semantics
```cpp
class BigObject {
private:
    int* data;
    size_t size;
public:
    BigObject(size_t s) : size(s) {
        data = new int[size];
        std::cout << "Constructor" << std::endl;
    }
    
    // Copy constructor
    BigObject(const BigObject& other) : size(other.size) {
        data = new int[size];
        std::copy(other.data, other.data + size, data);
        std::cout << "Copy constructor" << std::endl;
    }
    
    // Move constructor
    BigObject(BigObject&& other) noexcept : data(other.data), size(other.size) {
        other.data = nullptr;
        other.size = 0;
        std::cout << "Move constructor" << std::endl;
    }
    
    ~BigObject() {
        delete[] data;
        std::cout << "Destructor" << std::endl;
    }
};

BigObject createBigObject() {
    BigObject obj(1000);
    return obj;  // Move constructor called
}

void moveSemanticsExample() {
    BigObject obj1 = createBigObject();  // Move constructor
    BigObject obj2 = std::move(obj1);   // Move constructor
}
```

## Memory Management Best Practices

### 1. RAII (Resource Acquisition Is Initialization)

#### RAII Class Example
```cpp
class FileHandler {
private:
    FILE* file;
public:
    FileHandler(const char* filename, const char* mode) {
        file = fopen(filename, mode);
        if (!file) {
            throw std::runtime_error("Failed to open file");
        }
    }
    
    ~FileHandler() {
        if (file) {
            fclose(file);
        }
    }
    
    // Prevent copying
    FileHandler(const FileHandler&) = delete;
    FileHandler& operator=(const FileHandler&) = delete;
    
    // Allow moving
    FileHandler(FileHandler&& other) noexcept : file(other.file) {
        other.file = nullptr;
    }
    
    FILE* get() { return file; }
};

void raiiExample() {
    FileHandler file("example.txt", "w");
    // File is automatically closed when file goes out of scope
    fprintf(file.get(), "Hello, RAII!");
}
```

### 2. Smart Pointer Guidelines

#### When to Use Each Smart Pointer
```cpp
void smartPointerGuidelines() {
    // Use unique_ptr when:
    // - You need exclusive ownership
    // - You want automatic cleanup
    // - You want to transfer ownership
    
    std::unique_ptr<MyClass> unique = std::make_unique<MyClass>("Unique");
    
    // Use shared_ptr when:
    // - Multiple owners need access
    // - You need shared ownership
    // - Lifetime is complex to determine
    
    std::shared_ptr<MyClass> shared = std::make_shared<MyClass>("Shared");
    
    // Use weak_ptr when:
    // - You need to observe shared_ptr without ownership
    // - Breaking circular references
    // - Caching weak references
    
    std::weak_ptr<MyClass> weak = shared;
}
```

## Common Pitfalls and Solutions

### 1. Dangling Pointers
```cpp
// Wrong: Dangling pointer
int* danglingPointer() {
    int local = 42;
    return &local;  // Error: returning address of local variable
}

// Correct: Use static or dynamic allocation
int* validPointer() {
    static int local = 42;  // Static storage
    return &local;
}

// Better: Use smart pointers
std::unique_ptr<int> smartPointer() {
    return std::make_unique<int>(42);
}
```

### 2. Memory Leaks
```cpp
// Wrong: Memory leak
void memoryLeak() {
    int* ptr = new int(42);
    // Forgot to delete ptr
}

// Correct: Always delete
void noLeak() {
    int* ptr = new int(42);
    delete ptr;
    ptr = nullptr;
}

// Better: Use RAII
void automaticCleanup() {
    auto ptr = std::make_unique<int>(42);
    // Automatic cleanup
}
```

### 3. Double Delete
```cpp
// Wrong: Double delete
void doubleDelete() {
    int* ptr = new int(42);
    delete ptr;
    delete ptr;  // Error: double delete
}

// Correct: Set to nullptr after delete
void safeDelete() {
    int* ptr = new int(42);
    delete ptr;
    ptr = nullptr;
    if (ptr) {
        delete ptr;  // Safe: won't execute
    }
}
```

## Advanced Pointer Techniques

### 1. Function Pointers
```cpp
int add(int a, int b) { return a + b; }
int multiply(int a, int b) { return a * b; }

int operation(int a, int b, int (*op)(int, int)) {
    return op(a, b);
}

void functionPointerExample() {
    int result1 = operation(5, 3, add);       // 8
    int result2 = operation(5, 3, multiply); // 15
    
    std::cout << "Add: " << result1 << ", Multiply: " << result2 << std::endl;
}
```

### 2. Pointer to Member
```cpp
class MyClass {
public:
    int value;
    
    MyClass(int v) : value(v) {}
    
    int getValue() const { return value; }
    void setValue(int v) { value = v; }
};

void pointerToMemberExample() {
    MyClass obj(42);
    
    // Pointer to data member
    int MyClass::* memberPtr = &MyClass::value;
    std::cout << "Value: " << obj.*memberPtr << std::endl;
    
    // Pointer to member function
    int (MyClass::* methodPtr)() const = &MyClass::getValue;
    std::cout << "Method result: " << (obj.*methodPtr)() << std::endl;
}
```

---

*This guide provides a comprehensive overview of pointers and memory management in C++, covering fundamental concepts, smart pointers, and best practices for safe and efficient memory usage.*

---

## Next Step

- Go to [07_Error_Handling.md](07_Error%20Handling.md) to continue with Error Handling.