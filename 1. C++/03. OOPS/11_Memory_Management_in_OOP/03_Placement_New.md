# Placement New in C++ - Complete Guide

## 📖 Overview

Placement new is a special form of the `new` operator that constructs an object in pre-allocated memory. Unlike regular `new`, placement new does not allocate memory—it only constructs an object in memory that has already been allocated. This technique is essential for custom memory management, object pools, and embedded systems programming.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Placement New** | Constructs object in existing memory |
| **Separate Allocation** | Memory allocation and object construction are decoupled |
| **Manual Destructor Call** | Must call destructor explicitly |
| **Memory Reuse** | Same memory can be reused for different objects |

---

## 1. **Basic Placement New**

```cpp
#include <iostream>
#include <string>
#include <new>
using namespace std;

class Simple {
private:
    int id;
    string name;
    
public:
    Simple(int i, string n) : id(i), name(n) {
        cout << "Simple constructor: " << name << " (ID: " << id << ")" << endl;
    }
    
    ~Simple() {
        cout << "Simple destructor: " << name << endl;
    }
    
    void display() const {
        cout << "ID: " << id << ", Name: " << name << endl;
    }
};

int main() {
    cout << "=== Basic Placement New ===" << endl;
    
    // Regular new (allocation + construction)
    cout << "\n1. Regular new:" << endl;
    Simple* s1 = new Simple(1, "Regular");
    s1->display();
    delete s1;
    
    // Placement new (separate allocation and construction)
    cout << "\n2. Placement new:" << endl;
    
    // Step 1: Allocate memory
    char* buffer = new char[sizeof(Simple)];
    cout << "Memory allocated at: " << (void*)buffer << endl;
    
    // Step 2: Construct object in allocated memory
    Simple* s2 = new(buffer) Simple(2, "Placement");
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
Simple constructor: Regular (ID: 1)
ID: 1, Name: Regular
Simple destructor: Regular

2. Placement new:
Memory allocated at: 0x...
Simple constructor: Placement (ID: 2)
ID: 2, Name: Placement
Simple destructor: Placement

3. Multiple objects in one buffer:
Simple constructor: Obj0 (ID: 0)
Simple constructor: Obj1 (ID: 10)
Simple constructor: Obj2 (ID: 20)
ID: 0, Name: Obj0
ID: 10, Name: Obj1
ID: 20, Name: Obj2
Simple destructor: Obj2
Simple destructor: Obj1
Simple destructor: Obj0
```

---

## 2. **Placement New with Alignment**

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
    
    void display() const {
        cout << "  a=" << a << ", b=" << b << ", c=" << c << endl;
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
    obj1->display();
    
    // Create another object at next aligned position
    void* nextMem = reinterpret_cast<char*>(alignedMem) + sizeof(AlignedData);
    nextMem = reinterpret_cast<void*>((reinterpret_cast<uintptr_t>(nextMem) + 15) & ~15);
    AlignedData* obj2 = new(nextMem) AlignedData(20, 2.718, "Second");
    obj2->display();
    
    // Create third object
    void* nextMem2 = reinterpret_cast<char*>(nextMem) + sizeof(AlignedData);
    nextMem2 = reinterpret_cast<void*>((reinterpret_cast<uintptr_t>(nextMem2) + 15) & ~15);
    AlignedData* obj3 = new(nextMem2) AlignedData(30, 1.414, "Third");
    obj3->display();
    
    cout << "\n3. Object addresses:" << endl;
    cout << "obj1: " << obj1 << endl;
    cout << "obj2: " << obj2 << endl;
    cout << "obj3: " << obj3 << endl;
    cout << "Difference (obj1-obj2): " << (reinterpret_cast<char*>(obj2) - reinterpret_cast<char*>(obj1)) << " bytes" << endl;
    
    // Cleanup
    obj3->~AlignedData();
    obj2->~AlignedData();
    obj1->~AlignedData();
    
    return 0;
}
```

---

## 3. **Object Pool with Placement New**

```cpp
#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <new>
using namespace std;

class GameObject {
private:
    float x, y;
    string name;
    bool active;
    
public:
    GameObject() : x(0), y(0), name("Unnamed"), active(false) {
        cout << "  GameObject default constructed" << endl;
    }
    
    GameObject(string n, float xPos, float yPos) : name(n), x(xPos), y(yPos), active(true) {
        cout << "  GameObject created: " << name << " at (" << x << ", " << y << ")" << endl;
    }
    
    ~GameObject() {
        if (active) {
            cout << "  GameObject destroyed: " << name << endl;
        }
    }
    
    void update(float dt) {
        if (active) {
            x += dt;
            y += dt;
        }
    }
    
    void display() const {
        if (active) {
            cout << "  " << name << " at (" << x << ", " << y << ")" << endl;
        }
    }
    
    void activate(string n, float xPos, float yPos) {
        name = n;
        x = xPos;
        y = yPos;
        active = true;
    }
    
    void deactivate() {
        active = false;
    }
    
    bool isActive() const { return active; }
};

class ObjectPool {
private:
    char* memory;
    size_t objectSize;
    size_t capacity;
    size_t used;
    stack<GameObject*> available;
    vector<GameObject*> allObjects;
    
public:
    ObjectPool(size_t count, size_t objSize) : objectSize(objSize), capacity(count), used(0) {
        memory = new char[count * objSize];
        cout << "ObjectPool created: " << count << " objects, " << (count * objSize) << " bytes" << endl;
        
        // Pre-construct all objects (optional)
        for (size_t i = 0; i < count; i++) {
            void* mem = memory + i * objSize;
            GameObject* obj = new(mem) GameObject();
            allObjects.push_back(obj);
            available.push(obj);
        }
    }
    
    ~ObjectPool() {
        // Destroy all objects
        for (auto obj : allObjects) {
            obj->~GameObject();
        }
        delete[] memory;
        cout << "ObjectPool destroyed" << endl;
    }
    
    GameObject* acquire(const string& name, float x, float y) {
        if (available.empty()) {
            cout << "No objects available!" << endl;
            return nullptr;
        }
        
        GameObject* obj = available.top();
        available.pop();
        obj->activate(name, x, y);
        used++;
        return obj;
    }
    
    void release(GameObject* obj) {
        if (obj) {
            obj->deactivate();
            available.push(obj);
            used--;
        }
    }
    
    size_t availableCount() const { return available.size(); }
    size_t usedCount() const { return used; }
};

int main() {
    cout << "=== Object Pool with Placement New ===" << endl;
    
    ObjectPool pool(5, sizeof(GameObject));
    
    cout << "\n1. Acquiring objects:" << endl;
    vector<GameObject*> active;
    for (int i = 0; i < 5; i++) {
        GameObject* obj = pool.acquire("Enemy" + to_string(i), i * 10.0f, i * 5.0f);
        if (obj) active.push_back(obj);
    }
    
    cout << "\n2. Trying to acquire beyond pool size:" << endl;
    GameObject* extra = pool.acquire("Extra", 100, 100);
    if (!extra) cout << "  No object available" << endl;
    
    cout << "\n3. Updating objects:" << endl;
    for (int frame = 0; frame < 3; frame++) {
        cout << "  Frame " << frame << ":" << endl;
        for (auto obj : active) {
            obj->update(0.1f);
            obj->display();
        }
    }
    
    cout << "\n4. Releasing objects:" << endl;
    for (auto obj : active) {
        pool.release(obj);
    }
    
    cout << "\n5. Pool statistics:" << endl;
    cout << "  Available: " << pool.availableCount() << endl;
    cout << "  Used: " << pool.usedCount() << endl;
    
    cout << "\n6. Reusing objects:" << endl;
    GameObject* reused = pool.acquire("Reused", 999, 999);
    if (reused) {
        reused->display();
        pool.release(reused);
    }
    
    return 0;
}
```

---

## 4. **Placement New with Custom Allocator**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <new>
using namespace std;

class CustomAllocator {
private:
    struct Block {
        void* start;
        size_t size;
        bool used;
    };
    
    vector<Block> blocks;
    char* memory;
    size_t totalSize;
    
public:
    CustomAllocator(size_t size) : totalSize(size) {
        memory = new char[size];
        blocks.push_back({memory, size, false});
        cout << "CustomAllocator created with " << size << " bytes" << endl;
    }
    
    ~CustomAllocator() {
        delete[] memory;
        cout << "CustomAllocator destroyed" << endl;
    }
    
    void* allocate(size_t size, size_t alignment = alignof(max_align_t)) {
        for (auto& block : blocks) {
            if (!block.used && block.size >= size) {
                // Check alignment
                uintptr_t addr = reinterpret_cast<uintptr_t>(block.start);
                uintptr_t aligned = (addr + alignment - 1) & ~(alignment - 1);
                size_t offset = aligned - addr;
                
                if (offset + size <= block.size) {
                    block.used = true;
                    cout << "Allocated " << size << " bytes at " << (void*)aligned << endl;
                    return reinterpret_cast<void*>(aligned);
                }
            }
        }
        cout << "Allocation failed: insufficient memory" << endl;
        return nullptr;
    }
    
    void deallocate(void* ptr) {
        for (auto& block : blocks) {
            if (block.start <= ptr && ptr < static_cast<char*>(block.start) + block.size) {
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
    
    cout << "\n2. Trying to allocate beyond capacity:" << endl;
    void* extraMem = allocator.allocate(sizeof(Particle));
    if (!extraMem) cout << "  Allocation failed - out of memory" << endl;
    
    cout << "\n3. Updating particles:" << endl;
    for (int frame = 0; frame < 3; frame++) {
        cout << "  Frame " << frame << ":" << endl;
        for (auto p : particles) {
            p->update(0.1f);
            p->display();
        }
    }
    
    cout << "\n4. Destroying particles:" << endl;
    for (auto p : particles) {
        p->~Particle();
        allocator.deallocate(p);
    }
    
    cout << "\n5. Reusing memory:" << endl;
    void* reusedMem = allocator.allocate(sizeof(Particle));
    if (reusedMem) {
        Particle* p = new(reusedMem) Particle("Reused", 999, 999, 999);
        p->display();
        p->~Particle();
        allocator.deallocate(reusedMem);
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
#include <new>
using namespace std;

class Database {
private:
    string connection;
    bool connected;
    
public:
    Database(const string& conn) : connection(conn), connected(false) {
        cout << "  Database constructor: " << connection << endl;
        if (connection.empty()) {
            throw runtime_error("Invalid connection string");
        }
        connected = true;
    }
    
    ~Database() {
        if (connected) {
            cout << "  Database destructor: " << connection << endl;
        }
    }
    
    void query(const string& sql) {
        if (connected) {
            cout << "  Executing: " << sql << endl;
        }
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
        // Assume proper location
        used -= objSize;
    }
    
    void reset() {
        used = 0;
    }
};

int main() {
    cout << "=== Placement New with Exception Safety ===" << endl;
    
    SafePool pool(sizeof(Database) * 5);
    
    cout << "\n1. Creating databases (some may fail):" << endl;
    Database* dbs[5] = {nullptr};
    
    for (int i = 0; i < 5; i++) {
        try {
            string conn = (i == 2) ? "" : "db" + to_string(i);
            dbs[i] = pool.create<Database>(conn);
        } catch (const exception& e) {
            cout << "  Failed to create database " << i << ": " << e.what() << endl;
            // Rollback handled by pool
        }
    }
    
    cout << "\n2. Using successfully created databases:" << endl;
    for (int i = 0; i < 5; i++) {
        if (dbs[i]) {
            dbs[i]->query("SELECT * FROM users");
        }
    }
    
    cout << "\n3. Destroying databases:" << endl;
    for (int i = 0; i < 5; i++) {
        if (dbs[i]) {
            dbs[i]->~Database();
            pool.destroy(dbs[i], sizeof(Database));
        }
    }
    
    cout << "\n4. Pool reset and reuse:" << endl;
    pool.reset();
    
    // Create new databases after reset
    Database* newDb = pool.create<Database>("new_connection");
    newDb->query("SELECT * FROM products");
    newDb->~Database();
    pool.destroy(newDb, sizeof(Database));
    
    return 0;
}
```

---

## 📊 Placement New Summary

| Aspect | Regular new | Placement new |
|--------|-------------|---------------|
| **Memory Allocation** | Yes | No (uses existing memory) |
| **Construction** | Yes | Yes |
| **Destruction** | Automatic (delete) | Manual (~destructor) |
| **Memory Deallocation** | Automatic (delete) | Manual (free memory) |
| **Use Case** | General allocation | Custom memory management |

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
| **Forgetting destructor** | Resource leak | Always call destructor |
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