# Move Semantics in C++ - Complete Guide

## 📖 Overview

Move semantics, introduced in C++11, allows resources to be transferred from temporary objects instead of copying them. This significantly improves performance by eliminating unnecessary deep copies. Move semantics is enabled by rvalue references (`&&`), move constructors, and move assignment operators.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **lvalue** | Has an address, persists beyond expression |
| **rvalue** | Temporary, no address, destroyed after expression |
| **rvalue reference** | `&&`, binds to rvalues |
| **std::move** | Casts lvalue to rvalue |
| **Move constructor** | Transfers resources from temporary |
| **Move assignment** | Transfers resources in assignment |

---

## 1. **lvalues and rvalues**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Function overloading to demonstrate lvalue/rvalue
void process(int& x) {
    cout << "process(int&) - lvalue: " << x << endl;
}

void process(int&& x) {
    cout << "process(int&&) - rvalue: " << x << endl;
}

class Test {
public:
    void method() & { cout << "Called on lvalue" << endl; }
    void method() && { cout << "Called on rvalue" << endl; }
};

int main() {
    cout << "=== lvalues and rvalues ===" << endl;
    
    // lvalue: has a name, can take address
    int x = 42;
    process(x);  // lvalue
    
    // rvalue: temporary, no name
    process(42);  // rvalue
    process(x + 5);  // rvalue
    
    // std::move converts lvalue to rvalue
    process(move(x));  // rvalue
    cout << "After move, x = " << x << " (moved-from state)" << endl;
    
    // lvalue/rvalue with strings
    string s1 = "Hello";
    string s2 = "World";
    
    // s1 + s2 is rvalue (temporary)
    string s3 = s1 + s2;  // Uses move semantics internally
    
    // lvalue/rvalue ref-qualified methods
    Test t;
    t.method();      // Calls lvalue version
    Test().method(); // Calls rvalue version
    
    return 0;
}
```

**Output:**
```
=== lvalues and rvalues ===
process(int&) - lvalue: 42
process(int&&) - rvalue: 42
process(int&&) - rvalue: 47
process(int&&) - rvalue: 42
After move, x = 42 (moved-from state)
Called on lvalue
Called on rvalue
```

---

## 2. **Move Constructor and Move Assignment**

```cpp
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

class StringBuffer {
private:
    char* data_;
    size_t size_;
    
public:
    // Constructor
    StringBuffer(const char* str = "") {
        size_ = strlen(str);
        data_ = new char[size_ + 1];
        strcpy(data_, str);
        cout << "Constructed: " << data_ << endl;
    }
    
    // Copy constructor (expensive)
    StringBuffer(const StringBuffer& other) {
        size_ = other.size_;
        data_ = new char[size_ + 1];
        strcpy(data_, other.data_);
        cout << "Copied: " << data_ << endl;
    }
    
    // Move constructor (efficient)
    StringBuffer(StringBuffer&& other) noexcept
        : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr;
        other.size_ = 0;
        cout << "Moved: " << data_ << endl;
    }
    
    // Copy assignment
    StringBuffer& operator=(const StringBuffer& other) {
        if (this != &other) {
            delete[] data_;
            size_ = other.size_;
            data_ = new char[size_ + 1];
            strcpy(data_, other.data_);
            cout << "Copy assigned: " << data_ << endl;
        }
        return *this;
    }
    
    // Move assignment
    StringBuffer& operator=(StringBuffer&& other) noexcept {
        if (this != &other) {
            delete[] data_;
            data_ = other.data_;
            size_ = other.size_;
            other.data_ = nullptr;
            other.size_ = 0;
            cout << "Move assigned: " << data_ << endl;
        }
        return *this;
    }
    
    ~StringBuffer() {
        if (data_) {
            cout << "Destroyed: " << data_ << endl;
            delete[] data_;
        } else {
            cout << "Destroyed: (moved from)" << endl;
        }
    }
    
    void display() const {
        if (data_) cout << "String: " << data_ << endl;
        else cout << "String: (empty)" << endl;
    }
};

int main() {
    cout << "=== Move Constructor and Move Assignment ===" << endl;
    
    cout << "\n1. Copy vs Move:" << endl;
    StringBuffer s1("Hello");
    StringBuffer s2 = s1;           // Copy constructor
    StringBuffer s3 = move(s1);     // Move constructor
    
    cout << "\ns1 after move: ";
    s1.display();
    cout << "s2: ";
    s2.display();
    cout << "s3: ";
    s3.display();
    
    cout << "\n2. Move assignment:" << endl;
    StringBuffer s4("World");
    StringBuffer s5("Temporary");
    s5 = move(s4);  // Move assignment
    
    cout << "\ns4 after move: ";
    s4.display();
    cout << "s5: ";
    s5.display();
    
    cout << "\n3. Returning from function:" << endl;
    auto createBuffer = []() -> StringBuffer {
        StringBuffer temp("Temporary");
        return temp;  // Move or RVO
    };
    
    StringBuffer s6 = createBuffer();
    s6.display();
    
    return 0;
}
```

---

## 3. **std::move and Perfect Forwarding**

```cpp
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

class Widget {
private:
    string name_;
    int* data_;
    
public:
    Widget(string name, int value) : name_(name), data_(new int(value)) {
        cout << "Widget constructed: " << name_ << endl;
    }
    
    ~Widget() {
        delete data_;
        cout << "Widget destroyed: " << name_ << endl;
    }
    
    // Move constructor
    Widget(Widget&& other) noexcept
        : name_(move(other.name_)), data_(other.data_) {
        other.data_ = nullptr;
        cout << "Widget moved: " << name_ << endl;
    }
    
    // Copy constructor deleted
    Widget(const Widget&) = delete;
    
    void display() const {
        cout << name_ << ": " << (data_ ? *data_ : 0) << endl;
    }
};

// Perfect forwarding function
template<typename T>
void forwarder(T&& arg) {
    // Perfectly forwards lvalue as lvalue, rvalue as rvalue
    process(move(arg));  // Always moves
    // process(forward<T>(arg));  // Perfect forwarding
}

void process(Widget& w) {
    cout << "process lvalue: ";
    w.display();
}

void process(Widget&& w) {
    cout << "process rvalue: ";
    w.display();
}

int main() {
    cout << "=== std::move and Perfect Forwarding ===" << endl;
    
    cout << "\n1. std::move example:" << endl;
    vector<string> strings;
    string str = "Hello";
    
    cout << "Before move, str = " << str << endl;
    strings.push_back(move(str));  // Move instead of copy
    cout << "After move, str = " << str << endl;
    cout << "Vector contains: " << strings[0] << endl;
    
    cout << "\n2. Move with unique_ptr:" << endl;
    auto ptr1 = make_unique<int>(42);
    auto ptr2 = move(ptr1);  // Transfer ownership
    
    cout << "ptr1: " << (ptr1 ? "not null" : "null") << endl;
    cout << "ptr2: " << *ptr2 << endl;
    
    cout << "\n3. Perfect forwarding:" << endl;
    Widget w1("Widget1", 100);
    forwarder(w1);           // lvalue
    forwarder(Widget("Widget2", 200));  // rvalue
    
    cout << "\n4. Move with vector:" << endl;
    vector<Widget> widgets;
    widgets.push_back(Widget("A", 1));
    widgets.push_back(Widget("B", 2));
    widgets.push_back(Widget("C", 3));
    
    // widgets[0] is lvalue, would copy if copy constructor existed
    // widgets.push_back(widgets[0]);  // Would need copy constructor
    
    return 0;
}
```

---

## 4. **Move Semantics in Containers**

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <chrono>
using namespace std;

class LargeObject {
private:
    string name_;
    vector<int> data_;
    
public:
    LargeObject(string name, size_t size) : name_(name), data_(size) {
        for (size_t i = 0; i < size; i++) data_[i] = i;
        cout << "LargeObject created: " << name_ << endl;
    }
    
    // Copy constructor (expensive)
    LargeObject(const LargeObject& other) 
        : name_(other.name_ + "_copy"), data_(other.data_) {
        cout << "LargeObject copied: " << name_ << endl;
    }
    
    // Move constructor (cheap)
    LargeObject(LargeObject&& other) noexcept
        : name_(move(other.name_)), data_(move(other.data_)) {
        cout << "LargeObject moved: " << name_ << endl;
    }
    
    ~LargeObject() {
        cout << "LargeObject destroyed: " << name_ << endl;
    }
    
    void display() const {
        cout << name_ << " has " << data_.size() << " elements" << endl;
    }
};

int main() {
    cout << "=== Move Semantics in Containers ===" << endl;
    
    cout << "\n1. push_back vs emplace_back:" << endl;
    vector<LargeObject> vec;
    
    cout << "\npush_back (creates temporary, then moves):" << endl;
    vec.push_back(LargeObject("PushBack", 1000));
    
    cout << "\nemplace_back (constructs in place):" << endl;
    vec.emplace_back("EmplaceBack", 2000);
    
    cout << "\n2. Moving vector elements:" << endl;
    vector<LargeObject> vec2;
    vec2.push_back(move(vec[0]));  // Move from vec to vec2
    cout << "vec size: " << vec.size() << endl;
    cout << "vec2 size: " << vec2.size() << endl;
    
    cout << "\n3. Resizing vector (may cause moves):" << endl;
    vector<LargeObject> vec3;
    vec3.reserve(10);  // Reserve to avoid moves during push_back
    for (int i = 0; i < 5; i++) {
        vec3.emplace_back("Vec3_" + to_string(i), 100);
    }
    
    cout << "\n4. Returning vector (move or RVO):" << endl;
    auto createVector = []() -> vector<LargeObject> {
        vector<LargeObject> v;
        v.emplace_back("Returned1", 100);
        v.emplace_back("Returned2", 200);
        return v;  // Move or RVO
    };
    
    vector<LargeObject> vec4 = createVector();
    cout << "vec4 size: " << vec4.size() << endl;
    
    return 0;
}
```

---

## 5. **Move-Only Types**

```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <fstream>
using namespace std;

// Move-only class
class FileHandle {
private:
    FILE* file_;
    string filename_;
    
public:
    FileHandle(const string& filename, const string& mode) : filename_(filename) {
        file_ = fopen(filename.c_str(), mode.c_str());
        if (!file_) {
            throw runtime_error("Cannot open file: " + filename);
        }
        cout << "File opened: " << filename_ << endl;
    }
    
    // Move constructor
    FileHandle(FileHandle&& other) noexcept
        : file_(other.file_), filename_(move(other.filename_)) {
        other.file_ = nullptr;
        cout << "File moved: " << filename_ << endl;
    }
    
    // Move assignment
    FileHandle& operator=(FileHandle&& other) noexcept {
        if (this != &other) {
            if (file_) fclose(file_);
            file_ = other.file_;
            filename_ = move(other.filename_);
            other.file_ = nullptr;
            cout << "File move assigned: " << filename_ << endl;
        }
        return *this;
    }
    
    // Delete copy operations
    FileHandle(const FileHandle&) = delete;
    FileHandle& operator=(const FileHandle&) = delete;
    
    ~FileHandle() {
        if (file_) {
            fclose(file_);
            cout << "File closed: " << filename_ << endl;
        }
    }
    
    void write(const string& data) {
        if (file_) {
            fprintf(file_, "%s\n", data.c_str());
        }
    }
};

class MoveOnlyResource {
private:
    int* data_;
    size_t size_;
    
public:
    MoveOnlyResource(size_t size) : size_(size) {
        data_ = new int[size];
        cout << "Resource allocated: " << size << " ints" << endl;
    }
    
    ~MoveOnlyResource() {
        if (data_) {
            delete[] data_;
            cout << "Resource freed: " << size_ << " ints" << endl;
        }
    }
    
    // Move constructor
    MoveOnlyResource(MoveOnlyResource&& other) noexcept
        : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr;
        other.size_ = 0;
        cout << "Resource moved" << endl;
    }
    
    // Move assignment
    MoveOnlyResource& operator=(MoveOnlyResource&& other) noexcept {
        if (this != &other) {
            delete[] data_;
            data_ = other.data_;
            size_ = other.size_;
            other.data_ = nullptr;
            other.size_ = 0;
            cout << "Resource move assigned" << endl;
        }
        return *this;
    }
    
    // Delete copy
    MoveOnlyResource(const MoveOnlyResource&) = delete;
    MoveOnlyResource& operator=(const MoveOnlyResource&) = delete;
    
    void use() const {
        if (data_) cout << "Using resource of size " << size_ << endl;
        else cout << "Resource is empty" << endl;
    }
};

int main() {
    cout << "=== Move-Only Types ===" << endl;
    
    cout << "\n1. FileHandle (move-only):" << endl;
    FileHandle f1("test.txt", "w");
    // FileHandle f2 = f1;  // Error! Copy constructor deleted
    FileHandle f2 = move(f1);  // OK - move
    
    f2.write("Hello from moved file");
    
    cout << "\n2. Vector of move-only objects:" << endl;
    vector<MoveOnlyResource> resources;
    resources.push_back(MoveOnlyResource(100));   // Move into vector
    resources.push_back(MoveOnlyResource(200));   // Move into vector
    resources.push_back(MoveOnlyResource(300));   // Move into vector
    
    for (auto& r : resources) {
        r.use();
    }
    
    cout << "\n3. Transferring ownership:" << endl;
    MoveOnlyResource r1(50);
    MoveOnlyResource r2 = move(r1);  // Transfer ownership
    cout << "r1: ";
    r1.use();
    cout << "r2: ";
    r2.use();
    
    return 0;
}
```

---

## 6. **Practical Example: Network Buffer**

```cpp
#include <iostream>
#include <vector>
#include <cstring>
#include <memory>
using namespace std;

class NetworkBuffer {
private:
    char* data_;
    size_t size_;
    
public:
    NetworkBuffer(size_t size) : size_(size) {
        data_ = new char[size_];
        cout << "Buffer allocated: " << size_ << " bytes" << endl;
    }
    
    // Copy constructor (expensive)
    NetworkBuffer(const NetworkBuffer& other) : size_(other.size_) {
        data_ = new char[size_];
        memcpy(data_, other.data_, size_);
        cout << "Buffer copied: " << size_ << " bytes" << endl;
    }
    
    // Move constructor (efficient)
    NetworkBuffer(NetworkBuffer&& other) noexcept
        : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr;
        other.size_ = 0;
        cout << "Buffer moved: " << size_ << " bytes" << endl;
    }
    
    ~NetworkBuffer() {
        if (data_) {
            delete[] data_;
            cout << "Buffer freed: " << size_ << " bytes" << endl;
        }
    }
    
    void fill(const string& data) {
        size_t copySize = min(size_ - 1, data.size());
        memcpy(data_, data.c_str(), copySize);
        data_[copySize] = '\0';
    }
    
    string getData() const {
        return data_ ? string(data_) : "";
    }
    
    size_t size() const { return size_; }
};

class NetworkPacket {
private:
    string source_;
    string destination_;
    NetworkBuffer buffer_;
    
public:
    NetworkPacket(string src, string dest, size_t bufferSize)
        : source_(src), destination_(dest), buffer_(bufferSize) {
        cout << "Packet created: " << source_ << " -> " << destination_ << endl;
    }
    
    // Move constructor
    NetworkPacket(NetworkPacket&& other) noexcept
        : source_(move(other.source_)),
          destination_(move(other.destination_)),
          buffer_(move(other.buffer_)) {
        cout << "Packet moved" << endl;
    }
    
    void setData(const string& data) {
        buffer_.fill(data);
    }
    
    void display() const {
        cout << "Packet: " << source_ << " -> " << destination_ 
             << ", Data: " << buffer_.getData() << endl;
    }
};

class NetworkQueue {
private:
    vector<NetworkPacket> queue_;
    
public:
    void push(NetworkPacket&& packet) {
        queue_.push_back(move(packet));
        cout << "Packet queued. Queue size: " << queue_.size() << endl;
    }
    
    NetworkPacket pop() {
        NetworkPacket packet = move(queue_.front());
        queue_.erase(queue_.begin());
        cout << "Packet dequeued. Queue size: " << queue_.size() << endl;
        return packet;
    }
    
    bool empty() const { return queue_.empty(); }
};

int main() {
    cout << "=== Practical Example: Network Buffer ===" << endl;
    
    NetworkQueue queue;
    
    cout << "\n1. Creating and sending packets:" << endl;
    NetworkPacket p1("192.168.1.1", "192.168.1.2", 1024);
    p1.setData("Hello from client 1");
    queue.push(move(p1));
    
    NetworkPacket p2("10.0.0.1", "10.0.0.2", 2048);
    p2.setData("Hello from client 2");
    queue.push(move(p2));
    
    NetworkPacket p3("172.16.0.1", "172.16.0.2", 512);
    p3.setData("Hello from client 3");
    queue.push(move(p3));
    
    cout << "\n2. Processing packets:" << endl;
    while (!queue.empty()) {
        NetworkPacket packet = queue.pop();
        packet.display();
    }
    
    cout << "\n3. Move semantics benefits:" << endl;
    cout << "   ✓ No copying of buffer data" << endl;
    cout << "   ✓ Efficient queue operations" << endl;
    cout << "   ✓ Automatic resource management" << endl;
    
    return 0;
}
```

---

## 📊 Move Semantics Summary

| Operation | Copy | Move |
|-----------|------|------|
| **Memory** | New allocation | Pointer swap |
| **Performance** | O(n) | O(1) |
| **Exception safety** | May throw | noexcept |
| **Source state** | Unchanged | Valid but unspecified |

---

## ✅ Best Practices

1. **Mark move operations `noexcept`** for optimal performance
2. **Set moved-from objects to valid state** (e.g., nullptr)
3. **Use `std::move`** to cast lvalues to rvalues
4. **Prefer move for large objects** when copying is expensive
5. **Delete copy operations** for move-only types
6. **Use `std::forward`** for perfect forwarding

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Using moved-from object** | Undefined behavior | Don't use after move |
| **Missing noexcept** | Prevents optimizations | Add noexcept |
| **Not resetting source** | Double delete | Set to nullptr |
| **Overusing move** | Premature optimization | Use when beneficial |

---

## ✅ Key Takeaways

1. **Move semantics** transfers resources efficiently
2. **rvalue references** (`&&`) bind to temporaries
3. **Move constructor** transfers from temporary
4. **`std::move`** casts lvalue to rvalue
5. **Move-only types** cannot be copied
6. **Perfect forwarding** preserves value category
7. **`noexcept`** enables optimizations

---