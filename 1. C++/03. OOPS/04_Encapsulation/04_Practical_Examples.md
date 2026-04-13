# Encapsulation - Practical Examples

## 📖 Overview

This section provides real-world practical examples demonstrating encapsulation concepts in action. Each example shows how encapsulation is applied in actual software development scenarios, including validation, business logic, and data protection.

---

## 1. **Student Management System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;

class Student {
private:
    int rollNumber;
    string name;
    vector<double> marks;
    double attendancePercentage;
    bool isActive;
    static int nextRollNumber;
    
    // Private helper methods
    double calculateAverage() const {
        if (marks.empty()) return 0;
        double sum = 0;
        for (double m : marks) sum += m;
        return sum / marks.size();
    }
    
    char calculateGrade() const {
        double avg = calculateAverage();
        if (avg >= 90) return 'A';
        if (avg >= 80) return 'B';
        if (avg >= 70) return 'C';
        if (avg >= 60) return 'D';
        return 'F';
    }
    
    bool validateName(const string& n) const {
        if (n.empty()) return false;
        for (char c : n) {
            if (!isalpha(c) && c != ' ') return false;
        }
        return true;
    }
    
public:
    // Constructor
    Student(string n) : name(n), attendancePercentage(0), isActive(true) {
        if (!validateName(n)) {
            throw invalid_argument("Invalid name");
        }
        rollNumber = nextRollNumber++;
        cout << "Student created: " << name << " (Roll: " << rollNumber << ")" << endl;
    }
    
    // Getters - read-only access
    int getRollNumber() const { return rollNumber; }
    string getName() const { return name; }
    double getAttendance() const { return attendancePercentage; }
    bool isStudentActive() const { return isActive; }
    double getAverageMarks() const { return calculateAverage(); }
    char getGrade() const { return calculateGrade(); }
    
    // Get marks as const reference (no copy, read-only)
    const vector<double>& getMarks() const { return marks; }
    
    // Setters with validation
    void setName(string n) {
        if (validateName(n)) {
            name = n;
            cout << "Name updated to: " << name << endl;
        } else {
            cout << "Invalid name!" << endl;
        }
    }
    
    void addMark(double mark) {
        if (mark >= 0 && mark <= 100) {
            marks.push_back(mark);
            cout << "Mark " << mark << " added to " << name << endl;
        } else {
            cout << "Invalid mark! Must be 0-100." << endl;
        }
    }
    
    void setAttendance(double percent) {
        if (percent >= 0 && percent <= 100) {
            attendancePercentage = percent;
            cout << "Attendance updated to " << percent << "%" << endl;
        } else {
            cout << "Invalid attendance percentage!" << endl;
        }
    }
    
    void deactivate() {
        isActive = false;
        cout << name << " has been deactivated." << endl;
    }
    
    void activate() {
        isActive = true;
        cout << name << " has been activated." << endl;
    }
    
    // Business logic methods
    bool isPassing() const {
        return calculateAverage() >= 60 && attendancePercentage >= 75;
    }
    
    string getStatus() const {
        if (!isActive) return "Inactive";
        if (isPassing()) return "Passing";
        return "Failing";
    }
    
    void display() const {
        cout << "\n=== Student Details ===" << endl;
        cout << "Roll Number: " << rollNumber << endl;
        cout << "Name: " << name << endl;
        cout << "Status: " << getStatus() << endl;
        cout << "Attendance: " << attendancePercentage << "%" << endl;
        cout << "Marks: ";
        for (double m : marks) cout << m << " ";
        cout << endl;
        cout << "Average: " << fixed << setprecision(2) << calculateAverage() << endl;
        cout << "Grade: " << calculateGrade() << endl;
        cout << "Active: " << (isActive ? "Yes" : "No") << endl;
    }
};

int Student::nextRollNumber = 1001;

class Course {
private:
    string courseCode;
    string courseName;
    vector<Student*> enrolledStudents;
    int maxCapacity;
    
public:
    Course(string code, string name, int capacity) 
        : courseCode(code), courseName(name), maxCapacity(capacity) {
        cout << "Course created: " << courseCode << " - " << courseName << endl;
    }
    
    string getCourseCode() const { return courseCode; }
    string getCourseName() const { return courseName; }
    int getEnrollmentCount() const { return enrolledStudents.size(); }
    int getMaxCapacity() const { return maxCapacity; }
    
    bool enrollStudent(Student* student) {
        if (!student->isStudentActive()) {
            cout << "Cannot enroll inactive student!" << endl;
            return false;
        }
        
        if (enrolledStudents.size() >= maxCapacity) {
            cout << "Course is full!" << endl;
            return false;
        }
        
        enrolledStudents.push_back(student);
        cout << student->getName() << " enrolled in " << courseName << endl;
        return true;
    }
    
    void displayRoster() const {
        cout << "\n=== " << courseName << " Roster ===" << endl;
        cout << "Enrolled: " << enrolledStudents.size() << "/" << maxCapacity << endl;
        for (const auto& student : enrolledStudents) {
            cout << "  " << student->getRollNumber() << " - " 
                 << student->getName() << " (" << student->getStatus() << ")" << endl;
        }
    }
};

int main() {
    cout << "=== Student Management System ===" << endl;
    
    // Create students
    cout << "\n1. Creating students:" << endl;
    Student s1("Alice Johnson");
    Student s2("Bob Smith");
    Student s3("Charlie Brown");
    Student s4("Diana Prince");
    
    // Add marks and attendance
    cout << "\n2. Adding marks and attendance:" << endl;
    s1.addMark(85);
    s1.addMark(92);
    s1.addMark(78);
    s1.setAttendance(90);
    
    s2.addMark(65);
    s2.addMark(70);
    s2.addMark(68);
    s2.setAttendance(80);
    
    s3.addMark(45);
    s3.addMark(50);
    s3.addMark(55);
    s3.setAttendance(60);
    
    // Create courses
    cout << "\n3. Creating courses:" << endl;
    Course cs101("CS101", "Programming Fundamentals", 3);
    Course math201("MATH201", "Calculus I", 2);
    
    // Enroll students
    cout << "\n4. Enrolling students:" << endl;
    cs101.enrollStudent(&s1);
    cs101.enrollStudent(&s2);
    cs101.enrollStudent(&s3);
    cs101.enrollStudent(&s4);  // Should fail (capacity 3)
    
    math201.enrollStudent(&s1);
    math201.enrollStudent(&s2);
    
    // Display student details
    cout << "\n5. Student details:" << endl;
    s1.display();
    s2.display();
    s3.display();
    
    // Display course rosters
    cs101.displayRoster();
    math201.displayRoster();
    
    // Deactivate a student
    cout << "\n6. Deactivating student:" << endl;
    s3.deactivate();
    
    cout << "\n7. Final status:" << endl;
    s3.display();
    
    return 0;
}
```

---

## 2. **Shopping Cart System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
using namespace std;

class Product {
private:
    int id;
    string name;
    double price;
    int stockQuantity;
    static int nextId;
    
public:
    Product(string n, double p, int stock) : name(n), price(p), stockQuantity(stock) {
        id = nextId++;
        cout << "Product added: " << name << " (ID: " << id << ", $" << price << ")" << endl;
    }
    
    // Getters
    int getId() const { return id; }
    string getName() const { return name; }
    double getPrice() const { return price; }
    int getStock() const { return stockQuantity; }
    
    // Setters with validation
    void setPrice(double p) {
        if (p >= 0) {
            price = p;
            cout << "Price updated to $" << price << endl;
        }
    }
    
    bool reduceStock(int quantity) {
        if (quantity <= stockQuantity && quantity > 0) {
            stockQuantity -= quantity;
            return true;
        }
        return false;
    }
    
    void addStock(int quantity) {
        if (quantity > 0) {
            stockQuantity += quantity;
            cout << "Stock increased by " << quantity << endl;
        }
    }
    
    void display() const {
        cout << "ID: " << id << " | " << name 
             << " | $" << fixed << setprecision(2) << price 
             << " | Stock: " << stockQuantity << endl;
    }
};

int Product::nextId = 100;

class CartItem {
private:
    Product* product;
    int quantity;
    
public:
    CartItem(Product* p, int q) : product(p), quantity(q) {}
    
    Product* getProduct() const { return product; }
    int getQuantity() const { return quantity; }
    double getSubtotal() const { return product->getPrice() * quantity; }
    
    void increaseQuantity(int q) {
        if (q > 0) {
            quantity += q;
        }
    }
    
    bool decreaseQuantity(int q) {
        if (q >= quantity) {
            return false;  // Would remove item
        }
        quantity -= q;
        return true;
    }
    
    void display() const {
        cout << "  " << product->getName() << " x " << quantity 
             << " = $" << fixed << setprecision(2) << getSubtotal() << endl;
    }
};

class ShoppingCart {
private:
    vector<CartItem> items;
    
public:
    void addItem(Product* product, int quantity) {
        if (!product->reduceStock(quantity)) {
            cout << "Insufficient stock for " << product->getName() << endl;
            return;
        }
        
        // Check if item already in cart
        for (auto& item : items) {
            if (item.getProduct()->getId() == product->getId()) {
                item.increaseQuantity(quantity);
                cout << "Added " << quantity << " more " << product->getName() << "(s) to cart" << endl;
                return;
            }
        }
        
        items.emplace_back(product, quantity);
        cout << "Added " << quantity << " " << product->getName() << "(s) to cart" << endl;
    }
    
    bool removeItem(int productId) {
        for (auto it = items.begin(); it != items.end(); ++it) {
            if (it->getProduct()->getId() == productId) {
                // Return stock
                it->getProduct()->addStock(it->getQuantity());
                items.erase(it);
                cout << "Item removed from cart" << endl;
                return true;
            }
        }
        cout << "Item not found in cart" << endl;
        return false;
    }
    
    double getTotal() const {
        double total = 0;
        for (const auto& item : items) {
            total += item.getSubtotal();
        }
        return total;
    }
    
    int getItemCount() const {
        int count = 0;
        for (const auto& item : items) {
            count += item.getQuantity();
        }
        return count;
    }
    
    void display() const {
        if (items.empty()) {
            cout << "Cart is empty" << endl;
            return;
        }
        
        cout << "\n=== Shopping Cart (" << getItemCount() << " items) ===" << endl;
        for (const auto& item : items) {
            item.display();
        }
        cout << "Total: $" << fixed << setprecision(2) << getTotal() << endl;
    }
    
    void clear() {
        // Return all stock
        for (auto& item : items) {
            item.getProduct()->addStock(item.getQuantity());
        }
        items.clear();
        cout << "Cart cleared" << endl;
    }
};

class Order {
private:
    int orderId;
    vector<pair<Product*, int>> items;
    double total;
    string status;
    static int nextOrderId;
    
public:
    Order(const ShoppingCart& cart) : status("Pending") {
        orderId = nextOrderId++;
        total = cart.getTotal();
        
        // Need access to cart items - simplified for example
        cout << "Order #" << orderId << " created. Total: $" << total << endl;
    }
    
    void process() {
        status = "Processing";
        cout << "Order #" << orderId << " is being processed" << endl;
    }
    
    void ship() {
        status = "Shipped";
        cout << "Order #" << orderId << " has been shipped" << endl;
    }
    
    void deliver() {
        status = "Delivered";
        cout << "Order #" << orderId << " has been delivered" << endl;
    }
    
    void cancel() {
        status = "Cancelled";
        cout << "Order #" << orderId << " has been cancelled" << endl;
    }
    
    void display() const {
        cout << "Order #" << orderId << " | Status: " << status << " | Total: $" << total << endl;
    }
};

int Order::nextOrderId = 1000;

int main() {
    cout << "=== Shopping Cart System ===" << endl;
    
    // Create products
    cout << "\n1. Creating products:" << endl;
    Product laptop("Laptop", 999.99, 5);
    Product mouse("Wireless Mouse", 29.99, 20);
    Product keyboard("Mechanical Keyboard", 79.99, 10);
    Product monitor("24-inch Monitor", 199.99, 3);
    
    // Display products
    cout << "\n2. Available products:" << endl;
    laptop.display();
    mouse.display();
    keyboard.display();
    monitor.display();
    
    // Create shopping cart
    ShoppingCart cart;
    
    // Add items
    cout << "\n3. Adding items to cart:" << endl;
    cart.addItem(&laptop, 1);
    cart.addItem(&mouse, 2);
    cart.addItem(&keyboard, 1);
    cart.addItem(&laptop, 1);  // Should fail (stock check)
    
    // Display cart
    cart.display();
    
    // Remove item
    cout << "\n4. Removing item:" << endl;
    cart.removeItem(mouse.getId());
    cart.display();
    
    // Try to add more than stock
    cout << "\n5. Attempting to add more than stock:" << endl;
    cart.addItem(&monitor, 5);  // Only 3 in stock
    
    // Checkout
    cout << "\n6. Checkout:" << endl;
    Order order(cart);
    order.process();
    order.ship();
    
    // Clear cart after order
    cart.clear();
    cart.display();
    
    // Display final stock
    cout << "\n7. Final stock levels:" << endl;
    laptop.display();
    mouse.display();
    keyboard.display();
    monitor.display();
    
    return 0;
}
```

---

## 3. **Library Management System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <ctime>
#include <iomanip>
using namespace std;

class Book {
private:
    string isbn;
    string title;
    string author;
    int year;
    bool available;
    string borrowerName;
    time_t dueDate;
    
    string formatDate(time_t t) const {
        struct tm* timeinfo = localtime(&t);
        char buffer[20];
        strftime(buffer, sizeof(buffer), "%Y-%m-%d", timeinfo);
        return string(buffer);
    }
    
public:
    Book(string i, string t, string a, int y) 
        : isbn(i), title(t), author(a), year(y), available(true), borrowerName("") {}
    
    // Getters
    string getISBN() const { return isbn; }
    string getTitle() const { return title; }
    string getAuthor() const { return author; }
    int getYear() const { return year; }
    bool isAvailable() const { return available; }
    string getBorrower() const { return borrowerName; }
    
    // Borrow/Return methods
    bool borrow(string borrower) {
        if (!available) return false;
        
        available = false;
        borrowerName = borrower;
        dueDate = time(nullptr) + (14 * 24 * 60 * 60);  // 14 days
        cout << title << " borrowed by " << borrower << ". Due: " << formatDate(dueDate) << endl;
        return true;
    }
    
    bool returnBook() {
        if (available) return false;
        
        available = true;
        borrowerName = "";
        cout << title << " returned" << endl;
        return true;
    }
    
    bool isOverdue() const {
        if (available) return false;
        return time(nullptr) > dueDate;
    }
    
    void display() const {
        cout << "ISBN: " << isbn << " | " << title << " by " << author 
             << " (" << year << ")" << endl;
        cout << "  Status: " << (available ? "Available" : "Borrowed");
        if (!available) {
            cout << " by " << borrowerName;
            if (isOverdue()) cout << " (OVERDUE!)";
            else cout << " (Due: " << formatDate(dueDate) << ")";
        }
        cout << endl;
    }
};

class Member {
private:
    int memberId;
    string name;
    string email;
    vector<string> borrowedBooks;
    double fines;
    bool active;
    static int nextId;
    
public:
    Member(string n, string e) : name(n), email(e), fines(0), active(true) {
        memberId = nextId++;
        cout << "Member created: " << name << " (ID: " << memberId << ")" << endl;
    }
    
    // Getters
    int getId() const { return memberId; }
    string getName() const { return name; }
    string getEmail() const { return email; }
    double getFines() const { return fines; }
    bool isActive() const { return active; }
    int getBorrowedCount() const { return borrowedBooks.size(); }
    
    void borrowBook(const string& isbn) {
        if (!active) {
            cout << "Account is inactive!" << endl;
            return;
        }
        if (borrowedBooks.size() >= 5) {
            cout << "Maximum books borrowed!" << endl;
            return;
        }
        borrowedBooks.push_back(isbn);
    }
    
    void returnBook(const string& isbn) {
        for (auto it = borrowedBooks.begin(); it != borrowedBooks.end(); ++it) {
            if (*it == isbn) {
                borrowedBooks.erase(it);
                return;
            }
        }
    }
    
    void addFine(double amount) {
        if (amount > 0) {
            fines += amount;
            cout << "Fine of $" << amount << " added. Total fines: $" << fines << endl;
        }
    }
    
    void payFine(double amount) {
        if (amount > 0 && amount <= fines) {
            fines -= amount;
            cout << "Paid $" << amount << ". Remaining fines: $" << fines << endl;
        }
    }
    
    void deactivate() {
        active = false;
        cout << "Member " << name << " deactivated" << endl;
    }
    
    void display() const {
        cout << "ID: " << memberId << " | " << name << " (" << email << ")" << endl;
        cout << "  Borrowed: " << borrowedBooks.size() << " books" << endl;
        cout << "  Fines: $" << fixed << setprecision(2) << fines << endl;
        cout << "  Status: " << (active ? "Active" : "Inactive") << endl;
    }
};

int Member::nextId = 1000;

class Library {
private:
    map<string, Book> books;  // ISBN -> Book
    map<int, Member> members;  // ID -> Member
    
public:
    void addBook(const string& isbn, const string& title, 
                 const string& author, int year) {
        books.emplace(isbn, Book(isbn, title, author, year));
    }
    
    void addMember(const string& name, const string& email) {
        Member m(name, email);
        members.emplace(m.getId(), m);
    }
    
    bool borrowBook(int memberId, const string& isbn) {
        auto memberIt = members.find(memberId);
        if (memberIt == members.end()) {
            cout << "Member not found!" << endl;
            return false;
        }
        
        auto bookIt = books.find(isbn);
        if (bookIt == books.end()) {
            cout << "Book not found!" << endl;
            return false;
        }
        
        if (!bookIt->second.isAvailable()) {
            cout << "Book not available!" << endl;
            return false;
        }
        
        if (!memberIt->second.isActive()) {
            cout << "Member account inactive!" << endl;
            return false;
        }
        
        if (bookIt->second.borrow(memberIt->second.getName())) {
            memberIt->second.borrowBook(isbn);
            return true;
        }
        return false;
    }
    
    bool returnBook(int memberId, const string& isbn) {
        auto memberIt = members.find(memberId);
        if (memberIt == members.end()) return false;
        
        auto bookIt = books.find(isbn);
        if (bookIt == books.end()) return false;
        
        if (bookIt->second.returnBook()) {
            memberIt->second.returnBook(isbn);
            
            // Check for overdue fine
            if (bookIt->second.isOverdue()) {
                memberIt->second.addFine(5.0);
            }
            return true;
        }
        return false;
    }
    
    void displayBooks() const {
        cout << "\n=== Library Catalog (" << books.size() << " books) ===" << endl;
        for (const auto& pair : books) {
            pair.second.display();
        }
    }
    
    void displayMembers() const {
        cout << "\n=== Library Members (" << members.size() << " members) ===" << endl;
        for (const auto& pair : members) {
            pair.second.display();
        }
    }
};

int main() {
    cout << "=== Library Management System ===" << endl;
    
    Library library;
    
    // Add books
    cout << "\n1. Adding books:" << endl;
    library.addBook("978-0-321-99278-9", "C++ Primer", "Lippman", 2013);
    library.addBook("978-0-201-63361-0", "Design Patterns", "Gamma et al.", 1994);
    library.addBook("978-0-13-235088-4", "Clean Code", "Robert Martin", 2008);
    library.addBook("978-0-596-00571-1", "Head First Design Patterns", "Freeman", 2004);
    
    // Add members
    cout << "\n2. Adding members:" << endl;
    library.addMember("Alice Johnson", "alice@email.com");
    library.addMember("Bob Smith", "bob@email.com");
    library.addMember("Charlie Brown", "charlie@email.com");
    
    // Display initial state
    library.displayBooks();
    library.displayMembers();
    
    // Borrow books
    cout << "\n3. Borrowing books:" << endl;
    library.borrowBook(1000, "978-0-321-99278-9");  // Alice borrows C++ Primer
    library.borrowBook(1000, "978-0-201-63361-0");  // Alice borrows Design Patterns
    library.borrowBook(1001, "978-0-13-235088-4");  // Bob borrows Clean Code
    
    // Display after borrowing
    library.displayBooks();
    
    // Return a book
    cout << "\n4. Returning books:" << endl;
    library.returnBook(1000, "978-0-321-99278-9");
    
    // Final display
    library.displayBooks();
    library.displayMembers();
    
    return 0;
}
```

---

## 4. **Employee Payroll System**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <ctime>
using namespace std;

class Employee {
private:
    int id;
    string name;
    string department;
    double baseSalary;
    double bonus;
    double deductions;
    time_t hireDate;
    bool active;
    static int nextId;
    
    double calculateYearsOfService() const {
        time_t now = time(nullptr);
        double seconds = difftime(now, hireDate);
        return seconds / (365.25 * 24 * 60 * 60);
    }
    
    string formatDate(time_t t) const {
        struct tm* timeinfo = localtime(&t);
        char buffer[20];
        strftime(buffer, sizeof(buffer), "%Y-%m-%d", timeinfo);
        return string(buffer);
    }
    
public:
    Employee(string n, string dept, double salary) 
        : name(n), department(dept), baseSalary(salary), bonus(0), deductions(0), active(true) {
        id = nextId++;
        hireDate = time(nullptr);
        cout << "Employee created: " << name << " (ID: " << id << ")" << endl;
    }
    
    // Getters
    int getId() const { return id; }
    string getName() const { return name; }
    string getDepartment() const { return department; }
    double getBaseSalary() const { return baseSalary; }
    double getBonus() const { return bonus; }
    double getDeductions() const { return deductions; }
    bool isActive() const { return active; }
    double getYearsOfService() const { return calculateYearsOfService(); }
    
    // Salary calculations
    double calculateGrossSalary() const {
        return baseSalary + bonus;
    }
    
    double calculateNetSalary() const {
        return calculateGrossSalary() - deductions;
    }
    
    // Business logic methods
    void addBonus(double amount, string reason) {
        if (amount > 0 && active) {
            bonus += amount;
            cout << "Bonus of $" << amount << " added to " << name 
                 << " (" << reason << ")" << endl;
        }
    }
    
    void addDeduction(double amount, string reason) {
        if (amount > 0 && active) {
            deductions += amount;
            cout << "Deduction of $" << amount << " applied to " << name 
                 << " (" << reason << ")" << endl;
        }
    }
    
    void giveRaise(double percentage) {
        if (percentage > 0 && active) {
            double raise = baseSalary * (percentage / 100);
            baseSalary += raise;
            cout << name << " received " << percentage << "% raise. New salary: $" 
                 << baseSalary << endl;
        }
    }
    
    void terminate() {
        active = false;
        cout << name << " has been terminated." << endl;
    }
    
    void display() const {
        cout << "\n=== Employee Details ===" << endl;
        cout << "ID: " << id << endl;
        cout << "Name: " << name << endl;
        cout << "Department: " << department << endl;
        cout << "Hire Date: " << formatDate(hireDate) << endl;
        cout << "Years of Service: " << fixed << setprecision(1) 
             << calculateYearsOfService() << endl;
        cout << "Base Salary: $" << baseSalary << endl;
        cout << "Bonus: $" << bonus << endl;
        cout << "Deductions: $" << deductions << endl;
        cout << "Gross Salary: $" << calculateGrossSalary() << endl;
        cout << "Net Salary: $" << calculateNetSalary() << endl;
        cout << "Status: " << (active ? "Active" : "Terminated") << endl;
    }
};

int Employee::nextId = 1000;

class Department {
private:
    string name;
    vector<Employee*> employees;
    double budget;
    
public:
    Department(string n, double b) : name(n), budget(b) {
        cout << "Department created: " << name << " (Budget: $" << budget << ")" << endl;
    }
    
    void addEmployee(Employee* emp) {
        if (emp->getDepartment() == name) {
            employees.push_back(emp);
            cout << emp->getName() << " added to " << name << " department" << endl;
        }
    }
    
    double getTotalSalaryCost() const {
        double total = 0;
        for (const auto& emp : employees) {
            if (emp->isActive()) {
                total += emp->calculateGrossSalary();
            }
        }
        return total;
    }
    
    double getRemainingBudget() const {
        return budget - getTotalSalaryCost();
    }
    
    void display() const {
        cout << "\n=== " << name << " Department ===" << endl;
        cout << "Budget: $" << budget << endl;
        cout << "Salary Cost: $" << getTotalSalaryCost() << endl;
        cout << "Remaining: $" << getRemainingBudget() << endl;
        cout << "Employees (" << employees.size() << "):" << endl;
        for (const auto& emp : employees) {
            if (emp->isActive()) {
                cout << "  " << emp->getId() << " - " << emp->getName() 
                     << " ($" << emp->calculateGrossSalary() << ")" << endl;
            }
        }
    }
};

class Payroll {
private:
    map<int, vector<pair<string, double>>> transactions;  // Employee ID -> (date, amount)
    
public:
    void processPayroll(const vector<Employee*>& employees) {
        cout << "\n=== Processing Payroll ===" << endl;
        double totalPayroll = 0;
        
        for (auto emp : employees) {
            if (emp->isActive()) {
                double net = emp->calculateNetSalary();
                totalPayroll += net;
                
                // Record transaction
                time_t now = time(nullptr);
                transactions[emp->getId()].push_back({ctime(&now), net});
                
                cout << emp->getName() << ": $" << net << endl;
            }
        }
        
        cout << "Total Payroll: $" << totalPayroll << endl;
    }
    
    void displayPayrollHistory(int empId) const {
        auto it = transactions.find(empId);
        if (it != transactions.end()) {
            cout << "Payroll history for employee " << empId << ":" << endl;
            for (const auto& trans : it->second) {
                cout << "  " << trans.first << " - $" << trans.second << endl;
            }
        }
    }
};

int main() {
    cout << "=== Employee Payroll System ===" << endl;
    
    // Create employees
    cout << "\n1. Creating employees:" << endl;
    Employee e1("Alice Johnson", "Engineering", 85000);
    Employee e2("Bob Smith", "Sales", 65000);
    Employee e3("Charlie Brown", "Engineering", 75000);
    Employee e4("Diana Prince", "Marketing", 70000);
    
    // Add bonuses and deductions
    cout << "\n2. Adding bonuses and deductions:" << endl;
    e1.addBonus(5000, "Performance bonus");
    e1.addDeduction(2000, "Health insurance");
    e2.addBonus(3000, "Sales target achieved");
    e3.giveRaise(10);
    e4.addDeduction(1500, "401k contribution");
    
    // Create departments
    cout << "\n3. Creating departments:" << endl;
    Department engineering("Engineering", 300000);
    Department sales("Sales", 150000);
    Department marketing("Marketing", 120000);
    
    // Assign employees to departments
    cout << "\n4. Assigning employees to departments:" << endl;
    engineering.addEmployee(&e1);
    engineering.addEmployee(&e3);
    sales.addEmployee(&e2);
    marketing.addEmployee(&e4);
    
    // Display department details
    engineering.display();
    sales.display();
    marketing.display();
    
    // Process payroll
    vector<Employee*> allEmployees = {&e1, &e2, &e3, &e4};
    Payroll payroll;
    payroll.processPayroll(allEmployees);
    
    // Display individual employee details
    cout << "\n5. Employee details:" << endl;
    e1.display();
    e2.display();
    e3.display();
    e4.display();
    
    // Terminate an employee
    cout << "\n6. Terminating employee:" << endl;
    e4.terminate();
    
    // Process payroll again
    payroll.processPayroll(allEmployees);
    
    return 0;
}
```

---

## 📊 Summary of Practical Examples

| Example | Encapsulation Concepts Demonstrated |
|---------|-------------------------------------|
| **Student Management** | Data hiding, validation, business logic |
| **Shopping Cart** | Stock management, price validation, order processing |
| **Library System** | Book borrowing, member management, fine calculation |
| **Payroll System** | Salary calculations, bonuses, department budgets |

---

## ✅ Key Takeaways

1. **Encapsulation in practice** involves hiding implementation details
2. **Validation** ensures data integrity
3. **Business logic** is encapsulated within classes
4. **Getters and setters** provide controlled access
5. **Private helpers** keep complex logic hidden
6. **Const correctness** ensures read-only access where appropriate
7. **Real-world systems** naturally map to encapsulated objects

---
---

## Next Step

- Go to [05_Best_Practices.md](05_Best_Practices.md) to continue with Best Practices.
