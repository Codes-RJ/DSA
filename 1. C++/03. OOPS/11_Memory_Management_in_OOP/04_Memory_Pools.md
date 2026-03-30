# Memory Pools in C++ - Complete Guide

## 📖 Overview

Memory pools are custom memory allocators that pre-allocate a large block of memory and manage allocations from that block. They are used to improve performance, reduce fragmentation, and provide deterministic allocation times. Memory pools are essential in game development, embedded systems, and real-time applications.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Memory Pool** | Pre-allocated memory block for custom allocation |
| **Fixed-size Allocator** | Allocates blocks of a fixed size |
| **Variable-size Allocator** | Allocates blocks of varying sizes |
| **Object Pool** | Pool specialized for objects of a specific type |
| **Arena Allocator** | Simple allocator that only allocates (no deallocation) |

---

## 1. **Fixed-Size Memory Pool**

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <cstdint>
using namespace std;

class FixedSizePool {
private:
    char* memory;
    size_t blockSize;
    size_t blockCount;
    stack<void*> freeList;
    
public:
    FixedSizePool(size_t blockSize, size_t blockCount) 
        : blockSize(blockSize), blockCount(blockCount) {
        
        // Allocate memory
        memory = new char[blockSize * blockCount];
        
        // Initialize free list
        for (size_t i = 0; i < blockCount; i++) {
            freeList.push(memory + i * blockSize);
        }
        
        cout << "FixedSizePool created: " << blockCount << " blocks of " 
             << blockSize << " bytes each" << endl;
    }
    
    ~FixedSizePool() {
        delete[] memory;
        cout << "FixedSizePool destroyed" << endl;
    }
    
    void* allocate() {
        if (freeList.empty()) {
            cout << "Pool exhausted!" << endl;
            return nullptr;
        }
        
        void* ptr = freeList.top();
        freeList.pop();
        return ptr;
    }
    
    void deallocate(void* ptr) {
        if (ptr >= memory && ptr < memory + blockSize * blockCount) {
            freeList.push(ptr);
        }
    }
    
    size_t available() const {
        return freeList.size();
    }
    
    size_t used() const {
        return blockCount - freeList.size();
    }
};

class GameObject {
private:
    float x, y, z;
    char name[32];
    bool active;
    
public:
    GameObject() : x(0), y(0), z(0), active(false) {
        strcpy(name, "Unnamed");
        cout << "  GameObject default constructed" << endl;
    }
    
    void activate(const char* n, float xPos, float yPos, float zPos) {
        strcpy(name, n);
        x = xPos;
        y = yPos;
        z = zPos;
        active = true;
    }
    
    void deactivate() {
        active = false;
    }
    
    void update() {
        if (active) {
            x += 0.1f;
            y += 0.1f;
            z += 0.1f;
        }
    }
    
    void display() const {
        if (active) {
            cout << "  " << name << " at (" << x << ", " << y << ", " << z << ")" << endl;
        }
    }
};

int main() {
    cout << "=== Fixed-Size Memory Pool ===" << endl;
    
    FixedSizePool pool(sizeof(GameObject), 10);
    
    cout << "\n1. Allocating objects from pool:" << endl;
    vector<GameObject*> objects;
    
    for (int i = 0; i < 10; i++) {
        void* mem = pool.allocate();
        if (mem) {
            GameObject* obj = new(mem) GameObject();
            obj->activate(("Object" + to_string(i)).c_str(), i * 10.0f, i * 5.0f, 0);
            objects.push_back(obj);
        }
    }
    
    cout << "\n2. Trying to allocate beyond pool size:" << endl;
    void* extra = pool.allocate();
    if (!extra) cout << "  No more objects available" << endl;
    
    cout << "\n3. Updating objects:" << endl;
    for (int frame = 0; frame < 3; frame++) {
        cout << "  Frame " << frame << ":" << endl;
        for (auto obj : objects) {
            obj->update();
            obj->display();
        }
    }
    
    cout << "\n4. Deallocating some objects:" << endl;
    for (int i = 0; i < 5; i++) {
        objects[i]->~GameObject();
        pool.deallocate(objects[i]);
        cout << "  Deallocated object " << i << endl;
    }
    
    cout << "\n5. Pool statistics:" << endl;
    cout << "  Available: " << pool.available() << endl;
    cout << "  Used: " << pool.used() << endl;
    
    cout << "\n6. Reusing freed objects:" << endl;
    for (int i = 0; i < 5; i++) {
        void* mem = pool.allocate();
        if (mem) {
            GameObject* obj = new(mem) GameObject();
            obj->activate(("NewObject" + to_string(i)).c_str(), i * 100.0f, i * 50.0f, 0);
            objects.push_back(obj);
        }
    }
    
    cout << "\n7. Cleanup:" << endl;
    for (auto obj : objects) {
        obj->~GameObject();
        pool.deallocate(obj);
    }
    
    return 0;
}
```

---

## 2. **Object Pool (Type-Specific)**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <memory>
using namespace std;

template<typename T>
class ObjectPool {
private:
    vector<T*> pool;
    stack<T*> available;
    size_t capacity;
    
public:
    ObjectPool(size_t size) : capacity(size) {
        for (size_t i = 0; i < size; i++) {
            T* obj = new T();
            pool.push_back(obj);
            available.push(obj);
        }
        cout << "ObjectPool<" << typeid(T).name() << "> created with " 
             << size << " objects" << endl;
    }
    
    ~ObjectPool() {
        for (auto obj : pool) {
            delete obj;
        }
        cout << "ObjectPool destroyed" << endl;
    }
    
    T* acquire() {
        if (available.empty()) {
            cout << "No objects available!" << endl;
            return nullptr;
        }
        T* obj = available.top();
        available.pop();
        return obj;
    }
    
    void release(T* obj) {
        obj->reset();
        available.push(obj);
    }
    
    size_t availableCount() const {
        return available.size();
    }
    
    size_t usedCount() const {
        return capacity - available.size();
    }
};

class Particle {
private:
    float x, y, z;
    float vx, vy, vz;
    float life;
    bool active;
    
public:
    Particle() : x(0), y(0), z(0), vx(0), vy(0), vz(0), life(0), active(false) {
        // cout << "  Particle constructed" << endl;
    }
    
    void reset() {
        active = false;
        life = 0;
    }
    
    void activate(float xPos, float yPos, float zPos, 
                  float vxVal, float vyVal, float vzVal, float lifetime) {
        x = xPos;
        y = yPos;
        z = zPos;
        vx = vxVal;
        vy = vyVal;
        vz = vzVal;
        life = lifetime;
        active = true;
    }
    
    bool update(float dt) {
        if (!active) return false;
        
        x += vx * dt;
        y += vy * dt;
        z += vz * dt;
        life -= dt;
        
        if (life <= 0) {
            active = false;
            return false;
        }
        return true;
    }
    
    void display() const {
        if (active) {
            cout << "  Particle at (" << x << ", " << y << ", " << z 
                 << ") life: " << life << endl;
        }
    }
    
    bool isActive() const { return active; }
};

class ParticleSystem {
private:
    ObjectPool<Particle> pool;
    vector<Particle*> activeParticles;
    
public:
    ParticleSystem(int maxParticles) : pool(maxParticles) {}
    
    void emit(float x, float y, float z, float lifetime) {
        Particle* p = pool.acquire();
        if (p) {
            p->activate(x, y, z, (rand() % 100 - 50) / 10.0f,
                        (rand() % 100 - 50) / 10.0f,
                        (rand() % 100) / 10.0f, lifetime);
            activeParticles.push_back(p);
        }
    }
    
    void update(float dt) {
        for (auto it = activeParticles.begin(); it != activeParticles.end();) {
            if (!(*it)->update(dt)) {
                pool.release(*it);
                it = activeParticles.erase(it);
            } else {
                ++it;
            }
        }
    }
    
    void display() const {
        cout << "Active particles: " << activeParticles.size() << endl;
        for (auto p : activeParticles) {
            p->display();
        }
    }
};

int main() {
    cout << "=== Object Pool (Type-Specific) ===" << endl;
    
    ParticleSystem system(10);
    
    cout << "\n1. Emitting particles:" << endl;
    for (int i = 0; i < 15; i++) {
        system.emit(0, 0, 0, 2.0f);
        cout << "  Emitted particle " << i << endl;
    }
    
    cout << "\n2. Initial state:" << endl;
    system.display();
    
    cout << "\n3. Simulating particles:" << endl;
    for (int frame = 0; frame < 5; frame++) {
        cout << "  Frame " << frame << ":" << endl;
        system.update(0.5f);
        system.display();
    }
    
    return 0;
}
```

---

## 3. **Arena Allocator**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cstdint>
using namespace std;

class ArenaAllocator {
private:
    char* memory;
    size_t size;
    size_t used;
    
public:
    ArenaAllocator(size_t s) : size(s), used(0) {
        memory = new char[size];
        cout << "ArenaAllocator created: " << size << " bytes" << endl;
    }
    
    ~ArenaAllocator() {
        delete[] memory;
        cout << "ArenaAllocator destroyed" << endl;
    }
    
    void* allocate(size_t bytes, size_t alignment = alignof(max_align_t)) {
        // Align the current pointer
        uintptr_t current = reinterpret_cast<uintptr_t>(memory + used);
        uintptr_t aligned = (current + alignment - 1) & ~(alignment - 1);
        size_t offset = aligned - current;
        
        if (used + offset + bytes > size) {
            cout << "Arena exhausted!" << endl;
            return nullptr;
        }
        
        used += offset + bytes;
        return reinterpret_cast<void*>(aligned);
    }
    
    void reset() {
        used = 0;
        cout << "Arena reset" << endl;
    }
    
    size_t usedBytes() const { return used; }
    size_t freeBytes() const { return size - used; }
};

class FrameAllocator {
private:
    ArenaAllocator arena;
    vector<size_t> markers;
    
public:
    FrameAllocator(size_t size) : arena(size) {}
    
    void* allocate(size_t bytes, size_t alignment = alignof(max_align_t)) {
        return arena.allocate(bytes, alignment);
    }
    
    void mark() {
        markers.push_back(arena.usedBytes());
        cout << "Mark: " << markers.back() << " bytes used" << endl;
    }
    
    void resetToMark() {
        if (!markers.empty()) {
            size_t mark = markers.back();
            // Reset arena to mark (cannot free individual allocations)
            // In a real implementation, we would need to track allocations
            cout << "Reset to mark: " << mark << " bytes" << endl;
            markers.pop_back();
        }
    }
    
    void clear() {
        markers.clear();
        arena.reset();
    }
};

struct Vertex {
    float x, y, z;
    float nx, ny, nz;
    float u, v;
};

struct Mesh {
    Vertex* vertices;
    int* indices;
    int vertexCount;
    int indexCount;
};

int main() {
    cout << "=== Arena Allocator ===" << endl;
    
    ArenaAllocator arena(1024 * 1024);  // 1 MB
    
    cout << "\n1. Allocating objects:" << endl;
    
    // Allocate a string
    char* str = (char*)arena.allocate(100);
    strcpy(str, "Hello from arena");
    cout << "  String: " << str << endl;
    
    // Allocate an array
    int* arr = (int*)arena.allocate(10 * sizeof(int));
    for (int i = 0; i < 10; i++) {
        arr[i] = i * i;
    }
    cout << "  Array: ";
    for (int i = 0; i < 10; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    // Allocate a structure
    Vertex* v = (Vertex*)arena.allocate(sizeof(Vertex));
    v->x = 1.0f;
    v->y = 2.0f;
    v->z = 3.0f;
    cout << "  Vertex: (" << v->x << ", " << v->y << ", " << v->z << ")" << endl;
    
    cout << "\n2. Arena statistics:" << endl;
    cout << "  Used: " << arena.usedBytes() << " bytes" << endl;
    cout << "  Free: " << arena.freeBytes() << " bytes" << endl;
    
    cout << "\n3. Frame allocator with markers:" << endl;
    FrameAllocator frame(1024 * 1024);
    
    frame.mark();
    int* frameData1 = (int*)frame.allocate(1000 * sizeof(int));
    frame.mark();
    int* frameData2 = (int*)frame.allocate(2000 * sizeof(int));
    frame.mark();
    int* frameData3 = (int*)frame.allocate(3000 * sizeof(int));
    
    cout << "\n4. Reset to previous frame:" << endl;
    frame.resetToMark();  // Revert to after frameData2
    frame.resetToMark();  // Revert to after frameData1
    frame.resetToMark();  // Revert to start
    
    cout << "\n5. Clear arena:" << endl;
    frame.clear();
    
    return 0;
}
```

---

## 4. **Variable-Size Memory Pool**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
using namespace std;

struct Block {
    void* start;
    size_t size;
    bool free;
};

class VariableSizePool {
private:
    char* memory;
    size_t totalSize;
    list<Block> blocks;
    
public:
    VariableSizePool(size_t size) : totalSize(size) {
        memory = new char[size];
        blocks.push_back({memory, size, true});
        cout << "VariableSizePool created: " << size << " bytes" << endl;
    }
    
    ~VariableSizePool() {
        delete[] memory;
        cout << "VariableSizePool destroyed" << endl;
    }
    
    void* allocate(size_t size, size_t alignment = alignof(max_align_t)) {
        for (auto it = blocks.begin(); it != blocks.end(); ++it) {
            if (it->free && it->size >= size) {
                // Align the address
                uintptr_t addr = reinterpret_cast<uintptr_t>(it->start);
                uintptr_t aligned = (addr + alignment - 1) & ~(alignment - 1);
                size_t offset = aligned - addr;
                
                if (offset + size <= it->size) {
                    // Split block if necessary
                    if (offset > 0) {
                        blocks.insert(it, {it->start, offset, true});
                        it->start = reinterpret_cast<char*>(it->start) + offset;
                        it->size -= offset;
                    }
                    
                    if (it->size > size) {
                        blocks.insert(it, {it->start, size, false});
                        it->start = reinterpret_cast<char*>(it->start) + size;
                        it->size -= size;
                        return it->start;
                    } else {
                        it->free = false;
                        return it->start;
                    }
                }
            }
        }
        
        cout << "Allocation failed: insufficient memory" << endl;
        return nullptr;
    }
    
    void deallocate(void* ptr) {
        for (auto it = blocks.begin(); it != blocks.end(); ++it) {
            if (it->start == ptr) {
                it->free = true;
                
                // Merge with next block if free
                auto next = it;
                ++next;
                if (next != blocks.end() && next->free) {
                    it->size += next->size;
                    blocks.erase(next);
                }
                
                // Merge with previous block if free
                if (it != blocks.begin()) {
                    auto prev = it;
                    --prev;
                    if (prev->free) {
                        prev->size += it->size;
                        blocks.erase(it);
                    }
                }
                return;
            }
        }
    }
    
    void dump() const {
        cout << "Memory blocks:" << endl;
        for (const auto& block : blocks) {
            cout << "  " << (block.free ? "FREE" : "USED") 
                 << " at " << block.start << " size=" << block.size << endl;
        }
    }
};

int main() {
    cout << "=== Variable-Size Memory Pool ===" << endl;
    
    VariableSizePool pool(1024);
    
    cout << "\n1. Initial state:" << endl;
    pool.dump();
    
    cout << "\n2. Allocating blocks:" << endl;
    void* p1 = pool.allocate(100);
    void* p2 = pool.allocate(200);
    void* p3 = pool.allocate(300);
    pool.dump();
    
    cout << "\n3. Deallocating middle block:" << endl;
    pool.deallocate(p2);
    pool.dump();
    
    cout << "\n4. Allocating in freed space:" << endl;
    void* p4 = pool.allocate(150);
    pool.dump();
    
    cout << "\n5. Deallocating multiple blocks:" << endl;
    pool.deallocate(p1);
    pool.deallocate(p3);
    pool.deallocate(p4);
    pool.dump();
    
    return 0;
}
```

---

## 5. **Performance Comparison**

```cpp
#include <iostream>
#include <chrono>
#include <vector>
#include <memory>
#include <cstdlib>
using namespace std;
using namespace chrono;

class TestObject {
public:
    int data[16];
    TestObject() {
        for (int i = 0; i < 16; i++) data[i] = i;
    }
};

class SimplePool {
private:
    vector<void*> freeList;
    size_t objectSize;
    
public:
    SimplePool(size_t objSize, size_t count) : objectSize(objSize) {
        for (size_t i = 0; i < count; i++) {
            freeList.push_back(malloc(objSize));
        }
    }
    
    ~SimplePool() {
        for (auto p : freeList) {
            free(p);
        }
    }
    
    void* allocate() {
        if (freeList.empty()) return nullptr;
        void* p = freeList.back();
        freeList.pop_back();
        return p;
    }
    
    void deallocate(void* p) {
        freeList.push_back(p);
    }
};

int main() {
    cout << "=== Performance Comparison ===" << endl;
    
    const int ITERATIONS = 100000;
    const int OBJECTS = 1000;
    
    cout << "\n1. Regular new/delete:" << endl;
    auto start = high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++) {
        vector<TestObject*> objects;
        for (int j = 0; j < OBJECTS; j++) {
            objects.push_back(new TestObject());
        }
        for (auto obj : objects) {
            delete obj;
        }
    }
    auto end = high_resolution_clock::now();
    auto regularTime = duration_cast<milliseconds>(end - start).count();
    cout << "  Time: " << regularTime << " ms" << endl;
    
    cout << "\n2. Memory pool:" << endl;
    SimplePool pool(sizeof(TestObject), OBJECTS);
    
    start = high_resolution_clock::now();
    for (int i = 0; i < ITERATIONS; i++) {
        vector<TestObject*> objects;
        for (int j = 0; j < OBJECTS; j++) {
            void* mem = pool.allocate();
            TestObject* obj = new(mem) TestObject();
            objects.push_back(obj);
        }
        for (auto obj : objects) {
            obj->~TestObject();
            pool.deallocate(obj);
        }
    }
    end = high_resolution_clock::now();
    auto poolTime = duration_cast<milliseconds>(end - start).count();
    cout << "  Time: " << poolTime << " ms" << endl;
    
    cout << "\n3. Results:" << endl;
    cout << "  Regular new/delete: " << regularTime << " ms" << endl;
    cout << "  Memory pool: " << poolTime << " ms" << endl;
    cout << "  Speedup: " << (double)regularTime / poolTime << "x" << endl;
    
    cout << "\n4. Memory pool advantages:" << endl;
    cout << "  ✓ Faster allocation/deallocation" << endl;
    cout << "  ✓ Reduced fragmentation" << endl;
    cout << "  ✓ Deterministic performance" << endl;
    cout << "  ✓ Better cache locality" << endl;
    
    return 0;
}
```

---

## 📊 Memory Pool Summary

| Pool Type | Allocation | Deallocation | Fragmentation | Use Case |
|-----------|------------|--------------|---------------|----------|
| **Fixed-size** | O(1) | O(1) | None | Same-sized objects |
| **Object Pool** | O(1) | O(1) | None | Type-specific objects |
| **Arena** | O(1) | N/A (reset) | None | Frame allocations |
| **Variable-size** | O(n) | O(n) | Low | Mixed sizes |

---

## ✅ Best Practices

1. **Use fixed-size pools** for same-sized objects
2. **Use arena allocators** for frame-based allocations
3. **Choose pool size** based on peak usage
4. **Consider alignment** requirements for your objects
5. **Profile performance** before optimizing
6. **Use RAII** with pool allocations

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Pool exhaustion** | Allocation failure | Monitor usage, increase size |
| **Memory fragmentation** | Wasted memory | Use fixed-size pools |
| **Alignment issues** | Undefined behavior | Ensure proper alignment |
| **Double deallocation** | Corruption | Track ownership |
| **Cross-pool deallocation** | Corruption | Track which pool owns pointer |

---

## ✅ Key Takeaways

1. **Memory pools** pre-allocate memory for faster allocation
2. **Fixed-size pools** are simplest and fastest
3. **Object pools** manage objects of specific types
4. **Arena allocators** are great for temporary allocations
5. **Reduced fragmentation** compared to general allocators
6. **Deterministic performance** critical for real-time systems
7. **Customizable** for specific use cases

---