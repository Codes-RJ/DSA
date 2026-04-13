# Bridge Pattern in C++ - Complete Guide

## 📖 Overview

The Bridge pattern decouples an abstraction from its implementation so that the two can vary independently. It uses composition instead of inheritance to avoid a permanent binding between an abstraction and its implementation. This pattern is particularly useful when both the abstraction and implementation need to be extensible.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Abstraction** | High-level control layer that delegates work to implementation |
| **Implementor** | Interface for implementation classes |
| **Concrete Implementor** | Specific implementation of the implementor interface |
| **Refined Abstraction** | Extended abstraction with additional features |

---

## 1. **Basic Bridge Pattern**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Implementor (Device interface)
class IDevice {
public:
    virtual void turnOn() = 0;
    virtual void turnOff() = 0;
    virtual void setVolume(int volume) = 0;
    virtual int getVolume() const = 0;
    virtual ~IDevice() = default;
};

// Concrete Implementor 1: TV
class TV : public IDevice {
private:
    int volume;
    bool isOn;
    
public:
    TV() : volume(10), isOn(false) {}
    
    void turnOn() override {
        isOn = true;
        cout << "TV is now ON" << endl;
    }
    
    void turnOff() override {
        isOn = false;
        cout << "TV is now OFF" << endl;
    }
    
    void setVolume(int vol) override {
        if (isOn) {
            volume = max(0, min(100, vol));
            cout << "TV volume set to " << volume << endl;
        } else {
            cout << "TV is OFF. Turn it on first." << endl;
        }
    }
    
    int getVolume() const override {
        return volume;
    }
};

// Concrete Implementor 2: Radio
class Radio : public IDevice {
private:
    int volume;
    int frequency;
    bool isOn;
    
public:
    Radio() : volume(5), frequency(88,5), isOn(false) {}
    
    void turnOn() override {
        isOn = true;
        cout << "Radio is now ON" << endl;
    }
    
    void turnOff() override {
        isOn = false;
        cout << "Radio is now OFF" << endl;
    }
    
    void setVolume(int vol) override {
        if (isOn) {
            volume = max(0, min(100, vol));
            cout << "Radio volume set to " << volume << endl;
        } else {
            cout << "Radio is OFF. Turn it on first." << endl;
        }
    }
    
    int getVolume() const override {
        return volume;
    }
};

// Abstraction (Remote Control)
class RemoteControl {
protected:
    IDevice* device;
    
public:
    RemoteControl(IDevice* dev) : device(dev) {}
    
    virtual void turnOn() {
        device->turnOn();
    }
    
    virtual void turnOff() {
        device->turnOff();
    }
    
    virtual void volumeUp() {
        device->setVolume(device->getVolume() + 10);
    }
    
    virtual void volumeDown() {
        device->setVolume(device->getVolume() - 10);
    }
    
    virtual ~RemoteControl() = default;
};

// Refined Abstraction (Advanced Remote)
class AdvancedRemoteControl : public RemoteControl {
public:
    AdvancedRemoteControl(IDevice* dev) : RemoteControl(dev) {}
    
    void mute() {
        device->setVolume(0);
        cout << "Device muted" << endl;
    }
    
    void setVolume(int volume) {
        device->setVolume(volume);
    }
};

int main() {
    cout << "=== Basic Bridge Pattern ===" << endl;
    
    TV tv;
    Radio radio;
    
    cout << "\n1. Controlling TV with Basic Remote:" << endl;
    RemoteControl tvRemote(&tv);
    tvRemote.turnOn();
    tvRemote.volumeUp();
    tvRemote.volumeUp();
    tvRemote.volumeDown();
    tvRemote.turnOff();
    
    cout << "\n2. Controlling Radio with Advanced Remote:" << endl;
    AdvancedRemoteControl radioRemote(&radio);
    radioRemote.turnOn();
    radioRemote.setVolume(30);
    radioRemote.mute();
    radioRemote.turnOff();
    
    cout << "\n3. TV with Advanced Remote:" << endl;
    AdvancedRemoteControl tvAdvanced(&tv);
    tvAdvanced.turnOn();
    tvAdvanced.setVolume(50);
    tvAdvanced.mute();
    tvAdvanced.turnOff();
    
    return 0;
}
```

**Output:**
```
=== Basic Bridge Pattern ===

1. Controlling TV with Basic Remote:
TV is now ON
TV volume set to 20
TV volume set to 30
TV volume set to 20
TV is now OFF

2. Controlling Radio with Advanced Remote:
Radio is now ON
Radio volume set to 30
Radio volume set to 0
Device muted
Radio is now OFF

3. TV with Advanced Remote:
TV is now ON
TV volume set to 50
TV volume set to 0
Device muted
TV is now OFF
```

---

## 2. **Bridge Pattern with Multiple Abstractions**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

// Implementor (Drawing API)
class IDrawingAPI {
public:
    virtual void drawCircle(double x, double y, double radius) = 0;
    virtual void drawRectangle(double x, double y, double width, double height) = 0;
    virtual void drawText(double x, double y, const string& text) = 0;
    virtual ~IDrawingAPI() = default;
};

// Concrete Implementor 1: Vector Drawing
class VectorDrawingAPI : public IDrawingAPI {
public:
    void drawCircle(double x, double y, double radius) override {
        cout << "Vector: Circle at (" << x << ", " << y 
             << ") radius=" << radius << endl;
    }
    
    void drawRectangle(double x, double y, double width, double height) override {
        cout << "Vector: Rectangle at (" << x << ", " << y 
             << ") size=" << width << "x" << height << endl;
    }
    
    void drawText(double x, double y, const string& text) override {
        cout << "Vector: Text '" << text << "' at (" << x << ", " << y << ")" << endl;
    }
};

// Concrete Implementor 2: Raster Drawing
class RasterDrawingAPI : public IDrawingAPI {
public:
    void drawCircle(double x, double y, double radius) override {
        cout << "Raster: Circle at (" << x << ", " << y 
             << ") radius=" << radius << endl;
    }
    
    void drawRectangle(double x, double y, double width, double height) override {
        cout << "Raster: Rectangle at (" << x << ", " << y 
             << ") size=" << width << "x" << height << endl;
    }
    
    void drawText(double x, double y, const string& text) override {
        cout << "Raster: Text '" << text << "' at (" << x << ", " << y << ")" << endl;
    }
};

// Concrete Implementor 3: 3D Drawing
class ThreeDDrawingAPI : public IDrawingAPI {
public:
    void drawCircle(double x, double y, double radius) override {
        cout << "3D: Circle at (" << x << ", " << y 
             << ", 0) radius=" << radius << endl;
    }
    
    void drawRectangle(double x, double y, double width, double height) override {
        cout << "3D: Rectangle at (" << x << ", " << y 
             << ", 0) size=" << width << "x" << height << endl;
    }
    
    void drawText(double x, double y, const string& text) override {
        cout << "3D: Text '" << text << "' at (" << x << ", " << y << ", 0)" << endl;
    }
};

// Abstraction (Shape)
class Shape {
protected:
    IDrawingAPI* drawingAPI;
    double x, y;
    
public:
    Shape(IDrawingAPI* api, double xPos, double yPos) 
        : drawingAPI(api), x(xPos), y(yPos) {}
    
    virtual void draw() = 0;
    virtual void move(double dx, double dy) {
        x += dx;
        y += dy;
    }
    
    virtual ~Shape() = default;
};

// Refined Abstraction 1: Circle
class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(IDrawingAPI* api, double xPos, double yPos, double r) 
        : Shape(api, xPos, yPos), radius(r) {}
    
    void draw() override {
        drawingAPI->drawCircle(x, y, radius);
    }
};

// Refined Abstraction 2: Rectangle
class RectangleShape : public Shape {
private:
    double width, height;
    
public:
    RectangleShape(IDrawingAPI* api, double xPos, double yPos, double w, double h) 
        : Shape(api, xPos, yPos), width(w), height(h) {}
    
    void draw() override {
        drawingAPI->drawRectangle(x, y, width, height);
    }
};

// Refined Abstraction 3: Text
class TextShape : public Shape {
private:
    string text;
    
public:
    TextShape(IDrawingAPI* api, double xPos, double yPos, const string& txt) 
        : Shape(api, xPos, yPos), text(txt) {}
    
    void draw() override {
        drawingAPI->drawText(x, y, text);
    }
};

int main() {
    cout << "=== Bridge Pattern with Multiple Abstractions ===" << endl;
    
    VectorDrawingAPI vectorAPI;
    RasterDrawingAPI rasterAPI;
    ThreeDDrawingAPI threeDAPI;
    
    cout << "\n1. Vector Drawing:" << endl;
    Circle circle1(&vectorAPI, 10, 20, 5);
    RectangleShape rect1(&vectorAPI, 30, 40, 10, 6);
    TextShape text1(&vectorAPI, 50, 60, "Hello");
    
    circle1.draw();
    rect1.draw();
    text1.draw();
    
    cout << "\n2. Raster Drawing:" << endl;
    Circle circle2(&rasterAPI, 10, 20, 5);
    RectangleShape rect2(&rasterAPI, 30, 40, 10, 6);
    TextShape text2(&rasterAPI, 50, 60, "World");
    
    circle2.draw();
    rect2.draw();
    text2.draw();
    
    cout << "\n3. 3D Drawing:" << endl;
    Circle circle3(&threeDAPI, 10, 20, 5);
    circle3.draw();
    
    return 0;
}
```

---

## 3. **Bridge Pattern with Dynamic Switching**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// Implementor (Compression Algorithm)
class ICompression {
public:
    virtual string compress(const string& data) = 0;
    virtual string decompress(const string& data) = 0;
    virtual ~ICompression() = default;
};

// Concrete Implementor 1: ZIP Compression
class ZIPCompression : public ICompression {
public:
    string compress(const string& data) override {
        return "[ZIP:" + data + "]";
    }
    
    string decompress(const string& data) override {
        // Remove [ZIP: and ]
        return data.substr(5, data.length() - 6);
    }
};

// Concrete Implementor 2: RAR Compression
class RARCompression : public ICompression {
public:
    string compress(const string& data) override {
        return "[RAR:" + data + "]";
    }
    
    string decompress(const string& data) override {
        return data.substr(5, data.length() - 6);
    }
};

// Concrete Implementor 3: GZIP Compression
class GZIPCompression : public ICompression {
public:
    string compress(const string& data) override {
        return "[GZIP:" + data + "]";
    }
    
    string decompress(const string& data) override {
        return data.substr(6, data.length() - 7);
    }
};

// Abstraction (DataProcessor)
class DataProcessor {
protected:
    unique_ptr<ICompression> compression;
    
public:
    DataProcessor(ICompression* comp) : compression(comp) {}
    
    virtual string process(const string& data) {
        return compression->compress(data);
    }
    
    virtual string recover(const string& data) {
        return compression->decompress(data);
    }
    
    void setCompression(ICompression* comp) {
        compression.reset(comp);
    }
    
    virtual ~DataProcessor() = default;
};

// Refined Abstraction (EncryptedDataProcessor)
class EncryptedDataProcessor : public DataProcessor {
private:
    int shift;
    
    string encrypt(const string& data) {
        string result = data;
        for (char& c : result) {
            c = c + shift;
        }
        return result;
    }
    
    string decrypt(const string& data) {
        string result = data;
        for (char& c : result) {
            c = c - shift;
        }
        return result;
    }
    
public:
    EncryptedDataProcessor(ICompression* comp, int s) 
        : DataProcessor(comp), shift(s) {}
    
    string process(const string& data) override {
        string compressed = compression->compress(data);
        return encrypt(compressed);
    }
    
    string recover(const string& data) override {
        string decrypted = decrypt(data);
        return compression->decompress(decrypted);
    }
};

int main() {
    cout << "=== Bridge Pattern with Dynamic Switching ===" << endl;
    
    cout << "\n1. Basic Data Processor with different compression:" << endl;
    DataProcessor zipProc(new ZIPCompression());
    DataProcessor rarProc(new RARCompression());
    
    string data = "Hello World";
    
    string zipData = zipProc.process(data);
    cout << "ZIP compressed: " << zipData << endl;
    cout << "ZIP decompressed: " << zipProc.recover(zipData) << endl;
    
    string rarData = rarProc.process(data);
    cout << "RAR compressed: " << rarData << endl;
    cout << "RAR decompressed: " << rarProc.recover(rarData) << endl;
    
    cout << "\n2. Dynamic switching of compression:" << endl;
    DataProcessor processor(new ZIPCompression());
    
    string processed = processor.process("Test Data");
    cout << "With ZIP: " << processed << endl;
    
    processor.setCompression(new RARCompression());
    processed = processor.process("Test Data");
    cout << "With RAR: " << processed << endl;
    
    processor.setCompression(new GZIPCompression());
    processed = processor.process("Test Data");
    cout << "With GZIP: " << processed << endl;
    
    cout << "\n3. Encrypted Data Processor:" << endl;
    EncryptedDataProcessor encProc(new ZIPCompression(), 3);
    
    string original = "Secret Message";
    string processed2 = encProc.process(original);
    cout << "Processed: " << processed2 << endl;
    cout << "Recovered: " << encProc.recover(processed2) << endl;
    
    return 0;
}
```

---

## 4. **Bridge Pattern with Platform Abstraction**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <vector>
using namespace std;

// Implementor (Operating System)
class IOS {
public:
    virtual void createWindow(const string& title) = 0;
    virtual void createButton(const string& label) = 0;
    virtual void showMessage(const string& msg) = 0;
    virtual ~IOS() = default;
};

// Concrete Implementor 1: Windows
class WindowsOS : public IOS {
public:
    void createWindow(const string& title) override {
        cout << "[Windows] Creating window: " << title << endl;
    }
    
    void createButton(const string& label) override {
        cout << "[Windows] Creating button: " << label << endl;
    }
    
    void showMessage(const string& msg) override {
        cout << "[Windows] Message box: " << msg << endl;
    }
};

// Concrete Implementor 2: Linux
class LinuxOS : public IOS {
public:
    void createWindow(const string& title) override {
        cout << "[Linux] Creating window: " << title << endl;
    }
    
    void createButton(const string& label) override {
        cout << "[Linux] Creating button: " << label << endl;
    }
    
    void showMessage(const string& msg) override {
        cout << "[Linux] Dialog: " << msg << endl;
    }
};

// Concrete Implementor 3: MacOS
class MacOS : public IOS {
public:
    void createWindow(const string& title) override {
        cout << "[MacOS] Creating window: " << title << endl;
    }
    
    void createButton(const string& label) override {
        cout << "[MacOS] Creating button: " << label << endl;
    }
    
    void showMessage(const string& msg) override {
        cout << "[MacOS] Alert: " << msg << endl;
    }
};

// Abstraction (UI Element)
class UIElement {
protected:
    IOS* os;
    
public:
    UIElement(IOS* operatingSystem) : os(operatingSystem) {}
    
    virtual void render() = 0;
    virtual ~UIElement() = default;
};

// Refined Abstraction 1: Window
class Window : public UIElement {
private:
    string title;
    
public:
    Window(IOS* os, const string& t) : UIElement(os), title(t) {}
    
    void render() override {
        os->createWindow(title);
    }
};

// Refined Abstraction 2: Button
class Button : public UIElement {
private:
    string label;
    
public:
    Button(IOS* os, const string& l) : UIElement(os), label(l) {}
    
    void render() override {
        os->createButton(label);
    }
};

// Refined Abstraction 3: Dialog
class Dialog : public UIElement {
private:
    string message;
    
public:
    Dialog(IOS* os, const string& msg) : UIElement(os), message(msg) {}
    
    void render() override {
        os->showMessage(message);
    }
};

// Application class that can switch platforms
class Application {
private:
    vector<unique_ptr<UIElement>> elements;
    unique_ptr<IOS> currentOS;
    
public:
    void setPlatform(IOS* os) {
        currentOS.reset(os);
        // Recreate UI elements for new platform
        recreateUI();
    }
    
    void addWindow(const string& title) {
        if (currentOS) {
            elements.push_back(make_unique<Window>(currentOS.get(), title));
        }
    }
    
    void addButton(const string& label) {
        if (currentOS) {
            elements.push_back(make_unique<Button>(currentOS.get(), label));
        }
    }
    
    void addDialog(const string& message) {
        if (currentOS) {
            elements.push_back(make_unique<Dialog>(currentOS.get(), message));
        }
    }
    
    void render() {
        for (auto& elem : elements) {
            elem->render();
        }
    }
    
private:
    void recreateUI() {
        // In a real app, would need to store UI configuration
        cout << "\n--- Recreating UI for new platform ---" << endl;
    }
};

int main() {
    cout << "=== Bridge Pattern with Platform Abstraction ===" << endl;
    
    Application app;
    
    cout << "\n1. Windows Application:" << endl;
    app.setPlatform(new WindowsOS());
    app.addWindow("Main Window");
    app.addButton("Click Me");
    app.addDialog("Welcome to the app");
    app.render();
    
    cout << "\n2. Linux Application (same UI, different platform):" << endl;
    app.setPlatform(new LinuxOS());
    app.render();
    
    cout << "\n3. MacOS Application (same UI, different platform):" << endl;
    app.setPlatform(new MacOS());
    app.render();
    
    return 0;
}
```

---

## 5. **Practical Example: Database Abstraction Layer**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <map>
using namespace std;

// Implementor (Database Driver)
class IDatabaseDriver {
public:
    virtual void connect(const string& connectionString) = 0;
    virtual void disconnect() = 0;
    virtual void executeQuery(const string& sql) = 0;
    virtual vector<map<string, string>> fetchResults() = 0;
    virtual ~IDatabaseDriver() = default;
};

// Concrete Implementor 1: MySQL Driver
class MySQLDriver : public IDatabaseDriver {
private:
    bool connected;
    
public:
    MySQLDriver() : connected(false) {}
    
    void connect(const string& connectionString) override {
        cout << "MySQL: Connecting to " << connectionString << endl;
        connected = true;
    }
    
    void disconnect() override {
        cout << "MySQL: Disconnecting" << endl;
        connected = false;
    }
    
    void executeQuery(const string& sql) override {
        if (connected) {
            cout << "MySQL: Executing query: " << sql << endl;
        }
    }
    
    vector<map<string, string>> fetchResults() override {
        vector<map<string, string>> results;
        map<string, string> row;
        row["id"] = "1";
        row["name"] = "MySQL Data";
        results.push_back(row);
        return results;
    }
};

// Concrete Implementor 2: PostgreSQL Driver
class PostgreSQLDriver : public IDatabaseDriver {
private:
    bool connected;
    
public:
    PostgreSQLDriver() : connected(false) {}
    
    void connect(const string& connectionString) override {
        cout << "PostgreSQL: Connecting to " << connectionString << endl;
        connected = true;
    }
    
    void disconnect() override {
        cout << "PostgreSQL: Disconnecting" << endl;
        connected = false;
    }
    
    void executeQuery(const string& sql) override {
        if (connected) {
            cout << "PostgreSQL: Executing query: " << sql << endl;
        }
    }
    
    vector<map<string, string>> fetchResults() override {
        vector<map<string, string>> results;
        map<string, string> row;
        row["id"] = "1";
        row["name"] = "PostgreSQL Data";
        results.push_back(row);
        return results;
    }
};

// Concrete Implementor 3: SQLite Driver
class SQLiteDriver : public IDatabaseDriver {
private:
    bool connected;
    string dbFile;
    
public:
    SQLiteDriver() : connected(false) {}
    
    void connect(const string& connectionString) override {
        dbFile = connectionString;
        cout << "SQLite: Opening database file " << dbFile << endl;
        connected = true;
    }
    
    void disconnect() override {
        cout << "SQLite: Closing database" << endl;
        connected = false;
    }
    
    void executeQuery(const string& sql) override {
        if (connected) {
            cout << "SQLite: Executing query: " << sql << endl;
        }
    }
    
    vector<map<string, string>> fetchResults() override {
        vector<map<string, string>> results;
        map<string, string> row;
        row["id"] = "1";
        row["name"] = "SQLite Data";
        results.push_back(row);
        return results;
    }
};

// Abstraction (Database Layer)
class Database {
protected:
    unique_ptr<IDatabaseDriver> driver;
    string connectionString;
    
public:
    Database(IDatabaseDriver* drv, const string& conn) 
        : driver(drv), connectionString(conn) {}
    
    virtual void connect() {
        driver->connect(connectionString);
    }
    
    virtual void disconnect() {
        driver->disconnect();
    }
    
    virtual void query(const string& sql) {
        driver->executeQuery(sql);
    }
    
    virtual vector<map<string, string>> getResults() {
        return driver->fetchResults();
    }
    
    virtual ~Database() = default;
};

// Refined Abstraction (Transactional Database)
class TransactionalDatabase : public Database {
private:
    bool inTransaction;
    
public:
    TransactionalDatabase(IDatabaseDriver* drv, const string& conn) 
        : Database(drv, conn), inTransaction(false) {}
    
    void beginTransaction() {
        if (!inTransaction) {
            driver->executeQuery("BEGIN TRANSACTION");
            inTransaction = true;
            cout << "Transaction started" << endl;
        }
    }
    
    void commit() {
        if (inTransaction) {
            driver->executeQuery("COMMIT");
            inTransaction = false;
            cout << "Transaction committed" << endl;
        }
    }
    
    void rollback() {
        if (inTransaction) {
            driver->executeQuery("ROLLBACK");
            inTransaction = false;
            cout << "Transaction rolled back" << endl;
        }
    }
    
    void query(const string& sql) override {
        if (!inTransaction) {
            cout << "Warning: Query outside transaction!" << endl;
        }
        Database::query(sql);
    }
};

// Refined Abstraction (Cached Database)
class CachedDatabase : public Database {
private:
    map<string, vector<map<string, string>>> cache;
    
public:
    CachedDatabase(IDatabaseDriver* drv, const string& conn) 
        : Database(drv, conn) {}
    
    void query(const string& sql) override {
        if (cache.find(sql) != cache.end()) {
            cout << "Cache hit for: " << sql << endl;
            return;
        }
        
        cout << "Cache miss for: " << sql << endl;
        Database::query(sql);
        cache[sql] = driver->fetchResults();
    }
    
    void clearCache() {
        cache.clear();
        cout << "Cache cleared" << endl;
    }
};

int main() {
    cout << "=== Database Abstraction Layer with Bridge Pattern ===" << endl;
    
    cout << "\n1. Simple Database:" << endl;
    Database mysql(new MySQLDriver(), "mysql://localhost/mydb");
    mysql.connect();
    mysql.query("SELECT * FROM users");
    mysql.disconnect();
    
    cout << "\n2. Transactional Database:" << endl;
    TransactionalDatabase pg(new PostgreSQLDriver(), "postgresql://localhost/mydb");
    pg.connect();
    pg.beginTransaction();
    pg.query("INSERT INTO users VALUES('John')");
    pg.query("UPDATE users SET name='Jane'");
    pg.commit();
    pg.disconnect();
    
    cout << "\n3. Cached Database:" << endl;
    CachedDatabase sqlite(new SQLiteDriver(), "mydb.db");
    sqlite.connect();
    sqlite.query("SELECT * FROM products");
    sqlite.query("SELECT * FROM products");  // Cache hit
    sqlite.query("SELECT * FROM orders");
    sqlite.clearCache();
    sqlite.query("SELECT * FROM products");  // Cache miss again
    sqlite.disconnect();
    
    return 0;
}
```

---

## 📊 Bridge Pattern Summary

| Component | Description |
|-----------|-------------|
| **Abstraction** | High-level interface for clients |
| **Refined Abstraction** | Extended abstraction with additional features |
| **Implementor** | Interface for implementation classes |
| **Concrete Implementor** | Specific implementation |

---

## ✅ Best Practices

1. **Use Bridge** when both abstraction and implementation can vary
2. **Prefer composition** over inheritance for decoupling
3. **Keep implementor interface** stable and simple
4. **Document** the separation between abstraction and implementation
5. **Consider using** dependency injection for implementation selection

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Over-engineering** | Unnecessary complexity | Only use when both sides vary |
| **Leaky abstraction** | Implementation details exposed | Keep interfaces clean |
| **Performance overhead** | Extra indirection | Acceptable trade-off for flexibility |

---

## ✅ Key Takeaways

1. **Bridge pattern** decouples abstraction from implementation
2. **Both can vary** independently
3. **Uses composition** instead of inheritance
4. **Useful for** cross-platform development
5. **Follows** Open/Closed Principle
6. **Reduces** class explosion from combinatorial growth

---
---

## Next Step

- Go to [Composite.md](Composite.md) to continue with Composite.
