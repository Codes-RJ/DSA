# Smart Pointers Introduction - Complete Guide

## 📖 Overview

Smart pointers are C++ classes that act like pointers but provide automatic memory management. They implement the RAII (Resource Acquisition Is Initialization) idiom for dynamically allocated objects, ensuring that memory is automatically freed when it is no longer needed. Smart pointers are a cornerstone of modern C++ and eliminate most memory management bugs.

---

## 🎯 Key Concepts

| Smart Pointer | Ownership | Overhead | Use Case |
|---------------|-----------|----------|----------|
| **unique_ptr** | Exclusive | Minimal | Single ownership, no sharing |
| **shared_ptr** | Shared | Moderate | Multiple owners, shared lifetime |
| **weak_ptr** | Non-owning | Low | Observer, break cycles |

---

## 1. **The Problem with Raw Pointers**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

class Widget {
private:
    string name;
    int* data;
    
public:
    Widget(string n) : name(n) {
        data = new int(42);
        cout << "Widget created: " << name << endl;
    }
    
    ~Widget() {
        delete data;
        cout << "Widget destroyed: " << name << endl;
    }
    
    void process() {
        cout << "Processing " << name << ": " << *data << endl;
    }
};

// Problem 1: Memory leak
void memoryLeak() {
    Widget* w = new Widget("Leaky");
    w->process();
    // Missing delete! Memory leak!
}

// Problem 2: Double delete
void doubleDelete() {
    Widget* w1 = new Widget("Double");
    Widget* w2 = w1;  // Shallow copy!
    delete w1;
    delete w2;  // Double delete! Undefined behavior!
}

// Problem 3: Dangling pointer
void danglingPointer() {
    Widget* w = new Widget("Dangling");
    delete w;
    w->process();  // Using deleted object! Undefined behavior!
}

// Solution: Smart pointers
void smartPointerSolution() {
    unique_ptr<Widget> w = make_unique<Widget>("Smart");
    w->process();
    // Automatically deleted when w goes out of scope
}

int main() {
    cout << "=== Problems with Raw Pointers ===" << endl;
    
    cout << "\n1. Memory leak (commented out):" << endl;
    // memoryLeak();  // Uncomment to see memory leak
    
    cout << "\n2. Double delete (commented out):" << endl;
    // doubleDelete();  // Uncomment to see undefined behavior
    
    cout << "\n3. Dangling pointer (commented out):" << endl;
    // danglingPointer();  // Uncomment to see undefined behavior
    
    cout << "\n4. Smart pointer solution:" << endl;
    smartPointerSolution();
    
    cout << "\nSmart pointers prevent these issues!" << endl;
    
    return 0;
}
```

---

## 2. **unique_ptr - Exclusive Ownership**

```cpp
#include <iostream>
#include <memory>
#include <vector>
using namespace std;

class Resource {
private:
    int id;
    static int nextId;
    
public:
    Resource() : id(nextId++) {
        cout << "Resource " << id << " created" << endl;
    }
    
    ~Resource() {
        cout << "Resource " << id << " destroyed" << endl;
    }
    
    void use() {
        cout << "Using resource " << id << endl;
    }
    
    int getId() const { return id; }
};

int Resource::nextId = 1;

int main() {
    cout << "=== unique_ptr - Exclusive Ownership ===" << endl;
    
    cout << "\n1. Basic unique_ptr usage:" << endl;
    {
        unique_ptr<Resource> u1 = make_unique<Resource>();
        u1->use();
        cout << "Resource ID: " << u1->getId() << endl;
    }  // Resource automatically destroyed
    
    cout << "\n2. Transferring ownership (move):" << endl;
    {
        unique_ptr<Resource> u1 = make_unique<Resource>();
        unique_ptr<Resource> u2 = move(u1);  // Ownership transferred
        
        if (!u1) cout << "u1 is now empty" << endl;
        u2->use();
        // u1->use();  // Error! u1 no longer owns anything
    }
    
    cout << "\n3. Cannot copy unique_ptr:" << endl;
    {
        unique_ptr<Resource> u1 = make_unique<Resource>();
        // unique_ptr<Resource> u2 = u1;  // Error! Cannot copy
        unique_ptr<Resource> u2 = move(u1);  // OK - move only
    }
    
    cout << "\n4. Vector of unique_ptr:" << endl;
    {
        vector<unique_ptr<Resource>> resources;
        resources.push_back(make_unique<Resource>());
        resources.push_back(make_unique<Resource>());
        resources.push_back(make_unique<Resource>());
        
        for (const auto& r : resources) {
            r->use();
        }
        // All automatically destroyed
    }
    
    cout << "\n5. Returning unique_ptr from function:" << endl;
    {
        auto createResource = []() -> unique_ptr<Resource> {
            return make_unique<Resource>();
        };
        
        unique_ptr<Resource> u = createResource();
        u->use();
    }
    
    return 0;
}
```

---

## 3. **shared_ptr - Shared Ownership**

```cpp
#include <iostream>
#include <memory>
#include <vector>
using namespace std;

class Data {
private:
    string name;
    
public:
    Data(string n) : name(n) {
        cout << "Data created: " << name << endl;
    }
    
    ~Data() {
        cout << "Data destroyed: " << name << endl;
    }
    
    void process() {
        cout << "Processing data: " << name << endl;
    }
};

int main() {
    cout << "=== shared_ptr - Shared Ownership ===" << endl;
    
    cout << "\n1. Basic shared_ptr usage:" << endl;
    {
        shared_ptr<Data> s1 = make_shared<Data>("Shared1");
        cout << "Reference count: " << s1.use_count() << endl;
        
        shared_ptr<Data> s2 = s1;  // Copy - reference count increases
        cout << "Reference count: " << s1.use_count() << endl;
        
        shared_ptr<Data> s3 = s2;
        cout << "Reference count: " << s1.use_count() << endl;
        
        s2.reset();  // Decrease reference count
        cout << "Reference count: " << s1.use_count() << endl;
    }  // Last reference destroyed, Data destroyed
    
    cout << "\n2. Shared ownership in container:" << endl;
    {
        vector<shared_ptr<Data>> vec;
        auto s1 = make_shared<Data>("Container");
        vec.push_back(s1);
        vec.push_back(s1);
        vec.push_back(s1);
        
        cout << "Reference count: " << s1.use_count() << endl;
        vec.clear();
        cout << "After vector clear, reference count: " << s1.use_count() << endl;
    }
    
    cout << "\n3. shared_ptr with custom deleter:" << endl;
    {
        auto deleter = [](Data* d) {
            cout << "Custom deleting: " << d->getName() << endl;
            delete d;
        };
        
        shared_ptr<Data> s(new Data("Custom"), deleter);
        s->process();
    }
    
    cout << "\n4. Aliasing constructor:" << endl;
    {
        struct Pair {
            int first;
            int second;
        };
        
        auto sp = make_shared<Pair>();
        sp->first = 10;
        sp->second = 20;
        
        shared_ptr<int> sp_first(sp, &sp->first);
        shared_ptr<int> sp_second(sp, &sp->second);
        
        cout << "First: " << *sp_first << ", Second: " << *sp_second << endl;
        cout << "Reference count: " << sp.use_count() << endl;
    }
    
    return 0;
}
```

---

## 4. **weak_ptr - Non-owning Observer**

```cpp
#include <iostream>
#include <memory>
#include <vector>
using namespace std;

class Node {
private:
    string name;
    
public:
    Node(string n) : name(n) {
        cout << "Node created: " << name << endl;
    }
    
    ~Node() {
        cout << "Node destroyed: " << name << endl;
    }
    
    void display() const {
        cout << "Node: " << name << endl;
    }
    
    string getName() const { return name; }
};

class Observer {
private:
    weak_ptr<Node> node;
    
public:
    Observer(shared_ptr<Node> n) : node(n) {}
    
    void observe() {
        if (auto locked = node.lock()) {
            cout << "Observing: " << locked->getName() << endl;
        } else {
            cout << "Node no longer exists" << endl;
        }
    }
};

int main() {
    cout << "=== weak_ptr - Non-owning Observer ===" << endl;
    
    cout << "\n1. Basic weak_ptr usage:" << endl;
    {
        shared_ptr<Node> s = make_shared<Node>("Main");
        weak_ptr<Node> w = s;
        
        cout << "Reference count: " << s.use_count() << endl;
        
        if (auto locked = w.lock()) {
            locked->display();
        }
        
        s.reset();  // Destroy the object
        
        if (auto locked = w.lock()) {
            locked->display();
        } else {
            cout << "Weak pointer expired" << endl;
        }
    }
    
    cout << "\n2. Observer pattern with weak_ptr:" << endl;
    {
        auto node = make_shared<Node>("Observable");
        Observer observer(node);
        
        observer.observe();
        
        node.reset();
        observer.observe();  // Node no longer exists
    }
    
    cout << "\n3. Breaking circular references:" << endl;
    {
        struct B;
        
        struct A {
            shared_ptr<B> b;
            ~A() { cout << "A destroyed" << endl; }
        };
        
        struct B {
            weak_ptr<A> a;  // Use weak_ptr to break cycle
            ~B() { cout << "B destroyed" << endl; }
        };
        
        auto a = make_shared<A>();
        auto b = make_shared<B>();
        
        a->b = b;
        b->a = a;
        
        cout << "A use count: " << a.use_count() << endl;
        cout << "B use count: " << b.use_count() << endl;
        // Both will be destroyed properly
    }
    
    return 0;
}
```

---

## 5. **Comparing Smart Pointers**

```cpp
#include <iostream>
#include <memory>
#include <chrono>
#include <vector>
using namespace std;

class TestObject {
public:
    int data[100];
    TestObject() {
        for (int i = 0; i < 100; i++) data[i] = i;
    }
};

int main() {
    cout << "=== Comparing Smart Pointers ===" << endl;
    
    cout << "\n1. Size comparison:" << endl;
    cout << "sizeof(raw pointer): " << sizeof(TestObject*) << " bytes" << endl;
    cout << "sizeof(unique_ptr): " << sizeof(unique_ptr<TestObject>) << " bytes" << endl;
    cout << "sizeof(shared_ptr): " << sizeof(shared_ptr<TestObject>) << " bytes" << endl;
    cout << "sizeof(weak_ptr):   " << sizeof(weak_ptr<TestObject>) << " bytes" << endl;
    
    cout << "\n2. When to use each:" << endl;
    cout << "   unique_ptr:  Exclusive ownership, no sharing needed" << endl;
    cout << "   shared_ptr:  Shared ownership, multiple owners" << endl;
    cout << "   weak_ptr:    Observing, breaking cycles" << endl;
    
    cout << "\n3. Performance comparison (100,000 allocations):" << endl;
    
    // unique_ptr
    auto start = chrono::high_resolution_clock::now();
    for (int i = 0; i < 100000; i++) {
        auto u = make_unique<TestObject>();
    }
    auto end = chrono::high_resolution_clock::now();
    auto uniqueTime = chrono::duration_cast<chrono::milliseconds>(end - start).count();
    cout << "   unique_ptr: " << uniqueTime << " ms" << endl;
    
    // shared_ptr
    start = chrono::high_resolution_clock::now();
    for (int i = 0; i < 100000; i++) {
        auto s = make_shared<TestObject>();
    }
    end = chrono::high_resolution_clock::now();
    auto sharedTime = chrono::duration_cast<chrono::milliseconds>(end - start).count();
    cout << "   shared_ptr: " << sharedTime << " ms" << endl;
    
    cout << "\n4. Comparison summary:" << endl;
    cout << "   ┌─────────────┬────────────┬───────────┬─────────────┐" << endl;
    cout << "   │   Feature   │ unique_ptr │ shared_ptr│   weak_ptr  │" << endl;
    cout << "   ├─────────────┼────────────┼───────────┼─────────────┤" << endl;
    cout << "   │ Ownership   │ Exclusive  │  Shared   │ Non-owning  │" << endl;
    cout << "   │ Copyable    │     No     │    Yes    │     Yes     │" << endl;
    cout << "   │ Moveable    │    Yes     │    Yes    │     Yes     │" << endl;
    cout << "   │ Overhead    │   Minimal  │  Moderate │    Low      │" << endl;
    cout << "   │ Use Count   │    N/A     │    Yes    │    N/A      │" << endl;
    cout << "   └─────────────┴────────────┴───────────┴─────────────┘" << endl;
    
    return 0;
}
```

---

## 6. **Practical Example: Game Object Management**

```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <map>
#include <string>
using namespace std;

class GameObject {
private:
    int id;
    string name;
    static int nextId;
    
public:
    GameObject(string n) : id(nextId++), name(n) {
        cout << "  GameObject created: " << name << " (ID: " << id << ")" << endl;
    }
    
    ~GameObject() {
        cout << "  GameObject destroyed: " << name << " (ID: " << id << ")" << endl;
    }
    
    void update() {
        cout << "  Updating " << name << endl;
    }
    
    int getId() const { return id; }
    string getName() const { return name; }
};

int GameObject::nextId = 1;

class GameWorld {
private:
    vector<unique_ptr<GameObject>> objects;  // Unique ownership
    map<int, weak_ptr<GameObject>> registry; // Non-owning observers
    
public:
    void addObject(const string& name) {
        auto obj = make_shared<GameObject>(name);
        registry[obj->getId()] = obj;
        objects.push_back(move(obj));
    }
    
    void findObject(int id) {
        auto it = registry.find(id);
        if (it != registry.end()) {
            if (auto obj = it->second.lock()) {
                cout << "Found: " << obj->getName() << endl;
            } else {
                cout << "Object no longer exists" << endl;
                registry.erase(it);
            }
        } else {
            cout << "Object not found" << endl;
        }
    }
    
    void updateAll() {
        for (auto& obj : objects) {
            obj->update();
        }
    }
};

class ResourceManager {
private:
    map<string, shared_ptr<GameObject>> resources;
    
public:
    shared_ptr<GameObject> getResource(const string& name) {
        auto it = resources.find(name);
        if (it != resources.end()) {
            cout << "Resource cache hit: " << name << endl;
            return it->second;
        }
        
        cout << "Loading resource: " << name << endl;
        auto res = make_shared<GameObject>(name);
        resources[name] = res;
        return res;
    }
};

int main() {
    cout << "=== Game Object Management with Smart Pointers ===" << endl;
    
    cout << "\n1. Game world with unique_ptr:" << endl;
    {
        GameWorld world;
        world.addObject("Player");
        world.addObject("Enemy1");
        world.addObject("Enemy2");
        world.updateAll();
    }
    
    cout << "\n2. Resource manager with shared_ptr:" << endl;
    {
        ResourceManager rm;
        
        auto res1 = rm.getResource("Texture");
        auto res2 = rm.getResource("Texture");  // Cache hit
        auto res3 = rm.getResource("Sound");
        
        cout << "Texture reference count: " << res1.use_count() << endl;
    }
    
    cout << "\n3. Weak_ptr for object registry:" << endl;
    {
        GameWorld world;
        world.addObject("Target");
        world.addObject("Observer");
        world.findObject(1);
        world.findObject(2);
        world.findObject(99);
    }
    
    return 0;
}
```

---

## 📊 Smart Pointers Summary

| Smart Pointer | Characteristics | Use Case |
|---------------|-----------------|----------|
| **unique_ptr** | Move-only, no overhead | Exclusive ownership, containers |
| **shared_ptr** | Reference counting, copyable | Shared ownership, caches |
| **weak_ptr** | Non-owning, breaks cycles | Observers, circular references |

---

## ✅ Best Practices

1. **Prefer unique_ptr** for exclusive ownership
2. **Use make_unique/make_shared** for exception safety
3. **Use shared_ptr only when sharing is needed**
4. **Use weak_ptr to break cycles** with shared_ptr
5. **Never use raw pointers** for ownership
6. **Use smart pointers in containers** instead of raw pointers

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Circular references** | Memory leak with shared_ptr | Use weak_ptr |
| **Using raw pointer from smart pointer** | Dangling pointer | Use get() carefully |
| **Not using make_shared** | Two allocations | Use make_shared |
| **Mixing smart and raw pointers** | Ownership confusion | Be consistent |

---

## ✅ Key Takeaways

1. **unique_ptr**: Exclusive ownership, cannot be copied
2. **shared_ptr**: Shared ownership, reference counting
3. **weak_ptr**: Non-owning observer, breaks cycles
4. **Prefer smart pointers** over raw pointers for ownership
5. **Use make_unique/make_shared** for exception safety
6. **Smart pointers are RAII** - resources automatically managed

---