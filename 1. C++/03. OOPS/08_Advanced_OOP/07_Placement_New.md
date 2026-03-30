# Placement New in C++ - Complete Guide

## 📖 Overview

Placement `new` is a special form of the `new` operator that constructs an object in a pre-allocated memory buffer. It allows developers to separate memory allocation from object construction, enabling custom memory management, object pooling, and performance optimizations.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Placement New** | Constructs object in existing memory |
| **Memory Allocation** | Separate from object construction |
| **Explicit Destructor Call** | Required for manual cleanup |
| **Memory Pool** | Pre-allocated memory for objects |

---

## 1. **Basic Placement New**

```cpp
#include <iostream>
#include <string>
#include <cstring>
using namespace std;

class Simple {
private:
    int value;
    string name;
    
public:
    Simple(int v, string n) : value(v), name(n) {
        cout << "Simple constructor: " << name << " (" << value << ")" << endl;
    }
    
    ~Simple() {
        cout << "Simple destructor: " << name << endl;
    }
    
    void display() const {
        cout << "Value: " << value << ", Name: " << name << endl;
    }
};

int main() {
    cout << "=== Basic Placement New ===" << endl;
    
    // Regular new (allocation + construction)
    cout << "\n1. Regular new:" << endl;
    Simple* s1 = new Simple(10, "Regular");
    s1->display();
    delete s1;
    
    // Placement new (separate allocation and construction)
    cout << "\n2. Placement new:" << endl;
    
    // Step 1: Allocate memory
    char* buffer = new char[sizeof(Simple)];
    cout << "Memory allocated at: " << (void*)buffer << endl;
    
    // Step 2: Construct object in allocated memory
    Simple* s2 = new(buffer) Simple(20, "Placement");
    s2->display();
    
    // Step 3: Manually call destructor
    s2->~Simple();
    
    // Step 4: Deallocate memory
    delete[] buffer;
    
    cout << "\n3. Multiple objects in one buffer:" << endl;
    char* bigBuffer = new char[3 * sizeof(Simple)];
    
    Simple* arr[3];
    for (int i = 0; i < 3; i++) {
        arr[i] = new(bigBuffer + i * sizeof(Simple)) Simple(i * 10, "Obj" + to_string(i));
    }
    
    for (int i = 0; i < 3; i++) {
        arr[i]->display();
    }
    
    // Destruct in reverse order
    for (int i = 2; i >= 0; i--) {
        arr[i]->~Simple();
    }
    
    delete[] bigBuffer;
    
    return 0;
}
```

**Output:**
```
=== Basic Placement New ===

1. Regular new:
Simple constructor: Regular (10)
Value: 10, Name: Regular
Simple destructor: Regular

2. Placement new:
Memory allocated at: 0x...
Simple constructor: Placement (20)
Value: 20, Name: Placement
Simple destructor: Placement

3. Multiple objects in one buffer:
Simple constructor: Obj0 (0)
Simple constructor: Obj1 (10)
Simple constructor: Obj2 (20)
Value: 0, Name: Obj0
Value: 10, Name: Obj1
Value: 20, Name: Obj2
Simple destructor: Obj2
Simple destructor: Obj1
Simple destructor: Obj0
```

---

## 2. **Memory Pool with Placement New**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cstddef>
using namespace std;

class Pool {
private:
    char* memory;
    size_t poolSize;
    size_t used;
    
public:
    Pool(size_t size) : poolSize(size), used(0) {
        memory = new char[size];
        cout << "Pool created: " << size << " bytes" << endl;
    }
    
    ~Pool() {
        delete[] memory;
        cout << "Pool destroyed" << endl;
    }
    
    void* allocate(size_t size) {
        if (used + size > poolSize) {
            cout << "Pool exhausted!" << endl;
            return nullptr;
        }
        void* ptr = memory + used;
        used += size;
        cout << "Allocated " << size << " bytes at offset " 
             << (used - size) << endl;
        return ptr;
    }
    
    void reset() {
        used = 0;
        cout << "Pool reset" << endl;
    }
    
    size_t getUsed() const { return used; }
    size_t getFree() const { return poolSize - used; }
};

class GameObject {
private:
    int id;
    string name;
    float x, y;
    
public:
    GameObject(int i, string n, float xPos, float yPos) 
        : id(i), name(n), x(xPos), y(yPos) {
        cout << "  GameObject created: " << name << " (ID: " << id << ")" << endl;
    }
    
    ~GameObject() {
        cout << "  GameObject destroyed: " << name << endl;
    }
    
    void update() {
        x += 0.1f;
        y += 0.1f;
    }
    
    void display() const {
        cout << "  " << name << " at (" << x << ", " << y << ")" << endl;
    }
};

int main() {
    cout << "=== Memory Pool with Placement New ===" << endl;
    
    // Create pool for game objects
    Pool objectPool(sizeof(GameObject) * 5);
    
    cout << "\n1. Creating objects in pool:" << endl;
    vector<GameObject*> objects;
    
    for (int i = 0; i < 5; i++) {
        void* mem = objectPool.allocate(sizeof(GameObject));
        if (mem) {
            GameObject* obj = new(mem) GameObject(i, "Object" + to_string(i), i * 10.0f, i * 10.0f);
            objects.push_back(obj);
        }
    }
    
    cout << "\n2. Updating objects:" << endl;
    for (auto obj : objects) {
        obj->update();
        obj->display();
    }
    
    cout << "\n3. Destroying objects (manual destructor calls):" << endl;
    for (auto obj : objects) {
        obj->~GameObject();
    }
    
    cout << "\n4. Pool statistics:" << endl;
    cout << "Used: " << objectPool.getUsed() << " bytes" << endl;
    cout << "Free: " << objectPool.getFree() << " bytes" << endl;
    
    cout << "\n5. Reusing pool (reset):" << endl;
    objectPool.reset();
    
    // Create new objects in same pool
    void* mem = objectPool.allocate(sizeof(GameObject));
    GameObject* newObj = new(mem) GameObject(99, "NewObject", 0, 0);
    newObj->display();
    newObj->~GameObject();
    
    return 0;
}
```

---

## 3. **Placement New with Alignment**

```cpp
#include <iostream>
#include <string>
#include <new>
#include <cstdint>
using namespace std;

// Ensure proper alignment
struct alignas(16) AlignedData {
    int a;
    double b;
    char c[10];
    
    AlignedData(int x, double y, const char* z) : a(x), b(y) {
        strcpy(c, z);
        cout << "AlignedData constructed: " << a << ", " << b << ", " << c << endl;
    }
    
    ~AlignedData() {
        cout << "AlignedData destroyed" << endl;
    }
};

class Buffer {
private:
    char* data;
    size_t size;
    
public:
    Buffer(size_t s) : size(s) {
        // Allocate with extra space for alignment
        data = new char[size + 16];
        cout << "Buffer created: " << size << " bytes" << endl;
    }
    
    ~Buffer() {
        delete[] data;
        cout << "Buffer destroyed" << endl;
    }
    
    void* getAligned(size_t alignment) {
        uintptr_t addr = reinterpret_cast<uintptr_t>(data);
        uintptr_t aligned = (addr + alignment - 1) & ~(alignment - 1);
        return reinterpret_cast<void*>(aligned);
    }
    
    void* getRaw() { return data; }
};

int main() {
    cout << "=== Placement New with Alignment ===" << endl;
    
    Buffer buffer(sizeof(AlignedData) * 3);
    
    cout << "\n1. Raw buffer address: " << buffer.getRaw() << endl;
    cout << "Aligned address: " << buffer.getAligned(16) << endl;
    
    cout << "\n2. Creating aligned objects:" << endl;
    void* alignedMem = buffer.getAligned(16);
    AlignedData* obj1 = new(alignedMem) AlignedData(10, 3.14, "First");
    
    // Check alignment
    cout << "Object address: " << obj1 << endl;
    cout << "Alignment: " << (reinterpret_cast<uintptr_t>(obj1) % 16 == 0 ? "16-byte aligned" : "Not aligned") << endl;
    
    // Create another object at next aligned position
    void* nextMem = reinterpret_cast<char*>(alignedMem) + sizeof(AlignedData);
    nextMem = reinterpret_cast<void*>((reinterpret_cast<uintptr_t>(nextMem) + 15) & ~15);
    AlignedData* obj2 = new(nextMem) AlignedData(20, 2.718, "Second");
    
    cout << "\n3. Object addresses:" << endl;
    cout << "obj1: " << obj1 << endl;
    cout << "obj2: " << obj2 << endl;
    cout << "Difference: " << (reinterpret_cast<char*>(obj2) - reinterpret_cast<char*>(obj1)) << " bytes" << endl;
    
    // Cleanup
    obj1->~AlignedData();
    obj2->~AlignedData();
    
    return 0;
}
```

---

## 4. **Placement New with Custom Allocator**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <cstddef>
using namespace std;

class CustomAllocator {
private:
    struct Block {
        void* ptr;
        size_t size;
        bool used;
    };
    
    vector<Block> blocks;
    
public:
    CustomAllocator(size_t totalSize) {
        void* memory = operator new(totalSize);
        blocks.push_back({memory, totalSize, false});
        cout << "CustomAllocator created with " << totalSize << " bytes" << endl;
    }
    
    ~CustomAllocator() {
        for (auto& block : blocks) {
            if (block.ptr) {
                operator delete(block.ptr);
            }
        }
        cout << "CustomAllocator destroyed" << endl;
    }
    
    void* allocate(size_t size) {
        for (auto& block : blocks) {
            if (!block.used && block.size >= size) {
                block.used = true;
                cout << "Allocated " << size << " bytes at " << block.ptr << endl;
                return block.ptr;
            }
        }
        cout << "Allocation failed: insufficient memory" << endl;
        return nullptr;
    }
    
    void deallocate(void* ptr) {
        for (auto& block : blocks) {
            if (block.ptr == ptr && block.used) {
                block.used = false;
                cout << "Deallocated memory at " << ptr << endl;
                return;
            }
        }
        cout << "Deallocation failed: pointer not found" << endl;
    }
};

class Particle {
private:
    float x, y, z;
    float vx, vy, vz;
    string name;
    
public:
    Particle(string n, float px, float py, float pz) 
        : name(n), x(px), y(py), z(pz), vx(0), vy(0), vz(0) {
        cout << "  Particle created: " << name << " at (" << x << ", " << y << ", " << z << ")" << endl;
    }
    
    ~Particle() {
        cout << "  Particle destroyed: " << name << endl;
    }
    
    void update(float dt) {
        x += vx * dt;
        y += vy * dt;
        z += vz * dt;
    }
    
    void setVelocity(float vxVal, float vyVal, float vzVal) {
        vx = vxVal;
        vy = vyVal;
        vz = vzVal;
    }
    
    void display() const {
        cout << "  " << name << " at (" << x << ", " << y << ", " << z << ")" << endl;
    }
};

int main() {
    cout << "=== Placement New with Custom Allocator ===" << endl;
    
    CustomAllocator allocator(sizeof(Particle) * 5);
    
    cout << "\n1. Creating particles with custom allocator:" << endl;
    vector<Particle*> particles;
    
    for (int i = 0; i < 5; i++) {
        void* mem = allocator.allocate(sizeof(Particle));
        if (mem) {
            Particle* p = new(mem) Particle("Particle" + to_string(i), i * 10.0f, i * 5.0f, 0);
            p->setVelocity(1.0f, 0.5f, 0);
            particles.push_back(p);
        }
    }
    
    cout << "\n2. Updating particles:" << endl;
    for (int i = 0; i < 3; i++) {
        cout << "Frame " << i << ":" << endl;
        for (auto p : particles) {
            p->update(0.1f);
            p->display();
        }
        cout << endl;
    }
    
    cout << "\n3. Destroying particles:" << endl;
    for (auto p : particles) {
        p->~Particle();
        allocator.deallocate(p);
    }
    
    return 0;
}
```

---

## 5. **Placement New with Exception Safety**

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
#include <memory>
using namespace std;

class Resource {
private:
    int id;
    string data;
    
public:
    Resource(int i, string d) : id(i), data(d) {
        cout << "Resource " << id << " created: " << data << endl;
        if (id == 3) {
            throw runtime_error("Failed to create resource 3");
        }
    }
    
    ~Resource() {
        cout << "Resource " << id << " destroyed" << endl;
    }
    
    void use() const {
        cout << "Using resource " << id << ": " << data << endl;
    }
};

class SafePool {
private:
    char* buffer;
    size_t size;
    size_t used;
    
public:
    SafePool(size_t s) : size(s), used(0) {
        buffer = new char[size];
        cout << "SafePool created: " << size << " bytes" << endl;
    }
    
    ~SafePool() {
        delete[] buffer;
        cout << "SafePool destroyed" << endl;
    }
    
    template<typename T, typename... Args>
    T* create(Args&&... args) {
        if (used + sizeof(T) > size) {
            throw bad_alloc();
        }
        
        void* mem = buffer + used;
        used += sizeof(T);
        
        try {
            T* obj = new(mem) T(forward<Args>(args)...);
            return obj;
        } catch (...) {
            // Rollback on exception
            used -= sizeof(T);
            throw;
        }
    }
    
    void destroy(void* ptr, size_t objSize) {
        // Assume proper alignment and location
        // In practice, would need to track objects
        used -= objSize;
    }
    
    void reset() {
        used = 0;
    }
};

int main() {
    cout << "=== Placement New with Exception Safety ===" << endl;
    
    SafePool pool(sizeof(Resource) * 5);
    
    cout << "\n1. Creating resources (some may fail):" << endl;
    Resource* resources[5] = {nullptr};
    
    for (int i = 0; i < 5; i++) {
        try {
            resources[i] = pool.create<Resource>(i, "Data" + to_string(i));
        } catch (const exception& e) {
            cout << "Failed to create resource " << i << ": " << e.what() << endl;
            // Rollback handled by pool
        }
    }
    
    cout << "\n2. Using successfully created resources:" << endl;
    for (int i = 0; i < 5; i++) {
        if (resources[i]) {
            resources[i]->use();
        }
    }
    
    cout << "\n3. Destroying resources:" << endl;
    for (int i = 0; i < 5; i++) {
        if (resources[i]) {
            resources[i]->~Resource();
            pool.destroy(resources[i], sizeof(Resource));
        }
    }
    
    cout << "\n4. Pool reset and reuse:" << endl;
    pool.reset();
    
    // Create new resources after reset
    Resource* newRes = pool.create<Resource>(10, "NewData");
    newRes->use();
    newRes->~Resource();
    pool.destroy(newRes, sizeof(Resource));
    
    return 0;
}
```

---

## 📊 Placement New Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Construct object in pre-allocated memory |
| **Syntax** | `new(pointer) ClassName(args)` |
| **Memory** | Must be properly aligned and sized |
| **Cleanup** | Manual destructor call required |
| **Use Cases** | Memory pools, custom allocators, embedded systems |

---

## ✅ Best Practices

1. **Always call destructor** explicitly for placement new objects
2. **Ensure proper alignment** for the object type
3. **Track allocated objects** for proper cleanup
4. **Use RAII wrapper** for placement new objects
5. **Handle exceptions** to avoid memory leaks
6. **Consider alignment requirements** for the target architecture

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Forgetting destructor** | Memory leak | Always call destructor |
| **Wrong alignment** | Undefined behavior | Use alignas or std::align |
| **Incorrect size** | Buffer overflow | Use sizeof(T) |
| **Double delete** | Undefined behavior | Track ownership |
| **Exception safety** | Memory leak | Use RAII wrappers |

---

## ✅ Key Takeaways

1. **Placement new** separates allocation from construction
2. **Memory must be allocated** before placement new
3. **Destructor must be called** explicitly
4. **Use for** memory pools, custom allocators
5. **Use for** embedded systems, performance-critical code
6. **Requires careful** memory management
7. **Combine with RAII** for safety

---