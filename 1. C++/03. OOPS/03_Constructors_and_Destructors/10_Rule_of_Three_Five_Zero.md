# Rule of Three, Five, and Zero in C++ - Complete Guide

## 📖 Overview

The Rule of Three, Five, and Zero are guidelines for managing resources in C++ classes. They define which special member functions should be implemented based on whether a class manages resources. Following these rules prevents memory leaks, double deletions, and undefined behavior.

---

## 🎯 The Rules Explained

| Rule | Description | Special Members |
|------|-------------|-----------------|
| **Rule of Three** | If you need one, you need all three | Destructor, Copy Constructor, Copy Assignment |
| **Rule of Five** | Adds move operations | + Move Constructor, Move Assignment |
| **Rule of Zero** | Prefer no custom resource management | Use standard containers/smart pointers |

---

## 1. **Rule of Three: The Problem**

```cpp
#include <iostream>
#include <cstring>
using namespace std;

// WRONG: Violates Rule of Three - DANGEROUS!
class BadString {
private:
    char* data;
    size_t length;
    
public:
    // Constructor
    BadString(const char* str) {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "Created: " << data << endl;
    }
    
    // Destructor (exists)
    ~BadString() {
        cout << "Destroyed: " << data << endl;
        delete[] data;
    }
    
    // NO copy constructor! (uses shallow copy)
    // NO copy assignment! (uses shallow copy)
    
    void display() const {
        cout << "String: " << data << " (length=" << length << ")" << endl;
    }
    
    void setChar(size_t index, char c) {
        if (index < length) data[index] = c;
    }
};

int main() {
    cout << "=== Rule of Three Violation ===" << endl;
    
    cout << "\n1. Creating objects:" << endl;
    BadString s1("Hello");
    BadString s2 = s1;  // SHALLOW COPY! Both point to same memory
    
    cout << "\n2. Before modification:" << endl;
    cout << "s1: "; s1.display();
    cout << "s2: "; s2.display();
    
    cout << "\n3. Modifying s1:" << endl;
    s1.setChar(0, 'J');
    cout << "s1 after: "; s1.display();
    cout << "s2 after: "; s2.display();  // s2 also changed!
    
    cout << "\n4. Destructors will cause DOUBLE DELETE!" << endl;
    // When destructors run, same memory freed twice -> undefined behavior!
    
    return 0;
}
```

**Output:**
```
=== Rule of Three Violation ===

1. Creating objects:
Created: Hello

2. Before modification:
s1: String: Hello (length=5)
s2: String: Hello (length=5)

3. Modifying s1:
s1 after: String: Jello (length=5)
s2 after: String: Jello (length=5)

4. Destructors will cause DOUBLE DELETE!
Destroyed: Jello
Destroyed: Jello
```

---

## 2. **Rule of Three: Correct Implementation**

```cpp
#include <iostream>
#include <cstring>
using namespace std;

class GoodString {
private:
    char* data;
    size_t length;
    
public:
    // Constructor
    GoodString(const char* str = "") {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "Created: " << data << endl;
    }
    
    // Destructor (1 of 3)
    ~GoodString() {
        if (data) {
            cout << "Destroyed: " << data << endl;
            delete[] data;
            data = nullptr;
        }
    }
    
    // Copy Constructor (2 of 3)
    GoodString(const GoodString& other) {
        length = other.length;
        data = new char[length + 1];
        strcpy(data, other.data);
        cout << "Copied: " << data << " (from " << other.data << ")" << endl;
    }
    
    // Copy Assignment Operator (3 of 3)
    GoodString& operator=(const GoodString& other) {
        if (this != &other) {  // Self-assignment check
            cout << "Assigning: " << data << " = " << other.data << endl;
            delete[] data;
            length = other.length;
            data = new char[length + 1];
            strcpy(data, other.data);
        }
        return *this;
    }
    
    void display() const {
        cout << "String: " << data << " (length=" << length << ")" << endl;
    }
    
    void setChar(size_t index, char c) {
        if (index < length) data[index] = c;
    }
    
    size_t getLength() const { return length; }
};

int main() {
    cout << "=== Rule of Three Correct Implementation ===" << endl;
    
    cout << "\n1. Creating objects:" << endl;
    GoodString s1("Hello");
    GoodString s2 = s1;  // Copy constructor - DEEP COPY
    
    cout << "\n2. Before modification:" << endl;
    cout << "s1: "; s1.display();
    cout << "s2: "; s2.display();
    
    cout << "\n3. Modifying s1:" << endl;
    s1.setChar(0, 'J');
    cout << "s1 after: "; s1.display();
    cout << "s2 after: "; s2.display();  // s2 unchanged!
    
    cout << "\n4. Copy assignment:" << endl;
    GoodString s3("World");
    s3 = s1;  // Copy assignment
    cout << "s3: "; s3.display();
    
    cout << "\n5. Self-assignment test:" << endl;
    s1 = s1;  // Should not crash
    cout << "Self-assignment handled safely" << endl;
    
    cout << "\n6. Destructors called automatically" << endl;
    
    return 0;
}
```

**Output:**
```
=== Rule of Three Correct Implementation ===

1. Creating objects:
Created: Hello
Copied: Hello (from Hello)

2. Before modification:
s1: String: Hello (length=5)
s2: String: Hello (length=5)

3. Modifying s1:
s1 after: String: Jello (length=5)
s2 after: String: Hello (length=5)

4. Copy assignment:
Created: World
Assigning: World = Jello
s3: String: Jello (length=5)

5. Self-assignment test:
Self-assignment handled safely

6. Destructors called automatically
Destroyed: Jello
Destroyed: Jello
Destroyed: Jello
```

---

## 3. **Rule of Five: Adding Move Operations**

```cpp
#include <iostream>
#include <cstring>
#include <utility>
using namespace std;

class ModernString {
private:
    char* data;
    size_t length;
    
public:
    // Constructor
    ModernString(const char* str = "") {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        cout << "Created: " << data << endl;
    }
    
    // Destructor
    ~ModernString() {
        if (data) {
            cout << "Destroyed: " << data << endl;
            delete[] data;
            data = nullptr;
        }
    }
    
    // Copy Constructor
    ModernString(const ModernString& other) {
        length = other.length;
        data = new char[length + 1];
        strcpy(data, other.data);
        cout << "Copied: " << data << endl;
    }
    
    // Copy Assignment
    ModernString& operator=(const ModernString& other) {
        if (this != &other) {
            cout << "Copy Assign: " << data << " = " << other.data << endl;
            delete[] data;
            length = other.length;
            data = new char[length + 1];
            strcpy(data, other.data);
        }
        return *this;
    }
    
    // Move Constructor (C++11)
    ModernString(ModernString&& other) noexcept 
        : data(other.data), length(other.length) {
        other.data = nullptr;
        other.length = 0;
        cout << "Moved: " << data << endl;
    }
    
    // Move Assignment (C++11)
    ModernString& operator=(ModernString&& other) noexcept {
        if (this != &other) {
            cout << "Move Assign: " << (data ? data : "empty") 
                 << " = " << other.data << endl;
            delete[] data;
            data = other.data;
            length = other.length;
            other.data = nullptr;
            other.length = 0;
        }
        return *this;
    }
    
    void display() const {
        if (data) {
            cout << "String: " << data << " (length=" << length << ")" << endl;
        } else {
            cout << "String: (empty)" << endl;
        }
    }
};

ModernString createString() {
    ModernString temp("Temporary");
    return temp;  // Move constructor
}

int main() {
    cout << "=== Rule of Five: Move Operations ===" << endl;
    
    cout << "\n1. Copy operations (expensive):" << endl;
    ModernString s1("Hello");
    ModernString s2 = s1;  // Copy
    ModernString s3("World");
    s3 = s1;  // Copy assignment
    
    cout << "\n2. Move operations (efficient):" << endl;
    ModernString s4 = std::move(s1);  // Move constructor
    cout << "s1 after move: "; s1.display();
    cout << "s4: "; s4.display();
    
    ModernString s5("Temp");
    s5 = std::move(s2);  // Move assignment
    cout << "s2 after move: "; s2.display();
    cout << "s5: "; s5.display();
    
    cout << "\n3. Returning from function (move):" << endl;
    ModernString s6 = createString();
    s6.display();
    
    cout << "\n4. Performance comparison:" << endl;
    cout << "Copy: Allocates new memory, copies all data" << endl;
    cout << "Move: Transfers ownership, no allocation" << endl;
    
    return 0;
}
```

---

## 4. **Rule of Zero: Using RAII**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Rule of Zero: Use standard containers and smart pointers
class Employee {
private:
    string name;           // std::string manages its own memory
    int id;                // Primitive type
    vector<string> skills; // std::vector manages its own memory
    unique_ptr<int> bonus; // std::unique_ptr manages dynamic memory
    
public:
    // No need to write destructor, copy, or move operations
    // Compiler-generated ones work correctly
    
    Employee(string n, int i) : name(n), id(i) {
        bonus = make_unique<int>(0);
    }
    
    void addSkill(const string& skill) {
        skills.push_back(skill);
    }
    
    void setBonus(int b) {
        *bonus = b;
    }
    
    void display() const {
        cout << "Employee: " << name << " (ID: " << id << ")" << endl;
        cout << "Skills: ";
        for (const auto& s : skills) {
            cout << s << " ";
        }
        cout << endl;
        cout << "Bonus: $" << *bonus << endl;
    }
};

// Another Rule of Zero example
class Document {
private:
    string title;
    string content;
    vector<string> tags;
    vector<string> authors;
    
public:
    // Compiler-generated special members are sufficient
    Document(string t) : title(t) {}
    
    void addContent(const string& c) { content += c; }
    void addTag(const string& t) { tags.push_back(t); }
    void addAuthor(const string& a) { authors.push_back(a); }
    
    void display() const {
        cout << "Document: " << title << endl;
        cout << "Content length: " << content.length() << endl;
        cout << "Tags: ";
        for (const auto& t : tags) cout << t << " ";
        cout << endl;
        cout << "Authors: ";
        for (const auto& a : authors) cout << a << " ";
        cout << endl;
    }
};

class RuleOfZeroManager {
private:
    vector<unique_ptr<Employee>> employees;
    vector<Document> documents;
    
public:
    // No custom destructor needed - smart pointers handle cleanup
    
    void addEmployee(Employee* emp) {
        employees.emplace_back(emp);
    }
    
    void addDocument(const Document& doc) {
        documents.push_back(doc);
    }
    
    void displayAll() const {
        cout << "\n=== Employees ===" << endl;
        for (const auto& emp : employees) {
            emp->display();
            cout << endl;
        }
        
        cout << "=== Documents ===" << endl;
        for (const auto& doc : documents) {
            doc.display();
            cout << endl;
        }
    }
};

int main() {
    cout << "=== Rule of Zero: Using RAII ===" << endl;
    
    cout << "\n1. Creating employees:" << endl;
    Employee e1("Alice", 1001);
    e1.addSkill("C++");
    e1.addSkill("Python");
    e1.setBonus(5000);
    
    Employee e2("Bob", 1002);
    e2.addSkill("Java");
    e2.addSkill("SQL");
    e2.setBonus(4000);
    
    cout << "\n2. Creating documents:" << endl;
    Document doc1("Project Plan");
    doc1.addContent("Project timeline and milestones");
    doc1.addTag("planning");
    doc1.addAuthor("Alice");
    
    Document doc2("Technical Spec");
    doc2.addContent("System architecture design");
    doc2.addTag("design");
    doc2.addAuthor("Bob");
    
    cout << "\n3. Managing with Rule of Zero container:" << endl;
    RuleOfZeroManager manager;
    manager.addEmployee(new Employee(e1));  // Copy - OK
    manager.addEmployee(new Employee(e2));  // Copy - OK
    manager.addDocument(doc1);
    manager.addDocument(doc2);
    
    manager.displayAll();
    
    cout << "\n4. Benefits of Rule of Zero:" << endl;
    cout << "✓ No manual resource management" << endl;
    cout << "✓ No risk of memory leaks" << endl;
    cout << "✓ Compiler-generated members are correct" << endl;
    cout << "✓ Exception-safe by default" << endl;
    cout << "✓ Easier to maintain" << endl;
    
    return 0;
}
```

---

## 5. **Rule Comparison Matrix**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// Rule of Three: Manual resource management
class RuleOfThree {
private:
    int* data;
    size_t size;
    
public:
    RuleOfThree(size_t s) : size(s) {
        data = new int[size];
        cout << "RuleOfThree: allocated " << size << " ints" << endl;
    }
    
    ~RuleOfThree() {
        delete[] data;
        cout << "RuleOfThree: freed " << size << " ints" << endl;
    }
    
    RuleOfThree(const RuleOfThree& other) : size(other.size) {
        data = new int[size];
        for (size_t i = 0; i < size; i++) data[i] = other.data[i];
        cout << "RuleOfThree: copied" << endl;
    }
    
    RuleOfThree& operator=(const RuleOfThree& other) {
        if (this != &other) {
            delete[] data;
            size = other.size;
            data = new int[size];
            for (size_t i = 0; i < size; i++) data[i] = other.data[i];
            cout << "RuleOfThree: assigned" << endl;
        }
        return *this;
    }
};

// Rule of Five: Adds move operations
class RuleOfFive {
private:
    int* data;
    size_t size;
    
public:
    RuleOfFive(size_t s) : size(s) {
        data = new int[size];
        cout << "RuleOfFive: allocated " << size << " ints" << endl;
    }
    
    ~RuleOfFive() {
        delete[] data;
        cout << "RuleOfFive: freed " << size << " ints" << endl;
    }
    
    RuleOfFive(const RuleOfFive& other) : size(other.size) {
        data = new int[size];
        for (size_t i = 0; i < size; i++) data[i] = other.data[i];
        cout << "RuleOfFive: copied" << endl;
    }
    
    RuleOfFive& operator=(const RuleOfFive& other) {
        if (this != &other) {
            delete[] data;
            size = other.size;
            data = new int[size];
            for (size_t i = 0; i < size; i++) data[i] = other.data[i];
            cout << "RuleOfFive: copy assigned" << endl;
        }
        return *this;
    }
    
    RuleOfFive(RuleOfFive&& other) noexcept 
        : data(other.data), size(other.size) {
        other.data = nullptr;
        other.size = 0;
        cout << "RuleOfFive: moved" << endl;
    }
    
    RuleOfFive& operator=(RuleOfFive&& other) noexcept {
        if (this != &other) {
            delete[] data;
            data = other.data;
            size = other.size;
            other.data = nullptr;
            other.size = 0;
            cout << "RuleOfFive: move assigned" << endl;
        }
        return *this;
    }
};

// Rule of Zero: Use standard library
class RuleOfZero {
private:
    vector<int> data;
    
public:
    RuleOfZero(size_t s) : data(s) {
        cout << "RuleOfZero: created with " << s << " elements" << endl;
    }
    // Compiler-generated destructor, copy, move are correct
};

int main() {
    cout << "=== Rule Comparison Matrix ===" << endl;
    
    cout << "\n1. Rule of Three:" << endl;
    {
        RuleOfThree r1(100);
        RuleOfThree r2 = r1;  // Copy
        RuleOfThree r3(50);
        r3 = r1;  // Copy assignment
    }
    
    cout << "\n2. Rule of Five (with move):" << endl;
    {
        RuleOfFive r1(100);
        RuleOfFive r2 = std::move(r1);  // Move
        RuleOfFive r3(50);
        r3 = std::move(r2);  // Move assignment
    }
    
    cout << "\n3. Rule of Zero:" << endl;
    {
        RuleOfZero z1(100);
        RuleOfZero z2 = z1;  // Copy - vector handles it
        RuleOfZero z3 = std::move(z1);  // Move - vector handles it
    }
    
    cout << "\n4. When to use each rule:" << endl;
    cout << "Rule of Three:   Manual resource management (custom allocators)" << endl;
    cout << "Rule of Five:    Manual + move semantics (performance critical)" << endl;
    cout << "Rule of Zero:    Default (preferred for most code)" << endl;
    
    return 0;
}
```

---

## 6. **Practical Example: Database Connection Pool**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <mutex>
using namespace std;

// Rule of Zero: Connection managed by smart pointers
class Connection {
private:
    int id;
    string host;
    int port;
    bool connected;
    
public:
    Connection(int i, string h, int p) : id(i), host(h), port(p), connected(false) {
        cout << "Connection " << id << " created" << endl;
    }
    
    void connect() {
        if (!connected) {
            connected = true;
            cout << "Connection " << id << " connected to " << host << ":" << port << endl;
        }
    }
    
    void disconnect() {
        if (connected) {
            connected = false;
            cout << "Connection " << id << " disconnected" << endl;
        }
    }
    
    bool isConnected() const { return connected; }
    int getId() const { return id; }
    
    ~Connection() {
        if (connected) disconnect();
        cout << "Connection " << id << " destroyed" << endl;
    }
};

// Rule of Five: Pool manages connections manually
class ConnectionPool {
private:
    vector<unique_ptr<Connection>> connections;
    mutex poolMutex;
    int nextId;
    int maxSize;
    
public:
    ConnectionPool(int max, string host, int port) : nextId(1), maxSize(max) {
        cout << "Pool created (max=" << max << ")" << endl;
        for (int i = 0; i < max; i++) {
            connections.push_back(make_unique<Connection>(nextId++, host, port));
        }
    }
    
    // Rule of Five: Copy operations disabled
    ConnectionPool(const ConnectionPool&) = delete;
    ConnectionPool& operator=(const ConnectionPool&) = delete;
    
    // Move operations
    ConnectionPool(ConnectionPool&& other) noexcept 
        : connections(std::move(other.connections)), 
          nextId(other.nextId), 
          maxSize(other.maxSize) {
        cout << "Pool moved" << endl;
    }
    
    ConnectionPool& operator=(ConnectionPool&& other) noexcept {
        if (this != &other) {
            connections = std::move(other.connections);
            nextId = other.nextId;
            maxSize = other.maxSize;
            cout << "Pool move assigned" << endl;
        }
        return *this;
    }
    
    // Destructor - connections automatically cleaned by unique_ptr
    ~ConnectionPool() {
        cout << "Pool destroyed" << endl;
    }
    
    Connection* acquire() {
        lock_guard<mutex> lock(poolMutex);
        for (auto& conn : connections) {
            if (!conn->isConnected()) {
                conn->connect();
                return conn.get();
            }
        }
        return nullptr;
    }
    
    void release(Connection* conn) {
        if (conn) {
            conn->disconnect();
        }
    }
    
    size_t size() const { return connections.size(); }
};

// Rule of Zero: Client uses RAII
class DatabaseClient {
private:
    string name;
    ConnectionPool& pool;
    Connection* currentConn;
    
public:
    DatabaseClient(string n, ConnectionPool& p) : name(n), pool(p), currentConn(nullptr) {
        cout << "Client " << name << " created" << endl;
    }
    
    void execute(const string& query) {
        if (!currentConn) {
            currentConn = pool.acquire();
        }
        if (currentConn && currentConn->isConnected()) {
            cout << "Client " << name << " executing: " << query 
                 << " (conn=" << currentConn->getId() << ")" << endl;
        }
    }
    
    void disconnect() {
        if (currentConn) {
            pool.release(currentConn);
            currentConn = nullptr;
        }
    }
    
    // Rule of Zero: Compiler-generated destructor handles cleanup
    ~DatabaseClient() {
        disconnect();
        cout << "Client " << name << " destroyed" << endl;
    }
};

int main() {
    cout << "=== Database Connection Pool with Rule of Five/Zero ===" << endl;
    
    cout << "\n1. Creating connection pool:" << endl;
    ConnectionPool pool(3, "localhost", 5432);
    
    cout << "\n2. Creating clients:" << endl;
    DatabaseClient client1("App1", pool);
    DatabaseClient client2("App2", pool);
    DatabaseClient client3("App3", pool);
    
    cout << "\n3. Executing queries:" << endl;
    client1.execute("SELECT * FROM users");
    client2.execute("SELECT * FROM products");
    client3.execute("SELECT * FROM orders");
    
    cout << "\n4. Moving pool (demonstrating move operations):" << endl;
    ConnectionPool pool2 = std::move(pool);
    
    cout << "\n5. Clients using moved pool:" << endl;
    DatabaseClient client4("App4", pool2);
    client4.execute("INSERT INTO logs VALUES('test')");
    
    cout << "\n6. Cleanup (destructors called automatically):" << endl;
    
    return 0;
}
```

---

## 📊 Rule Summary Table

| Rule | Destructor | Copy Constructor | Copy Assignment | Move Constructor | Move Assignment | When to Use |
|------|------------|------------------|-----------------|------------------|-----------------|-------------|
| **Three** | ✓ Custom | ✓ Custom | ✓ Custom | ✗ Not needed | ✗ Not needed | Manual resource management (C++98) |
| **Five** | ✓ Custom | ✓ Custom | ✓ Custom | ✓ Custom | ✓ Custom | Manual + move semantics (C++11) |
| **Zero** | ✗ Default | ✗ Default | ✗ Default | ✗ Default | ✗ Default | Use RAII types (preferred) |

---

## ✅ Best Practices

1. **Prefer Rule of Zero** - Use standard containers and smart pointers
2. **Follow Rule of Five** when manual resource management is necessary
3. **Always implement Rule of Three** if you need custom destructor
4. **Use `= default`** for compiler-generated special members
5. **Use `= delete`** to disable unwanted operations
6. **Mark move operations `noexcept`** for optimal performance

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Missing copy operations** | Shallow copy, double delete | Implement or delete them |
| **Missing move operations** | Copies instead of moves | Add move operations |
| **Self-assignment not checked** | Resource corruption | Check `this != &other` |
| **Move without `noexcept`** | Copies instead of moves | Add `noexcept` |
| **Not following Rule of Zero** | Unnecessary complexity | Use RAII types |

---

## ✅ Key Takeaways

1. **Rule of Three**: Destructor, Copy Constructor, Copy Assignment
2. **Rule of Five**: + Move Constructor, Move Assignment
3. **Rule of Zero**: Prefer RAII types, let compiler generate special members
4. **Rule of Three/Five** applies when managing resources manually
5. **Rule of Zero** is the modern C++ best practice
6. **Use `= default` and `= delete`** to control special members

---
---

## Next Step

- Go to [Encapsulation](../04_Encapsulation/README.md) to continue with Encapsulation.
