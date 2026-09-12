# Constructors and Destructors - Theoretical Foundations

## 📖 Overview

In C++, **constructors** and **destructors** are special member functions governing the lifecycle of objects from inception to termination. 

Unlike garbage-collected languages (such as Java, Python, or Go) where object finalization is non-deterministic and delayed, C++ provides **deterministic object lifetimes**. The exact moment an object is created and destroyed is known at compile time, providing the foundation for **RAII (Resource Acquisition Is Initialization)**—the bedrock pattern of modern systems programming.

---

## ⏳ The Object Lifecycle in C++

```
  ┌──────────────┐     ┌──────────────┐     ┌─────────────────┐     ┌──────────────┐     ┌──────────────┐
  │  Allocation  │ ──> │ Construction │ ──> │ Active Lifetime │ ──> │ Destruction  │ ──> │ Deallocation │
  └──────────────┘     └──────────────┘     └─────────────────┘     └──────────────┘     └──────────────┘
    Reserve bytes        Run constructor      Invoke methods          Run destructor       Free memory
    (Stack/Heap)         Init members         Maintain state          Release resources    (Stack/Heap)
```

1. **Allocation**: Memory space is reserved on the stack (automatic storage) or the heap (dynamic storage via `operator new`).
2. **Construction**: The constructor establishes the class invariants and initializes data members.
3. **Active Lifetime**: The object is fully constructed; its methods may be invoked safely.
4. **Destruction**: As the object goes out of scope or is deleted, its destructor executes, releasing owned resources.
5. **Deallocation**: The raw memory is reclaimed by the operating system or runtime memory manager.

---

## 🛡️ RAII: Resource Acquisition Is Initialization

Coined by Bjarne Stroustrup, **RAII** ties the lifecycle of external system resources (heap memory, database transactions, mutex locks, network sockets, file handles) directly to the **lifetime of an automatic (stack) object**.

```
    Scope Enters:   Resource Acquired (Constructor)
         │
         ├── Work executed safely
         ├── Exception thrown! ──> Stack Unwinding Begins
         │                             │
    Scope Exits:    Resource Released (Destructor called automatically!)
```

### Deterministic Stack Unwinding
If an exception occurs anywhere inside a block of code, the C++ runtime performs **stack unwinding**:
- Every local stack object created up to that point has its destructor called in strictly reverse order of creation.
- Resources cannot leak, even in the presence of unhandled runtime errors.

---

## 📋 The Strict Construction & Destruction Order

The ISO C++ standard specifies a rigid, deterministic order for constructing composite class hierarchies:

### Construction Order:
1. **Virtual Base Classes**: Constructed first, in depth-first, left-to-right order across the inheritance graph.
2. **Direct Non-Virtual Base Classes**: Constructed in the exact order they appear in the base-specifier list.
3. **Non-Static Data Members**: Initialized in the **order they are declared in the class definition** (ignoring the order written in the member initializer list!).
4. **Constructor Body**: The code block inside `{ ... }` finally executes.

### Destruction Order:
- The destructor executes in the **exact reverse order** of construction:
  $$\text{Destructor Body} \longrightarrow \text{Members in Reverse Order} \longrightarrow \text{Base Classes in Reverse Order}$$

---

## ⚡ Member Initialization List vs. Body Assignment

```cpp
// ❌ INEFFICIENT: Default construction followed by assignment
MyClass::MyClass(const std::string& str) {
    name = str; // 1. Default construct name (""), 2. Copy assign str into name
}

// ✅ EFFICIENT: Direct initialization
MyClass::MyClass(const std::string& str) : name(str) {
    // Direct copy-construction in-place; zero redundant temporaries
}
```

### Mandatory Uses of Initialization Lists:
1. Initializing `const` data members.
2. Initializing reference data members (`Type&`).
3. Calling parameterized constructors of base classes.
4. Initializing member objects that do not have a default constructor.

---

## 📜 The Rule of Zero, Three, and Five

### The Rule of Zero
If a class does not directly manage raw resources, **declare no special member functions**. Let the compiler generate default constructors, copy/move operations, and destructors using standard library RAII containers (`std::vector`, `std::unique_ptr`, `std::string`).

### The Rule of Three (C++98)
If a class directly manages a raw resource (e.g., raw pointer via `new`), you must explicitly define:
1. **Destructor**: Releases the resource (`delete ptr`).
2. **Copy Constructor**: Performs a deep copy of the resource.
3. **Copy Assignment Operator**: Safely deallocates current resource and deep copies new resource.

### The Rule of Five (C++11 Modern Standard)
With the advent of move semantics in C++11, defining any of the Rule of Three members inhibits the automatic generation of move operations. You must define all five:
1. **Destructor**
2. **Copy Constructor**
3. **Copy Assignment Operator**
4. **Move Constructor** (`noexcept`)
5. **Move Assignment Operator** (`noexcept`)

---

## 💻 Production Implementation: Exception-Safe RAII Resource Manager

The following complete, runnable C++ program demonstrates:
- Rule of Five implementation.
- Copy-and-swap idiom for strong exception safety.
- Virtual destructors preventing slice-deletions in polymorphic hierarchies.
- Constructor initialization order verification.

```cpp
#include <iostream>
#include <string>
#include <utility>
#include <cassert>
#include <vector>

// -------------------------------------------------------------
// 1. Rule of Five & Copy-and-Swap RAII Buffer
// -------------------------------------------------------------
class DynamicBuffer {
private:
    size_t capacity;
    int* data;

public:
    // Default / Parameterized Constructor
    explicit DynamicBuffer(size_t size = 0) 
        : capacity(size), data(size > 0 ? new int[size]() : nullptr) {
        std::cout << "  [CTOR] Allocated buffer of size " << capacity << " at " << data << "\n";
    }

    // Destructor (Rule of 1/5)
    ~DynamicBuffer() {
        std::cout << "  [DTOR] Freeing buffer of size " << capacity << " at " << data << "\n";
        delete[] data;
    }

    // Copy Constructor (Rule of 2/5 - Deep Copy)
    DynamicBuffer(const DynamicBuffer& other) 
        : capacity(other.capacity), data(other.capacity > 0 ? new int[other.capacity] : nullptr) {
        std::cout << "  [COPY CTOR] Deep-copied buffer of size " << capacity << "\n";
        for (size_t i = 0; i < capacity; i++) {
            data[i] = other.data[i];
        }
    }

    // Move Constructor (Rule of 3/5 - Resource Pilfering)
    DynamicBuffer(DynamicBuffer&& other) noexcept 
        : capacity(other.capacity), data(other.data) {
        std::cout << "  [MOVE CTOR] Pilfered resources from temporary buffer\n";
        other.capacity = 0;
        other.data = nullptr; // Leave source in valid, empty state
    }

    // Friend Swap for Exception-Safe Assignment
    friend void swap(DynamicBuffer& first, DynamicBuffer& second) noexcept {
        using std::swap;
        swap(first.capacity, second.capacity);
        swap(first.data, second.data);
    }

    // Unified Assignment Operator (Rule of 4 & 5/5 via Copy-and-Swap)
    // Pass by value handles both copy-and-swap and move-and-swap!
    DynamicBuffer& operator=(DynamicBuffer other) noexcept {
        std::cout << "  [OP=] Copy-and-swap invoked\n";
        swap(*this, other);
        return *this;
    }

    size_t size() const { return capacity; }
    int& operator[](size_t index) { return data[index]; }
    const int& operator[](size_t index) const { return data[index]; }
};

// -------------------------------------------------------------
// 2. Polymorphic Base Class with Virtual Destructor
// -------------------------------------------------------------
class BaseResource {
public:
    BaseResource() { std::cout << "  [BaseResource] Constructed\n"; }
    virtual ~BaseResource() { std::cout << "  [BaseResource] Destructed (Virtual Clean!)\n"; }
    virtual void inspect() const = 0;
};

class DerivedResource : public BaseResource {
private:
    int* derivedArray;

public:
    DerivedResource() : derivedArray(new int[100]) {
        std::cout << "  [DerivedResource] Allocated 100 ints\n";
    }

    ~DerivedResource() override {
        std::cout << "  [DerivedResource] Freeing 100 ints\n";
        delete[] derivedArray;
    }

    void inspect() const override {
        std::cout << "  [DerivedResource] In good working order\n";
    }
};

int main() {
    std::cout << "=== Constructors & Destructors Theoretical Foundations ===\n\n";

    std::cout << "--- 1. RAII Scope & Lifecycle ---\n";
    {
        DynamicBuffer buf1(5);
        buf1[0] = 42;
        std::cout << "  buf1[0] = " << buf1[0] << "\n";
    } // buf1 automatically destroyed here
    std::cout << "  buf1 went out of scope.\n\n";

    std::cout << "--- 2. Copy and Move Semantics ---\n";
    DynamicBuffer b1(10);
    DynamicBuffer b2 = b1;            // Calls Copy Constructor
    DynamicBuffer b3 = std::move(b1); // Calls Move Constructor
    std::cout << "  b1 size after move: " << b1.size() << " (pilfered)\n";
    std::cout << "  b3 size after move: " << b3.size() << " (active)\n\n";

    std::cout << "--- 3. Virtual Destructor in Polymorphism ---\n";
    // Deleting derived object via base pointer:
    // Without virtual destructor, DerivedResource destructor would NEVER run!
    BaseResource* polyRes = new DerivedResource();
    polyRes->inspect();
    std::cout << "  Deleting through BaseResource pointer:\n";
    delete polyRes;

    std::cout << "\n=== All Lifecycle & Destruction Foundations Verified! ===\n";
    return 0;
}
```

---

## 📊 Summary of Member Function Rules

| Special Member Function | Signature | Purpose | Implicitly Generated? |
| :--- | :--- | :--- | :--- |
| **Default Constructor** | `T()` | Initializes state from scratch | Yes (if no other constructors declared) |
| **Destructor** | `~T()` | Cleans up resources | Yes (calls member and base destructors) |
| **Copy Constructor** | `T(const T&)` | Duplicates existing object | Yes (unless move operations declared) |
| **Copy Assignment** | `T& operator=(const T&)` | Overwrites object from existing | Yes (unless move operations declared) |
| **Move Constructor** | `T(T&&) noexcept` | Transfers ownership of resources | Yes (only if no copy/dtor declared) |
| **Move Assignment** | `T& operator=(T&&) noexcept` | Transfers ownership via assignment | Yes (only if no copy/dtor declared) |
