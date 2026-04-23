# Theory.md

## Memory Management - Theoretical Foundations

### Overview

Memory management is the process of allocating, using, and freeing memory in a computer program. In C++, memory management is manual by default, giving programmers direct control over memory but also requiring careful attention to avoid leaks, dangling pointers, and undefined behavior. This document covers the theoretical foundations of memory management, including memory hierarchy, allocation strategies, fragmentation, ownership models, and the RAII philosophy.

---

### 1. Memory Hierarchy

Computer systems have a hierarchy of memory types with different characteristics:

| Memory Type | Allocation | Speed | Size | Lifetime | Scope |
|-------------|------------|-------|------|----------|-------|
| **Registers** | Compiler | Fastest | Bytes | Function | CPU |
| **Stack** | Automatic | Very Fast | MB | Function | Function |
| **Heap** | Manual | Fast | GB | Programmer-controlled | Program |
| **Static** | Compile-time | Fast | MB | Program | Global |
| **Thread Local** | Compile-time | Fast | MB | Thread | Thread |

**Stack Characteristics:**

| Property | Description |
|----------|-------------|
| **LIFO** | Last-In-First-Out allocation |
| **Automatic** | Allocated/deallocated on function entry/exit |
| **Fixed Size** | Size determined at compile time |
| **Fast** | Only pointer adjustment needed |
| **Limited** | Stack overflow risk for large allocations |

**Heap Characteristics:**

| Property | Description |
|----------|-------------|
| **Arbitrary** | Any size, any order allocation |
| **Manual** | Programmer controls lifetime |
| **Flexible** | Can allocate at runtime |
| **Slower** | Allocation algorithms have overhead |
| **Fragmentation** | Can lead to unusable memory |

---

### 2. Allocation Strategies

Memory allocators use various strategies to manage free memory:

| Strategy | Description | Pros | Cons |
|----------|-------------|------|------|
| **First-Fit** | First block large enough | Fast | Can fragment |
| **Best-Fit** | Smallest block large enough | Reduces waste | Slower search |
| **Worst-Fit** | Largest block | Reduces fragmentation | Slower, waste |
| **Buddy Allocator** | Split into power-of-two blocks | Fast merging | Internal fragmentation |
| **Pool Allocator** | Fixed-size blocks | Very fast | Only one size |

**First-Fit Allocation Example:**
```
Free List: [100][200][50][300]
Request: 150

First-Fit: Takes block 200 → splits into [150][50]
```

**Buddy Allocator Example:**
```
Request 64KB (buddy system with 4KB minimum)
- 1MB block split into 512KB + 512KB
- 512KB split into 256KB + 256KB
- 256KB split into 128KB + 128KB
- 128KB split into 64KB + 64KB
Allocate one 64KB block
```

---

### 3. Memory Fragmentation

Fragmentation occurs when free memory is not contiguous, making it unavailable for large allocations.

**External Fragmentation:**

| Aspect | Description |
|--------|-------------|
| **Definition** | Free memory split into small blocks |
| **Cause** | Allocating and freeing blocks of different sizes |
| **Effect** | Cannot allocate large block even though total free memory is sufficient |
| **Solution** | Compaction, pool allocators, buddy allocator |

```
External Fragmentation Visualization:
┌────┬───┬────┬─┬───┬────┐
│ A  │   │ B  │ │ C │    │
└────┴───┴────┴─┴───┴────┘
Used  Free Used Free Used Free
Total free = 3 blocks
Can we allocate a block of size (Free1+Free2+Free3)? No - not contiguous
```

**Internal Fragmentation:**

| Aspect | Description |
|--------|-------------|
| **Definition** | Wasted memory within allocated blocks |
| **Cause** | Allocation rounding, fixed-size blocks |
| **Effect** | Memory is allocated but not used |
| **Solution** | Smaller block sizes, variable allocation |

```
Internal Fragmentation Visualization:
Allocation request: 150 bytes
Allocator rounds to: 200 bytes
Wasted: 50 bytes (internal fragmentation)
```

---

### 4. RAII (Resource Acquisition Is Initialization)

RAII is a C++ idiom that ties resource lifetime to object lifetime.

**Core Principle:**

| Rule | Description |
|------|-------------|
| **Acquire** | Resource acquired in constructor |
| **Release** | Resource released in destructor |
| **Automatic** | Destructor called automatically when object goes out of scope |

**RAII Benefits:**

| Benefit | Description |
|---------|-------------|
| **Exception Safety** | Resources automatically freed during stack unwinding |
| **No Leaks** | Impossible to forget to release |
| **No Dangling** | Resource released exactly when object destroyed |
| **Deterministic** | Lifetime predictable and controllable |

**RAII vs Manual Management:**
```cpp
// Manual management (error-prone)
void manual() {
    Resource* r = new Resource();
    if (error) {
        delete r;  // Must remember
        return;
    }
    delete r;  // Must remember
}

// RAII (safe)
void raii() {
    Resource r;  // Automatic cleanup
    if (error) {
        return;  // r destroyed automatically
    }
    // r destroyed automatically
}
```

---

### 5. Ownership Models

Ownership defines who is responsible for releasing memory.

| Model | Description | C++ Representation |
|-------|-------------|-------------------|
| **No Ownership** | Observer, no responsibility | Raw pointer, reference |
| **Exclusive Ownership** | Single owner | `std::unique_ptr` |
| **Shared Ownership** | Multiple owners | `std::shared_ptr` |
| **Borrowing** | Temporary access | Reference, raw pointer |

**Ownership Rules:**

| Rule | Description |
|------|-------------|
| **Single Owner** | Only one entity responsible for deletion |
| **Ownership Transfer** | Can move ownership between owners |
| **Borrowing** | Non-owning access should not outlive owner |
| **Cycle Prevention** | Shared ownership can create cycles |

**Ownership Hierarchy:**
```
                    ┌─────────────────┐
                    │   Owner (unique) │
                    └────────┬────────┘
                             │ owns
                             ▼
                    ┌─────────────────┐
                    │    Resource      │
                    └────────┬────────┘
                             │ borrowed by
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │ Observer │  │ Observer │  │ Observer │
        └──────────┘  └──────────┘  └──────────┘
```

---

### 6. Smart Pointer Implementation

Smart pointers are RAII wrappers for raw pointers.

**unique_ptr Implementation (Conceptual):**

| Feature | Description |
|---------|-------------|
| **Exclusive Ownership** | No copy constructor or copy assignment |
| **Move Semantics** | Transfer ownership via move |
| **Deleter** | Customizable deletion strategy |
| **Zero Overhead** | Same size as raw pointer (usually) |

```cpp
template <typename T>
class SimpleUniquePtr {
private:
    T* ptr_;
    
public:
    explicit SimpleUniquePtr(T* ptr = nullptr) : ptr_(ptr) { }
    
    ~SimpleUniquePtr() { delete ptr_; }
    
    // No copy
    SimpleUniquePtr(const SimpleUniquePtr&) = delete;
    SimpleUniquePtr& operator=(const SimpleUniquePtr&) = delete;
    
    // Move
    SimpleUniquePtr(SimpleUniquePtr&& other) noexcept 
        : ptr_(other.ptr_) {
        other.ptr_ = nullptr;
    }
    
    T* operator->() { return ptr_; }
    T& operator*() { return *ptr_; }
};
```

**shared_ptr Implementation (Conceptual):**

| Feature | Description |
|---------|-------------|
| **Shared Ownership** | Multiple pointers can own same object |
| **Reference Counting** | Tracks number of owners |
| **Control Block** | Separate block for ref count and deleter |
| **Atomic Operations** | Thread-safe reference counting |

```cpp
template <typename T>
class SimpleSharedPtr {
private:
    T* ptr_;
    int* refCount_;
    
public:
    explicit SimpleSharedPtr(T* ptr = nullptr) 
        : ptr_(ptr), refCount_(new int(1)) { }
    
    ~SimpleSharedPtr() {
        if (--(*refCount_) == 0) {
            delete ptr_;
            delete refCount_;
        }
    }
    
    SimpleSharedPtr(const SimpleSharedPtr& other)
        : ptr_(other.ptr_), refCount_(other.refCount_) {
        (*refCount_)++;
    }
    
    T* operator->() { return ptr_; }
    T& operator*() { return *ptr_; }
};
```

---

### 7. Memory Overhead Analysis

Different memory management approaches have different overheads:

| Approach | Per-Allocation Overhead | Per-Object Overhead | Time Overhead |
|----------|------------------------|---------------------|---------------|
| **Raw new/delete** | 8-16 bytes (allocator) | 0 | Moderate |
| **unique_ptr** | 0 (same as raw) | 0 | Minimal |
| **shared_ptr** | 16-24 bytes (control block) | 0 | Atomic operations |
| **Pool Allocator** | 0 (fixed size) | 0 | Very low |
| **GC (hypothetical)** | Varies | Varies | Unpredictable |

**shared_ptr Control Block Size:**
```
Control Block:
┌─────────────────────┐
│ strong ref count    │  (4-8 bytes)
├─────────────────────┤
│ weak ref count      │  (4-8 bytes)
├─────────────────────┤
│ deleter (optional)  │  (8+ bytes)
├─────────────────────┤
│ allocator (optional)│  (8+ bytes)
└─────────────────────┘
Total: 24-48 bytes typical
```

---

### 8. Garbage Collection Comparison

C++ does not have automatic garbage collection. Here's how it compares:

| Aspect | C++ (Manual/RAII) | Java/C# (GC) |
|--------|-------------------|--------------|
| **Control** | Full control | Limited |
| **Predictability** | Deterministic | Non-deterministic |
| **Performance** | Consistent | Pauses possible |
| **Memory Overhead** | Minimal | Significant |
| **Leaks Possible** | Yes | Rare |
| **Cycles** | Problem for shared_ptr | Handled |

**GC Advantages:**
- No manual memory management
- No dangling pointers
- Handles cycles automatically

**GC Disadvantages:**
- Unpredictable pauses
- Higher memory overhead
- Less control over performance

---

### 9. Memory Management Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **RAII** | Resource tied to object lifetime | Most resources |
| **Factory** | Centralized object creation | Complex initialization |
| **Pool** | Pre-allocated fixed-size blocks | Many small objects |
| **Singleton** | Single instance | Global resource |
| **Flyweight** | Shared immutable objects | Many identical objects |
| **Proxy** | Lazy allocation | Expensive resources |

**Factory Pattern with Memory Management:**
```cpp
class WidgetFactory {
private:
    MemoryPool pool_;
public:
    Widget* create() {
        void* mem = pool_.allocate();
        return new (mem) Widget();
    }
    
    void destroy(Widget* w) {
        w->~Widget();
        pool_.deallocate(w);
    }
};
```

---

### 10. Common Memory Errors

| Error | Description | Prevention |
|-------|-------------|------------|
| **Memory Leak** | Memory not freed | RAII, smart pointers |
| **Double Delete** | Deleting same memory twice | Set to nullptr after delete |
| **Dangling Pointer** | Access after free | Use references, reset pointers |
| **Buffer Overflow** | Writing past array bounds | Use containers, bounds checking |
| **Use After Free** | Accessing freed memory | Smart pointers, RAII |
| **Mismatched Delete** | delete vs delete[] | Use vector, unique_ptr<T[]> |

**Memory Error Example:**
```cpp
// Memory leak
int* leak = new int(42);
// no delete

// Double delete
int* p = new int(42);
delete p;
delete p;  // Undefined behavior

// Dangling pointer
int* dangling = new int(42);
delete dangling;
*dangling = 10;  // Undefined behavior

// Buffer overflow
int arr[10];
arr[10] = 42;  // Out of bounds

// Mismatched delete
int* arr2 = new int[10];
delete arr2;  // Should be delete[]
```

---

### 11. Best Practices Summary

| Practice | Rationale |
|----------|-----------|
| **Prefer stack allocation** | Automatic lifetime, no leaks |
| **Use smart pointers** | RAII for heap memory |
| **Follow Rule of Three/Five/Zero** | Consistent resource management |
| **Use containers (vector, string)** | Automatic memory management |
| **Avoid raw new/delete** | Error-prone |
| **Set pointers to nullptr after delete** | Prevent dangling pointers |
| **Use make_unique/make_shared** | Exception-safe, efficient |
| **Prefer unique_ptr over shared_ptr** | Clearer ownership, less overhead |

---

### Key Takeaways

1. **Memory hierarchy** includes stack (automatic) and heap (manual)
2. **RAII** is the fundamental C++ idiom for resource management
3. **Smart pointers** provide RAII for dynamic memory
4. **unique_ptr** represents exclusive ownership
5. **shared_ptr** represents shared ownership with reference counting
6. **weak_ptr** breaks cycles in shared ownership
7. **Memory pools** improve performance for many small objects
8. **Fragmentation** can make memory unusable even when free
9. **Rule of Three/Five/Zero** guides class design
10. **C++ has no garbage collector** - manual management required

---

### Next Steps

- Go to [01_New_and_Delete.md](01_New_and_Delete.md) to understand New and Delete Operators.