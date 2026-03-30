# Decorator Pattern in C++ - Complete Guide

## 📖 Overview

The Decorator pattern attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality. This pattern is also known as the Wrapper pattern and follows the Open/Closed Principle by allowing behavior extension without modifying existing code.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Component** | Interface for objects that can have responsibilities added |
| **Concrete Component** | The original object to which additional responsibilities can be attached |
| **Decorator** | Maintains reference to component and conforms to its interface |
| **Concrete Decorator** | Adds additional responsibilities to the component |

---

## 1. **Basic Decorator Pattern**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// Component interface
class Coffee {
public:
    virtual string getDescription() const = 0;
    virtual double getCost() const = 0;
    virtual ~Coffee() = default;
};

// Concrete Component
class SimpleCoffee : public Coffee {
public:
    string getDescription() const override {
        return "Simple Coffee";
    }
    
    double getCost() const override {
        return 2.0;
    }
};

// Decorator abstract class
class CoffeeDecorator : public Coffee {
protected:
    unique_ptr<Coffee> coffee;
    
public:
    CoffeeDecorator(Coffee* c) : coffee(c) {}
    
    virtual string getDescription() const override {
        return coffee->getDescription();
    }
    
    virtual double getCost() const override {
        return coffee->getCost();
    }
};

// Concrete Decorator 1
class MilkDecorator : public CoffeeDecorator {
public:
    MilkDecorator(Coffee* c) : CoffeeDecorator(c) {}
    
    string getDescription() const override {
        return coffee->getDescription() + ", Milk";
    }
    
    double getCost() const override {
        return coffee->getCost() + 0.5;
    }
};

// Concrete Decorator 2
class SugarDecorator : public CoffeeDecorator {
public:
    SugarDecorator(Coffee* c) : CoffeeDecorator(c) {}
    
    string getDescription() const override {
        return coffee->getDescription() + ", Sugar";
    }
    
    double getCost() const override {
        return coffee->getCost() + 0.2;
    }
};

// Concrete Decorator 3
class WhippedCreamDecorator : public CoffeeDecorator {
public:
    WhippedCreamDecorator(Coffee* c) : CoffeeDecorator(c) {}
    
    string getDescription() const override {
        return coffee->getDescription() + ", Whipped Cream";
    }
    
    double getCost() const override {
        return coffee->getCost() + 0.7;
    }
};

int main() {
    cout << "=== Basic Decorator Pattern ===" << endl;
    
    // Create a simple coffee
    Coffee* coffee = new SimpleCoffee();
    cout << coffee->getDescription() << " - $" << coffee->getCost() << endl;
    
    // Add milk
    coffee = new MilkDecorator(coffee);
    cout << coffee->getDescription() << " - $" << coffee->getCost() << endl;
    
    // Add sugar
    coffee = new SugarDecorator(coffee);
    cout << coffee->getDescription() << " - $" << coffee->getCost() << endl;
    
    // Add whipped cream
    coffee = new WhippedCreamDecorator(coffee);
    cout << coffee->getDescription() << " - $" << coffee->getCost() << endl;
    
    delete coffee;
    
    return 0;
}
```

**Output:**
```
=== Basic Decorator Pattern ===
Simple Coffee - $2
Simple Coffee, Milk - $2.5
Simple Coffee, Milk, Sugar - $2.7
Simple Coffee, Milk, Sugar, Whipped Cream - $3.4
```

---

## 2. **Decorator with Different Combinations**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <vector>
using namespace std;

// Component interface
class Pizza {
public:
    virtual string getDescription() const = 0;
    virtual double getCost() const = 0;
    virtual ~Pizza() = default;
};

// Concrete Component
class PlainPizza : public Pizza {
public:
    string getDescription() const override {
        return "Plain Pizza";
    }
    
    double getCost() const override {
        return 5.0;
    }
};

// Decorator base class
class PizzaDecorator : public Pizza {
protected:
    unique_ptr<Pizza> pizza;
    
public:
    PizzaDecorator(Pizza* p) : pizza(p) {}
    
    string getDescription() const override {
        return pizza->getDescription();
    }
    
    double getCost() const override {
        return pizza->getCost();
    }
};

// Concrete Decorators
class CheeseDecorator : public PizzaDecorator {
public:
    CheeseDecorator(Pizza* p) : PizzaDecorator(p) {}
    
    string getDescription() const override {
        return pizza->getDescription() + ", Extra Cheese";
    }
    
    double getCost() const override {
        return pizza->getCost() + 1.5;
    }
};

class PepperoniDecorator : public PizzaDecorator {
public:
    PepperoniDecorator(Pizza* p) : PizzaDecorator(p) {}
    
    string getDescription() const override {
        return pizza->getDescription() + ", Pepperoni";
    }
    
    double getCost() const override {
        return pizza->getCost() + 2.0;
    }
};

class MushroomDecorator : public PizzaDecorator {
public:
    MushroomDecorator(Pizza* p) : PizzaDecorator(p) {}
    
    string getDescription() const override {
        return pizza->getDescription() + ", Mushrooms";
    }
    
    double getCost() const override {
        return pizza->getCost() + 1.0;
    }
};

class OlivesDecorator : public PizzaDecorator {
public:
    OlivesDecorator(Pizza* p) : PizzaDecorator(p) {}
    
    string getDescription() const override {
        return pizza->getDescription() + ", Olives";
    }
    
    double getCost() const override {
        return pizza->getCost() + 0.8;
    }
};

int main() {
    cout << "=== Decorator with Different Combinations ===" << endl;
    
    // Different pizza combinations
    cout << "\n1. Vegetarian Pizza:" << endl;
    Pizza* vegPizza = new PlainPizza();
    vegPizza = new CheeseDecorator(vegPizza);
    vegPizza = new MushroomDecorator(vegPizza);
    vegPizza = new OlivesDecorator(vegPizza);
    cout << vegPizza->getDescription() << " - $" << vegPizza->getCost() << endl;
    
    cout << "\n2. Meat Lover's Pizza:" << endl;
    Pizza* meatPizza = new PlainPizza();
    meatPizza = new CheeseDecorator(meatPizza);
    meatPizza = new PepperoniDecorator(meatPizza);
    meatPizza = new PepperoniDecorator(meatPizza);  // Double pepperoni
    cout << meatPizza->getDescription() << " - $" << meatPizza->getCost() << endl;
    
    cout << "\n3. Supreme Pizza:" << endl;
    Pizza* supremePizza = new PlainPizza();
    supremePizza = new CheeseDecorator(supremePizza);
    supremePizza = new PepperoniDecorator(supremePizza);
    supremePizza = new MushroomDecorator(supremePizza);
    supremePizza = new OlivesDecorator(supremePizza);
    cout << supremePizza->getDescription() << " - $" << supremePizza->getCost() << endl;
    
    cout << "\n4. Cheese Lover's Pizza:" << endl;
    Pizza* cheesePizza = new PlainPizza();
    cheesePizza = new CheeseDecorator(cheesePizza);
    cheesePizza = new CheeseDecorator(cheesePizza);
    cheesePizza = new CheeseDecorator(cheesePizza);
    cout << cheesePizza->getDescription() << " - $" << cheesePizza->getCost() << endl;
    
    delete vegPizza;
    delete meatPizza;
    delete supremePizza;
    delete cheesePizza;
    
    return 0;
}
```

---

## 3. **Decorator with State**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <algorithm>
using namespace std;

// Component interface
class DataSource {
public:
    virtual void writeData(const string& data) = 0;
    virtual string readData() = 0;
    virtual ~DataSource() = default;
};

// Concrete Component
class FileDataSource : public DataSource {
private:
    string filename;
    string data;
    
public:
    FileDataSource(const string& name) : filename(name), data("") {}
    
    void writeData(const string& d) override {
        data = d;
        cout << "FileDataSource: Writing '" << data << "' to " << filename << endl;
    }
    
    string readData() override {
        cout << "FileDataSource: Reading from " << filename << endl;
        return data;
    }
};

// Decorator base class
class DataSourceDecorator : public DataSource {
protected:
    unique_ptr<DataSource> source;
    
public:
    DataSourceDecorator(DataSource* s) : source(s) {}
    
    void writeData(const string& data) override {
        source->writeData(data);
    }
    
    string readData() override {
        return source->readData();
    }
};

// Concrete Decorator: Encryption
class EncryptionDecorator : public DataSourceDecorator {
private:
    int shift;
    
    string encrypt(const string& data) {
        string result = data;
        for (char& c : result) {
            c = c + shift;
        }
        return result;
    }
    
    string decrypt(const string& data) {
        string result = data;
        for (char& c : result) {
            c = c - shift;
        }
        return result;
    }
    
public:
    EncryptionDecorator(DataSource* s, int sft = 3) 
        : DataSourceDecorator(s), shift(sft) {}
    
    void writeData(const string& data) override {
        string encrypted = encrypt(data);
        cout << "EncryptionDecorator: Encrypting data" << endl;
        source->writeData(encrypted);
    }
    
    string readData() override {
        string encrypted = source->readData();
        cout << "EncryptionDecorator: Decrypting data" << endl;
        return decrypt(encrypted);
    }
};

// Concrete Decorator: Compression
class CompressionDecorator : public DataSourceDecorator {
private:
    string compress(const string& data) {
        // Simulate compression
        return "[COMPRESSED]" + data;
    }
    
    string decompress(const string& data) {
        // Simulate decompression
        if (data.find("[COMPRESSED]") == 0) {
            return data.substr(12);
        }
        return data;
    }
    
public:
    CompressionDecorator(DataSource* s) : DataSourceDecorator(s) {}
    
    void writeData(const string& data) override {
        string compressed = compress(data);
        cout << "CompressionDecorator: Compressing data" << endl;
        source->writeData(compressed);
    }
    
    string readData() override {
        string compressed = source->readData();
        cout << "CompressionDecorator: Decompressing data" << endl;
        return decompress(compressed);
    }
};

// Concrete Decorator: Logging
class LoggingDecorator : public DataSourceDecorator {
private:
    vector<string> logs;
    
public:
    LoggingDecorator(DataSource* s) : DataSourceDecorator(s) {}
    
    void writeData(const string& data) override {
        logs.push_back("WRITE: " + data);
        cout << "LoggingDecorator: Logging write operation" << endl;
        source->writeData(data);
    }
    
    string readData() override {
        logs.push_back("READ");
        cout << "LoggingDecorator: Logging read operation" << endl;
        return source->readData();
    }
    
    void showLogs() const {
        cout << "\n--- Logs ---" << endl;
        for (const auto& log : logs) {
            cout << log << endl;
        }
    }
};

int main() {
    cout << "=== Decorator with State ===" << endl;
    
    // Create a data source with multiple decorators
    DataSource* source = new FileDataSource("data.txt");
    source = new EncryptionDecorator(source, 5);
    source = new CompressionDecorator(source);
    source = new LoggingDecorator(source);
    
    // Write data
    cout << "\n1. Writing data:" << endl;
    source->writeData("Hello World");
    
    // Read data
    cout << "\n2. Reading data:" << endl;
    string data = source->readData();
    cout << "Retrieved: " << data << endl;
    
    // Show logs (requires downcasting - not ideal, but for demonstration)
    cout << "\n3. Operation logs:" << endl;
    LoggingDecorator* logger = dynamic_cast<LoggingDecorator*>(source);
    if (logger) {
        logger->showLogs();
    }
    
    delete source;
    
    return 0;
}
```

---

## 4. **Decorator for UI Components**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <vector>
using namespace std;

// Component interface
class UIComponent {
public:
    virtual void draw() const = 0;
    virtual string getDescription() const = 0;
    virtual ~UIComponent() = default;
};

// Concrete Component
class TextView : public UIComponent {
private:
    string text;
    
public:
    TextView(const string& t) : text(t) {}
    
    void draw() const override {
        cout << "Drawing text: '" << text << "'" << endl;
    }
    
    string getDescription() const override {
        return "Text View";
    }
};

// Decorator base class
class UIDecorator : public UIComponent {
protected:
    unique_ptr<UIComponent> component;
    
public:
    UIDecorator(UIComponent* c) : component(c) {}
    
    void draw() const override {
        component->draw();
    }
    
    string getDescription() const override {
        return component->getDescription();
    }
};

// Concrete Decorator: Border
class BorderDecorator : public UIDecorator {
private:
    int thickness;
    string color;
    
public:
    BorderDecorator(UIComponent* c, int t, const string& col) 
        : UIDecorator(c), thickness(t), color(col) {}
    
    void draw() const override {
        component->draw();
        cout << "  Adding " << thickness << "px " << color << " border" << endl;
    }
    
    string getDescription() const override {
        return component->getDescription() + " with border";
    }
};

// Concrete Decorator: Shadow
class ShadowDecorator : public UIDecorator {
private:
    int offsetX, offsetY;
    int blur;
    
public:
    ShadowDecorator(UIComponent* c, int x, int y, int b) 
        : UIDecorator(c), offsetX(x), offsetY(y), blur(b) {}
    
    void draw() const override {
        component->draw();
        cout << "  Adding shadow (offset=" << offsetX << "," << offsetY 
             << ", blur=" << blur << ")" << endl;
    }
    
    string getDescription() const override {
        return component->getDescription() + " with shadow";
    }
};

// Concrete Decorator: Background
class BackgroundDecorator : public UIDecorator {
private:
    string color;
    
public:
    BackgroundDecorator(UIComponent* c, const string& col) 
        : UIDecorator(c), color(col) {}
    
    void draw() const override {
        cout << "  Drawing " << color << " background" << endl;
        component->draw();
    }
    
    string getDescription() const override {
        return component->getDescription() + " with background";
    }
};

// Concrete Decorator: Tooltip
class TooltipDecorator : public UIDecorator {
private:
    string tooltipText;
    
public:
    TooltipDecorator(UIComponent* c, const string& tip) 
        : UIDecorator(c), tooltipText(tip) {}
    
    void draw() const override {
        component->draw();
        cout << "  Adding tooltip: '" << tooltipText << "'" << endl;
    }
    
    string getDescription() const override {
        return component->getDescription() + " with tooltip";
    }
};

int main() {
    cout << "=== Decorator for UI Components ===" << endl;
    
    cout << "\n1. Simple text view:" << endl;
    UIComponent* text1 = new TextView("Hello");
    text1->draw();
    cout << "Description: " << text1->getDescription() << endl;
    
    cout << "\n2. Text with border:" << endl;
    UIComponent* text2 = new BorderDecorator(new TextView("World"), 2, "blue");
    text2->draw();
    cout << "Description: " << text2->getDescription() << endl;
    
    cout << "\n3. Text with border and shadow:" << endl;
    UIComponent* text3 = new ShadowDecorator(
        new BorderDecorator(new TextView("Styled"), 3, "red"), 5, 5, 10);
    text3->draw();
    cout << "Description: " << text3->getDescription() << endl;
    
    cout << "\n4. Fully decorated text:" << endl;
    UIComponent* text4 = new TooltipDecorator(
        new BackgroundDecorator(
            new ShadowDecorator(
                new BorderDecorator(new TextView("Rich Text"), 2, "darkblue"), 
                4, 4, 8),
            "lightgray"),
        "Click me for info");
    text4->draw();
    cout << "Description: " << text4->getDescription() << endl;
    
    delete text1;
    delete text2;
    delete text3;
    delete text4;
    
    return 0;
}
```

---

## 5. **Practical Example: Notification System**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <algorithm>
using namespace std;

// Component interface
class Notifier {
public:
    virtual void send(const string& message) = 0;
    virtual string getType() const = 0;
    virtual ~Notifier() = default;
};

// Concrete Component
class EmailNotifier : public Notifier {
private:
    string email;
    
public:
    EmailNotifier(const string& e) : email(e) {}
    
    void send(const string& message) override {
        cout << "Sending email to " << email << ": " << message << endl;
    }
    
    string getType() const override {
        return "Email";
    }
};

// Decorator base class
class NotifierDecorator : public Notifier {
protected:
    unique_ptr<Notifier> notifier;
    
public:
    NotifierDecorator(Notifier* n) : notifier(n) {}
    
    void send(const string& message) override {
        notifier->send(message);
    }
    
    string getType() const override {
        return notifier->getType();
    }
};

// Concrete Decorator: SMS
class SMSNotifier : public NotifierDecorator {
private:
    string phoneNumber;
    
public:
    SMSNotifier(Notifier* n, const string& phone) 
        : NotifierDecorator(n), phoneNumber(phone) {}
    
    void send(const string& message) override {
        NotifierDecorator::send(message);
        cout << "Sending SMS to " << phoneNumber << ": " << message << endl;
    }
    
    string getType() const override {
        return NotifierDecorator::getType() + " + SMS";
    }
};

// Concrete Decorator: Slack
class SlackNotifier : public NotifierDecorator {
private:
    string channel;
    
public:
    SlackNotifier(Notifier* n, const string& ch) 
        : NotifierDecorator(n), channel(ch) {}
    
    void send(const string& message) override {
        NotifierDecorator::send(message);
        cout << "Sending Slack message to #" << channel << ": " << message << endl;
    }
    
    string getType() const override {
        return NotifierDecorator::getType() + " + Slack";
    }
};

// Concrete Decorator: Push Notification
class PushNotifier : public NotifierDecorator {
private:
    string deviceId;
    
public:
    PushNotifier(Notifier* n, const string& device) 
        : NotifierDecorator(n), deviceId(device) {}
    
    void send(const string& message) override {
        NotifierDecorator::send(message);
        cout << "Sending push notification to device " << deviceId << ": " << message << endl;
    }
    
    string getType() const override {
        return NotifierDecorator::getType() + " + Push";
    }
};

// Concrete Decorator: Logging
class LoggingNotifier : public NotifierDecorator {
private:
    vector<string> logs;
    
public:
    LoggingNotifier(Notifier* n) : NotifierDecorator(n) {}
    
    void send(const string& message) override {
        logs.push_back(message);
        NotifierDecorator::send(message);
        cout << "Logging notification: " << message << endl;
    }
    
    string getType() const override {
        return NotifierDecorator::getType() + " + Logging";
    }
    
    void showLogs() const {
        cout << "\n--- Notification Logs ---" << endl;
        for (const auto& log : logs) {
            cout << "  " << log << endl;
        }
    }
};

class NotificationService {
private:
    unique_ptr<Notifier> notifier;
    
public:
    void setNotifier(Notifier* n) {
        notifier.reset(n);
    }
    
    void sendNotification(const string& message) {
        if (notifier) {
            cout << "\nSending notification via: " << notifier->getType() << endl;
            notifier->send(message);
        }
    }
    
    void showLogs() {
        LoggingNotifier* logger = dynamic_cast<LoggingNotifier*>(notifier.get());
        if (logger) {
            logger->showLogs();
        }
    }
};

int main() {
    cout << "=== Notification System ===" << endl;
    
    NotificationService service;
    
    cout << "\n1. Email only:" << endl;
    service.setNotifier(new EmailNotifier("user@example.com"));
    service.sendNotification("Welcome to the system!");
    
    cout << "\n2. Email + SMS:" << endl;
    service.setNotifier(new SMSNotifier(
        new EmailNotifier("admin@example.com"), "+1234567890"));
    service.sendNotification("System alert: High CPU usage");
    
    cout << "\n3. Email + SMS + Slack:" << endl;
    service.setNotifier(new SlackNotifier(
        new SMSNotifier(
            new EmailNotifier("team@example.com"), "+9876543210"),
        "alerts"));
    service.sendNotification("Deployment completed");
    
    cout << "\n4. All channels + Logging:" << endl;
    service.setNotifier(new LoggingNotifier(
        new PushNotifier(
            new SlackNotifier(
                new SMSNotifier(
                    new EmailNotifier("all@example.com"), "+1111111111"),
                "general"),
            "device-123")));
    service.sendNotification("Critical: Database connection lost");
    service.showLogs();
    
    return 0;
}
```

---

## 📊 Decorator Pattern Summary

| Component | Description |
|-----------|-------------|
| **Component** | Defines the interface for objects that can be decorated |
| **Concrete Component** | The original object to be decorated |
| **Decorator** | Abstract class that implements the component interface |
| **Concrete Decorator** | Adds specific responsibilities to the component |

---

## ✅ Best Practices

1. **Use Decorator** when you need to add responsibilities dynamically
2. **Keep decorators lightweight** - each should add a single responsibility
3. **Maintain component interface** - decorators must conform to the same interface
4. **Consider ordering** - decorator order affects behavior
5. **Use with factory** to create complex decorated objects

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Too many decorators** | Complex, hard to debug | Limit decorator depth |
| **Identity issues** | Decorated object not same as component | Use component interface |
| **Order dependency** | Results vary with order | Document ordering requirements |

---

## ✅ Key Takeaways

1. **Decorator pattern** adds responsibilities dynamically
2. **Alternative to subclassing** for extending functionality
3. **Flexible** - can combine decorators in any order
4. **Follows** Open/Closed Principle
5. **Useful for** UI components, I/O streams, notification systems
6. **Enables** composition of behaviors at runtime

---