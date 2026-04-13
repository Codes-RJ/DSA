# Memory Management - Resource Lifetime in C++

Modern C++ resource management is built on **ownership** and **RAII** — tying resource lifetime to object lifetime so that resources are always cleaned up, even in the presence of exceptions.

## 📖 Overview

C++ gives you direct control over memory, which is powerful but requires discipline. The language provides a layered toolkit:

1. **Automatic (stack) storage** — simplest, fastest, automatically destroyed
2. **Dynamic (heap) storage** — flexible lifetime, must be explicitly managed
3. **RAII wrappers** — smart pointers and containers that automate heap cleanup
4. **Custom allocators** — for specialised or high-performance scenarios

The modern C++ philosophy: **never write `new`/`delete` directly in application code**; always use RAII wrappers instead.

## 🎯 Key Concepts

### RAII — Resource Acquisition Is Initialisation
The principle: acquire a resource in a constructor, release it in a destructor. Since destructors are always called when an object goes out of scope (even during stack unwinding), resources are never leaked.

### Ownership Rules
| Question | Answer using |
|----------|-------------|
| Who owns this resource? | `unique_ptr` (exclusive), `shared_ptr` (shared) |
| Who just looks but doesn't own? | Raw pointer or `weak_ptr` |
| Should the resource follow a single scope? | Stack allocation or `unique_ptr` |
| Should the resource outlive multiple scopes? | `shared_ptr` |

### The Rule of Zero / Three / Five
- **Rule of Zero**: use standard RAII types (`vector`, `string`, smart pointers) and let the compiler generate everything
- **Rule of Three**: if you write destructor, copy constructor, or copy assignment — write all three
- **Rule of Five**: add move constructor and move assignment for efficiency

## 🔧 Basic Operations

### Stack vs Heap vs RAII
```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <string>

void demonstrate() {
    // Stack allocation: automatic lifetime
    int x = 42;
    std::string s = "hello"; // string manages its buffer via RAII internally

    // Heap via raw pointer (avoid in modern C++)
    int* raw = new int(10);
    delete raw; // must match every new with delete

    // Heap via unique_ptr (preferred for exclusive ownership)
    auto up = std::make_unique<int>(42);
    // deleted automatically when up goes out of scope

    // Heap via shared_ptr (for shared ownership)
    auto sp1 = std::make_shared<std::string>("shared data");
    auto sp2 = sp1; // reference count = 2
    // deleted when last shared_ptr is destroyed

    // Heap via standard containers (preferred for arrays)
    std::vector<int> vec(100, 0); // manages 100 ints on heap automatically

    (void)x;
} // s, up, sp1, sp2, vec all cleaned up here — no leaks

int main() {
    demonstrate();
    std::cout << "No leaks.\n";
    return 0;
}
```

### RAII Resource Wrapper Pattern
```cpp
#include <iostream>
#include <stdexcept>
#include <cstdio>

// RAII wrapper for C FILE*
class FileRAII {
    FILE* file_;

public:
    explicit FileRAII(const char* path, const char* mode) {
        file_ = fopen(path, mode);
        if (!file_) throw std::runtime_error(std::string("Cannot open: ") + path);
        std::cout << "File opened: " << path << "\n";
    }

    ~FileRAII() noexcept {
        if (file_) {
            fclose(file_);
            std::cout << "File closed\n";
        }
    }

    // Move-only (no copy)
    FileRAII(const FileRAII&)            = delete;
    FileRAII& operator=(const FileRAII&) = delete;
    FileRAII(FileRAII&& o) noexcept : file_(o.file_) { o.file_ = nullptr; }
    FileRAII& operator=(FileRAII&& o) noexcept {
        if (this != &o) { if (file_) fclose(file_); file_ = o.file_; o.file_ = nullptr; }
        return *this;
    }

    FILE* get() { return file_; }
};

int main() {
    try {
        FileRAII f("notes.txt", "w");
        fprintf(f.get(), "Hello, RAII!\n");
        // File is closed here automatically — even if an exception occurs
    } catch (const std::exception& e) {
        std::cerr << e.what() << "\n";
    }
    return 0;
}
```

### Smart Pointer Quick Reference
```cpp
#include <memory>
#include <iostream>

struct Resource {
    int id;
    Resource(int i) : id(i) { std::cout << "Resource(" << id << ") created\n"; }
    ~Resource()              { std::cout << "Resource(" << id << ") destroyed\n"; }
};

int main() {
    // unique_ptr — exclusive owner, zero overhead
    {
        auto u = std::make_unique<Resource>(1);
        std::unique_ptr<Resource> u2 = std::move(u); // transfer ownership
        // u1 is now null; u2 owns it
    } // destroyed here

    // shared_ptr — shared ownership via reference counting
    {
        auto s1 = std::make_shared<Resource>(2);
        {
            auto s2 = s1;          // count = 2
            auto s3 = s1;          // count = 3
        }                          // s2, s3 destroyed, count = 1
    }                              // s1 destroyed, count = 0 → Resource deleted

    // weak_ptr — observe without owning
    {
        auto sp = std::make_shared<Resource>(3);
        std::weak_ptr<Resource> wp = sp;

        if (auto locked = wp.lock()) {
            std::cout << "Resource " << locked->id << " still alive\n";
        }
        sp.reset();
        std::cout << "Expired: " << std::boolalpha << wp.expired() << "\n";
    }

    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Tracking Memory with a Pool Allocator
```cpp
#include <iostream>
#include <vector>
#include <cassert>

// Simple bump allocator (for illustration)
class BumpAllocator {
    std::vector<char> pool_;
    size_t offset_ = 0;

public:
    explicit BumpAllocator(size_t capacity) : pool_(capacity, 0) {}

    void* allocate(size_t bytes, size_t align = alignof(std::max_align_t)) {
        size_t aligned = (offset_ + align - 1) & ~(align - 1);
        if (aligned + bytes > pool_.size()) return nullptr;
        void* ptr = pool_.data() + aligned;
        offset_ = aligned + bytes;
        return ptr;
    }

    // All memory freed at once (no individual free)
    void reset() { offset_ = 0; }

    size_t used()    const { return offset_; }
    size_t capacity() const { return pool_.size(); }
};

int main() {
    BumpAllocator alloc(1024);

    int*    a = static_cast<int*>   (alloc.allocate(sizeof(int)));
    double* b = static_cast<double*>(alloc.allocate(sizeof(double)));
    char*   c = static_cast<char*>  (alloc.allocate(10));

    *a = 42;
    *b = 3.14;
    c[0] = 'H'; c[1] = 'i'; c[2] = '\0';

    std::cout << "a=" << *a << " b=" << *b << " c=" << c << "\n";
    std::cout << "Used: " << alloc.used() << " / " << alloc.capacity() << " bytes\n";

    alloc.reset(); // reuse all memory
    return 0;
}
```

### Example 2: Exception-Safe Resource Management
```cpp
#include <iostream>
#include <memory>
#include <stdexcept>

class Database {
public:
    Database() { std::cout << "DB connection opened\n"; }
    ~Database() { std::cout << "DB connection closed\n"; }
    void query(const std::string& sql) { std::cout << "Query: " << sql << "\n"; }
};

class Logger {
public:
    Logger() { std::cout << "Logger started\n"; }
    ~Logger() { std::cout << "Logger stopped\n"; }
    void log(const std::string& msg) { std::cout << "[LOG] " << msg << "\n"; }
};

void runApplication() {
    // Both are cleaned up if an exception occurs at any point
    auto db     = std::make_unique<Database>();
    auto logger = std::make_unique<Logger>();

    logger->log("Application started");
    db->query("SELECT * FROM users");

    throw std::runtime_error("Something went wrong!"); // both still cleaned up
}

int main() {
    try {
        runApplication();
    } catch (const std::exception& e) {
        std::cerr << "Caught: " << e.what() << "\n";
    }
    std::cout << "After catch — all resources were properly released\n";
    return 0;
}
```

### Example 3: Object Pool with `shared_ptr` and Custom Deleter
```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <functional>

class Widget {
public:
    int id;
    bool active = false;
    Widget(int i) : id(i) {}
};

class WidgetPool {
    std::vector<std::unique_ptr<Widget>> pool_;

public:
    WidgetPool(int n) {
        for (int i = 0; i < n; i++)
            pool_.push_back(std::make_unique<Widget>(i));
    }

    // Return a Widget that automatically returns itself to the pool
    std::shared_ptr<Widget> acquire() {
        for (auto& w : pool_) {
            if (!w->active) {
                w->active = true;
                Widget* raw = w.get();
                return std::shared_ptr<Widget>(raw, [this](Widget* w) {
                    w->active = false;
                    std::cout << "Widget " << w->id << " returned to pool\n";
                });
            }
        }
        return nullptr;
    }

    int available() const {
        int count = 0;
        for (const auto& w : pool_) if (!w->active) count++;
        return count;
    }
};

int main() {
    WidgetPool pool(3);
    std::cout << "Available: " << pool.available() << "\n"; // 3

    {
        auto w1 = pool.acquire();
        auto w2 = pool.acquire();
        std::cout << "Available: " << pool.available() << "\n"; // 1
        std::cout << "Using widgets " << w1->id << " and " << w2->id << "\n";
    } // w1 and w2 returned automatically

    std::cout << "Available: " << pool.available() << "\n"; // 3
    return 0;
}
```

### Example 4: Detecting Memory Problems with `valgrind`-Friendly Code
```cpp
#include <iostream>
#include <memory>
#include <vector>

// Demonstrates common memory issues and their fixes

void memoryLeakExample() {
    // BAD: memory leak
    // int* leaked = new int(42);
    // (no delete)

    // GOOD: no leak possible
    auto safe = std::make_unique<int>(42);
    std::cout << "Value: " << *safe << "\n";
} // safe deleted here automatically

void danglingPointerExample() {
    // BAD: dangling pointer
    // int* p;
    // { int x = 5; p = &x; }
    // std::cout << *p; // UB: x is destroyed

    // GOOD: use smart pointers or ensure lifetimes are correct
    std::shared_ptr<int> sp;
    {
        sp = std::make_shared<int>(5);
    }
    std::cout << "Still valid: " << *sp << "\n"; // OK: sp keeps it alive
}

void doubleDeleteExample() {
    // BAD: double delete
    // int* p = new int(42);
    // delete p;
    // delete p; // UB

    // GOOD: smart pointer prevents double delete
    auto up = std::make_unique<int>(42);
    // up.reset(); up.reset(); // second reset is a no-op — safe
}

int main() {
    memoryLeakExample();
    danglingPointerExample();
    doubleDeleteExample();
    std::cout << "All memory examples OK\n";
    return 0;
}
```

## ⚡ Performance Tips

### Prefer Stack Allocation
```cpp
// Stack is orders of magnitude faster than heap
int arr[1000];           // stack: 1 instruction
auto vec = std::vector<int>(1000); // heap: OS call + bookkeeping
```

### Use `reserve()` to Avoid Repeated Reallocation
```cpp
std::vector<int> v;
v.reserve(10000); // one heap allocation
for (int i = 0; i < 10000; i++) v.push_back(i); // no reallocations
```

### Prefer `make_unique` and `make_shared` Over `new`
```cpp
// Bad: potential leak if constructor throws
std::unique_ptr<int> p(new int(42));

// Good: exception-safe and a single allocation
auto p = std::make_unique<int>(42);
auto s = std::make_shared<int>(42); // single allocation for control block + object
```

### `unique_ptr` Has Zero Overhead vs. Raw Pointer
```cpp
// unique_ptr<T> with default deleter: same size as T*, same speed
// shared_ptr<T>: two word overhead (pointer + control block pointer)
// Cost of shared_ptr: ~3–5x unique_ptr due to reference count atomics
```

## 🐛 Common Pitfalls & Solutions

### 1. Memory Leak — Forgetting `delete`
```cpp
int* p = new int(42);
// ... function may return early or throw ...
delete p; // might never run

// Fix: use unique_ptr
auto p = std::make_unique<int>(42);
```

### 2. Dangling Pointer — Using Memory After Free
```cpp
int* p = new int(42);
delete p;
std::cout << *p; // UB: use-after-free

// Fix: set to nullptr after delete, or use smart pointers
```

### 3. Double Delete
```cpp
int* p = new int(42);
delete p;
delete p; // UB: double free

// Fix: smart pointers can only delete once
```

### 4. Circular `shared_ptr` References (Memory Leak)
```cpp
struct Node { std::shared_ptr<Node> next; }; // both nodes keep each other alive!
// Fix: use weak_ptr for back-references
struct Node { std::weak_ptr<Node> next; };
```

## 🎯 Best Practices

1. **Follow the Rule of Zero** — use containers and smart pointers; let the compiler generate special members
2. **Prefer `unique_ptr`** for exclusive ownership; `shared_ptr` only when ownership is genuinely shared
3. **Never call `delete` directly** in application code — always use RAII wrappers
4. **Prefer stack allocation** over heap for small, fixed-size objects
5. **Use `make_unique`/`make_shared`** instead of `new T(...)` directly
6. **Break cyclic ownership** with `weak_ptr`

## 📚 Related Topics

- [`smart_pointers.md`](smart_pointers.md) — Deep dive into `unique_ptr`, `shared_ptr`, `weak_ptr`
- [`move_semantics.md`](move_semantics.md) — Move constructors for RAII resource transfer
- [`exception.md`](../Fundamentals/31_exception.md) — Exception safety levels: basic, strong, noexcept

## 🚀 Next Steps

1. Write your own RAII wrapper for a C library handle (e.g., `SDL_Surface*`)
2. Audit an existing codebase for raw `new`/`delete` and replace with smart pointers
3. Use `valgrind --leak-check=full` to detect leaks in a C++ program
4. Explore C++23 `std::out_ptr` for integrating smart pointers with C APIs
---

## Next Step

- Go to [miscellaneous.md](miscellaneous.md) to continue with miscellaneous.
