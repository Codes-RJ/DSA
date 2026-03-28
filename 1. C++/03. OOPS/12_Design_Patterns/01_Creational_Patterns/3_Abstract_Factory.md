# 12_Design_Patterns/01_Creational_Patterns/Abstract_Factory.md

# Abstract Factory Pattern in C++ - Complete Guide

## 📖 Overview

The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. It encapsulates a group of individual factories that share a common theme. This pattern is particularly useful when a system needs to be independent of how its objects are created, composed, and represented.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Abstract Factory** | Interface for creating families of related objects |
| **Concrete Factory** | Implements creation methods for a specific family |
| **Abstract Product** | Interface for a type of product |
| **Concrete Product** | Specific implementation of a product |

---

## 1. **Basic Abstract Factory**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// Abstract Products
class IButton {
public:
    virtual void render() = 0;
    virtual void onClick() = 0;
    virtual ~IButton() = default;
};

class ITextBox {
public:
    virtual void render() = 0;
    virtual void setText(const string& text) = 0;
    virtual ~ITextBox() = default;
};

// Concrete Products for Windows
class WindowsButton : public IButton {
public:
    void render() override {
        cout << "Rendering Windows button" << endl;
    }
    
    void onClick() override {
        cout << "Windows button clicked" << endl;
    }
};

class WindowsTextBox : public ITextBox {
private:
    string text;
    
public:
    void render() override {
        cout << "Rendering Windows text box: " << text << endl;
    }
    
    void setText(const string& t) override {
        text = t;
    }
};

// Concrete Products for Mac
class MacButton : public IButton {
public:
    void render() override {
        cout << "Rendering Mac button" << endl;
    }
    
    void onClick() override {
        cout << "Mac button clicked" << endl;
    }
};

class MacTextBox : public ITextBox {
private:
    string text;
    
public:
    void render() override {
        cout << "Rendering Mac text box: " << text << endl;
    }
    
    void setText(const string& t) override {
        text = t;
    }
};

// Abstract Factory
class GUIFactory {
public:
    virtual unique_ptr<IButton> createButton() = 0;
    virtual unique_ptr<ITextBox> createTextBox() = 0;
    virtual ~GUIFactory() = default;
};

// Concrete Factory for Windows
class WindowsFactory : public GUIFactory {
public:
    unique_ptr<IButton> createButton() override {
        return make_unique<WindowsButton>();
    }
    
    unique_ptr<ITextBox> createTextBox() override {
        return make_unique<WindowsTextBox>();
    }
};

// Concrete Factory for Mac
class MacFactory : public GUIFactory {
public:
    unique_ptr<IButton> createButton() override {
        return make_unique<MacButton>();
    }
    
    unique_ptr<ITextBox> createTextBox() override {
        return make_unique<MacTextBox>();
    }
};

class Application {
private:
    unique_ptr<GUIFactory> factory;
    unique_ptr<IButton> button;
    unique_ptr<ITextBox> textBox;
    
public:
    Application(unique_ptr<GUIFactory> f) : factory(move(f)) {
        button = factory->createButton();
        textBox = factory->createTextBox();
    }
    
    void renderUI() {
        textBox->setText("Hello World");
        textBox->render();
        button->render();
    }
    
    void handleClick() {
        button->onClick();
    }
};

int main() {
    cout << "=== Basic Abstract Factory ===" << endl;
    
    cout << "\n1. Windows Application:" << endl;
    Application winApp(make_unique<WindowsFactory>());
    winApp.renderUI();
    winApp.handleClick();
    
    cout << "\n2. Mac Application:" << endl;
    Application macApp(make_unique<MacFactory>());
    macApp.renderUI();
    macApp.handleClick();
    
    return 0;
}
```

**Output:**
```
=== Basic Abstract Factory ===

1. Windows Application:
Rendering Windows text box: Hello World
Rendering Windows button
Windows button clicked

2. Mac Application:
Rendering Mac text box: Hello World
Rendering Mac button
Mac button clicked
```

---

## 2. **Abstract Factory with Multiple Product Families**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <vector>
using namespace std;

// Abstract Products
class IChair {
public:
    virtual void sit() = 0;
    virtual string getStyle() const = 0;
    virtual ~IChair() = default;
};

class ISofa {
public:
    virtual void lie() = 0;
    virtual string getStyle() const = 0;
    virtual ~ISofa() = default;
};

class ICoffeeTable {
public:
    virtual void place() = 0;
    virtual string getStyle() const = 0;
    virtual ~ICoffeeTable() = default;
};

// Victorian Family
class VictorianChair : public IChair {
public:
    void sit() override {
        cout << "Sitting on Victorian chair" << endl;
    }
    
    string getStyle() const override {
        return "Victorian";
    }
};

class VictorianSofa : public ISofa {
public:
    void lie() override {
        cout << "Lying on Victorian sofa" << endl;
    }
    
    string getStyle() const override {
        return "Victorian";
    }
};

class VictorianCoffeeTable : public ICoffeeTable {
public:
    void place() override {
        cout << "Placing items on Victorian coffee table" << endl;
    }
    
    string getStyle() const override {
        return "Victorian";
    }
};

// Modern Family
class ModernChair : public IChair {
public:
    void sit() override {
        cout << "Sitting on modern chair" << endl;
    }
    
    string getStyle() const override {
        return "Modern";
    }
};

class ModernSofa : public ISofa {
public:
    void lie() override {
        cout << "Lying on modern sofa" << endl;
    }
    
    string getStyle() const override {
        return "Modern";
    }
};

class ModernCoffeeTable : public ICoffeeTable {
public:
    void place() override {
        cout << "Placing items on modern coffee table" << endl;
    }
    
    string getStyle() const override {
        return "Modern";
    }
};

// Abstract Factory
class FurnitureFactory {
public:
    virtual unique_ptr<IChair> createChair() = 0;
    virtual unique_ptr<ISofa> createSofa() = 0;
    virtual unique_ptr<ICoffeeTable> createCoffeeTable() = 0;
    virtual ~FurnitureFactory() = default;
};

// Victorian Factory
class VictorianFactory : public FurnitureFactory {
public:
    unique_ptr<IChair> createChair() override {
        return make_unique<VictorianChair>();
    }
    
    unique_ptr<ISofa> createSofa() override {
        return make_unique<VictorianSofa>();
    }
    
    unique_ptr<ICoffeeTable> createCoffeeTable() override {
        return make_unique<VictorianCoffeeTable>();
    }
};

// Modern Factory
class ModernFactory : public FurnitureFactory {
public:
    unique_ptr<IChair> createChair() override {
        return make_unique<ModernChair>();
    }
    
    unique_ptr<ISofa> createSofa() override {
        return make_unique<ModernSofa>();
    }
    
    unique_ptr<ICoffeeTable> createCoffeeTable() override {
        return make_unique<ModernCoffeeTable>();
    }
};

class FurnitureStore {
private:
    unique_ptr<FurnitureFactory> factory;
    
public:
    FurnitureStore(unique_ptr<FurnitureFactory> f) : factory(move(f)) {}
    
    void setupRoom() {
        auto chair = factory->createChair();
        auto sofa = factory->createSofa();
        auto table = factory->createCoffeeTable();
        
        cout << "\nFurniture style: " << chair->getStyle() << endl;
        chair->sit();
        sofa->lie();
        table->place();
    }
};

int main() {
    cout << "=== Abstract Factory with Multiple Product Families ===" << endl;
    
    FurnitureStore victorianStore(make_unique<VictorianFactory>());
    victorianStore.setupRoom();
    
    FurnitureStore modernStore(make_unique<ModernFactory>());
    modernStore.setupRoom();
    
    return 0;
}
```

---

## 3. **Abstract Factory with Configuration**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <map>
#include <functional>
using namespace std;

// Abstract Products
class IDatabaseConnection {
public:
    virtual void connect() = 0;
    virtual void disconnect() = 0;
    virtual void query(const string& sql) = 0;
    virtual ~IDatabaseConnection() = default;
};

class IDataReader {
public:
    virtual void read() = 0;
    virtual void parse() = 0;
    virtual ~IDataReader() = default;
};

// MySQL Products
class MySQLConnection : public IDatabaseConnection {
public:
    void connect() override {
        cout << "MySQL: Connection established" << endl;
    }
    
    void disconnect() override {
        cout << "MySQL: Connection closed" << endl;
    }
    
    void query(const string& sql) override {
        cout << "MySQL: Executing: " << sql << endl;
    }
};

class MySQLDataReader : public IDataReader {
public:
    void read() override {
        cout << "MySQL: Reading data" << endl;
    }
    
    void parse() override {
        cout << "MySQL: Parsing data" << endl;
    }
};

// PostgreSQL Products
class PostgreSQLConnection : public IDatabaseConnection {
public:
    void connect() override {
        cout << "PostgreSQL: Connection established" << endl;
    }
    
    void disconnect() override {
        cout << "PostgreSQL: Connection closed" << endl;
    }
    
    void query(const string& sql) override {
        cout << "PostgreSQL: Executing: " << sql << endl;
    }
};

class PostgreSQLDataReader : public IDataReader {
public:
    void read() override {
        cout << "PostgreSQL: Reading data" << endl;
    }
    
    void parse() override {
        cout << "PostgreSQL: Parsing data" << endl;
    }
};

// SQLite Products
class SQLiteConnection : public IDatabaseConnection {
public:
    void connect() override {
        cout << "SQLite: Connection established" << endl;
    }
    
    void disconnect() override {
        cout << "SQLite: Connection closed" << endl;
    }
    
    void query(const string& sql) override {
        cout << "SQLite: Executing: " << sql << endl;
    }
};

class SQLiteDataReader : public IDataReader {
public:
    void read() override {
        cout << "SQLite: Reading data" << endl;
    }
    
    void parse() override {
        cout << "SQLite: Parsing data" << endl;
    }
};

// Abstract Factory
class DatabaseFactory {
public:
    virtual unique_ptr<IDatabaseConnection> createConnection() = 0;
    virtual unique_ptr<IDataReader> createDataReader() = 0;
    virtual ~DatabaseFactory() = default;
};

// Concrete Factories
class MySQLFactory : public DatabaseFactory {
public:
    unique_ptr<IDatabaseConnection> createConnection() override {
        return make_unique<MySQLConnection>();
    }
    
    unique_ptr<IDataReader> createDataReader() override {
        return make_unique<MySQLDataReader>();
    }
};

class PostgreSQLFactory : public DatabaseFactory {
public:
    unique_ptr<IDatabaseConnection> createConnection() override {
        return make_unique<PostgreSQLConnection>();
    }
    
    unique_ptr<IDataReader> createDataReader() override {
        return make_unique<PostgreSQLDataReader>();
    }
};

class SQLiteFactory : public DatabaseFactory {
public:
    unique_ptr<IDatabaseConnection> createConnection() override {
        return make_unique<SQLiteConnection>();
    }
    
    unique_ptr<IDataReader> createDataReader() override {
        return make_unique<SQLiteDataReader>();
    }
};

// Factory with configuration
class DatabaseFactoryProvider {
private:
    map<string, function<unique_ptr<DatabaseFactory>()>> factories;
    
public:
    DatabaseFactoryProvider() {
        factories["mysql"] = []() { return make_unique<MySQLFactory>(); };
        factories["postgresql"] = []() { return make_unique<PostgreSQLFactory>(); };
        factories["sqlite"] = []() { return make_unique<SQLiteFactory>(); };
    }
    
    unique_ptr<DatabaseFactory> getFactory(const string& type) {
        auto it = factories.find(type);
        if (it != factories.end()) {
            return it->second();
        }
        return nullptr;
    }
};

class DataAccessLayer {
private:
    unique_ptr<DatabaseFactory> factory;
    unique_ptr<IDatabaseConnection> connection;
    unique_ptr<IDataReader> reader;
    
public:
    DataAccessLayer(const string& dbType) {
        DatabaseFactoryProvider provider;
        factory = provider.getFactory(dbType);
        if (factory) {
            connection = factory->createConnection();
            reader = factory->createDataReader();
        }
    }
    
    void execute(const string& sql) {
        if (connection && reader) {
            connection->connect();
            connection->query(sql);
            reader->read();
            reader->parse();
            connection->disconnect();
        }
    }
};

int main() {
    cout << "=== Abstract Factory with Configuration ===" << endl;
    
    cout << "\n1. MySQL Database:" << endl;
    DataAccessLayer mysql("mysql");
    mysql.execute("SELECT * FROM users");
    
    cout << "\n2. PostgreSQL Database:" << endl;
    DataAccessLayer postgresql("postgresql");
    postgresql.execute("SELECT * FROM products");
    
    cout << "\n3. SQLite Database:" << endl;
    DataAccessLayer sqlite("sqlite");
    sqlite.execute("SELECT * FROM logs");
    
    return 0;
}
```

---

## 4. **Abstract Factory with Singleton**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

// Abstract Products
class ITheme {
public:
    virtual void apply() = 0;
    virtual string getName() const = 0;
    virtual ~ITheme() = default;
};

class IWidget {
public:
    virtual void render() = 0;
    virtual ~IWidget() = default;
};

// Light Theme Products
class LightTheme : public ITheme {
public:
    void apply() override {
        cout << "Applying light theme" << endl;
    }
    
    string getName() const override {
        return "Light";
    }
};

class LightButton : public IWidget {
public:
    void render() override {
        cout << "Rendering light button" << endl;
    }
};

class LightPanel : public IWidget {
public:
    void render() override {
        cout << "Rendering light panel" << endl;
    }
};

// Dark Theme Products
class DarkTheme : public ITheme {
public:
    void apply() override {
        cout << "Applying dark theme" << endl;
    }
    
    string getName() const override {
        return "Dark";
    }
};

class DarkButton : public IWidget {
public:
    void render() override {
        cout << "Rendering dark button" << endl;
    }
};

class DarkPanel : public IWidget {
public:
    void render() override {
        cout << "Rendering dark panel" << endl;
    }
};

// Abstract Factory with Singleton
class UIFactory {
private:
    static unique_ptr<UIFactory> instance;
    string currentTheme;
    
    UIFactory() : currentTheme("light") {}
    
public:
    static UIFactory& getInstance() {
        if (!instance) {
            instance.reset(new UIFactory());
        }
        return *instance;
    }
    
    void setTheme(const string& theme) {
        currentTheme = theme;
        cout << "Theme changed to: " << theme << endl;
    }
    
    unique_ptr<ITheme> createTheme() {
        if (currentTheme == "light") {
            return make_unique<LightTheme>();
        } else {
            return make_unique<DarkTheme>();
        }
    }
    
    unique_ptr<IWidget> createButton() {
        if (currentTheme == "light") {
            return make_unique<LightButton>();
        } else {
            return make_unique<DarkButton>();
        }
    }
    
    unique_ptr<IWidget> createPanel() {
        if (currentTheme == "light") {
            return make_unique<LightPanel>();
        } else {
            return make_unique<DarkPanel>();
        }
    }
    
    // Prevent copying
    UIFactory(const UIFactory&) = delete;
    UIFactory& operator=(const UIFactory&) = delete;
};

unique_ptr<UIFactory> UIFactory::instance;

class Application {
public:
    void renderUI() {
        auto& factory = UIFactory::getInstance();
        
        auto theme = factory.createTheme();
        auto button = factory.createButton();
        auto panel = factory.createPanel();
        
        theme->apply();
        button->render();
        panel->render();
    }
};

int main() {
    cout << "=== Abstract Factory with Singleton ===" << endl;
    
    Application app;
    
    cout << "\n1. Light theme:" << endl;
    UIFactory::getInstance().setTheme("light");
    app.renderUI();
    
    cout << "\n2. Dark theme:" << endl;
    UIFactory::getInstance().setTheme("dark");
    app.renderUI();
    
    return 0;
}
```

---

## 5. **Practical Example: Cross-Platform Game Engine**

```cpp
#include <iostream>
#include <string>
#include <memory>
#include <map>
using namespace std;

// Abstract Products
class ITexture {
public:
    virtual void load(const string& path) = 0;
    virtual void bind() = 0;
    virtual ~ITexture() = default;
};

class IShader {
public:
    virtual void compile(const string& source) = 0;
    virtual void use() = 0;
    virtual ~IShader() = default;
};

class IRenderer {
public:
    virtual void clear() = 0;
    virtual void draw() = 0;
    virtual void present() = 0;
    virtual ~IRenderer() = default;
};

// OpenGL Products
class OpenGLTexture : public ITexture {
public:
    void load(const string& path) override {
        cout << "OpenGL: Loading texture from " << path << endl;
    }
    
    void bind() override {
        cout << "OpenGL: Binding texture" << endl;
    }
};

class OpenGLShader : public IShader {
public:
    void compile(const string& source) override {
        cout << "OpenGL: Compiling shader: " << source << endl;
    }
    
    void use() override {
        cout << "OpenGL: Using shader program" << endl;
    }
};

class OpenGLRenderer : public IRenderer {
public:
    void clear() override {
        cout << "OpenGL: Clearing screen" << endl;
    }
    
    void draw() override {
        cout << "OpenGL: Drawing primitives" << endl;
    }
    
    void present() override {
        cout << "OpenGL: Presenting frame" << endl;
    }
};

// DirectX Products
class DirectXTexture : public ITexture {
public:
    void load(const string& path) override {
        cout << "DirectX: Loading texture from " << path << endl;
    }
    
    void bind() override {
        cout << "DirectX: Binding texture" << endl;
    }
};

class DirectXShader : public IShader {
public:
    void compile(const string& source) override {
        cout << "DirectX: Compiling shader: " << source << endl;
    }
    
    void use() override {
        cout << "DirectX: Using shader program" << endl;
    }
};

class DirectXRenderer : public IRenderer {
public:
    void clear() override {
        cout << "DirectX: Clearing screen" << endl;
    }
    
    void draw() override {
        cout << "DirectX: Drawing primitives" << endl;
    }
    
    void present() override {
        cout << "DirectX: Presenting frame" << endl;
    }
};

// Abstract Factory
class GraphicsFactory {
public:
    virtual unique_ptr<ITexture> createTexture() = 0;
    virtual unique_ptr<IShader> createShader() = 0;
    virtual unique_ptr<IRenderer> createRenderer() = 0;
    virtual ~GraphicsFactory() = default;
};

// OpenGL Factory
class OpenGLFactory : public GraphicsFactory {
public:
    unique_ptr<ITexture> createTexture() override {
        return make_unique<OpenGLTexture>();
    }
    
    unique_ptr<IShader> createShader() override {
        return make_unique<OpenGLShader>();
    }
    
    unique_ptr<IRenderer> createRenderer() override {
        return make_unique<OpenGLRenderer>();
    }
};

// DirectX Factory
class DirectXFactory : public GraphicsFactory {
public:
    unique_ptr<ITexture> createTexture() override {
        return make_unique<DirectXTexture>();
    }
    
    unique_ptr<IShader> createShader() override {
        return make_unique<DirectXShader>();
    }
    
    unique_ptr<IRenderer> createRenderer() override {
        return make_unique<DirectXRenderer>();
    }
};

class GameEngine {
private:
    unique_ptr<GraphicsFactory> factory;
    unique_ptr<ITexture> texture;
    unique_ptr<IShader> shader;
    unique_ptr<IRenderer> renderer;
    
public:
    GameEngine(unique_ptr<GraphicsFactory> f) : factory(move(f)) {
        texture = factory->createTexture();
        shader = factory->createShader();
        renderer = factory->createRenderer();
    }
    
    void initialize(const string& texturePath, const string& shaderSource) {
        texture->load(texturePath);
        shader->compile(shaderSource);
        cout << "Game engine initialized" << endl;
    }
    
    void render() {
        renderer->clear();
        shader->use();
        texture->bind();
        renderer->draw();
        renderer->present();
    }
};

int main() {
    cout << "=== Cross-Platform Game Engine ===" << endl;
    
    cout << "\n1. OpenGL Version:" << endl;
    GameEngine openglEngine(make_unique<OpenGLFactory>());
    openglEngine.initialize("texture.png", "vertex_shader.glsl");
    openglEngine.render();
    
    cout << "\n2. DirectX Version:" << endl;
    GameEngine directxEngine(make_unique<DirectXFactory>());
    directxEngine.initialize("texture.dds", "vertex_shader.hlsl");
    directxEngine.render();
    
    return 0;
}
```

---

## 📊 Abstract Factory Summary

| Component | Description |
|-----------|-------------|
| **Abstract Factory** | Declares interfaces for creating products |
| **Concrete Factory** | Implements creation for a specific family |
| **Abstract Product** | Declares interface for a type of product |
| **Concrete Product** | Implements product for a specific family |

---

## ✅ Best Practices

1. **Use when** families of related objects need to be created
2. **Encapsulate** product creation in factory classes
3. **Keep factory interface** stable while products can vary
4. **Use with singleton** for global factory access
5. **Consider dependency injection** for flexibility

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Too many products** | Complex factory | Consider composition |
| **Rigid interface** | Hard to extend | Use parameterized factories |
| **Factory explosion** | Too many factories | Use registry pattern |

---

## ✅ Key Takeaways

1. **Abstract Factory** creates families of related objects
2. **Encapsulates** product creation logic
3. **Promotes consistency** across products in a family
4. **Supports Open/Closed Principle** - easy to add new families
5. **Useful for** cross-platform development
6. **Combines well** with Singleton and Factory Method

---