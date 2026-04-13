# Custom Exceptions

## 📖 Overview

Custom exceptions allow you to create domain-specific error types that carry meaningful information about errors specific to your application. By inheriting from standard exception classes, you can build a robust exception hierarchy that provides clear, actionable error information while maintaining compatibility with standard exception handling mechanisms.

---

## 🎯 Key Concepts

- **Exception Inheritance**: Deriving from standard exception classes
- **Domain-Specific Errors**: Tailored exceptions for your application domain
- **Error Context**: Adding relevant data to exception objects
- **Exception Chaining**: Linking related exceptions
- **Custom Error Codes**: Application-specific error identifiers

---

## 💻 Basic Custom Exception Syntax

```cpp
class CustomException : public std::exception {
private:
    std::string message;
    
public:
    CustomException(const std::string& msg) : message(msg) {}
    
    const char* what() const noexcept override {
        return message.c_str();
    }
};
```

---

## 🔍 Detailed Explanation

### 1. **Basic Custom Exception Creation**

```cpp
#include <iostream>
#include <string>
#include <exception>
#include <vector>
using namespace std;

// Simple custom exception
class ApplicationException : public exception {
private:
    string message;
    
public:
    ApplicationException(const string& msg) : message(msg) {}
    
    const char* what() const noexcept override {
        return message.c_str();
    }
};

// Custom exception with additional data
class ValidationException : public ApplicationException {
private:
    string fieldName;
    string fieldValue;
    
public:
    ValidationException(const string& field, const string& value)
        : ApplicationException("Validation failed for field: " + field),
          fieldName(field), fieldValue(value) {}
    
    const string& getFieldName() const { return fieldName; }
    const string& getFieldValue() const { return fieldValue; }
    
    string getDetailedMessage() const {
        return "Field '" + fieldName + "' with value '" + fieldValue + "' is invalid";
    }
};

// Function using custom exceptions
void validateUser(const string& username, const string& email, int age) {
    cout << "Validating user: " << username << ", " << email << ", age " << age << endl;
    
    if (username.empty()) {
        throw ValidationException("username", "empty");
    }
    
    if (username.length() < 3) {
        throw ValidationException("username", "too short");
    }
    
    if (email.find('@') == string::npos) {
        throw ValidationException("email", "invalid format");
    }
    
    if (age < 0) {
        throw ValidationException("age", "negative");
    }
    
    if (age < 18) {
        throw ApplicationException("User must be at least 18 years old");
    }
    
    cout << "User validation successful" << endl;
}

int main() {
    cout << "=== Basic Custom Exceptions ===" << endl;
    
    vector<tuple<string, string, int>> testUsers = {
        {"alice", "alice@example.com", 25},    // Valid
        {"", "bob@example.com", 30},           // Empty username
        {"jo", "jo@example.com", 22},          // Short username
        {"charlie", "charlieexample.com", 28}, // Invalid email
        {"dave", "dave@example.com", -5},      // Negative age
        {"eve", "eve@example.com", 16}         // Underage
    };
    
    for (const auto& [username, email, age] : testUsers) {
        try {
            validateUser(username, email, age);
        } catch (const ValidationException& e) {
            cout << "Validation error: " << e.getDetailedMessage() << endl;
        } catch (const ApplicationException& e) {
            cout << "Application error: " << e.what() << endl;
        }
    }
    
    return 0;
}
```

### 2. **Exception Hierarchy Design**

```cpp
#include <iostream>
#include <string>
#include <exception>
#include <stdexcept>
using namespace std;

// Base banking exception
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

// Account-related exceptions
class AccountException : public BankingException {
public:
    AccountException(const string& msg, const string& accNum = "")
        : BankingException("Account error: " + msg, accNum) {}
};

class InsufficientFundsException : public AccountException {
private:
    double requestedAmount;
    double availableBalance;
    
public:
    InsufficientFundsException(const string& accNum, double requested, double available)
        : AccountException("Insufficient funds", accNum),
          requestedAmount(requested), availableBalance(available) {}
    
    double getRequestedAmount() const { return requestedAmount; }
    double getAvailableBalance() const { return availableBalance; }
    
    string getDetailedMessage() const {
        return "Account " + accountNumber + ": Requested $" + 
               to_string(requestedAmount) + ", Available $" + 
               to_string(availableBalance);
    }
};

class AccountNotFoundException : public AccountException {
public:
    AccountNotFoundException(const string& accNum)
        : AccountException("Account not found", accNum) {}
};

// Transaction-related exceptions
class TransactionException : public BankingException {
private:
    string transactionId;
    
public:
    TransactionException(const string& msg, const string& transId = "", const string& accNum = "")
        : BankingException("Transaction error: " + msg, accNum), transactionId(transId) {}
    
    const string& getTransactionId() const { return transactionId; }
};

class DuplicateTransactionException : public TransactionException {
public:
    DuplicateTransactionException(const string& transId, const string& accNum = "")
        : TransactionException("Duplicate transaction", transId, accNum) {}
};

class TransactionLimitExceededException : public TransactionException {
private:
    double transactionAmount;
    double limitAmount;
    
public:
    TransactionLimitExceededException(const string& transId, double transAmt, double limitAmt, const string& accNum = "")
        : TransactionException("Transaction limit exceeded", transId, accNum),
          transactionAmount(transAmt), limitAmount(limitAmt) {}
    
    double getTransactionAmount() const { return transactionAmount; }
    double getLimitAmount() const { return limitAmount; }
};

// Demonstration functions
void processWithdrawal(const string& accountNum, double amount) {
    cout << "Processing withdrawal: $" << amount << " from account " << accountNum << endl;
    
    if (accountNum == "ACC001") {
        throw InsufficientFundsException(accountNum, amount, 100.0);
    } else if (accountNum == "ACC002") {
        throw AccountNotFoundException(accountNum);
    }
    
    cout << "Withdrawal processed successfully" << endl;
}

void processTransaction(const string& transId, const string& accountNum, double amount) {
    cout << "Processing transaction " << transId << ": $" << amount << endl;
    
    if (transId == "TXN001") {
        throw DuplicateTransactionException(transId, accountNum);
    } else if (amount > 10000) {
        throw TransactionLimitExceededException(transId, amount, 10000, accountNum);
    }
    
    cout << "Transaction processed successfully" << endl;
}

int main() {
    cout << "=== Exception Hierarchy Design ===" << endl;
    
    // Test withdrawal scenarios
    cout << "\n--- Withdrawal Tests ---" << endl;
    vector<pair<string, double>> withdrawals = {
        {"ACC001", 200.0},  // Insufficient funds
        {"ACC002", 50.0},   // Account not found
        {"ACC003", 100.0}   // Success
    };
    
    for (const auto& [account, amount] : withdrawals) {
        try {
            processWithdrawal(account, amount);
        } catch (const InsufficientFundsException& e) {
            cout << "Insufficient funds: " << e.getDetailedMessage() << endl;
        } catch (const AccountNotFoundException& e) {
            cout << "Account not found: " << e.getAccountNumber() << endl;
        } catch (const AccountException& e) {
            cout << "Account error: " << e.what() << endl;
        } catch (const BankingException& e) {
            cout << "Banking error: " << e.what() << endl;
        }
    }
    
    // Test transaction scenarios
    cout << "\n--- Transaction Tests ---" << endl;
    vector<tuple<string, string, double>> transactions = {
        {"TXN001", "ACC001", 100.0},  // Duplicate transaction
        {"TXN002", "ACC001", 15000.0}, // Limit exceeded
        {"TXN003", "ACC001", 500.0}   // Success
    };
    
    for (const auto& [transId, account, amount] : transactions) {
        try {
            processTransaction(transId, account, amount);
        } catch (const DuplicateTransactionException& e) {
            cout << "Duplicate transaction: " << e.getTransactionId() << endl;
        } catch (const TransactionLimitExceededException& e) {
            cout << "Limit exceeded: $" << e.getTransactionAmount() 
                 << " (limit: $" << e.getLimitAmount() << ")" << endl;
        } catch (const TransactionException& e) {
            cout << "Transaction error: " << e.what() << endl;
        } catch (const BankingException& e) {
            cout << "Banking error: " << e.what() << endl;
        }
    }
    
    return 0;
}
```

### 3. **Exception Chaining and Context**

```cpp
#include <iostream>
#include <string>
#include <exception>
#include <stdexcept>
#include <memory>
using namespace std;

// Base exception with chaining support
class ChainedException : public exception {
private:
    string message;
    unique_ptr<exception> cause;
    
public:
    ChainedException(const string& msg, exception* c = nullptr)
        : message(msg), cause(c) {}
    
    const char* what() const noexcept override {
        return message.c_str();
    }
    
    const exception* getCause() const { return cause.get(); }
    
    string getFullMessage() const {
        string full = message;
        if (cause) {
            full += "\nCaused by: " + string(cause->what());
        }
        return full;
    }
};

// Data layer exception
class DataLayerException : public ChainedException {
private:
    string operation;
    string dataSource;
    
public:
    DataLayerException(const string& msg, const string& op, const string& source, exception* cause = nullptr)
        : ChainedException("Data layer error: " + msg, cause),
          operation(op), dataSource(source) {}
    
    const string& getOperation() const { return operation; }
    const string& getDataSource() const { return dataSource; }
};

// Business layer exception
class BusinessLayerException : public ChainedException {
private:
    string businessRule;
    string context;
    
public:
    BusinessLayerException(const string& msg, const string& rule, const string& ctx, exception* cause = nullptr)
        : ChainedException("Business layer error: " + msg, cause),
          businessRule(rule), context(ctx) {}
    
    const string& getBusinessRule() const { return businessRule; }
    const string& getContext() const { return context; }
};

// Service layer exception
class ServiceLayerException : public ChainedException {
private:
    string serviceName;
    string method;
    
public:
    ServiceLayerException(const string& msg, const string& service, const string& meth, exception* cause = nullptr)
        : ChainedException("Service layer error: " + msg, cause),
          serviceName(service), method(meth) {}
    
    const string& getServiceName() const { return serviceName; }
    const string& getMethod() const { return method; }
};

// Simulation of different layers
class Database {
public:
    void connect() {
        throw runtime_error("Connection timeout");
    }
    
    void query(const string& sql) {
        throw runtime_error("SQL syntax error");
    }
};

class UserRepository {
private:
    Database db;
    
public:
    void saveUser(const string& userData) {
        try {
            db.connect();
            db.query("INSERT INTO users VALUES ('" + userData + "')");
        } catch (const exception& e) {
            throw DataLayerException("Failed to save user", "saveUser", "users_table", new runtime_error(e.what()));
        }
    }
};

class UserService {
private:
    UserRepository repository;
    
public:
    void createUser(const string& username, const string& email) {
        try {
            string userData = username + "," + email;
            repository.saveUser(userData);
        } catch (const DataLayerException& e) {
            throw BusinessLayerException("User creation failed", "user_validation", 
                                       "username=" + username, new DataLayerException(e));
        }
    }
};

class UserAPI {
private:
    UserService service;
    
public:
    void registerUser(const string& username, const string& email) {
        try {
            service.createUser(username, email);
        } catch (const BusinessLayerException& e) {
            throw ServiceLayerException("User registration failed", "UserAPI", 
                                       "registerUser", new BusinessLayerException(e));
        }
    }
};

// Exception handler that prints the full chain
void handleException(const ChainedException& e) {
    cout << "=== Exception Chain ===" << endl;
    
    const ChainedException* current = &e;
    int level = 0;
    
    while (current) {
        cout << "Level " << level << ": " << current->what() << endl;
        
        // Add specific context based on exception type
        if (auto dataEx = dynamic_cast<const DataLayerException*>(current)) {
            cout << "  Operation: " << dataEx->getOperation() << endl;
            cout << "  Data Source: " << dataEx->getDataSource() << endl;
        } else if (auto businessEx = dynamic_cast<const BusinessLayerException*>(current)) {
            cout << "  Business Rule: " << businessEx->getBusinessRule() << endl;
            cout << "  Context: " << businessEx->getContext() << endl;
        } else if (auto serviceEx = dynamic_cast<const ServiceLayerException*>(current)) {
            cout << "  Service: " << serviceEx->getServiceName() << endl;
            cout << "  Method: " << serviceEx->getMethod() << endl;
        }
        
        if (current->getCause()) {
            current = dynamic_cast<const ChainedException*>(current->getCause());
        } else {
            break;
        }
        level++;
    }
}

int main() {
    cout << "=== Exception Chaining and Context ===" << endl;
    
    UserAPI api;
    
    try {
        api.registerUser("alice", "alice@example.com");
    } catch (const ServiceLayerException& e) {
        handleException(e);
    } catch (const exception& e) {
        cout << "Unhandled exception: " << e.what() << endl;
    }
    
    return 0;
}
```

### 4. **Custom Exceptions with Error Codes**

```cpp
#include <iostream>
#include <string>
#include <exception>
#include <map>
#include <sstream>
using namespace std;

// Error code enumeration
enum class ErrorCode {
    SUCCESS = 0,
    INVALID_INPUT = 1001,
    PERMISSION_DENIED = 1002,
    RESOURCE_NOT_FOUND = 1003,
    OPERATION_TIMEOUT = 1004,
    QUOTA_EXCEEDED = 1005,
    SYSTEM_ERROR = 2001,
    NETWORK_ERROR = 2002,
    DATABASE_ERROR = 2003
};

// Error code to string conversion
string errorCodeToString(ErrorCode code) {
    static const map<ErrorCode, string> errorMap = {
        {ErrorCode::SUCCESS, "SUCCESS"},
        {ErrorCode::INVALID_INPUT, "INVALID_INPUT"},
        {ErrorCode::PERMISSION_DENIED, "PERMISSION_DENIED"},
        {ErrorCode::RESOURCE_NOT_FOUND, "RESOURCE_NOT_FOUND"},
        {ErrorCode::OPERATION_TIMEOUT, "OPERATION_TIMEOUT"},
        {ErrorCode::QUOTA_EXCEEDED, "QUOTA_EXCEEDED"},
        {ErrorCode::SYSTEM_ERROR, "SYSTEM_ERROR"},
        {ErrorCode::NETWORK_ERROR, "NETWORK_ERROR"},
        {ErrorCode::DATABASE_ERROR, "DATABASE_ERROR"}
    };
    
    auto it = errorMap.find(code);
    return it != errorMap.end() ? it->second : "UNKNOWN";
}

// Base exception with error code support
class CodedException : public exception {
protected:
    ErrorCode errorCode;
    string message;
    map<string, string> context;
    
public:
    CodedException(ErrorCode code, const string& msg)
        : errorCode(code), message(msg) {}
    
    ErrorCode getErrorCode() const { return errorCode; }
    
    const char* what() const noexcept override {
        return message.c_str();
    }
    
    void addContext(const string& key, const string& value) {
        context[key] = value;
    }
    
    string getContext(const string& key) const {
        auto it = context.find(key);
        return it != context.end() ? it->second : "";
    }
    
    string getFullMessage() const {
        stringstream ss;
        ss << "[" << errorCodeToString(errorCode) << "] " << message;
        
        if (!context.empty()) {
            ss << " (Context: ";
            bool first = true;
            for (const auto& [key, value] : context) {
                if (!first) ss << ", ";
                ss << key << "=" << value;
                first = false;
            }
            ss << ")";
        }
        
        return ss.str();
    }
};

// Specific exception classes
class FileException : public CodedException {
private:
    string filename;
    
public:
    FileException(ErrorCode code, const string& msg, const string& file = "")
        : CodedException(code, msg), filename(file) {
        if (!filename.empty()) {
            addContext("filename", filename);
        }
    }
    
    const string& getFilename() const { return filename; }
};

class NetworkException : public CodedException {
private:
    string host;
    int port;
    
public:
    NetworkException(ErrorCode code, const string& msg, const string& h = "", int p = 0)
        : CodedException(code, msg), host(h), port(p) {
        if (!host.empty()) {
            addContext("host", host);
        }
        if (port > 0) {
            addContext("port", to_string(port));
        }
    }
    
    const string& getHost() const { return host; }
    int getPort() const { return port; }
};

class ValidationException : public CodedException {
private:
    string field;
    string value;
    
public:
    ValidationException(const string& fld, const string& val)
        : CodedException(ErrorCode::INVALID_INPUT, "Validation failed"), 
          field(fld), value(val) {
        addContext("field", field);
        addContext("value", value);
    }
    
    const string& getField() const { return field; }
    const string& getValue() const { return value; }
};

// Exception factory
class ExceptionFactory {
public:
    static unique_ptr<FileException> createFileNotFound(const string& filename) {
        return make_unique<FileException>(ErrorCode::RESOURCE_NOT_FOUND, 
                                        "File not found", filename);
    }
    
    static unique_ptr<FileException> createPermissionDenied(const string& filename) {
        return make_unique<FileException>(ErrorCode::PERMISSION_DENIED, 
                                        "Permission denied", filename);
    }
    
    static unique_ptr<NetworkException> createConnectionTimeout(const string& host, int port) {
        return make_unique<NetworkException>(ErrorCode::OPERATION_TIMEOUT, 
                                           "Connection timeout", host, port);
    }
    
    static unique_ptr<ValidationException> createInvalidEmail(const string& email) {
        return make_unique<ValidationException>("email", email);
    }
};

// Demonstration functions
void readFile(const string& filename) {
    cout << "Reading file: " << filename << endl;
    
    if (filename == "missing.txt") {
        auto ex = ExceptionFactory::createFileNotFound(filename);
        ex->addContext("operation", "read");
        ex->addContext("user_id", "12345");
        throw *ex;
    }
    
    if (filename == "restricted.txt") {
        auto ex = ExceptionFactory::createPermissionDenied(filename);
        ex->addContext("operation", "read");
        ex->addContext("user_role", "guest");
        throw *ex;
    }
    
    cout << "File read successfully" << endl;
}

void connectToServer(const string& host, int port) {
    cout << "Connecting to " << host << ":" << port << endl;
    
    if (host == "timeout.example.com") {
        auto ex = ExceptionFactory::createConnectionTimeout(host, port);
        ex->addContext("timeout_seconds", "30");
        ex->addContext("retry_count", "3");
        throw *ex;
    }
    
    cout << "Connected successfully" << endl;
}

void validateEmail(const string& email) {
    cout << "Validating email: " << email << endl;
    
    if (email.find('@') == string::npos) {
        auto ex = ExceptionFactory::createInvalidEmail(email);
        ex->addContext("validation_rule", "email_format");
        throw *ex;
    }
    
    cout << "Email is valid" << endl;
}

// Exception handler
void handleCodedException(const CodedException& e) {
    cout << "=== Coded Exception Details ===" << endl;
    cout << "Error Code: " << static_cast<int>(e.getErrorCode()) << endl;
    cout << "Error Name: " << errorCodeToString(e.getErrorCode()) << endl;
    cout << "Message: " << e.what() << endl;
    cout << "Full Message: " << e.getFullMessage() << endl;
    
    // Handle specific exception types
    if (auto fileEx = dynamic_cast<const FileException*>(&e)) {
        cout << "Exception Type: FileException" << endl;
        if (!fileEx->getFilename().empty()) {
            cout << "Filename: " << fileEx->getFilename() << endl;
        }
    } else if (auto netEx = dynamic_cast<const NetworkException*>(&e)) {
        cout << "Exception Type: NetworkException" << endl;
        if (!netEx->getHost().empty()) {
            cout << "Host: " << netEx->getHost() << endl;
        }
        if (netEx->getPort() > 0) {
            cout << "Port: " << netEx->getPort() << endl;
        }
    } else if (auto valEx = dynamic_cast<const ValidationException*>(&e)) {
        cout << "Exception Type: ValidationException" << endl;
        cout << "Field: " << valEx->getField() << endl;
        cout << "Value: " << valEx->getValue() << endl;
    }
}

int main() {
    cout << "=== Custom Exceptions with Error Codes ===" << endl;
    
    // Test file operations
    cout << "\n--- File Operation Tests ---" << endl;
    vector<string> testFiles = {"data.txt", "missing.txt", "restricted.txt"};
    
    for (const string& filename : testFiles) {
        try {
            readFile(filename);
        } catch (const CodedException& e) {
            handleCodedException(e);
        }
    }
    
    // Test network operations
    cout << "\n--- Network Operation Tests ---" << endl;
    vector<pair<string, int>> testServers = {
        {"example.com", 80},
        {"timeout.example.com", 8080}
    };
    
    for (const auto& [host, port] : testServers) {
        try {
            connectToServer(host, port);
        } catch (const CodedException& e) {
            handleCodedException(e);
        }
    }
    
    // Test validation
    cout << "\n--- Validation Tests ---" << endl;
    vector<string> testEmails = {"user@example.com", "invalid-email"};
    
    for (const string& email : testEmails) {
        try {
            validateEmail(email);
        } catch (const CodedException& e) {
            handleCodedException(e);
        }
    }
    
    return 0;
}
```

### 5. **Advanced Custom Exception Features**

```cpp
#include <iostream>
#include <string>
#include <exception>
#include <vector>
#include <chrono>
#include <sstream>
#include <iomanip>
using namespace std;
using namespace std::chrono;

// Exception with timestamp and severity
class AdvancedException : public exception {
public:
    enum class Severity {
        INFO,
        WARNING,
        ERROR,
        CRITICAL
    };
    
private:
    string message;
    Severity severity;
    system_clock::time_point timestamp;
    string component;
    string operation;
    vector<pair<string, string>> metadata;
    
public:
    AdvancedException(const string& msg, Severity sev = Severity::ERROR,
                     const string& comp = "", const string& op = "")
        : message(msg), severity(sev), timestamp(system_clock::now()),
          component(comp), operation(op) {}
    
    const char* what() const noexcept override {
        return message.c_str();
    }
    
    Severity getSeverity() const { return severity; }
    system_clock::time_point getTimestamp() const { return timestamp; }
    const string& getComponent() const { return component; }
    const string& getOperation() const { return operation; }
    
    void addMetadata(const string& key, const string& value) {
        metadata.emplace_back(key, value);
    }
    
    string getTimestampString() const {
        auto time_t = system_clock::to_time_t(timestamp);
        auto ms = duration_cast<milliseconds>(timestamp.time_since_epoch()) % 1000;
        
        stringstream ss;
        ss << put_time(localtime(&time_t), "%Y-%m-%d %H:%M:%S");
        ss << '.' << setfill('0') << setw(3) << ms.count();
        return ss.str();
    }
    
    string severityToString() const {
        switch (severity) {
            case Severity::INFO: return "INFO";
            case Severity::WARNING: return "WARNING";
            case Severity::ERROR: return "ERROR";
            case Severity::CRITICAL: return "CRITICAL";
            default: return "UNKNOWN";
        }
    }
    
    string getFullReport() const {
        stringstream ss;
        ss << "=== Exception Report ===" << endl;
        ss << "Timestamp: " << getTimestampString() << endl;
        ss << "Severity: " << severityToString() << endl;
        ss << "Component: " << (component.empty() ? "Unknown" : component) << endl;
        ss << "Operation: " << (operation.empty() ? "Unknown" : operation) << endl;
        ss << "Message: " << message << endl;
        
        if (!metadata.empty()) {
            ss << "Metadata:" << endl;
            for (const auto& [key, value] : metadata) {
                ss << "  " << key << ": " << value << endl;
            }
        }
        
        return ss.str();
    }
};

// Exception with retry capability
class RetryableException : public AdvancedException {
private:
    int maxRetries;
    int currentAttempt;
    milliseconds retryDelay;
    
public:
    RetryableException(const string& msg, int maxRet = 3, int current = 0,
                      milliseconds delay = milliseconds(1000),
                      Severity sev = Severity::WARNING,
                      const string& comp = "", const string& op = "")
        : AdvancedException(msg, sev, comp, op),
          maxRetries(maxRet), currentAttempt(current), retryDelay(delay) {
        addMetadata("max_retries", to_string(maxRetries));
        addMetadata("current_attempt", to_string(currentAttempt));
        addMetadata("retry_delay_ms", to_string(retryDelay.count()));
    }
    
    bool canRetry() const {
        return currentAttempt < maxRetries;
    }
    
    int getMaxRetries() const { return maxRetries; }
    int getCurrentAttempt() const { return currentAttempt; }
    milliseconds getRetryDelay() const { return retryDelay; }
    
    RetryableException createNextAttempt() const {
        return RetryableException(message, maxRetries, currentAttempt + 1, 
                                retryDelay, severity, component, operation);
    }
};

// Exception aggregator for multiple errors
class MultiException : public AdvancedException {
private:
    vector<unique_ptr<AdvancedException>> exceptions;
    
public:
    MultiException(const string& msg, Severity sev = Severity::ERROR,
                   const string& comp = "", const string& op = "")
        : AdvancedException(msg, sev, comp, op) {}
    
    void addException(unique_ptr<AdvancedException> ex) {
        exceptions.push_back(move(ex));
        addMetadata("exception_count", to_string(exceptions.size()));
    }
    
    const vector<unique_ptr<AdvancedException>>& getExceptions() const {
        return exceptions;
    }
    
    string getFullReport() const override {
        stringstream ss;
        ss << AdvancedException::getFullReport();
        
        if (!exceptions.empty()) {
            ss << "Contained Exceptions:" << endl;
            for (size_t i = 0; i < exceptions.size(); i++) {
                ss << "  Exception " << (i + 1) << ":" << endl;
                string exReport = exceptions[i]->getFullReport();
                // Indent the contained exception report
                for (char c : exReport) {
                    ss << c;
                    if (c == '\n') ss << "  ";
                }
            }
        }
        
        return ss.str();
    }
};

// Demonstration functions
void riskyOperation(int attempt = 0) {
    cout << "Attempting risky operation (attempt " << attempt + 1 << ")" << endl;
    
    if (attempt < 2) {
        throw RetryableException("Operation failed", 3, attempt, 
                                milliseconds(1000), 
                                AdvancedException::Severity::WARNING,
                                "Database", "connect");
    }
    
    cout << "Operation succeeded!" << endl;
}

void processWithRetry() {
    int attempt = 0;
    const int maxAttempts = 3;
    
    while (attempt < maxAttempts) {
        try {
            riskyOperation(attempt);
            return;
        } catch (const RetryableException& e) {
            cout << "Operation failed: " << e.what() << endl;
            
            if (e.canRetry()) {
                cout << "Retrying in " << e.getRetryDelay().count() << "ms..." << endl;
                this_thread::sleep_for(e.getRetryDelay());
                attempt++;
            } else {
                cout << "Max retries exceeded" << endl;
                throw;
            }
        }
    }
}

void validateMultipleFields(const map<string, string>& data) {
    auto multiEx = make_unique<MultiException>("Validation failed for multiple fields");
    
    for (const auto& [field, value] : data) {
        if (value.empty()) {
            auto ex = make_unique<AdvancedException>(
                "Field cannot be empty",
                AdvancedException::Severity::ERROR,
                "Validator",
                "validateField"
            );
            ex->addMetadata("field", field);
            ex->addMetadata("value", value);
            multiEx->addException(move(ex));
        } else if (field == "email" && value.find('@') == string::npos) {
            auto ex = make_unique<AdvancedException>(
                "Invalid email format",
                AdvancedException::Severity::ERROR,
                "Validator",
                "validateEmail"
            );
            ex->addMetadata("field", field);
            ex->addMetadata("value", value);
            multiEx->addException(move(ex));
        }
    }
    
    if (!multiEx->getExceptions().empty()) {
        throw *multiEx;
    }
}

int main() {
    cout << "=== Advanced Custom Exception Features ===" << endl;
    
    // Test retryable exception
    cout << "\n--- Retryable Exception Test ---" << endl;
    try {
        processWithRetry();
    } catch (const RetryableException& e) {
        cout << e.getFullReport() << endl;
    }
    
    // Test multi-exception
    cout << "\n--- Multi-Exception Test ---" << endl;
    map<string, string> testData = {
        {"name", ""},
        {"email", "invalid-email"},
        {"age", "25"}
    };
    
    try {
        validateMultipleFields(testData);
    } catch (const MultiException& e) {
        cout << e.getFullReport() << endl;
    }
    
    // Test advanced exception with metadata
    cout << "\n--- Advanced Exception with Metadata ---" << endl;
    try {
        AdvancedException ex("Database connection failed", 
                           AdvancedException::Severity::CRITICAL,
                           "DatabaseService", "connect");
        ex.addMetadata("server", "db.example.com");
        ex.addMetadata("port", "5432");
        ex.addMetadata("timeout", "30");
        ex.addMetadata("user_id", "12345");
        ex.addMetadata("session_id", "abcdef123456");
        
        throw ex;
    } catch (const AdvancedException& e) {
        cout << e.getFullReport() << endl;
    }
    
    return 0;
}
```

---

## 🎮 Complete Example: E-Commerce System with Custom Exceptions

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <memory>
#include <exception>
#include <stdexcept>
using namespace std;

// E-Commerce exception hierarchy
class ECommerceException : public exception {
protected:
    string message;
    string orderId;
    string userId;
    
public:
    ECommerceException(const string& msg, const string& order = "", const string& user = "")
        : message(msg), orderId(order), userId(user) {}
    
    const char* what() const noexcept override {
        return message.c_str();
    }
    
    const string& getOrderId() const { return orderId; }
    const string& getUserId() const { return userId; }
};

// Inventory exceptions
class InventoryException : public ECommerceException {
private:
    string productId;
    int requestedQuantity;
    int availableQuantity;
    
public:
    InventoryException(const string& msg, const string& prodId, int requested, int available,
                      const string& order = "", const string& user = "")
        : ECommerceException(msg, order, user), productId(prodId),
          requestedQuantity(requested), availableQuantity(available) {}
    
    const string& getProductId() const { return productId; }
    int getRequestedQuantity() const { return requestedQuantity; }
    int getAvailableQuantity() const { return availableQuantity; }
};

class OutOfStockException : public InventoryException {
public:
    OutOfStockException(const string& prodId, int requested, int available,
                       const string& order = "", const string& user = "")
        : InventoryException("Product out of stock", prodId, requested, available, order, user) {}
};

class InsufficientStockException : public InventoryException {
public:
    InsufficientStockException(const string& prodId, int requested, int available,
                             const string& order = "", const string& user = "")
        : InventoryException("Insufficient stock", prodId, requested, available, order, user) {}
};

// Payment exceptions
class PaymentException : public ECommerceException {
private:
    double amount;
    string paymentMethod;
    
public:
    PaymentException(const string& msg, double amt, const string& method,
                    const string& order = "", const string& user = "")
        : ECommerceException(msg, order, user), amount(amt), paymentMethod(method) {}
    
    double getAmount() const { return amount; }
    const string& getPaymentMethod() const { return paymentMethod; }
};

class PaymentDeclinedException : public PaymentException {
private:
    string declineReason;
    
public:
    PaymentDeclinedException(const string& reason, double amt, const string& method,
                           const string& order = "", const string& user = "")
        : PaymentException("Payment declined: " + reason, amt, method, order, user),
          declineReason(reason) {}
    
    const string& getDeclineReason() const { return declineReason; }
};

class InsufficientFundsException : public PaymentException {
private:
    double availableBalance;
    
public:
    InsufficientFundsException(double amt, double available, const string& method,
                             const string& order = "", const string& user = "")
        : PaymentException("Insufficient funds", amt, method, order, user),
          availableBalance(available) {}
    
    double getAvailableBalance() const { return availableBalance; }
};

// Order processing exceptions
class OrderException : public ECommerceException {
private:
    string orderStatus;
    
public:
    OrderException(const string& msg, const string& status,
                  const string& order = "", const string& user = "")
        : ECommerceException(msg, order, user), orderStatus(status) {}
    
    const string& getOrderStatus() const { return orderStatus; }
};

class OrderNotFoundException : public OrderException {
public:
    OrderNotFoundException(const string& orderId, const string& userId = "")
        : OrderException("Order not found", "UNKNOWN", orderId, userId) {}
};

class OrderAlreadyProcessedException : public OrderException {
public:
    OrderAlreadyProcessedException(const string& orderId, const string& status, const string& userId = "")
        : OrderException("Order already processed", status, orderId, userId) {}
};

// Product and Order classes
class Product {
private:
    string id;
    string name;
    double price;
    int stock;
    
public:
    Product(const string& i, const string& n, double p, int s)
        : id(i), name(n), price(p), stock(s) {}
    
    void reserve(int quantity) {
        if (stock <= 0) {
            throw OutOfStockException(id, quantity, 0);
        }
        if (stock < quantity) {
            throw InsufficientStockException(id, quantity, stock);
        }
        stock -= quantity;
    }
    
    void release(int quantity) {
        stock += quantity;
    }
    
    string getId() const { return id; }
    string getName() const { return name; }
    double getPrice() const { return price; }
    int getStock() const { return stock; }
};

class Order {
private:
    string id;
    string userId;
    map<string, int> items; // productId -> quantity
    double totalAmount;
    string status;
    
public:
    Order(const string& orderId, const string& user)
        : id(orderId), userId(user), totalAmount(0.0), status("PENDING") {}
    
    void addItem(const Product& product, int quantity) {
        if (status != "PENDING") {
            throw OrderAlreadyProcessedException(id, status, userId);
        }
        
        items[product.getId()] += quantity;
        totalAmount += product.getPrice() * quantity;
    }
    
    void confirm() {
        if (status != "PENDING") {
            throw OrderAlreadyProcessedException(id, status, userId);
        }
        status = "CONFIRMED";
    }
    
    string getId() const { return id; }
    string getUserId() const { return userId; }
    const map<string, int>& getItems() const { return items; }
    double getTotalAmount() const { return totalAmount; }
    string getStatus() const { return status; }
};

// Payment processor
class PaymentProcessor {
public:
    void processPayment(const string& method, double amount, const string& orderId, const string& userId) {
        if (method == "credit_card") {
            if (amount > 1000) {
                throw PaymentDeclinedException("Credit limit exceeded", amount, method, orderId, userId);
            }
        } else if (method == "paypal") {
            if (amount > 500) {
                throw InsufficientFundsException(amount, 450, method, orderId, userId);
            }
        } else if (method == "declined") {
            throw PaymentDeclinedException("Card declined by bank", amount, method, orderId, userId);
        }
        
        cout << "Payment of $" << amount << " processed via " << method << endl;
    }
};

// E-Commerce system
class ECommerceSystem {
private:
    map<string, unique_ptr<Product>> products;
    map<string, unique_ptr<Order>> orders;
    PaymentProcessor paymentProcessor;
    
public:
    void addProduct(unique_ptr<Product> product) {
        products[product->getId()] = move(product);
    }
    
    Order& createOrder(const string& orderId, const string& userId) {
        if (orders.find(orderId) != orders.end()) {
            throw OrderException("Order already exists", "PENDING", orderId, userId);
        }
        
        orders[orderId] = make_unique<Order>(orderId, userId);
        return *orders[orderId];
    }
    
    void addToOrder(const string& orderId, const string& productId, int quantity) {
        auto orderIt = orders.find(orderId);
        if (orderIt == orders.end()) {
            throw OrderNotFoundException(orderId);
        }
        
        auto productIt = products.find(productId);
        if (productIt == products.end()) {
            throw InventoryException("Product not found", productId, quantity, 0, orderId, orderIt->second->getUserId());
        }
        
        Order& order = *orderIt->second;
        Product& product = *productIt->second;
        
        try {
            product.reserve(quantity);
            order.addItem(product, quantity);
        } catch (const InventoryException& e) {
            // Rollback any previous reservations for this order
            rollbackOrder(order);
            throw;
        }
    }
    
    void processOrder(const string& orderId, const string& paymentMethod) {
        auto orderIt = orders.find(orderId);
        if (orderIt == orders.end()) {
            throw OrderNotFoundException(orderId);
        }
        
        Order& order = *orderIt->second;
        
        try {
            order.confirm();
            paymentProcessor.processPayment(paymentMethod, order.getTotalAmount(), 
                                         orderId, order.getUserId());
            order.status = "COMPLETED";
            cout << "Order " << orderId << " completed successfully" << endl;
        } catch (const PaymentException& e) {
            order.status = "PAYMENT_FAILED";
            rollbackOrder(order);
            throw;
        } catch (const OrderException& e) {
            rollbackOrder(order);
            throw;
        }
    }
    
    void rollbackOrder(Order& order) {
        for (const auto& [productId, quantity] : order.getItems()) {
            auto productIt = products.find(productId);
            if (productIt != products.end()) {
                productIt->second->release(quantity);
            }
        }
    }
    
    void displayOrder(const string& orderId) {
        auto orderIt = orders.find(orderId);
        if (orderIt == orders.end()) {
            throw OrderNotFoundException(orderId);
        }
        
        const Order& order = *orderIt->second;
        cout << "\n=== Order Details ===" << endl;
        cout << "Order ID: " << order.getId() << endl;
        cout << "User ID: " << order.getUserId() << endl;
        cout << "Status: " << order.getStatus() << endl;
        cout << "Total Amount: $" << order.getTotalAmount() << endl;
        cout << "Items:" << endl;
        
        for (const auto& [productId, quantity] : order.getItems()) {
            auto productIt = products.find(productId);
            if (productIt != products.end()) {
                const Product& product = *productIt->second;
                cout << "  " << product.getName() << " (ID: " << productId 
                     << ") - Quantity: " << quantity << " - Price: $" << product.getPrice() << endl;
            }
        }
    }
};

// Exception handler
void handleECommerceException(const ECommerceException& e) {
    cout << "\n=== E-Commerce Exception ===" << endl;
    cout << "Error: " << e.what() << endl;
    
    if (!e.getOrderId().empty()) {
        cout << "Order ID: " << e.getOrderId() << endl;
    }
    if (!e.getUserId().empty()) {
        cout << "User ID: " << e.getUserId() << endl;
    }
    
    // Handle specific exception types
    if (auto stockEx = dynamic_cast<const OutOfStockException*>(&e)) {
        cout << "Type: Out of Stock" << endl;
        cout << "Product ID: " << stockEx->getProductId() << endl;
        cout << "Requested: " << stockEx->getRequestedQuantity() << endl;
        cout << "Available: " << stockEx->getAvailableQuantity() << endl;
    } else if (auto insuffEx = dynamic_cast<const InsufficientStockException*>(&e)) {
        cout << "Type: Insufficient Stock" << endl;
        cout << "Product ID: " << insuffEx->getProductId() << endl;
        cout << "Requested: " << insuffEx->getRequestedQuantity() << endl;
        cout << "Available: " << insuffEx->getAvailableQuantity() << endl;
    } else if (auto paymentEx = dynamic_cast<const PaymentDeclinedException*>(&e)) {
        cout << "Type: Payment Declined" << endl;
        cout << "Amount: $" << paymentEx->getAmount() << endl;
        cout << "Payment Method: " << paymentEx->getPaymentMethod() << endl;
        cout << "Reason: " << paymentEx->getDeclineReason() << endl;
    } else if (auto fundsEx = dynamic_cast<const InsufficientFundsException*>(&e)) {
        cout << "Type: Insufficient Funds" << endl;
        cout << "Amount: $" << fundsEx->getAmount() << endl;
        cout << "Available: $" << fundsEx->getAvailableBalance() << endl;
        cout << "Payment Method: " << fundsEx->getPaymentMethod() << endl;
    } else if (auto orderEx = dynamic_cast<const OrderNotFoundException*>(&e)) {
        cout << "Type: Order Not Found" << endl;
    } else if (auto processedEx = dynamic_cast<const OrderAlreadyProcessedException*>(&e)) {
        cout << "Type: Order Already Processed" << endl;
        cout << "Current Status: " << processedEx->getOrderStatus() << endl;
    }
}

int main() {
    cout << "=== E-Commerce System with Custom Exceptions ===" << endl;
    
    ECommerceSystem system;
    
    // Add products
    system.addProduct(make_unique<Product>("P001", "Laptop", 999.99, 5));
    system.addProduct(make_unique<Product>("P002", "Mouse", 29.99, 10));
    system.addProduct(make_unique<Product>("P003", "Keyboard", 79.99, 0)); // Out of stock
    system.addProduct(make_unique<Product>("P004", "Monitor", 299.99, 2));
    
    // Test different scenarios
    vector<function<void()>> testScenarios = {
        // Scenario 1: Successful order
        [&]() {
            Order& order = system.createOrder("ORDER001", "USER001");
            system.addToOrder("ORDER001", "P001", 1);
            system.addToOrder("ORDER001", "P002", 2);
            system.processOrder("ORDER001", "credit_card");
            system.displayOrder("ORDER001");
        },
        
        // Scenario 2: Out of stock
        [&]() {
            Order& order = system.createOrder("ORDER002", "USER002");
            system.addToOrder("ORDER002", "P003", 1); // Out of stock
        },
        
        // Scenario 3: Insufficient stock
        [&]() {
            Order& order = system.createOrder("ORDER003", "USER003");
            system.addToOrder("ORDER003", "P004", 5); // Only 2 available
        },
        
        // Scenario 4: Payment declined
        [&]() {
            Order& order = system.createOrder("ORDER004", "USER004");
            system.addToOrder("ORDER004", "P001", 2); // $1999.98 > $1000 limit
            system.processOrder("ORDER004", "credit_card");
        },
        
        // Scenario 5: Insufficient funds
        [&]() {
            Order& order = system.createOrder("ORDER005", "USER005");
            system.addToOrder("ORDER005", "P001", 1); // $999.99 > $450 available
            system.processOrder("ORDER005", "paypal");
        },
        
        // Scenario 6: Order not found
        [&]() {
            system.displayOrder("ORDER999");
        }
    };
    
    for (size_t i = 0; i < testScenarios.size(); i++) {
        cout << "\n--- Test Scenario " << (i + 1) << " ---" << endl;
        
        try {
            testScenarios[i]();
        } catch (const ECommerceException& e) {
            handleECommerceException(e);
        } catch (const exception& e) {
            cout << "Unexpected error: " << e.what() << endl;
        }
    }
    
    return 0;
}
```

---

## ⚡ Performance Considerations

### Advantages
- ✅ **Domain Specific**: Tailored to your application's needs
- ✅ **Rich Context**: Can carry relevant error information
- ✅ **Type Safety**: Strong typing for different error categories
- ✅ **Extensible**: Easy to extend and maintain

### Considerations
- ⚠️ **Memory Overhead**: Custom exceptions consume more memory
- ⚠️ **Compilation Time**: More code to compile
- ⚠️ **Binary Size**: Increases executable size
- ⚠️ **Complexity**: May introduce unnecessary complexity

---

## 🐛 Common Pitfalls

| Problem | Solution |
|---------|----------|
| **Too many exception types** | Keep hierarchy simple and logical |
| **Not inheriting from standard exceptions** | Always inherit from `std::exception` or its derivatives |
| **Forgetting `noexcept` on `what()`** | Always mark `what()` as `noexcept` |
| **Throwing by value instead of reference** | Use `throw MyException()` not `throw new MyException()` |
| **Missing copy/move semantics** | Implement proper copy/move constructors if needed |

---

## ✅ Best Practices

1. **Inherit from standard exceptions** for compatibility
2. **Keep exception names descriptive** and clear
3. **Include relevant context** in exception objects
4. **Implement `what()` method** properly with `noexcept`
5. **Use exception chaining** for related errors
6. **Don't over-engineer** - keep it simple
7. **Document exception behavior** and usage

---

## 📚 Related Topics

- [Try-Catch-Throw](01_Try_Catch_Throw.md)
- [Standard Exceptions](02_Standard_Exceptions.md)
- [Exception Specifications](04_Exception_Specifications.md)
- [RAII Pattern](05_RAII.md)

---

## 🚀 Next Steps

Continue learning about:
- **Exception Specifications**: noexcept and exception guarantees
- **RAII Pattern**: Resource management with exceptions
- **Exception Safety Levels**: Basic, strong, and no-throw guarantees
- **Error Handling Strategies**: When to use exceptions vs error codes

---
---

## Next Step

- Go to [04_Exception_Specifications.md](04_Exception_Specifications.md) to continue with Exception Specifications.
