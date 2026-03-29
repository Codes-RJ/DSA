# 14_Modern_Cpp_OOP_Features/04_Smart_Pointers.md

# Smart Pointers in C++ - Complete Guide

## 📖 Overview

Smart pointers are class templates that manage dynamically allocated objects, ensuring automatic memory deallocation. They implement the RAII (Resource Acquisition Is Initialization) idiom and eliminate most memory management bugs. C++11 introduced `std::unique_ptr`, `std::shared_ptr`, and `std::weak_ptr`, which should be used instead of raw pointers for ownership.

---

## 🎯 Key Concepts

| Smart Pointer | Ownership | Overhead | Use Case |
|---------------|-----------|----------|----------|
| **unique_ptr** | Exclusive | Minimal | Single ownership |
| **shared_ptr** | Shared | Moderate | Multiple owners |
| **weak_ptr** | Non-owning | Low | Observer, break cycles |

---

## 1. **unique_ptr - Exclusive Ownership**

```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <string>
using namespace std;

class Resource {
private:
    string name_;
    static int count_;
    
public:
    Resource(string name) : name_(name) {
        count_++;
        cout << "Resource '" << name_ << "' created (total: " << count_ << ")" << endl;
    }
    
    ~Resource() {
        count_--;
        cout << "Resource '" << name_ << "' destroyed (remaining: " << count_ << ")" << endl;
    }
    
    void use() const {
        cout << "Using resource: " << name_ << endl;
    }
    
    string getName() const { return name_; }
};

int Resource::count_ = 0;

int main() {
    cout << "=== unique_ptr - Exclusive Ownership ===" << endl;
    
    // Basic unique_ptr
    cout << "\n1. Basic usage:" << endl;
    unique_ptr<Resource> u1 = make_unique<Resource>("Unique1");
    unique_ptr<Resource> u2(new Resource("Unique2"));
    
    u1->use();
    (*u2).use();
    
    // Cannot copy, only move
    // unique_ptr<Resource> u3 = u1;  // Error!
    unique_ptr<Resource> u3 = move(u1);  // OK - transfer ownership
    
    if (!u1) cout << "u1 is now empty" << endl;
    u3->use();
    
    // Release ownership
    Resource* raw = u3.release();
    cout << "Released: " << raw->getName() << endl;
    delete raw;  // Must manually delete
    
    // Reset
    u2.reset();  // Deletes managed object
    if (!u2) cout << "u2 is now empty" << endl;
    
    // Vector of unique_ptr
    cout << "\n2. Vector of unique_ptr:" << endl;
    vector<unique_ptr<Resource>> resources;
    resources.push_back(make_unique<Resource>("Vector1"));
    resources.push_back(make_unique<Resource>("Vector2"));
    resources.push_back(make_unique<Resource>("Vector3"));
    
    for (const auto& res : resources) {
        res->use();
    }
    // Automatically destroyed when vector goes out of scope
    
    // Custom deleter
    cout << "\n3. Custom deleter:" << endl;
    auto deleter = [](Resource* r) {
        cout << "Custom deleting: " << r->getName() << endl;
        delete r;
    };
    
    unique_ptr<Resource, decltype(deleter)> u4(new Resource("Custom"), deleter);
    u4->use();
    
    return 0;
}
```

**Output:**
```
=== unique_ptr - Exclusive Ownership ===

1. Basic usage:
Resource 'Unique1' created (total: 1)
Resource 'Unique2' created (total: 2)
Using resource: Unique1
Using resource: Unique2
u1 is now empty
Using resource: Unique1
Released: Unique1
Resource 'Unique1' destroyed (remaining: 1)
u2 is now empty

2. Vector of unique_ptr:
Resource 'Vector1' created (total: 2)
Resource 'Vector2' created (total: 3)
Resource 'Vector3' created (total: 4)
Using resource: Vector1
Using resource: Vector2
Using resource: Vector3

3. Custom deleter:
Resource 'Custom' created (total: 5)
Using resource: Custom
Custom deleting: Custom
Resource 'Custom' destroyed (remaining: 4)
Resource 'Vector3' destroyed (remaining: 3)
Resource 'Vector2' destroyed (remaining: 2)
Resource 'Vector1' destroyed (remaining: 1)
Resource 'Unique2' destroyed (remaining: 0)
```

---

## 2. **shared_ptr - Shared Ownership**

```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <thread>
using namespace std;

class SharedResource {
private:
    string name_;
    
public:
    SharedResource(string name) : name_(name) {
        cout << "SharedResource '" << name_ << "' created" << endl;
    }
    
    ~SharedResource() {
        cout << "SharedResource '" << name_ << "' destroyed" << endl;
    }
    
    void use() const {
        cout << "Using resource: " << name_ << endl;
    }
    
    string getName() const { return name_; }
};

void threadFunction(shared_ptr<SharedResource> res) {
    cout << "Thread " << this_thread::get_id() << " using: " 
         << res->getName() << " (count: " << res.use_count() << ")" << endl;
    this_thread::sleep_for(chrono::milliseconds(100));
}

int main() {
    cout << "=== shared_ptr - Shared Ownership ===" << endl;
    
    // Basic shared_ptr
    cout << "\n1. Basic usage:" << endl;
    shared_ptr<SharedResource> s1 = make_shared<SharedResource>("Shared1");
    {
        shared_ptr<SharedResource> s2 = s1;  // Copy - reference count increases
        shared_ptr<SharedResource> s3 = s2;  // Another copy
        cout << "Reference count: " << s1.use_count() << endl;
        s2->use();
    }  // s2 and s3 destroyed, count decreases
    cout << "Reference count: " << s1.use_count() << endl;
    
    // make_shared is more efficient
    cout << "\n2. make_shared vs new:" << endl;
    auto s4 = make_shared<SharedResource>("MakeShared");
    shared_ptr<SharedResource> s5(new SharedResource("NewShared"));
    
    // Vector of shared_ptr
    cout << "\n3. Vector of shared_ptr:" << endl;
    vector<shared_ptr<SharedResource>> resources;
    resources.push_back(make_shared<SharedResource>("Vec1"));
    resources.push_back(make_shared<SharedResource>("Vec2"));
    resources.push_back(s1);  // Share existing
    
    for (const auto& res : resources) {
        cout << res->getName() << " (count: " << res.use_count() << ")" << endl;
    }
    
    // Thread safety
    cout << "\n4. Thread safety:" << endl;
    auto shared = make_shared<SharedResource>("ThreadSafe");
    vector<thread> threads;
    
    for (int i = 0; i < 3; i++) {
        threads.emplace_back(threadFunction, shared);
    }
    
    for (auto& t : threads) {
        t.join();
    }
    cout << "Final reference count: " << shared.use_count() << endl;
    
    // Custom deleter
    cout << "\n5. Custom deleter:" << endl;
    auto deleter = [](SharedResource* r) {
        cout << "Custom deleting: " << r->getName() << endl;
        delete r;
    };
    shared_ptr<SharedResource> s6(new SharedResource("CustomDel"), deleter);
    
    return 0;
}
```

---

## 3. **weak_ptr - Non-owning Observer**

```cpp
#include <iostream>
#include <memory>
#include <vector>
using namespace std;

class Observer {
private:
    string name_;
    weak_ptr<Observer> friend_;
    
public:
    Observer(string name) : name_(name) {
        cout << "Observer " << name_ << " created" << endl;
    }
    
    ~Observer() {
        cout << "Observer " << name_ << " destroyed" << endl;
    }
    
    void setFriend(shared_ptr<Observer> f) {
        friend_ = f;
    }
    
    void notify() {
        cout << name_ << " notifying: ";
        if (auto f = friend_.lock()) {
            cout << "Friend " << f->name_ << " is alive" << endl;
        } else {
            cout << "Friend is dead" << endl;
        }
    }
    
    string getName() const { return name_; }
};

class Cache {
private:
    struct Entry {
        string data;
        weak_ptr<void> owner;
    };
    vector<Entry> cache_;
    
public:
    void add(const string& data, shared_ptr<void> owner) {
        cache_.push_back({data, owner});
        cout << "Cached: " << data << endl;
    }
    
    void cleanup() {
        auto it = cache_.begin();
        while (it != cache_.end()) {
            if (it->owner.expired()) {
                cout << "Removing expired: " << it->data << endl;
                it = cache_.erase(it);
            } else {
                ++it;
            }
        }
    }
    
    void display() const {
        cout << "Cache contents:" << endl;
        for (const auto& entry : cache_) {
            cout << "  " << entry.data << " (owner " 
                 << (entry.owner.expired() ? "dead" : "alive") << ")" << endl;
        }
    }
};

int main() {
    cout << "=== weak_ptr - Non-owning Observer ===" << endl;
    
    // Basic weak_ptr
    cout << "\n1. Basic usage:" << endl;
    shared_ptr<Observer> s1 = make_shared<Observer>("Alice");
    weak_ptr<Observer> w = s1;
    
    cout << "Reference count: " << s1.use_count() << endl;
    
    if (auto locked = w.lock()) {
        cout << "Locked: " << locked->getName() << endl;
    }
    
    s1.reset();  // Destroy the object
    
    if (auto locked = w.lock()) {
        cout << "Still alive" << endl;
    } else {
        cout << "Weak pointer expired" << endl;
    }
    
    // Observer pattern with weak_ptr
    cout << "\n2. Observer pattern:" << endl;
    auto alice = make_shared<Observer>("Alice");
    auto bob = make_shared<Observer>("Bob");
    
    alice->setFriend(bob);
    bob->setFriend(alice);
    
    alice->notify();
    bob->notify();
    
    bob.reset();  // Destroy Bob
    alice->notify();  // Alice's friend is dead
    
    // Cache with weak_ptr
    cout << "\n3. Cache with weak_ptr:" << endl;
    Cache cache;
    
    {
        auto owner = make_shared<int>(42);
        cache.add("Data1", owner);
        cache.add("Data2", owner);
        cache.add("Data3", owner);
        cache.display();
    }  // owner destroyed
    
    cache.cleanup();
    cache.display();
    
    return 0;
}
```

---

## 4. **Smart Pointer Conversions**

```cpp
#include <iostream>
#include <memory>
#include <string>
using namespace std;

class Base {
public:
    virtual void speak() { cout << "Base speaking" << endl; }
    virtual ~Base() = default;
};

class Derived : public Base {
public:
    void speak() override { cout << "Derived speaking" << endl; }
    void derivedOnly() { cout << "Derived only method" << endl; }
};

int main() {
    cout << "=== Smart Pointer Conversions ===" << endl;
    
    // unique_ptr conversions
    cout << "\n1. unique_ptr conversions:" << endl;
    unique_ptr<Derived> derived = make_unique<Derived>();
    derived->speak();
    
    // Upcast (Derived to Base)
    unique_ptr<Base> base = move(derived);  // Transfer ownership
    base->speak();
    // derived is now empty
    
    // Downcast (Base to Derived) - not directly supported
    // unique_ptr<Derived> derived2 = move(base);  // Error!
    
    // shared_ptr conversions
    cout << "\n2. shared_ptr conversions:" << endl;
    shared_ptr<Derived> s_derived = make_shared<Derived>();
    s_derived->speak();
    
    // Upcast (Derived to Base)
    shared_ptr<Base> s_base = s_derived;  // Shares ownership
    s_base->speak();
    cout << "Reference count: " << s_derived.use_count() << endl;
    
    // Downcast (Base to Derived) - use static_pointer_cast
    shared_ptr<Derived> s_derived2 = static_pointer_cast<Derived>(s_base);
    s_derived2->derivedOnly();
    
    // dynamic_pointer_cast for polymorphic types
    shared_ptr<Base> s_base2 = make_shared<Derived>();
    if (auto s_derived3 = dynamic_pointer_cast<Derived>(s_base2)) {
        cout << "Dynamic cast successful" << endl;
        s_derived3->derivedOnly();
    }
    
    // const_pointer_cast
    shared_ptr<const Base> const_base = make_shared<Derived>();
    // const_base->speak();  // Error! const
    auto mutable_base = const_pointer_cast<Base>(const_base);
    mutable_base->speak();
    
    return 0;
}
```

---

## 5. **Practical Example: Object Pool with Smart Pointers**

```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <queue>
#include <mutex>
#include <thread>
using namespace std;

class PooledObject {
private:
    int id_;
    static int nextId_;
    
public:
    PooledObject() : id_(nextId_++) {
        cout << "PooledObject " << id_ << " created" << endl;
    }
    
    ~PooledObject() {
        cout << "PooledObject " << id_ << " destroyed" << endl;
    }
    
    void use() {
        cout << "Using PooledObject " << id_ << endl;
    }
    
    int getId() const { return id_; }
};

int PooledObject::nextId_ = 1;

class ObjectPool {
private:
    queue<unique_ptr<PooledObject>> pool_;
    mutex mtx_;
    
public:
    ObjectPool(int size) {
        for (int i = 0; i < size; i++) {
            pool_.push(make_unique<PooledObject>());
        }
        cout << "ObjectPool created with " << size << " objects" << endl;
    }
    
    unique_ptr<PooledObject, function<void(PooledObject*)>> acquire() {
        lock_guard<mutex> lock(mtx_);
        
        if (pool_.empty()) {
            cout << "No objects available!" << endl;
            return {nullptr, [](PooledObject*) {}};
        }
        
        unique_ptr<PooledObject> obj = move(pool_.front());
        pool_.pop();
        
        // Return with custom deleter that returns to pool
        return {obj.release(), [this](PooledObject* ptr) {
            lock_guard<mutex> lock(mtx_);
            pool_.push(unique_ptr<PooledObject>(ptr));
            cout << "Object returned to pool" << endl;
        }};
    }
    
    size_t available() const {
        lock_guard<mutex> lock(mtx_);
        return pool_.size();
    }
};

void worker(ObjectPool& pool, int id) {
    auto obj = pool.acquire();
    if (obj) {
        cout << "Worker " << id << " acquired object" << endl;
        obj->use();
        this_thread::sleep_for(chrono::milliseconds(100));
        // Object automatically returned to pool when obj goes out of scope
    }
}

int main() {
    cout << "=== Object Pool with Smart Pointers ===" << endl;
    
    ObjectPool pool(3);
    
    cout << "\n1. Acquiring objects:" << endl;
    auto obj1 = pool.acquire();
    auto obj2 = pool.acquire();
    auto obj3 = pool.acquire();
    auto obj4 = pool.acquire();  // Should fail
    
    if (obj1) obj1->use();
    if (obj2) obj2->use();
    if (obj3) obj3->use();
    
    cout << "\n2. Returning objects:" << endl;
    obj1.reset();  // Returns to pool
    obj2.reset();
    
    cout << "\n3. Acquiring again:" << endl;
    auto obj5 = pool.acquire();
    if (obj5) obj5->use();
    
    cout << "\n4. Multi-threaded usage:" << endl;
    vector<thread> threads;
    for (int i = 0; i < 5; i++) {
        threads.emplace_back(worker, ref(pool), i);
    }
    
    for (auto& t : threads) {
        t.join();
    }
    
    return 0;
}
```

---

## 📊 Smart Pointers Summary

| Pointer | Copyable | Moveable | Reference Count | Use Case |
|---------|----------|----------|-----------------|----------|
| **unique_ptr** | No | Yes | No | Exclusive ownership |
| **shared_ptr** | Yes | Yes | Yes | Shared ownership |
| **weak_ptr** | Yes | Yes | No | Non-owning observer |

---

## ✅ Best Practices

1. **Use unique_ptr** for exclusive ownership
2. **Use shared_ptr** when sharing is needed
3. **Use weak_ptr** to break cycles and observe
4. **Prefer make_unique/make_shared** for exception safety
5. **Avoid raw pointers** for ownership
6. **Use custom deleters** when needed
7. **Never use delete** on smart pointer managed objects

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
7. **Custom deleters** provide flexibility

---