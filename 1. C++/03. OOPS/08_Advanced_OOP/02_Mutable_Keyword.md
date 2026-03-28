# 08_Advanced_OOP/02_Mutable_Keyword.md

# Mutable Keyword in C++ - Complete Guide

## 📖 Overview

The `mutable` keyword in C++ allows a data member of a const object to be modified. It is used when a member variable needs to be changed even in const member functions. Common use cases include caching, lazy initialization, logging, reference counting, and mutex locks.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **mutable** | Allows modification of member in const functions |
| **Const Correctness** | `mutable` provides exceptions to const correctness |
| **Use Cases** | Caching, logging, reference counting, mutexes |
| **Philosophy** | Logical constness vs physical constness |

---

## 1. **Basic Mutable Usage**

```cpp
#include <iostream>
#include <string>
#include <chrono>
#include <thread>
using namespace std;

class Logger {
private:
    string name;
    mutable int logCount;      // Can be modified in const methods
    mutable chrono::steady_clock::time_point lastLogTime;
    
public:
    Logger(string n) : name(n), logCount(0) {}
    
    void log(const string& message) const {
        // Can modify mutable members even in const method
        logCount++;
        lastLogTime = chrono::steady_clock::now();
        
        cout << "[" << name << "] " << message 
             << " (log #" << logCount << ")" << endl;
    }
    
    int getLogCount() const { return logCount; }
};

class ExpensiveCalculator {
private:
    int value;
    mutable double cachedResult;
    mutable bool cacheValid;
    mutable int computeCount;
    
    double expensiveComputation() const {
        // Simulate expensive calculation
        this_thread::sleep_for(chrono::milliseconds(100));
        return value * value * 3.14159;
    }
    
public:
    ExpensiveCalculator(int v) : value(v), cacheValid(false), computeCount(0) {}
    
    double getResult() const {
        computeCount++;
        if (!cacheValid) {
            cachedResult = expensiveComputation();
            cacheValid = true;
        }
        return cachedResult;
    }
    
    void setValue(int v) {
        value = v;
        cacheValid = false;  // Invalidate cache
    }
    
    int getComputeCount() const { return computeCount; }
};

int main() {
    cout << "=== Basic Mutable Usage ===" << endl;
    
    cout << "\n1. Logger with mutable counter:" << endl;
    const Logger logger("System");  // Const object
    
    logger.log("Application started");
    logger.log("User logged in");
    logger.log("Processing data");
    cout << "Total logs: " << logger.getLogCount() << endl;
    
    cout << "\n2. ExpensiveCalculator with mutable cache:" << endl;
    const ExpensiveCalculator calc(10);  // Const object
    
    cout << "First calculation: " << calc.getResult() << endl;
    cout << "Second calculation: " << calc.getResult() << endl;
    cout << "Third calculation: " << calc.getResult() << endl;
    cout << "Compute count: " << calc.getComputeCount() << endl;
    
    return 0;
}
```

**Output:**
```
=== Basic Mutable Usage ===

1. Logger with mutable counter:
[System] Application started (log #1)
[System] User logged in (log #2)
[System] Processing data (log #3)
Total logs: 3

2. ExpensiveCalculator with mutable cache:
First calculation: 314.159
Second calculation: 314.159
Third calculation: 314.159
Compute count: 1
```

---

## 2. **Lazy Initialization with Mutable**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
using namespace std;

class LargeData {
private:
    string filename;
    mutable vector<string> data;
    mutable bool loaded;
    
    void loadData() const {
        if (!loaded) {
            cout << "Loading data from " << filename << "..." << endl;
            ifstream file(filename);
            string line;
            while (getline(file, line)) {
                const_cast<vector<string>&>(data).push_back(line);
            }
            loaded = true;
            cout << "Loaded " << data.size() << " records" << endl;
        }
    }
    
public:
    LargeData(string fname) : filename(fname), loaded(false) {}
    
    size_t size() const {
        loadData();
        return data.size();
    }
    
    string getLine(size_t index) const {
        loadData();
        if (index < data.size()) {
            return data[index];
        }
        return "";
    }
    
    vector<string> search(const string& keyword) const {
        loadData();
        vector<string> results;
        for (const auto& line : data) {
            if (line.find(keyword) != string::npos) {
                results.push_back(line);
            }
        }
        return results;
    }
};

class Connection {
private:
    string host;
    int port;
    mutable bool connected;
    mutable string connectionId;
    
    void establishConnection() const {
        if (!connected) {
            cout << "Establishing connection to " << host << ":" << port << endl;
            connectionId = "CONN-" + to_string(rand() % 10000);
            connected = true;
        }
    }
    
public:
    Connection(string h, int p) : host(h), port(p), connected(false) {}
    
    void send(const string& data) const {
        establishConnection();
        cout << "[" << connectionId << "] Sending: " << data << endl;
    }
    
    string receive() const {
        establishConnection();
        return "Data from " + host;
    }
    
    bool isConnected() const { return connected; }
};

int main() {
    cout << "=== Lazy Initialization with Mutable ===" << endl;
    
    // Create a test file
    ofstream file("test.txt");
    file << "Line 1: Hello World\n";
    file << "Line 2: C++ Programming\n";
    file << "Line 3: Mutable Keyword\n";
    file << "Line 4: Lazy Loading\n";
    file << "Line 5: Hello Again\n";
    file.close();
    
    cout << "\n1. LargeData with lazy loading:" << endl;
    const LargeData data("test.txt");
    
    cout << "Data not loaded yet" << endl;
    cout << "Size: " << data.size() << endl;  // Triggers load
    cout << "Line 2: " << data.getLine(1) << endl;
    
    cout << "\n2. Searching:" << endl;
    auto results = data.search("Hello");
    cout << "Found " << results.size() << " lines containing 'Hello':" << endl;
    for (const auto& line : results) {
        cout << "  " << line << endl;
    }
    
    cout << "\n3. Connection with lazy connection:" << endl;
    const Connection conn("localhost", 8080);
    
    cout << "Connected? " << (conn.isConnected() ? "Yes" : "No") << endl;
    conn.send("Hello Server");  // Triggers connection
    cout << "Connected? " << (conn.isConnected() ? "Yes" : "No") << endl;
    conn.send("Another message");
    
    return 0;
}
```

---

## 3. **Caching with Mutable**

```cpp
#include <iostream>
#include <string>
#include <map>
#include <chrono>
#include <cmath>
using namespace std;

class MathFunctions {
private:
    mutable map<double, double> sqrtCache;
    mutable map<double, double> logCache;
    
public:
    double sqrt(double x) const {
        auto it = sqrtCache.find(x);
        if (it != sqrtCache.end()) {
            cout << "sqrt(" << x << ") - cache hit" << endl;
            return it->second;
        }
        
        cout << "sqrt(" << x << ") - computing" << endl;
        double result = std::sqrt(x);
        sqrtCache[x] = result;
        return result;
    }
    
    double log(double x) const {
        auto it = logCache.find(x);
        if (it != logCache.end()) {
            cout << "log(" << x << ") - cache hit" << endl;
            return it->second;
        }
        
        cout << "log(" << x << ") - computing" << endl;
        double result = std::log(x);
        logCache[x] = result;
        return result;
    }
    
    void clearCache() {
        sqrtCache.clear();
        logCache.clear();
        cout << "Cache cleared" << endl;
    }
};

class DatabaseQuery {
private:
    string connection;
    mutable map<string, vector<string>> queryCache;
    mutable int cacheHits;
    mutable int cacheMisses;
    
    vector<string> executeQuery(const string& sql) const {
        // Simulate database query
        cout << "Executing query: " << sql << endl;
        return {"result1", "result2", "result3"};
    }
    
public:
    DatabaseQuery(string conn) : connection(conn), cacheHits(0), cacheMisses(0) {}
    
    vector<string> query(const string& sql) const {
        auto it = queryCache.find(sql);
        if (it != queryCache.end()) {
            cacheHits++;
            cout << "Cache hit for: " << sql << endl;
            return it->second;
        }
        
        cacheMisses++;
        cout << "Cache miss for: " << sql << endl;
        vector<string> results = executeQuery(sql);
        queryCache[sql] = results;
        return results;
    }
    
    void printStats() const {
        cout << "Cache hits: " << cacheHits << ", Misses: " << cacheMisses 
             << ", Hit rate: " << (cacheHits * 100.0 / (cacheHits + cacheMisses)) << "%" << endl;
    }
};

int main() {
    cout << "=== Caching with Mutable ===" << endl;
    
    cout << "\n1. MathFunctions with caching:" << endl;
    const MathFunctions math;
    
    for (int i = 0; i < 3; i++) {
        cout << math.sqrt(2.0) << endl;
        cout << math.sqrt(3.0) << endl;
        cout << math.log(2.71828) << endl;
    }
    
    cout << "\n2. DatabaseQuery with caching:" << endl;
    const DatabaseQuery db("postgresql://localhost/db");
    
    db.query("SELECT * FROM users");
    db.query("SELECT * FROM products");
    db.query("SELECT * FROM users");  // Cache hit
    db.query("SELECT * FROM orders");
    db.query("SELECT * FROM products"); // Cache hit
    
    db.printStats();
    
    return 0;
}
```

---

## 4. **Reference Counting with Mutable**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

class SharedData {
private:
    int* data;
    mutable int* refCount;
    
public:
    SharedData(int value) {
        data = new int(value);
        refCount = new int(1);
        cout << "SharedData created with value " << *data << ", refCount = 1" << endl;
    }
    
    // Copy constructor - increases reference count
    SharedData(const SharedData& other) : data(other.data), refCount(other.refCount) {
        (*refCount)++;
        cout << "SharedData copied, refCount = " << *refCount << endl;
    }
    
    // Destructor - decreases reference count
    ~SharedData() {
        (*refCount)--;
        cout << "SharedData destructor, refCount = " << *refCount << endl;
        
        if (*refCount == 0) {
            cout << "Deleting data and refCount" << endl;
            delete data;
            delete refCount;
        }
    }
    
    int getValue() const { return *data; }
    
    void setValue(int value) const {
        // If we're the only reference, modify directly
        if (*refCount == 1) {
            *data = value;
        } else {
            // Copy on write - create new copy
            cout << "Copy on write: creating new copy" << endl;
            (*refCount)--;
            data = new int(value);
            refCount = new int(1);
        }
    }
};

class StringBuffer {
private:
    mutable char* buffer;
    mutable size_t length;
    mutable int* refCount;
    
public:
    StringBuffer(const char* str) {
        length = strlen(str);
        buffer = new char[length + 1];
        strcpy(buffer, str);
        refCount = new int(1);
    }
    
    StringBuffer(const StringBuffer& other) 
        : buffer(other.buffer), length(other.length), refCount(other.refCount) {
        (*refCount)++;
    }
    
    ~StringBuffer() {
        (*refCount)--;
        if (*refCount == 0) {
            delete[] buffer;
            delete refCount;
        }
    }
    
    size_t getLength() const { return length; }
    
    const char* c_str() const { return buffer; }
    
    void setChar(size_t index, char c) const {
        if (*refCount > 1) {
            // Copy on write
            (*refCount)--;
            char* newBuffer = new char[length + 1];
            strcpy(newBuffer, buffer);
            buffer = newBuffer;
            refCount = new int(1);
        }
        
        if (index < length) {
            buffer[index] = c;
        }
    }
    
    void display() const {
        cout << buffer << " (refCount=" << *refCount << ")" << endl;
    }
};

int main() {
    cout << "=== Reference Counting with Mutable ===" << endl;
    
    cout << "\n1. SharedData with reference counting:" << endl;
    SharedData sd1(42);
    {
        SharedData sd2 = sd1;  // Copy - refCount becomes 2
        SharedData sd3 = sd2;  // Copy - refCount becomes 3
        
        cout << "sd1 value: " << sd1.getValue() << endl;
        cout << "sd2 value: " << sd2.getValue() << endl;
        cout << "sd3 value: " << sd3.getValue() << endl;
        
        sd2.setValue(100);  // Copy on write
        cout << "After sd2.setValue(100):" << endl;
        cout << "sd1 value: " << sd1.getValue() << endl;
        cout << "sd2 value: " << sd2.getValue() << endl;
        cout << "sd3 value: " << sd3.getValue() << endl;
    }  // sd2 and sd3 destroyed
    
    cout << "\n2. StringBuffer with copy-on-write:" << endl;
    StringBuffer sb1("Hello");
    StringBuffer sb2 = sb1;
    StringBuffer sb3 = sb2;
    
    cout << "sb1: "; sb1.display();
    cout << "sb2: "; sb2.display();
    cout << "sb3: "; sb3.display();
    
    sb2.setChar(0, 'J');  // Copy on write
    cout << "After sb2.setChar(0, 'J'):" << endl;
    cout << "sb1: "; sb1.display();
    cout << "sb2: "; sb2.display();
    cout << "sb3: "; sb3.display();
    
    return 0;
}
```

---

## 5. **Mutex with Mutable (Thread Safety)**

```cpp
#include <iostream>
#include <string>
#include <thread>
#include <vector>
#include <mutex>
#include <chrono>
using namespace std;

class ThreadSafeCounter {
private:
    mutable mutex mtx;
    int count;
    
public:
    ThreadSafeCounter() : count(0) {}
    
    void increment() const {
        lock_guard<mutex> lock(mtx);
        count++;
    }
    
    int getValue() const {
        lock_guard<mutex> lock(mtx);
        return count;
    }
};

class ThreadSafeCache {
private:
    mutable mutex cacheMutex;
    mutable map<string, string> cache;
    mutable map<string, chrono::steady_clock::time_point> timestamps;
    mutable int hits;
    mutable int misses;
    
    const chrono::seconds TTL{30};
    
public:
    ThreadSafeCache() : hits(0), misses(0) {}
    
    void put(const string& key, const string& value) const {
        lock_guard<mutex> lock(cacheMutex);
        cache[key] = value;
        timestamps[key] = chrono::steady_clock::now();
    }
    
    bool get(const string& key, string& value) const {
        lock_guard<mutex> lock(cacheMutex);
        
        auto it = cache.find(key);
        if (it != cache.end()) {
            auto age = chrono::steady_clock::now() - timestamps[key];
            if (age < TTL) {
                hits++;
                value = it->second;
                return true;
            } else {
                // Expired
                cache.erase(it);
                timestamps.erase(key);
            }
        }
        
        misses++;
        return false;
    }
    
    void stats() const {
        lock_guard<mutex> lock(cacheMutex);
        cout << "Cache hits: " << hits << ", misses: " << misses 
             << ", size: " << cache.size() << endl;
    }
};

class Logger {
private:
    mutable mutex logMutex;
    mutable vector<string> logEntries;
    mutable int logLevel;
    
public:
    Logger(int level = 1) : logLevel(level) {}
    
    void log(const string& message, int level = 1) const {
        if (level >= logLevel) {
            lock_guard<mutex> lock(logMutex);
            logEntries.push_back(message);
            cout << "[LOG] " << message << endl;
        }
    }
    
    vector<string> getLogs() const {
        lock_guard<mutex> lock(logMutex);
        return logEntries;
    }
    
    void setLogLevel(int level) {
        lock_guard<mutex> lock(logMutex);
        logLevel = level;
    }
};

void worker(const ThreadSafeCounter& counter, int id) {
    for (int i = 0; i < 1000; i++) {
        counter.increment();
    }
    cout << "Worker " << id << " finished" << endl;
}

int main() {
    cout << "=== Mutex with Mutable (Thread Safety) ===" << endl;
    
    cout << "\n1. ThreadSafeCounter:" << endl;
    ThreadSafeCounter counter;
    
    vector<thread> threads;
    for (int i = 0; i < 10; i++) {
        threads.emplace_back(worker, ref(counter), i);
    }
    
    for (auto& t : threads) {
        t.join();
    }
    
    cout << "Final count: " << counter.getValue() << endl;
    
    cout << "\n2. ThreadSafeCache:" << endl;
    const ThreadSafeCache cache;
    
    cache.put("key1", "value1");
    cache.put("key2", "value2");
    
    string value;
    if (cache.get("key1", value)) {
        cout << "Found: " << value << endl;
    }
    
    cache.stats();
    
    cout << "\n3. Logger with mutable mutex:" << endl;
    const Logger logger(1);
    
    logger.log("Info message");
    logger.log("Debug message", 2);
    logger.log("Error message", 0);
    
    auto logs = logger.getLogs();
    cout << "Total logs: " << logs.size() << endl;
    
    return 0;
}
```

---

## 📊 Mutable Keyword Summary

| Use Case | Description | Example |
|----------|-------------|---------|
| **Caching** | Store computed results | `mutable double cachedResult` |
| **Logging** | Count operations in const methods | `mutable int logCount` |
| **Lazy Initialization** | Load on demand | `mutable bool loaded` |
| **Reference Counting** | Track references | `mutable int* refCount` |
| **Mutex** | Thread safety in const methods | `mutable mutex mtx` |

---

## ✅ Best Practices

1. **Use mutable for caching** - Logical constness
2. **Use mutable for logging** - Doesn't affect logical state
3. **Use mutable for lazy initialization** - Performance optimization
4. **Use mutable for mutexes** - Thread safety in const methods
5. **Avoid mutable for regular data** - Should be const if logically const
6. **Document why mutable is used** - Explain logical vs physical constness

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Overusing mutable** | Breaks const correctness | Only use when truly needed |
| **Mutable for regular data** | Confusing semantics | Reconsider design |
| **Not documenting** | Maintenance issues | Comment mutable usage |
| **Thread safety** | Data races | Combine with mutex |

---

## ✅ Key Takeaways

1. **mutable** allows modification in const member functions
2. **Logical constness**: Object appears unchanged externally
3. **Physical constness**: Object's memory doesn't change
4. **Use for**: Caching, logging, lazy initialization, reference counting
5. **Use for**: Mutex locks in const methods
6. **Not for**: Regular data that should be const
7. **Document** why mutable is used

---