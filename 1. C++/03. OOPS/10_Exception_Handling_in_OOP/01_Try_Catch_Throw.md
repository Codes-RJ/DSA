# Try, Catch, and Throw

## 📖 Overview

The try-catch-throw mechanism is the foundation of exception handling in C++. It provides a structured way to handle errors and exceptional conditions that disrupt the normal flow of program execution. This trio of keywords enables robust error handling while keeping code clean and maintainable.

---

## 🎯 Key Concepts

- **try Block**: Encloses code that might throw exceptions
- **throw Statement**: Raises an exception when an error occurs
- **catch Block**: Handles specific types of exceptions
- **Exception Propagation**: The process of searching for handlers
- **Stack Unwinding**: Automatic cleanup during exception propagation

---

## 💻 Basic Syntax

```cpp
try {
    // Code that might throw an exception
    if (error_condition) {
        throw exception_object;
    }
} catch (ExceptionType& e) {
    // Handle the exception
} catch (...) {
    // Handle any other exception
}
```

---

## 🔍 Detailed Explanation

### 1. **Basic Try-Catch Structure**

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;

// Function that demonstrates basic exception throwing
void divideNumbers(double a, double b) {
    cout << "Attempting to divide " << a << " by " << b << endl;
    
    if (b == 0.0) {
        throw runtime_error("Division by zero is not allowed!");
    }
    
    double result = a / b;
    cout << "Result: " << result << endl;
}

// Function with multiple possible exceptions
void processAge(int age) {
    cout << "Processing age: " << age << endl;
    
    if (age < 0) {
        throw invalid_argument("Age cannot be negative");
    } else if (age > 150) {
        throw out_of_range("Age seems unrealistic (over 150)");
    } else if (age < 18) {
        throw domain_error("User must be at least 18 years old");
    }
    
    cout << "Age " << age << " is valid" << endl;
}

int main() {
    cout << "=== Basic Try-Catch Structure ===" << endl;
    
    // Example 1: Successful operation
    cout << "\nExample 1: Successful division" << endl;
    try {
        divideNumbers(10.0, 2.0);
        cout << "Division completed successfully" << endl;
    } catch (const runtime_error& e) {
        cout << "Caught runtime_error: " << e.what() << endl;
    }
    
    // Example 2: Division by zero
    cout << "\nExample 2: Division by zero" << endl;
    try {
        divideNumbers(10.0, 0.0);
        cout << "This line won't execute" << endl;
    } catch (const runtime_error& e) {
        cout << "Caught runtime_error: " << e.what() << endl;
    }
    
    // Example 3: Multiple catch blocks
    cout << "\nExample 3: Multiple exception types" << endl;
    vector<int> testAges = {25, -5, 200, 16};
    
    for (int age : testAges) {
        try {
            processAge(age);
        } catch (const invalid_argument& e) {
            cout << "Invalid argument: " << e.what() << endl;
        } catch (const out_of_range& e) {
            cout << "Out of range: " << e.what() << endl;
        } catch (const domain_error& e) {
            cout << "Domain error: " << e.what() << endl;
        }
    }
    
    // Example 4: Catch-all handler
    cout << "\nExample 4: Catch-all handler" << endl;
    try {
        throw "This is a string literal exception";
    } catch (const runtime_error& e) {
        cout << "Caught runtime_error: " << e.what() << endl;
    } catch (const exception& e) {
        cout << "Caught standard exception: " << e.what() << endl;
    } catch (...) {
        cout << "Caught unknown exception type" << endl;
    }
    
    return 0;
}
```

### 2. **Exception Propagation and Stack Unwinding**

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;

// Class to demonstrate stack unwinding
class ResourceHolder {
private:
    string name;
    int* data;
    
public:
    ResourceHolder(const string& n, int size) : name(n) {
        data = new int[size];
        cout << "ResourceHolder '" << name << "' created" << endl;
    }
    
    ~ResourceHolder() {
        delete[] data;
        cout << "ResourceHolder '" << name << "' destroyed" << endl;
    }
    
    void processData(int value) {
        cout << "Processing data in '" << name << "'" << endl;
        if (value < 0) {
            throw runtime_error("Negative value not allowed in " + name);
        }
    }
};

// Nested function calls to demonstrate propagation
void level3Function(int value) {
    cout << "Entering level3Function" << endl;
    ResourceHolder resource3("Level3", 10);
    
    if (value == 3) {
        throw logic_error("Error in level 3");
    }
    
    resource3.processData(value);
    cout << "Exiting level3Function" << endl;
}

void level2Function(int value) {
    cout << "Entering level2Function" << endl;
    ResourceHolder resource2("Level2", 20);
    
    try {
        level3Function(value);
    } catch (const logic_error& e) {
        cout << "Caught logic_error in level2: " << e.what() << endl;
        throw; // Re-throw the exception
    }
    
    cout << "Exiting level2Function" << endl;
}

void level1Function(int value) {
    cout << "Entering level1Function" << endl;
    ResourceHolder resource1("Level1", 30);
    
    level2Function(value);
    
    cout << "Exiting level1Function" << endl;
}

// Function demonstrating different throw scenarios
void demonstrateThrows(int scenario) {
    cout << "\n--- Scenario " << scenario << " ---" << endl;
    
    try {
        level1Function(scenario);
        cout << "All levels completed successfully" << endl;
    } catch (const runtime_error& e) {
        cout << "Caught runtime_error at top level: " << e.what() << endl;
    } catch (const logic_error& e) {
        cout << "Caught logic_error at top level: " << e.what() << endl;
    } catch (...) {
        cout << "Caught unknown exception at top level" << endl;
    }
}

int main() {
    cout << "=== Exception Propagation and Stack Unwinding ===" << endl;
    
    // Scenario 1: No exception
    demonstrateThrows(1);
    
    // Scenario 2: Runtime error in level 3
    demonstrateThrows(-1);
    
    // Scenario 3: Logic error in level 3 (caught and re-thrown)
    demonstrateThrows(3);
    
    return 0;
}
```

### 3. **Throwing Different Types of Exceptions**

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
#include <memory>
using namespace std;

// Custom exception classes
class BusinessException : public exception {
private:
    string message;
    
public:
    BusinessException(const string& msg) : message(msg) {}
    const char* what() const noexcept override {
        return message.c_str();
    }
};

class ValidationException : public BusinessException {
public:
    ValidationException(const string& field, const string& value)
        : BusinessException("Validation failed for " + field + ": " + value) {}
};

// Function throwing different exception types
void validateUser(const string& username, int age, double balance) {
    cout << "Validating user: " << username << ", age: " << age << ", balance: " << balance << endl;
    
    if (username.empty()) {
        throw ValidationException("username", "empty");
    }
    
    if (username.length() < 3) {
        throw ValidationException("username", "too short");
    }
    
    if (age < 0) {
        throw invalid_argument("Age cannot be negative");
    }
    
    if (age < 18) {
        throw domain_error("User must be at least 18 years old");
    }
    
    if (balance < 0) {
        throw BusinessException("Account balance cannot be negative");
    }
    
    cout << "User validation passed" << endl;
}

// Function demonstrating throw with different objects
void processTransaction(int amount) {
    cout << "Processing transaction: $" << amount << endl;
    
    if (amount <= 0) {
        throw amount; // Throwing integer
    }
    
    if (amount > 10000) {
        throw "Transaction amount exceeds limit"; // Throwing string literal
    }
    
    if (amount % 100 != 0) {
        throw 3.14; // Throwing double
    }
    
    cout << "Transaction processed successfully" << endl;
}

// Exception handling with polymorphism
class Animal {
public:
    virtual ~Animal() = default;
    virtual string makeSound() const = 0;
};

class Dog : public Animal {
public:
    string makeSound() const override { return "Woof!"; }
};

class Cat : public Animal {
public:
    string makeSound() const override { return "Meow!"; }
};

void demonstrateAnimalException(const Animal* animal) {
    cout << "Demonstrating with animal: " << animal->makeSound() << endl;
    throw *animal; // Throwing polymorphic object
}

int main() {
    cout << "=== Throwing Different Types of Exceptions ===" << endl;
    
    // Example 1: Validation exceptions
    cout << "\n--- Validation Examples ---" << endl;
    vector<pair<string, int>> users = {
        {"", 25},           // Empty username
        {"Jo", 30},         // Short username
        {"Alice", -5},      // Negative age
        {"Bob", 16},        // Underage
        {"Charlie", 25},    // Valid
        {"David", 30, -100} // Negative balance (won't reach due to syntax error)
    };
    
    for (const auto& user : users) {
        try {
            validateUser(user.first, user.second, 1000.0);
        } catch (const ValidationException& e) {
            cout << "Validation error: " << e.what() << endl;
        } catch (const invalid_argument& e) {
            cout << "Invalid argument: " << e.what() << endl;
        } catch (const domain_error& e) {
            cout << "Domain error: " << e.what() << endl;
        } catch (const BusinessException& e) {
            cout << "Business error: " << e.what() << endl;
        }
    }
    
    // Example 2: Different exception types
    cout << "\n--- Transaction Examples ---" << endl;
    vector<int> amounts = {100, -50, 15000, 123};
    
    for (int amount : amounts) {
        try {
            processTransaction(amount);
        } catch (int e) {
            cout << "Caught integer exception: " << e << " (invalid amount)" << endl;
        } catch (const char* e) {
            cout << "Caught string exception: " << e << endl;
        } catch (double e) {
            cout << "Caught double exception: " << e << " (amount must be multiple of 100)" << endl;
        }
    }
    
    // Example 3: Polymorphic exceptions
    cout << "\n--- Polymorphic Exception Examples ---" << endl;
    vector<unique_ptr<Animal>> animals;
    animals.emplace_back(make_unique<Dog>());
    animals.emplace_back(make_unique<Cat>());
    
    for (const auto& animal : animals) {
        try {
            demonstrateAnimalException(animal.get());
        } catch (const Animal& e) {
            cout << "Caught animal exception: " << e.makeSound() << endl;
        }
    }
    
    return 0;
}
```

### 4. **Exception Handling Best Practices**

```cpp
#include <iostream>
#include <stdexcept>
#include <memory>
#include <vector>
using namespace std;

// Good practice: Catch by reference
void demonstrateCatchByReference() {
    cout << "--- Catch by Reference ---" << endl;
    
    class CustomException : public exception {
    public:
        const char* what() const noexcept override { return "Custom exception"; }
    };
    
    try {
        throw CustomException();
    } catch (CustomException e) {  // BAD: Catches by value
        cout << "Caught by value (bad practice)" << endl;
    }
    
    try {
        throw CustomException();
    } catch (const CustomException& e) {  // GOOD: Catches by reference
        cout << "Caught by reference (good practice): " << e.what() << endl;
    }
}

// Good practice: Order catch blocks from most specific to most general
void demonstrateCatchOrder() {
    cout << "\n--- Catch Block Order ---" << endl;
    
    try {
        throw runtime_error("Runtime error occurred");
    } catch (const exception& e) {  // BAD: Too general first
        cout << "Caught general exception: " << e.what() << endl;
    } catch (const runtime_error& e) {  // This will never be reached
        cout << "Caught runtime error: " << e.what() << endl;
    }
    
    try {
        throw runtime_error("Runtime error occurred");
    } catch (const runtime_error& e) {  // GOOD: Most specific first
        cout << "Caught runtime error: " << e.what() << endl;
    } catch (const exception& e) {  // Then general
        cout << "Caught general exception: " << e.what() << endl;
    }
}

// Good practice: Use RAII with exceptions
class ResourceManager {
private:
    int* data;
    FILE* file;
    
public:
    ResourceManager(size_t size, const string& filename) {
        data = new int[size];
        file = fopen(filename.c_str(), "w");
        cout << "Resources acquired" << endl;
    }
    
    ~ResourceManager() {
        delete[] data;
        if (file) fclose(file);
        cout << "Resources released" << endl;
    }
    
    void riskyOperation(bool shouldFail) {
        if (shouldFail) {
            throw runtime_error("Risky operation failed");
        }
        cout << "Risky operation succeeded" << endl;
    }
};

void demonstrateRAII() {
    cout << "\n--- RAII with Exceptions ---" << endl;
    
    try {
        ResourceManager manager(100, "test.txt");
        manager.riskyOperation(false);
        cout << "Operation completed" << endl;
    } catch (const exception& e) {
        cout << "Exception caught: " << e.what() << endl;
        cout << "Resources automatically cleaned up" << endl;
    }
    
    try {
        ResourceManager manager(100, "test.txt");
        manager.riskyOperation(true);
        cout << "This won't be reached" << endl;
    } catch (const exception& e) {
        cout << "Exception caught: " << e.what() << endl;
        cout << "Resources automatically cleaned up despite exception" << endl;
    }
}

// Good practice: Don't swallow exceptions unexpectedly
void demonstrateExceptionSwallowing() {
    cout << "\n--- Exception Swallowing ---" << endl;
    
    auto processData = []() {
        throw runtime_error("Data processing failed");
    };
    
    // BAD: Swallowing without information
    try {
        processData();
    } catch (...) {
        cout << "Something went wrong (bad: no information)" << endl;
    }
    
    // GOOD: At least log the exception
    try {
        processData();
    } catch (const exception& e) {
        cout << "Processing failed: " << e.what() << endl;
        // Maybe re-throw if you can't handle it properly
        // throw;
    }
}

// Good practice: Exception specifications with noexcept
void demonstrateNoexcept() {
    cout << "\n--- Noexcept Specifications ---" << endl;
    
    auto safeFunction = []() noexcept {
        cout << "This function promises not to throw" << endl;
    };
    
    auto riskyFunction = []() {
        throw runtime_error("This function can throw");
    };
    
    cout << "safeFunction is noexcept: " << noexcept(safeFunction()) << endl;
    cout << "riskyFunction is noexcept: " << noexcept(riskyFunction()) << endl;
    
    safeFunction();
    
    try {
        riskyFunction();
    } catch (const exception& e) {
        cout << "Caught exception from risky function: " << e.what() << endl;
    }
}

int main() {
    cout << "=== Exception Handling Best Practices ===" << endl;
    
    demonstrateCatchByReference();
    demonstrateCatchOrder();
    demonstrateRAII();
    demonstrateExceptionSwallowing();
    demonstrateNoexcept();
    
    return 0;
}
```

### 5. **Advanced Exception Handling Patterns**

```cpp
#include <iostream>
#include <stdexcept>
#include <functional>
#include <memory>
using namespace std;

// Pattern 1: Exception-safe factory
class DatabaseConnection {
private:
    string connectionString;
    bool connected;
    
public:
    DatabaseConnection(const string& connStr) : connectionString(connStr), connected(false) {
        if (connStr.empty()) {
            throw invalid_argument("Connection string cannot be empty");
        }
        if (connStr == "invalid") {
            throw runtime_error("Invalid connection string");
        }
        connected = true;
        cout << "Connected to database: " << connectionString << endl;
    }
    
    ~DatabaseConnection() {
        if (connected) {
            cout << "Disconnected from database" << endl;
        }
    }
    
    void executeQuery(const string& query) {
        if (!connected) {
            throw runtime_error("Not connected to database");
        }
        cout << "Executing query: " << query << endl;
    }
};

class DatabaseConnectionFactory {
public:
    static unique_ptr<DatabaseConnection> create(const string& connectionString) {
        try {
            return make_unique<DatabaseConnection>(connectionString);
        } catch (const invalid_argument& e) {
            cout << "Factory caught invalid argument: " << e.what() << endl;
            throw; // Re-throw for caller to handle
        } catch (const runtime_error& e) {
            cout << "Factory caught runtime error: " << e.what() << endl;
            throw; // Re-throw for caller to handle
        }
    }
};

// Pattern 2: Exception-safe transaction
class Transaction {
private:
    DatabaseConnection& db;
    bool committed;
    
public:
    explicit Transaction(DatabaseConnection& database) 
        : db(database), committed(false) {}
    
    ~Transaction() {
        if (!committed) {
            try {
                cout << "Auto-rollback on destruction" << endl;
            } catch (...) {
                // Destructor should not throw
            }
        }
    }
    
    void execute(const string& query) {
        db.executeQuery(query);
    }
    
    void commit() {
        cout << "Transaction committed" << endl;
        committed = true;
    }
};

// Pattern 3: Exception chaining
class ApplicationException : public exception {
private:
    string message;
    exception* cause;
    
public:
    ApplicationException(const string& msg, exception* c = nullptr) 
        : message(msg), cause(c) {}
    
    const char* what() const noexcept override {
        return message.c_str();
    }
    
    const exception* getCause() const { return cause; }
};

class DataLayerException : public ApplicationException {
public:
    DataLayerException(const string& msg, exception* cause = nullptr)
        : ApplicationException("Data layer: " + msg, cause) {}
};

void simulateDataLayerError() {
    throw DataLayerException("Database connection failed", 
                           new runtime_error("Network timeout"));
}

// Pattern 4: Exception-safe function wrapper
template <typename Func>
auto safeExecute(Func&& func, const string& operationName) -> decltype(func()) {
    try {
        return func();
    } catch (const exception& e) {
        cout << "Error in " << operationName << ": " << e.what() << endl;
        throw;
    }
}

// Pattern 5: Exception handling with lambdas
void demonstrateLambdaExceptionHandling() {
    cout << "--- Lambda Exception Handling ---" << endl;
    
    auto riskyOperation = [](int value) -> int {
        if (value < 0) {
            throw invalid_argument("Negative value not allowed");
        }
        return value * 2;
    };
    
    auto safeOperation = [riskyOperation](int value) {
        try {
            return riskyOperation(value);
        } catch (const exception& e) {
            cout << "Handled in lambda: " << e.what() << endl;
            return 0; // Default value
        }
    };
    
    cout << "Safe operation with 5: " << safeOperation(5) << endl;
    cout << "Safe operation with -3: " << safeOperation(-3) << endl;
}

int main() {
    cout << "=== Advanced Exception Handling Patterns ===" << endl;
    
    // Pattern 1: Factory with exception handling
    cout << "\n--- Factory Pattern ---" << endl;
    try {
        auto db1 = DatabaseConnectionFactory::create("localhost:5432");
        db1->executeQuery("SELECT * FROM users");
    } catch (const exception& e) {
        cout << "Failed to create database connection: " << e.what() << endl;
    }
    
    try {
        auto db2 = DatabaseConnectionFactory::create("invalid");
    } catch (const exception& e) {
        cout << "Expected failure: " << e.what() << endl;
    }
    
    // Pattern 2: Transaction pattern
    cout << "\n--- Transaction Pattern ---" << endl;
    try {
        auto db = DatabaseConnectionFactory::create("localhost:5432");
        {
            Transaction transaction(*db);
            transaction.execute("INSERT INTO logs VALUES ('test')");
            transaction.execute("UPDATE stats SET count = count + 1");
            transaction.commit(); // Explicit commit
        }
        
        {
            Transaction transaction(*db);
            transaction.execute("INSERT INTO logs VALUES ('test2')");
            // Forget to commit - will auto-rollback
        }
    } catch (const exception& e) {
        cout << "Transaction error: " << e.what() << endl;
    }
    
    // Pattern 3: Exception chaining
    cout << "\n--- Exception Chaining ---" << endl;
    try {
        simulateDataLayerError();
    } catch (const ApplicationException& e) {
        cout << "Caught application exception: " << e.what() << endl;
        if (e.getCause()) {
            cout << "Caused by: " << e.getCause()->what() << endl;
        }
    }
    
    // Pattern 4: Safe execution wrapper
    cout << "\n--- Safe Execution Wrapper ---" << endl;
    try {
        auto result = safeExecute([]() -> int {
            if (true) throw runtime_error("Something went wrong");
            return 42;
        }, "test operation");
        cout << "Result: " << result << endl;
    } catch (const exception& e) {
        cout << "Operation failed: " << e.what() << endl;
    }
    
    // Pattern 5: Lambda exception handling
    demonstrateLambdaExceptionHandling();
    
    return 0;
}
```

---

## 🎮 Complete Example: Banking System with Exception Handling

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <map>
using namespace std;

// Custom exception hierarchy for banking system
class BankingException : public exception {
protected:
    string message;
    string accountNumber;
    
public:
    BankingException(const string& msg, const string& accNum = "") 
        : message(msg), accountNumber(accNum) {}
    
    const char* what() const noexcept override {
        return message.c_str();
    }
    
    const string& getAccountNumber() const { return accountNumber; }
};

class InsufficientFundsException : public BankingException {
private:
    double requestedAmount;
    double availableBalance;
    
public:
    InsufficientFundsException(const string& accNum, double requested, double available)
        : BankingException("Insufficient funds for account " + accNum, accNum),
          requestedAmount(requested), availableBalance(available) {}
    
    double getRequestedAmount() const { return requestedAmount; }
    double getAvailableBalance() const { return availableBalance; }
};

class AccountNotFoundException : public BankingException {
public:
    AccountNotFoundException(const string& accNum)
        : BankingException("Account not found: " + accNum, accNum) {}
};

class InvalidAmountException : public BankingException {
private:
    double amount;
    
public:
    InvalidAmountException(double amount)
        : BankingException("Invalid amount: " + to_string(amount)), amount(amount) {}
    
    double getAmount() const { return amount; }
};

class Transaction {
private:
    string fromAccount;
    string toAccount;
    double amount;
    string timestamp;
    
public:
    Transaction(const string& from, const string& to, double amt, const string& time)
        : fromAccount(from), toAccount(to), amount(amt), timestamp(time) {}
    
    void display() const {
        cout << "Transaction: " << fromAccount << " -> " << toAccount 
             << ", Amount: $" << amount << ", Time: " << timestamp << endl;
    }
    
    string getFromAccount() const { return fromAccount; }
    string getToAccount() const { return toAccount; }
    double getAmount() const { return amount; }
};

class Account {
private:
    string accountNumber;
    string ownerName;
    double balance;
    vector<Transaction> transactions;
    
public:
    Account(const string& accNum, const string& owner, double initialBalance)
        : accountNumber(accNum), ownerName(owner), balance(initialBalance) {
        if (initialBalance < 0) {
            throw InvalidAmountException(initialBalance);
        }
    }
    
    void deposit(double amount) {
        if (amount <= 0) {
            throw InvalidAmountException(amount);
        }
        balance += amount;
        string timestamp = "2024-01-01 12:00:00"; // Simplified
        transactions.emplace_back("DEPOSIT", accountNumber, amount, timestamp);
        cout << "Deposited $" << amount << " to account " << accountNumber << endl;
    }
    
    void withdraw(double amount) {
        if (amount <= 0) {
            throw InvalidAmountException(amount);
        }
        if (amount > balance) {
            throw InsufficientFundsException(accountNumber, amount, balance);
        }
        balance -= amount;
        string timestamp = "2024-01-01 12:00:00"; // Simplified
        transactions.emplace_back(accountNumber, "WITHDRAW", amount, timestamp);
        cout << "Withdrew $" << amount << " from account " << accountNumber << endl;
    }
    
    void transferTo(Account& toAccount, double amount) {
        withdraw(amount); // May throw InsufficientFundsException
        toAccount.deposit(amount); // May throw InvalidAmountException
        
        string timestamp = "2024-01-01 12:00:00"; // Simplified
        transactions.emplace_back(accountNumber, toAccount.accountNumber, amount, timestamp);
        toAccount.transactions.emplace_back(accountNumber, toAccount.accountNumber, amount, timestamp);
        
        cout << "Transferred $" << amount << " from " << accountNumber 
             << " to " << toAccount.accountNumber << endl;
    }
    
    string getAccountNumber() const { return accountNumber; }
    string getOwnerName() const { return ownerName; }
    double getBalance() const { return balance; }
    
    void displayStatement() const {
        cout << "\n=== Account Statement ===" << endl;
        cout << "Account: " << accountNumber << endl;
        cout << "Owner: " << ownerName << endl;
        cout << "Balance: $" << balance << endl;
        cout << "Transactions:" << endl;
        for (const auto& transaction : transactions) {
            transaction.display();
        }
    }
};

class Bank {
private:
    map<string, unique_ptr<Account>> accounts;
    
public:
    Account& createAccount(const string& accNum, const string& owner, double initialBalance) {
        if (accounts.find(accNum) != accounts.end()) {
            throw BankingException("Account already exists: " + accNum, accNum);
        }
        
        auto account = make_unique<Account>(accNum, owner, initialBalance);
        Account& ref = *account;
        accounts[accNum] = move(account);
        cout << "Created account " << accNum << " for " << owner << endl;
        return ref;
    }
    
    Account& getAccount(const string& accNum) {
        auto it = accounts.find(accNum);
        if (it == accounts.end()) {
            throw AccountNotFoundException(accNum);
        }
        return *it->second;
    }
    
    void transferFunds(const string& fromAcc, const string& toAcc, double amount) {
        try {
            Account& from = getAccount(fromAcc);
            Account& to = getAccount(toAcc);
            from.transferTo(to, amount);
        } catch (const BankingException& e) {
            cout << "Transfer failed: " << e.what() << endl;
            throw; // Re-throw for caller to handle
        }
    }
    
    void displayAllAccounts() const {
        cout << "\n=== All Bank Accounts ===" << endl;
        for (const auto& pair : accounts) {
            const auto& account = pair.second;
            cout << "Account: " << account->getAccountNumber() 
                 << ", Owner: " << account->getOwnerName() 
                 << ", Balance: $" << account->getBalance() << endl;
        }
    }
};

int main() {
    cout << "=== Banking System with Exception Handling ===" << endl;
    
    Bank bank;
    
    try {
        // Create accounts
        Account& alice = bank.createAccount("ACC001", "Alice Smith", 1000.0);
        Account& bob = bank.createAccount("ACC002", "Bob Johnson", 500.0);
        Account& charlie = bank.createAccount("ACC003", "Charlie Brown", 2000.0);
        
        bank.displayAllAccounts();
        
        // Perform some operations
        cout << "\n--- Performing Operations ---" << endl;
        alice.deposit(500.0);
        bob.withdraw(200.0);
        
        // Transfer funds
        bank.transferFunds("ACC001", "ACC002", 300.0);
        bank.transferFunds("ACC003", "ACC001", 1000.0);
        
        bank.displayAllAccounts();
        
        // Try some operations that will fail
        cout << "\n--- Testing Exception Scenarios ---" << endl;
        
        // Test 1: Insufficient funds
        try {
            bob.withdraw(1000.0);
        } catch (const InsufficientFundsException& e) {
            cout << "Insufficient funds: Requested $" << e.getRequestedAmount() 
                 << ", Available: $" << e.getAvailableBalance() << endl;
        }
        
        // Test 2: Invalid amount
        try {
            alice.deposit(-100.0);
        } catch (const InvalidAmountException& e) {
            cout << "Invalid amount: " << e.getAmount() << endl;
        }
        
        // Test 3: Account not found
        try {
            bank.transferFunds("ACC001", "ACC999", 100.0);
        } catch (const AccountNotFoundException& e) {
            cout << "Account not found: " << e.getAccountNumber() << endl;
        }
        
        // Test 4: Transfer with insufficient funds
        try {
            bank.transferFunds("ACC002", "ACC003", 1000.0);
        } catch (const InsufficientFundsException& e) {
            cout << "Transfer failed - Insufficient funds in account " 
                 << e.getAccountNumber() << endl;
        }
        
        // Display final statements
        cout << "\n--- Final Account Statements ---" << endl;
        bank.getAccount("ACC001").displayStatement();
        bank.getAccount("ACC002").displayStatement();
        bank.getAccount("ACC003").displayStatement();
        
    } catch (const BankingException& e) {
        cout << "Banking system error: " << e.what() << endl;
        if (!e.getAccountNumber().empty()) {
            cout << "Account involved: " << e.getAccountNumber() << endl;
        }
    } catch (const exception& e) {
        cout << "Unexpected error: " << e.what() << endl;
    }
    
    return 0;
}
```

---

## ⚡ Performance Considerations

### Advantages
- ✅ **Clean Error Handling**: Separates error handling from normal flow
- ✅ **Resource Safety**: Automatic cleanup through stack unwinding
- ✅ **Exception Safety**: Strong guarantees about object state
- ✅ **Maintainability**: Centralized error handling logic

### Considerations
- ⚠️ **Runtime Overhead**: Exception handling has performance cost
- ⚠️ **Binary Size**: Increases executable size
- ⚠️ **Memory Usage**: Stack unwinding requires additional memory
- ⚠️ **Compiler Optimization**: May limit some optimizations

---

## 🐛 Common Pitfalls

| Problem | Solution |
|---------|----------|
| **Catching by value** | Always catch exceptions by reference |
| **Wrong catch order** | Order from most specific to most general |
| **Throwing in destructors** | Never throw in destructors or use noexcept |
| **Swallowing exceptions** | Handle exceptions properly or re-throw |
| **Memory leaks** | Use RAII and smart pointers |

---

## ✅ Best Practices

1. **Catch by reference** to avoid object slicing
2. **Order catch blocks** from specific to general
3. **Use RAII** for automatic resource management
4. **Don't throw in destructors** unless you catch all exceptions
5. **Be specific** about which exceptions you catch
6. **Provide meaningful error messages** in exception objects
7. **Use noexcept** for functions that don't throw

---

## 📚 Related Topics

- [Standard Exceptions](02_Standard_Exceptions.md)
- [Custom Exceptions](03_Custom_Exceptions.md)
- [Exception Specifications](04_Exception_Specifications.md)
- [RAII Pattern](05_RAII.md)

---

## 🚀 Next Steps

Continue learning about:
- **Standard Exception Hierarchy**: Built-in exception types
- **Custom Exception Design**: Creating domain-specific exceptions
- **Exception Specifications**: noexcept and exception guarantees
- **RAII Pattern**: Resource management with exceptions

---
