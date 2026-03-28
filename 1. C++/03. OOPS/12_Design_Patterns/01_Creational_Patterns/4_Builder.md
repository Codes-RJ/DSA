# 12_Design_Patterns/01_Creational_Patterns/Builder.md

# Builder Pattern in C++ - Complete Guide

## 📖 Overview

The Builder pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations. It is particularly useful when an object requires many optional parameters or has a complex initialization process. The Builder pattern improves code readability and maintainability by providing a fluent interface.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Director** | Controls the construction process |
| **Builder** | Abstract interface for building parts |
| **Concrete Builder** | Implements the construction steps |
| **Product** | The complex object being built |

---

## 1. **Basic Builder Pattern**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

// Product
class Pizza {
private:
    string size;
    string crust;
    vector<string> toppings;
    bool cheese;
    bool sauce;
    
public:
    void setSize(const string& s) { size = s; }
    void setCrust(const string& c) { crust = c; }
    void addTopping(const string& t) { toppings.push_back(t); }
    void setCheese(bool c) { cheese = c; }
    void setSauce(bool s) { sauce = s; }
    
    void display() const {
        cout << "Pizza: " << size << " " << crust << " crust";
        if (cheese) cout << ", Extra cheese";
        if (sauce) cout << ", Extra sauce";
        if (!toppings.empty()) {
            cout << ", Toppings: ";
            for (const auto& t : toppings) cout << t << " ";
        }
        cout << endl;
    }
};

// Builder Interface
class PizzaBuilder {
protected:
    Pizza pizza;
    
public:
    virtual ~PizzaBuilder() = default;
    
    Pizza getPizza() { return pizza; }
    
    virtual void buildSize() = 0;
    virtual void buildCrust() = 0;
    virtual void buildToppings() = 0;
    virtual void buildCheese() = 0;
    virtual void buildSauce() = 0;
};

// Concrete Builder 1
class MargheritaBuilder : public PizzaBuilder {
public:
    void buildSize() override {
        pizza.setSize("Medium");
    }
    
    void buildCrust() override {
        pizza.setCrust("Thin");
    }
    
    void buildToppings() override {
        pizza.addTopping("Tomato");
        pizza.addTopping("Basil");
        pizza.addTopping("Mozzarella");
    }
    
    void buildCheese() override {
        pizza.setCheese(true);
    }
    
    void buildSauce() override {
        pizza.setSauce(true);
    }
};

// Concrete Builder 2
class PepperoniBuilder : public PizzaBuilder {
public:
    void buildSize() override {
        pizza.setSize("Large");
    }
    
    void buildCrust() override {
        pizza.setCrust("Thick");
    }
    
    void buildToppings() override {
        pizza.addTopping("Pepperoni");
        pizza.addTopping("Mozzarella");
        pizza.addTopping("Oregano");
    }
    
    void buildCheese() override {
        pizza.setCheese(true);
    }
    
    void buildSauce() override {
        pizza.setSauce(true);
    }
};

// Concrete Builder 3
class VegetarianBuilder : public PizzaBuilder {
public:
    void buildSize() override {
        pizza.setSize("Small");
    }
    
    void buildCrust() override {
        pizza.setCrust("Whole Wheat");
    }
    
    void buildToppings() override {
        pizza.addTopping("Mushrooms");
        pizza.addTopping("Bell Peppers");
        pizza.addTopping("Onions");
        pizza.addTopping("Olives");
    }
    
    void buildCheese() override {
        pizza.setCheese(false);
    }
    
    void buildSauce() override {
        pizza.setSauce(true);
    }
};

// Director
class PizzaChef {
public:
    void construct(PizzaBuilder& builder) {
        builder.buildSize();
        builder.buildCrust();
        builder.buildToppings();
        builder.buildCheese();
        builder.buildSauce();
    }
};

int main() {
    cout << "=== Basic Builder Pattern ===" << endl;
    
    PizzaChef chef;
    
    cout << "\n1. Margherita Pizza:" << endl;
    MargheritaBuilder margheritaBuilder;
    chef.construct(margheritaBuilder);
    Pizza margherita = margheritaBuilder.getPizza();
    margherita.display();
    
    cout << "\n2. Pepperoni Pizza:" << endl;
    PepperoniBuilder pepperoniBuilder;
    chef.construct(pepperoniBuilder);
    Pizza pepperoni = pepperoniBuilder.getPizza();
    pepperoni.display();
    
    cout << "\n3. Vegetarian Pizza:" << endl;
    VegetarianBuilder vegetarianBuilder;
    chef.construct(vegetarianBuilder);
    Pizza vegetarian = vegetarianBuilder.getPizza();
    vegetarian.display();
    
    return 0;
}
```

**Output:**
```
=== Basic Builder Pattern ===

1. Margherita Pizza:
Pizza: Medium Thin crust, Extra cheese, Extra sauce, Toppings: Tomato Basil Mozzarella 

2. Pepperoni Pizza:
Pizza: Large Thick crust, Extra cheese, Extra sauce, Toppings: Pepperoni Mozzarella Oregano 

3. Vegetarian Pizza:
Pizza: Small Whole Wheat crust, Extra sauce, Toppings: Mushrooms Bell Peppers Onions Olives 
```

---

## 2. **Fluent Builder (Method Chaining)**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <iomanip>
using namespace std;

class Computer {
private:
    string cpu;
    string gpu;
    int ram;
    int storage;
    string motherboard;
    string powerSupply;
    vector<string> peripherals;
    
public:
    class Builder {
    private:
        Computer computer;
        
    public:
        Builder& setCPU(const string& c) {
            computer.cpu = c;
            return *this;
        }
        
        Builder& setGPU(const string& g) {
            computer.gpu = g;
            return *this;
        }
        
        Builder& setRAM(int r) {
            computer.ram = r;
            return *this;
        }
        
        Builder& setStorage(int s) {
            computer.storage = s;
            return *this;
        }
        
        Builder& setMotherboard(const string& m) {
            computer.motherboard = m;
            return *this;
        }
        
        Builder& setPowerSupply(const string& p) {
            computer.powerSupply = p;
            return *this;
        }
        
        Builder& addPeripheral(const string& p) {
            computer.peripherals.push_back(p);
            return *this;
        }
        
        Computer build() {
            return computer;
        }
    };
    
    void display() const {
        cout << "\n=== Computer Configuration ===" << endl;
        cout << "CPU: " << cpu << endl;
        cout << "GPU: " << gpu << endl;
        cout << "RAM: " << ram << " GB" << endl;
        cout << "Storage: " << storage << " GB" << endl;
        cout << "Motherboard: " << motherboard << endl;
        cout << "Power Supply: " << powerSupply << endl;
        if (!peripherals.empty()) {
            cout << "Peripherals: ";
            for (const auto& p : peripherals) {
                cout << p << " ";
            }
            cout << endl;
        }
    }
};

class Email {
private:
    string from;
    string to;
    string subject;
    string body;
    vector<string> cc;
    vector<string> bcc;
    bool isHtml;
    
public:
    class Builder {
    private:
        Email email;
        
    public:
        Builder& setFrom(const string& f) {
            email.from = f;
            return *this;
        }
        
        Builder& setTo(const string& t) {
            email.to = t;
            return *this;
        }
        
        Builder& setSubject(const string& s) {
            email.subject = s;
            return *this;
        }
        
        Builder& setBody(const string& b) {
            email.body = b;
            return *this;
        }
        
        Builder& addCC(const string& c) {
            email.cc.push_back(c);
            return *this;
        }
        
        Builder& addBCC(const string& b) {
            email.bcc.push_back(b);
            return *this;
        }
        
        Builder& setHtml(bool html) {
            email.isHtml = html;
            return *this;
        }
        
        Email build() {
            return email;
        }
    };
    
    void send() const {
        cout << "\n=== Sending Email ===" << endl;
        cout << "From: " << from << endl;
        cout << "To: " << to << endl;
        if (!cc.empty()) {
            cout << "CC: ";
            for (const auto& c : cc) cout << c << " ";
            cout << endl;
        }
        cout << "Subject: " << subject << endl;
        cout << "Format: " << (isHtml ? "HTML" : "Text") << endl;
        cout << "Body: " << body << endl;
        cout << "Email sent!" << endl;
    }
};

int main() {
    cout << "=== Fluent Builder (Method Chaining) ===" << endl;
    
    cout << "\n1. Gaming Computer:" << endl;
    Computer gamingPC = Computer::Builder()
        .setCPU("Intel i9-13900K")
        .setGPU("NVIDIA RTX 4090")
        .setRAM(64)
        .setStorage(2000)
        .setMotherboard("ASUS ROG Maximus")
        .setPowerSupply("1000W Gold")
        .addPeripheral("Mechanical Keyboard")
        .addPeripheral("Gaming Mouse")
        .addPeripheral("4K Monitor")
        .build();
    gamingPC.display();
    
    cout << "\n2. Office Computer:" << endl;
    Computer officePC = Computer::Builder()
        .setCPU("Intel i5-13400")
        .setRAM(16)
        .setStorage(512)
        .setMotherboard("MSI B760")
        .setPowerSupply("500W Bronze")
        .build();
    officePC.display();
    
    cout << "\n3. Email Builder:" << endl;
    Email email = Email::Builder()
        .setFrom("admin@example.com")
        .setTo("user@example.com")
        .setSubject("Welcome to the System")
        .setBody("Thank you for registering!\n\nBest regards,\nAdmin")
        .addCC("support@example.com")
        .setHtml(false)
        .build();
    email.send();
    
    return 0;
}
```

---

## 3. **Builder with Validation**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <stdexcept>
#include <regex>
using namespace std;

class UserProfile {
private:
    string username;
    string email;
    int age;
    string phone;
    vector<string> interests;
    
public:
    class Builder {
    private:
        UserProfile user;
        bool usernameSet = false;
        bool emailSet = false;
        
        bool validateUsername(const string& name) {
            regex usernameRegex(R"([a-zA-Z0-9_]{3,20})");
            return regex_match(name, usernameRegex);
        }
        
        bool validateEmail(const string& email) {
            regex emailRegex(R"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})");
            return regex_match(email, emailRegex);
        }
        
        bool validateAge(int age) {
            return age >= 13 && age <= 120;
        }
        
        bool validatePhone(const string& phone) {
            regex phoneRegex(R"(\d{3}-\d{3}-\d{4})");
            return phone.empty() || regex_match(phone, phoneRegex);
        }
        
    public:
        Builder& setUsername(const string& name) {
            if (!validateUsername(name)) {
                throw invalid_argument("Invalid username (3-20 alphanumeric or underscore)");
            }
            user.username = name;
            usernameSet = true;
            return *this;
        }
        
        Builder& setEmail(const string& mail) {
            if (!validateEmail(mail)) {
                throw invalid_argument("Invalid email format");
            }
            user.email = mail;
            emailSet = true;
            return *this;
        }
        
        Builder& setAge(int a) {
            if (!validateAge(a)) {
                throw invalid_argument("Age must be between 13 and 120");
            }
            user.age = a;
            return *this;
        }
        
        Builder& setPhone(const string& p) {
            if (!validatePhone(p)) {
                throw invalid_argument("Invalid phone format (XXX-XXX-XXXX)");
            }
            user.phone = p;
            return *this;
        }
        
        Builder& addInterest(const string& interest) {
            if (!interest.empty()) {
                user.interests.push_back(interest);
            }
            return *this;
        }
        
        UserProfile build() {
            if (!usernameSet) {
                throw invalid_argument("Username is required");
            }
            if (!emailSet) {
                throw invalid_argument("Email is required");
            }
            return user;
        }
    };
    
    void display() const {
        cout << "\n=== User Profile ===" << endl;
        cout << "Username: " << username << endl;
        cout << "Email: " << email << endl;
        if (age > 0) cout << "Age: " << age << endl;
        if (!phone.empty()) cout << "Phone: " << phone << endl;
        if (!interests.empty()) {
            cout << "Interests: ";
            for (const auto& i : interests) cout << i << " ";
            cout << endl;
        }
    }
};

int main() {
    cout << "=== Builder with Validation ===" << endl;
    
    try {
        cout << "\n1. Valid user profile:" << endl;
        UserProfile user1 = UserProfile::Builder()
            .setUsername("john_doe")
            .setEmail("john@example.com")
            .setAge(25)
            .setPhone("555-123-4567")
            .addInterest("Programming")
            .addInterest("Gaming")
            .addInterest("Reading")
            .build();
        user1.display();
        
        cout << "\n2. Minimal user profile:" << endl;
        UserProfile user2 = UserProfile::Builder()
            .setUsername("alice")
            .setEmail("alice@email.com")
            .build();
        user2.display();
        
        cout << "\n3. Invalid user profile (will throw):" << endl;
        UserProfile user3 = UserProfile::Builder()
            .setUsername("a")  // Too short
            .setEmail("invalid")
            .build();
        
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }
    
    return 0;
}
```

---

## 4. **Builder with Different Representations**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
using namespace std;

// Product
class Report {
private:
    string title;
    string author;
    vector<string> sections;
    string footer;
    
public:
    void setTitle(const string& t) { title = t; }
    void setAuthor(const string& a) { author = a; }
    void addSection(const string& s) { sections.push_back(s); }
    void setFooter(const string& f) { footer = f; }
    
    string getTitle() const { return title; }
    string getAuthor() const { return author; }
    vector<string> getSections() const { return sections; }
    string getFooter() const { return footer; }
};

// Abstract Builder
class ReportBuilder {
protected:
    Report report;
    
public:
    virtual ~ReportBuilder() = default;
    virtual void buildTitle() = 0;
    virtual void buildAuthor() = 0;
    virtual void buildSections() = 0;
    virtual void buildFooter() = 0;
    
    Report getReport() { return report; }
};

// Concrete Builder for Text Format
class TextReportBuilder : public ReportBuilder {
public:
    void buildTitle() override {
        report.setTitle("Annual Report");
    }
    
    void buildAuthor() override {
        report.setAuthor("John Doe");
    }
    
    void buildSections() override {
        report.addSection("Introduction");
        report.addSection("Methodology");
        report.addSection("Results");
        report.addSection("Conclusion");
    }
    
    void buildFooter() override {
        report.setFooter("Confidential - Internal Use Only");
    }
    
    string getFormattedReport() {
        Report r = getReport();
        stringstream ss;
        ss << "=== " << r.getTitle() << " ===" << endl;
        ss << "Author: " << r.getAuthor() << endl << endl;
        for (const auto& section : r.getSections()) {
            ss << "> " << section << endl;
        }
        ss << endl << r.getFooter() << endl;
        return ss.str();
    }
};

// Concrete Builder for HTML Format
class HTMLReportBuilder : public ReportBuilder {
public:
    void buildTitle() override {
        report.setTitle("Annual Report");
    }
    
    void buildAuthor() override {
        report.setAuthor("John Doe");
    }
    
    void buildSections() override {
        report.addSection("Introduction");
        report.addSection("Methodology");
        report.addSection("Results");
        report.addSection("Conclusion");
    }
    
    void buildFooter() override {
        report.setFooter("Copyright 2024, All Rights Reserved");
    }
    
    string getFormattedReport() {
        Report r = getReport();
        stringstream ss;
        ss << "<!DOCTYPE html>\n<html>\n<head>\n";
        ss << "<title>" << r.getTitle() << "</title>\n";
        ss << "</head>\n<body>\n";
        ss << "<h1>" << r.getTitle() << "</h1>\n";
        ss << "<p>Author: " << r.getAuthor() << "</p>\n";
        ss << "<ul>\n";
        for (const auto& section : r.getSections()) {
            ss << "  <li>" << section << "</li>\n";
        }
        ss << "</ul>\n";
        ss << "<footer>" << r.getFooter() << "</footer>\n";
        ss << "</body>\n</html>\n";
        return ss.str();
    }
};

// Director
class ReportDirector {
public:
    void construct(ReportBuilder& builder) {
        builder.buildTitle();
        builder.buildAuthor();
        builder.buildSections();
        builder.buildFooter();
    }
};

int main() {
    cout << "=== Builder with Different Representations ===" << endl;
    
    ReportDirector director;
    
    cout << "\n1. Text Report:" << endl;
    TextReportBuilder textBuilder;
    director.construct(textBuilder);
    cout << textBuilder.getFormattedReport() << endl;
    
    cout << "\n2. HTML Report:" << endl;
    HTMLReportBuilder htmlBuilder;
    director.construct(htmlBuilder);
    cout << htmlBuilder.getFormattedReport() << endl;
    
    return 0;
}
```

---

## 5. **Practical Example: Query Builder**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

class SQLQuery {
private:
    string operation;
    string table;
    vector<string> columns;
    vector<string> conditions;
    vector<string> orderBy;
    int limit;
    int offset;
    
public:
    class Builder {
    private:
        SQLQuery query;
        
    public:
        Builder& select(const vector<string>& cols) {
            query.operation = "SELECT";
            query.columns = cols;
            return *this;
        }
        
        Builder& select(const string& col) {
            query.operation = "SELECT";
            query.columns = {col};
            return *this;
        }
        
        Builder& from(const string& tbl) {
            query.table = tbl;
            return *this;
        }
        
        Builder& where(const string& condition) {
            query.conditions.push_back(condition);
            return *this;
        }
        
        Builder& andWhere(const string& condition) {
            if (!query.conditions.empty()) {
                query.conditions.push_back("AND " + condition);
            } else {
                query.conditions.push_back(condition);
            }
            return *this;
        }
        
        Builder& orWhere(const string& condition) {
            if (!query.conditions.empty()) {
                query.conditions.push_back("OR " + condition);
            } else {
                query.conditions.push_back(condition);
            }
            return *this;
        }
        
        Builder& orderBy(const string& column, bool ascending = true) {
            query.orderBy.push_back(column + (ascending ? " ASC" : " DESC"));
            return *this;
        }
        
        Builder& limit(int l) {
            query.limit = l;
            return *this;
        }
        
        Builder& offset(int o) {
            query.offset = o;
            return *this;
        }
        
        SQLQuery build() {
            return query;
        }
    };
    
    string toString() const {
        stringstream ss;
        
        if (operation == "SELECT") {
            ss << "SELECT ";
            if (columns.empty()) {
                ss << "*";
            } else {
                for (size_t i = 0; i < columns.size(); i++) {
                    if (i > 0) ss << ", ";
                    ss << columns[i];
                }
            }
            ss << " FROM " << table;
            
            if (!conditions.empty()) {
                ss << " WHERE ";
                for (size_t i = 0; i < conditions.size(); i++) {
                    if (i > 0 && conditions[i].find("AND") == 0) {
                        ss << " " << conditions[i];
                    } else if (i > 0 && conditions[i].find("OR") == 0) {
                        ss << " " << conditions[i];
                    } else {
                        if (i > 0) ss << " AND ";
                        ss << conditions[i];
                    }
                }
            }
            
            if (!orderBy.empty()) {
                ss << " ORDER BY ";
                for (size_t i = 0; i < orderBy.size(); i++) {
                    if (i > 0) ss << ", ";
                    ss << orderBy[i];
                }
            }
            
            if (limit > 0) {
                ss << " LIMIT " << limit;
            }
            
            if (offset > 0) {
                ss << " OFFSET " << offset;
            }
        }
        
        return ss.str();
    }
};

int main() {
    cout << "=== Practical Example: Query Builder ===" << endl;
    
    cout << "\n1. Simple query:" << endl;
    SQLQuery query1 = SQLQuery::Builder()
        .select({"id", "name", "email"})
        .from("users")
        .build();
    cout << query1.toString() << endl;
    
    cout << "\n2. Query with conditions:" << endl;
    SQLQuery query2 = SQLQuery::Builder()
        .select("*")
        .from("products")
        .where("price > 100")
        .andWhere("category = 'Electronics'")
        .orderBy("price", false)
        .limit(10)
        .build();
    cout << query2.toString() << endl;
    
    cout << "\n3. Complex query:" << endl;
    SQLQuery query3 = SQLQuery::Builder()
        .select({"id", "name", "created_at"})
        .from("orders")
        .where("status = 'pending'")
        .orWhere("status = 'processing'")
        .orderBy("created_at")
        .limit(50)
        .offset(100)
        .build();
    cout << query3.toString() << endl;
    
    return 0;
}
```

---

## 📊 Builder Pattern Summary

| Component | Description |
|-----------|-------------|
| **Director** | Orchestrates the construction process |
| **Builder** | Interface for building product parts |
| **Concrete Builder** | Implements specific construction steps |
| **Product** | The complex object being built |
| **Fluent Interface** | Method chaining for readability |

---

## ✅ Best Practices

1. **Use Builder** when objects have many optional parameters
2. **Use Fluent Interface** for readability (method chaining)
3. **Validate** during build phase, not during construction
4. **Make Builder immutable** after build
5. **Consider using** `std::optional` for optional parameters

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Missing validation** | Invalid objects created | Validate in build() method |
| **Builder state** | Reusing builder incorrectly | Create new builder each time |
| **Too many methods** | Complex builder | Consider grouping parameters |
| **Not resetting builder** | Stale state | Create fresh builder for each object |

---

## ✅ Key Takeaways

1. **Builder pattern** separates construction from representation
2. **Fluent interface** provides readable method chaining
3. **Validates** complex object creation
4. **Handles** optional parameters elegantly
5. **Useful for** DTOs, configuration objects, queries
6. **Improves** code readability and maintainability

---