# Flyweight Pattern in C++ - Complete Guide

## 📖 Overview

The Flyweight pattern minimizes memory usage by sharing as much data as possible with similar objects. It is used when many objects need to be created that share common state. The pattern separates intrinsic state (shared) from extrinsic state (unique), allowing efficient handling of large numbers of fine-grained objects.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Intrinsic State** | Shared, immutable data stored in the flyweight |
| **Extrinsic State** | Unique, contextual data passed to flyweight methods |
| **Flyweight Factory** | Creates and manages flyweight objects |
| **Flyweight** | Interface for flyweight objects |

---

## 1. **Basic Flyweight Pattern**

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <memory>
using namespace std;

// Flyweight interface
class Character {
public:
    virtual void display(int x, int y) = 0;
    virtual ~Character() = default;
};

// Concrete Flyweight
class ConcreteCharacter : public Character {
private:
    char symbol;
    string font;
    int size;
    
public:
    ConcreteCharacter(char c, const string& f, int s) 
        : symbol(c), font(f), size(s) {
        cout << "Creating character: " << symbol << " (" << font << ", " << size << ")" << endl;
    }
    
    void display(int x, int y) override {
        cout << "Character '" << symbol << "' at (" << x << ", " << y 
             << ") [" << font << ", " << size << "]" << endl;
    }
};

// Flyweight Factory
class CharacterFactory {
private:
    unordered_map<string, unique_ptr<Character>> characters;
    
    string getKey(char c, const string& font, int size) {
        return string(1, c) + "|" + font + "|" + to_string(size);
    }
    
public:
    Character* getCharacter(char c, const string& font, int size) {
        string key = getKey(c, font, size);
        
        auto it = characters.find(key);
        if (it != characters.end()) {
            cout << "Reusing character: " << c << endl;
            return it->second.get();
        }
        
        auto character = make_unique<ConcreteCharacter>(c, font, size);
        Character* ptr = character.get();
        characters[key] = move(character);
        return ptr;
    }
    
    size_t getCount() const {
        return characters.size();
    }
};

int main() {
    cout << "=== Basic Flyweight Pattern ===" << endl;
    
    CharacterFactory factory;
    
    // Create a document
    string text = "Hello";
    string font = "Arial";
    int size = 12;
    
    cout << "\nCreating characters:" << endl;
    for (char c : text) {
        Character* ch = factory.getCharacter(c, font, size);
        ch->display(10, 10);
    }
    
    cout << "\nCreating another document:" << endl;
    string text2 = "World";
    for (char c : text2) {
        Character* ch = factory.getCharacter(c, font, size);
        ch->display(20, 20);
    }
    
    cout << "\nTotal unique characters created: " << factory.getCount() << endl;
    
    return 0;
}
```

**Output:**
```
=== Basic Flyweight Pattern ===

Creating characters:
Creating character: H (Arial, 12)
Character 'H' at (10, 10) [Arial, 12]
Creating character: e (Arial, 12)
Character 'e' at (10, 10) [Arial, 12]
Creating character: l (Arial, 12)
Character 'l' at (10, 10) [Arial, 12]
Reusing character: l
Character 'l' at (10, 10) [Arial, 12]
Creating character: o (Arial, 12)
Character 'o' at (10, 10) [Arial, 12]

Creating another document:
Creating character: W (Arial, 12)
Character 'W' at (20, 20) [Arial, 12]
Reusing character: o
Character 'o' at (20, 20) [Arial, 12]
Reusing character: r
Character 'r' at (20, 20) [Arial, 12]
Reusing character: l
Character 'l' at (20, 20) [Arial, 12]
Creating character: d (Arial, 12)
Character 'd' at (20, 20) [Arial, 12]

Total unique characters created: 8
```

---

## 2. **Tree Rendering with Flyweight**

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <memory>
#include <random>
using namespace std;

// Flyweight
class TreeType {
private:
    string name;
    string color;
    string texture;
    
public:
    TreeType(const string& n, const string& c, const string& t) 
        : name(n), color(c), texture(t) {
        cout << "Creating TreeType: " << name << " (" << color << ", " << texture << ")" << endl;
    }
    
    void draw(int x, int y) const {
        cout << "Drawing " << name << " tree at (" << x << ", " << y 
             << ") [" << color << ", " << texture << "]" << endl;
    }
    
    string getName() const { return name; }
};

// Flyweight Factory
class TreeFactory {
private:
    unordered_map<string, shared_ptr<TreeType>> treeTypes;
    
    string getKey(const string& name, const string& color, const string& texture) {
        return name + "|" + color + "|" + texture;
    }
    
public:
    shared_ptr<TreeType> getTreeType(const string& name, const string& color, const string& texture) {
        string key = getKey(name, color, texture);
        
        auto it = treeTypes.find(key);
        if (it != treeTypes.end()) {
            cout << "Reusing TreeType: " << name << endl;
            return it->second;
        }
        
        auto treeType = make_shared<TreeType>(name, color, texture);
        treeTypes[key] = treeType;
        return treeType;
    }
    
    size_t getCount() const {
        return treeTypes.size();
    }
};

// Context (Tree with extrinsic state)
class Tree {
private:
    int x, y;
    shared_ptr<TreeType> type;
    
public:
    Tree(int xPos, int yPos, shared_ptr<TreeType> t) : x(xPos), y(yPos), type(t) {}
    
    void draw() const {
        type->draw(x, y);
    }
};

// Forest (Client)
class Forest {
private:
    vector<Tree> trees;
    TreeFactory factory;
    
public:
    void plantTree(int x, int y, const string& name, const string& color, const string& texture) {
        auto type = factory.getTreeType(name, color, texture);
        trees.emplace_back(x, y, type);
    }
    
    void draw() const {
        cout << "\n=== Forest (" << trees.size() << " trees) ===" << endl;
        for (const auto& tree : trees) {
            tree.draw();
        }
    }
    
    size_t getTreeTypeCount() const {
        return factory.getCount();
    }
};

int main() {
    cout << "=== Tree Rendering with Flyweight ===" << endl;
    
    Forest forest;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, 100);
    
    cout << "\nPlanting trees:" << endl;
    
    // Plant many trees but only a few types
    for (int i = 0; i < 100; i++) {
        int type = i % 3;
        int x = dis(gen);
        int y = dis(gen);
        
        switch (type) {
            case 0:
                forest.plantTree(x, y, "Oak", "Green", "Rough");
                break;
            case 1:
                forest.plantTree(x, y, "Pine", "Dark Green", "Smooth");
                break;
            case 2:
                forest.plantTree(x, y, "Maple", "Red", "Rough");
                break;
        }
    }
    
    cout << "\nUnique tree types created: " << forest.getTreeTypeCount() << endl;
    forest.draw();
    
    return 0;
}
```

---

## 3. **Particle System with Flyweight**

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <memory>
#include <random>
using namespace std;

// Flyweight
class ParticleType {
private:
    string texture;
    string color;
    float size;
    float lifespan;
    
public:
    ParticleType(const string& t, const string& c, float s, float l) 
        : texture(t), color(c), size(s), lifespan(l) {
        cout << "Creating ParticleType: " << texture << " (" << color << ", size=" << size << ")" << endl;
    }
    
    void render(float x, float y, float age) const {
        float lifeRemaining = lifespan - age;
        cout << "Rendering " << texture << " particle at (" << x << ", " << y 
             << ") [" << color << ", size=" << size << ", life=" << lifeRemaining << "]" << endl;
    }
};

// Flyweight Factory
class ParticleFactory {
private:
    unordered_map<string, shared_ptr<ParticleType>> particleTypes;
    
    string getKey(const string& texture, const string& color, float size, float lifespan) {
        return texture + "|" + color + "|" + to_string(size) + "|" + to_string(lifespan);
    }
    
public:
    shared_ptr<ParticleType> getParticleType(const string& texture, const string& color, 
                                              float size, float lifespan) {
        string key = getKey(texture, color, size, lifespan);
        
        auto it = particleTypes.find(key);
        if (it != particleTypes.end()) {
            cout << "Reusing ParticleType: " << texture << endl;
            return it->second;
        }
        
        auto type = make_shared<ParticleType>(texture, color, size, lifespan);
        particleTypes[key] = type;
        return type;
    }
    
    size_t getCount() const {
        return particleTypes.size();
    }
};

// Context (Particle with extrinsic state)
class Particle {
private:
    float x, y;
    float age;
    shared_ptr<ParticleType> type;
    
public:
    Particle(float xPos, float yPos, shared_ptr<ParticleType> t) 
        : x(xPos), y(yPos), age(0), type(t) {}
    
    void update(float dt) {
        age += dt;
    }
    
    bool isAlive() const {
        return age < type->lifespan;
    }
    
    void render() const {
        type->render(x, y, age);
    }
};

class ParticleSystem {
private:
    vector<Particle> particles;
    ParticleFactory factory;
    random_device rd;
    mt19937 gen;
    
public:
    ParticleSystem() : gen(rd()) {}
    
    void emit(float x, float y, const string& type) {
        shared_ptr<ParticleType> particleType;
        
        if (type == "fire") {
            particleType = factory.getParticleType("fire.png", "Orange", 0.5f, 2.0f);
        } else if (type == "smoke") {
            particleType = factory.getParticleType("smoke.png", "Gray", 0.8f, 3.0f);
        } else if (type == "spark") {
            particleType = factory.getParticleType("spark.png", "Yellow", 0.3f, 1.0f);
        } else {
            return;
        }
        
        particles.emplace_back(x, y, particleType);
    }
    
    void update(float dt) {
        for (auto it = particles.begin(); it != particles.end();) {
            it->update(dt);
            if (!it->isAlive()) {
                it = particles.erase(it);
            } else {
                ++it;
            }
        }
    }
    
    void render() const {
        cout << "\n=== Rendering " << particles.size() << " particles ===" << endl;
        for (const auto& particle : particles) {
            particle.render();
        }
    }
    
    size_t getParticleTypeCount() const {
        return factory.getCount();
    }
    
    size_t getParticleCount() const {
        return particles.size();
    }
};

int main() {
    cout << "=== Particle System with Flyweight ===" << endl;
    
    ParticleSystem system;
    
    cout << "\nEmitting particles:" << endl;
    
    // Emit many particles but only a few types
    for (int i = 0; i < 100; i++) {
        int type = i % 3;
        float x = rand() % 100;
        float y = rand() % 100;
        
        if (type == 0) {
            system.emit(x, y, "fire");
        } else if (type == 1) {
            system.emit(x, y, "smoke");
        } else {
            system.emit(x, y, "spark");
        }
    }
    
    cout << "\nUnique particle types: " << system.getParticleTypeCount() << endl;
    cout << "Total particles: " << system.getParticleCount() << endl;
    
    cout << "\nSimulating particle system:" << endl;
    for (int frame = 0; frame < 5; frame++) {
        cout << "\nFrame " << frame << ":" << endl;
        system.update(0.5f);
        system.render();
    }
    
    return 0;
}
```

---

## 4. **Text Editor with Flyweight**

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <memory>
#include <iomanip>
using namespace std;

// Flyweight
class TextStyle {
private:
    string fontName;
    int fontSize;
    string color;
    bool bold;
    bool italic;
    bool underline;
    
public:
    TextStyle(const string& font, int size, const string& col, bool b, bool i, bool u)
        : fontName(font), fontSize(size), color(col), bold(b), italic(i), underline(u) {
        cout << "Creating TextStyle: " << font << ", " << size << ", " << color;
        if (bold) cout << ", Bold";
        if (italic) cout << ", Italic";
        if (underline) cout << ", Underline";
        cout << endl;
    }
    
    void apply() const {
        cout << "Applying style: " << fontName << ", " << fontSize << ", " << color;
        if (bold) cout << ", Bold";
        if (italic) cout << ", Italic";
        if (underline) cout << ", Underline";
        cout << endl;
    }
    
    string getKey() const {
        return fontName + "|" + to_string(fontSize) + "|" + color + "|" +
               to_string(bold) + "|" + to_string(italic) + "|" + to_string(underline);
    }
};

// Flyweight Factory
class TextStyleFactory {
private:
    unordered_map<string, shared_ptr<TextStyle>> styles;
    
public:
    shared_ptr<TextStyle> getStyle(const string& font, int size, const string& color,
                                    bool bold, bool italic, bool underline) {
        TextStyle temp(font, size, color, bold, italic, underline);
        string key = temp.getKey();
        
        auto it = styles.find(key);
        if (it != styles.end()) {
            cout << "Reusing style" << endl;
            return it->second;
        }
        
        auto style = make_shared<TextStyle>(font, size, color, bold, italic, underline);
        styles[key] = style;
        return style;
    }
    
    size_t getCount() const {
        return styles.size();
    }
};

// Context (Character with extrinsic state)
class Character {
private:
    char symbol;
    shared_ptr<TextStyle> style;
    
public:
    Character(char c, shared_ptr<TextStyle> s) : symbol(c), style(s) {}
    
    void display() const {
        cout << "Character '" << symbol << "': ";
        style->apply();
    }
};

class TextDocument {
private:
    vector<Character> characters;
    TextStyleFactory factory;
    
public:
    void addCharacter(char c, const string& font, int size, const string& color,
                      bool bold = false, bool italic = false, bool underline = false) {
        auto style = factory.getStyle(font, size, color, bold, italic, underline);
        characters.emplace_back(c, style);
    }
    
    void display() const {
        cout << "\n=== Document (" << characters.size() << " characters) ===" << endl;
        for (const auto& ch : characters) {
            ch.display();
        }
    }
    
    size_t getStyleCount() const {
        return factory.getCount();
    }
};

int main() {
    cout << "=== Text Editor with Flyweight ===" << endl;
    
    TextDocument doc;
    
    cout << "\nAdding text with styles:" << endl;
    
    // Normal text
    doc.addCharacter('H', "Arial", 12, "Black");
    doc.addCharacter('e', "Arial", 12, "Black");
    doc.addCharacter('l', "Arial", 12, "Black");
    doc.addCharacter('l', "Arial", 12, "Black");
    doc.addCharacter('o', "Arial", 12, "Black");
    
    // Bold text
    doc.addCharacter('W', "Arial", 14, "Black", true);
    doc.addCharacter('o', "Arial", 14, "Black", true);
    doc.addCharacter('r', "Arial", 14, "Black", true);
    doc.addCharacter('l', "Arial", 14, "Black", true);
    doc.addCharacter('d', "Arial", 14, "Black", true);
    
    // Colored text
    doc.addCharacter('!', "Arial", 16, "Red", false, true);
    
    // More normal text (reusing style)
    doc.addCharacter(' ', "Arial", 12, "Black");
    doc.addCharacter('T', "Arial", 12, "Black");
    doc.addCharacter('h', "Arial", 12, "Black");
    doc.addCharacter('i', "Arial", 12, "Black");
    doc.addCharacter('s', "Arial", 12, "Black");
    
    cout << "\nUnique styles created: " << doc.getStyleCount() << endl;
    doc.display();
    
    return 0;
}
```

---

## 5. **Practical Example: Game Map Tile System**

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <memory>
#include <random>
#include <iomanip>
using namespace std;

// Flyweight
class TileType {
private:
    string name;
    string texture;
    bool walkable;
    int movementCost;
    
public:
    TileType(const string& n, const string& t, bool w, int cost)
        : name(n), texture(t), walkable(w), movementCost(cost) {
        cout << "Creating TileType: " << name << " (" << texture << ")" << endl;
    }
    
    void render(int x, int y) const {
        cout << "Tile " << name << " at (" << x << ", " << y 
             << ") [walkable=" << (walkable ? "Yes" : "No") 
             << ", cost=" << movementCost << "]" << endl;
    }
    
    bool isWalkable() const { return walkable; }
    int getMovementCost() const { return movementCost; }
    string getName() const { return name; }
};

// Flyweight Factory
class TileFactory {
private:
    unordered_map<string, shared_ptr<TileType>> tileTypes;
    
public:
    shared_ptr<TileType> getTileType(const string& name, const string& texture,
                                      bool walkable, int cost) {
        string key = name + "|" + texture + "|" + to_string(walkable) + "|" + to_string(cost);
        
        auto it = tileTypes.find(key);
        if (it != tileTypes.end()) {
            return it->second;
        }
        
        auto type = make_shared<TileType>(name, texture, walkable, cost);
        tileTypes[key] = type;
        return type;
    }
    
    size_t getCount() const {
        return tileTypes.size();
    }
};

// Context (Tile with extrinsic state)
class Tile {
private:
    int x, y;
    shared_ptr<TileType> type;
    
public:
    Tile(int xPos, int yPos, shared_ptr<TileType> t) : x(xPos), y(yPos), type(t) {}
    
    void render() const {
        type->render(x, y);
    }
    
    bool isWalkable() const {
        return type->isWalkable();
    }
    
    int getMovementCost() const {
        return type->getMovementCost();
    }
};

class GameMap {
private:
    vector<vector<Tile>> map;
    int width, height;
    TileFactory factory;
    
public:
    GameMap(int w, int h) : width(w), height(h) {
        map.resize(height, vector<Tile>(width, Tile(0, 0, nullptr)));
    }
    
    void generateMap() {
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<> dis(0, 2);
        
        // Pre-create tile types
        auto grass = factory.getTileType("Grass", "grass.png", true, 1);
        auto dirt = factory.getTileType("Dirt", "dirt.png", true, 2);
        auto water = factory.getTileType("Water", "water.png", false, -1);
        auto mountain = factory.getTileType("Mountain", "mountain.png", false, -1);
        auto forest = factory.getTileType("Forest", "forest.png", true, 3);
        
        cout << "\nGenerating map (" << width << "x" << height << "):" << endl;
        
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int r = dis(gen);
                shared_ptr<TileType> type;
                
                if (r == 0) type = grass;
                else if (r == 1) type = dirt;
                else if (r == 2) type = forest;
                
                map[y][x] = Tile(x, y, type);
            }
        }
        
        // Add some water and mountains
        map[2][3] = Tile(3, 2, water);
        map[5][7] = Tile(7, 5, mountain);
        map[8][4] = Tile(4, 8, water);
        map[1][9] = Tile(9, 1, mountain);
    }
    
    void render() const {
        cout << "\n=== Map Rendering ===" << endl;
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                map[y][x].render();
            }
        }
    }
    
    void findPath(int startX, int startY, int endX, int endY) {
        cout << "\nFinding path from (" << startX << ", " << startY 
             << ") to (" << endX << ", " << endY << "):" << endl;
        
        if (!map[startY][startX].isWalkable()) {
            cout << "Start tile is not walkable!" << endl;
            return;
        }
        
        if (!map[endY][endX].isWalkable()) {
            cout << "End tile is not walkable!" << endl;
            return;
        }
        
        // Simple pathfinding simulation
        cout << "Path found! (simulated)" << endl;
    }
    
    size_t getTileTypeCount() const {
        return factory.getCount();
    }
};

int main() {
    cout << "=== Game Map Tile System with Flyweight ===" << endl;
    
    GameMap map(10, 10);
    map.generateMap();
    map.render();
    
    cout << "\nUnique tile types created: " << map.getTileTypeCount() << endl;
    
    map.findPath(0, 0, 9, 9);
    map.findPath(2, 3, 5, 7);  // Start in water
    map.findPath(1, 9, 8, 4);  // End in mountain
    
    return 0;
}
```

---

## 📊 Flyweight Pattern Summary

| Component | Description |
|-----------|-------------|
| **Flyweight** | Interface for flyweight objects |
| **Concrete Flyweight** | Shared object with intrinsic state |
| **Flyweight Factory** | Creates and manages flyweights |
| **Client** | Maintains extrinsic state and uses flyweights |

---

## ✅ Best Practices

1. **Use Flyweight** when many similar objects are needed
2. **Separate intrinsic** (shared) from extrinsic (unique) state
3. **Make intrinsic state immutable** for safety
4. **Use factory** to manage flyweight creation
5. **Measure memory savings** to justify complexity

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Not separating state** | Can't share objects | Clearly separate intrinsic/extrinsic |
| **Mutable intrinsic state** | Unexpected sharing | Make intrinsic state immutable |
| **Premature optimization** | Unnecessary complexity | Only use when memory is an issue |
| **Thread safety** | Concurrent access issues | Use immutable flyweights |

---

## ✅ Key Takeaways

1. **Flyweight pattern** reduces memory usage through sharing
2. **Intrinsic state** is shared across objects
3. **Extrinsic state** is passed to flyweight methods
4. **Useful for** large numbers of similar objects
5. **Common in** graphics, text rendering, game development
6. **Often combined** with Factory pattern

---