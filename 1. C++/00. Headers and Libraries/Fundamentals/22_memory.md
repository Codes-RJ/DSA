# 22_memory.md - Smart Pointer and Memory Utilities

The `memory` header provides modern C++ tools for resource management, including smart pointers and memory allocation utilities.

## 📖 Overview

The `memory` header is central to RAII (Resource Acquisition Is Initialization) and safe ownership in modern C++. It provides smart pointers that automatically manage memory and help prevent memory leaks, dangling pointers, and other common memory management issues.

## 🎯 Key Features

- **Automatic memory management** - Smart pointers automatically delete managed objects
- **RAII compliance** - Resources are cleaned up when pointers go out of scope
- **Exception safety** - Memory is properly cleaned up even when exceptions are thrown
- **Ownership semantics** - Clear ownership models (unique, shared, weak)
- **Custom deleters** - Support for custom cleanup logic
- **Allocator support** - Memory allocation utilities

## 🔧 Smart Pointer Types

### unique_ptr - Exclusive Ownership
```cpp
#include <iostream>
#include <memory>
#include <vector>

class Resource {
private:
    std::string name;
    int value;
    
public:
    Resource(const std::string& n, int v) : name(n), value(v) {
        std::cout << "Resource " << name << " created" << std::endl;
    }
    
    ~Resource() {
        std::cout << "Resource " << name << " destroyed" << std::endl;
    }
    
    void doSomething() const {
        std::cout << "Resource " << name << " doing something with value " << value << std::endl;
    }
    
    int getValue() const { return value; }
    void setValue(int v) { value = v; }
};

void demonstrateUniquePtr() {
    std::cout << "=== unique_ptr Examples ===" << std::endl;
    
    // Basic unique_ptr usage
    auto ptr1 = std::make_unique<Resource>("A", 42);
    ptr1->doSomething();
    
    // unique_ptr with custom deleter
    auto custom_deleter = [](Resource* p) {
        std::cout << "Custom deleter called for Resource" << std::endl;
        delete p;
    };
    
    std::unique_ptr<Resource, decltype(custom_deleter)> ptr2(
        new Resource("B", 100), custom_deleter);
    
    // Move semantics
    std::unique_ptr<Resource> ptr3 = std::move(ptr1);
    if (!ptr1) {
        std::cout << "ptr1 is now empty after move" << std::endl;
    }
    
    // unique_ptr with arrays
    auto array_ptr = std::make_unique<std::unique_ptr<Resource>[]>(3);
    for (int i = 0; i < 3; ++i) {
        array_ptr[i] = std::make_unique<Resource>("Array_" + std::to_string(i), i * 10);
    }
    
    // unique_ptr in containers
    std::vector<std::unique_ptr<Resource>> resources;
    resources.push_back(std::make_unique<Resource>("Vec1", 1));
    resources.push_back(std::make_unique<Resource>("Vec2", 2));
    
    for (const auto& res : resources) {
        res->doSomething();
    }
}
```

### shared_ptr - Shared Ownership
```cpp
void demonstrateSharedPtr() {
    std::cout << "\n=== shared_ptr Examples ===" << std::endl;
    
    // Basic shared_ptr usage
    auto ptr1 = std::make_shared<Resource>("Shared", 200);
    std::cout << "Reference count: " << ptr1.use_count() << std::endl;
    
    {
        auto ptr2 = ptr1;  // Copy increases reference count
        std::cout << "Reference count: " << ptr1.use_count() << std::endl;
        ptr2->doSomething();
    }
    
    std::cout << "Reference count after ptr2 destroyed: " << ptr1.use_count() << std::endl;
    
    // shared_ptr with custom deleter
    auto custom_deleter = [](Resource* p) {
        std::cout << "Custom deleter for shared Resource" << std::endl;
        delete p;
    };
    
    std::shared_ptr<Resource> custom_ptr(new Resource("CustomShared", 300), custom_deleter);
    
    // shared_ptr with arrays (C++17 and later)
    auto array_shared = std::make_shared<Resource[]>(3);
    // Note: Custom deleter needed for proper array cleanup before C++17
}
```

### weak_ptr - Non-Owning References
```cpp
void demonstrateWeakPtr() {
    std::cout << "\n=== weak_ptr Examples ===" << std::endl;
    
    // Create shared_ptr
    auto shared = std::make_shared<Resource>("WeakExample", 400);
    
    // Create weak_ptr
    std::weak_ptr<Resource> weak = shared;
    
    std::cout << "Reference count: " << shared.use_count() << std::endl;
    
    // Check if weak_ptr is valid
    if (auto locked = weak.lock()) {
        std::cout << "Weak pointer is valid, value: " << locked->getValue() << std::endl;
        locked->doSomething();
    }
    
    // Reset shared_ptr
    shared.reset();
    
    // Try to lock weak_ptr after shared is destroyed
    if (auto locked = weak.lock()) {
        std::cout << "This shouldn't print" << std::endl;
    } else {
        std::cout << "Weak pointer is now invalid" << std::endl;
    }
    
    // Check expired
    if (weak.expired()) {
        std::cout << "Weak pointer has expired" << std::endl;
    }
}
```

## 🔧 Advanced Memory Management

### Custom Allocators
```cpp
#include <memory>
#include <vector>
#include <cstddef>

template<typename T>
class TrackingAllocator {
public:
    using value_type = T;
    
    TrackingAllocator() noexcept = default;
    
    template<typename U>
    TrackingAllocator(const TrackingAllocator<U>&) noexcept {}
    
    T* allocate(std::size_t n) {
        std::cout << "Allocating " << n << " objects of size " << sizeof(T) << std::endl;
        return static_cast<T*>(::operator new(n * sizeof(T)));
    }
    
    void deallocate(T* p, std::size_t n) noexcept {
        std::cout << "Deallocating " << n << " objects" << std::endl;
        ::operator delete(p);
    }
    
    template<typename U>
    bool operator==(const TrackingAllocator<U>&) const noexcept {
        return true;
    }
    
    template<typename U>
    bool operator!=(const TrackingAllocator<U>&) const noexcept {
        return false;
    }
};

void demonstrateCustomAllocator() {
    std::cout << "\n=== Custom Allocator Examples ===" << std::endl;
    
    // Vector with custom allocator
    std::vector<int, TrackingAllocator<int>> vec;
    vec.reserve(5);
    
    for (int i = 0; i < 5; ++i) {
        vec.push_back(i * 10);
    }
    
    for (int val : vec) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}
```

### Memory Pool
```cpp
class MemoryPool {
private:
    struct Block {
        Block* next;
    };
    
    std::vector<std::unique_ptr<char[]>> chunks;
    Block* free_list;
    size_t block_size;
    size_t blocks_per_chunk;
    
public:
    MemoryPool(size_t block_sz, size_t blocks_per_chk = 1000) 
        : block_size(block_sz), blocks_per_chunk(blocks_per_chk), free_list(nullptr) {
        allocateNewChunk();
    }
    
    ~MemoryPool() {
        // Chunks are automatically cleaned up by unique_ptr
    }
    
    void* allocate() {
        if (!free_list) {
            allocateNewChunk();
        }
        
        Block* block = free_list;
        free_list = free_list->next;
        return block;
    }
    
    void deallocate(void* ptr) {
        Block* block = static_cast<Block*>(ptr);
        block->next = free_list;
        free_list = block;
    }
    
private:
    void allocateNewChunk() {
        auto chunk = std::make_unique<char[]>(block_size * blocks_per_chunk);
        char* start = chunk.get();
        
        // Add blocks to free list
        for (size_t i = 0; i < blocks_per_chunk; ++i) {
            Block* block = reinterpret_cast<Block*>(start + i * block_size);
            block->next = free_list;
            free_list = block;
        }
        
        chunks.push_back(std::move(chunk));
    }
};

template<typename T>
class PoolAllocator {
public:
    using value_type = T;
    
    PoolAllocator(MemoryPool* pool) : memory_pool(pool) {}
    
    template<typename U>
    PoolAllocator(const PoolAllocator<U>& other) : memory_pool(other.getPool()) {}
    
    T* allocate(std::size_t n) {
        if (n != 1) {
            throw std::bad_alloc();
        }
        return static_cast<T*>(memory_pool->allocate());
    }
    
    void deallocate(T* p, std::size_t n) noexcept {
        if (n == 1) {
            memory_pool->deallocate(p);
        }
    }
    
    MemoryPool* getPool() const { return memory_pool; }
    
private:
    MemoryPool* memory_pool;
};

void demonstrateMemoryPool() {
    std::cout << "\n=== Memory Pool Examples ===" << std::endl;
    
    MemoryPool pool(sizeof(int), 10);
    PoolAllocator<int> allocator(&pool);
    
    std::vector<int, PoolAllocator<int>> vec(allocator);
    vec.reserve(10);
    
    for (int i = 0; i < 10; ++i) {
        vec.push_back(i * 100);
    }
    
    std::cout << "Pool allocated vector: ";
    for (int val : vec) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}
```

## 🎮 Practical Examples

### Example 1: Resource Management System
```cpp
#include <iostream>
#include <memory>
#include <string>
#include <unordered_map>
#include <fstream>

class FileResource {
private:
    std::string filename;
    std::unique_ptr<std::ifstream> file;
    
public:
    FileResource(const std::string& name) : filename(name) {
        file = std::make_unique<std::ifstream>(filename);
        if (*file) {
            std::cout << "Opened file: " << filename << std::endl;
        } else {
            std::cout << "Failed to open file: " << filename << std::endl;
        }
    }
    
    ~FileResource() {
        if (file && file->is_open()) {
            file->close();
            std::cout << "Closed file: " << filename << std::endl;
        }
    }
    
    bool isOpen() const {
        return file && file->is_open();
    }
    
    void readLine() {
        if (isOpen()) {
            std::string line;
            if (std::getline(*file, line)) {
                std::cout << "Read: " << line << std::endl;
            }
        }
    }
};

class ResourceManager {
private:
    std::unordered_map<std::string, std::shared_ptr<FileResource>> resources;
    
public:
    std::shared_ptr<FileResource> getResource(const std::string& filename) {
        auto it = resources.find(filename);
        if (it != resources.end()) {
            return it->second;
        }
        
        auto resource = std::make_shared<FileResource>(filename);
        resources[filename] = resource;
        return resource;
    }
    
    void cleanupUnused() {
        for (auto it = resources.begin(); it != resources.end();) {
            if (it->second.use_count() == 1) {
                std::cout << "Cleaning up unused resource: " << it->first << std::endl;
                it = resources.erase(it);
            } else {
                ++it;
            }
        }
    }
    
    size_t getResourceCount() const {
        return resources.size();
    }
};

int main() {
    std::cout << "=== Resource Management System ===" << std::endl;
    
    ResourceManager manager;
    
    // Get some resources
    auto file1 = manager.getResource("test1.txt");
    auto file2 = manager.getResource("test2.txt");
    auto file3 = manager.getResource("test1.txt");  // Should return same resource
    
    std::cout << "Resource count: " << manager.getResourceCount() << std::endl;
    std::cout << "file1 use count: " << file1.use_count() << std::endl;
    std::cout << "file3 use count: " << file3.use_count() << std::endl;
    
    // Use resources
    if (file1->isOpen()) {
        file1->readLine();
    }
    
    // Release some resources
    file2.reset();
    manager.cleanupUnused();
    
    std::cout << "Resource count after cleanup: " << manager.getResourceCount() << std::endl;
    
    return 0;
}
```

### Example 2: Observer Pattern with weak_ptr
```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <string>

class Observer {
public:
    virtual ~Observer() = default;
    virtual void update(const std::string& message) = 0;
};

class Subject {
private:
    std::vector<std::weak_ptr<Observer>> observers;
    
public:
    void addObserver(std::shared_ptr<Observer> observer) {
        observers.push_back(observer);
    }
    
    void notify(const std::string& message) {
        // Remove expired observers and notify valid ones
        for (auto it = observers.begin(); it != observers.end();) {
            if (auto observer = it->lock()) {
                observer->update(message);
                ++it;
            } else {
                // Remove expired observer
                it = observers.erase(it);
            }
        }
    }
    
    size_t getObserverCount() const {
        return observers.size();
    }
};

class ConcreteObserver : public Observer {
private:
    std::string name;
    
public:
    ConcreteObserver(const std::string& n) : name(n) {
        std::cout << "Observer " << name << " created" << std::endl;
    }
    
    ~ConcreteObserver() {
        std::cout << "Observer " << name << " destroyed" << std::endl;
    }
    
    void update(const std::string& message) override {
        std::cout << "Observer " << name << " received: " << message << std::endl;
    }
};

int main() {
    std::cout << "=== Observer Pattern with weak_ptr ===" << std::endl;
    
    Subject subject;
    
    // Create observers
    auto obs1 = std::make_shared<ConcreteObserver>("Alice");
    auto obs2 = std::make_shared<ConcreteObserver>("Bob");
    
    // Add observers
    subject.addObserver(obs1);
    subject.addObserver(obs2);
    
    std::cout << "Observer count: " << subject.getObserverCount() << std::endl;
    
    // Notify observers
    subject.notify("Hello World!");
    
    // Remove one observer by resetting shared_ptr
    obs1.reset();
    
    std::cout << "After resetting obs1:" << std::endl;
    subject.notify("Second message");
    
    std::cout << "Final observer count: " << subject.getObserverCount() << std::endl;
    
    return 0;
}
```

### Example 3: Factory Pattern with Smart Pointers
```cpp
#include <iostream>
#include <memory>
#include <string>
#include <unordered_map>
#include <functional>

class Product {
public:
    virtual ~Product() = default;
    virtual void use() = 0;
};

class ConcreteProductA : public Product {
public:
    void use() override {
        std::cout << "Using Product A" << std::endl;
    }
};

class ConcreteProductB : public Product {
public:
    void use() override {
        std::cout << "Using Product B" << std::endl;
    }
};

class ProductFactory {
private:
    std::unordered_map<std::string, std::function<std::unique_ptr<Product>()>> creators;
    
public:
    ProductFactory() {
        // Register product creators
        creators["A"] = []() { return std::make_unique<ConcreteProductA>(); };
        creators["B"] = []() { return std::make_unique<ConcreteProductB>(); };
    }
    
    std::unique_ptr<Product> createProduct(const std::string& type) {
        auto it = creators.find(type);
        if (it != creators.end()) {
            return it->second();
        }
        return nullptr;
    }
    
    void registerProduct(const std::string& type, 
                        std::function<std::unique_ptr<Product>()> creator) {
        creators[type] = creator;
    }
    
    std::vector<std::string> getAvailableProducts() const {
        std::vector<std::string> products;
        for (const auto& pair : creators) {
            products.push_back(pair.first);
        }
        return products;
    }
};

int main() {
    std::cout << "=== Factory Pattern with Smart Pointers ===" << std::endl;
    
    ProductFactory factory;
    
    // Create products
    auto productA = factory.createProduct("A");
    auto productB = factory.createProduct("B");
    auto productC = factory.createProduct("C");  // Doesn't exist
    
    if (productA) {
        productA->use();
    }
    
    if (productB) {
        productB->use();
    }
    
    if (!productC) {
        std::cout << "Product C not available" << std::endl;
    }
    
    // Register new product type
    factory.registerProduct("C", []() { 
        return std::make_unique<ConcreteProductA>();  // Reuse A for demo
    });
    
    auto productC2 = factory.createProduct("C");
    if (productC2) {
        productC2->use();
    }
    
    // Show available products
    auto available = factory.getAvailableProducts();
    std::cout << "Available products: ";
    for (const auto& product : available) {
        std::cout << product << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

### Example 4: Memory Leak Detection
```cpp
#include <iostream>
#include <memory>
#include <unordered_set>
#include <mutex>

class LeakDetector {
private:
    static std::unordered_set<void*> allocated_ptrs;
    static std::mutex mutex;
    
public:
    static void trackAllocation(void* ptr) {
        std::lock_guard<std::mutex> lock(mutex);
        allocated_ptrs.insert(ptr);
    }
    
    static void trackDeallocation(void* ptr) {
        std::lock_guard<std::mutex> lock(mutex);
        allocated_ptrs.erase(ptr);
    }
    
    static void reportLeaks() {
        std::lock_guard<std::mutex> lock(mutex);
        if (!allocated_ptrs.empty()) {
            std::cout << "Memory leaks detected! " << allocated_ptrs.size() 
                      << " allocations not freed:" << std::endl;
            for (void* ptr : allocated_ptrs) {
                std::cout << "  Leak at address: " << ptr << std::endl;
            }
        } else {
            std::cout << "No memory leaks detected!" << std::endl;
        }
    }
};

std::unordered_set<void*> LeakDetector::allocated_ptrs;
std::mutex LeakDetector::mutex;

template<typename T>
class TrackedDeleter {
public:
    void operator()(T* ptr) const {
        LeakDetector::trackDeallocation(ptr);
        delete ptr;
    }
};

template<typename T, typename... Args>
std::unique_ptr<T, TrackedDeleter<T>> make_tracked(Args&&... args) {
    auto ptr = new T(std::forward<Args>(args)...);
    LeakDetector::trackAllocation(ptr);
    return std::unique_ptr<T, TrackedDeleter<T>>(ptr);
}

class TrackedObject {
private:
    std::string name;
    
public:
    TrackedObject(const std::string& n) : name(n) {
        std::cout << "TrackedObject " << name << " created" << std::endl;
    }
    
    ~TrackedObject() {
        std::cout << "TrackedObject " << name << " destroyed" << std::endl;
    }
    
    void doSomething() const {
        std::cout << "TrackedObject " << name << " doing something" << std::endl;
    }
};

int main() {
    std::cout << "=== Memory Leak Detection ===" << std::endl;
    
    // Tracked allocations
    auto tracked1 = make_tracked<TrackedObject>("Tracked1");
    auto tracked2 = make_tracked<TrackedObject>("Tracked2");
    
    tracked1->doSomething();
    tracked2->doSomething();
    
    // Intentionally leak one object for demonstration
    auto leaked = make_tracked<TrackedObject>("Leaked");
    leaked->doSomething();
    leaked.release();  // Leak the raw pointer
    
    // Properly clean up tracked objects
    tracked1.reset();
    tracked2.reset();
    
    // Report leaks
    LeakDetector::reportLeaks();
    
    return 0;
}
```

## 📊 Complete Function Reference

### Smart Pointer Creation
| Function | Description | Notes |
|----------|-------------|-------|
| `make_unique<T>()` | Create unique_ptr | C++14 and later |
| `make_shared<T>()` | Create shared_ptr | More efficient than separate allocation |
| `allocate_shared<T>()` | Create shared_ptr with custom allocator | |

### unique_ptr Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `get()` | Get raw pointer | O(1) |
| `release()` | Release ownership | O(1) |
| `reset()` | Reset pointer | O(1) |
| `swap()` | Swap pointers | O(1) |
| `operator*` | Dereference | O(1) |
| `operator->` | Member access | O(1) |

### shared_ptr Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `get()` | Get raw pointer | O(1) |
| `use_count()` | Get reference count | O(1) |
| `unique()` | Check if unique owner | O(1) |
| `reset()` | Reset pointer | O(1) |
| `swap()` | Swap pointers | O(1) |

### weak_ptr Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `lock()` | Convert to shared_ptr | O(1) |
| `expired()` | Check if expired | O(1) |
| `reset()` | Reset weak_ptr | O(1) |

## ⚡ Performance Considerations

### Memory Overhead
```cpp
// unique_ptr - no overhead (same size as raw pointer)
std::unique_ptr<int> unique_ptr_size;  // Typically 8 bytes on 64-bit

// shared_ptr - includes control block
std::shared_ptr<int> shared_ptr_size;  // Typically 16 bytes on 64-bit

// weak_ptr - same size as shared_ptr
std::weak_ptr<int> weak_ptr_size;      // Typically 16 bytes on 64-bit
```

### Allocation Efficiency
```cpp
// More efficient - single allocation
auto shared = std::make_shared<Resource>("name", 42);

// Less efficient - two allocations
std::shared_ptr<Resource> shared(new Resource("name", 42));
```

## 🎯 Common Patterns

### Pattern 1: PImpl with unique_ptr
```cpp
class MyClass {
private:
    struct Impl;
    std::unique_ptr<Impl> pimpl;
    
public:
    MyClass();
    ~MyClass();  // Must be defined in cpp file
    
    // Public interface...
};
```

### Pattern 2: Factory Functions
```cpp
template<typename T, typename... Args>
std::unique_ptr<T> createUnique(Args&&... args) {
    return std::make_unique<T>(std::forward<Args>(args)...);
}
```

### Pattern 3: Enable Shared From This
```cpp
class MyClass : public std::enable_shared_from_this<MyClass> {
public:
    std::shared_ptr<MyClass> getShared() {
        return shared_from_this();
    }
};
```

## 🐛 Common Pitfalls & Solutions

### 1. Circular References
```cpp
// Problem - circular reference prevents deletion
struct Node {
    std::shared_ptr<Node> next;
    std::shared_ptr<Node> prev;  // Circular reference!
};

// Solution - use weak_ptr for one direction
struct Node {
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;    // Breaks circular reference
};
```

### 2. Dangling Pointers
```cpp
// Problem - accessing expired weak_ptr
std::weak_ptr<int> weak;
{
    auto shared = std::make_shared<int>(42);
    weak = shared;
}
*weak.lock();  // weak is expired!

// Solution - always check lock()
if (auto ptr = weak.lock()) {
    *ptr;  // Safe to use
}
```

### 3. Mixing Raw and Smart Pointers
```cpp
// Problem - mixing ownership models
std::unique_ptr<int> smart_ptr(new int(42));
int* raw_ptr = smart_ptr.get();
delete raw_ptr;  // Double deletion!

// Solution - stick to one ownership model
std::unique_ptr<int> smart_ptr = std::make_unique<int>(42);
// Don't manually delete managed memory
```

## 📚 Related Headers

- `iterator.md` - Iterator utilities
- `functional.md` - Function objects
- `type_traits.md` - Type traits
- `new.md` - Memory allocation operators

## 🚀 Best Practices

1. **Prefer make_unique/make_shared** over direct new
2. **Use unique_ptr** for exclusive ownership
3. **Use shared_ptr** only when sharing is necessary
4. **Use weak_ptr** to break circular references
5. **Avoid raw pointers** when smart pointers suffice
6. **Be careful with enable_shared_from_this**
7. **Consider custom allocators** for performance-critical code

## 🎯 When to Use Smart Pointers

✅ **Use unique_ptr when:**
- Single owner of resource
- Transfer of ownership needed
- Performance is critical
- PImpl idiom implementation

✅ **Use shared_ptr when:**
- Multiple owners needed
- Shared ownership semantics
- Reference counting required
- Caching with shared resources

✅ **Use weak_ptr when:**
- Observing shared resources
- Breaking circular references
- Caching without ownership
- Observer pattern implementation

❌ **Avoid when:**
- Simple stack allocation suffices
- References are more appropriate
- Performance is extremely critical
- Ownership is unclear
---

## Next Step

- Go to [23_iterator.md](23_iterator.md) to continue with iterator.
