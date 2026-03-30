# C++ OOP Projects and Applications - Complete Guide

## 📖 Overview

This section provides complete, real-world projects that demonstrate the practical application of Object-Oriented Programming concepts. Each project showcases different OOP principles and serves as a comprehensive example of how to design and implement systems using C++.

---

## 🎯 Project List

| Project | Key Concepts | Difficulty |
|---------|--------------|------------|
| **Banking System** | Classes, Encapsulation, Inheritance, Polymorphism | Beginner |
| **Library Management** | Composition, Aggregation, File I/O, Exception Handling | Intermediate |
| **Employee Management** | Inheritance, Polymorphism, Abstract Classes | Intermediate |
| **Shape Calculator** | Abstract Classes, Polymorphism, Templates | Beginner |
| **Game Character System** | Inheritance, Polymorphism, Design Patterns | Advanced |

---

## 1. **Banking System**

### Overview
A comprehensive banking system that manages accounts, transactions, and customer information. Demonstrates encapsulation, inheritance, and polymorphism.

### Key Features
- Account types (Savings, Checking, Business)
- Deposit and withdrawal operations
- Interest calculation
- Transaction history
- Customer management

### Code Implementation

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <ctime>
#include <memory>
#include <algorithm>
using namespace std;

// Abstract base class for transactions
class Transaction {
protected:
    double amount_;
    time_t timestamp_;
    string description_;
    
public:
    Transaction(double amount, const string& desc) 
        : amount_(amount), description_(desc) {
        timestamp_ = time(nullptr);
    }
    
    virtual void display() const = 0;
    virtual string getType() const = 0;
    virtual ~Transaction() = default;
    
    double getAmount() const { return amount_; }
    string getDescription() const { return description_; }
};

// Concrete transaction types
class DepositTransaction : public Transaction {
public:
    DepositTransaction(double amount) 
        : Transaction(amount, "Deposit") {}
    
    void display() const override {
        cout << "DEPOSIT: +$" << fixed << setprecision(2) << amount_ 
             << " - " << ctime(&timestamp_);
    }
    
    string getType() const override { return "Deposit"; }
};

class WithdrawalTransaction : public Transaction {
public:
    WithdrawalTransaction(double amount) 
        : Transaction(amount, "Withdrawal") {}
    
    void display() const override {
        cout << "WITHDRAWAL: -$" << fixed << setprecision(2) << amount_ 
             << " - " << ctime(&timestamp_);
    }
    
    string getType() const override { return "Withdrawal"; }
};

class InterestTransaction : public Transaction {
public:
    InterestTransaction(double amount) 
        : Transaction(amount, "Interest") {}
    
    void display() const override {
        cout << "INTEREST: +$" << fixed << setprecision(2) << amount_ 
             << " - " << ctime(&timestamp_);
    }
    
    string getType() const override { return "Interest"; }
};

// Abstract Account class
class Account {
protected:
    string accountNumber_;
    string accountHolder_;
    double balance_;
    vector<unique_ptr<Transaction>> transactions_;
    static int nextAccountNumber_;
    
public:
    Account(const string& holder) 
        : accountNumber_("ACC" + to_string(nextAccountNumber_++)),
          accountHolder_(holder), balance_(0.0) {}
    
    virtual ~Account() = default;
    
    void deposit(double amount) {
        if (amount > 0) {
            balance_ += amount;
            transactions_.push_back(make_unique<DepositTransaction>(amount));
            cout << "Deposited: $" << amount << endl;
        }
    }
    
    virtual bool withdraw(double amount) {
        if (amount > 0 && amount <= balance_) {
            balance_ -= amount;
            transactions_.push_back(make_unique<WithdrawalTransaction>(amount));
            cout << "Withdrawn: $" << amount << endl;
            return true;
        }
        cout << "Insufficient funds!" << endl;
        return false;
    }
    
    virtual void addInterest() = 0;
    
    void displayStatement() const {
        cout << "\n=== Account Statement ===" << endl;
        cout << "Account: " << accountNumber_ << endl;
        cout << "Holder: " << accountHolder_ << endl;
        cout << "Balance: $" << fixed << setprecision(2) << balance_ << endl;
        cout << "\nTransactions:" << endl;
        for (const auto& t : transactions_) {
            t->display();
        }
    }
    
    double getBalance() const { return balance_; }
    string getAccountNumber() const { return accountNumber_; }
    string getAccountHolder() const { return accountHolder_; }
};

int Account::nextAccountNumber_ = 1000;

// Savings Account
class SavingsAccount : public Account {
private:
    double interestRate_;
    
public:
    SavingsAccount(const string& holder, double rate = 0.02) 
        : Account(holder), interestRate_(rate) {}
    
    void addInterest() override {
        double interest = balance_ * interestRate_;
        balance_ += interest;
        transactions_.push_back(make_unique<InterestTransaction>(interest));
        cout << "Interest added: $" << interest << endl;
    }
    
    bool withdraw(double amount) override {
        if (balance_ - amount >= 100) {  // Minimum balance requirement
            return Account::withdraw(amount);
        }
        cout << "Cannot withdraw: Minimum balance of $100 required!" << endl;
        return false;
    }
};

// Checking Account
class CheckingAccount : public Account {
private:
    double overdraftLimit_;
    
public:
    CheckingAccount(const string& holder, double limit = 500) 
        : Account(holder), overdraftLimit_(limit) {}
    
    bool withdraw(double amount) override {
        if (amount > 0 && amount <= balance_ + overdraftLimit_) {
            balance_ -= amount;
            transactions_.push_back(make_unique<WithdrawalTransaction>(amount));
            cout << "Withdrawn: $" << amount << endl;
            if (balance_ < 0) {
                cout << "Overdraft used! Balance: $" << balance_ << endl;
            }
            return true;
        }
        cout << "Withdrawal exceeds overdraft limit!" << endl;
        return false;
    }
    
    void addInterest() override {
        // Checking accounts typically don't earn interest
        cout << "Checking accounts do not earn interest." << endl;
    }
};

// Business Account
class BusinessAccount : public Account {
private:
    double transactionFee_;
    
public:
    BusinessAccount(const string& holder, double fee = 0.50) 
        : Account(holder), transactionFee_(fee) {}
    
    bool withdraw(double amount) override {
        double totalAmount = amount + transactionFee_;
        if (totalAmount > 0 && totalAmount <= balance_) {
            balance_ -= totalAmount;
            transactions_.push_back(make_unique<WithdrawalTransaction>(amount));
            cout << "Withdrawn: $" << amount << " (Fee: $" << transactionFee_ << ")" << endl;
            return true;
        }
        cout << "Insufficient funds (including fee)!" << endl;
        return false;
    }
    
    void addInterest() override {
        double interest = balance_ * 0.01;  // 1% interest
        balance_ += interest;
        transactions_.push_back(make_unique<InterestTransaction>(interest));
        cout << "Business interest added: $" << interest << endl;
    }
};

// Bank class (Facade)
class Bank {
private:
    vector<unique_ptr<Account>> accounts_;
    
public:
    void openSavingsAccount(const string& holder, double rate = 0.02) {
        accounts_.push_back(make_unique<SavingsAccount>(holder, rate));
        cout << "Savings account opened for " << holder << endl;
    }
    
    void openCheckingAccount(const string& holder, double limit = 500) {
        accounts_.push_back(make_unique<CheckingAccount>(holder, limit));
        cout << "Checking account opened for " << holder << endl;
    }
    
    void openBusinessAccount(const string& holder, double fee = 0.50) {
        accounts_.push_back(make_unique<BusinessAccount>(holder, fee));
        cout << "Business account opened for " << holder << endl;
    }
    
    Account* findAccount(const string& accountNumber) {
        for (auto& acc : accounts_) {
            if (acc->getAccountNumber() == accountNumber) {
                return acc.get();
            }
        }
        return nullptr;
    }
    
    void deposit(const string& accountNumber, double amount) {
        auto acc = findAccount(accountNumber);
        if (acc) {
            acc->deposit(amount);
        } else {
            cout << "Account not found!" << endl;
        }
    }
    
    void withdraw(const string& accountNumber, double amount) {
        auto acc = findAccount(accountNumber);
        if (acc) {
            acc->withdraw(amount);
        } else {
            cout << "Account not found!" << endl;
        }
    }
    
    void addInterest(const string& accountNumber) {
        auto acc = findAccount(accountNumber);
        if (acc) {
            acc->addInterest();
        } else {
            cout << "Account not found!" << endl;
        }
    }
    
    void statement(const string& accountNumber) {
        auto acc = findAccount(accountNumber);
        if (acc) {
            acc->displayStatement();
        } else {
            cout << "Account not found!" << endl;
        }
    }
    
    void displayAllAccounts() const {
        cout << "\n=== All Accounts ===" << endl;
        for (const auto& acc : accounts_) {
            cout << acc->getAccountNumber() << " - " << acc->getAccountHolder()
                 << " - Balance: $" << fixed << setprecision(2) << acc->getBalance() << endl;
        }
    }
};

int main() {
    cout << "=== Banking System ===" << endl;
    
    Bank bank;
    
    // Open accounts
    bank.openSavingsAccount("Alice Johnson", 0.03);
    bank.openCheckingAccount("Bob Smith", 1000);
    bank.openBusinessAccount("Charlie Brown", 0.75);
    
    cout << "\n--- Transactions ---" << endl;
    
    // Deposits
    bank.deposit("ACC1000", 1000);
    bank.deposit("ACC1001", 500);
    bank.deposit("ACC1002", 2000);
    
    cout << "\n--- Withdrawals ---" << endl;
    bank.withdraw("ACC1000", 200);
    bank.withdraw("ACC1001", 600);  // Should be allowed (overdraft)
    bank.withdraw("ACC1002", 2500); // Should be allowed
    bank.withdraw("ACC1000", 900);  // Should fail (minimum balance)
    
    cout << "\n--- Interest ---" << endl;
    bank.addInterest("ACC1000");
    bank.addInterest("ACC1001");
    bank.addInterest("ACC1002");
    
    // Statements
    bank.statement("ACC1000");
    bank.statement("ACC1001");
    bank.statement("ACC1002");
    
    bank.displayAllAccounts();
    
    return 0;
}
```

---

## 2. **Library Management System**

### Overview
A library management system that handles books, members, borrowing, and returns. Demonstrates composition, aggregation, file I/O, and exception handling.

### Key Features
- Book catalog management
- Member registration
- Borrow/return books
- Fine calculation for overdue books
- Search functionality

### Code Implementation

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <stdexcept>
#include <chrono>
#include <ctime>
using namespace std;

// Book class
class Book {
private:
    string isbn_;
    string title_;
    string author_;
    int year_;
    bool available_;
    string borrowerId_;
    time_t dueDate_;
    
public:
    Book(string isbn, string title, string author, int year)
        : isbn_(isbn), title_(title), author_(author), year_(year), 
          available_(true), borrowerId_(""), dueDate_(0) {}
    
    string getISBN() const { return isbn_; }
    string getTitle() const { return title_; }
    string getAuthor() const { return author_; }
    int getYear() const { return year_; }
    bool isAvailable() const { return available_; }
    
    bool borrow(const string& memberId, int days = 14) {
        if (!available_) return false;
        available_ = false;
        borrowerId_ = memberId;
        dueDate_ = time(nullptr) + (days * 24 * 60 * 60);
        return true;
    }
    
    bool returnBook() {
        if (available_) return false;
        available_ = true;
        borrowerId_ = "";
        dueDate_ = 0;
        return true;
    }
    
    bool isOverdue() const {
        if (available_) return false;
        return time(nullptr) > dueDate_;
    }
    
    double calculateFine() const {
        if (available_ || !isOverdue()) return 0.0;
        double daysOverdue = difftime(time(nullptr), dueDate_) / (24 * 60 * 60);
        return daysOverdue * 0.50; // $0.50 per day
    }
    
    string getBorrowerId() const { return borrowerId_; }
    time_t getDueDate() const { return dueDate_; }
    
    void display() const {
        cout << "ISBN: " << isbn_ << endl;
        cout << "Title: " << title_ << endl;
        cout << "Author: " << author_ << endl;
        cout << "Year: " << year_ << endl;
        cout << "Status: " << (available_ ? "Available" : "Borrowed");
        if (!available_) {
            cout << " by " << borrowerId_;
            if (isOverdue()) cout << " (OVERDUE!)";
        }
        cout << endl;
    }
};

// Member class
class Member {
private:
    string id_;
    string name_;
    string email_;
    string phone_;
    double fines_;
    vector<string> borrowedBooks_;
    static int nextId_;
    
public:
    Member(string name, string email, string phone)
        : id_("M" + to_string(nextId_++)), name_(name), email_(email), 
          phone_(phone), fines_(0.0) {}
    
    string getId() const { return id_; }
    string getName() const { return name_; }
    string getEmail() const { return email_; }
    double getFines() const { return fines_; }
    
    void addFine(double amount) {
        fines_ += amount;
    }
    
    void payFine(double amount) {
        if (amount > 0 && amount <= fines_) {
            fines_ -= amount;
        }
    }
    
    void borrowBook(const string& isbn) {
        borrowedBooks_.push_back(isbn);
    }
    
    void returnBook(const string& isbn) {
        auto it = find(borrowedBooks_.begin(), borrowedBooks_.end(), isbn);
        if (it != borrowedBooks_.end()) {
            borrowedBooks_.erase(it);
        }
    }
    
    int getBorrowedCount() const {
        return borrowedBooks_.size();
    }
    
    void display() const {
        cout << "ID: " << id_ << endl;
        cout << "Name: " << name_ << endl;
        cout << "Email: " << email_ << endl;
        cout << "Phone: " << phone_ << endl;
        cout << "Fines: $" << fixed << setprecision(2) << fines_ << endl;
        cout << "Books Borrowed: " << borrowedBooks_.size() << endl;
    }
};

int Member::nextId_ = 1000;

// Library class
class Library {
private:
    map<string, Book> books_;
    map<string, Member> members_;
    
public:
    void addBook(const string& isbn, const string& title, 
                 const string& author, int year) {
        if (books_.find(isbn) != books_.end()) {
            throw runtime_error("Book already exists!");
        }
        books_.emplace(isbn, Book(isbn, title, author, year));
        cout << "Book added: " << title << endl;
    }
    
    void addMember(const string& name, const string& email, const string& phone) {
        Member m(name, email, phone);
        members_.emplace(m.getId(), m);
        cout << "Member added: " << name << " (ID: " << m.getId() << ")" << endl;
    }
    
    void borrowBook(const string& memberId, const string& isbn, int days = 14) {
        auto memberIt = members_.find(memberId);
        if (memberIt == members_.end()) {
            throw runtime_error("Member not found!");
        }
        
        auto bookIt = books_.find(isbn);
        if (bookIt == books_.end()) {
            throw runtime_error("Book not found!");
        }
        
        if (!bookIt->second.isAvailable()) {
            throw runtime_error("Book already borrowed!");
        }
        
        if (memberIt->second.getFines() > 0) {
            throw runtime_error("Member has unpaid fines!");
        }
        
        if (memberIt->second.getBorrowedCount() >= 5) {
            throw runtime_error("Maximum books borrowed (5)!");
        }
        
        bookIt->second.borrow(memberId, days);
        memberIt->second.borrowBook(isbn);
        cout << "Book borrowed successfully! Due in " << days << " days." << endl;
    }
    
    void returnBook(const string& memberId, const string& isbn) {
        auto memberIt = members_.find(memberId);
        if (memberIt == members_.end()) {
            throw runtime_error("Member not found!");
        }
        
        auto bookIt = books_.find(isbn);
        if (bookIt == books_.end()) {
            throw runtime_error("Book not found!");
        }
        
        if (bookIt->second.isAvailable()) {
            throw runtime_error("Book is not borrowed!");
        }
        
        double fine = bookIt->second.calculateFine();
        if (fine > 0) {
            memberIt->second.addFine(fine);
            cout << "Late return! Fine added: $" << fine << endl;
        }
        
        bookIt->second.returnBook();
        memberIt->second.returnBook(isbn);
        cout << "Book returned successfully!" << endl;
    }
    
    void searchBooks(const string& query) const {
        cout << "\n=== Search Results ===" << endl;
        bool found = false;
        
        for (const auto& [isbn, book] : books_) {
            if (book.getTitle().find(query) != string::npos ||
                book.getAuthor().find(query) != string::npos) {
                book.display();
                cout << endl;
                found = true;
            }
        }
        
        if (!found) {
            cout << "No books found matching: " << query << endl;
        }
    }
    
    void displayAllBooks() const {
        cout << "\n=== Library Catalog ===" << endl;
        for (const auto& [isbn, book] : books_) {
            book.display();
            cout << endl;
        }
    }
    
    void displayAllMembers() const {
        cout << "\n=== Library Members ===" << endl;
        for (const auto& [id, member] : members_) {
            member.display();
            cout << endl;
        }
    }
    
    void saveToFile(const string& filename) const {
        ofstream file(filename);
        if (!file.is_open()) {
            throw runtime_error("Cannot open file for writing!");
        }
        
        // Save books
        file << "BOOKS\n";
        for (const auto& [isbn, book] : books_) {
            file << isbn << "|" << book.getTitle() << "|" 
                 << book.getAuthor() << "|" << book.getYear() << "\n";
        }
        
        file << "MEMBERS\n";
        for (const auto& [id, member] : members_) {
            file << id << "|" << member.getName() << "|" 
                 << member.getEmail() << "|" << member.getPhone() << "\n";
        }
        
        cout << "Data saved to " << filename << endl;
    }
};

int main() {
    cout << "=== Library Management System ===" << endl;
    
    Library library;
    
    // Add books
    library.addBook("978-0-321-99278-9", "C++ Primer", "Lippman", 2013);
    library.addBook("978-0-201-63361-0", "Design Patterns", "Gamma et al.", 1994);
    library.addBook("978-0-13-235088-4", "Clean Code", "Robert Martin", 2008);
    library.addBook("978-0-596-00571-1", "Head First Design Patterns", "Freeman", 2004);
    
    // Add members
    library.addMember("Alice Johnson", "alice@email.com", "555-0101");
    library.addMember("Bob Smith", "bob@email.com", "555-0102");
    
    // Display catalog
    library.displayAllBooks();
    
    // Borrow books
    cout << "\n--- Borrowing Books ---" << endl;
    try {
        library.borrowBook("M1000", "978-0-321-99278-9", 7);
        library.borrowBook("M1000", "978-0-201-63361-0", 7);
        library.borrowBook("M1001", "978-0-13-235088-4", 7);
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    // Search books
    library.searchBooks("Design");
    library.searchBooks("C++");
    
    // Return book (simulate late return by adjusting time in real implementation)
    cout << "\n--- Returning Books ---" << endl;
    try {
        library.returnBook("M1000", "978-0-321-99278-9");
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    // Display members
    library.displayAllMembers();
    
    // Save data
    library.saveToFile("library_data.txt");
    
    return 0;
}
```

---

## 3. **Employee Management System**

### Overview
A comprehensive employee management system that handles different employee types, payroll, departments, and reports. Demonstrates inheritance, polymorphism, abstract classes, and composition.

### Key Features
- Employee hierarchy (full-time, part-time, contract)
- Salary calculation
- Department management
- Payroll processing
- Performance reviews

### Code Implementation

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <ctime>
#include <memory>
#include <algorithm>
using namespace std;

// Abstract Employee class
class Employee {
protected:
    int id_;
    string name_;
    string department_;
    time_t hireDate_;
    bool active_;
    static int nextId_;
    
    string formatDate(time_t t) const {
        struct tm* timeinfo = localtime(&t);
        char buffer[20];
        strftime(buffer, sizeof(buffer), "%Y-%m-%d", timeinfo);
        return string(buffer);
    }
    
public:
    Employee(string name, string dept) 
        : id_(nextId_++), name_(name), department_(dept), active_(true) {
        hireDate_ = time(nullptr);
    }
    
    virtual ~Employee() = default;
    
    virtual double calculateSalary() const = 0;
    virtual double calculateBonus() const = 0;
    virtual void display() const = 0;
    
    int getId() const { return id_; }
    string getName() const { return name_; }
    string getDepartment() const { return department_; }
    bool isActive() const { return active_; }
    
    void setDepartment(const string& dept) { department_ = dept; }
    void terminate() { active_ = false; }
    
    void displayBasic() const {
        cout << "ID: " << id_ << ", Name: " << name_ 
             << ", Dept: " << department_ 
             << ", Hired: " << formatDate(hireDate_)
             << ", Status: " << (active_ ? "Active" : "Terminated") << endl;
    }
};

int Employee::nextId_ = 1000;

// Full-time Employee
class FullTimeEmployee : public Employee {
private:
    double baseSalary_;
    double bonus_;
    
public:
    FullTimeEmployee(string name, string dept, double salary) 
        : Employee(name, dept), baseSalary_(salary), bonus_(0) {}
    
    double calculateSalary() const override {
        return baseSalary_;
    }
    
    double calculateBonus() const override {
        return baseSalary_ * 0.10;  // 10% annual bonus
    }
    
    void giveRaise(double percent) {
        if (percent > 0) {
            baseSalary_ += baseSalary_ * (percent / 100);
        }
    }
    
    void setBonus(double bonus) {
        bonus_ = bonus;
    }
    
    void display() const override {
        displayBasic();
        cout << "  Type: Full-time" << endl;
        cout << "  Base Salary: $" << fixed << setprecision(2) << baseSalary_ << endl;
        cout << "  Bonus: $" << bonus_ << endl;
        cout << "  Total Compensation: $" << calculateSalary() + calculateBonus() + bonus_ << endl;
    }
};

// Part-time Employee
class PartTimeEmployee : public Employee {
private:
    double hourlyRate_;
    int hoursPerWeek_;
    
public:
    PartTimeEmployee(string name, string dept, double rate, int hours) 
        : Employee(name, dept), hourlyRate_(rate), hoursPerWeek_(hours) {}
    
    double calculateSalary() const override {
        return hourlyRate_ * hoursPerWeek_ * 52;  // Annual salary
    }
    
    double calculateBonus() const override {
        return 0;  // No bonus for part-time
    }
    
    void setHours(int hours) {
        hoursPerWeek_ = hours;
    }
    
    void display() const override {
        displayBasic();
        cout << "  Type: Part-time" << endl;
        cout << "  Hourly Rate: $" << fixed << setprecision(2) << hourlyRate_ << endl;
        cout << "  Hours/Week: " << hoursPerWeek_ << endl;
        cout << "  Annual Salary: $" << calculateSalary() << endl;
    }
};

// Contract Employee
class ContractEmployee : public Employee {
private:
    double contractAmount_;
    int durationMonths_;
    
public:
    ContractEmployee(string name, string dept, double amount, int months) 
        : Employee(name, dept), contractAmount_(amount), durationMonths_(months) {}
    
    double calculateSalary() const override {
        return contractAmount_ / durationMonths_ * 12;  // Annualized
    }
    
    double calculateBonus() const override {
        return contractAmount_ * 0.05;  // 5% completion bonus
    }
    
    void display() const override {
        displayBasic();
        cout << "  Type: Contract" << endl;
        cout << "  Contract Amount: $" << fixed << setprecision(2) << contractAmount_ << endl;
        cout << "  Duration: " << durationMonths_ << " months" << endl;
        cout << "  Annualized Salary: $" << calculateSalary() << endl;
    }
};

// Department class
class Department {
private:
    string name_;
    vector<shared_ptr<Employee>> employees_;
    double budget_;
    
public:
    Department(string name, double budget) : name_(name), budget_(budget) {}
    
    void addEmployee(shared_ptr<Employee> emp) {
        employees_.push_back(emp);
        cout << emp->getName() << " added to " << name_ << " department" << endl;
    }
    
    void removeEmployee(int id) {
        auto it = find_if(employees_.begin(), employees_.end(),
            [id](const auto& emp) { return emp->getId() == id; });
        if (it != employees_.end()) {
            employees_.erase(it);
        }
    }
    
    double getTotalSalary() const {
        double total = 0;
        for (const auto& emp : employees_) {
            if (emp->isActive()) {
                total += emp->calculateSalary();
            }
        }
        return total;
    }
    
    double getRemainingBudget() const {
        return budget_ - getTotalSalary();
    }
    
    void display() const {
        cout << "\n=== " << name_ << " Department ===" << endl;
        cout << "Budget: $" << fixed << setprecision(2) << budget_ << endl;
        cout << "Salary Cost: $" << getTotalSalary() << endl;
        cout << "Remaining: $" << getRemainingBudget() << endl;
        cout << "Employees (" << employees_.size() << "):" << endl;
        for (const auto& emp : employees_) {
            emp->displayBasic();
        }
    }
    
    void displayDetails() const {
        cout << "\n=== " << name_ << " Department Details ===" << endl;
        for (const auto& emp : employees_) {
            emp->display();
            cout << endl;
        }
    }
};

// Payroll class
class Payroll {
private:
    struct Payment {
        int employeeId;
        string name;
        double amount;
        time_t date;
    };
    vector<Payment> history_;
    
public:
    void processPayroll(const vector<shared_ptr<Employee>>& employees) {
        cout << "\n=== Processing Payroll ===" << endl;
        double total = 0;
        time_t now = time(nullptr);
        
        for (const auto& emp : employees) {
            if (emp->isActive()) {
                double salary = emp->calculateSalary() / 12;  // Monthly salary
                total += salary;
                history_.push_back({emp->getId(), emp->getName(), salary, now});
                cout << emp->getName() << ": $" << fixed << setprecision(2) << salary << endl;
            }
        }
        
        cout << "Total Payroll: $" << total << endl;
    }
    
    void processBonuses(const vector<shared_ptr<Employee>>& employees) {
        cout << "\n=== Processing Annual Bonuses ===" << endl;
        double total = 0;
        
        for (const auto& emp : employees) {
            if (emp->isActive()) {
                double bonus = emp->calculateBonus();
                total += bonus;
                cout << emp->getName() << ": $" << fixed << setprecision(2) << bonus << endl;
            }
        }
        
        cout << "Total Bonuses: $" << total << endl;
    }
    
    void displayHistory() const {
        cout << "\n=== Payment History ===" << endl;
        for (const auto& payment : history_) {
            cout << payment.name << " (ID: " << payment.employeeId 
                 << ") - $" << fixed << setprecision(2) << payment.amount << endl;
        }
    }
};

// Company class
class Company {
private:
    string name_;
    vector<shared_ptr<Employee>> employees_;
    vector<Department> departments_;
    Payroll payroll_;
    
public:
    Company(string name) : name_(name) {}
    
    void addDepartment(const string& name, double budget) {
        departments_.emplace_back(name, budget);
    }
    
    void hireEmployee(shared_ptr<Employee> emp, const string& deptName) {
        employees_.push_back(emp);
        
        auto deptIt = find_if(departments_.begin(), departments_.end(),
            [&deptName](const Department& d) { return d.getName() == deptName; });
        if (deptIt != departments_.end()) {
            deptIt->addEmployee(emp);
        }
    }
    
    void processPayroll() {
        payroll_.processPayroll(employees_);
    }
    
    void processBonuses() {
        payroll_.processBonuses(employees_);
    }
    
    void displayOrganization() const {
        cout << "\n=== " << name_ << " Organization ===" << endl;
        for (const auto& dept : departments_) {
            dept.display();
        }
    }
    
    void displayDetails() const {
        for (const auto& dept : departments_) {
            dept.displayDetails();
        }
    }
    
    void showPayrollHistory() const {
        payroll_.displayHistory();
    }
};

int main() {
    cout << "=== Employee Management System ===" << endl;
    
    Company company("Tech Corp");
    
    // Add departments
    company.addDepartment("Engineering", 500000);
    company.addDepartment("Sales", 300000);
    company.addDepartment("Marketing", 200000);
    
    // Hire employees
    auto alice = make_shared<FullTimeEmployee>("Alice Johnson", "Engineering", 85000);
    auto bob = make_shared<FullTimeEmployee>("Bob Smith", "Sales", 75000);
    auto charlie = make_shared<PartTimeEmployee>("Charlie Brown", "Engineering", 35, 20);
    auto diana = make_shared<ContractEmployee>("Diana Prince", "Marketing", 50000, 6);
    
    company.hireEmployee(alice, "Engineering");
    company.hireEmployee(bob, "Sales");
    company.hireEmployee(charlie, "Engineering");
    company.hireEmployee(diana, "Marketing");
    
    // Give raises
    alice->giveRaise(10);
    bob->giveRaise(5);
    
    // Display organization
    company.displayOrganization();
    
    // Process payroll
    company.processPayroll();
    company.processBonuses();
    
    // Display detailed employee info
    company.displayDetails();
    
    // Show payroll history
    company.showPayrollHistory();
    
    return 0;
}
```

---

## 4. **Shape Calculator System**

### Overview
A shape calculator that demonstrates polymorphism, abstract classes, and templates. Calculates area, perimeter, and volume for various shapes.

### Key Features
- Multiple shape types (2D and 3D)
- Area and perimeter calculations
- Volume calculations for 3D shapes
- Template-based calculations
- Shape collections

### Code Implementation

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <cmath>
#include <numbers>
#include <algorithm>
using namespace std;

// Abstract 2D Shape class
class Shape2D {
protected:
    string name_;
    
public:
    Shape2D(const string& name) : name_(name) {}
    virtual ~Shape2D() = default;
    
    virtual double area() const = 0;
    virtual double perimeter() const = 0;
    virtual void draw() const = 0;
    
    string getName() const { return name_; }
};

// Circle class
class Circle : public Shape2D {
private:
    double radius_;
    
public:
    Circle(double radius) : Shape2D("Circle"), radius_(radius) {}
    
    double area() const override {
        return numbers::pi * radius_ * radius_;
    }
    
    double perimeter() const override {
        return 2 * numbers::pi * radius_;
    }
    
    void draw() const override {
        cout << "Drawing circle with radius " << radius_ << endl;
    }
    
    double getRadius() const { return radius_; }
};

// Rectangle class
class Rectangle : public Shape2D {
private:
    double width_;
    double height_;
    
public:
    Rectangle(double width, double height) 
        : Shape2D("Rectangle"), width_(width), height_(height) {}
    
    double area() const override {
        return width_ * height_;
    }
    
    double perimeter() const override {
        return 2 * (width_ + height_);
    }
    
    void draw() const override {
        cout << "Drawing rectangle " << width_ << "x" << height_ << endl;
    }
};

// Triangle class
class Triangle : public Shape2D {
private:
    double side1_, side2_, side3_;
    
public:
    Triangle(double a, double b, double c) 
        : Shape2D("Triangle"), side1_(a), side2_(b), side3_(c) {}
    
    double area() const override {
        double s = (side1_ + side2_ + side3_) / 2;
        return sqrt(s * (s - side1_) * (s - side2_) * (s - side3_));
    }
    
    double perimeter() const override {
        return side1_ + side2_ + side3_;
    }
    
    void draw() const override {
        cout << "Drawing triangle with sides " << side1_ << ", " 
             << side2_ << ", " << side3_ << endl;
    }
};

// Square class (derived from Rectangle)
class Square : public Rectangle {
public:
    Square(double side) : Rectangle(side, side) {
        name_ = "Square";
    }
    
    void draw() const override {
        cout << "Drawing square with side " << getWidth() << endl;
    }
};

// Abstract 3D Shape class
class Shape3D : public Shape2D {
public:
    Shape3D(const string& name) : Shape2D(name) {}
    
    virtual double volume() const = 0;
    virtual double surfaceArea() const = 0;
};

// Cube class
class Cube : public Shape3D {
private:
    double side_;
    
public:
    Cube(double side) : Shape3D("Cube"), side_(side) {}
    
    double area() const override {
        return side_ * side_;  // Face area
    }
    
    double perimeter() const override {
        return 4 * side_;  // Perimeter of one face
    }
    
    double volume() const override {
        return side_ * side_ * side_;
    }
    
    double surfaceArea() const override {
        return 6 * side_ * side_;
    }
    
    void draw() const override {
        cout << "Drawing cube with side " << side_ << endl;
    }
};

// Sphere class
class Sphere : public Shape3D {
private:
    double radius_;
    
public:
    Sphere(double radius) : Shape3D("Sphere"), radius_(radius) {}
    
    double area() const override {
        return numbers::pi * radius_ * radius_;  // Great circle area
    }
    
    double perimeter() const override {
        return 2 * numbers::pi * radius_;  // Great circle circumference
    }
    
    double volume() const override {
        return (4.0 / 3.0) * numbers::pi * radius_ * radius_ * radius_;
    }
    
    double surfaceArea() const override {
        return 4 * numbers::pi * radius_ * radius_;
    }
    
    void draw() const override {
        cout << "Drawing sphere with radius " << radius_ << endl;
    }
};

// Cylinder class
class Cylinder : public Shape3D {
private:
    double radius_;
    double height_;
    
public:
    Cylinder(double radius, double height) 
        : Shape3D("Cylinder"), radius_(radius), height_(height) {}
    
    double area() const override {
        return numbers::pi * radius_ * radius_;  // Base area
    }
    
    double perimeter() const override {
        return 2 * numbers::pi * radius_;  // Base circumference
    }
    
    double volume() const override {
        return numbers::pi * radius_ * radius_ * height_;
    }
    
    double surfaceArea() const override {
        return 2 * numbers::pi * radius_ * (radius_ + height_);
    }
    
    void draw() const override {
        cout << "Drawing cylinder with radius " << radius_ 
             << " and height " << height_ << endl;
    }
};

// Shape calculator template
template<typename T>
class ShapeCalculator {
private:
    vector<unique_ptr<T>> shapes_;
    
public:
    void addShape(T* shape) {
        shapes_.emplace_back(shape);
    }
    
    double totalArea() const {
        double total = 0;
        for (const auto& shape : shapes_) {
            total += shape->area();
        }
        return total;
    }
    
    double totalPerimeter() const {
        double total = 0;
        for (const auto& shape : shapes_) {
            total += shape->perimeter();
        }
        return total;
    }
    
    void drawAll() const {
        for (const auto& shape : shapes_) {
            shape->draw();
        }
    }
    
    void displayStats() const {
        cout << "\n=== Shape Statistics ===" << endl;
        for (const auto& shape : shapes_) {
            cout << shape->getName() << ":" << endl;
            cout << "  Area: " << shape->area() << endl;
            cout << "  Perimeter: " << shape->perimeter() << endl;
            if constexpr (is_base_of_v<Shape3D, T>) {
                auto* shape3D = dynamic_cast<Shape3D*>(shape.get());
                if (shape3D) {
                    cout << "  Volume: " << shape3D->volume() << endl;
                    cout << "  Surface Area: " << shape3D->surfaceArea() << endl;
                }
            }
        }
    }
};

int main() {
    cout << "=== Shape Calculator System ===" << endl;
    
    // 2D Shapes
    ShapeCalculator<Shape2D> calculator2D;
    calculator2D.addShape(new Circle(5.0));
    calculator2D.addShape(new Rectangle(4.0, 6.0));
    calculator2D.addShape(new Triangle(3.0, 4.0, 5.0));
    calculator2D.addShape(new Square(7.0));
    
    cout << "\n2D Shapes:" << endl;
    calculator2D.drawAll();
    calculator2D.displayStats();
    cout << "\nTotal Area: " << calculator2D.totalArea() << endl;
    cout << "Total Perimeter: " << calculator2D.totalPerimeter() << endl;
    
    // 3D Shapes
    ShapeCalculator<Shape3D> calculator3D;
    calculator3D.addShape(new Cube(3.0));
    calculator3D.addShape(new Sphere(4.0));
    calculator3D.addShape(new Cylinder(2.0, 5.0));
    
    cout << "\n3D Shapes:" << endl;
    calculator3D.drawAll();
    calculator3D.displayStats();
    
    return 0;
}
```

---

## 5. **Game Character System**

### Overview
A game character system demonstrating inheritance, polymorphism, and design patterns. Features different character classes, abilities, combat system, and level progression.

### Key Features
- Character classes (Warrior, Mage, Archer)
- Combat system
- Level progression
- Ability system
- Equipment management

### Code Implementation

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <map>
#include <random>
#include <algorithm>
using namespace std;

// Ability class
class Ability {
private:
    string name_;
    string description_;
    int damage_;
    int manaCost_;
    int cooldown_;
    int currentCooldown_;
    
public:
    Ability(string name, string desc, int damage, int manaCost, int cooldown)
        : name_(name), description_(desc), damage_(damage), manaCost_(manaCost),
          cooldown_(cooldown), currentCooldown_(0) {}
    
    bool canUse(int mana) const {
        return currentCooldown_ == 0 && mana >= manaCost_;
    }
    
    void use() {
        currentCooldown_ = cooldown_;
    }
    
    void updateCooldown() {
        if (currentCooldown_ > 0) {
            currentCooldown_--;
        }
    }
    
    int getDamage() const { return damage_; }
    int getManaCost() const { return manaCost_; }
    string getName() const { return name_; }
    string getDescription() const { return description_; }
};

// Equipment class
class Equipment {
private:
    string name_;
    int attackBonus_;
    int defenseBonus_;
    int healthBonus_;
    
public:
    Equipment(string name, int attack, int defense, int health)
        : name_(name), attackBonus_(attack), defenseBonus_(defense), healthBonus_(health) {}
    
    int getAttackBonus() const { return attackBonus_; }
    int getDefenseBonus() const { return defenseBonus_; }
    int getHealthBonus() const { return healthBonus_; }
    string getName() const { return name_; }
};

// Abstract Character class
class Character {
protected:
    string name_;
    int level_;
    int health_;
    int maxHealth_;
    int mana_;
    int maxMana_;
    int attack_;
    int defense_;
    vector<Ability> abilities_;
    map<string, Equipment> equipment_;
    
public:
    Character(string name, int health, int mana, int attack, int defense)
        : name_(name), level_(1), health_(health), maxHealth_(health),
          mana_(mana), maxMana_(mana), attack_(attack), defense_(defense) {}
    
    virtual ~Character() = default;
    
    virtual void attack(Character& target) = 0;
    virtual void levelUp() = 0;
    virtual void display() const = 0;
    
    void takeDamage(int damage) {
        int actualDamage = max(1, damage - defense_ / 2);
        health_ -= actualDamage;
        cout << name_ << " takes " << actualDamage << " damage! Health: " 
             << max(0, health_) << "/" << maxHealth_ << endl;
    }
    
    void heal(int amount) {
        health_ = min(maxHealth_, health_ + amount);
        cout << name_ << " heals for " << amount << "! Health: " 
             << health_ << "/" << maxHealth_ << endl;
    }
    
    void restoreMana(int amount) {
        mana_ = min(maxMana_, mana_ + amount);
    }
    
    bool isAlive() const { return health_ > 0; }
    
    void equip(const Equipment& equip) {
        equipment_[equip.getName()] = equip;
        attack_ += equip.getAttackBonus();
        defense_ += equip.getDefenseBonus();
        maxHealth_ += equip.getHealthBonus();
        health_ += equip.getHealthBonus();
        cout << name_ << " equipped " << equip.getName() << endl;
    }
    
    void updateCooldowns() {
        for (auto& ability : abilities_) {
            ability.updateCooldown();
        }
    }
    
    bool useAbility(int index, Character& target) {
        if (index < 0 || index >= abilities_.size()) return false;
        
        Ability& ability = abilities_[index];
        if (ability.canUse(mana_)) {
            mana_ -= ability.getManaCost();
            ability.use();
            target.takeDamage(ability.getDamage());
            cout << name_ << " uses " << ability.getName() << "!" << endl;
            return true;
        }
        return false;
    }
    
    void addAbility(const Ability& ability) {
        abilities_.push_back(ability);
    }
    
    void displayAbilities() const {
        cout << "\nAbilities:" << endl;
        for (size_t i = 0; i < abilities_.size(); i++) {
            cout << "  " << i + 1 << ". " << abilities_[i].getName() 
                 << " (" << abilities_[i].getManaCost() << " mana)" << endl;
            cout << "     " << abilities_[i].getDescription() << endl;
        }
    }
    
    string getName() const { return name_; }
    int getHealth() const { return health_; }
    int getMana() const { return mana_; }
};

// Warrior class
class Warrior : public Character {
private:
    int rage_;
    
public:
    Warrior(string name) 
        : Character(name, 150, 50, 25, 20), rage_(0) {
        addAbility(Ability("Slash", "A powerful slash attack", 30, 10, 2));
        addAbility(Ability("Shield Bash", "Stuns and damages enemy", 25, 15, 3));
        addAbility(Ability("Whirlwind", "Damages all enemies", 20, 20, 4));
        addAbility(Ability("Rage", "Increases damage temporarily", 0, 20, 5));
    }
    
    void attack(Character& target) override {
        int damage = attack_ + rage_;
        target.takeDamage(damage);
        rage_ += 5;
        cout << name_ << " attacks with sword for " << damage << " damage!" << endl;
    }
    
    void levelUp() override {
        level_++;
        maxHealth_ += 20;
        health_ = maxHealth_;
        maxMana_ += 5;
        mana_ = maxMana_;
        attack_ += 3;
        defense_ += 2;
        cout << name_ << " leveled up to level " << level_ << "!" << endl;
    }
    
    void display() const override {
        cout << "\n=== Warrior: " << name_ << " ===" << endl;
        cout << "Level: " << level_ << endl;
        cout << "Health: " << health_ << "/" << maxHealth_ << endl;
        cout << "Mana: " << mana_ << "/" << maxMana_ << endl;
        cout << "Attack: " << attack_ << ", Defense: " << defense_ << endl;
        cout << "Rage: " << rage_ << endl;
        displayAbilities();
    }
};

// Mage class
class Mage : public Character {
public:
    Mage(string name) 
        : Character(name, 100, 150, 15, 10) {
        addAbility(Ability("Fireball", "Hurls a ball of fire", 40, 20, 3));
        addAbility(Ability("Ice Bolt", "Freezes the enemy", 30, 15, 2));
        addAbility(Ability("Lightning", "Strikes with lightning", 50, 25, 4));
        addAbility(Ability("Arcane Shield", "Protects from damage", 0, 30, 5));
    }
    
    void attack(Character& target) override {
        int damage = attack_ + 10;
        target.takeDamage(damage);
        cout << name_ << " casts magic missile for " << damage << " damage!" << endl;
    }
    
    void levelUp() override {
        level_++;
        maxHealth_ += 10;
        health_ = maxHealth_;
        maxMana_ += 20;
        mana_ = maxMana_;
        attack_ += 2;
        defense_ += 1;
        cout << name_ << " leveled up to level " << level_ << "!" << endl;
    }
    
    void display() const override {
        cout << "\n=== Mage: " << name_ << " ===" << endl;
        cout << "Level: " << level_ << endl;
        cout << "Health: " << health_ << "/" << maxHealth_ << endl;
        cout << "Mana: " << mana_ << "/" << maxMana_ << endl;
        cout << "Attack: " << attack_ << ", Defense: " << defense_ << endl;
        displayAbilities();
    }
};

// Archer class
class Archer : public Character {
private:
    int focus_;
    
public:
    Archer(string name) 
        : Character(name, 120, 80, 22, 15), focus_(0) {
        addAbility(Ability("Arrow Shot", "Precise arrow strike", 35, 15, 2));
        addAbility(Ability("Multi-Shot", "Fires multiple arrows", 25, 20, 3));
        addAbility(Ability("Poison Arrow", "Damages over time", 20, 15, 4));
        addAbility(Ability("Eagle Eye", "Increases critical chance", 0, 25, 5));
    }
    
    void attack(Character& target) override {
        int damage = attack_ + focus_ / 2;
        target.takeDamage(damage);
        focus_ = min(50, focus_ + 5);
        cout << name_ << " fires an arrow for " << damage << " damage!" << endl;
    }
    
    void levelUp() override {
        level_++;
        maxHealth_ += 15;
        health_ = maxHealth_;
        maxMana_ += 10;
        mana_ = maxMana_;
        attack_ += 3;
        defense_ += 2;
        cout << name_ << " leveled up to level " << level_ << "!" << endl;
    }
    
    void display() const override {
        cout << "\n=== Archer: " << name_ << " ===" << endl;
        cout << "Level: " << level_ << endl;
        cout << "Health: " << health_ << "/" << maxHealth_ << endl;
        cout << "Mana: " << mana_ << "/" << maxMana_ << endl;
        cout << "Attack: " << attack_ << ", Defense: " << defense_ << endl;
        cout << "Focus: " << focus_ << endl;
        displayAbilities();
    }
};

// Combat class
class Combat {
private:
    unique_ptr<Character> player_;
    vector<unique_ptr<Character>> enemies_;
    random_device rd_;
    mt19937 gen_;
    
public:
    Combat(Character* player) : player_(player), gen_(rd_) {}
    
    void addEnemy(Character* enemy) {
        enemies_.emplace_back(enemy);
    }
    
    void start() {
        cout << "\n=== Combat Started! ===" << endl;
        cout << player_->getName() << " vs " << enemies_.size() << " enemies" << endl;
        
        while (player_->isAlive() && !enemies_.empty()) {
            displayStatus();
            playerTurn();
            if (!enemies_.empty()) {
                enemyTurn();
            }
            updateCooldowns();
        }
        
        if (player_->isAlive()) {
            cout << "\n=== Victory! ===" << endl;
            player_->levelUp();
        } else {
            cout << "\n=== Defeat! ===" << endl;
        }
    }
    
private:
    void displayStatus() {
        cout << "\n--- Player Status ---" << endl;
        cout << player_->getName() << ": HP " << player_->getHealth() 
             << "/? MP " << player_->getMana() << "/?" << endl;
        cout << "--- Enemies ---" << endl;
        for (size_t i = 0; i < enemies_.size(); i++) {
            cout << i + 1 << ". " << enemies_[i]->getName() 
                 << ": HP " << enemies_[i]->getHealth() << "/?" << endl;
        }
    }
    
    void playerTurn() {
        cout << "\nYour turn!" << endl;
        int choice;
        do {
            cout << "1. Attack" << endl;
            cout << "2. Use Ability" << endl;
            cout << "3. Pass" << endl;
            cout << "Choice: ";
            cin >> choice;
        } while (choice < 1 || choice > 3);
        
        if (choice == 1) {
            int target = selectTarget();
            player_->attack(*enemies_[target]);
            if (!enemies_[target]->isAlive()) {
                cout << enemies_[target]->getName() << " defeated!" << endl;
                enemies_.erase(enemies_.begin() + target);
            }
        } else if (choice == 2) {
            player_->displayAbilities();
            int ability;
            cout << "Select ability: ";
            cin >> ability;
            int target = selectTarget();
            if (player_->useAbility(ability - 1, *enemies_[target])) {
                if (!enemies_[target]->isAlive()) {
                    cout << enemies_[target]->getName() << " defeated!" << endl;
                    enemies_.erase(enemies_.begin() + target);
                }
            } else {
                cout << "Cannot use ability!" << endl;
            }
        }
    }
    
    void enemyTurn() {
        cout << "\nEnemy turn!" << endl;
        for (auto& enemy : enemies_) {
            if (enemy->isAlive()) {
                enemy->attack(*player_);
            }
        }
    }
    
    void updateCooldowns() {
        player_->updateCooldowns();
        for (auto& enemy : enemies_) {
            enemy->updateCooldowns();
        }
    }
    
    int selectTarget() {
        if (enemies_.size() == 1) return 0;
        int target;
        do {
            cout << "Select target (1-" << enemies_.size() << "): ";
            cin >> target;
        } while (target < 1 || target > enemies_.size());
        return target - 1;
    }
};

int main() {
    cout << "=== Game Character System ===" << endl;
    
    // Create equipment
    Equipment sword("Excalibur", 10, 0, 20);
    Equipment shield("Aegis", 0, 8, 15);
    Equipment staff("Staff of Wisdom", 5, 2, 10);
    
    // Create characters
    Warrior warrior("Conan");
    Mage mage("Gandalf");
    Archer archer("Legolas");
    
    // Equip items
    warrior.equip(sword);
    warrior.equip(shield);
    mage.equip(staff);
    
    // Display characters
    warrior.display();
    mage.display();
    archer.display();
    
    // Create combat
    Combat combat(&warrior);
    combat.addEnemy(new Warrior("Orc Warrior"));
    combat.addEnemy(new Mage("Dark Mage"));
    combat.addEnemy(new Archer("Goblin Archer"));
    
    // Start combat
    combat.start();
    
    return 0;
}
```

---

## 📊 Project Summary

| Project | Key Concepts | Lines of Code | Learning Outcomes |
|---------|--------------|---------------|-------------------|
| **Banking System** | Inheritance, Polymorphism | ~350 | Account management, transactions |
| **Library Management** | Composition, File I/O | ~400 | Data persistence, search |
| **Employee Management** | Abstract Classes, Payroll | ~450 | Salary calculation, reporting |
| **Shape Calculator** | Templates, Polymorphism | ~300 | Geometric calculations |
| **Game Character System** | Design Patterns, Combat | ~500 | Game mechanics, AI |

---

## ✅ Key Takeaways

1. **Real-world applications** demonstrate OOP principles
2. **Inheritance** creates hierarchical relationships
3. **Polymorphism** enables flexible, extensible code
4. **Encapsulation** protects data integrity
5. **Composition** builds complex objects from simpler ones
6. **Design patterns** solve common design problems
7. **Error handling** ensures robust applications

---