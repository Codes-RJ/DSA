# Singleton Pattern in C++ - Complete Guide

## 📖 Overview

The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. It is one of the simplest and most widely used design patterns. Singleton is useful for managing shared resources like configuration settings, logging, thread pools, and database connections.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Single Instance** | Only one instance of the class can exist |
| **Global Access** | Provides a global access point to the instance |
| **Lazy Initialization** | Instance created only when first accessed |
| **Thread Safety** | Ensures single instance in multi-threaded environments |

---

## 1. **Basic Singleton (Naive Implementation)**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Singleton {
private:
    static Singleton* instance;
    string data;
    
    // Private constructor - prevents instantiation
    Singleton() : data("Default Data") {
        cout << "Singleton created" << endl;
    }
    
    // Delete copy constructor and assignment
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;
    
public:
    static Singleton* getInstance() {
        if (instance == nullptr) {
            instance = new Singleton();
        }
        return instance;
    }
    
    void setData(const string& d) {
        data = d;
    }
    
    string getData() const {
        return data;
    }
    
    static void destroy() {
        delete instance;
        instance = nullptr;
    }
};

Singleton* Singleton::instance = nullptr;

int main() {
    cout << "=== Basic Singleton (Naive Implementation) ===" << endl;
    
    // Singleton* s1 = new Singleton();  // Error! Constructor is private
    
    Singleton* s1 = Singleton::getInstance();
    Singleton* s2 = Singleton::getInstance();
    
    cout << "\nBoth pointers point to same instance:" << endl;
    cout << "s1 address: " << s1 << endl;
    cout << "s2 address: " << s2 << endl;
    cout << "Same instance? " << (s1 == s2 ? "Yes" : "No") << endl;
    
    s1->setData("Modified Data");
    cout << "\nAfter modification:" << endl;
    cout << "s1 data: " << s1->getData() << endl;
    cout << "s2 data: " << s2->getData() << endl;
    
    Singleton::destroy();
    
    return 0;
}
```

**Output:**
```
=== Basic Singleton (Naive Implementation) ===
Singleton created

Both pointers point to same instance:
s1 address: 0x...
s2 address: 0x...
Same instance? Yes

After modification:
s1 data: Modified Data
s2 data: Modified Data
```

---

## 2. **Thread-Safe Singleton (Mutex)**

```cpp
#include <iostream>
#include <string>
#include <thread>
#include <vector>
#include <mutex>
using namespace std;

class ThreadSafeSingleton {
private:
    static ThreadSafeSingleton* instance;
    static mutex mtx;
    string data;
    
    ThreadSafeSingleton() : data("ThreadSafe Data") {
        cout << "ThreadSafeSingleton created" << endl;
    }
    
    ThreadSafeSingleton(const ThreadSafeSingleton&) = delete;
    ThreadSafeSingleton& operator=(const ThreadSafeSingleton&) = delete;
    
public:
    static ThreadSafeSingleton* getInstance() {
        // Double-checked locking
        if (instance == nullptr) {
            lock_guard<mutex> lock(mtx);
            if (instance == nullptr) {
                instance = new ThreadSafeSingleton();
            }
        }
        return instance;
    }
    
    void setData(const string& d) {
        lock_guard<mutex> lock(mtx);
        data = d;
    }
    
    string getData() const {
        lock_guard<mutex> lock(mtx);
        return data;
    }
    
    static void destroy() {
        lock_guard<mutex> lock(mtx);
        delete instance;
        instance = nullptr;
    }
};

ThreadSafeSingleton* ThreadSafeSingleton::instance = nullptr;
mutex ThreadSafeSingleton::mtx;

void worker(int id) {
    ThreadSafeSingleton* s = ThreadSafeSingleton::getInstance();
    cout << "Thread " << id << " got instance: " << s << endl;
    s->setData("Thread " + to_string(id) + " data");
    cout << "Thread " << id << " data: " << s->getData() << endl;
}

int main() {
    cout << "=== Thread-Safe Singleton (Mutex) ===" << endl;
    
    cout << "\n1. Single-threaded access:" << endl;
    ThreadSafeSingleton* s1 = ThreadSafeSingleton::getInstance();
    ThreadSafeSingleton* s2 = ThreadSafeSingleton::getInstance();
    cout << "Same instance? " << (s1 == s2 ? "Yes" : "No") << endl;
    
    cout << "\n2. Multi-threaded access:" << endl;
    vector<thread> threads;
    for (int i = 0; i < 5; i++) {
        threads.emplace_back(worker, i);
    }
    
    for (auto& t : threads) {
        t.join();
    }
    
    ThreadSafeSingleton::destroy();
    
    return 0;
}
```

---

## 3. **Meyers Singleton (C++11 Static Local)**

```cpp
#include <iostream>
#include <string>
#include <thread>
#include <vector>
using namespace std;

class MeyersSingleton {
private:
    string data;
    
    // Private constructor
    MeyersSingleton() : data("Meyers Singleton Data") {
        cout << "MeyersSingleton created (thread-safe)" << endl;
    }
    
    // Delete copy operations
    MeyersSingleton(const MeyersSingleton&) = delete;
    MeyersSingleton& operator=(const MeyersSingleton&) = delete;
    
public:
    static MeyersSingleton& getInstance() {
        static MeyersSingleton instance;  // Guaranteed to be initialized once
        return instance;
    }
    
    void setData(const string& d) {
        data = d;
    }
    
    string getData() const {
        return data;
    }
};

void worker(int id) {
    MeyersSingleton& s = MeyersSingleton::getInstance();
    cout << "Thread " << id << " got instance address: " << &s << endl;
    s.setData("Thread " + to_string(id) + " data");
    cout << "Thread " << id << " data: " << s.getData() << endl;
}

int main() {
    cout << "=== Meyers Singleton (C++11 Static Local) ===" << endl;
    
    cout << "\n1. Single-threaded access:" << endl;
    MeyersSingleton& s1 = MeyersSingleton::getInstance();
    MeyersSingleton& s2 = MeyersSingleton::getInstance();
    cout << "Same instance? " << (&s1 == &s2 ? "Yes" : "No") << endl;
    cout << "Data: " << s1.getData() << endl;
    
    s1.setData("Modified Data");
    cout << "After modification: " << s2.getData() << endl;
    
    cout << "\n2. Multi-threaded access (thread-safe by default):" << endl;
    vector<thread> threads;
    for (int i = 0; i < 5; i++) {
        threads.emplace_back(worker, i);
    }
    
    for (auto& t : threads) {
        t.join();
    }
    
    // No need to destroy - static variable destroyed at program exit
    
    return 0;
}
```

---

## 4. **Singleton with Template**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <mutex>
using namespace std;

template<typename T>
class Singleton {
private:
    static unique_ptr<T> instance;
    static mutex mtx;
    
protected:
    Singleton() = default;
    
public:
    virtual ~Singleton() = default;
    
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;
    
    static T& getInstance() {
        if (!instance) {
            lock_guard<mutex> lock(mtx);
            if (!instance) {
                instance.reset(new T());
            }
        }
        return *instance;
    }
    
    static void destroy() {
        lock_guard<mutex> lock(mtx);
        instance.reset();
    }
};

template<typename T>
unique_ptr<T> Singleton<T>::instance = nullptr;

template<typename T>
mutex Singleton<T>::mtx;

// Concrete singleton classes
class Logger : public Singleton<Logger> {
private:
    int logCount;
    
    Logger() : logCount(0) {
        cout << "Logger created" << endl;
    }
    
    friend class Singleton<Logger>;
    
public:
    void log(const string& message) {
        logCount++;
        cout << "[LOG " << logCount << "] " << message << endl;
    }
};

class Configuration : public Singleton<Configuration> {
private:
    string serverAddress;
    int port;
    
    Configuration() : serverAddress("localhost"), port(8080) {
        cout << "Configuration created" << endl;
    }
    
    friend class Singleton<Configuration>;
    
public:
    void setServer(const string& addr, int p) {
        serverAddress = addr;
        port = p;
    }
    
    void display() const {
        cout << "Server: " << serverAddress << ":" << port << endl;
    }
};

int main() {
    cout << "=== Singleton with Template ===" << endl;
    
    cout << "\n1. Logger singleton:" << endl;
    Logger& logger1 = Logger::getInstance();
    Logger& logger2 = Logger::getInstance();
    
    logger1.log("Application started");
    logger2.log("User logged in");
    logger1.log("Processing data");
    
    cout << "Same instance? " << (&logger1 == &logger2 ? "Yes" : "No") << endl;
    
    cout << "\n2. Configuration singleton:" << endl;
    Configuration& config1 = Configuration::getInstance();
    Configuration& config2 = Configuration::getInstance();
    
    config1.display();
    config2.setServer("production.example.com", 443);
    config1.display();
    
    cout << "Same instance? " << (&config1 == &config2 ? "Yes" : "No") << endl;
    
    return 0;
}
```

---

## 5. **Practical Example: Configuration Manager**

```cpp
#include <iostream>
#include <string>
#include <map>
#include <fstream>
#include <sstream>
#include <mutex>
using namespace std;

class ConfigManager {
private:
    static ConfigManager* instance;
    static mutex mtx;
    map<string, string> config;
    string filename;
    
    ConfigManager() : filename("config.ini") {
        loadConfig();
        cout << "ConfigManager initialized" << endl;
    }
    
    void loadConfig() {
        // Simulate loading configuration
        config["server"] = "localhost";
        config["port"] = "8080";
        config["database"] = "mydb";
        config["user"] = "admin";
        config["password"] = "secret";
        config["debug"] = "true";
        cout << "Configuration loaded" << endl;
    }
    
    ConfigManager(const ConfigManager&) = delete;
    ConfigManager& operator=(const ConfigManager&) = delete;
    
public:
    static ConfigManager* getInstance() {
        if (instance == nullptr) {
            lock_guard<mutex> lock(mtx);
            if (instance == nullptr) {
                instance = new ConfigManager();
            }
        }
        return instance;
    }
    
    string get(const string& key, const string& defaultValue = "") {
        lock_guard<mutex> lock(mtx);
        auto it = config.find(key);
        if (it != config.end()) {
            return it->second;
        }
        return defaultValue;
    }
    
    void set(const string& key, const string& value) {
        lock_guard<mutex> lock(mtx);
        config[key] = value;
        cout << "Config updated: " << key << " = " << value << endl;
    }
    
    int getInt(const string& key, int defaultValue = 0) {
        string val = get(key);
        if (val.empty()) return defaultValue;
        return stoi(val);
    }
    
    bool getBool(const string& key, bool defaultValue = false) {
        string val = get(key);
        if (val.empty()) return defaultValue;
        return (val == "true" || val == "1" || val == "yes");
    }
    
    void save() {
        lock_guard<mutex> lock(mtx);
        cout << "Saving configuration to " << filename << endl;
        // In real implementation, would write to file
        for (const auto& [key, value] : config) {
            cout << "  " << key << "=" << value << endl;
        }
    }
    
    static void destroy() {
        lock_guard<mutex> lock(mtx);
        delete instance;
        instance = nullptr;
    }
};

ConfigManager* ConfigManager::instance = nullptr;
mutex ConfigManager::mtx;

class Database {
public:
    void connect() {
        ConfigManager* config = ConfigManager::getInstance();
        string server = config->get("server");
        int port = config->getInt("port");
        string db = config->get("database");
        string user = config->get("user");
        string password = config->get("password");
        
        cout << "Connecting to " << server << ":" << port 
             << "/" << db << " as " << user << endl;
    }
};

class Server {
public:
    void start() {
        ConfigManager* config = ConfigManager::getInstance();
        string server = config->get("server");
        int port = config->getInt("port");
        bool debug = config->getBool("debug");
        
        cout << "Starting server on " << server << ":" << port << endl;
        if (debug) {
            cout << "Debug mode enabled" << endl;
        }
    }
};

int main() {
    cout << "=== Configuration Manager Singleton ===" << endl;
    
    ConfigManager* config = ConfigManager::getInstance();
    
    cout << "\n1. Reading configuration:" << endl;
    cout << "Server: " << config->get("server") << endl;
    cout << "Port: " << config->getInt("port") << endl;
    cout << "Debug: " << (config->getBool("debug") ? "true" : "false") << endl;
    cout << "Unknown key: " << config->get("unknown", "default") << endl;
    
    cout << "\n2. Updating configuration:" << endl;
    config->set("port", "9090");
    config->set("debug", "false");
    
    cout << "\n3. Using configuration in other classes:" << endl;
    Database db;
    db.connect();
    
    Server server;
    server.start();
    
    cout << "\n4. Saving configuration:" << endl;
    config->save();
    
    ConfigManager::destroy();
    
    return 0;
}
```

---

## 6. **Singleton with Lazy Initialization and RAII**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <mutex>
using namespace std;

class DatabaseConnection {
private:
    string connectionString;
    bool connected;
    
    DatabaseConnection() : connectionString(""), connected(false) {
        cout << "DatabaseConnection created" << endl;
    }
    
    DatabaseConnection(const DatabaseConnection&) = delete;
    DatabaseConnection& operator=(const DatabaseConnection&) = delete;
    
public:
    static DatabaseConnection& getInstance() {
        static DatabaseConnection instance;
        return instance;
    }
    
    void connect(const string& connStr) {
        connectionString = connStr;
        connected = true;
        cout << "Connected to " << connectionString << endl;
    }
    
    void disconnect() {
        if (connected) {
            connected = false;
            cout << "Disconnected from " << connectionString << endl;
        }
    }
    
    void query(const string& sql) {
        if (connected) {
            cout << "Executing: " << sql << " on " << connectionString << endl;
        } else {
            cout << "Not connected!" << endl;
        }
    }
    
    ~DatabaseConnection() {
        disconnect();
        cout << "DatabaseConnection destroyed" << endl;
    }
};

class Logger {
private:
    string logFile;
    int logLevel;
    
    Logger() : logFile("app.log"), logLevel(1) {
        cout << "Logger created" << endl;
    }
    
    ~Logger() {
        cout << "Logger destroyed" << endl;
    }
    
public:
    static Logger& getInstance() {
        static Logger instance;
        return instance;
    }
    
    void setLogLevel(int level) {
        logLevel = level;
    }
    
    void log(const string& message, int level = 1) {
        if (level >= logLevel) {
            cout << "[LOG] " << message << endl;
        }
    }
};

class Application {
public:
    void run() {
        // Get singletons
        DatabaseConnection& db = DatabaseConnection::getInstance();
        Logger& logger = Logger::getInstance();
        
        logger.log("Application starting");
        
        db.connect("postgresql://localhost/mydb");
        db.query("SELECT * FROM users");
        db.query("INSERT INTO logs VALUES('startup')");
        
        logger.log("Application running");
        
        db.disconnect();
        logger.log("Application shutting down");
    }
};

int main() {
    cout << "=== Singleton with Lazy Initialization and RAII ===" << endl;
    
    cout << "\n1. Singletons are created on first use:" << endl;
    // No instances created yet
    
    cout << "\n2. Running application (creates singletons):" << endl;
    Application app;
    app.run();
    
    cout << "\n3. Singletons still exist after app.run():" << endl;
    DatabaseConnection::getInstance().query("SELECT * FROM cache");
    Logger::getInstance().log("Post-application log", 1);
    
    cout << "\n4. Singletons destroyed at program exit" << endl;
    
    return 0;
}
```

---

## 📊 Singleton Pattern Summary

| Implementation | Thread Safety | Lazy Initialization | Complexity | Use Case |
|----------------|---------------|---------------------|------------|----------|
| **Naive** | No | Yes | Low | Single-threaded |
| **Mutex (Double-checked)** | Yes | Yes | Medium | Multi-threaded |
| **Meyers (Static Local)** | Yes | Yes | Low | C++11 and later |
| **Template** | Yes | Yes | Medium | Multiple singletons |

---

## ✅ Best Practices

1. **Prefer Meyers Singleton** for C++11 and later
2. **Make constructor private** to prevent instantiation
3. **Delete copy operations** to prevent copying
4. **Use lazy initialization** to avoid unnecessary creation
5. **Consider thread safety** in multi-threaded environments
6. **Avoid global state** when possible - singletons can make testing difficult

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Not thread-safe** | Multiple instances in threads | Use thread-safe implementation |
| **Global state issues** | Hard to test | Consider dependency injection |
| **Circular dependencies** | Deadlock | Avoid singletons referencing each other |
| **Memory leak** | Never destroyed | Use Meyers Singleton |
| **Hidden dependencies** | Hard to understand | Document singleton usage |

---

## ✅ Key Takeaways

1. **Singleton** ensures only one instance of a class
2. **Global access point** provides consistent interface
3. **Lazy initialization** creates instance on first use
4. **Meyers Singleton** is the preferred C++11 implementation
5. **Thread safety** is critical for multi-threaded environments
6. **Use sparingly** - singletons can make code harder to test

---