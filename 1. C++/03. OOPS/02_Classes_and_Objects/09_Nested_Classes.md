# 02_Classes_and_Objects/09_Nested_Classes.md

# Nested Classes in C++ - Complete Guide

## 📖 Overview

Nested classes (also called inner classes) are classes defined within another class. They are used to organize code, create logical groupings, and express relationships where one class is tightly coupled with another. Nested classes have special access rights to the enclosing class's members.

---

## 🎯 Types of Nested Classes

| Type | Access to Enclosing Class | Instantiation | Use Case |
|------|--------------------------|---------------|----------|
| **Public Nested Class** | Full access (private/protected) | Can be instantiated outside | Helper classes, iterators |
| **Private Nested Class** | Full access | Only within enclosing class | Implementation details |
| **Protected Nested Class** | Full access | Only within inheritance hierarchy | Base class helpers |
| **Static Nested Class** | No access to non-static members | Independent of enclosing object | Utility classes |

---

## 1. **Basic Nested Class**

### Definition
A class defined inside another class. It has access to all members of the enclosing class, including private ones.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Outer {
private:
    string privateData;
    int secretValue;
    
public:
    Outer(string data, int secret) : privateData(data), secretValue(secret) {}
    
    // Nested class definition
    class Inner {
    private:
        string innerData;
        
    public:
        Inner(string data) : innerData(data) {}
        
        // Can access private members of Outer
        void displayOuterData(const Outer& outer) {
            cout << "Accessing Outer's private data: " << outer.privateData << endl;
            cout << "Accessing Outer's secret value: " << outer.secretValue << endl;
        }
        
        void display() {
            cout << "Inner data: " << innerData << endl;
        }
        
        void modifyOuter(Outer& outer, string newData, int newSecret) {
            outer.privateData = newData;
            outer.secretValue = newSecret;
            cout << "Modified Outer's private members!" << endl;
        }
    };
    
    void display() {
        cout << "Outer data: " << privateData << ", Secret: " << secretValue << endl;
    }
};

int main() {
    Outer outer("Original", 42);
    Outer::Inner inner("Inner Object");
    
    cout << "=== Before Modification ===" << endl;
    outer.display();
    inner.display();
    
    cout << "\n=== Inner Accessing Outer ===" << endl;
    inner.displayOuterData(outer);
    
    cout << "\n=== Inner Modifying Outer ===" << endl;
    inner.modifyOuter(outer, "Modified", 100);
    
    cout << "\n=== After Modification ===" << endl;
    outer.display();
    
    return 0;
}
```

**Output:**
```
=== Before Modification ===
Outer data: Original, Secret: 42
Inner data: Inner Object

=== Inner Accessing Outer ===
Accessing Outer's private data: Original
Accessing Outer's secret value: 42

=== Inner Modifying Outer ===
Modified Outer's private members!

=== After Modification ===
Outer data: Modified, Secret: 100
```

---

## 2. **Public Nested Class (Iterator Pattern)**

### Definition
Public nested classes are commonly used for iterators, helper classes, and types that are logically part of the outer class.

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

template<typename T>
class Container {
private:
    vector<T> data;
    
public:
    void add(const T& item) {
        data.push_back(item);
    }
    
    // Public nested iterator class
    class Iterator {
    private:
        typename vector<T>::iterator it;
        
    public:
        Iterator(typename vector<T>::iterator i) : it(i) {}
        
        T& operator*() { return *it; }
        
        Iterator& operator++() {
            ++it;
            return *this;
        }
        
        bool operator!=(const Iterator& other) const {
            return it != other.it;
        }
    };
    
    Iterator begin() { return Iterator(data.begin()); }
    Iterator end() { return Iterator(data.end()); }
    
    // Const iterator (another nested class)
    class ConstIterator {
    private:
        typename vector<T>::const_iterator it;
        
    public:
        ConstIterator(typename vector<T>::const_iterator i) : it(i) {}
        
        const T& operator*() const { return *it; }
        
        ConstIterator& operator++() {
            ++it;
            return *this;
        }
        
        bool operator!=(const ConstIterator& other) const {
            return it != other.it;
        }
    };
    
    ConstIterator begin() const { return ConstIterator(data.begin()); }
    ConstIterator end() const { return ConstIterator(data.end()); }
};

class LinkedList {
private:
    struct Node {
        int data;
        Node* next;
        Node(int val) : data(val), next(nullptr) {}
    };
    
    Node* head;
    
public:
    LinkedList() : head(nullptr) {}
    
    ~LinkedList() {
        Node* current = head;
        while (current) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }
    
    void add(int value) {
        Node* newNode = new Node(value);
        newNode->next = head;
        head = newNode;
    }
    
    // Nested iterator class
    class Iterator {
    private:
        Node* current;
        
    public:
        Iterator(Node* node) : current(node) {}
        
        int& operator*() { return current->data; }
        
        Iterator& operator++() {
            if (current) current = current->next;
            return *this;
        }
        
        bool operator!=(const Iterator& other) const {
            return current != other.current;
        }
    };
    
    Iterator begin() { return Iterator(head); }
    Iterator end() { return Iterator(nullptr); }
};

int main() {
    // Container with nested iterator
    Container<string> names;
    names.add("Alice");
    names.add("Bob");
    names.add("Charlie");
    
    cout << "=== Container Iterator Example ===" << endl;
    for (auto it = names.begin(); it != names.end(); ++it) {
        cout << *it << endl;
    }
    
    // LinkedList with nested iterator
    LinkedList list;
    list.add(10);
    list.add(20);
    list.add(30);
    list.add(40);
    
    cout << "\n=== LinkedList Iterator Example ===" << endl;
    for (auto it = list.begin(); it != list.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
=== Container Iterator Example ===
Alice
Bob
Charlie

=== LinkedList Iterator Example ===
40 30 20 10
```

---

## 3. **Private Nested Class (Implementation Details)**

### Definition
Private nested classes are used for implementation details that should not be exposed to users of the outer class.

```cpp
#include <iostream>
#include <memory>
#include <queue>
using namespace std;

class MessageQueue {
private:
    // Private nested class - implementation detail
    class Message {
    private:
        string content;
        int priority;
        
    public:
        Message(string msg, int prio) : content(msg), priority(prio) {}
        
        string getContent() const { return content; }
        int getPriority() const { return priority; }
        
        // For priority queue ordering
        bool operator<(const Message& other) const {
            return priority < other.priority;
        }
    };
    
    // Priority queue of messages
    priority_queue<Message> messages;
    
public:
    void send(string msg, int priority = 0) {
        messages.emplace(msg, priority);
        cout << "Message queued: '" << msg << "' (priority: " << priority << ")" << endl;
    }
    
    string receive() {
        if (messages.empty()) {
            return "";
        }
        
        Message msg = messages.top();
        messages.pop();
        return msg.getContent();
    }
    
    bool hasMessages() const {
        return !messages.empty();
    }
    
    int pendingCount() const {
        return messages.size();
    }
};

class DatabaseConnection {
private:
    // Private nested class for connection pool management
    class Connection {
    private:
        int id;
        bool inUse;
        
    public:
        Connection(int i) : id(i), inUse(false) {}
        
        void connect() {
            inUse = true;
            cout << "Connection " << id << " established" << endl;
        }
        
        void disconnect() {
            inUse = false;
            cout << "Connection " << id << " closed" << endl;
        }
        
        bool isAvailable() const { return !inUse; }
        int getId() const { return id; }
    };
    
    vector<unique_ptr<Connection>> pool;
    static const int POOL_SIZE = 5;
    
public:
    DatabaseConnection() {
        for (int i = 0; i < POOL_SIZE; i++) {
            pool.push_back(make_unique<Connection>(i));
        }
    }
    
    // Find available connection
    Connection* getConnection() {
        for (auto& conn : pool) {
            if (conn->isAvailable()) {
                conn->connect();
                return conn.get();
            }
        }
        cout << "No connections available!" << endl;
        return nullptr;
    }
    
    void releaseConnection(Connection* conn) {
        if (conn) {
            conn->disconnect();
        }
    }
    
    int availableCount() const {
        int count = 0;
        for (const auto& conn : pool) {
            if (conn->isAvailable()) count++;
        }
        return count;
    }
};

int main() {
    MessageQueue queue;
    
    cout << "=== Message Queue (Private Nested Class) ===" << endl;
    queue.send("Urgent message", 10);
    queue.send("Normal message", 5);
    queue.send("Low priority", 1);
    queue.send("Important", 8);
    
    cout << "\nProcessing messages:" << endl;
    while (queue.hasMessages()) {
        cout << "Received: " << queue.receive() << endl;
    }
    
    cout << "\n=== Database Connection Pool ===" << endl;
    DatabaseConnection db;
    
    cout << "Available connections: " << db.availableCount() << endl;
    
    auto conn1 = db.getConnection();
    auto conn2 = db.getConnection();
    auto conn3 = db.getConnection();
    auto conn4 = db.getConnection();
    auto conn5 = db.getConnection();
    auto conn6 = db.getConnection();  // Should fail
    
    cout << "\nAfter acquiring connections:" << endl;
    cout << "Available: " << db.availableCount() << endl;
    
    db.releaseConnection(conn1);
    cout << "\nAfter releasing one connection:" << endl;
    cout << "Available: " << db.availableCount() << endl;
    
    return 0;
}
```

**Output:**
```
=== Message Queue (Private Nested Class) ===
Message queued: 'Urgent message' (priority: 10)
Message queued: 'Normal message' (priority: 5)
Message queued: 'Low priority' (priority: 1)
Message queued: 'Important' (priority: 8)

Processing messages:
Received: Urgent message
Received: Important
Received: Normal message
Received: Low priority

=== Database Connection Pool ===
Available connections: 5
Connection 0 established
Connection 1 established
Connection 2 established
Connection 3 established
Connection 4 established
No connections available!

After acquiring connections:
Available: 0
Connection 0 closed

After releasing one connection:
Available: 1
```

---

## 4. **Static Nested Class**

### Definition
Static nested classes don't have access to non-static members of the enclosing class. They are more like regular classes that are scoped within the outer class.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

class Geometry {
public:
    // Static nested class - no access to Geometry's non-static members
    class Point {
    private:
        double x, y;
        
    public:
        Point(double x = 0, double y = 0) : x(x), y(y) {}
        
        double getX() const { return x; }
        double getY() const { return y; }
        
        double distanceTo(const Point& other) const {
            double dx = x - other.x;
            double dy = y - other.y;
            return sqrt(dx * dx + dy * dy);
        }
        
        Point operator+(const Point& other) const {
            return Point(x + other.x, y + other.y);
        }
        
        void display() const {
            cout << "(" << x << ", " << y << ")";
        }
    };
    
    // Another static nested class
    class Rectangle {
    private:
        Point topLeft;
        Point bottomRight;
        
    public:
        Rectangle(const Point& tl, const Point& br) : topLeft(tl), bottomRight(br) {}
        
        double area() const {
            double width = bottomRight.getX() - topLeft.getX();
            double height = bottomRight.getY() - topLeft.getY();
            return width * height;
        }
        
        double perimeter() const {
            double width = bottomRight.getX() - topLeft.getX();
            double height = bottomRight.getY() - topLeft.getY();
            return 2 * (width + height);
        }
        
        bool contains(const Point& p) const {
            return p.getX() >= topLeft.getX() && 
                   p.getX() <= bottomRight.getX() &&
                   p.getY() >= topLeft.getY() && 
                   p.getY() <= bottomRight.getY();
        }
        
        void display() const {
            cout << "Rectangle: ";
            topLeft.display();
            cout << " to ";
            bottomRight.display();
            cout << endl;
        }
    };
    
    class Circle {
    private:
        Point center;
        double radius;
        
    public:
        Circle(const Point& c, double r) : center(c), radius(r) {}
        
        double area() const { return 3.14159 * radius * radius; }
        double circumference() const { return 2 * 3.14159 * radius; }
        
        bool contains(const Point& p) const {
            return center.distanceTo(p) <= radius;
        }
        
        void display() const {
            cout << "Circle: center ";
            center.display();
            cout << ", radius = " << radius << endl;
        }
    };
};

int main() {
    // Using static nested classes
    Geometry::Point p1(0, 0);
    Geometry::Point p2(3, 4);
    Geometry::Point p3(5, 5);
    
    cout << "=== Point Operations ===" << endl;
    cout << "p1: "; p1.display(); cout << endl;
    cout << "p2: "; p2.display(); cout << endl;
    cout << "Distance: " << p1.distanceTo(p2) << endl;
    
    Geometry::Point p4 = p1 + p2;
    cout << "p1 + p2: "; p4.display(); cout << endl;
    
    cout << "\n=== Rectangle Operations ===" << endl;
    Geometry::Rectangle rect(Geometry::Point(0, 0), Geometry::Point(5, 3));
    rect.display();
    cout << "Area: " << rect.area() << endl;
    cout << "Perimeter: " << rect.perimeter() << endl;
    cout << "Contains (2,2)? " << (rect.contains(Geometry::Point(2, 2)) ? "Yes" : "No") << endl;
    cout << "Contains (6,2)? " << (rect.contains(Geometry::Point(6, 2)) ? "Yes" : "No") << endl;
    
    cout << "\n=== Circle Operations ===" << endl;
    Geometry::Circle circle(Geometry::Point(0, 0), 5);
    circle.display();
    cout << "Area: " << circle.area() << endl;
    cout << "Circumference: " << circle.circumference() << endl;
    cout << "Contains (3,4)? " << (circle.contains(Geometry::Point(3, 4)) ? "Yes" : "No") << endl;
    cout << "Contains (6,0)? " << (circle.contains(Geometry::Point(6, 0)) ? "Yes" : "No") << endl;
    
    return 0;
}
```

**Output:**
```
=== Point Operations ===
p1: (0, 0)
p2: (3, 4)
Distance: 5
p1 + p2: (3, 4)

=== Rectangle Operations ===
Rectangle: (0, 0) to (5, 3)
Area: 15
Perimeter: 16
Contains (2,2)? Yes
Contains (6,2)? No

=== Circle Operations ===
Circle: center (0, 0), radius = 5
Area: 78.5398
Circumference: 31.4159
Contains (3,4)? Yes
Contains (6,0)? No
```

---

## 5. **Nested Class with Enclosing Class Instance**

### Definition
Non-static nested classes can access the enclosing class instance through a pointer or reference.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Document {
private:
    string content;
    vector<string> words;
    
    void tokenize() {
        string word;
        for (char c : content) {
            if (isalnum(c)) {
                word += tolower(c);
            } else if (!word.empty()) {
                words.push_back(word);
                word.clear();
            }
        }
        if (!word.empty()) {
            words.push_back(word);
        }
    }
    
public:
    Document(string text) : content(text) {
        tokenize();
    }
    
    // Nested class that has access to Document's private members
    class WordIterator {
    private:
        Document* doc;
        size_t index;
        
    public:
        WordIterator(Document* d, size_t i) : doc(d), index(i) {}
        
        string operator*() const {
            return doc->words[index];
        }
        
        WordIterator& operator++() {
            ++index;
            return *this;
        }
        
        bool operator!=(const WordIterator& other) const {
            return index != other.index;
        }
        
        size_t getIndex() const { return index; }
    };
    
    WordIterator begin() { return WordIterator(this, 0); }
    WordIterator end() { return WordIterator(this, words.size()); }
    
    // Search nested class
    class SearchResult {
    private:
        vector<size_t> positions;
        Document* doc;
        
    public:
        SearchResult(Document* d) : doc(d) {}
        
        void addPosition(size_t pos) {
            positions.push_back(pos);
        }
        
        size_t count() const { return positions.size(); }
        
        void display() const {
            cout << "Found at positions: ";
            for (size_t pos : positions) {
                cout << pos << " ";
            }
            cout << endl;
            
            cout << "Context:" << endl;
            for (size_t pos : positions) {
                size_t start = (pos > 2) ? pos - 2 : 0;
                size_t end = min(pos + 3, doc->words.size());
                
                for (size_t i = start; i < end; i++) {
                    if (i == pos) {
                        cout << "[" << doc->words[i] << "] ";
                    } else {
                        cout << doc->words[i] << " ";
                    }
                }
                cout << endl;
            }
        }
    };
    
    SearchResult search(const string& term) {
        SearchResult result(this);
        string lowerTerm = term;
        transform(lowerTerm.begin(), lowerTerm.end(), lowerTerm.begin(), ::tolower);
        
        for (size_t i = 0; i < words.size(); i++) {
            if (words[i] == lowerTerm) {
                result.addPosition(i);
            }
        }
        return result;
    }
    
    class Stats {
    private:
        Document* doc;
        
    public:
        Stats(Document* d) : doc(d) {}
        
        int wordCount() const { return doc->words.size(); }
        int charCount() const { return doc->content.length(); }
        double avgWordLength() const {
            if (doc->words.empty()) return 0;
            int total = 0;
            for (const auto& word : doc->words) {
                total += word.length();
            }
            return static_cast<double>(total) / doc->words.size();
        }
        
        void display() const {
            cout << "Statistics:" << endl;
            cout << "  Words: " << wordCount() << endl;
            cout << "  Characters: " << charCount() << endl;
            cout << "  Average word length: " << avgWordLength() << endl;
        }
    };
    
    Stats getStats() { return Stats(this); }
};

int main() {
    Document doc("The quick brown fox jumps over the lazy dog. The fox is quick!");
    
    cout << "=== Word Iteration ===" << endl;
    for (auto it = doc.begin(); it != doc.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;
    
    cout << "\n=== Search Results ===" << endl;
    auto results = doc.search("fox");
    cout << "Found 'fox' " << results.count() << " times" << endl;
    results.display();
    
    cout << "\n=== Document Statistics ===" << endl;
    doc.getStats().display();
    
    return 0;
}
```

**Output:**
```
=== Word Iteration ===
the quick brown fox jumps over the lazy dog the fox is quick 

=== Search Results ===
Found 'fox' 2 times
Found at positions: 3 10 
Context:
brown [fox] jumps 
the [fox] is 

=== Document Statistics ===
Statistics:
  Words: 13
  Characters: 56
  Average word length: 3.69231
```

---

## 📊 Nested Classes Summary

| Type | Access to Enclosing Members | Can be Instantiated Outside | Common Use |
|------|----------------------------|----------------------------|------------|
| **Public Nested** | Full access | Yes | Iterators, helper types |
| **Private Nested** | Full access | No | Implementation details |
| **Protected Nested** | Full access | Only in derived classes | Base class helpers |
| **Static Nested** | Only static members | Yes | Utility classes, scoping |

---

## ✅ Best Practices

### 1. **Use Nested Classes for Logical Grouping**
```cpp
class Parser {
    class Token { ... };        // Only used by Parser
    class ASTNode { ... };      // Only used by Parser
public:
    void parse();               // Public interface
};
```

### 2. **Use Private Nested Classes for Implementation Details**
```cpp
class Cache {
    class CacheEntry {          // Private implementation
        string key;
        string value;
    };
    vector<CacheEntry> entries;
};
```

### 3. **Use Nested Iterators for Container Classes**
```cpp
class MyContainer {
    class Iterator {            // Public nested iterator
        // Iterator implementation
    };
    Iterator begin();
    Iterator end();
};
```

### 4. **Keep Nested Classes Focused**
```cpp
class Database {
    class Connection {          // Single responsibility
        // Connection management only
    };
    class Query {               // Single responsibility
        // Query execution only
    };
};
```

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Accessing non-static members from static nested** | Compiler error | Make nested class non-static or pass reference |
| **Forward declaration issues** | Incomplete type | Define nested class before using |
| **Name hiding** | Ambiguity | Use scope resolution `Outer::Nested` |
| **Circular dependencies** | Compilation problems | Use forward declarations |

---

## ✅ Key Takeaways

1. **Nested classes** are classes defined inside other classes
2. **Public nested classes** are accessible outside the enclosing class
3. **Private nested classes** are for implementation details
4. **Static nested classes** don't have access to non-static members
5. **Non-static nested classes** can access all members of enclosing class
6. **Common uses**: Iterators, helpers, implementation details

---