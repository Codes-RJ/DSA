# 12_Design_Patterns/03_Behavioral_Patterns/Observer.md

# Observer Pattern in C++ - Complete Guide

## 📖 Overview

The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. It is also known as the Publish-Subscribe pattern and is widely used in event handling systems, GUI frameworks, and message broadcasting.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Subject** | Object that maintains a list of observers and notifies them of state changes |
| **Observer** | Interface for objects that should be notified of changes |
| **Concrete Subject** | Stores state of interest and sends notifications |
| **Concrete Observer** | Implements update method to respond to notifications |

---

## 1. **Basic Observer Pattern**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <memory>
using namespace std;

// Observer interface
class IObserver {
public:
    virtual void update(const string& message) = 0;
    virtual ~IObserver() = default;
};

// Subject interface
class ISubject {
public:
    virtual void attach(IObserver* observer) = 0;
    virtual void detach(IObserver* observer) = 0;
    virtual void notify() = 0;
    virtual ~ISubject() = default;
};

// Concrete Subject
class NewsPublisher : public ISubject {
private:
    vector<IObserver*> observers;
    string latestNews;
    
public:
    void attach(IObserver* observer) override {
        observers.push_back(observer);
        cout << "Observer attached" << endl;
    }
    
    void detach(IObserver* observer) override {
        auto it = find(observers.begin(), observers.end(), observer);
        if (it != observers.end()) {
            observers.erase(it);
            cout << "Observer detached" << endl;
        }
    }
    
    void notify() override {
        cout << "Notifying " << observers.size() << " observers..." << endl;
        for (auto observer : observers) {
            observer->update(latestNews);
        }
    }
    
    void setNews(const string& news) {
        latestNews = news;
        cout << "\nNews updated: " << news << endl;
        notify();
    }
};

// Concrete Observer 1
class EmailSubscriber : public IObserver {
private:
    string email;
    
public:
    EmailSubscriber(const string& e) : email(e) {}
    
    void update(const string& message) override {
        cout << "Email to " << email << ": " << message << endl;
    }
};

// Concrete Observer 2
class SMSSubscriber : public IObserver {
private:
    string phoneNumber;
    
public:
    SMSSubscriber(const string& phone) : phoneNumber(phone) {}
    
    void update(const string& message) override {
        cout << "SMS to " << phoneNumber << ": " << message << endl;
    }
};

// Concrete Observer 3
class LoggerSubscriber : public IObserver {
public:
    void update(const string& message) override {
        cout << "[LOG] News received: " << message << endl;
    }
};

int main() {
    cout << "=== Basic Observer Pattern ===" << endl;
    
    NewsPublisher publisher;
    
    EmailSubscriber email1("user1@example.com");
    EmailSubscriber email2("user2@example.com");
    SMSSubscriber sms("+1234567890");
    LoggerSubscriber logger;
    
    publisher.attach(&email1);
    publisher.attach(&email2);
    publisher.attach(&sms);
    publisher.attach(&logger);
    
    publisher.setNews("Breaking: C++20 released!");
    
    publisher.detach(&email2);
    
    publisher.setNews("Update: New design patterns added");
    
    return 0;
}
```

**Output:**
```
=== Basic Observer Pattern ===
Observer attached
Observer attached
Observer attached
Observer attached

News updated: Breaking: C++20 released!
Notifying 4 observers...
Email to user1@example.com: Breaking: C++20 released!
Email to user2@example.com: Breaking: C++20 released!
SMS to +1234567890: Breaking: C++20 released!
[LOG] News received: Breaking: C++20 released!
Observer detached

News updated: Update: New design patterns added
Notifying 3 observers...
Email to user1@example.com: Update: New design patterns added
SMS to +1234567890: Update: New design patterns added
[LOG] News received: Update: New design patterns added
```

---

## 2. **Observer with State**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <memory>
using namespace std;

class IObserver {
public:
    virtual void update(int temperature, int humidity, int pressure) = 0;
    virtual ~IObserver() = default;
};

class ISubject {
public:
    virtual void attach(IObserver* observer) = 0;
    virtual void detach(IObserver* observer) = 0;
    virtual void notify() = 0;
    virtual ~ISubject() = default;
};

class WeatherStation : public ISubject {
private:
    vector<IObserver*> observers;
    int temperature;
    int humidity;
    int pressure;
    
public:
    void attach(IObserver* observer) override {
        observers.push_back(observer);
    }
    
    void detach(IObserver* observer) override {
        auto it = find(observers.begin(), observers.end(), observer);
        if (it != observers.end()) {
            observers.erase(it);
        }
    }
    
    void notify() override {
        for (auto observer : observers) {
            observer->update(temperature, humidity, pressure);
        }
    }
    
    void setMeasurements(int temp, int hum, int pres) {
        temperature = temp;
        humidity = hum;
        pressure = pres;
        measurementsChanged();
    }
    
    void measurementsChanged() {
        notify();
    }
};

class CurrentConditionsDisplay : public IObserver {
public:
    void update(int temperature, int humidity, int pressure) override {
        cout << "Current conditions: " << temperature << "°C, "
             << humidity << "%, " << pressure << " hPa" << endl;
    }
};

class StatisticsDisplay : public IObserver {
private:
    vector<int> temperatures;
    
public:
    void update(int temperature, int humidity, int pressure) override {
        temperatures.push_back(temperature);
        
        int sum = 0;
        for (int t : temperatures) sum += t;
        double avg = static_cast<double>(sum) / temperatures.size();
        
        cout << "Statistics: Avg temperature = " << avg << "°C, "
             << "Min = " << *min_element(temperatures.begin(), temperatures.end()) << "°C, "
             << "Max = " << *max_element(temperatures.begin(), temperatures.end()) << "°C" << endl;
    }
};

class ForecastDisplay : public IObserver {
private:
    int lastPressure;
    
public:
    ForecastDisplay() : lastPressure(0) {}
    
    void update(int temperature, int humidity, int pressure) override {
        string forecast;
        if (pressure > lastPressure) {
            forecast = "Improving weather";
        } else if (pressure < lastPressure) {
            forecast = "Cooler, rainy weather";
        } else {
            forecast = "More of the same";
        }
        lastPressure = pressure;
        
        cout << "Forecast: " << forecast << endl;
    }
};

class HeatIndexDisplay : public IObserver {
public:
    void update(int temperature, int humidity, int pressure) override {
        double heatIndex = temperature + 0.1 * humidity;
        cout << "Heat index: " << heatIndex << endl;
    }
};

int main() {
    cout << "=== Observer with State ===" << endl;
    
    WeatherStation station;
    
    CurrentConditionsDisplay current;
    StatisticsDisplay stats;
    ForecastDisplay forecast;
    HeatIndexDisplay heatIndex;
    
    station.attach(&current);
    station.attach(&stats);
    station.attach(&forecast);
    station.attach(&heatIndex);
    
    cout << "\nFirst measurement:" << endl;
    station.setMeasurements(25, 65, 1013);
    
    cout << "\nSecond measurement:" << endl;
    station.setMeasurements(28, 70, 1010);
    
    cout << "\nThird measurement:" << endl;
    station.setMeasurements(22, 55, 1015);
    
    return 0;
}
```

---

## 3. **Observer with Event Data**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <functional>
#include <chrono>
#include <iomanip>
#include <sstream>
using namespace std;

// Event data structure
struct EventData {
    string eventType;
    string source;
    string message;
    chrono::system_clock::time_point timestamp;
    
    string getTimestamp() const {
        auto time = chrono::system_clock::to_time_t(timestamp);
        stringstream ss;
        ss << put_time(localtime(&time), "%H:%M:%S");
        return ss.str();
    }
};

// Observer interface
class IEventListener {
public:
    virtual void onEvent(const EventData& event) = 0;
    virtual ~IEventListener() = default;
};

class EventManager {
private:
    map<string, vector<IEventListener*>> listeners;
    
public:
    void subscribe(const string& eventType, IEventListener* listener) {
        listeners[eventType].push_back(listener);
        cout << "Listener subscribed to: " << eventType << endl;
    }
    
    void unsubscribe(const string& eventType, IEventListener* listener) {
        auto& vec = listeners[eventType];
        auto it = find(vec.begin(), vec.end(), listener);
        if (it != vec.end()) {
            vec.erase(it);
            cout << "Listener unsubscribed from: " << eventType << endl;
        }
    }
    
    void publish(const EventData& event) {
        auto it = listeners.find(event.eventType);
        if (it != listeners.end()) {
            cout << "\nPublishing event: " << event.eventType << " at " 
                 << event.getTimestamp() << endl;
            for (auto listener : it->second) {
                listener->onEvent(event);
            }
        }
    }
};

// Concrete listeners
class EmailNotifier : public IEventListener {
private:
    string email;
    
public:
    EmailNotifier(const string& e) : email(e) {}
    
    void onEvent(const EventData& event) override {
        cout << "  Email to " << email << ": [" << event.eventType 
             << "] " << event.message << endl;
    }
};

class SMSNotifier : public IEventListener {
private:
    string phone;
    
public:
    SMSNotifier(const string& p) : phone(p) {}
    
    void onEvent(const EventData& event) override {
        cout << "  SMS to " << phone << ": [" << event.eventType 
             << "] " << event.message << endl;
    }
};

class Logger : public IEventListener {
public:
    void onEvent(const EventData& event) override {
        cout << "  [LOG] " << event.getTimestamp() << " - " 
             << event.eventType << " - " << event.message << endl;
    }
};

class AlertSystem : public IEventListener {
public:
    void onEvent(const EventData& event) override {
        if (event.eventType == "CRITICAL") {
            cout << "  [ALERT] CRITICAL EVENT: " << event.message << endl;
        }
    }
};

int main() {
    cout << "=== Observer with Event Data ===" << endl;
    
    EventManager eventManager;
    
    EmailNotifier email("admin@example.com");
    SMSNotifier sms("+1234567890");
    Logger logger;
    AlertSystem alert;
    
    // Subscribe to different events
    eventManager.subscribe("INFO", &email);
    eventManager.subscribe("INFO", &logger);
    eventManager.subscribe("WARNING", &email);
    eventManager.subscribe("WARNING", &sms);
    eventManager.subscribe("WARNING", &logger);
    eventManager.subscribe("CRITICAL", &email);
    eventManager.subscribe("CRITICAL", &sms);
    eventManager.subscribe("CRITICAL", &logger);
    eventManager.subscribe("CRITICAL", &alert);
    
    // Publish events
    EventData infoEvent{"INFO", "System", "User logged in", chrono::system_clock::now()};
    eventManager.publish(infoEvent);
    
    EventData warningEvent{"WARNING", "Database", "Connection pool low", chrono::system_clock::now()};
    eventManager.publish(warningEvent);
    
    EventData criticalEvent{"CRITICAL", "Server", "CPU usage 95%", chrono::system_clock::now()};
    eventManager.publish(criticalEvent);
    
    // Unsubscribe and publish again
    eventManager.unsubscribe("INFO", &email);
    
    EventData anotherInfoEvent{"INFO", "System", "User logged out", chrono::system_clock::now()};
    eventManager.publish(anotherInfoEvent);
    
    return 0;
}
```

---

## 4. **Observer with Weak Ptr (Preventing Memory Leaks)**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
using namespace std;

class IObserver {
public:
    virtual void update(const string& message) = 0;
    virtual ~IObserver() = default;
};

class Subject {
private:
    vector<weak_ptr<IObserver>> observers;
    
public:
    void attach(shared_ptr<IObserver> observer) {
        observers.push_back(observer);
        cout << "Observer attached" << endl;
    }
    
    void notify(const string& message) {
        cout << "Notifying observers..." << endl;
        
        // Clean up expired weak_ptrs while notifying
        for (auto it = observers.begin(); it != observers.end();) {
            if (auto observer = it->lock()) {
                observer->update(message);
                ++it;
            } else {
                cout << "Removing expired observer" << endl;
                it = observers.erase(it);
            }
        }
    }
};

class ConcreteObserver : public IObserver, public enable_shared_from_this<ConcreteObserver> {
private:
    string name;
    
public:
    ConcreteObserver(const string& n) : name(n) {}
    
    void update(const string& message) override {
        cout << "Observer " << name << " received: " << message << endl;
    }
    
    ~ConcreteObserver() {
        cout << "Observer " << name << " destroyed" << endl;
    }
};

int main() {
    cout << "=== Observer with Weak Ptr ===" << endl;
    
    Subject subject;
    
    {
        auto observer1 = make_shared<ConcreteObserver>("Observer1");
        auto observer2 = make_shared<ConcreteObserver>("Observer2");
        
        subject.attach(observer1);
        subject.attach(observer2);
        
        cout << "\nFirst notification:" << endl;
        subject.notify("Hello World");
        
        cout << "\nObserver2 going out of scope..." << endl;
    } // observer2 destroyed here
    
    cout << "\nSecond notification (observer2 automatically removed):" << endl;
    subject.notify("Goodbye");
    
    return 0;
}
```

---

## 5. **Practical Example: Stock Market System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <memory>
#include <random>
#include <iomanip>
using namespace std;

class IStockObserver {
public:
    virtual void onPriceChange(const string& symbol, double oldPrice, double newPrice) = 0;
    virtual ~IStockObserver() = default;
};

class Stock {
private:
    string symbol;
    double price;
    vector<IStockObserver*> observers;
    
public:
    Stock(const string& sym, double initialPrice) 
        : symbol(sym), price(initialPrice) {}
    
    void attach(IStockObserver* observer) {
        observers.push_back(observer);
    }
    
    void detach(IStockObserver* observer) {
        auto it = find(observers.begin(), observers.end(), observer);
        if (it != observers.end()) {
            observers.erase(it);
        }
    }
    
    void setPrice(double newPrice) {
        if (price != newPrice) {
            double oldPrice = price;
            price = newPrice;
            notify(oldPrice, newPrice);
        }
    }
    
    double getPrice() const { return price; }
    string getSymbol() const { return symbol; }
    
private:
    void notify(double oldPrice, double newPrice) {
        cout << "\nStock " << symbol << " price changed: $" 
             << fixed << setprecision(2) << oldPrice << " -> $" << newPrice << endl;
        for (auto observer : observers) {
            observer->onPriceChange(symbol, oldPrice, newPrice);
        }
    }
};

class Investor : public IStockObserver {
private:
    string name;
    double budget;
    map<string, int> portfolio;
    
public:
    Investor(const string& n, double b) : name(n), budget(b) {}
    
    void onPriceChange(const string& symbol, double oldPrice, double newPrice) override {
        double change = ((newPrice - oldPrice) / oldPrice) * 100;
        
        cout << "  Investor " << name << ": " << symbol 
             << " changed by " << (change > 0 ? "+" : "") << change << "%" << endl;
        
        // Simple trading strategy
        if (change < -5 && budget > newPrice) {
            buy(symbol, 10, newPrice);
        } else if (change > 10 && portfolio[symbol] > 0) {
            sell(symbol, 5, newPrice);
        }
    }
    
    void buy(const string& symbol, int shares, double price) {
        double cost = shares * price;
        if (cost <= budget) {
            portfolio[symbol] += shares;
            budget -= cost;
            cout << "    " << name << " bought " << shares << " shares of " 
                 << symbol << " for $" << cost << endl;
        }
    }
    
    void sell(const string& symbol, int shares, double price) {
        if (portfolio[symbol] >= shares) {
            double revenue = shares * price;
            portfolio[symbol] -= shares;
            budget += revenue;
            cout << "    " << name << " sold " << shares << " shares of " 
                 << symbol << " for $" << revenue << endl;
        }
    }
    
    void displayPortfolio() const {
        cout << "\n" << name << "'s Portfolio:" << endl;
        cout << "  Budget: $" << budget << endl;
        for (const auto& [symbol, shares] : portfolio) {
            if (shares > 0) {
                cout << "  " << symbol << ": " << shares << " shares" << endl;
            }
        }
    }
};

class MarketAnalyzer : public IStockObserver {
public:
    void onPriceChange(const string& symbol, double oldPrice, double newPrice) override {
        double change = ((newPrice - oldPrice) / oldPrice) * 100;
        
        if (change > 5) {
            cout << "  [ANALYSIS] " << symbol << " is showing strong upward momentum" << endl;
        } else if (change < -5) {
            cout << "  [ANALYSIS] " << symbol << " is showing downward pressure" << endl;
        }
    }
};

class AlertSystem : public IStockObserver {
public:
    void onPriceChange(const string& symbol, double oldPrice, double newPrice) override {
        if (newPrice > 150) {
            cout << "  [ALERT] " << symbol << " has exceeded $150!" << endl;
        } else if (newPrice < 50) {
            cout << "  [ALERT] " << symbol << " has fallen below $50!" << endl;
        }
    }
};

class StockMarket {
private:
    map<string, unique_ptr<Stock>> stocks;
    random_device rd;
    mt19937 gen;
    
public:
    StockMarket() : gen(rd()) {}
    
    void addStock(const string& symbol, double initialPrice) {
        stocks[symbol] = make_unique<Stock>(symbol, initialPrice);
    }
    
    Stock* getStock(const string& symbol) {
        return stocks[symbol].get();
    }
    
    void simulatePriceChanges(int iterations) {
        uniform_real_distribution<> dis(-10, 10);
        
        for (int i = 0; i < iterations; i++) {
            cout << "\n=== Market Update " << (i + 1) << " ===" << endl;
            
            for (auto& [symbol, stock] : stocks) {
                double changePercent = dis(gen) / 100;
                double newPrice = stock->getPrice() * (1 + changePercent);
                stock->setPrice(newPrice);
            }
        }
    }
};

int main() {
    cout << "=== Stock Market System ===" << endl;
    
    StockMarket market;
    
    // Add stocks
    market.addStock("AAPL", 150.0);
    market.addStock("GOOGL", 2800.0);
    market.addStock("MSFT", 300.0);
    market.addStock("AMZN", 3300.0);
    
    // Create investors and observers
    Investor alice("Alice", 10000);
    Investor bob("Bob", 15000);
    MarketAnalyzer analyzer;
    AlertSystem alerts;
    
    // Attach observers to stocks
    Stock* aapl = market.getStock("AAPL");
    Stock* googl = market.getStock("GOOGL");
    Stock* msft = market.getStock("MSFT");
    
    aapl->attach(&alice);
    aapl->attach(&bob);
    aapl->attach(&analyzer);
    aapl->attach(&alerts);
    
    googl->attach(&alice);
    googl->attach(&analyzer);
    
    msft->attach(&bob);
    msft->attach(&alerts);
    
    // Simulate market
    market.simulatePriceChanges(5);
    
    // Display final portfolios
    alice.displayPortfolio();
    bob.displayPortfolio();
    
    return 0;
}
```

---

## 📊 Observer Pattern Summary

| Component | Description |
|-----------|-------------|
| **Subject** | Maintains observers and notifies them of changes |
| **Observer** | Interface for objects that need to be notified |
| **Concrete Subject** | Stores state and sends notifications |
| **Concrete Observer** | Implements update method |

---

## ✅ Best Practices

1. **Use Observer** for one-to-many dependencies
2. **Avoid memory leaks** - use weak_ptr for observers
3. **Consider event data** - pass context information
4. **Be careful with order** - notification order may matter
5. **Handle exceptions** - one observer shouldn't break others

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Memory leaks** | Observers not removed | Use weak_ptr or ensure detach |
| **Performance** | Too many notifications | Batch updates, throttle |
| **Circular dependencies** | Infinite loops | Check for cycles |
| **Order dependency** | Unexpected behavior | Document order or make independent |

---

## ✅ Key Takeaways

1. **Observer pattern** enables one-to-many notification
2. **Subject** notifies observers of state changes
3. **Loose coupling** between subject and observers
4. **Widely used** in event-driven systems
5. **Multiple observers** can react to same event
6. **Can be implemented** with weak_ptr to avoid leaks

---