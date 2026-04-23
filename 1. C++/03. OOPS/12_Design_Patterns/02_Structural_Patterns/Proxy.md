# Proxy Pattern in C++ - Complete Guide

## 📖 Overview

The Proxy pattern provides a surrogate or placeholder for another object to control access to it. Proxies are used for lazy initialization, access control, logging, caching, and many other cross-cutting concerns. The proxy implements the same interface as the real object, allowing it to be used interchangeably.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Subject** | Interface common to RealSubject and Proxy |
| **RealSubject** | The actual object being represented |
| **Proxy** | Controls access to the RealSubject |
| **Virtual Proxy** | Defers object creation until needed |
| **Protection Proxy** | Controls access permissions |
| **Cache Proxy** | Caches results of expensive operations |

---

## 1. **Basic Virtual Proxy (Lazy Initialization)**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// Subject interface
class Image {
public:
    virtual void display() = 0;
    virtual ~Image() = default;
};

// RealSubject
class RealImage : public Image {
private:
    string filename;
    
    void loadFromDisk() {
        cout << "Loading image from disk: " << filename << endl;
        // Simulate expensive loading operation
    }
    
public:
    RealImage(const string& file) : filename(file) {
        loadFromDisk();
    }
    
    void display() override {
        cout << "Displaying image: " << filename << endl;
    }
};

// Virtual Proxy (Lazy loading)
class ProxyImage : public Image {
private:
    string filename;
    unique_ptr<RealImage> realImage;
    
public:
    ProxyImage(const string& file) : filename(file), realImage(nullptr) {}
    
    void display() override {
        if (!realImage) {
            realImage = make_unique<RealImage>(filename);
        }
        realImage->display();
    }
};

int main() {
    cout << "=== Basic Virtual Proxy (Lazy Initialization) ===" << endl;
    
    cout << "\nCreating proxy image (not loaded yet):" << endl;
    ProxyImage image1("photo1.jpg");
    
    cout << "\nFirst display (loads image):" << endl;
    image1.display();
    
    cout << "\nSecond display (already loaded):" << endl;
    image1.display();
    
    return 0;
}
```

**Output:**
```
=== Basic Virtual Proxy (Lazy Initialization) ===

Creating proxy image (not loaded yet):

First display (loads image):
Loading image from disk: photo1.jpg
Displaying image: photo1.jpg

Second display (already loaded):
Displaying image: photo1.jpg
```

---

## 2. **Protection Proxy (Access Control)**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <map>
using namespace std;

// Subject interface
class Document {
public:
    virtual void view() = 0;
    virtual void edit() = 0;
    virtual void delete_() = 0;
    virtual ~Document() = default;
};

// RealSubject
class RealDocument : public Document {
private:
    string filename;
    string content;
    string owner;
    
public:
    RealDocument(const string& file, const string& own, const string& cont) 
        : filename(file), owner(own), content(cont) {
        cout << "RealDocument created: " << filename << " (owner: " << owner << ")" << endl;
    }
    
    void view() override {
        cout << "Viewing document: " << filename << endl;
        cout << "Content: " << content << endl;
    }
    
    void edit() override {
        cout << "Editing document: " << filename << endl;
        content += " [edited]";
    }
    
    void delete_() override {
        cout << "Deleting document: " << filename << endl;
    }
    
    string getOwner() const { return owner; }
};

// Protection Proxy
class DocumentProxy : public Document {
private:
    unique_ptr<RealDocument> realDoc;
    string currentUser;
    map<string, string> permissions; // user -> role
    
    bool hasPermission(const string& action) {
        string role = permissions[currentUser];
        
        if (action == "view") {
            return true; // Everyone can view
        } else if (action == "edit") {
            return role == "owner" || role == "admin";
        } else if (action == "delete") {
            return role == "owner";
        }
        return false;
    }
    
public:
    DocumentProxy(const string& file, const string& owner, const string& content,
                  const string& user) : currentUser(user) {
        realDoc = make_unique<RealDocument>(file, owner, content);
        permissions["admin"] = "admin";
        permissions[owner] = "owner";
        permissions["guest"] = "guest";
    }
    
    void view() override {
        if (hasPermission("view")) {
            realDoc->view();
        } else {
            cout << "Access denied: Cannot view document" << endl;
        }
    }
    
    void edit() override {
        if (hasPermission("edit")) {
            realDoc->edit();
        } else {
            cout << "Access denied: Cannot edit document (requires owner or admin)" << endl;
        }
    }
    
    void delete_() override {
        if (hasPermission("delete")) {
            realDoc->delete_();
        } else {
            cout << "Access denied: Cannot delete document (owner only)" << endl;
        }
    }
};

int main() {
    cout << "=== Protection Proxy (Access Control) ===" << endl;
    
    cout << "\nOwner accessing document:" << endl;
    DocumentProxy doc1("report.txt", "alice", "Annual report content", "alice");
    doc1.view();
    doc1.edit();
    doc1.delete_();
    
    cout << "\nAdmin accessing document:" << endl;
    DocumentProxy doc2("report.txt", "alice", "Annual report content", "admin");
    doc2.view();
    doc2.edit();
    doc2.delete_();
    
    cout << "\nGuest accessing document:" << endl;
    DocumentProxy doc3("report.txt", "alice", "Annual report content", "guest");
    doc3.view();
    doc3.edit();
    doc3.delete_();
    
    return 0;
}
```

---

## 3. **Cache Proxy**

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <memory>
#include <chrono>
#include <thread>
using namespace std;

// Subject interface
class DataFetcher {
public:
    virtual string fetchData(const string& key) = 0;
    virtual ~DataFetcher() = default;
};

// RealSubject
class RealDataFetcher : public DataFetcher {
private:
    string fetchFromDatabase(const string& key) {
        // Simulate database query delay
        this_thread::sleep_for(chrono::milliseconds(500));
        return "Data for " + key + " (from database)";
    }
    
public:
    string fetchData(const string& key) override {
        cout << "RealDataFetcher: Fetching from database..." << endl;
        return fetchFromDatabase(key);
    }
};

// Cache Proxy
class CacheProxy : public DataFetcher {
private:
    unique_ptr<RealDataFetcher> realFetcher;
    unordered_map<string, pair<string, chrono::steady_clock::time_point>> cache;
    chrono::seconds ttl;
    
    bool isExpired(const chrono::steady_clock::time_point& timestamp) {
        return chrono::steady_clock::now() - timestamp > ttl;
    }
    
public:
    CacheProxy(chrono::seconds cacheTTL = chrono::seconds(30)) 
        : realFetcher(make_unique<RealDataFetcher>()), ttl(cacheTTL) {}
    
    string fetchData(const string& key) override {
        auto it = cache.find(key);
        
        if (it != cache.end() && !isExpired(it->second.second)) {
            cout << "CacheProxy: Returning cached data for " << key << endl;
            return it->second.first;
        }
        
        cout << "CacheProxy: Cache miss for " << key << endl;
        string data = realFetcher->fetchData(key);
        cache[key] = {data, chrono::steady_clock::now()};
        return data;
    }
    
    void clearCache() {
        cache.clear();
        cout << "CacheProxy: Cache cleared" << endl;
    }
};

int main() {
    cout << "=== Cache Proxy ===" << endl;
    
    CacheProxy proxy(chrono::seconds(10));
    
    cout << "\nFirst fetch (cache miss):" << endl;
    string data1 = proxy.fetchData("user:123");
    cout << "Result: " << data1 << endl;
    
    cout << "\nSecond fetch (cache hit):" << endl;
    string data2 = proxy.fetchData("user:123");
    cout << "Result: " << data2 << endl;
    
    cout << "\nFetching different key:" << endl;
    string data3 = proxy.fetchData("product:456");
    cout << "Result: " << data3 << endl;
    
    cout << "\nFirst key again (still cached):" << endl;
    string data4 = proxy.fetchData("user:123");
    cout << "Result: " << data4 << endl;
    
    cout << "\nClearing cache:" << endl;
    proxy.clearCache();
    
    cout << "\nFetch after cache clear (cache miss):" << endl;
    string data5 = proxy.fetchData("user:123");
    cout << "Result: " << data5 << endl;
    
    return 0;
}
```

---

## 4. **Logging Proxy**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <chrono>
#include <iomanip>
using namespace std;

// Subject interface
class Calculator {
public:
    virtual int add(int a, int b) = 0;
    virtual int subtract(int a, int b) = 0;
    virtual int multiply(int a, int b) = 0;
    virtual int divide(int a, int b) = 0;
    virtual ~Calculator() = default;
};

// RealSubject
class RealCalculator : public Calculator {
public:
    int add(int a, int b) override {
        return a + b;
    }
    
    int subtract(int a, int b) override {
        return a - b;
    }
    
    int multiply(int a, int b) override {
        return a * b;
    }
    
    int divide(int a, int b) override {
        if (b == 0) throw runtime_error("Division by zero");
        return a / b;
    }
};

// Logging Proxy
class LoggingProxy : public Calculator {
private:
    unique_ptr<RealCalculator> realCalc;
    vector<string> logs;
    
    void logOperation(const string& operation, int a, int b, int result) {
        auto now = chrono::system_clock::now();
        auto time = chrono::system_clock::to_time_t(now);
        
        stringstream ss;
        ss << put_time(localtime(&time), "%H:%M:%S") << " - ";
        ss << operation << "(" << a << ", " << b << ") = " << result;
        logs.push_back(ss.str());
        
        cout << "[LOG] " << ss.str() << endl;
    }
    
    void logError(const string& operation, int a, int b, const string& error) {
        auto now = chrono::system_clock::now();
        auto time = chrono::system_clock::to_time_t(now);
        
        stringstream ss;
        ss << put_time(localtime(&time), "%H:%M:%S") << " - ";
        ss << operation << "(" << a << ", " << b << ") ERROR: " << error;
        logs.push_back(ss.str());
        
        cout << "[LOG] " << ss.str() << endl;
    }
    
public:
    LoggingProxy() : realCalc(make_unique<RealCalculator>()) {}
    
    int add(int a, int b) override {
        int result = realCalc->add(a, b);
        logOperation("add", a, b, result);
        return result;
    }
    
    int subtract(int a, int b) override {
        int result = realCalc->subtract(a, b);
        logOperation("subtract", a, b, result);
        return result;
    }
    
    int multiply(int a, int b) override {
        int result = realCalc->multiply(a, b);
        logOperation("multiply", a, b, result);
        return result;
    }
    
    int divide(int a, int b) override {
        try {
            int result = realCalc->divide(a, b);
            logOperation("divide", a, b, result);
            return result;
        } catch (const exception& e) {
            logError("divide", a, b, e.what());
            throw;
        }
    }
    
    void showLogs() const {
        cout << "\n=== Operation Logs ===" << endl;
        for (const auto& log : logs) {
            cout << log << endl;
        }
    }
};

int main() {
    cout << "=== Logging Proxy ===" << endl;
    
    LoggingProxy calc;
    
    cout << "\nPerforming calculations:" << endl;
    int result1 = calc.add(10, 5);
    cout << "Result: " << result1 << endl;
    
    int result2 = calc.subtract(10, 3);
    cout << "Result: " << result2 << endl;
    
    int result3 = calc.multiply(4, 7);
    cout << "Result: " << result3 << endl;
    
    try {
        int result4 = calc.divide(10, 0);
        cout << "Result: " << result4 << endl;
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    int result5 = calc.divide(20, 4);
    cout << "Result: " << result5 << endl;
    
    calc.showLogs();
    
    return 0;
}
```

---

## 5. **Practical Example: Remote Service Proxy**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <unordered_map>
#include <chrono>
#include <thread>
#include <random>
using namespace std;

// Subject interface
class WeatherService {
public:
    virtual double getTemperature(const string& city) = 0;
    virtual double getHumidity(const string& city) = 0;
    virtual string getForecast(const string& city) = 0;
    virtual ~WeatherService() = default;
};

// RealSubject (Remote service)
class RemoteWeatherService : public WeatherService {
private:
    string apiKey;
    
    double fetchTemperature(const string& city) {
        // Simulate network delay
        this_thread::sleep_for(chrono::milliseconds(500));
        
        // Simulate API call
        random_device rd;
        mt19937 gen(rd());
        uniform_real_distribution<> dis(-10, 40);
        return dis(gen);
    }
    
    double fetchHumidity(const string& city) {
        this_thread::sleep_for(chrono::milliseconds(500));
        random_device rd;
        mt19937 gen(rd());
        uniform_real_distribution<> dis(0, 100);
        return dis(gen);
    }
    
    string fetchForecast(const string& city) {
        this_thread::sleep_for(chrono::milliseconds(800));
        vector<string> forecasts = {"Sunny", "Cloudy", "Rainy", "Stormy", "Snowy"};
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<> dis(0, forecasts.size() - 1);
        return forecasts[dis(gen)];
    }
    
public:
    RemoteWeatherService(const string& key) : apiKey(key) {
        cout << "RemoteWeatherService initialized with API key" << endl;
    }
    
    double getTemperature(const string& city) override {
        cout << "RemoteWeatherService: Fetching temperature for " << city << "..." << endl;
        return fetchTemperature(city);
    }
    
    double getHumidity(const string& city) override {
        cout << "RemoteWeatherService: Fetching humidity for " << city << "..." << endl;
        return fetchHumidity(city);
    }
    
    string getForecast(const string& city) override {
        cout << "RemoteWeatherService: Fetching forecast for " << city << "..." << endl;
        return fetchForecast(city);
    }
};

// Proxy with caching and connection management
class WeatherProxy : public WeatherService {
private:
    unique_ptr<RemoteWeatherService> remoteService;
    unordered_map<string, pair<double, chrono::steady_clock::time_point>> tempCache;
    unordered_map<string, pair<double, chrono::steady_clock::time_point>> humidityCache;
    unordered_map<string, pair<string, chrono::steady_clock::time_point>> forecastCache;
    chrono::seconds cacheTTL;
    bool connected;
    
    bool isConnected() {
        // Simulate connection check
        return connected;
    }
    
    void connect() {
        cout << "WeatherProxy: Establishing connection..." << endl;
        this_thread::sleep_for(chrono::milliseconds(200));
        connected = true;
        cout << "WeatherProxy: Connected" << endl;
    }
    
    void disconnect() {
        if (connected) {
            cout << "WeatherProxy: Disconnecting..." << endl;
            connected = false;
        }
    }
    
    bool isExpired(const chrono::steady_clock::time_point& timestamp) {
        return chrono::steady_clock::now() - timestamp > cacheTTL;
    }
    
public:
    WeatherProxy(const string& apiKey, chrono::seconds ttl = chrono::seconds(60))
        : remoteService(make_unique<RemoteWeatherService>(apiKey)), cacheTTL(ttl), connected(false) {}
    
    ~WeatherProxy() {
        disconnect();
    }
    
    double getTemperature(const string& city) override {
        if (!isConnected()) {
            connect();
        }
        
        auto it = tempCache.find(city);
        if (it != tempCache.end() && !isExpired(it->second.second)) {
            cout << "WeatherProxy: Returning cached temperature for " << city << endl;
            return it->second.first;
        }
        
        cout << "WeatherProxy: Cache miss for temperature" << endl;
        double temp = remoteService->getTemperature(city);
        tempCache[city] = {temp, chrono::steady_clock::now()};
        return temp;
    }
    
    double getHumidity(const string& city) override {
        if (!isConnected()) {
            connect();
        }
        
        auto it = humidityCache.find(city);
        if (it != humidityCache.end() && !isExpired(it->second.second)) {
            cout << "WeatherProxy: Returning cached humidity for " << city << endl;
            return it->second.first;
        }
        
        cout << "WeatherProxy: Cache miss for humidity" << endl;
        double humidity = remoteService->getHumidity(city);
        humidityCache[city] = {humidity, chrono::steady_clock::now()};
        return humidity;
    }
    
    string getForecast(const string& city) override {
        if (!isConnected()) {
            connect();
        }
        
        auto it = forecastCache.find(city);
        if (it != forecastCache.end() && !isExpired(it->second.second)) {
            cout << "WeatherProxy: Returning cached forecast for " << city << endl;
            return it->second.first;
        }
        
        cout << "WeatherProxy: Cache miss for forecast" << endl;
        string forecast = remoteService->getForecast(city);
        forecastCache[city] = {forecast, chrono::steady_clock::now()};
        return forecast;
    }
    
    void clearCache() {
        tempCache.clear();
        humidityCache.clear();
        forecastCache.clear();
        cout << "WeatherProxy: Cache cleared" << endl;
    }
};

class WeatherApp {
private:
    unique_ptr<WeatherService> weatherService;
    
public:
    WeatherApp(WeatherService* service) : weatherService(service) {}
    
    void displayWeather(const string& city) {
        cout << "\n=== Weather for " << city << " ===" << endl;
        double temp = weatherService->getTemperature(city);
        double humidity = weatherService->getHumidity(city);
        string forecast = weatherService->getForecast(city);
        
        cout << "Temperature: " << temp << "°C" << endl;
        cout << "Humidity: " << humidity << "%" << endl;
        cout << "Forecast: " << forecast << endl;
    }
};

int main() {
    cout << "=== Remote Service Proxy ===" << endl;
    
    WeatherProxy proxy("API_KEY_12345", chrono::seconds(30));
    WeatherApp app(&proxy);
    
    cout << "\nFirst request (cache miss):" << endl;
    app.displayWeather("New York");
    
    cout << "\nSecond request (cache hit):" << endl;
    app.displayWeather("New York");
    
    cout << "\nDifferent city:" << endl;
    app.displayWeather("London");
    
    cout << "\nFirst city again (still cached):" << endl;
    app.displayWeather("New York");
    
    cout << "\nClearing cache:" << endl;
    proxy.clearCache();
    
    cout << "\nAfter cache clear (cache miss):" << endl;
    app.displayWeather("New York");
    
    return 0;
}
```

---

## 📊 Proxy Pattern Summary

| Proxy Type | Purpose | Example |
|------------|---------|---------|
| **Virtual Proxy** | Lazy initialization | Image loading, document loading |
| **Protection Proxy** | Access control | Authentication, authorization |
| **Cache Proxy** | Result caching | Database queries, API calls |
| **Logging Proxy** | Operation logging | Audit trails, debugging |
| **Remote Proxy** | Remote access | RMI, web services |

---

## ✅ Best Practices

1. **Use Proxy** when you need to control access to an object
2. **Implement same interface** as RealSubject
3. **Keep proxy lightweight** - defer to RealSubject when possible
4. **Consider thread safety** for concurrent access
5. **Document proxy behavior** (caching, lazy loading, etc.)

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Proxy becomes too complex** | Violates Single Responsibility | Separate concerns into multiple proxies |
| **Incorrect interface** | Proxy not usable as RealSubject | Ensure same interface |
| **Performance overhead** | Proxy adds unnecessary cost | Measure and optimize |
| **State synchronization** | Proxy and RealSubject out of sync | Properly manage state |

---

## ✅ Key Takeaways

1. **Proxy pattern** controls access to another object
2. **Virtual proxy** delays object creation
3. **Protection proxy** manages access permissions
4. **Cache proxy** stores results of expensive operations
5. **Logging proxy** records operations
6. **Useful for** cross-cutting concerns
7. **Same interface** as RealSubject

---
---

## Next Step

- Go to [03_Behavioral_Patterns](../03_Behavioral_Patterns/README.md) to continue.
