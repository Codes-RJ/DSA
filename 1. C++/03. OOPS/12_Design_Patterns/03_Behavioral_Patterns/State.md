# 12_Design_Patterns/03_Behavioral_Patterns/State.md

# State Pattern in C++ - Complete Guide

## 📖 Overview

The State pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class. This pattern is particularly useful when an object has many states with different behaviors, and the state transitions are complex.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Context** | Maintains an instance of a ConcreteState |
| **State** | Interface for encapsulating behavior associated with a state |
| **Concrete State** | Implements behavior associated with a state |
| **State Transition** | Changing from one state to another |

---

## 1. **Basic State Pattern**

```cpp
#include <iostream>
#include <string>
using namespace std;

// Forward declaration
class Context;

// State interface
class State {
public:
    virtual void handle(Context& context) = 0;
    virtual string getName() const = 0;
    virtual ~State() = default;
};

// Context
class Context {
private:
    State* currentState;
    
public:
    Context(State* initialState) : currentState(initialState) {}
    
    void setState(State* state) {
        currentState = state;
        cout << "Context: State changed to " << currentState->getName() << endl;
    }
    
    void request() {
        currentState->handle(*this);
    }
    
    State* getState() const { return currentState; }
};

// Concrete State A
class StateA : public State {
public:
    void handle(Context& context) override {
        cout << "StateA: Handling request" << endl;
        context.setState(new StateB());
    }
    
    string getName() const override { return "StateA"; }
};

// Concrete State B
class StateB : public State {
public:
    void handle(Context& context) override {
        cout << "StateB: Handling request" << endl;
        context.setState(new StateC());
    }
    
    string getName() const override { return "StateB"; }
};

// Concrete State C
class StateC : public State {
public:
    void handle(Context& context) override {
        cout << "StateC: Handling request" << endl;
        context.setState(new StateA());
    }
    
    string getName() const override { return "StateC"; }
};

int main() {
    cout << "=== Basic State Pattern ===" << endl;
    
    Context context(new StateA());
    
    for (int i = 0; i < 6; i++) {
        cout << "\nRequest " << i + 1 << ":" << endl;
        context.request();
    }
    
    return 0;
}
```

**Output:**
```
=== Basic State Pattern ===

Request 1:
StateA: Handling request
Context: State changed to StateB

Request 2:
StateB: Handling request
Context: State changed to StateC

Request 3:
StateC: Handling request
Context: State changed to StateA

Request 4:
StateA: Handling request
Context: State changed to StateB

Request 5:
StateB: Handling request
Context: State changed to StateC

Request 6:
StateC: Handling request
Context: State changed to StateA
```

---

## 2. **Traffic Light Example**

```cpp
#include <iostream>
#include <string>
#include <thread>
#include <chrono>
using namespace std;

class TrafficLight;

// State interface
class LightState {
public:
    virtual void change(TrafficLight& light) = 0;
    virtual void display() const = 0;
    virtual string getName() const = 0;
    virtual ~LightState() = default;
};

// Context
class TrafficLight {
private:
    LightState* currentState;
    
public:
    TrafficLight(LightState* initialState) : currentState(initialState) {}
    
    void setState(LightState* state) {
        currentState = state;
        cout << "Light changed to " << currentState->getName() << endl;
    }
    
    void change() {
        currentState->change(*this);
    }
    
    void display() const {
        currentState->display();
    }
};

// Concrete State: Red
class RedState : public LightState {
public:
    void change(TrafficLight& light) override;
    void display() const override {
        cout << "🔴 RED - STOP" << endl;
    }
    
    string getName() const override { return "RED"; }
};

// Concrete State: Yellow
class YellowState : public LightState {
public:
    void change(TrafficLight& light) override;
    void display() const override {
        cout << "🟡 YELLOW - CAUTION" << endl;
    }
    
    string getName() const override { return "YELLOW"; }
};

// Concrete State: Green
class GreenState : public LightState {
public:
    void change(TrafficLight& light) override;
    void display() const override {
        cout << "🟢 GREEN - GO" << endl;
    }
    
    string getName() const override { return "GREEN"; }
};

// Implementations to avoid circular dependency
void RedState::change(TrafficLight& light) {
    light.setState(new YellowState());
}

void YellowState::change(TrafficLight& light) {
    light.setState(new GreenState());
}

void GreenState::change(TrafficLight& light) {
    light.setState(new RedState());
}

int main() {
    cout << "=== Traffic Light Example ===" << endl;
    
    TrafficLight light(new RedState());
    
    for (int i = 0; i < 6; i++) {
        cout << "\nState " << i + 1 << ":" << endl;
        light.display();
        this_thread::sleep_for(chrono::seconds(1));
        light.change();
    }
    
    return 0;
}
```

---

## 3. **Document State Example**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

class Document;

// State interface
class DocumentState {
public:
    virtual void edit(Document& doc, const string& text) = 0;
    virtual void save(Document& doc) = 0;
    virtual void submit(Document& doc) = 0;
    virtual void approve(Document& doc) = 0;
    virtual void reject(Document& doc) = 0;
    virtual string getName() const = 0;
    virtual ~DocumentState() = default;
};

// Context
class Document {
private:
    string content;
    string author;
    DocumentState* state;
    
public:
    Document(const string& auth) : author(auth), state(nullptr) {}
    
    void setState(DocumentState* newState) {
        state = newState;
        cout << "Document state changed to: " << state->getName() << endl;
    }
    
    void edit(const string& text) {
        if (state) state->edit(*this, text);
        else cout << "No state set!" << endl;
    }
    
    void save() {
        if (state) state->save(*this);
        else cout << "No state set!" << endl;
    }
    
    void submit() {
        if (state) state->submit(*this);
        else cout << "No state set!" << endl;
    }
    
    void approve() {
        if (state) state->approve(*this);
        else cout << "No state set!" << endl;
    }
    
    void reject() {
        if (state) state->reject(*this);
        else cout << "No state set!" << endl;
    }
    
    void setContent(const string& text) { content = text; }
    string getContent() const { return content; }
    string getAuthor() const { return author; }
    DocumentState* getState() const { return state; }
};

// Concrete State: Draft
class DraftState : public DocumentState {
public:
    void edit(Document& doc, const string& text) override {
        doc.setContent(text);
        cout << "Document content updated: " << text << endl;
    }
    
    void save(Document& doc) override {
        cout << "Document saved as draft" << endl;
    }
    
    void submit(Document& doc) override;
    
    void approve(Document& doc) override {
        cout << "Cannot approve: Document is in draft state" << endl;
    }
    
    void reject(Document& doc) override {
        cout << "Cannot reject: Document is in draft state" << endl;
    }
    
    string getName() const override { return "Draft"; }
};

// Concrete State: Submitted
class SubmittedState : public DocumentState {
public:
    void edit(Document& doc, const string& text) override {
        cout << "Cannot edit: Document has been submitted" << endl;
    }
    
    void save(Document& doc) override {
        cout << "Cannot save: Document has been submitted" << endl;
    }
    
    void submit(Document& doc) override {
        cout << "Document already submitted" << endl;
    }
    
    void approve(Document& doc) override;
    
    void reject(Document& doc) override;
    
    string getName() const override { return "Submitted"; }
};

// Concrete State: Approved
class ApprovedState : public DocumentState {
public:
    void edit(Document& doc, const string& text) override {
        cout << "Cannot edit: Document is approved" << endl;
    }
    
    void save(Document& doc) override {
        cout << "Document saved as approved version" << endl;
    }
    
    void submit(Document& doc) override {
        cout << "Document already approved" << endl;
    }
    
    void approve(Document& doc) override {
        cout << "Document already approved" << endl;
    }
    
    void reject(Document& doc) override {
        cout << "Cannot reject approved document" << endl;
    }
    
    string getName() const override { return "Approved"; }
};

// Concrete State: Rejected
class RejectedState : public DocumentState {
public:
    void edit(Document& doc, const string& text) override {
        doc.setContent(text);
        cout << "Document content updated after rejection: " << text << endl;
        doc.setState(new DraftState());
    }
    
    void save(Document& doc) override {
        cout << "Cannot save rejected document" << endl;
    }
    
    void submit(Document& doc) override {
        cout << "Cannot submit rejected document. Please edit first." << endl;
    }
    
    void approve(Document& doc) override {
        cout << "Cannot approve rejected document" << endl;
    }
    
    void reject(Document& doc) override {
        cout << "Document already rejected" << endl;
    }
    
    string getName() const override { return "Rejected"; }
};

// Implementations to avoid circular dependency
void DraftState::submit(Document& doc) {
    doc.setState(new SubmittedState());
    cout << "Document submitted for review" << endl;
}

void SubmittedState::approve(Document& doc) {
    doc.setState(new ApprovedState());
    cout << "Document approved" << endl;
}

void SubmittedState::reject(Document& doc) {
    doc.setState(new RejectedState());
    cout << "Document rejected. Please revise." << endl;
}

int main() {
    cout << "=== Document State Example ===" << endl;
    
    Document doc("John Doe");
    doc.setState(new DraftState());
    
    cout << "\n1. Editing and saving draft:" << endl;
    doc.edit("Initial content");
    doc.save();
    
    cout << "\n2. Submitting document:" << endl;
    doc.submit();
    
    cout << "\n3. Trying to edit submitted document:" << endl;
    doc.edit("New content");
    
    cout << "\n4. Rejecting document:" << endl;
    doc.reject();
    
    cout << "\n5. Editing rejected document:" << endl;
    doc.edit("Revised content after rejection");
    
    cout << "\n6. Submitting revised document:" << endl;
    doc.submit();
    
    cout << "\n7. Approving document:" << endl;
    doc.approve();
    
    cout << "\n8. Trying to edit approved document:" << endl;
    doc.edit("Final content");
    
    return 0;
}
```

---

## 4. **Player State Example (Game Character)**

```cpp
#include <iostream>
#include <string>
#include <memory>
using namespace std;

class Player;

// State interface
class PlayerState {
public:
    virtual void move(Player& player) = 0;
    virtual void attack(Player& player) = 0;
    virtual void takeDamage(Player& player, int damage) = 0;
    virtual void heal(Player& player, int amount) = 0;
    virtual string getName() const = 0;
    virtual ~PlayerState() = default;
};

// Context
class Player {
private:
    string name;
    int health;
    int maxHealth;
    PlayerState* state;
    
public:
    Player(const string& n, int maxHp) : name(n), maxHealth(maxHp), health(maxHp), state(nullptr) {}
    
    void setState(PlayerState* newState) {
        state = newState;
        cout << name << " entered " << state->getName() << " state" << endl;
    }
    
    void move() {
        if (state) state->move(*this);
    }
    
    void attack() {
        if (state) state->attack(*this);
    }
    
    void takeDamage(int damage) {
        if (state) state->takeDamage(*this, damage);
    }
    
    void heal(int amount) {
        if (state) state->heal(*this, amount);
    }
    
    void setHealth(int hp) { 
        health = hp;
        if (health > maxHealth) health = maxHealth;
        if (health <= 0) health = 0;
    }
    
    int getHealth() const { return health; }
    int getMaxHealth() const { return maxHealth; }
    string getName() const { return name; }
};

// Concrete State: Normal
class NormalState : public PlayerState {
public:
    void move(Player& player) override {
        cout << player.getName() << " moves normally" << endl;
    }
    
    void attack(Player& player) override {
        cout << player.getName() << " attacks with full power" << endl;
    }
    
    void takeDamage(Player& player, int damage) override {
        int newHealth = player.getHealth() - damage;
        player.setHealth(newHealth);
        cout << player.getName() << " takes " << damage << " damage. Health: " 
             << player.getHealth() << "/" << player.getMaxHealth() << endl;
        
        if (player.getHealth() <= 0) {
            player.setState(new DeadState());
        } else if (player.getHealth() < player.getMaxHealth() / 4) {
            player.setState(new CriticalState());
        }
    }
    
    void heal(Player& player, int amount) override {
        int newHealth = player.getHealth() + amount;
        player.setHealth(newHealth);
        cout << player.getName() << " heals " << amount << " HP. Health: " 
             << player.getHealth() << "/" << player.getMaxHealth() << endl;
    }
    
    string getName() const override { return "Normal"; }
};

// Concrete State: Critical
class CriticalState : public PlayerState {
public:
    void move(Player& player) override {
        cout << player.getName() << " moves slowly (wounded)" << endl;
    }
    
    void attack(Player& player) override {
        cout << player.getName() << " attacks weakly (critical condition)" << endl;
    }
    
    void takeDamage(Player& player, int damage) override {
        int newHealth = player.getHealth() - damage;
        player.setHealth(newHealth);
        cout << player.getName() << " takes " << damage << " damage. Health: " 
             << player.getHealth() << "/" << player.getMaxHealth() << endl;
        
        if (player.getHealth() <= 0) {
            player.setState(new DeadState());
        }
    }
    
    void heal(Player& player, int amount) override {
        int newHealth = player.getHealth() + amount;
        player.setHealth(newHealth);
        cout << player.getName() << " heals " << amount << " HP. Health: " 
             << player.getHealth() << "/" << player.getMaxHealth() << endl;
        
        if (player.getHealth() > player.getMaxHealth() / 4) {
            player.setState(new NormalState());
        }
    }
    
    string getName() const override { return "Critical"; }
};

// Concrete State: Dead
class DeadState : public PlayerState {
public:
    void move(Player& player) override {
        cout << player.getName() << " cannot move (dead)" << endl;
    }
    
    void attack(Player& player) override {
        cout << player.getName() << " cannot attack (dead)" << endl;
    }
    
    void takeDamage(Player& player, int damage) override {
        cout << player.getName() << " is already dead" << endl;
    }
    
    void heal(Player& player, int amount) override {
        player.setHealth(amount);
        cout << player.getName() << " is revived with " << amount << " HP" << endl;
        player.setState(new NormalState());
    }
    
    string getName() const override { return "Dead"; }
};

int main() {
    cout << "=== Player State Example ===" << endl;
    
    Player player("Hero", 100);
    player.setState(new NormalState());
    
    cout << "\n1. Normal state actions:" << endl;
    player.move();
    player.attack();
    
    cout << "\n2. Taking damage:" << endl;
    player.takeDamage(30);
    player.takeDamage(50);
    
    cout << "\n3. Critical state actions:" << endl;
    player.move();
    player.attack();
    
    cout << "\n4. Healing from critical:" << endl;
    player.heal(30);
    
    cout << "\n5. Taking fatal damage:" << endl;
    player.takeDamage(80);
    
    cout << "\n6. Dead state actions:" << endl;
    player.move();
    player.attack();
    player.takeDamage(10);
    
    cout << "\n7. Reviving:" << endl;
    player.heal(50);
    
    return 0;
}
```

---

## 5. **Practical Example: Vending Machine**

```cpp
#include <iostream>
#include <string>
#include <map>
#include <memory>
using namespace std;

class VendingMachine;

// State interface
class VendingMachineState {
public:
    virtual void insertCoin(VendingMachine& machine, double amount) = 0;
    virtual void selectProduct(VendingMachine& machine, const string& product) = 0;
    virtual void dispense(VendingMachine& machine) = 0;
    virtual void refund(VendingMachine& machine) = 0;
    virtual string getName() const = 0;
    virtual ~VendingMachineState() = default;
};

// Context
class VendingMachine {
private:
    map<string, double> products;
    double balance;
    string selectedProduct;
    VendingMachineState* state;
    
public:
    VendingMachine() : balance(0), state(nullptr) {
        products["Coke"] = 1.50;
        products["Pepsi"] = 1.50;
        products["Water"] = 1.00;
        products["Chips"] = 1.25;
        products["Candy"] = 0.75;
    }
    
    void setState(VendingMachineState* newState) {
        state = newState;
        cout << "Vending machine state: " << state->getName() << endl;
    }
    
    void insertCoin(double amount) {
        if (state) state->insertCoin(*this, amount);
    }
    
    void selectProduct(const string& product) {
        if (state) state->selectProduct(*this, product);
    }
    
    void dispense() {
        if (state) state->dispense(*this);
    }
    
    void refund() {
        if (state) state->refund(*this);
    }
    
    void addBalance(double amount) { balance += amount; }
    double getBalance() const { return balance; }
    void resetBalance() { balance = 0; }
    
    double getProductPrice(const string& product) const {
        auto it = products.find(product);
        if (it != products.end()) return it->second;
        return 0;
    }
    
    void setSelectedProduct(const string& product) { selectedProduct = product; }
    string getSelectedProduct() const { return selectedProduct; }
    
    void dispenseProduct() {
        cout << "Dispensing " << selectedProduct << endl;
        balance -= getProductPrice(selectedProduct);
    }
    
    bool isProductAvailable(const string& product) const {
        return products.find(product) != products.end();
    }
};

// Concrete State: NoCoinState
class NoCoinState : public VendingMachineState {
public:
    void insertCoin(VendingMachine& machine, double amount) override {
        machine.addBalance(amount);
        cout << "Inserted $" << amount << ". Balance: $" << machine.getBalance() << endl;
        machine.setState(new HasCoinState());
    }
    
    void selectProduct(VendingMachine& machine, const string& product) override {
        cout << "Please insert coin first" << endl;
    }
    
    void dispense(VendingMachine& machine) override {
        cout << "Please insert coin first" << endl;
    }
    
    void refund(VendingMachine& machine) override {
        cout << "No money to refund" << endl;
    }
    
    string getName() const override { return "No Coin"; }
};

// Concrete State: HasCoinState
class HasCoinState : public VendingMachineState {
public:
    void insertCoin(VendingMachine& machine, double amount) override {
        machine.addBalance(amount);
        cout << "Inserted $" << amount << ". Balance: $" << machine.getBalance() << endl;
    }
    
    void selectProduct(VendingMachine& machine, const string& product) override {
        if (!machine.isProductAvailable(product)) {
            cout << "Product not available" << endl;
            return;
        }
        
        double price = machine.getProductPrice(product);
        if (machine.getBalance() >= price) {
            machine.setSelectedProduct(product);
            machine.setState(new SoldState());
            machine.dispense();
        } else {
            cout << "Insufficient balance. Need $" << (price - machine.getBalance()) 
                 << " more" << endl;
        }
    }
    
    void dispense(VendingMachine& machine) override {
        cout << "Please select a product first" << endl;
    }
    
    void refund(VendingMachine& machine) override {
        cout << "Refunding $" << machine.getBalance() << endl;
        machine.resetBalance();
        machine.setState(new NoCoinState());
    }
    
    string getName() const override { return "Has Coin"; }
};

// Concrete State: SoldState
class SoldState : public VendingMachineState {
public:
    void insertCoin(VendingMachine& machine, double amount) override {
        cout << "Please wait, dispensing product" << endl;
    }
    
    void selectProduct(VendingMachine& machine, const string& product) override {
        cout << "Please wait, dispensing product" << endl;
    }
    
    void dispense(VendingMachine& machine) override {
        machine.dispenseProduct();
        cout << "Remaining balance: $" << machine.getBalance() << endl;
        
        if (machine.getBalance() > 0) {
            machine.setState(new HasCoinState());
        } else {
            machine.setState(new NoCoinState());
        }
    }
    
    void refund(VendingMachine& machine) override {
        cout << "Cannot refund, product already selected" << endl;
    }
    
    string getName() const override { return "Sold"; }
};

int main() {
    cout << "=== Vending Machine Example ===" << endl;
    
    VendingMachine machine;
    machine.setState(new NoCoinState());
    
    cout << "\n1. Try to select product without money:" << endl;
    machine.selectProduct("Coke");
    
    cout << "\n2. Insert money:" << endl;
    machine.insertCoin(1.00);
    machine.insertCoin(0.50);
    
    cout << "\n3. Select product:" << endl;
    machine.selectProduct("Coke");
    
    cout << "\n4. Try to insert more money while dispensing:" << endl;
    machine.insertCoin(1.00);
    
    cout << "\n5. Another transaction:" << endl;
    machine.insertCoin(2.00);
    machine.selectProduct("Chips");
    
    cout << "\n6. Refund test:" << endl;
    machine.insertCoin(1.00);
    machine.refund();
    machine.selectProduct("Water");
    
    return 0;
}
```

---

## 📊 State Pattern Summary

| Component | Description |
|-----------|-------------|
| **Context** | Maintains current state |
| **State** | Interface for state-specific behavior |
| **Concrete State** | Implements behavior for a specific state |
| **State Transition** | States can change to other states |

---

## ✅ Best Practices

1. **Use State** when object behavior depends on its state
2. **Encapsulate state-specific** behavior in state classes
3. **Avoid large conditional** statements for state handling
4. **Let states manage** their own transitions
5. **Consider using** flyweight pattern for states

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **State explosion** | Too many states | Evaluate if needed |
| **Tight coupling** | States know each other | Use context for transitions |
| **Memory usage** | Many state objects | Use singleton states |

---

## ✅ Key Takeaways

1. **State pattern** encapsulates state-specific behavior
2. **Objects change behavior** when state changes
3. **Eliminates large conditional** statements
4. **Makes state transitions** explicit
5. **Useful for** workflow systems, game AI, vending machines
6. **Follows** Open/Closed Principle

---