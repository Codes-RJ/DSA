# Exception Specifications

## 📖 Overview

Exception specifications provide a way to declare which exceptions a function might throw. In modern C++, this is primarily done using the `noexcept` specifier, which replaced the older dynamic exception specification mechanism (`throw()`). Understanding exception specifications is crucial for writing exception-safe code and enabling compiler optimizations.

---

## 🎯 Key Concepts

- **noexcept Specifier**: Declares that a function won't throw exceptions
- **noexcept Operator**: Compile-time check if an expression can throw
- **Exception Safety Guarantees**: Basic, strong, and no-throw guarantees
- **Conditional noexcept**: noexcept based on template parameters or conditions
- **Deprecated throw()**: Old-style exception specifications

---

## 💻 Syntax Overview

```cpp
// Modern noexcept specifications
void function() noexcept;                    // Function promises not to throw
void function() noexcept(true);              // Explicitly promises not to throw
void function() noexcept(false);             // May throw (same as no specification)

// Conditional noexcept
template<typename T>
void function(T t) noexcept(noexcept(t.someMethod()));

// noexcept operator
bool canThrow = noexcept(function());        // Compile-time check

// Deprecated (pre-C++11)
void function() throw();                    // Deprecated: equivalent to noexcept(true)
void function() throw(ExceptionType);       // Deprecated: dynamic exception spec
```

---

## 🔍 Detailed Explanation

### 1. **Basic noexcept Usage**

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;

// Function that promises not to throw
void safeFunction() noexcept {
    cout << "This function promises not to throw" << endl;
    // If an exception occurs here, std::terminate() will be called
}

// Function that may throw
void riskyFunction() {
    cout << "This function may throw exceptions" << endl;
    throw runtime_error("Something went wrong");
}

// Function with conditional noexcept
void conditionalFunction(bool shouldThrow) noexcept(!shouldThrow) {
    cout << "Conditional noexcept function" << endl;
    if (shouldThrow) {
        throw runtime_error("Throwing as expected");
    }
}

// noexcept operator examples
void demonstrateNoexceptOperator() {
    cout << "=== noexcept Operator ===" << endl;
    
    cout << "safeFunction() is noexcept: " << noexcept(safeFunction()) << endl;
    cout << "riskyFunction() is noexcept: " << noexcept(riskyFunction()) << endl;
    cout << "conditionalFunction(true) is noexcept: " << noexcept(conditionalFunction(true)) << endl;
    cout << "conditionalFunction(false) is noexcept: " << noexcept(conditionalFunction(false)) << endl;
    
    // Test with lambda expressions
    auto safeLambda = []() noexcept { cout << "Safe lambda" << endl; };
    auto riskyLambda = []() { throw runtime_error("Risky lambda"); };
    
    cout << "safeLambda is noexcept: " << noexcept(safeLambda()) << endl;
    cout << "riskyLambda is noexcept: " << noexcept(riskyLambda()) << endl;
}

int main() {
    cout << "=== Basic noexcept Usage ===" << endl;
    
    demonstrateNoexceptOperator();
    
    cout << "\n--- Testing noexcept functions ---" << endl;
    
    // Test safe function
    try {
        safeFunction();
        cout << "safeFunction completed successfully" << endl;
    } catch (...) {
        cout << "This should never be printed" << endl;
    }
    
    // Test risky function
    try {
        riskyFunction();
    } catch (const exception& e) {
        cout << "Caught exception from riskyFunction: " << e.what() << endl;
    }
    
    // Test conditional noexcept
    cout << "\n--- Testing conditional noexcept ---" << endl;
    
    try {
        conditionalFunction(false);
        cout << "conditionalFunction(false) completed" << endl;
    } catch (const exception& e) {
        cout << "Caught: " << e.what() << endl;
    }
    
    try {
        conditionalFunction(true);
        cout << "This won't be printed" << endl;
    } catch (const exception& e) {
        cout << "Caught: " << e.what() << endl;
    }
    
    return 0;
}
```

### 2. **noexcept with Templates and Classes**

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include <type_traits>
using namespace std;

// Template class with conditional noexcept
template <typename T>
class SafeContainer {
private:
    vector<T> data;
    
public:
    // Constructor is noexcept if T's default constructor is noexcept
    SafeContainer() noexcept(is_nothrow_default_constructible_v<T>) {
        cout << "SafeContainer constructor (noexcept: " 
             << noexcept(SafeContainer()) << ")" << endl;
    }
    
    // push_back is noexcept if T's move constructor is noexcept
    void push_back(T&& value) noexcept(is_nothrow_move_constructible_v<T>) {
        data.push_back(move(value));
    }
    
    // emplace_back is noexcept if T's constructor with args is noexcept
    template <typename... Args>
    void emplace_back(Args&&... args) noexcept(is_nothrow_constructible_v<T, Args...>) {
        data.emplace_back(forward<Args>(args)...);
    }
    
    // clear is always noexcept (doesn't throw)
    void clear() noexcept {
        data.clear();
    }
    
    // size is always noexcept
    size_t size() const noexcept {
        return data.size();
    }
    
    // Element access with bounds checking
    T& at(size_t index) noexcept(false) { // Explicitly may throw
        return data.at(index);
    }
    
    // Element access without bounds checking
    T& operator[](size_t index) noexcept {
        return data[index];
    }
};

// Template function with conditional noexcept
template <typename T>
T safeAdd(const T& a, const T& b) noexcept(noexcept(a + b)) {
    return a + b;
}

// Function that uses noexcept for optimization
class FastString {
private:
    char* data;
    size_t length;
    
public:
    FastString(const char* str) : length(strlen(str)) {
        data = new char[length + 1];
        strcpy(data, str);
    }
    
    // Move constructor is noexcept
    FastString(FastString&& other) noexcept 
        : data(other.data), length(other.length) {
        other.data = nullptr;
        other.length = 0;
    }
    
    // Move assignment is noexcept
    FastString& operator=(FastString&& other) noexcept {
        if (this != &other) {
            delete[] data;
            data = other.data;
            length = other.length;
            other.data = nullptr;
            other.length = 0;
        }
        return *this;
    }
    
    // Destructor is noexcept by default
    ~FastString() {
        delete[] data;
    }
    
    // Swap is noexcept for better performance
    void swap(FastString& other) noexcept {
        std::swap(data, other.data);
        std::swap(length, other.length);
    }
    
    const char* c_str() const noexcept {
        return data;
    }
};

// noexcept in inheritance
class Base {
public:
    virtual void safeMethod() noexcept {
        cout << "Base::safeMethod (noexcept)" << endl;
    }
    
    virtual void riskyMethod() {
        cout << "Base::riskyMethod (may throw)" << endl;
    }
    
    virtual ~Base() = default; // Virtual destructor
};

class Derived : public Base {
public:
    // Override must also be noexcept
    void safeMethod() noexcept override {
        cout << "Derived::safeMethod (noexcept)" << endl;
    }
    
    // Override may be noexcept even if base is not
    void riskyMethod() noexcept override {
        cout << "Derived::riskyMethod (noexcept override)" << endl;
    }
};

int main() {
    cout << "=== noexcept with Templates and Classes ===" << endl;
    
    // Test SafeContainer with different types
    cout << "\n--- SafeContainer Tests ---" << endl;
    
    SafeContainer<int> intContainer;
    cout << "intContainer operations are mostly noexcept" << endl;
    
    SafeContainer<string> stringContainer;
    cout << "stringContainer operations may not be noexcept" << endl;
    
    // Test template function
    cout << "\n--- Template Function Tests ---" << endl;
    cout << "safeAdd(1, 2) is noexcept: " << noexcept(safeAdd(1, 2)) << endl;
    cout << "safeAdd(string(\"a\"), string(\"b\")) is noexcept: " 
         << noexcept(safeAdd(string("a"), string("b"))) << endl;
    
    // Test FastString move operations
    cout << "\n--- FastString Move Tests ---" << endl;
    FastString str1("Hello");
    FastString str2("World");
    
    cout << "Move constructor is noexcept: " << noexcept(FastString(move(str1))) << endl;
    cout << "Move assignment is noexcept: " << noexcept(str2 = move(str1)) << endl;
    
    str2 = move(str1);
    cout << "After move: " << str2.c_str() << endl;
    
    // Test inheritance
    cout << "\n--- Inheritance Tests ---" << endl;
    Base* base = new Derived();
    
    cout << "Base::safeMethod is noexcept: " << noexcept(base->safeMethod()) << endl;
    cout << "Base::riskyMethod is noexcept: " << noexcept(base->riskyMethod()) << endl;
    
    base->safeMethod();
    base->riskyMethod();
    
    delete base;
    
    return 0;
}
```

### 3. **Exception Safety Guarantees**

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include <algorithm>
using namespace std;

// Class demonstrating different exception safety levels
class SafeVector {
private:
    int* data;
    size_t size;
    size_t capacity;
    
public:
    // Constructor: Basic guarantee (if allocation fails, object is not created)
    SafeVector(size_t initialCapacity = 10) : size(0), capacity(initialCapacity) {
        data = new int[capacity];
        cout << "SafeVector constructed with capacity " << capacity << endl;
    }
    
    // Destructor: No-throw guarantee
    ~SafeVector() noexcept {
        delete[] data;
        cout << "SafeVector destroyed" << endl;
    }
    
    // Copy constructor: Strong guarantee
    SafeVector(const SafeVector& other) : size(other.size), capacity(other.capacity) {
        data = new int[capacity];
        
        // If copy throws, we haven't modified this object yet
        copy(other.data, other.data + other.size, data);
        cout << "SafeVector copy constructed" << endl;
    }
    
    // Copy assignment: Strong guarantee
    SafeVector& operator=(const SafeVector& other) {
        if (this != &other) {
            // Create temporary copy first
            SafeVector temp(other);
            
            // If we get here, copy succeeded, now swap
            swap(temp);
            
            cout << "SafeVector copy assigned" << endl;
        }
        return *this;
    }
    
    // Move constructor: No-throw guarantee
    SafeVector(SafeVector&& other) noexcept 
        : data(other.data), size(other.size), capacity(other.capacity) {
        other.data = nullptr;
        other.size = 0;
        other.capacity = 0;
        cout << "SafeVector move constructed" << endl;
    }
    
    // Move assignment: No-throw guarantee
    SafeVector& operator=(SafeVector&& other) noexcept {
        if (this != &other) {
            delete[] data;
            data = other.data;
            size = other.size;
            capacity = other.capacity;
            
            other.data = nullptr;
            other.size = 0;
            other.capacity = 0;
            
            cout << "SafeVector move assigned" << endl;
        }
        return *this;
    }
    
    // push_back: Strong guarantee
    void push_back(int value) {
        if (size >= capacity) {
            resize(capacity * 2);
        }
        data[size++] = value;
    }
    
    // resize: Strong guarantee
    void resize(size_t newCapacity) {
        if (newCapacity <= capacity) return;
        
        // Allocate new memory first
        int* newData = new int[newCapacity];
        
        // Copy existing data
        copy(data, data + size, newData);
        
        // If everything succeeded, update state
        delete[] data;
        data = newData;
        capacity = newCapacity;
        
        cout << "SafeVector resized to " << newCapacity << endl;
    }
    
    // swap: No-throw guarantee
    void swap(SafeVector& other) noexcept {
        std::swap(data, other.data);
        std::swap(size, other.size);
        std::swap(capacity, other.capacity);
    }
    
    // at: Basic guarantee (may throw, but object remains valid)
    int& at(size_t index) {
        if (index >= size) {
            throw out_of_range("Index out of bounds");
        }
        return data[index];
    }
    
    // operator[]: No-throw guarantee (no bounds checking)
    int& operator[](size_t index) noexcept {
        return data[index];
    }
    
    // Getter methods: No-throw guarantee
    size_t getSize() const noexcept { return size; }
    size_t getCapacity() const noexcept { return capacity; }
    
    // clear: No-throw guarantee
    void clear() noexcept {
        size = 0;
    }
};

// Function demonstrating exception safety
void demonstrateExceptionSafety() {
    cout << "=== Exception Safety Guarantees ===" << endl;
    
    // No-throw guarantee example
    cout << "\n--- No-throw Guarantee ---" << endl;
    SafeVector vec1(5);
    SafeVector vec2(10);
    
    cout << "Swap is noexcept: " << noexcept(vec1.swap(vec2)) << endl;
    vec1.swap(vec2);
    
    // Strong guarantee example
    cout << "\n--- Strong Guarantee ---" << endl;
    SafeVector vec3(3);
    vec3.push_back(1);
    vec3.push_back(2);
    vec3.push_back(3);
    
    SafeVector vec4;
    vec4 = vec3; // Copy assignment with strong guarantee
    
    // Basic guarantee example
    cout << "\n--- Basic Guarantee ---" << endl;
    try {
        SafeVector vec5(2);
        vec5.push_back(10);
        vec5.push_back(20);
        int value = vec5.at(5); // Will throw, but vec5 remains valid
        cout << "This won't print" << endl;
    } catch (const out_of_range& e) {
        cout << "Caught exception: " << e.what() << endl;
        cout << "Vector remains in a valid state" << endl;
    }
}

// Exception-safe factory function
unique_ptr<SafeVector> createSafeVector(size_t size) {
    try {
        return make_unique<SafeVector>(size);
    } catch (const bad_alloc&) {
        cout << "Memory allocation failed" << endl;
        return nullptr;
    }
}

// Exception-safe algorithm
void safeSort(SafeVector& vec) noexcept(false) {
    // Simple bubble sort with strong exception safety
    size_t n = vec.getSize();
    for (size_t i = 0; i < n - 1; i++) {
        for (size_t j = 0; j < n - i - 1; j++) {
            if (vec[j] > vec[j + 1]) {
                // Swap is noexcept, so this operation is safe
                std::swap(vec[j], vec[j + 1]);
            }
        }
    }
}

int main() {
    demonstrateExceptionSafety();
    
    // Test factory function
    cout << "\n--- Factory Function ---" << endl;
    auto vecPtr = createSafeVector(5);
    if (vecPtr) {
        cout << "SafeVector created successfully" << endl;
    }
    
    // Test exception-safe algorithm
    cout << "\n--- Exception-Safe Algorithm ---" << endl;
    SafeVector sortVec(10);
    sortVec.push_back(5);
    sortVec.push_back(2);
    sortVec.push_back(8);
    sortVec.push_back(1);
    sortVec.push_back(9);
    
    cout << "Before sorting: ";
    for (size_t i = 0; i < sortVec.getSize(); i++) {
        cout << sortVec[i] << " ";
    }
    cout << endl;
    
    safeSort(sortVec);
    
    cout << "After sorting: ";
    for (size_t i = 0; i < sortVec.getSize(); i++) {
        cout << sortVec[i] << " ";
    }
    cout << endl;
    
    return 0;
}
```

### 4. **Advanced noexcept Techniques**

```cpp
#include <iostream>
#include <type_traits>
#include <utility>
#include <memory>
using namespace std;

// SFINAE with noexcept
template <typename T>
enable_if_t<is_nothrow_move_constructible_v<T>, void>
safeMove(T&& dest, T& src) noexcept {
    dest = move(src);
}

template <typename T>
enable_if_t<!is_nothrow_move_constructible_v<T>, void>
safeMove(T&& dest, T& src) {
    // Use copy when move is not noexcept
    dest = src;
}

// noexcept perfect forwarding
template <typename T, typename... Args>
unique_ptr<T> makeUniqueNoThrow(Args&&... args) 
    noexcept(is_nothrow_constructible_v<T, Args...>) {
    return make_unique<T>(forward<Args>(args)...);
}

// Conditional noexcept based on template parameters
template <typename T>
class ConditionalNoexceptContainer {
private:
    T* data;
    size_t size;
    
public:
    // Constructor is noexcept if T is nothrow default constructible
    ConditionalNoexceptContainer(size_t s) 
        noexcept(is_nothrow_default_constructible_v<T>) 
        : size(s) {
        data = new T[size](); // Value-initialize
        
        // If T's constructor throws, we need cleanup
        // This is simplified - in real code, you'd need more sophisticated handling
    }
    
    // Destructor is noexcept
    ~ConditionalNoexceptContainer() noexcept {
        delete[] data;
    }
    
    // Element access
    T& operator[](size_t index) noexcept(is_nothrow_default_constructible_v<T>) {
        return data[index];
    }
    
    const T& operator[](size_t index) const noexcept(is_nothrow_default_constructible_v<T>) {
        return data[index];
    }
    
    // Size is always noexcept
    size_t getSize() const noexcept {
        return size;
    }
};

// noexcept with constexpr (C++17)
constexpr int divide(int a, int b) noexcept(b != 0) {
    return b != 0 ? a / b : throw runtime_error("Division by zero");
}

// noexcept operator in templates
template <typename T>
constexpr bool isNothrowSwappable() noexcept {
    using std::swap;
    return noexcept(swap(declval<T&>(), declval<T&>()));
}

// Custom deleter with noexcept
class CustomDeleter {
public:
    void operator()(void* ptr) const noexcept {
        cout << "Custom deleter called" << endl;
        free(ptr);
    }
};

// Exception-safe resource management
class ResourceManager {
private:
    void* resource;
    
public:
    ResourceManager() : resource(nullptr) {}
    
    // Acquire resource with noexcept guarantee
    bool acquire(size_t size) noexcept {
        resource = malloc(size);
        return resource != nullptr;
    }
    
    // Release with noexcept guarantee
    void release() noexcept {
        if (resource) {
            free(resource);
            resource = nullptr;
        }
    }
    
    // Destructor is noexcept
    ~ResourceManager() noexcept {
        release();
    }
    
    // Check if resource is valid
    bool isValid() const noexcept {
        return resource != nullptr;
    }
    
    // Get resource (no ownership transfer)
    void* get() const noexcept {
        return resource;
    }
};

// noexcept with lambda expressions
void demonstrateLambdaNoexcept() {
    cout << "=== Lambda noexcept ===" << endl;
    
    // noexcept lambda
    auto nothrowLambda = []() noexcept { cout << "No-throw lambda" << endl; };
    
    // May throw lambda
    auto throwingLambda = []() { throw runtime_error("Throwing lambda"); };
    
    cout << "nothrowLambda is noexcept: " << noexcept(nothrowLambda()) << endl;
    cout << "throwingLambda is noexcept: " << noexcept(throwingLambda()) << endl;
    
    // Conditional noexcept lambda
    auto conditionalLambda = [](bool shouldThrow) noexcept(!shouldThrow) {
        if (shouldThrow) {
            throw runtime_error("Conditional throw");
        }
        cout << "Conditional lambda executed" << endl;
    };
    
    cout << "conditionalLambda(true) is noexcept: " << noexcept(conditionalLambda(true)) << endl;
    cout << "conditionalLambda(false) is noexcept: " << noexcept(conditionalLambda(false)) << endl;
}

// noexcept with function pointers
using NothrowFunction = void(*)() noexcept;
using ThrowingFunction = void(*)();

void nothrowFunc() noexcept {
    cout << "No-throw function" << endl;
}

void throwingFunc() {
    cout << "Throwing function" << endl;
}

void demonstrateFunctionPointerNoexcept() {
    cout << "\n=== Function Pointer noexcept ===" << endl;
    
    NothrowFunction ntFunc = nothrowFunc;
    ThrowingFunction tFunc = throwingFunc;
    
    cout << "ntFunc is noexcept: " << noexcept(ntFunc()) << endl;
    cout << "tFunc is noexcept: " << noexcept(tFunc()) << endl;
}

int main() {
    cout << "=== Advanced noexcept Techniques ===" << endl;
    
    // Test SFINAE with noexcept
    cout << "\n--- SFINAE with noexcept ---" << endl;
    
    int a = 10, b = 20;
    safeMove(a, b);
    cout << "After safeMove: a = " << a << ", b = " << b << endl;
    
    // Test conditional noexcept container
    cout << "\n--- Conditional noexcept Container ---" << endl;
    
    ConditionalNoexceptContainer<int> intContainer(5);
    cout << "intContainer constructor is noexcept: " 
         << noexcept(ConditionalNoexceptContainer<int>(5)) << endl;
    
    ConditionalNoexceptContainer<string> stringContainer(3);
    cout << "stringContainer constructor is noexcept: " 
         << noexcept(ConditionalNoexceptContainer<string>(3)) << endl;
    
    // Test constexpr noexcept
    cout << "\n--- constexpr noexcept ---" << endl;
    
    constexpr int result1 = divide(10, 2);
    cout << "divide(10, 2) = " << result1 << endl;
    
    // constexpr int result2 = divide(10, 0); // Compile-time error
    
    // Test noexcept operator
    cout << "\n--- noexcept operator ---" << endl;
    
    cout << "int is nothrow swappable: " << isNothrowSwappable<int>() << endl;
    cout << "string is nothrow swappable: " << isNothrowSwappable<string>() << endl;
    
    // Test resource management
    cout << "\n--- Resource Management ---" << endl;
    
    {
        ResourceManager rm;
        if (rm.acquire(1024)) {
            cout << "Resource acquired successfully" << endl;
        }
        // Automatically released when rm goes out of scope
    }
    
    // Test lambda noexcept
    demonstrateLambdaNoexcept();
    
    // Test function pointer noexcept
    demonstrateFunctionPointerNoexcept();
    
    return 0;
}
```

### 5. **noexcept and Performance**

```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <algorithm>
using namespace std;
using namespace std::chrono;

// Performance comparison between noexcept and non-noexcept functions
class PerformanceTest {
private:
    static const int ITERATIONS = 1000000;
    
public:
    // noexcept version
    static void noexceptSwap(int& a, int& b) noexcept {
        int temp = a;
        a = b;
        b = temp;
    }
    
    // Non-noexcept version
    static void regularSwap(int& a, int& b) {
        int temp = a;
        a = b;
        b = temp;
    }
    
    // noexcept vector operations
    static void noexceptVectorOperations() {
        vector<int> vec;
        vec.reserve(ITERATIONS);
        
        for (int i = 0; i < ITERATIONS; i++) {
            vec.push_back(i); // May throw, but vector handles it
        }
        
        for (int i = 0; i < ITERATIONS; i++) {
            for (int j = i + 1; j < ITERATIONS; j++) {
                if (vec[i] > vec[j]) {
                    noexceptSwap(vec[i], vec[j]);
                }
            }
        }
    }
    
    // Regular vector operations
    static void regularVectorOperations() {
        vector<int> vec;
        vec.reserve(ITERATIONS);
        
        for (int i = 0; i < ITERATIONS; i++) {
            vec.push_back(i);
        }
        
        for (int i = 0; i < ITERATIONS; i++) {
            for (int j = i + 1; j < ITERATIONS; j++) {
                if (vec[i] > vec[j]) {
                    regularSwap(vec[i], vec[j]);
                }
            }
        }
    }
    
    // noexcept move operations
    static void testNoexceptMoves() {
        vector<string> vec1, vec2;
        vec1.reserve(ITERATIONS);
        vec2.reserve(ITERATIONS);
        
        // Fill vector with strings
        for (int i = 0; i < ITERATIONS; i++) {
            vec1.emplace_back("String " + to_string(i));
        }
        
        // Move operations (should be optimized due to noexcept)
        for (int i = 0; i < ITERATIONS; i++) {
            vec2.push_back(move(vec1[i]));
        }
    }
    
    // Regular move operations
    static void testRegularMoves() {
        vector<string> vec1, vec2;
        vec1.reserve(ITERATIONS);
        vec2.reserve(ITERATIONS);
        
        // Fill vector with strings
        for (int i = 0; i < ITERATIONS; i++) {
            vec1.emplace_back("String " + to_string(i));
        }
        
        // Force copy operations (less efficient)
        for (int i = 0; i < ITERATIONS; i++) {
            vec2.push_back(vec1[i]); // Copy instead of move
        }
    }
    
    // noexcept sorting
    static void noexceptSort() {
        vector<int> vec;
        vec.reserve(ITERATIONS);
        
        for (int i = 0; i < ITERATIONS; i++) {
            vec.push_back(rand() % 1000);
        }
        
        sort(vec.begin(), vec.end(), [](int a, int b) noexcept {
            return a < b;
        });
    }
    
    // Regular sorting
    static void regularSort() {
        vector<int> vec;
        vec.reserve(ITERATIONS);
        
        for (int i = 0; i < ITERATIONS; i++) {
            vec.push_back(rand() % 1000);
        }
        
        sort(vec.begin(), vec.end(), [](int a, int b) {
            return a < b;
        });
    }
    
    // Performance measurement template
    template <typename Func>
    static void measureTime(const string& testName, Func&& func) {
        auto start = high_resolution_clock::now();
        func();
        auto end = high_resolution_clock::now();
        
        auto duration = duration_cast<microseconds>(end - start);
        cout << testName << ": " << duration.count() << " microseconds" << endl;
    }
    
    static void runPerformanceTests() {
        cout << "=== noexcept Performance Tests ===" << endl;
        cout << "Iterations: " << ITERATIONS << endl;
        
        cout << "\n--- Swap Operations ---" << endl;
        measureTime("noexceptSwap", []() {
            int a = 1, b = 2;
            for (int i = 0; i < ITERATIONS; i++) {
                noexceptSwap(a, b);
            }
        });
        
        measureTime("regularSwap", []() {
            int a = 1, b = 2;
            for (int i = 0; i < ITERATIONS; i++) {
                regularSwap(a, b);
            }
        });
        
        cout << "\n--- Vector Operations ---" << endl;
        measureTime("noexceptVectorOperations", noexceptVectorOperations);
        measureTime("regularVectorOperations", regularVectorOperations);
        
        cout << "\n--- Move Operations ---" << endl;
        measureTime("noexceptMoves", testNoexceptMoves);
        measureTime("regularMoves", testRegularMoves);
        
        cout << "\n--- Sorting Operations ---" << endl;
        measureTime("noexceptSort", noexceptSort);
        measureTime("regularSort", regularSort);
    }
};

// noexcept optimization examples
class OptimizedString {
private:
    char* data;
    size_t size;
    
public:
    OptimizedString(const char* str) : size(strlen(str)) {
        data = new char[size + 1];
        strcpy(data, str);
    }
    
    // noexcept move constructor enables optimizations
    OptimizedString(OptimizedString&& other) noexcept 
        : data(other.data), size(other.size) {
        other.data = nullptr;
        other.size = 0;
    }
    
    // noexcept move assignment
    OptimizedString& operator=(OptimizedString&& other) noexcept {
        if (this != &other) {
            delete[] data;
            data = other.data;
            size = other.size;
            other.data = nullptr;
            other.size = 0;
        }
        return *this;
    }
    
    ~OptimizedString() {
        delete[] data;
    }
    
    size_t getSize() const noexcept { return size; }
    const char* c_str() const noexcept { return data; }
};

void demonstrateOptimizations() {
    cout << "\n=== noexcept Optimizations ===" << endl;
    
    vector<OptimizedString> strings;
    strings.reserve(1000);
    
    // These moves are optimized because move constructor is noexcept
    for (int i = 0; i < 1000; i++) {
        strings.emplace_back(("String " + to_string(i)).c_str());
    }
    
    cout << "Created " << strings.size() << " strings with optimized moves" << endl;
    cout << "Total characters: " << strings[0].getSize() << endl;
}

int main() {
    // Run performance tests
    PerformanceTest::runPerformanceTests();
    
    // Demonstrate optimizations
    demonstrateOptimizations();
    
    cout << "\n=== noexcept Benefits Summary ===" << endl;
    cout << "1. Enables compiler optimizations" << endl;
    cout << "2. Better performance with move operations" << endl;
    cout << "3. Allows use in noexcept contexts" << endl;
    cout << "4. Improves exception safety analysis" << endl;
    cout << "5. Reduces binary size in some cases" << endl;
    
    return 0;
}
```

---

## 🎮 Complete Example: Exception-Safe File System

```cpp
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <memory>
#include <map>
using namespace std;

// Exception-safe file handle
class FileHandle {
private:
    FILE* file;
    
public:
    // Constructor may throw (basic guarantee)
    FileHandle(const string& filename, const string& mode) : file(nullptr) {
        file = fopen(filename.c_str(), mode.c_str());
        if (!file) {
            throw runtime_error("Failed to open file: " + filename);
        }
    }
    
    // Destructor is noexcept
    ~FileHandle() noexcept {
        if (file) {
            fclose(file);
        }
    }
    
    // Move constructor is noexcept
    FileHandle(FileHandle&& other) noexcept : file(other.file) {
        other.file = nullptr;
    }
    
    // Move assignment is noexcept
    FileHandle& operator=(FileHandle&& other) noexcept {
        if (this != &other) {
            if (file) {
                fclose(file);
            }
            file = other.file;
            other.file = nullptr;
        }
        return *this;
    }
    
    // Delete copy operations
    FileHandle(const FileHandle&) = delete;
    FileHandle& operator=(const FileHandle&) = delete;
    
    // File operations with different exception guarantees
    void write(const string& data) noexcept(false) { // May throw
        if (fprintf(file, "%s\n", data.c_str()) < 0) {
            throw runtime_error("Failed to write to file");
        }
    }
    
    string readLine() noexcept(false) { // May throw
        char buffer[1024];
        if (fgets(buffer, sizeof(buffer), file)) {
            return string(buffer);
        }
        if (ferror(file)) {
            throw runtime_error("Error reading from file");
        }
        return ""; // EOF
    }
    
    void flush() noexcept(false) { // May throw
        if (fflush(file) != 0) {
            throw runtime_error("Failed to flush file");
        }
    }
    
    bool isOpen() const noexcept { // No-throw guarantee
        return file != nullptr;
    }
    
    FILE* get() const noexcept { // No-throw guarantee
        return file;
    }
};

// Exception-safe file system
class FileSystem {
private:
    map<string, unique_ptr<FileHandle>> openFiles;
    
public:
    // Open file with strong guarantee
    FileHandle& openFile(const string& filename, const string& mode) {
        if (openFiles.find(filename) != openFiles.end()) {
            throw runtime_error("File already open: " + filename);
        }
        
        auto handle = make_unique<FileHandle>(filename, mode);
        FileHandle& ref = *handle;
        openFiles[filename] = move(handle);
        
        return ref;
    }
    
    // Close file with no-throw guarantee
    void closeFile(const string& filename) noexcept {
        openFiles.erase(filename);
    }
    
    // Write to file with basic guarantee
    void writeFile(const string& filename, const string& data) {
        auto it = openFiles.find(filename);
        if (it == openFiles.end()) {
            throw runtime_error("File not open: " + filename);
        }
        
        it->second->write(data);
    }
    
    // Read from file with basic guarantee
    string readFile(const string& filename) {
        auto it = openFiles.find(filename);
        if (it == openFiles.end()) {
            throw runtime_error("File not open: " + filename);
        }
        
        return it->second->readLine();
    }
    
    // List open files with no-throw guarantee
    vector<string> listOpenFiles() const noexcept {
        vector<string> files;
        for (const auto& [filename, handle] : openFiles) {
            files.push_back(filename);
        }
        return files;
    }
    
    // Close all files with no-throw guarantee
    void closeAllFiles() noexcept {
        openFiles.clear();
    }
    
    // Get file count with no-throw guarantee
    size_t getOpenFileCount() const noexcept {
        return openFiles.size();
    }
};

// Transaction system with exception safety
class FileTransaction {
private:
    FileSystem& fs;
    vector<string> modifiedFiles;
    bool committed;
    
public:
    explicit FileTransaction(FileSystem& filesystem) 
        : fs(filesystem), committed(false) {}
    
    // Destructor with no-throw guarantee
    ~FileTransaction() noexcept {
        if (!committed) {
            rollback();
        }
    }
    
    // Write operation with strong guarantee
    void writeFile(const string& filename, const string& data) {
        try {
            fs.writeFile(filename, data);
            modifiedFiles.push_back(filename);
        } catch (...) {
            // If write fails, we don't add to modified files
            throw;
        }
    }
    
    // Commit with no-throw guarantee (assuming file operations don't throw after this point)
    void commit() noexcept {
        committed = true;
        modifiedFiles.clear();
    }
    
    // Rollback with no-throw guarantee
    void rollback() noexcept {
        // In a real system, you would restore original content
        // For this example, we just clear the transaction
        modifiedFiles.clear();
    }
    
    // Get modified files with no-throw guarantee
    const vector<string>& getModifiedFiles() const noexcept {
        return modifiedFiles;
    }
};

// Exception-safe file processor
class FileProcessor {
private:
    FileSystem fs;
    
public:
    // Process files with strong exception safety
    void processFiles(const vector<pair<string, string>>& fileData) {
        FileTransaction transaction(fs);
        
        try {
            // Write all files
            for (const auto& [filename, data] : fileData) {
                fs.openFile(filename, "w");
                transaction.writeFile(filename, data);
            }
            
            // If all writes succeed, commit transaction
            transaction.commit();
            
            cout << "All files processed successfully" << endl;
            
        } catch (...) {
            cout << "File processing failed, transaction rolled back" << endl;
            throw;
        }
    }
    
    // Read file with basic guarantee
    string readFile(const string& filename) {
        fs.openFile(filename, "r");
        return fs.readFile(filename);
    }
    
    // Cleanup with no-throw guarantee
    void cleanup() noexcept {
        fs.closeAllFiles();
    }
    
    // Get status with no-throw guarantee
    void printStatus() const noexcept {
        cout << "Open files: " << fs.getOpenFileCount() << endl;
        auto files = fs.listOpenFiles();
        for (const string& file : files) {
            cout << "  " << file << endl;
        }
    }
};

// noexcept utilities
class NoexceptUtils {
public:
    // noexcept string concatenation
    static string safeConcat(const string& a, const string& b) noexcept {
        try {
            return a + b;
        } catch (...) {
            return ""; // Return empty string on allocation failure
        }
    }
    
    // noexcept file size check
    static bool fileExists(const string& filename) noexcept {
        FILE* file = fopen(filename.c_str(), "r");
        if (file) {
            fclose(file);
            return true;
        }
        return false;
    }
    
    // noexcept safe conversion
    template <typename T>
    static string safeToString(T value) noexcept {
        try {
            return to_string(value);
        } catch (...) {
            return "conversion_error";
        }
    }
};

int main() {
    cout << "=== Exception-Safe File System ===" << endl;
    
    FileProcessor processor;
    
    // Test successful processing
    cout << "\n--- Successful Processing ---" << endl;
    vector<pair<string, string>> filesToWrite = {
        {"file1.txt", "Hello World"},
        {"file2.txt", "C++ Programming"},
        {"file3.txt", "Exception Safety"}
    };
    
    try {
        processor.processFiles(filesToWrite);
        processor.printStatus();
        
        // Read files
        for (const auto& [filename, _] : filesToWrite) {
            string content = processor.readFile(filename);
            cout << filename << ": " << content;
        }
        
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    // Test failed processing
    cout << "\n--- Failed Processing ---" << endl;
    vector<pair<string, string>> problematicFiles = {
        {"file4.txt", "First file"},
        {"", "Invalid filename"}, // This will cause failure
        {"file6.txt", "This won't be written"}
    };
    
    try {
        processor.processFiles(problematicFiles);
    } catch (const exception& e) {
        cout << "Expected error: " << e.what() << endl;
    }
    
    processor.printStatus();
    
    // Test noexcept utilities
    cout << "\n--- noexcept Utilities ---" << endl;
    
    string result1 = NoexceptUtils::safeConcat("Hello", " World");
    cout << "Safe concat: " << result1 << endl;
    
    bool exists = NoexceptUtils::fileExists("file1.txt");
    cout << "file1.txt exists: " << exists << endl;
    
    string numberStr = NoexceptUtils::safeToString(42);
    cout << "Safe to string: " << numberStr << endl;
    
    // Cleanup
    processor.cleanup();
    cout << "\nAfter cleanup:" << endl;
    processor.printStatus();
    
    return 0;
}
```

---

## 📊 Exception Specifications Summary

| Specification | Meaning | Use Case |
|---------------|---------|----------|
| `noexcept` | Function promises not to throw | Performance-critical functions |
| `noexcept(true)` | Explicitly promises not to throw | Clear documentation |
| `noexcept(false)` | May throw (same as no spec) | Regular functions |
| `noexcept(condition)` | Conditional based on condition | Template functions |
| `noexcept(expr)` | Compile-time check for expressions | Template metaprogramming |

---

## ⚡ Performance Considerations

### Advantages
- ✅ **Compiler Optimization**: Enables better code generation
- ✅ **Move Operations**: Optimizes std::move usage
- ✅ **Exception Safety**: Clear guarantees about behavior
- ✅ **Binary Size**: May reduce exception handling code
- ✅ **Static Analysis**: Better compile-time checking

### Considerations
- ⚠️ **std::terminate**: Program terminates if noexcept function throws
- ⚠️ **Complexity**: May add complexity to template code
- ⚠️ **Maintenance**: Need to update when implementations change
- ⚠️ **Debugging**: Harder to debug noexcept violations

---

## 🐛 Common Pitfalls

| Problem | Solution |
|---------|----------|
| **Forgetting to update noexcept** | Use `noexcept(noexcept(...))` for automatic detection |
| **Throwing in noexcept functions** | Use try-catch or ensure operations don't throw |
| **Marking destructors as throwing** | Always make destructors noexcept |
| **Overlooking noexcept in overrides** | Override functions must have same noexcept specification |
| **Complex conditional noexcept** | Keep conditions simple and clear |

---

## ✅ Best Practices

1. **Mark move operations** as noexcept when possible
2. **Use conditional noexcept** in templates for flexibility
3. **Make destructors** always noexcept
4. **Use noexcept operator** for compile-time checks
5. **Document exception safety** guarantees clearly
6. **Test noexcept violations** during development
7. **Prefer noexcept** for performance-critical code

---

## 📚 Related Topics

- [Try-Catch-Throw](01_Try_Catch_Throw.md)
- [Standard Exceptions](02_Standard_Exceptions.md)
- [Custom Exceptions](03_Custom_Exceptions.md)
- [RAII Pattern](05_RAII.md)

---

## 🚀 Next Steps

Continue learning about:
- **RAII Pattern**: Resource management with exceptions
- **Exception Safety Levels**: Basic, strong, and no-throw guarantees
- **Move Semantics**: Optimizing with noexcept move operations
- **Template Metaprogramming**: Advanced noexcept techniques

---
---

## Next Step

- Go to [05_RAII.md](05_RAII.md) to continue with RAII.
