# 10_Exception_Handling/05_RAII.md

# RAII (Resource Acquisition Is Initialization) in C++ - Complete Guide

## 📖 Overview

RAII (Resource Acquisition Is Initialization) is a fundamental C++ programming idiom where resource acquisition is tied to object lifetime. Resources are acquired in constructors and released in destructors, ensuring that resources are properly cleaned up even when exceptions occur. RAII is the cornerstone of exception-safe C++ code.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **RAII** | Resource Acquisition Is Initialization |
| **Constructor** | Acquires resources |
| **Destructor** | Releases resources |
| **Exception Safety** | Resources released during stack unwinding |
| **Scope-based Management** | Resources tied to object lifetime |

---

## 1. **Basic RAII Concept**

```cpp
#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

// Without RAII (manual resource management - error prone)
class BadFileHandler {
private:
    FILE* file;
    
public:
    BadFileHandler(const char* filename) {
        file = fopen(filename, "w");
        if (!file) {
            throw runtime_error("Cannot open file");
        }
    }
    
    void write(const char* data) {
        if (file) {
            fprintf(file, "%s\n", data);
        }
    }
    
    void close() {
        if (file) {
            fclose(file);
            file = nullptr;
        }
    }
    
    ~BadFileHandler() {
        // Not automatically called if exception thrown before close
    }
};

// With RAII (automatic resource management)
class FileHandler {
private:
    FILE* file;
    
public:
    FileHandler(const char* filename) : file(nullptr) {
        file = fopen(filename, "w");
        if (!file) {
            throw runtime_error("Cannot open file");
        }
        cout << "File opened: " << filename << endl;
    }
    
    ~FileHandler() {
        if (file) {
            fclose(file);
            cout << "File closed automatically" << endl;
        }
    }
    
    void write(const char* data) {
        if (file) {
            fprintf(file, "%s\n", data);
        }
    }
    
    // Prevent copying
    FileHandler(const FileHandler&) = delete;
    FileHandler& operator=(const FileHandler&) = delete;
};

void riskyFunction() {
    FileHandler file("test.txt");
    file.write("First line");
    file.write("Second line");
    // No need to close - destructor will handle it
    throw runtime_error("Something went wrong!");
    file.write("This won't execute");
}

int main() {
    cout << "=== Basic RAII Concept ===" << endl;
    
    cout << "\n1. RAII in normal flow:" << endl;
    {
        FileHandler file("normal.txt");
        file.write("Normal operation");
    }  // File automatically closed
    
    cout << "\n2. RAII with exceptions (stack unwinding):" << endl;
    try {
        riskyFunction();
    } catch (const exception& e) {
        cout << "Caught: " << e.what() << endl;
    }
    
    cout << "\nFile will be closed even though exception occurred!" << endl;
    
    return 0;
}
```

**Output:**
```
=== Basic RAII Concept ===

1. RAII in normal flow:
File opened: normal.txt
File closed automatically

2. RAII with exceptions (stack unwinding):
File opened: test.txt
File closed automatically
Caught: Something went wrong!

File will be closed even though exception occurred!
```

---

## 2. **RAII for Dynamic Memory**

```cpp
#include <iostream>
#include <memory>
#include <vector>
using namespace std;

// Manual memory management (error prone)
class ManualBuffer {
private:
    int* data;
    size_t size;
    
public:
    ManualBuffer(size_t s) : size(s) {
        data = new int[size];
        cout << "ManualBuffer: allocated " << size << " ints" << endl;
    }
    
    ~ManualBuffer() {
        delete[] data;
        cout << "ManualBuffer: freed " << size << " ints" << endl;
    }
    
    void set(size_t index, int value) {
        if (index < size) data[index] = value;
    }
    
    // Need copy constructor and assignment (Rule of Three)
    ManualBuffer(const ManualBuffer&) = delete;
    ManualBuffer& operator=(const ManualBuffer&) = delete;
};

// RAII with smart pointers
class SmartBuffer {
private:
    unique_ptr<int[]> data;
    size_t size;
    
public:
    SmartBuffer(size_t s) : size(s), data(make_unique<int[]>(s)) {
        cout << "SmartBuffer: allocated " << size << " ints" << endl;
    }
    
    void set(size_t index, int value) {
        if (index < size) data[index] = value;
    }
    
    int get(size_t index) const {
        return (index < size) ? data[index] : -1;
    }
    
    // No need for destructor, copy, move - Rule of Zero
};

class ResourceManager {
private:
    vector<unique_ptr<ManualBuffer>> buffers;
    
public:
    void addBuffer(size_t size) {
        buffers.push_back(make_unique<ManualBuffer>(size));
    }
    
    // No need for manual cleanup - unique_ptr handles it
};

void createBuffers() {
    SmartBuffer sb(1000);  // Automatically managed
    sb.set(0, 42);
    
    ResourceManager rm;
    rm.addBuffer(100);
    rm.addBuffer(200);
    rm.addBuffer(300);
    // All buffers automatically freed
}

int main() {
    cout << "=== RAII for Dynamic Memory ===" << endl;
    
    cout << "\n1. Manual buffer (needs explicit cleanup):" << endl;
    {
        ManualBuffer mb(100);
        mb.set(0, 10);
    }  // Destructor called
    
    cout << "\n2. Smart buffer (automatically managed):" << endl;
    {
        SmartBuffer sb(200);
        sb.set(0, 20);
    }  // Automatic cleanup
    
    cout << "\n3. Resource manager with multiple buffers:" << endl;
    createBuffers();
    
    cout << "\nAll resources automatically freed!" << endl;
    
    return 0;
}
```

---

## 3. **RAII for Mutex Locks**

```cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <vector>
#include <chrono>
using namespace std;

class Counter {
private:
    int value;
    mutex mtx;
    
public:
    Counter() : value(0) {}
    
    // Bad: manual lock/unlock (error prone)
    void incrementBad() {
        mtx.lock();
        value++;
        // If exception here, mutex never unlocked!
        mtx.unlock();
    }
    
    // Good: RAII with lock_guard
    void increment() {
        lock_guard<mutex> lock(mtx);  // Lock acquired
        value++;                       // Automatically unlocked on exit
    }
    
    int getValue() const {
        lock_guard<mutex> lock(mtx);
        return value;
    }
};

class ThreadSafeQueue {
private:
    vector<int> data;
    mutable mutex mtx;
    
public:
    void push(int value) {
        lock_guard<mutex> lock(mtx);
        data.push_back(value);
    }
    
    bool pop(int& value) {
        lock_guard<mutex> lock(mtx);
        if (data.empty()) return false;
        value = data.back();
        data.pop_back();
        return true;
    }
    
    size_t size() const {
        lock_guard<mutex> lock(mtx);
        return data.size();
    }
};

void worker(Counter& counter, int iterations) {
    for (int i = 0; i < iterations; i++) {
        counter.increment();
    }
}

int main() {
    cout << "=== RAII for Mutex Locks ===" << endl;
    
    Counter counter;
    const int THREADS = 10;
    const int ITERATIONS = 100000;
    
    cout << "\n1. Thread-safe counter with RAII mutex:" << endl;
    vector<thread> threads;
    
    for (int i = 0; i < THREADS; i++) {
        threads.emplace_back(worker, ref(counter), ITERATIONS);
    }
    
    for (auto& t : threads) {
        t.join();
    }
    
    cout << "Final count: " << counter.getValue() << endl;
    cout << "Expected: " << (THREADS * ITERATIONS) << endl;
    
    cout << "\n2. Thread-safe queue with RAII mutex:" << endl;
    ThreadSafeQueue queue;
    
    thread producer([&queue]() {
        for (int i = 0; i < 100; i++) {
            queue.push(i);
            this_thread::sleep_for(chrono::milliseconds(1));
        }
    });
    
    thread consumer([&queue]() {
        int value;
        for (int i = 0; i < 100; i++) {
            if (queue.pop(value)) {
                cout << "Consumed: " << value << endl;
            }
            this_thread::sleep_for(chrono::milliseconds(1));
        }
    });
    
    producer.join();
    consumer.join();
    
    return 0;
}
```

---

## 4. **RAII for Database Connections**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <stdexcept>
using namespace std;

// Simulated database connection
class DatabaseConnection {
private:
    string connectionString;
    bool connected;
    
public:
    DatabaseConnection(const string& conn) : connectionString(conn), connected(false) {
        cout << "DatabaseConnection object created" << endl;
    }
    
    void connect() {
        if (!connected) {
            cout << "Connecting to " << connectionString << endl;
            connected = true;
        }
    }
    
    void disconnect() {
        if (connected) {
            cout << "Disconnecting from " << connectionString << endl;
            connected = false;
        }
    }
    
    void execute(const string& query) {
        if (!connected) {
            throw runtime_error("Not connected!");
        }
        cout << "Executing: " << query << endl;
    }
    
    bool isConnected() const { return connected; }
    
    ~DatabaseConnection() {
        if (connected) {
            disconnect();
        }
        cout << "DatabaseConnection destroyed" << endl;
    }
};

// RAII wrapper for database connection
class DBConnectionGuard {
private:
    DatabaseConnection& conn;
    
public:
    DBConnectionGuard(DatabaseConnection& c) : conn(c) {
        conn.connect();
        cout << "Connection guard acquired" << endl;
    }
    
    ~DBConnectionGuard() {
        conn.disconnect();
        cout << "Connection guard released" << endl;
    }
    
    DatabaseConnection& get() { return conn; }
};

class Transaction {
private:
    DatabaseConnection& conn;
    bool active;
    
public:
    Transaction(DatabaseConnection& c) : conn(c), active(false) {
        begin();
    }
    
    void begin() {
        if (!active) {
            conn.execute("BEGIN TRANSACTION");
            active = true;
            cout << "Transaction started" << endl;
        }
    }
    
    void commit() {
        if (active) {
            conn.execute("COMMIT");
            active = false;
            cout << "Transaction committed" << endl;
        }
    }
    
    void rollback() {
        if (active) {
            conn.execute("ROLLBACK");
            active = false;
            cout << "Transaction rolled back" << endl;
        }
    }
    
    ~Transaction() {
        if (active) {
            rollback();
        }
    }
};

void performDatabaseOperations() {
    DatabaseConnection db("postgresql://localhost/mydb");
    
    // RAII ensures connection is managed
    DBConnectionGuard guard(db);
    
    {
        Transaction tx(db);
        db.execute("UPDATE users SET active=1 WHERE id=1");
        db.execute("INSERT INTO logs VALUES('update')");
        tx.commit();
    }
    
    {
        Transaction tx(db);
        db.execute("UPDATE products SET price=price*1.1");
        // Exception will cause rollback
        throw runtime_error("Operation failed!");
        tx.commit();  // Never reached
    }
}

int main() {
    cout << "=== RAII for Database Connections ===" << endl;
    
    cout << "\n1. Normal operation with RAII:" << endl;
    try {
        DatabaseConnection db("postgresql://localhost/test");
        {
            DBConnectionGuard guard(db);
            db.execute("SELECT * FROM users");
        }  // Auto-disconnect
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    cout << "\n2. Transaction with RAII (auto-rollback on exception):" << endl;
    try {
        performDatabaseOperations();
    } catch (const exception& e) {
        cout << "Caught: " << e.what() << endl;
    }
    
    return 0;
}
```

---

## 5. **RAII for File Handles**

```cpp
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;

// C-style file handling with RAII
class CFile {
private:
    FILE* file;
    string filename;
    
public:
    CFile(const string& name, const string& mode) : filename(name), file(nullptr) {
        file = fopen(name.c_str(), mode.c_str());
        if (!file) {
            throw runtime_error("Cannot open file: " + name);
        }
        cout << "File opened: " << name << endl;
    }
    
    ~CFile() {
        if (file) {
            fclose(file);
            cout << "File closed: " << filename << endl;
        }
    }
    
    void write(const string& data) {
        if (file) {
            fprintf(file, "%s\n", data.c_str());
        }
    }
    
    string readLine() {
        char buffer[1024];
        if (file && fgets(buffer, sizeof(buffer), file)) {
            return string(buffer);
        }
        return "";
    }
    
    // Prevent copying
    CFile(const CFile&) = delete;
    CFile& operator=(const CFile&) = delete;
};

// C++ stream with RAII (already RAII)
class LogFile {
private:
    ofstream file;
    string name;
    
public:
    LogFile(const string& n) : name(n) {
        file.open(n, ios::app);
        if (!file.is_open()) {
            throw runtime_error("Cannot open log file");
        }
        cout << "Log file opened: " << name << endl;
    }
    
    ~LogFile() {
        if (file.is_open()) {
            file.close();
            cout << "Log file closed: " << name << endl;
        }
    }
    
    void log(const string& message) {
        if (file.is_open()) {
            file << message << endl;
        }
    }
    
    // Move constructor
    LogFile(LogFile&& other) noexcept : file(move(other.file)), name(move(other.name)) {}
};

class ConfigFile {
private:
    CFile file;
    
public:
    ConfigFile(const string& name) : file(name, "r") {}
    
    void loadConfig() {
        string line;
        while ((line = file.readLine()) != "") {
            cout << "Loading config: " << line;
        }
    }
};

void processFiles() {
    CFile data("data.txt", "w");
    data.write("First line");
    data.write("Second line");
    
    {
        LogFile log("app.log");
        log.log("Processing started");
        log.log("Data written");
    }  // Log file auto-closed
    
    ConfigFile config("config.txt");
    config.loadConfig();
    // File auto-closed
}

int main() {
    cout << "=== RAII for File Handles ===" << endl;
    
    cout << "\n1. Basic CFile RAII:" << endl;
    {
        CFile file("test.txt", "w");
        file.write("Hello, RAII!");
    }  // File auto-closed
    
    cout << "\n2. LogFile with RAII:" << endl;
    {
        LogFile log("app.log");
        log.log("Application started");
        log.log("User logged in");
        // Exception would still close file
    }
    
    cout << "\n3. Multiple files with RAII:" << endl;
    processFiles();
    
    cout << "\nAll files properly closed!" << endl;
    
    return 0;
}
```

---

## 6. **Practical Example: Resource Pool with RAII**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <mutex>
#include <stack>
#include <chrono>
#include <thread>
using namespace std;

class Connection {
private:
    int id;
    bool inUse;
    
public:
    Connection(int i) : id(i), inUse(false) {
        cout << "Connection " << id << " created" << endl;
    }
    
    ~Connection() {
        cout << "Connection " << id << " destroyed" << endl;
    }
    
    void connect() {
        inUse = true;
        cout << "Connection " << id << " connected" << endl;
    }
    
    void disconnect() {
        inUse = false;
        cout << "Connection " << id << " disconnected" << endl;
    }
    
    void execute(const string& query) {
        if (inUse) {
            cout << "Connection " << id << " executing: " << query << endl;
            this_thread::sleep_for(chrono::milliseconds(100));
        }
    }
    
    bool isInUse() const { return inUse; }
    int getId() const { return id; }
};

class ConnectionPool {
private:
    vector<unique_ptr<Connection>> connections;
    stack<Connection*> available;
    mutex poolMutex;
    int nextId;
    int maxSize;
    
public:
    ConnectionPool(int size) : nextId(1), maxSize(size) {
        for (int i = 0; i < size; i++) {
            auto conn = make_unique<Connection>(nextId++);
            available.push(conn.get());
            connections.push_back(move(conn));
        }
        cout << "Connection pool created with " << size << " connections" << endl;
    }
    
    class ConnectionGuard {
    private:
        ConnectionPool& pool;
        Connection* conn;
        
    public:
        ConnectionGuard(ConnectionPool& p) : pool(p), conn(nullptr) {
            conn = pool.acquire();
            if (conn) {
                conn->connect();
                cout << "Connection guard acquired: " << conn->getId() << endl;
            }
        }
        
        ~ConnectionGuard() {
            if (conn) {
                conn->disconnect();
                pool.release(conn);
                cout << "Connection guard released: " << conn->getId() << endl;
            }
        }
        
        Connection* operator->() { return conn; }
        Connection& operator*() { return *conn; }
        explicit operator bool() const { return conn != nullptr; }
        
        // Prevent copying
        ConnectionGuard(const ConnectionGuard&) = delete;
        ConnectionGuard& operator=(const ConnectionGuard&) = delete;
    };
    
private:
    Connection* acquire() {
        lock_guard<mutex> lock(poolMutex);
        if (available.empty()) {
            cout << "No connections available!" << endl;
            return nullptr;
        }
        Connection* conn = available.top();
        available.pop();
        return conn;
    }
    
    void release(Connection* conn) {
        lock_guard<mutex> lock(poolMutex);
        available.push(conn);
    }
    
public:
    ConnectionGuard getConnection() {
        return ConnectionGuard(*this);
    }
    
    size_t availableCount() const {
        lock_guard<mutex> lock(poolMutex);
        return available.size();
    }
};

int main() {
    cout << "=== Resource Pool with RAII ===" << endl;
    
    ConnectionPool pool(3);
    
    cout << "\n1. Using connections with RAII guard:" << endl;
    {
        auto guard = pool.getConnection();
        if (guard) {
            guard->execute("SELECT * FROM users");
        }
    }  // Connection automatically released
    
    cout << "\n2. Multiple concurrent connections:" << endl;
    {
        auto g1 = pool.getConnection();
        auto g2 = pool.getConnection();
        auto g3 = pool.getConnection();
        auto g4 = pool.getConnection();  // No connection available
        
        if (g1) g1->execute("Query 1");
        if (g2) g2->execute("Query 2");
        if (g3) g3->execute("Query 3");
    }  // All connections released
    
    cout << "\n3. Exception safety:" << endl;
    try {
        auto guard = pool.getConnection();
        if (guard) {
            guard->execute("Before exception");
            throw runtime_error("Simulated error");
            guard->execute("After exception");  // Never reached
        }
    } catch (const exception& e) {
        cout << "Caught: " << e.what() << endl;
    }
    // Connection still released!
    
    cout << "\nAvailable connections: " << pool.availableCount() << endl;
    
    return 0;
}
```

---

## 📊 RAII Summary

| Resource Type | RAII Class | Constructor | Destructor |
|---------------|------------|-------------|------------|
| **File** | `ifstream`, `ofstream` | Opens file | Closes file |
| **Memory** | `unique_ptr`, `shared_ptr` | Allocates | Deallocates |
| **Mutex** | `lock_guard`, `unique_lock` | Locks | Unlocks |
| **Connection** | Custom class | Acquires | Releases |

---

## ✅ Best Practices

1. **Always use RAII** for resource management
2. **Follow Rule of Zero** - use RAII classes instead of manual management
3. **Use smart pointers** for dynamic memory
4. **Use lock guards** for mutex synchronization
5. **Make destructors non-throwing** - essential for RAII
6. **Prevent copying** of RAII classes (or implement properly)

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Manual resource management** | Memory leaks | Use RAII classes |
| **Throwing destructors** | Program termination | Make destructors noexcept |
| **Copying RAII objects** | Double delete | Delete copy operations |
| **Resource leak in constructor** | Exception safety | Use RAII for members |

---

## ✅ Key Takeaways

1. **RAII** ties resource lifetime to object lifetime
2. **Constructor acquires**, destructor releases
3. **Exception-safe** - resources released during stack unwinding
4. **Core of C++ resource management**
5. **Smart pointers** implement RAII for memory
6. **Lock guards** implement RAII for mutexes
7. **File streams** implement RAII for files

---