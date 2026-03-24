# Smart Pointers - Modern Memory Management

Smart pointers are a key feature of modern C++ that provide automatic memory management and help prevent memory leaks and dangling pointers.

## 📖 Overview

Smart pointers are objects that act like pointers but provide automatic memory management through RAII (Resource Acquisition Is Initialization). They automatically delete the object they point to when the smart pointer goes out of scope.

## 🎯 Types of Smart Pointers

### 1. unique_ptr - Exclusive Ownership
- **Single ownership** - Only one pointer can own the object
- **Lightweight** - No overhead compared to raw pointers
- **Movable** - Can transfer ownership
- **Non-copyable** - Cannot be copied

### 2. shared_ptr - Shared Ownership
- **Multiple ownership** - Multiple pointers can share ownership
- **Reference counting** - Deletes object when last pointer is destroyed
- **Thread-safe** - Reference counting is thread-safe
- **Copyable** - Can be copied

### 3. weak_ptr - Non-owning Reference
- **Observer** - Observes objects managed by shared_ptr
- **No ownership** - Doesn't affect reference count
- **Prevents cycles** - Breaks circular references
- **Must be locked** - Convert to shared_ptr to access object

## 🔧 Basic Usage

### unique_ptr Examples
```cpp
#include <iostream>
#include <memory>
#include <vector>

class UniquePtrExample {
public:
    // Basic unique_ptr usage
    void basicUsage() {
        // Create unique_ptr with make_unique
        auto ptr = std::make_unique<int>(42);
        
        std::cout << "Value: " << *ptr << std::endl;  // 42
        
        // unique_ptr automatically deletes the object when it goes out of scope
    }
    
    // Custom object with unique_ptr
    class Resource {
    private:
        std::string m_name;
        
    public:
        Resource(const std::string& name) : m_name(name) {
            std::cout << "Resource " << m_name << " created" << std::endl;
        }
        
        ~Resource() {
            std::cout << "Resource " << m_name << " destroyed" << std::endl;
        }
        
        void doSomething() {
            std::cout << "Resource " << m_name << " is working" << std::endl;
        }
    };
    
    void demonstrateResourceManagement() {
        std::cout << "=== unique_ptr Resource Management ===" << std::endl;
        
        {
            auto resource = std::make_unique<Resource>("FileHandler");
            resource->doSomething();
            
            // Transfer ownership
            auto resource2 = std::move(resource);
            resource2->doSomething();
            
            std::cout << "resource is now: " << (resource ? "valid" : "null") << std::endl;
            std::cout << "resource2 is now: " << (resource2 ? "valid" : "null") << std::endl;
        }  // resource2 goes out of scope, Resource is destroyed
        
        std::cout << "=== End of scope ===" << std::endl;
    }
    
    // unique_ptr with custom deleters
    void customDeleter() {
        // Custom deleter for array
        auto array_deleter = [](int* p) {
            std::cout << "Custom array deleter called" << std::endl;
            delete[] p;
        };
        
        std::unique_ptr<int[], decltype(array_deleter)> arr(new int[5], array_deleter);
        
        for (int i = 0; i < 5; i++) {
            arr[i] = i * 10;
        }
        
        std::cout << "Array values: ";
        for (int i = 0; i < 5; i++) {
            std::cout << arr[i] << " ";
        }
        std::cout << std::endl;
    }
    
    // unique_ptr in containers
    void uniquePtrInContainer() {
        std::vector<std::unique_ptr<Resource>> resources;
        
        // Add resources to vector
        resources.push_back(std::make_unique<Resource>("Resource1"));
        resources.push_back(std::make_unique<Resource>("Resource2"));
        resources.push_back(std::make_unique<Resource>("Resource3"));
        
        // Use resources
        for (const auto& res : resources) {
            res->doSomething();
        }
        
        // Move resource out of vector
        if (!resources.empty()) {
            auto extracted = std::move(resources.back());
            resources.pop_back();
            extracted->doSomething();
        }
        
        // All remaining resources automatically destroyed when vector goes out of scope
    }
};
```

### shared_ptr Examples
```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <thread>
#include <chrono>

class SharedPtrExample {
public:
    class SharedResource {
    private:
        std::string m_name;
        
    public:
        SharedResource(const std::string& name) : m_name(name) {
            std::cout << "SharedResource " << m_name << " created (ref count: 1)" << std::endl;
        }
        
        ~SharedResource() {
            std::cout << "SharedResource " << m_name << " destroyed" << std::endl;
        }
        
        void use() {
            std::cout << "Using SharedResource " << m_name << std::endl;
        }
        
        std::string getName() const { return m_name; }
    };
    
    void basicSharedPtrUsage() {
        std::cout << "=== Basic shared_ptr Usage ===" << std::endl;
        
        // Create shared_ptr
        auto ptr1 = std::make_shared<SharedResource>("Database");
        std::cout << "After creation: " << ptr1.use_count() << " references" << std::endl;
        
        {
            auto ptr2 = ptr1;  // Copy - increases reference count
            std::cout << "After copy: " << ptr1.use_count() << " references" << std::endl;
            
            ptr2->use();
            
            auto ptr3 = ptr1;  // Another copy
            std::cout << "After second copy: " << ptr1.use_count() << " references" << std::endl;
            
        }  // ptr2 and ptr3 go out of scope
        
        std::cout << "After scope exit: " << ptr1.use_count() << " references" << std::endl;
        
        std::cout << "=== End of function ===" << std::endl;
    }
    
    void sharedPtrInContainers() {
        std::cout << "=== shared_ptr in Containers ===" << std::endl;
        
        std::vector<std::shared_ptr<SharedResource>> resources;
        
        auto resource = std::make_shared<SharedResource>("Cache");
        
        // Add to multiple containers
        resources.push_back(resource);
        std::vector<std::shared_ptr<SharedResource>> backup;
        backup.push_back(resource);
        
        std::cout << "Resource references: " << resource.use_count() << std::endl;
        
        // Use resource through any pointer
        resources[0]->use();
        backup[0]->use();
        
        std::cout << "=== End of function ===" << std::endl;
    }
    
    // Thread-safe demonstration
    void threadSafeExample() {
        std::cout << "=== Thread-safe shared_ptr ===" << std::endl;
        
        auto shared_data = std::make_shared<SharedResource>("ThreadSafe");
        std::vector<std::thread> threads;
        
        // Create multiple threads that share the resource
        for (int i = 0; i < 3; i++) {
            threads.emplace_back([shared_data, i]() {
                std::this_thread::sleep_for(std::chrono::milliseconds(100));
                std::cout << "Thread " << i << " using resource (ref count: " 
                         << shared_data.use_count() << ")" << std::endl;
                shared_data->use();
            });
        }
        
        // Wait for all threads to complete
        for (auto& t : threads) {
            t.join();
        }
        
        std::cout << "=== End of thread example ===" << std::endl;
    }
    
    // Custom deleters with shared_ptr
    void customDeleter() {
        auto custom_deleter = [](SharedResource* p) {
            std::cout << "Custom deleter for " << p->getName() << std::endl;
            delete p;
        };
        
        std::shared_ptr<SharedResource> custom_ptr(
            new SharedResource("Custom"), custom_deleter
        );
        
        custom_ptr->use();
        std::cout << "=== End of custom deleter example ===" << std::endl;
    }
};
```

### weak_ptr Examples
```cpp
#include <iostream>
#include <memory>
#include <vector>

class WeakPtrExample {
public:
    class Node {
    private:
        std::string m_name;
        std::vector<std::weak_ptr<Node>> m_children;
        std::weak_ptr<Node> m_parent;
        
    public:
        Node(const std::string& name) : m_name(name) {
            std::cout << "Node " << m_name << " created" << std::endl;
        }
        
        ~Node() {
            std::cout << "Node " << m_name << " destroyed" << std::endl;
        }
        
        void addChild(std::shared_ptr<Node> child) {
            m_children.push_back(child);
            child->m_parent = shared_from_this();  // Enable shared_from_this
        }
        
        void displayChildren() {
            std::cout << "Node " << m_name << " children: ";
            
            for (auto weak_child : m_children) {
                if (auto child = weak_child.lock()) {  // Convert weak_ptr to shared_ptr
                    std::cout << child->m_name << " ";
                } else {
                    std::cout << "(destroyed) ";
                }
            }
            std::cout << std::endl;
        }
        
        void displayParent() {
            if (auto parent = m_parent.lock()) {
                std::cout << "Node " << m_name << " parent: " << parent->m_name << std::endl;
            } else {
                std::cout << "Node " << m_name << " has no parent or parent was destroyed" << std::endl;
            }
        }
        
        std::string getName() const { return m_name; }
    };
    
    // Enable shared_from_this
    class SharedNode : public Node, public std::enable_shared_from_this<SharedNode> {
    public:
        SharedNode(const std::string& name) : Node(name) {}
    };
    
    void demonstrateWeakPtr() {
        std::cout << "=== weak_ptr Demonstration ===" << std::endl;
        
        auto parent = std::make_shared<SharedNode>("Root");
        auto child1 = std::make_shared<SharedNode>("Child1");
        auto child2 = std::make_shared<SharedNode>("Child2");
        
        parent->addChild(child1);
        parent->addChild(child2);
        
        std::cout << "Parent references: " << parent.use_count() << std::endl;
        std::cout << "Child1 references: " << child1.use_count() << std::endl;
        std::cout << "Child2 references: " << child2.use_count() << std::endl;
        
        parent->displayChildren();
        child1->displayParent();
        
        // Remove one child
        child1.reset();
        
        std::cout << "\nAfter child1 reset:" << std::endl;
        parent->displayChildren();  // Shows that child1 was destroyed
        
        std::cout << "=== End of weak_ptr demonstration ===" << std::endl;
    }
    
    // Observer pattern with weak_ptr
    class Subject {
    private:
        std::string m_name;
        std::vector<std::weak_ptr<class Observer>> m_observers;
        
    public:
        Subject(const std::string& name) : m_name(name) {}
        
        void addObserver(std::shared_ptr<Observer> observer) {
            m_observers.push_back(observer);
        }
        
        void notify(const std::string& message) {
            std::cout << "Subject " << m_name << " notifying observers: " << message << std::endl;
            
            // Remove expired observers and notify valid ones
            auto it = m_observers.begin();
            while (it != m_observers.end()) {
                if (auto observer = it->lock()) {
                    observer->onNotify(m_name, message);
                    ++it;
                } else {
                    // Remove expired observer
                    it = m_observers.erase(it);
                }
            }
        }
    };
    
    class Observer {
    private:
        std::string m_name;
        
    public:
        Observer(const std::string& name) : m_name(name) {
            std::cout << "Observer " << m_name << " created" << std::endl;
        }
        
        ~Observer() {
            std::cout << "Observer " << m_name << " destroyed" << std::endl;
        }
        
        void onNotify(const std::string& subject, const std::string& message) {
            std::cout << "Observer " << m_name << " received from " 
                     << subject << ": " << message << std::endl;
        }
    };
    
    void observerPattern() {
        std::cout << "=== Observer Pattern with weak_ptr ===" << std::endl;
        
        auto subject = std::make_shared<Subject>("NewsAgency");
        auto observer1 = std::make_shared<Observer>("Reader1");
        auto observer2 = std::make_shared<Observer>("Reader2");
        
        subject->addObserver(observer1);
        subject->addObserver(observer2);
        
        subject->notify("Breaking news!");
        
        // Observer1 stops observing (gets destroyed)
        observer1.reset();
        
        std::cout << "\nAfter observer1 destruction:" << std::endl;
        subject->notify("Another news update!");
        
        std::cout << "=== End of observer pattern ===" << std::endl;
    }
};
```

## 🎮 Practical Examples

### Example 1: Complete Smart Pointer Demonstration
```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <map>

class SmartPointerDemo {
public:
    class DatabaseConnection {
    private:
        std::string m_connection_string;
        
    public:
        DatabaseConnection(const std::string& conn_str) 
            : m_connection_string(conn_str) {
            std::cout << "Database connection established: " << m_connection_string << std::endl;
        }
        
        ~DatabaseConnection() {
            std::cout << "Database connection closed: " << m_connection_string << std::endl;
        }
        
        void query(const std::string& sql) {
            std::cout << "Executing query: " << sql << std::endl;
        }
    };
    
    class ResourceManager {
    private:
        std::unique_ptr<DatabaseConnection> m_connection;
        std::map<std::string, std::shared_ptr<class Cache>> m_caches;
        
    public:
        ResourceManager() {
            // unique_ptr for exclusive ownership
            m_connection = std::make_unique<DatabaseConnection>("localhost:5432");
        }
        
        // Factory method returning shared_ptr
        std::shared_ptr<Cache> getCache(const std::string& name) {
            auto it = m_caches.find(name);
            if (it != m_caches.end()) {
                return it->second;  // Return existing cache
            }
            
            // Create new cache and share it
            auto cache = std::make_shared<Cache>(name);
            m_caches[name] = cache;
            return cache;
        }
        
        void performOperation() {
            m_connection->query("SELECT * FROM users");
            
            auto user_cache = getCache("users");
            auto product_cache = getCache("products");
            
            user_cache->store("user1", "data1");
            product_cache->store("product1", "data2");
        }
        
    private:
        class Cache {
        private:
            std::string m_name;
            std::map<std::string, std::string> m_data;
            
        public:
            Cache(const std::string& name) : m_name(name) {
                std::cout << "Cache " << m_name << " created" << std::endl;
            }
            
            ~Cache() {
                std::cout << "Cache " << m_name << " destroyed" << std::endl;
            }
            
            void store(const std::string& key, const std::string& value) {
                m_data[key] = value;
                std::cout << "Cache " << m_name << " stored: " << key << " -> " << value << std::endl;
            }
            
            std::string get(const std::string& key) {
                auto it = m_data.find(key);
                return (it != m_data.end()) ? it->second : "";
            }
        };
    };
    
    void demonstrateCompleteExample() {
        std::cout << "=== Complete Smart Pointer Example ===" << std::endl;
        
        {
            ResourceManager manager;
            manager.performOperation();
            
            // Multiple parts of the system can share the same cache
            auto cache1 = manager.getCache("users");
            auto cache2 = manager.getCache("users");  // Same cache object
            
            std::cout << "Cache references: " << cache1.use_count() << std::endl;
            
        }  // ResourceManager and all resources automatically cleaned up
        
        std::cout << "=== End of complete example ===" << std::endl;
    }
};
```

### Example 2: Performance Comparison
```cpp
#include <iostream>
#include <memory>
#include <chrono>
#include <vector>

class PerformanceComparison {
public:
    void comparePerformance() {
        const int SIZE = 1000000;
        
        // Raw pointer performance
        auto start = std::chrono::high_resolution_clock::now();
        {
            int* raw_array = new int[SIZE];
            for (int i = 0; i < SIZE; i++) {
                raw_array[i] = i * 2;
            }
            long long sum = 0;
            for (int i = 0; i < SIZE; i++) {
                sum += raw_array[i];
            }
            delete[] raw_array;
        }
        auto end = std::chrono::high_resolution_clock::now();
        auto raw_time = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        // unique_ptr performance
        start = std::chrono::high_resolution_clock::now();
        {
            auto unique_array = std::make_unique<int[]>(SIZE);
            for (int i = 0; i < SIZE; i++) {
                unique_array[i] = i * 2;
            }
            long long sum = 0;
            for (int i = 0; i < SIZE; i++) {
                sum += unique_array[i];
            }
        }
        end = std::chrono::high_resolution_clock::now();
        auto unique_time = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        // vector performance (recommended)
        start = std::chrono::high_resolution_clock::now();
        {
            std::vector<int> vec(SIZE);
            for (int i = 0; i < SIZE; i++) {
                vec[i] = i * 2;
            }
            long long sum = 0;
            for (int i = 0; i < SIZE; i++) {
                sum += vec[i];
            }
        }
        end = std::chrono::high_resolution_clock::now();
        auto vector_time = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
        
        std::cout << "Performance comparison (1M elements):" << std::endl;
        std::cout << "Raw pointer:  " << raw_time.count() << " μs" << std::endl;
        std::cout << "unique_ptr:   " << unique_time.count() << " μs" << std::endl;
        std::cout << "vector:       " << vector_time.count() << " μs" << std::endl;
        
        std::cout << "unique_ptr overhead: " << 
            (double)unique_time.count() / raw_time.count() << "x" << std::endl;
        std::cout << "vector overhead: " << 
            (double)vector_time.count() / raw_time.count() << "x" << std::endl;
    }
};
```

## ⚡ Best Practices

### When to Use Each Smart Pointer

#### unique_ptr
✅ **Use when:**
- You need exclusive ownership
- Performance is critical
- You want to transfer ownership
- Resource should not be shared

❌ **Avoid when:**
- You need shared ownership
- You need to copy the pointer
- Multiple parts need access

#### shared_ptr
✅ **Use when:**
- Multiple owners need access
- You need to copy pointers
- Lifetime is complex
- Thread-safe sharing is needed

❌ **Avoid when:**
- Ownership is exclusive
- Performance is critical
- Circular references are possible

#### weak_ptr
✅ **Use when:**
- You need to observe shared resources
- Breaking circular references
- Observer pattern
- Caching systems

❌ **Avoid when:**
- You need ownership
- You need direct access without locking
- Performance is critical

### Common Patterns

#### Factory Pattern
```cpp
class Factory {
public:
    static std::unique_ptr<Resource> createResource() {
        return std::make_unique<Resource>();
    }
    
    static std::shared_ptr<Resource> createSharedResource() {
        return std::make_shared<Resource>();
    }
};
```

#### Pimpl Idiom
```cpp
class PublicInterface {
private:
    class Implementation;
    std::unique_ptr<Implementation> pImpl;
    
public:
    PublicInterface();
    ~PublicInterface();
    
    // Public interface delegates to pImpl
};
```

## 🐛 Common Pitfalls

### 1. Circular References
```cpp
// Problem - circular reference
class Node {
public:
    std::shared_ptr<Node> parent;
    std::shared_ptr<Node> child;
};

auto parent = std::make_shared<Node>();
auto child = std::make_shared<Node>();
parent->child = child;
child->parent = parent;  // Circular reference!

// Solution - use weak_ptr for back references
class Node {
public:
    std::weak_ptr<Node> parent;  // weak_ptr breaks cycle
    std::shared_ptr<Node> child;
};
```

### 2. Mixing Raw and Smart Pointers
```cpp
// Problem - mixing ownership
std::unique_ptr<int> smart = std::make_unique<int>(42);
int* raw = smart.get();
delete raw;  // Double deletion!

// Solution - be consistent
std::unique_ptr<int> smart = std::make_unique<int>(42);
int* raw = smart.get();
// Don't delete raw - let smart_ptr handle it
```

### 3. Dangling weak_ptr
```cpp
std::shared_ptr<int> shared = std::make_shared<int>(42);
std::weak_ptr<int> weak = shared;

shared.reset();  // Destroy the object

if (auto locked = weak.lock()) {  // Check before using
    std::cout << *locked << std::endl;
} else {
    std::cout << "Object was destroyed" << std::endl;
}
```

## 🚀 Migration Guide

### From Raw Pointers to Smart Pointers

```cpp
// Before
class OldClass {
private:
    Resource* m_resource;
    
public:
    OldClass() : m_resource(new Resource()) {}
    ~OldClass() { delete m_resource; }
    
    // Need to handle copy constructor and assignment operator
};

// After
class NewClass {
private:
    std::unique_ptr<Resource> m_resource;
    
public:
    NewClass() : m_resource(std::make_unique<Resource>()) {}
    // Destructor automatically handled
    // Copy and assignment properly deleted (rule of five)
};
```

---

**Examples in this file**: 2 comprehensive programs  
**Key Concepts**: RAII, ownership semantics, memory management  
**Time Complexity**: O(1) for most operations  
**Space Complexity**: O(1) overhead per smart pointer
