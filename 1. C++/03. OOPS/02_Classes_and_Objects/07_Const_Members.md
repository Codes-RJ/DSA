# Const Members in C++ - Complete Guide

## 📖 Overview

Const members in C++ enforce immutability and const-correctness. They include const member variables, const member functions, const objects, and const references. Const correctness is a fundamental practice in C++ that prevents unintended modifications and enables compiler optimizations.

---

## 🎯 Types of Const Members

| Type | Declaration | Purpose | Restrictions |
|------|-------------|---------|--------------|
| **Const Data Member** | `const int x;` | Immutable per object | Must initialize in initialization list |
| **Const Member Function** | `void func() const;` | Promises not to modify object | Cannot modify non-mutable members |
| **Const Object** | `const Class obj;` | Object cannot be modified | Can only call const member functions |
| **Const Reference** | `const Class& ref;` | Read-only reference | Cannot modify referenced object |
| **Const Pointer** | `const Class* ptr;` | Pointer to const object | Cannot modify pointed object |

---

## 1. **Const Member Variables**

### Definition
Const member variables cannot be modified after object construction. They must be initialized using the constructor initialization list.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Employee {
private:
    const int employeeID;        // Const member - must be initialized
    const string companyName;    // Const member
    string name;
    double salary;
    static const int MAX_EMPLOYEES = 1000;  // Static const - class-level constant
    
public:
    // Const members must be initialized in initialization list
    Employee(int id, string company, string n, double s) 
        : employeeID(id), companyName(company), name(n), salary(s) {
        // employeeID = id;     // Error! Cannot assign in constructor body
        // companyName = company; // Error! Cannot assign in constructor body
    }
    
    // Getter methods (const methods can return const members)
    int getID() const { return employeeID; }
    string getCompany() const { return companyName; }
    string getName() const { return name; }
    double getSalary() const { return salary; }
    
    // Non-const method can modify non-const members
    void setName(string n) { name = n; }
    void setSalary(double s) { 
        if (s >= 0) salary = s;
    }
    
    void display() const {
        cout << "ID: " << employeeID << endl;
        cout << "Company: " << companyName << endl;
        cout << "Name: " << name << endl;
        cout << "Salary: $" << salary << endl;
        cout << "Max Employees: " << MAX_EMPLOYEES << endl;
    }
    
    static int getMaxEmployees() { return MAX_EMPLOYEES; }
};

class Date {
private:
    const int year;      // Const members
    const int month;
    const int day;
    
public:
    // Const members must be initialized in initialization list
    Date(int y, int m, int d) : year(y), month(m), day(d) {
        // Validation can still be done in constructor body
        if (month < 1 || month > 12) {
            throw invalid_argument("Invalid month");
        }
        if (day < 1 || day > 31) {
            throw invalid_argument("Invalid day");
        }
    }
    
    // All getters can be const
    int getYear() const { return year; }
    int getMonth() const { return month; }
    int getDay() const { return day; }
    
    void display() const {
        cout << year << "-" << month << "-" << day << endl;
    }
    
    // Cannot have setters for const members
    // void setYear(int y) { year = y; }  // Error!
};

int main() {
    Employee emp(1001, "TechCorp", "Alice", 75000);
    emp.display();
    
    // Cannot modify const members
    // emp.employeeID = 1002;     // Error! const member
    // emp.companyName = "NewCorp"; // Error! const member
    
    // Can modify non-const members
    emp.setName("Alicia");
    emp.setSalary(80000);
    
    cout << "\nAfter modifications:" << endl;
    emp.display();
    
    // Static const member
    cout << "\nMax Employees: " << Employee::getMaxEmployees() << endl;
    
    // Date example
    Date today(2024, 3, 27);
    cout << "\nToday: ";
    today.display();
    
    return 0;
}
```

**Output:**
```
ID: 1001
Company: TechCorp
Name: Alice
Salary: $75000
Max Employees: 1000

After modifications:
ID: 1001
Company: TechCorp
Name: Alicia
Salary: $80000
Max Employees: 1000

Max Employees: 1000

Today: 2024-3-27
```

---

## 2. **Const Member Functions**

### Definition
Const member functions promise not to modify the object's state. They can be called on const objects and can only modify mutable data members.

```cpp
#include <iostream>
#include <string>
#include <cstring>
using namespace std;

class String {
private:
    char* data;
    size_t length;
    mutable int accessCount;  // mutable - can be modified in const functions
    
public:
    String(const char* str) {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
        accessCount = 0;
    }
    
    ~String() {
        delete[] data;
    }
    
    // Const member functions - cannot modify non-mutable members
    size_t getLength() const {
        accessCount++;  // OK - mutable member
        // length = 0;  // Error! Cannot modify non-mutable
        return length;
    }
    
    char charAt(size_t index) const {
        accessCount++;
        if (index < length) {
            return data[index];
        }
        return '\0';
    }
    
    void display() const {
        cout << "String: " << data << " (length: " << length << ")" << endl;
        cout << "Access count: " << accessCount << endl;
    }
    
    // Non-const member functions - can modify
    void toUpper() {
        for (size_t i = 0; i < length; i++) {
            data[i] = toupper(data[i]);
        }
    }
    
    void setChar(size_t index, char c) {
        if (index < length) {
            data[index] = c;
        }
    }
    
    // Overloaded methods - const and non-const versions
    char& operator[](size_t index) {
        return data[index];
    }
    
    const char& operator[](size_t index) const {
        return data[index];
    }
    
    int getAccessCount() const { return accessCount; }
};

class Rectangle {
private:
    double width;
    double height;
    mutable int computeCount;  // For caching expensive computations
    
public:
    Rectangle(double w, double h) : width(w), height(h), computeCount(0) {}
    
    // Const method - can't modify width/height
    double area() const {
        computeCount++;  // OK - mutable
        return width * height;
    }
    
    double perimeter() const {
        computeCount++;
        return 2 * (width + height);
    }
    
    int getComputeCount() const { return computeCount; }
    
    // Non-const method
    void scale(double factor) {
        width *= factor;
        height *= factor;
    }
    
    void setWidth(double w) { width = w; }
    void setHeight(double h) { height = h; }
    
    double getWidth() const { return width; }
    double getHeight() const { return height; }
};

int main() {
    String s1("Hello");
    const String s2("World");
    
    cout << "=== Const and Non-Const Objects ===" << endl;
    
    // Non-const object can call both const and non-const methods
    s1.display();
    s1.toUpper();          // OK - non-const method
    s1.display();
    
    // Const object can only call const methods
    s2.display();          // OK - const method
    // s2.toUpper();       // Error! Cannot call non-const on const object
    cout << "s2[0] = " << s2[0] << endl;  // OK - const version of operator[]
    
    cout << "\n=== Mutable Member Example ===" << endl;
    Rectangle rect(10, 5);
    const Rectangle rectConst(7, 3);
    
    rect.area();
    rect.perimeter();
    cout << "Rectangle compute count: " << rect.getComputeCount() << endl;
    
    rectConst.area();
    rectConst.perimeter();
    cout << "Const rectangle compute count: " << rectConst.getComputeCount() << endl;
    
    return 0;
}
```

**Output:**
```
=== Const and Non-Const Objects ===
String: Hello (length: 5)
Access count: 0
String: HELLO (length: 5)
Access count: 1
String: World (length: 5)
Access count: 0
s2[0] = W

=== Mutable Member Example ===
Rectangle compute count: 2
Const rectangle compute count: 2
```

---

## 3. **Const Objects**

### Definition
Const objects cannot be modified after creation. They can only call const member functions.

```cpp
#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    double balance;
    mutable int transactionCount;  // mutable for logging
    
public:
    BankAccount(string accNo, double initial) 
        : accountNumber(accNo), balance(initial), transactionCount(0) {}
    
    // Const methods - safe for const objects
    double getBalance() const {
        transactionCount++;  // OK - mutable
        return balance;
    }
    
    string getAccountNumber() const {
        return accountNumber;
    }
    
    int getTransactionCount() const {
        return transactionCount;
    }
    
    void display() const {
        cout << "Account: " << accountNumber << ", Balance: $" << balance << endl;
        cout << "Transactions: " << transactionCount << endl;
    }
    
    // Non-const methods - cannot be called on const objects
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            transactionCount++;
        }
    }
    
    bool withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            transactionCount++;
            return true;
        }
        return false;
    }
};

class ConstDemo {
private:
    int value;
    
public:
    ConstDemo(int v) : value(v) {}
    
    // Const and non-const overloads
    int& get() { return value; }           // Non-const version
    const int& get() const { return value; } // Const version
    
    void set(int v) { value = v; }
    int getValue() const { return value; }
};

void processAccount(const BankAccount& account) {
    // Function takes const reference - can only call const methods
    cout << "Processing account: " << account.getAccountNumber() << endl;
    cout << "Balance: $" << account.getBalance() << endl;
    
    // account.deposit(100);  // Error! Cannot call non-const on const reference
}

int main() {
    // Const object
    const BankAccount constAccount("SAVINGS001", 5000);
    
    cout << "=== Const Object ===" << endl;
    constAccount.display();                    // OK - const method
    cout << "Balance: $" << constAccount.getBalance() << endl;
    
    // constAccount.deposit(100);              // Error! Cannot call non-const
    // constAccount.withdraw(50);              // Error! Cannot call non-const
    
    // Non-const object
    BankAccount account("CHECKING001", 1000);
    
    cout << "\n=== Non-Const Object ===" << endl;
    account.display();                         // OK
    account.deposit(500);                      // OK
    account.withdraw(200);                     // OK
    account.display();
    
    // Passing to function taking const reference
    cout << "\n=== Passing to Const Reference Function ===" << endl;
    processAccount(account);
    processAccount(constAccount);
    
    // Const and non-const overloads
    cout << "\n=== Const/Non-Const Overloads ===" << endl;
    ConstDemo obj(42);
    const ConstDemo constObj(100);
    
    obj.get() = 99;                     // Non-const version - can modify
    cout << "obj.get(): " << obj.get() << endl;
    
    // constObj.get() = 200;            // Error! Const version returns const reference
    cout << "constObj.get(): " << constObj.get() << endl;
    
    return 0;
}
```

**Output:**
```
=== Const Object ===
Account: SAVINGS001, Balance: $5000
Transactions: 0
Balance: $5000

=== Non-Const Object ===
Account: CHECKING001, Balance: $1000
Transactions: 0
Account: CHECKING001, Balance: $1300
Transactions: 2

=== Passing to Const Reference Function ===
Processing account: CHECKING001
Balance: $1300
Processing account: SAVINGS001
Balance: $5000

=== Const/Non-Const Overloads ===
obj.get(): 99
constObj.get(): 100
```

---

## 4. **Const References and Pointers**

### Definition
Const references and pointers provide read-only access to objects, preventing modification through that reference or pointer.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class DataProcessor {
private:
    vector<int> data;
    
public:
    DataProcessor(initializer_list<int> list) : data(list) {}
    
    // Const reference parameter - won't modify
    void process(const vector<int>& input) const {
        // input.push_back(10);  // Error! Cannot modify const reference
        for (int val : input) {
            cout << val << " ";
        }
        cout << endl;
    }
    
    // Const reference return - prevents modification
    const vector<int>& getData() const {
        return data;
    }
    
    // Non-const version - allows modification
    vector<int>& getData() {
        return data;
    }
    
    void display() const {
        for (int val : data) {
            cout << val << " ";
        }
        cout << endl;
    }
    
    void addValue(int val) {
        data.push_back(val);
    }
};

class StringView {
private:
    const string& str;  // Const reference member
    size_t start;
    size_t length;
    
public:
    StringView(const string& s, size_t pos = 0, size_t len = string::npos)
        : str(s), start(pos) {
        length = (len == string::npos) ? str.length() - pos : len;
    }
    
    void display() const {
        for (size_t i = 0; i < length; i++) {
            cout << str[start + i];
        }
        cout << endl;
    }
    
    size_t size() const { return length; }
};

int main() {
    DataProcessor processor({1, 2, 3, 4, 5});
    
    cout << "=== Const Reference Parameters ===" << endl;
    vector<int> input = {10, 20, 30, 40, 50};
    processor.process(input);
    
    cout << "\n=== Const Reference Return ===" << endl;
    const vector<int>& constData = processor.getData();
    // constData.push_back(10);  // Error! Cannot modify const reference
    
    for (int val : constData) {
        cout << val << " ";
    }
    cout << endl;
    
    // Non-const version allows modification
    vector<int>& data = processor.getData();
    data.push_back(6);
    data.push_back(7);
    
    cout << "\nAfter modification:" << endl;
    processor.display();
    
    cout << "\n=== String View Example ===" << endl;
    string text = "Hello, World! This is a long string.";
    StringView view1(text, 0, 5);      // "Hello"
    StringView view2(text, 7, 5);      // "World"
    StringView view3(text, 13);         // Rest of string
    
    view1.display();
    view2.display();
    view3.display();
    
    // Const pointer examples
    cout << "\n=== Const Pointer Examples ===" << endl;
    int value = 42;
    const int* ptrToConst = &value;   // Pointer to const int
    int* const constPtr = &value;     // Const pointer to int
    const int* const constPtrToConst = &value; // Const pointer to const int
    
    // *ptrToConst = 100;    // Error! Cannot modify through pointer to const
    ptrToConst = nullptr;    // OK - pointer itself can be reassigned
    
    *constPtr = 100;         // OK - can modify pointed value
    // constPtr = nullptr;   // Error! Cannot reassign const pointer
    
    cout << "Value after modifications: " << value << endl;
    
    return 0;
}
```

---

## 5. **Const Correctness in Practice**

### Definition
Const correctness is the practice of using the `const` keyword to prevent unintended modifications and document intent.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Library {
private:
    struct Book {
        string title;
        string author;
        int year;
        bool available;
    };
    
    vector<Book> books;
    
public:
    void addBook(string title, string author, int year) {
        books.push_back({title, author, year, true});
    }
    
    // Const member functions - for querying
    vector<string> getAvailableTitles() const {
        vector<string> titles;
        for (const auto& book : books) {
            if (book.available) {
                titles.push_back(book.title);
            }
        }
        return titles;
    }
    
    bool isBookAvailable(const string& title) const {
        auto it = find_if(books.begin(), books.end(),
            [&](const Book& b) { return b.title == title; });
        return it != books.end() && it->available;
    }
    
    void displayAll() const {
        for (const auto& book : books) {
            cout << book.title << " by " << book.author 
                 << " (" << book.year << ") - "
                 << (book.available ? "Available" : "Checked Out") << endl;
        }
    }
    
    // Non-const member functions - for modification
    bool borrowBook(const string& title) {
        auto it = find_if(books.begin(), books.end(),
            [&](Book& b) { return b.title == title && b.available; });
        
        if (it != books.end()) {
            it->available = false;
            return true;
        }
        return false;
    }
    
    bool returnBook(const string& title) {
        auto it = find_if(books.begin(), books.end(),
            [&](Book& b) { return b.title == title && !b.available; });
        
        if (it != books.end()) {
            it->available = true;
            return true;
        }
        return false;
    }
    
    // Const and non-const overloads for element access
    Book& operator[](size_t index) {
        return books[index];
    }
    
    const Book& operator[](size_t index) const {
        return books[index];
    }
    
    size_t size() const { return books.size(); }
};

// Function that takes const reference - promises not to modify
void printLibrary(const Library& lib) {
    cout << "\n=== Library Catalog ===" << endl;
    lib.displayAll();
    
    vector<string> available = lib.getAvailableTitles();
    cout << "\nAvailable titles: ";
    for (const auto& title : available) {
        cout << title << ", ";
    }
    cout << endl;
}

int main() {
    Library library;
    
    // Add books
    library.addBook("The C++ Programming Language", "Bjarne Stroustrup", 2013);
    library.addBook("Effective Modern C++", "Scott Meyers", 2014);
    library.addBook("Clean Code", "Robert Martin", 2008);
    library.addBook("Design Patterns", "Gamma et al.", 1994);
    
    // Const-correct usage
    printLibrary(library);  // Pass by const reference
    
    // Modify the library
    cout << "\n=== Borrowing Books ===" << endl;
    if (library.borrowBook("Effective Modern C++")) {
        cout << "Successfully borrowed 'Effective Modern C++'" << endl;
    }
    
    if (library.borrowBook("The C++ Programming Language")) {
        cout << "Successfully borrowed 'The C++ Programming Language'" << endl;
    }
    
    // Check availability
    cout << "\n=== Checking Availability ===" << endl;
    cout << "'Clean Code' available? " 
         << (library.isBookAvailable("Clean Code") ? "Yes" : "No") << endl;
    cout << "'Effective Modern C++' available? " 
         << (library.isBookAvailable("Effective Modern C++") ? "Yes" : "No") << endl;
    
    // Display updated catalog
    printLibrary(library);
    
    // Return a book
    cout << "\n=== Returning Book ===" << endl;
    if (library.returnBook("Effective Modern C++")) {
        cout << "Successfully returned 'Effective Modern C++'" << endl;
    }
    
    printLibrary(library);
    
    // Const overload example
    const Library& constLib = library;
    const auto& firstBook = constLib[0];  // Calls const version
    // firstBook.available = false;       // Error! const reference
    
    return 0;
}
```

---

## 📊 Const Members Summary

| Const Type | Declaration | Can Modify | Can Call |
|------------|-------------|------------|----------|
| **Const Data Member** | `const int x;` | Never after construction | N/A |
| **Const Member Function** | `void f() const;` | Mutable members only | Only const methods |
| **Const Object** | `const Class obj;` | No modifications | Only const methods |
| **Const Reference** | `const Class& ref;` | No modifications | Only const methods |
| **Const Pointer** | `const Class* ptr;` | Cannot modify object | Only const methods |

---

## ✅ Best Practices

### 1. **Use Const Correctness Everywhere**
```cpp
class Good {
private:
    int data;
    
public:
    int getData() const { return data; }        // ✓ Const getter
    void setData(int d) { data = d; }           // ✓ Non-const setter
    const int& getDataRef() const { return data; } // ✓ Const reference return
};
```

### 2. **Overload for Const and Non-Const**
```cpp
class Container {
    vector<int> data;
    
public:
    int& operator[](size_t i) { return data[i]; }           // Non-const
    const int& operator[](size_t i) const { return data[i]; } // Const
};
```

### 3. **Use Mutable for Caching/Logging**
```cpp
class Expensive {
    mutable int cacheCount;  // ✓ Good for caching
    mutable Logger logger;   // ✓ Good for logging
    
public:
    int compute() const {
        cacheCount++;
        logger.log("Computed");
        return expensiveCalculation();
    }
};
```

### 4. **Pass by Const Reference for Large Objects**
```cpp
void process(const LargeObject& obj) {  // ✓ No copy, no modification
    obj.readOnlyOperation();
}
```

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Const member not initialized** | Compiler error | Use initialization list |
| **Modifying in const function** | Compiler error | Use `mutable` if needed |
| **Const-correctness inconsistency** | Casting away const | Redesign to avoid casting |
| **Const reference to temporary** | Dangling reference | Store by value or ensure lifetime |
| **Forgetting const in getters** | Can't call on const objects | Always mark getters const |

---

## ✅ Key Takeaways

1. **Const data members**: Initialize in initialization list, never modify
2. **Const member functions**: Promise not to modify object, callable on const objects
3. **Const objects**: Cannot be modified, only call const methods
4. **Const references**: Read-only access, prevent copying
5. **Mutable members**: Can be modified in const functions (use sparingly)
6. **Const correctness**: Essential for safe, maintainable code

---
---

## Next Step

- Go to [08_Inline_Functions.md](08_Inline_Functions.md) to continue with Inline Functions.
