# Facade Pattern in C++ - Complete Guide

## 📖 Overview

The Facade pattern provides a simplified interface to a complex subsystem. It hides the complexities of the system and provides a unified, higher-level interface that makes the subsystem easier to use. This pattern is particularly useful for legacy systems or complex libraries where you want to provide a simpler interface for common use cases.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Facade** | Simplified interface to a complex subsystem |
| **Subsystem** | Collection of classes with complex interactions |
| **Client** | Uses the facade instead of interacting with subsystem directly |
| **Decoupling** | Reduces dependencies between client and subsystem |

---

## 1. **Basic Facade Pattern**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// Subsystem classes
class CPU {
public:
    void start() {
        cout << "CPU: Starting..." << endl;
    }
    
    void execute() {
        cout << "CPU: Executing instructions..." << endl;
    }
    
    void shutdown() {
        cout << "CPU: Shutting down..." << endl;
    }
};

class Memory {
public:
    void load() {
        cout << "Memory: Loading data..." << endl;
    }
    
    void clear() {
        cout << "Memory: Clearing..." << endl;
    }
};

class HardDrive {
public:
    void read() {
        cout << "HardDrive: Reading data..." << endl;
    }
    
    void write() {
        cout << "HardDrive: Writing data..." << endl;
    }
};

class GraphicsCard {
public:
    void initialize() {
        cout << "GraphicsCard: Initializing..." << endl;
    }
    
    void render() {
        cout << "GraphicsCard: Rendering..." << endl;
    }
};

class NetworkCard {
public:
    void connect() {
        cout << "NetworkCard: Connecting..." << endl;
    }
    
    void disconnect() {
        cout << "NetworkCard: Disconnecting..." << endl;
    }
};

// Facade
class ComputerFacade {
private:
    unique_ptr<CPU> cpu;
    unique_ptr<Memory> memory;
    unique_ptr<HardDrive> hardDrive;
    unique_ptr<GraphicsCard> graphicsCard;
    unique_ptr<NetworkCard> networkCard;
    
public:
    ComputerFacade() {
        cpu = make_unique<CPU>();
        memory = make_unique<Memory>();
        hardDrive = make_unique<HardDrive>();
        graphicsCard = make_unique<GraphicsCard>();
        networkCard = make_unique<NetworkCard>();
    }
    
    void start() {
        cout << "\n=== Starting Computer ===" << endl;
        cpu->start();
        memory->load();
        hardDrive->read();
        graphicsCard->initialize();
        networkCard->connect();
        cpu->execute();
        graphicsCard->render();
        cout << "Computer ready!" << endl;
    }
    
    void shutdown() {
        cout << "\n=== Shutting Down Computer ===" << endl;
        cpu->shutdown();
        memory->clear();
        hardDrive->write();
        networkCard->disconnect();
        cout << "Computer off!" << endl;
    }
};

int main() {
    cout << "=== Basic Facade Pattern ===" << endl;
    
    ComputerFacade computer;
    computer.start();
    computer.shutdown();
    
    return 0;
}
```

**Output:**
```
=== Basic Facade Pattern ===

=== Starting Computer ===
CPU: Starting...
Memory: Loading data...
HardDrive: Reading data...
GraphicsCard: Initializing...
NetworkCard: Connecting...
CPU: Executing instructions...
GraphicsCard: Rendering...
Computer ready!

=== Shutting Down Computer ===
CPU: Shutting down...
Memory: Clearing...
HardDrive: Writing data...
NetworkCard: Disconnecting...
Computer off!
```

---

## 2. **Home Theater Facade**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <vector>
using namespace std;

// Subsystem classes
class Amplifier {
public:
    void on() { cout << "Amplifier: ON" << endl; }
    void off() { cout << "Amplifier: OFF" << endl; }
    void setVolume(int level) { cout << "Amplifier: Volume set to " << level << endl; }
    void setSurroundSound() { cout << "Amplifier: Surround sound ON" << endl; }
};

class DVDPlayer {
public:
    void on() { cout << "DVD Player: ON" << endl; }
    void off() { cout << "DVD Player: OFF" << endl; }
    void play(const string& movie) { cout << "DVD Player: Playing '" << movie << "'" << endl; }
    void pause() { cout << "DVD Player: Paused" << endl; }
    void stop() { cout << "DVD Player: Stopped" << endl; }
    void eject() { cout << "DVD Player: Ejecting disc" << endl; }
};

class Projector {
public:
    void on() { cout << "Projector: ON" << endl; }
    void off() { cout << "Projector: OFF" << endl; }
    void wideScreenMode() { cout << "Projector: Widescreen mode ON" << endl; }
    void setInput(const string& input) { cout << "Projector: Input set to " << input << endl; }
};

class Screen {
public:
    void down() { cout << "Screen: Lowered" << endl; }
    void up() { cout << "Screen: Raised" << endl; }
};

class Lights {
public:
    void dim(int level) { cout << "Lights: Dimmed to " << level << "%" << endl; }
    void on() { cout << "Lights: ON" << endl; }
};

class PopcornPopper {
public:
    void on() { cout << "Popcorn Popper: ON" << endl; }
    void off() { cout << "Popcorn Popper: OFF" << endl; }
    void pop() { cout << "Popcorn Popper: Popping popcorn!" << endl; }
};

// Facade
class HomeTheaterFacade {
private:
    unique_ptr<Amplifier> amp;
    unique_ptr<DVDPlayer> dvd;
    unique_ptr<Projector> projector;
    unique_ptr<Screen> screen;
    unique_ptr<Lights> lights;
    unique_ptr<PopcornPopper> popper;
    
public:
    HomeTheaterFacade() {
        amp = make_unique<Amplifier>();
        dvd = make_unique<DVDPlayer>();
        projector = make_unique<Projector>();
        screen = make_unique<Screen>();
        lights = make_unique<Lights>();
        popper = make_unique<PopcornPopper>();
    }
    
    void watchMovie(const string& movie) {
        cout << "\n=== Getting ready to watch a movie ===" << endl;
        popper->on();
        popper->pop();
        lights->dim(10);
        screen->down();
        projector->on();
        projector->wideScreenMode();
        projector->setInput("DVD");
        amp->on();
        amp->setSurroundSound();
        amp->setVolume(30);
        dvd->on();
        dvd->play(movie);
        cout << "Movie started! Enjoy!" << endl;
    }
    
    void endMovie() {
        cout << "\n=== Ending movie ===" << endl;
        dvd->stop();
        dvd->eject();
        dvd->off();
        amp->off();
        projector->off();
        screen->up();
        lights->on();
        popper->off();
        cout << "Movie ended!" << endl;
    }
};

int main() {
    cout << "=== Home Theater Facade ===" << endl;
    
    HomeTheaterFacade homeTheater;
    homeTheater.watchMovie("The Matrix");
    homeTheater.endMovie();
    
    return 0;
}
```

---

## 3. **Banking System Facade**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <map>
#include <random>
using namespace std;

// Subsystem classes
class AccountService {
private:
    map<string, double> accounts;
    map<string, string> pins;
    
public:
    AccountService() {
        accounts["123456"] = 1000.0;
        accounts["654321"] = 500.0;
        pins["123456"] = "1234";
        pins["654321"] = "5678";
    }
    
    bool accountExists(const string& accountNumber) {
        return accounts.find(accountNumber) != accounts.end();
    }
    
    bool validatePin(const string& accountNumber, const string& pin) {
        auto it = pins.find(accountNumber);
        return it != pins.end() && it->second == pin;
    }
    
    double getBalance(const string& accountNumber) {
        auto it = accounts.find(accountNumber);
        return it != accounts.end() ? it->second : 0;
    }
    
    void updateBalance(const string& accountNumber, double amount) {
        accounts[accountNumber] += amount;
        cout << "Account " << accountNumber << " balance updated to $" 
             << accounts[accountNumber] << endl;
    }
};

class FraudDetectionService {
private:
    bool checkFraud(const string& accountNumber, double amount) {
        // Simulate fraud detection
        if (amount > 10000) {
            cout << "Fraud detection: Large transaction flagged!" << endl;
            return false;
        }
        return true;
    }
    
public:
    bool isTransactionSafe(const string& accountNumber, double amount) {
        return checkFraud(accountNumber, amount);
    }
};

class NotificationService {
public:
    void sendSMS(const string& phone, const string& message) {
        cout << "SMS to " << phone << ": " << message << endl;
    }
    
    void sendEmail(const string& email, const string& message) {
        cout << "Email to " << email << ": " << message << endl;
    }
};

class TransactionLogger {
private:
    vector<string> logs;
    
public:
    void logTransaction(const string& accountNumber, double amount, bool success) {
        string log = "Account: " + accountNumber + 
                     ", Amount: $" + to_string(amount) +
                     ", Status: " + (success ? "SUCCESS" : "FAILED");
        logs.push_back(log);
        cout << "Transaction logged: " << log << endl;
    }
    
    void showLogs() {
        cout << "\n=== Transaction Logs ===" << endl;
        for (const auto& log : logs) {
            cout << "  " << log << endl;
        }
    }
};

// Facade
class BankingFacade {
private:
    unique_ptr<AccountService> accountService;
    unique_ptr<FraudDetectionService> fraudService;
    unique_ptr<NotificationService> notificationService;
    unique_ptr<TransactionLogger> logger;
    
public:
    BankingFacade() {
        accountService = make_unique<AccountService>();
        fraudService = make_unique<FraudDetectionService>();
        notificationService = make_unique<NotificationService>();
        logger = make_unique<TransactionLogger>();
    }
    
    bool withdraw(const string& accountNumber, const string& pin, double amount) {
        cout << "\n--- Withdrawal Request ---" << endl;
        
        // Validate account
        if (!accountService->accountExists(accountNumber)) {
            cout << "Error: Account not found!" << endl;
            logger->logTransaction(accountNumber, amount, false);
            return false;
        }
        
        // Validate PIN
        if (!accountService->validatePin(accountNumber, pin)) {
            cout << "Error: Invalid PIN!" << endl;
            logger->logTransaction(accountNumber, amount, false);
            return false;
        }
        
        // Check fraud
        if (!fraudService->isTransactionSafe(accountNumber, amount)) {
            cout << "Error: Transaction flagged as fraudulent!" << endl;
            logger->logTransaction(accountNumber, amount, false);
            return false;
        }
        
        // Check balance
        double balance = accountService->getBalance(accountNumber);
        if (balance < amount) {
            cout << "Error: Insufficient funds!" << endl;
            logger->logTransaction(accountNumber, amount, false);
            return false;
        }
        
        // Process withdrawal
        accountService->updateBalance(accountNumber, -amount);
        notificationService->sendSMS("555-1234", "Withdrawal of $" + to_string(amount) + " processed");
        notificationService->sendEmail("customer@example.com", "Withdrawal of $" + to_string(amount) + " completed");
        logger->logTransaction(accountNumber, amount, true);
        
        cout << "Withdrawal successful!" << endl;
        return true;
    }
    
    double checkBalance(const string& accountNumber, const string& pin) {
        cout << "\n--- Balance Check ---" << endl;
        
        if (!accountService->accountExists(accountNumber)) {
            cout << "Error: Account not found!" << endl;
            return -1;
        }
        
        if (!accountService->validatePin(accountNumber, pin)) {
            cout << "Error: Invalid PIN!" << endl;
            return -1;
        }
        
        double balance = accountService->getBalance(accountNumber);
        cout << "Current balance: $" << balance << endl;
        return balance;
    }
    
    void showTransactionLogs() {
        logger->showLogs();
    }
};

int main() {
    cout << "=== Banking System Facade ===" << endl;
    
    BankingFacade bank;
    
    // Check balance
    bank.checkBalance("123456", "1234");
    
    // Withdraw money
    bank.withdraw("123456", "1234", 200);
    
    // Check balance again
    bank.checkBalance("123456", "1234");
    
    // Attempt large withdrawal (fraud detection)
    bank.withdraw("123456", "1234", 15000);
    
    // Attempt withdrawal from invalid account
    bank.withdraw("999999", "0000", 100);
    
    // Attempt withdrawal with wrong PIN
    bank.withdraw("123456", "9999", 100);
    
    // Show all transaction logs
    bank.showTransactionLogs();
    
    return 0;
}
```

---

## 4. **Compiler Facade**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <fstream>
#include <sstream>
using namespace std;

// Subsystem classes
class Scanner {
public:
    vector<string> scan(const string& sourceCode) {
        cout << "Scanner: Tokenizing source code..." << endl;
        vector<string> tokens;
        stringstream ss(sourceCode);
        string token;
        while (ss >> token) {
            tokens.push_back(token);
        }
        cout << "Scanner: Found " << tokens.size() << " tokens" << endl;
        return tokens;
    }
};

class Parser {
public:
    void parse(const vector<string>& tokens) {
        cout << "Parser: Building AST from " << tokens.size() << " tokens..." << endl;
        // Simulate parsing
        cout << "Parser: AST built successfully" << endl;
    }
};

class SemanticAnalyzer {
public:
    void analyze() {
        cout << "SemanticAnalyzer: Performing semantic analysis..." << endl;
        cout << "SemanticAnalyzer: No errors found" << endl;
    }
};

class CodeGenerator {
public:
    void generate() {
        cout << "CodeGenerator: Generating machine code..." << endl;
        cout << "CodeGenerator: Code generation complete" << endl;
    }
};

class Optimizer {
public:
    void optimize() {
        cout << "Optimizer: Optimizing generated code..." << endl;
        cout << "Optimizer: Optimization complete" << endl;
    }
};

class Linker {
public:
    void link() {
        cout << "Linker: Linking object files..." << endl;
        cout << "Linker: Executable created" << endl;
    }
};

// Facade
class CompilerFacade {
private:
    unique_ptr<Scanner> scanner;
    unique_ptr<Parser> parser;
    unique_ptr<SemanticAnalyzer> semanticAnalyzer;
    unique_ptr<CodeGenerator> codeGenerator;
    unique_ptr<Optimizer> optimizer;
    unique_ptr<Linker> linker;
    
public:
    CompilerFacade() {
        scanner = make_unique<Scanner>();
        parser = make_unique<Parser>();
        semanticAnalyzer = make_unique<SemanticAnalyzer>();
        codeGenerator = make_unique<CodeGenerator>();
        optimizer = make_unique<Optimizer>();
        linker = make_unique<Linker>();
    }
    
    void compile(const string& sourceCode) {
        cout << "\n=== Compilation Process ===" << endl;
        
        vector<string> tokens = scanner->scan(sourceCode);
        
        if (tokens.empty()) {
            cout << "Error: No tokens found!" << endl;
            return;
        }
        
        parser->parse(tokens);
        semanticAnalyzer->analyze();
        codeGenerator->generate();
        optimizer->optimize();
        linker->link();
        
        cout << "Compilation successful!" << endl;
    }
    
    void quickCompile(const string& sourceCode) {
        cout << "\n=== Quick Compilation (No optimization) ===" << endl;
        
        vector<string> tokens = scanner->scan(sourceCode);
        
        if (tokens.empty()) {
            cout << "Error: No tokens found!" << endl;
            return;
        }
        
        parser->parse(tokens);
        semanticAnalyzer->analyze();
        codeGenerator->generate();
        linker->link();
        
        cout << "Quick compilation successful!" << endl;
    }
    
    void compileAndRun(const string& sourceCode) {
        compile(sourceCode);
        cout << "Running executable..." << endl;
        cout << "Output: Hello from compiled program!" << endl;
    }
};

int main() {
    cout << "=== Compiler Facade ===" << endl;
    
    CompilerFacade compiler;
    string sourceCode = "int main() { return 0; }";
    
    cout << "\n1. Full compilation with optimization:" << endl;
    compiler.compile(sourceCode);
    
    cout << "\n2. Quick compilation (no optimization):" << endl;
    compiler.quickCompile(sourceCode);
    
    cout << "\n3. Compile and run:" << endl;
    compiler.compileAndRun(sourceCode);
    
    return 0;
}
```

---

## 5. **Practical Example: E-commerce System**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <map>
#include <random>
using namespace std;

// Subsystem classes
class InventoryService {
private:
    map<string, int> stock;
    
public:
    InventoryService() {
        stock["Laptop"] = 10;
        stock["Mouse"] = 50;
        stock["Keyboard"] = 30;
        stock["Monitor"] = 5;
    }
    
    bool checkStock(const string& product, int quantity) {
        auto it = stock.find(product);
        return it != stock.end() && it->second >= quantity;
    }
    
    void reserveStock(const string& product, int quantity) {
        stock[product] -= quantity;
        cout << "Inventory: Reserved " << quantity << " " << product << "(s)" << endl;
    }
    
    void releaseStock(const string& product, int quantity) {
        stock[product] += quantity;
        cout << "Inventory: Released " << quantity << " " << product << "(s)" << endl;
    }
};

class PaymentService {
private:
    bool processPayment(const string& cardNumber, double amount) {
        // Simulate payment processing
        cout << "Payment: Processing $" << amount << " from card " << cardNumber << endl;
        return true; // Assume success
    }
    
public:
    bool charge(const string& cardNumber, double amount) {
        if (processPayment(cardNumber, amount)) {
            cout << "Payment: $" << amount << " charged successfully" << endl;
            return true;
        }
        cout << "Payment: Failed!" << endl;
        return false;
    }
    
    void refund(const string& cardNumber, double amount) {
        cout << "Payment: $" << amount << " refunded to card " << cardNumber << endl;
    }
};

class ShippingService {
private:
    string generateTrackingNumber() {
        static int counter = 1000;
        return "TRK" + to_string(counter++);
    }
    
public:
    string createShipment(const string& address, const vector<pair<string, int>>& items) {
        cout << "Shipping: Creating shipment to " << address << endl;
        for (const auto& item : items) {
            cout << "  " << item.second << "x " << item.first << endl;
        }
        string tracking = generateTrackingNumber();
        cout << "Shipping: Tracking number: " << tracking << endl;
        return tracking;
    }
    
    void cancelShipment(const string& tracking) {
        cout << "Shipping: Cancelled shipment " << tracking << endl;
    }
};

class EmailService {
public:
    void sendOrderConfirmation(const string& email, const string& orderId) {
        cout << "Email: Order confirmation sent to " << email 
             << " for order " << orderId << endl;
    }
    
    void sendShippingConfirmation(const string& email, const string& tracking) {
        cout << "Email: Shipping confirmation sent to " << email 
             << " with tracking " << tracking << endl;
    }
    
    void sendOrderCancellation(const string& email, const string& orderId) {
        cout << "Email: Order cancellation sent to " << email 
             << " for order " << orderId << endl;
    }
};

// Facade
class OrderProcessor {
private:
    unique_ptr<InventoryService> inventory;
    unique_ptr<PaymentService> payment;
    unique_ptr<ShippingService> shipping;
    unique_ptr<EmailService> email;
    static int orderCounter;
    
    struct Order {
        int id;
        string product;
        int quantity;
        double amount;
        string status;
        string tracking;
    };
    vector<Order> orders;
    
public:
    OrderProcessor() {
        inventory = make_unique<InventoryService>();
        payment = make_unique<PaymentService>();
        shipping = make_unique<ShippingService>();
        email = make_unique<EmailService>();
    }
    
    string placeOrder(const string& product, int quantity, 
                      const string& cardNumber, const string& address,
                      const string& customerEmail) {
        int orderId = ++orderCounter;
        string orderIdStr = "ORD" + to_string(orderId);
        
        cout << "\n=== Processing Order " << orderIdStr << " ===" << endl;
        
        // Check inventory
        if (!inventory->checkStock(product, quantity)) {
            cout << "Order failed: Insufficient stock!" << endl;
            return "";
        }
        
        // Calculate amount
        double amount = quantity * getProductPrice(product);
        
        // Process payment
        if (!payment->charge(cardNumber, amount)) {
            cout << "Order failed: Payment declined!" << endl;
            return "";
        }
        
        // Reserve inventory
        inventory->reserveStock(product, quantity);
        
        // Create shipment
        vector<pair<string, int>> items = {{product, quantity}};
        string tracking = shipping->createShipment(address, items);
        
        // Send confirmation email
        email->sendOrderConfirmation(customerEmail, orderIdStr);
        email->sendShippingConfirmation(customerEmail, tracking);
        
        // Store order
        orders.push_back({orderId, product, quantity, amount, "Completed", tracking});
        
        cout << "Order " << orderIdStr << " completed successfully!" << endl;
        return orderIdStr;
    }
    
    void cancelOrder(const string& orderIdStr) {
        int orderId = stoi(orderIdStr.substr(3));
        
        cout << "\n=== Cancelling Order " << orderIdStr << " ===" << endl;
        
        for (auto& order : orders) {
            if (order.id == orderId && order.status != "Cancelled") {
                // Release inventory
                inventory->releaseStock(order.product, order.quantity);
                
                // Refund payment
                payment->refund("****", order.amount);
                
                // Cancel shipment
                if (!order.tracking.empty()) {
                    shipping->cancelShipment(order.tracking);
                }
                
                // Send cancellation email
                email->sendOrderCancellation("customer@example.com", orderIdStr);
                
                order.status = "Cancelled";
                cout << "Order " << orderIdStr << " cancelled successfully!" << endl;
                return;
            }
        }
        
        cout << "Order not found or already cancelled!" << endl;
    }
    
    void checkOrderStatus(const string& orderIdStr) {
        int orderId = stoi(orderIdStr.substr(3));
        
        for (const auto& order : orders) {
            if (order.id == orderId) {
                cout << "\nOrder " << orderIdStr << " Status: " << order.status << endl;
                if (!order.tracking.empty()) {
                    cout << "Tracking: " << order.tracking << endl;
                }
                return;
            }
        }
        
        cout << "Order not found!" << endl;
    }
    
private:
    double getProductPrice(const string& product) {
        if (product == "Laptop") return 999.99;
        if (product == "Mouse") return 29.99;
        if (product == "Keyboard") return 79.99;
        if (product == "Monitor") return 299.99;
        return 0;
    }
};

int OrderProcessor::orderCounter = 0;

int main() {
    cout << "=== E-commerce System Facade ===" << endl;
    
    OrderProcessor orderProcessor;
    
    // Place orders
    string order1 = orderProcessor.placeOrder("Laptop", 1, "4111-1111-1111-1111", 
                                               "123 Main St, NY", "customer@example.com");
    string order2 = orderProcessor.placeOrder("Mouse", 2, "4111-1111-1111-1111", 
                                               "456 Oak Ave, CA", "customer@example.com");
    string order3 = orderProcessor.placeOrder("Keyboard", 1, "4111-1111-1111-1111", 
                                               "789 Pine Rd, TX", "customer@example.com");
    
    // Check order status
    orderProcessor.checkOrderStatus(order1);
    orderProcessor.checkOrderStatus(order2);
    
    // Cancel an order
    orderProcessor.cancelOrder(order2);
    
    // Check status after cancellation
    orderProcessor.checkOrderStatus(order2);
    
    return 0;
}
```

---

## 📊 Facade Pattern Summary

| Component | Description |
|-----------|-------------|
| **Facade** | Simplified interface to the subsystem |
| **Subsystem** | Complex set of classes with their own interfaces |
| **Client** | Uses the facade instead of interacting with subsystem directly |

---

## ✅ Best Practices

1. **Use Facade** to simplify complex subsystems
2. **Keep facade focused** on common use cases
3. **Don't hide all functionality** - allow direct access to subsystem when needed
4. **Use multiple facades** for different client needs
5. **Decouple** clients from subsystem changes

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **God facade** | Does too much | Split into multiple facades |
| **Hiding necessary functionality** | Clients need direct access | Allow access to subsystem |
| **Tight coupling** | Changes affect facade | Keep facade thin |

---

## ✅ Key Takeaways

1. **Facade pattern** provides a simplified interface
2. **Reduces complexity** for clients
3. **Decouples** clients from subsystem
4. **Useful for** legacy systems, complex libraries
5. **Does not hide** subsystem - clients can still use it directly
6. **Follows** Law of Demeter (principle of least knowledge)

---
---

## Next Step

- Go to [Flyweight.md](Flyweight.md) to continue with Flyweight.
