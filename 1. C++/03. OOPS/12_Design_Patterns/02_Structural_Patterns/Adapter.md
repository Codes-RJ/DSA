# 12_Design_Patterns/02_Structural_Patterns/Adapter.md

# Adapter Pattern in C++ - Complete Guide

## 📖 Overview

The Adapter pattern converts the interface of a class into another interface that clients expect. It allows classes to work together that couldn't otherwise because of incompatible interfaces. The Adapter pattern is also known as the Wrapper pattern and is commonly used to integrate legacy code or third-party libraries.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Target** | The interface that the client expects |
| **Adaptee** | The existing class with an incompatible interface |
| **Adapter** | Converts the Adaptee's interface to the Target interface |
| **Class Adapter** | Uses inheritance (multiple inheritance in C++) |
| **Object Adapter** | Uses composition (preferred approach) |

---

## 1. **Object Adapter (Composition-based)**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// Target interface (what the client expects)
class ITarget {
public:
    virtual void request(const string& data) = 0;
    virtual ~ITarget() = default;
};

// Adaptee (existing class with incompatible interface)
class LegacySystem {
public:
    void legacyRequest(const char* data, int length) {
        cout << "LegacySystem processing: " << string(data, length) << endl;
    }
    
    void oldMethod() {
        cout << "LegacySystem: old method called" << endl;
    }
};

// Object Adapter (uses composition)
class ObjectAdapter : public ITarget {
private:
    unique_ptr<LegacySystem> adaptee;
    
public:
    ObjectAdapter() : adaptee(make_unique<LegacySystem>()) {}
    
    void request(const string& data) override {
        // Convert the interface
        adaptee->legacyRequest(data.c_str(), data.length());
    }
};

// Another Adaptee
class ThirdPartyLibrary {
public:
    void process(const string& input) {
        cout << "ThirdPartyLibrary processing: " << input << endl;
    }
    
    void execute(const string& cmd) {
        cout << "ThirdPartyLibrary executing: " << cmd << endl;
    }
};

// Adapter for ThirdPartyLibrary
class LibraryAdapter : public ITarget {
private:
    unique_ptr<ThirdPartyLibrary> library;
    
public:
    LibraryAdapter() : library(make_unique<ThirdPartyLibrary>()) {}
    
    void request(const string& data) override {
        library->process(data);
    }
};

int main() {
    cout << "=== Object Adapter (Composition-based) ===" << endl;
    
    // Client works with ITarget interface
    ITarget* targets[] = {
        new ObjectAdapter(),
        new LibraryAdapter()
    };
    
    string data = "Hello World";
    
    for (auto target : targets) {
        target->request(data);
    }
    
    for (auto target : targets) {
        delete target;
    }
    
    return 0;
}
```

**Output:**
```
=== Object Adapter (Composition-based) ===
LegacySystem processing: Hello World
ThirdPartyLibrary processing: Hello World
```

---

## 2. **Class Adapter (Multiple Inheritance)**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Target interface
class IPrinter {
public:
    virtual void print(const string& text) = 0;
    virtual ~IPrinter() = default;
};

// Adaptee 1
class LegacyPrinter {
public:
    void printOld(const char* text) {
        cout << "LegacyPrinter: " << text << endl;
    }
};

// Adaptee 2
class ModernPrinter {
public:
    void printModern(const string& text) {
        cout << "ModernPrinter: " << text << endl;
    }
};

// Class Adapter using multiple inheritance
class LegacyPrinterAdapter : public IPrinter, private LegacyPrinter {
public:
    void print(const string& text) override {
        printOld(text.c_str());
    }
};

class ModernPrinterAdapter : public IPrinter, private ModernPrinter {
public:
    void print(const string& text) override {
        printModern(text);
    }
};

// Client code
class Document {
public:
    void print(IPrinter& printer, const string& content) {
        printer.print(content);
    }
};

int main() {
    cout << "=== Class Adapter (Multiple Inheritance) ===" << endl;
    
    Document doc;
    
    LegacyPrinterAdapter legacyAdapter;
    ModernPrinterAdapter modernAdapter;
    
    doc.print(legacyAdapter, "Hello from legacy");
    doc.print(modernAdapter, "Hello from modern");
    
    return 0;
}
```

---

## 3. **Two-Way Adapter**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// Interface 1
class IUSBDevice {
public:
    virtual void transferData(const string& data) = 0;
    virtual ~IUSBDevice() = default;
};

// Interface 2
class IHDMIDevice {
public:
    virtual void sendSignal(const string& signal) = 0;
    virtual ~IHDMIDevice() = default;
};

// USB device
class USBKeyboard : public IUSBDevice {
public:
    void transferData(const string& data) override {
        cout << "USB Keyboard sending: " << data << endl;
    }
};

// HDMI device
class HDMIMonitor : public IHDMIDevice {
public:
    void sendSignal(const string& signal) override {
        cout << "HDMI Monitor displaying: " << signal << endl;
    }
};

// Two-way Adapter: USB to HDMI and HDMI to USB
class USBToHDMIAdapter : public IHDMIDevice, public IUSBDevice {
private:
    IUSBDevice* usbDevice;
    IHDMIDevice* hdmiDevice;
    
public:
    USBToHDMIAdapter(IUSBDevice* usb) : usbDevice(usb), hdmiDevice(nullptr) {}
    USBToHDMIAdapter(IHDMIDevice* hdmi) : usbDevice(nullptr), hdmiDevice(hdmi) {}
    
    // As HDMI device (receiving from USB)
    void sendSignal(const string& signal) override {
        if (usbDevice) {
            cout << "USB->HDMI Adapter converting signal: " << signal << endl;
            usbDevice->transferData(signal);
        } else {
            cout << "No USB device connected!" << endl;
        }
    }
    
    // As USB device (receiving from HDMI)
    void transferData(const string& data) override {
        if (hdmiDevice) {
            cout << "HDMI->USB Adapter converting data: " << data << endl;
            hdmiDevice->sendSignal(data);
        } else {
            cout << "No HDMI device connected!" << endl;
        }
    }
};

int main() {
    cout << "=== Two-Way Adapter ===" << endl;
    
    USBKeyboard keyboard;
    HDMIMonitor monitor;
    
    // USB to HDMI conversion
    USBToHDMIAdapter usbToHdmi(&keyboard);
    cout << "\n1. USB to HDMI:" << endl;
    usbToHdmi.sendSignal("Hello Monitor");
    
    // HDMI to USB conversion
    USBToHDMIAdapter hdmiToUsb(&monitor);
    cout << "\n2. HDMI to USB:" << endl;
    hdmiToUsb.transferData("Hello Keyboard");
    
    return 0;
}
```

---

## 4. **Adapter with Data Conversion**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cmath>
using namespace std;

// Target interface (XML format)
class IXMLParser {
public:
    virtual string toXML(const string& data) = 0;
    virtual string fromXML(const string& xml) = 0;
    virtual ~IXMLParser() = default;
};

// Adaptee (JSON format)
class JSONParser {
public:
    string toJSON(const string& data) {
        // Simulate JSON conversion
        return "{ \"data\": \"" + data + "\" }";
    }
    
    string fromJSON(const string& json) {
        // Simulate parsing JSON
        size_t start = json.find("\"data\": \"") + 9;
        size_t end = json.find("\"", start);
        return json.substr(start, end - start);
    }
};

// Adaptee (CSV format)
class CSVParser {
private:
    vector<vector<string>> data;
    
public:
    string toCSV(const vector<string>& row) {
        stringstream ss;
        for (size_t i = 0; i < row.size(); i++) {
            if (i > 0) ss << ",";
            ss << row[i];
        }
        return ss.str();
    }
    
    vector<string> fromCSV(const string& csv) {
        vector<string> row;
        stringstream ss(csv);
        string item;
        while (getline(ss, item, ',')) {
            row.push_back(item);
        }
        return row;
    }
};

// Adapter for JSON
class JSONAdapter : public IXMLParser {
private:
    JSONParser parser;
    
public:
    string toXML(const string& data) override {
        string json = parser.toJSON(data);
        // Convert JSON to XML (simplified)
        return "<data>" + data + "</data>";
    }
    
    string fromXML(const string& xml) override {
        // Extract data from XML
        size_t start = xml.find("<data>") + 6;
        size_t end = xml.find("</data>");
        string data = xml.substr(start, end - start);
        // Convert to JSON then parse
        return parser.fromJSON(parser.toJSON(data));
    }
};

// Adapter for CSV with data conversion
class CSVAdapter : public IXMLParser {
private:
    CSVParser parser;
    
public:
    string toXML(const string& data) override {
        // Convert data to CSV row format
        vector<string> row;
        row.push_back(data);
        string csv = parser.toCSV(row);
        return "<data>" + data + "</data>";
    }
    
    string fromXML(const string& xml) override {
        size_t start = xml.find("<data>") + 6;
        size_t end = xml.find("</data>");
        string data = xml.substr(start, end - start);
        
        // Convert to CSV row
        vector<string> row;
        row.push_back(data);
        return parser.fromCSV(parser.toCSV(row))[0];
    }
};

int main() {
    cout << "=== Adapter with Data Conversion ===" << endl;
    
    JSONAdapter jsonAdapter;
    CSVAdapter csvAdapter;
    
    string originalData = "Hello World";
    
    cout << "\n1. JSON Adapter:" << endl;
    string jsonXML = jsonAdapter.toXML(originalData);
    cout << "XML: " << jsonXML << endl;
    string recoveredData = jsonAdapter.fromXML(jsonXML);
    cout << "Recovered: " << recoveredData << endl;
    
    cout << "\n2. CSV Adapter:" << endl;
    string csvXML = csvAdapter.toXML(originalData);
    cout << "XML: " << csvXML << endl;
    recoveredData = csvAdapter.fromXML(csvXML);
    cout << "Recovered: " << recoveredData << endl;
    
    return 0;
}
```

---

## 5. **Practical Example: Payment Gateway Integration**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <map>
#include <vector>
using namespace std;

// Target interface (our payment system)
class IPaymentProcessor {
public:
    virtual bool processPayment(double amount, const string& currency) = 0;
    virtual bool refundPayment(const string& transactionId, double amount) = 0;
    virtual string getStatus(const string& transactionId) = 0;
    virtual ~IPaymentProcessor() = default;
};

// Adaptee 1: PayPal API
class PayPalAPI {
private:
    map<string, double> transactions;
    int nextId;
    
public:
    PayPalAPI() : nextId(1000) {}
    
    bool makePayment(double amount, string currency) {
        string id = "PP" + to_string(nextId++);
        transactions[id] = amount;
        cout << "[PayPal] Payment of " << amount << " " << currency 
             << " processed. Transaction ID: " << id << endl;
        return true;
    }
    
    bool issueRefund(string transactionId, double amount) {
        if (transactions.find(transactionId) != transactions.end()) {
            cout << "[PayPal] Refund of " << amount << " issued for " << transactionId << endl;
            return true;
        }
        return false;
    }
    
    string checkStatus(string transactionId) {
        if (transactions.find(transactionId) != transactions.end()) {
            return "COMPLETED";
        }
        return "NOT_FOUND";
    }
};

// Adaptee 2: Stripe API
class StripeAPI {
private:
    struct Transaction {
        double amount;
        string currency;
        string status;
    };
    map<string, Transaction> transactions;
    int nextId;
    
public:
    StripeAPI() : nextId(2000) {}
    
    string createCharge(double amount, string currency) {
        string id = "STR" + to_string(nextId++);
        transactions[id] = {amount, currency, "succeeded"};
        cout << "[Stripe] Charge of " << amount << " " << currency 
             << " created. ID: " << id << endl;
        return id;
    }
    
    bool createRefund(string chargeId, double amount) {
        if (transactions.find(chargeId) != transactions.end()) {
            transactions[chargeId].status = "refunded";
            cout << "[Stripe] Refund of " << amount << " processed for " << chargeId << endl;
            return true;
        }
        return false;
    }
    
    string retrieveCharge(string chargeId) {
        if (transactions.find(chargeId) != transactions.end()) {
            return transactions[chargeId].status;
        }
        return "not_found";
    }
};

// Adaptee 3: Bank Transfer API
class BankAPI {
private:
    vector<string> transactions;
    int nextRef;
    
public:
    BankAPI() : nextRef(3000) {}
    
    string initiateTransfer(double amount, string account) {
        string ref = "BANK" + to_string(nextRef++);
        transactions.push_back(ref);
        cout << "[Bank] Transfer of " << amount << " to account " << account 
             << " initiated. Reference: " << ref << endl;
        return ref;
    }
    
    bool cancelTransfer(string reference) {
        auto it = find(transactions.begin(), transactions.end(), reference);
        if (it != transactions.end()) {
            cout << "[Bank] Transfer " << reference << " cancelled" << endl;
            return true;
        }
        return false;
    }
    
    string getTransferStatus(string reference) {
        auto it = find(transactions.begin(), transactions.end(), reference);
        if (it != transactions.end()) {
            return "PROCESSING";
        }
        return "NOT_FOUND";
    }
};

// PayPal Adapter
class PayPalAdapter : public IPaymentProcessor {
private:
    unique_ptr<PayPalAPI> paypal;
    map<string, double> transactions;
    
public:
    PayPalAdapter() : paypal(make_unique<PayPalAPI>()) {}
    
    bool processPayment(double amount, const string& currency) override {
        return paypal->makePayment(amount, currency);
    }
    
    bool refundPayment(const string& transactionId, double amount) override {
        return paypal->issueRefund(transactionId, amount);
    }
    
    string getStatus(const string& transactionId) override {
        return paypal->checkStatus(transactionId);
    }
};

// Stripe Adapter
class StripeAdapter : public IPaymentProcessor {
private:
    unique_ptr<StripeAPI> stripe;
    map<string, string> chargeIds;
    int nextId;
    
public:
    StripeAdapter() : stripe(make_unique<StripeAPI>()), nextId(5000) {}
    
    bool processPayment(double amount, const string& currency) override {
        string chargeId = stripe->createCharge(amount, currency);
        string ourId = "TXN" + to_string(nextId++);
        chargeIds[ourId] = chargeId;
        return true;
    }
    
    bool refundPayment(const string& transactionId, double amount) override {
        auto it = chargeIds.find(transactionId);
        if (it != chargeIds.end()) {
            return stripe->createRefund(it->second, amount);
        }
        return false;
    }
    
    string getStatus(const string& transactionId) override {
        auto it = chargeIds.find(transactionId);
        if (it != chargeIds.end()) {
            string status = stripe->retrieveCharge(it->second);
            if (status == "succeeded") return "COMPLETED";
            if (status == "refunded") return "REFUNDED";
        }
        return "NOT_FOUND";
    }
};

// Bank Adapter
class BankAdapter : public IPaymentProcessor {
private:
    unique_ptr<BankAPI> bank;
    map<string, string> references;
    int nextId;
    
public:
    BankAdapter() : bank(make_unique<BankAPI>()), nextId(7000) {}
    
    bool processPayment(double amount, const string& currency) override {
        string ref = bank->initiateTransfer(amount, "ACC123456");
        string ourId = "TXN" + to_string(nextId++);
        references[ourId] = ref;
        return true;
    }
    
    bool refundPayment(const string& transactionId, double amount) override {
        auto it = references.find(transactionId);
        if (it != references.end()) {
            return bank->cancelTransfer(it->second);
        }
        return false;
    }
    
    string getStatus(const string& transactionId) override {
        auto it = references.find(transactionId);
        if (it != references.end()) {
            string status = bank->getTransferStatus(it->second);
            if (status == "PROCESSING") return "PENDING";
            if (status == "COMPLETED") return "COMPLETED";
        }
        return "NOT_FOUND";
    }
};

class PaymentGateway {
private:
    unique_ptr<IPaymentProcessor> processor;
    
public:
    void setProcessor(IPaymentProcessor* p) {
        processor.reset(p);
    }
    
    bool pay(double amount, const string& currency) {
        if (!processor) return false;
        return processor->processPayment(amount, currency);
    }
    
    bool refund(const string& transactionId, double amount) {
        if (!processor) return false;
        return processor->refundPayment(transactionId, amount);
    }
    
    string getStatus(const string& transactionId) {
        if (!processor) return "NO_PROCESSOR";
        return processor->getStatus(transactionId);
    }
};

int main() {
    cout << "=== Payment Gateway Integration with Adapter ===" << endl;
    
    PaymentGateway gateway;
    
    cout << "\n1. Using PayPal:" << endl;
    gateway.setProcessor(new PayPalAdapter());
    gateway.pay(99.99, "USD");
    
    cout << "\n2. Using Stripe:" << endl;
    gateway.setProcessor(new StripeAdapter());
    gateway.pay(149.99, "EUR");
    
    cout << "\n3. Using Bank Transfer:" << endl;
    gateway.setProcessor(new BankAdapter());
    gateway.pay(500.00, "GBP");
    
    cout << "\n4. Checking status (Stripe):" << endl;
    gateway.setProcessor(new StripeAdapter());
    gateway.pay(75.50, "USD");
    
    return 0;
}
```

---

## 📊 Adapter Pattern Summary

| Type | Description | Pros | Cons |
|------|-------------|------|------|
| **Object Adapter** | Uses composition | Flexible, works with adaptee subclasses | Slightly more code |
| **Class Adapter** | Uses multiple inheritance | Simpler, can override adaptee behavior | Requires multiple inheritance |

---

## ✅ Best Practices

1. **Prefer object adapter** over class adapter (composition over inheritance)
2. **Use adapter pattern** when integrating third-party libraries
3. **Keep adapter simple** - only convert interface, don't add logic
4. **Document the conversion** clearly for maintenance
5. **Consider using multiple adapters** for different adaptees

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Adding business logic** | Adapter becomes complex | Keep adapter focused on interface conversion |
| **Performance overhead** | Multiple conversions | Cache converted data if needed |
| **Error handling** | Lost error information | Preserve error details during conversion |

---

## ✅ Key Takeaways

1. **Adapter pattern** converts incompatible interfaces
2. **Object adapter** uses composition (preferred)
3. **Class adapter** uses multiple inheritance
4. **Useful for** integrating legacy code and third-party libraries
5. **Promotes** reusability and maintainability
6. **Follows** Open/Closed Principle - add adapters without changing existing code

---