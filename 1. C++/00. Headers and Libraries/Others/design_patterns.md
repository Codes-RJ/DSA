# Design Patterns - Common C++ Design Patterns

Design patterns are proven, reusable solutions to recurring software design problems. They are blueprints — not code — that you adapt to your specific situation.

## 📖 Overview

Patterns are grouped into three categories (Gang of Four, GoF):
- **Creational** — how objects are created (Singleton, Factory, Builder, Prototype)
- **Structural** — how objects are composed (Adapter, Decorator, Facade, Proxy)
- **Behavioural** — how objects communicate (Observer, Strategy, Command, Visitor)

**Rule of thumb**: use a pattern only when it solves a real design problem you actually have. Over-engineering with patterns is a common mistake.

## 🎯 Key Patterns Overview

| Pattern | Category | Purpose |
|---------|----------|---------|
| Singleton | Creational | Exactly one instance of a class |
| Factory Method | Creational | Subclasses decide which class to instantiate |
| Abstract Factory | Creational | Families of related objects |
| Builder | Creational | Step-by-step complex object construction |
| Observer | Behavioural | One-to-many event notification |
| Strategy | Behavioural | Swappable algorithms at runtime |
| Command | Behavioural | Encapsulate requests as objects |
| Decorator | Structural | Add behaviour without subclassing |
| CRTP | C++-specific | Compile-time polymorphism |
| PIMPL | C++-specific | ABI stability / hide implementation |

## 🔧 Creational Patterns

### Singleton — Exactly One Instance
```cpp
#include <iostream>
#include <mutex>

class AppConfig {
    std::string dbHost_ = "localhost";
    int         dbPort_ = 5432;

    // Private constructor prevents external construction
    AppConfig() { std::cout << "AppConfig initialised\n"; }

public:
    // Thread-safe lazy init (C++11 guarantees static local init is thread-safe)
    static AppConfig& getInstance() {
        static AppConfig instance;
        return instance;
    }

    // Delete copy and assignment
    AppConfig(const AppConfig&)            = delete;
    AppConfig& operator=(const AppConfig&) = delete;

    const std::string& dbHost() const { return dbHost_; }
    int                dbPort() const { return dbPort_; }

    void setDbHost(const std::string& h) { dbHost_ = h; }
};

int main() {
    AppConfig& cfg = AppConfig::getInstance();
    cfg.setDbHost("db.example.com");

    // Same instance everywhere
    std::cout << AppConfig::getInstance().dbHost() << "\n"; // db.example.com
    return 0;
}
```

### Factory Method — Let Subclasses Decide
```cpp
#include <iostream>
#include <memory>
#include <string>

class Logger {
public:
    virtual ~Logger() = default;
    virtual void log(const std::string& msg) = 0;
};

class ConsoleLogger : public Logger {
public:
    void log(const std::string& msg) override {
        std::cout << "[CONSOLE] " << msg << "\n";
    }
};

class FileLogger : public Logger {
    std::string filename_;
public:
    FileLogger(const std::string& f) : filename_(f) {}
    void log(const std::string& msg) override {
        std::cout << "[FILE:" << filename_ << "] " << msg << "\n";
    }
};

// Factory function
std::unique_ptr<Logger> createLogger(const std::string& type) {
    if (type == "console") return std::make_unique<ConsoleLogger>();
    if (type == "file")    return std::make_unique<FileLogger>("app.log");
    return nullptr;
}

int main() {
    auto log1 = createLogger("console");
    auto log2 = createLogger("file");

    log1->log("Application started");
    log2->log("Application started");
    return 0;
}
```

### Builder — Step-by-Step Construction
```cpp
#include <iostream>
#include <string>

struct HttpRequest {
    std::string method  = "GET";
    std::string url;
    std::string body;
    int         timeout = 30;
    bool        ssl     = true;
};

class HttpRequestBuilder {
    HttpRequest req_;
public:
    HttpRequestBuilder& method (const std::string& m) { req_.method  = m; return *this; }
    HttpRequestBuilder& url    (const std::string& u) { req_.url     = u; return *this; }
    HttpRequestBuilder& body   (const std::string& b) { req_.body    = b; return *this; }
    HttpRequestBuilder& timeout(int t)                 { req_.timeout = t; return *this; }
    HttpRequestBuilder& ssl    (bool s)                { req_.ssl     = s; return *this; }
    HttpRequest build() { return req_; }
};

int main() {
    HttpRequest req = HttpRequestBuilder()
        .method("POST")
        .url("https://api.example.com/data")
        .body(R"({"key":"value"})")
        .timeout(60)
        .ssl(true)
        .build();

    std::cout << req.method << " " << req.url << "\n";
    std::cout << "Timeout: " << req.timeout << "s, SSL: " << std::boolalpha << req.ssl << "\n";
    return 0;
}
```

## 🔧 Behavioural Patterns

### Observer — Event Notification
```cpp
#include <iostream>
#include <vector>
#include <functional>
#include <string>

class EventEmitter {
    std::vector<std::function<void(const std::string&)>> listeners_;
    std::string name_;
public:
    EventEmitter(const std::string& n) : name_(n) {}

    void subscribe(std::function<void(const std::string&)> fn) {
        listeners_.push_back(std::move(fn));
    }

    void emit(const std::string& event) {
        std::cout << "[" << name_ << "] emitting: " << event << "\n";
        for (auto& fn : listeners_) fn(event);
    }
};

int main() {
    EventEmitter btn("SubmitButton");

    btn.subscribe([](const std::string& e) {
        std::cout << "  Handler A: got '" << e << "'\n";
    });
    btn.subscribe([](const std::string& e) {
        std::cout << "  Handler B: validating for '" << e << "'\n";
    });

    btn.emit("click");
    btn.emit("focus");
    return 0;
}
```

### Strategy — Swappable Algorithms
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

class Sorter {
    std::function<void(std::vector<int>&)> strategy_;
public:
    void setStrategy(std::function<void(std::vector<int>&)> s) {
        strategy_ = std::move(s);
    }
    void sort(std::vector<int>& v) {
        if (strategy_) strategy_(v);
    }
};

int main() {
    std::vector<int> data = {5, 2, 8, 1, 9, 3};

    Sorter sorter;

    // Strategy 1: ascending
    sorter.setStrategy([](std::vector<int>& v) {
        std::sort(v.begin(), v.end());
    });
    sorter.sort(data);
    for (int n : data) std::cout << n << " ";
    std::cout << "\n"; // 1 2 3 5 8 9

    // Strategy 2: descending
    sorter.setStrategy([](std::vector<int>& v) {
        std::sort(v.rbegin(), v.rend());
    });
    sorter.sort(data);
    for (int n : data) std::cout << n << " ";
    std::cout << "\n"; // 9 8 5 3 2 1

    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Command Pattern — Undo/Redo
```cpp
#include <iostream>
#include <stack>
#include <functional>
#include <string>

class TextEditor {
    std::string text_;
    std::stack<std::pair<std::function<void()>, std::function<void()>>> history_;

public:
    void execute(std::function<void()> doFn, std::function<void()> undoFn) {
        doFn();
        history_.push({doFn, undoFn});
    }

    void type(const std::string& s) {
        execute(
            [this, s]() { text_ += s; std::cout << "Typed: '" << s << "'\n"; },
            [this, n = s.size()]() { text_.resize(text_.size() - n); std::cout << "Undo type\n"; }
        );
    }

    void undo() {
        if (!history_.empty()) {
            history_.top().second();
            history_.pop();
        }
    }

    const std::string& text() const { return text_; }
};

int main() {
    TextEditor editor;
    editor.type("Hello");
    editor.type(", World");
    std::cout << "Text: " << editor.text() << "\n";

    editor.undo();
    std::cout << "After undo: " << editor.text() << "\n";

    editor.undo();
    std::cout << "After undo: " << editor.text() << "\n";
    return 0;
}
```

### Example 2: Decorator — Adding Behaviour Without Subclassing
```cpp
#include <iostream>
#include <memory>
#include <string>

// Base interface
class DataSource {
public:
    virtual ~DataSource() = default;
    virtual std::string read()               = 0;
    virtual void        write(const std::string& data) = 0;
};

// Concrete component
class FileDataSource : public DataSource {
    std::string content_;
public:
    std::string read() override { return content_; }
    void write(const std::string& data) override {
        content_ = data;
        std::cout << "FileDataSource wrote: " << data << "\n";
    }
};

// Decorator base
class DataSourceDecorator : public DataSource {
protected:
    std::unique_ptr<DataSource> wrappee_;
public:
    DataSourceDecorator(std::unique_ptr<DataSource> ds) : wrappee_(std::move(ds)) {}
    std::string read()               override { return wrappee_->read(); }
    void        write(const std::string& data) override { wrappee_->write(data); }
};

// Compression decorator
class CompressionDecorator : public DataSourceDecorator {
public:
    using DataSourceDecorator::DataSourceDecorator;
    void write(const std::string& data) override {
        std::string compressed = "[COMPRESSED:" + data + "]";
        std::cout << "CompressionDecorator compressing\n";
        wrappee_->write(compressed);
    }
    std::string read() override {
        std::string raw = wrappee_->read();
        // strip [COMPRESSED:...] wrapper
        if (raw.size() > 14) return raw.substr(13, raw.size() - 14);
        return raw;
    }
};

// Encryption decorator
class EncryptionDecorator : public DataSourceDecorator {
public:
    using DataSourceDecorator::DataSourceDecorator;
    void write(const std::string& data) override {
        std::string encrypted = "{ENCRYPTED:" + data + "}";
        std::cout << "EncryptionDecorator encrypting\n";
        wrappee_->write(encrypted);
    }
};

int main() {
    // Stack decorators: File → Compression → Encryption
    auto source = std::make_unique<FileDataSource>();
    auto compressed = std::make_unique<CompressionDecorator>(std::move(source));
    auto encrypted  = std::make_unique<EncryptionDecorator>(std::move(compressed));

    encrypted->write("Hello, World!");
    return 0;
}
```

### Example 3: PIMPL — Hide Implementation Details
```cpp
// Widget.h — public header (no implementation details exposed)
#include <memory>
#include <string>

class Widget {
public:
    Widget();
    ~Widget();
    Widget(Widget&&) noexcept;
    Widget& operator=(Widget&&) noexcept;

    void setTitle(const std::string& title);
    void render() const;

private:
    class Impl;                    // forward declaration only
    std::unique_ptr<Impl> pImpl_;  // pointer to implementation
};

// Widget.cpp — implementation hidden from users
struct Widget::Impl {
    std::string title = "Untitled";
    int x = 0, y = 0, w = 800, h = 600;

    void render() const {
        std::cout << "Rendering Widget '" << title << "' at ("
                  << x << "," << y << ") size " << w << "x" << h << "\n";
    }
};

Widget::Widget()  : pImpl_(std::make_unique<Impl>()) {}
Widget::~Widget() = default;
Widget::Widget(Widget&&) noexcept            = default;
Widget& Widget::operator=(Widget&&) noexcept = default;

void Widget::setTitle(const std::string& t) { pImpl_->title = t; }
void Widget::render() const                 { pImpl_->render(); }

int main() {
    Widget w;
    w.setTitle("My App Window");
    w.render();
    return 0;
}
```

### Example 4: Visitor — Operations on an Object Hierarchy
```cpp
#include <iostream>
#include <vector>
#include <memory>
#include <string>

// Forward declarations
class Circle; class Rectangle; class Triangle;

class ShapeVisitor {
public:
    virtual ~ShapeVisitor() = default;
    virtual void visit(const Circle&)    = 0;
    virtual void visit(const Rectangle&) = 0;
    virtual void visit(const Triangle&)  = 0;
};

class Shape {
public:
    virtual ~Shape() = default;
    virtual void accept(ShapeVisitor& v) const = 0;
};

class Circle : public Shape {
public:
    double radius;
    Circle(double r) : radius(r) {}
    void accept(ShapeVisitor& v) const override { v.visit(*this); }
};

class Rectangle : public Shape {
public:
    double w, h;
    Rectangle(double w, double h) : w(w), h(h) {}
    void accept(ShapeVisitor& v) const override { v.visit(*this); }
};

class Triangle : public Shape {
public:
    double base, height;
    Triangle(double b, double h) : base(b), height(h) {}
    void accept(ShapeVisitor& v) const override { v.visit(*this); }
};

// Area computing visitor
class AreaVisitor : public ShapeVisitor {
public:
    double total = 0;
    void visit(const Circle& c)    override { total += 3.14159 * c.radius * c.radius; }
    void visit(const Rectangle& r) override { total += r.w * r.h; }
    void visit(const Triangle& t)  override { total += 0.5 * t.base * t.height; }
};

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>(5));
    shapes.push_back(std::make_unique<Rectangle>(4, 6));
    shapes.push_back(std::make_unique<Triangle>(3, 8));

    AreaVisitor areaCalc;
    for (const auto& s : shapes) s->accept(areaCalc);
    std::cout << "Total area: " << areaCalc.total << "\n";
    return 0;
}
```

## ⚡ Performance Tips

### Prefer CRTP Over Virtual for Compile-Time Polymorphism
```cpp
// CRTP: zero virtual dispatch overhead
template <typename Derived>
class Base {
public:
    void doWork() { static_cast<Derived*>(this)->impl(); }
};

class Concrete : public Base<Concrete> {
public:
    void impl() { std::cout << "Concrete::impl\n"; }
};
```

### Use `std::function` Lazily — It Has Overhead
```cpp
// std::function involves type erasure and potential heap allocation
// For performance-critical callbacks, use templates with `auto` or function pointers
```

## 🐛 Common Pitfalls & Solutions

### 1. Singleton as Global State (Testability Problem)
```cpp
// Singletons make unit testing hard — code can't easily swap implementations
// Fix: prefer dependency injection; use Singleton only for truly global resources
```

### 2. Circular References in Observer
```cpp
// Subject holds shared_ptr<Observer>; Observer holds shared_ptr<Subject>
// Fix: Subject holds weak_ptr<Observer> to break the cycle
```

### 3. Forgetting to Make Destructor `virtual` in Abstract Base
```cpp
// Deleting via base pointer without virtual destructor → partial destruction!
class Base {
public:
    virtual ~Base() = default; // REQUIRED for polymorphic deletion
};
```

### 4. Over-Using Patterns
```cpp
// Not every function needs a Strategy, not every class needs a Factory
// Ask: does this pattern solve a problem I actually have?
```

## 🎯 Best Practices

1. **Use patterns to solve real problems** — not to show off architecture
2. **Prefer composition over inheritance** — it's more flexible
3. **Always declare virtual destructors** in polymorphic base classes
4. **Use `unique_ptr` for ownership** in patterns involving dynamic allocation
5. **Prefer lambdas over functor classes** for Strategy and Command in modern C++
6. **Document why you chose a pattern** — future readers will thank you

## 📚 Related Topics

- [`smart_pointers.md`](smart_pointers.md) — Essential for managing lifetime in pattern implementations
- [`lambda_expressions.md`](lambda_expressions.md) — Lambdas as lightweight Strategy/Command objects
- [`templates.md`](templates.md) — CRTP for compile-time patterns
- [`move_semantics.md`](move_semantics.md) — Move uniquely-owned objects through patterns

## 🚀 Next Steps

1. Implement an Observer-based event system with automatic cleanup via `weak_ptr`
2. Build a Builder for a complex configuration object in your project
3. Read "Design Patterns" (GoF) for the original 23 patterns with UML diagrams
4. Explore modern C++ pattern implementations in "Hands-On Design Patterns with C++" by Fedor Pikus
---

## Next Step

- Go to [filesystem.md](filesystem.md) to continue with filesystem.
