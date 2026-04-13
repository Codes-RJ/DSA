# Command Pattern in C++ - Complete Guide

## 📖 Overview

The Command pattern encapsulates a request as an object, thereby allowing for parameterization of clients with different requests, queueing of requests, and logging of requests. It also provides support for undoable operations. This pattern decouples the object that invokes the operation from the one that knows how to perform it.

---

## 🎯 Key Concepts

| Concept | Description |
|---------|-------------|
| **Command** | Declares interface for executing operations |
| **Concrete Command** | Implements execute method and binds receiver |
| **Receiver** | Knows how to perform the operation |
| **Invoker** | Asks the command to carry out the request |
| **Client** | Creates concrete command and sets its receiver |

---

## 1. **Basic Command Pattern**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
using namespace std;

// Receiver
class Light {
private:
    string location;
    
public:
    Light(const string& loc) : location(loc) {}
    
    void turnOn() {
        cout << location << " light is ON" << endl;
    }
    
    void turnOff() {
        cout << location << " light is OFF" << endl;
    }
};

// Command interface
class ICommand {
public:
    virtual void execute() = 0;
    virtual void undo() = 0;
    virtual ~ICommand() = default;
};

// Concrete Command 1: TurnOnCommand
class TurnOnCommand : public ICommand {
private:
    Light& light;
    
public:
    TurnOnCommand(Light& l) : light(l) {}
    
    void execute() override {
        light.turnOn();
    }
    
    void undo() override {
        light.turnOff();
    }
};

// Concrete Command 2: TurnOffCommand
class TurnOffCommand : public ICommand {
private:
    Light& light;
    
public:
    TurnOffCommand(Light& l) : light(l) {}
    
    void execute() override {
        light.turnOff();
    }
    
    void undo() override {
        light.turnOn();
    }
};

// Invoker
class RemoteControl {
private:
    vector<unique_ptr<ICommand>> history;
    
public:
    void executeCommand(ICommand* cmd) {
        cmd->execute();
        history.emplace_back(cmd);
    }
    
    void undo() {
        if (!history.empty()) {
            history.back()->undo();
            history.pop_back();
        } else {
            cout << "Nothing to undo" << endl;
        }
    }
};

int main() {
    cout << "=== Basic Command Pattern ===" << endl;
    
    Light livingRoom("Living Room");
    Light kitchen("Kitchen");
    
    TurnOnCommand turnOnLiving(livingRoom);
    TurnOffCommand turnOffLiving(livingRoom);
    TurnOnCommand turnOnKitchen(kitchen);
    
    RemoteControl remote;
    
    cout << "\nExecuting commands:" << endl;
    remote.executeCommand(&turnOnLiving);
    remote.executeCommand(&turnOnKitchen);
    remote.executeCommand(&turnOffLiving);
    
    cout << "\nUndoing last command:" << endl;
    remote.undo();
    
    cout << "\nUndoing another command:" << endl;
    remote.undo();
    
    return 0;
}
```

**Output:**
```
=== Basic Command Pattern ===

Executing commands:
Living Room light is ON
Kitchen light is ON
Living Room light is OFF

Undoing last command:
Living Room light is ON

Undoing another command:
Kitchen light is OFF
```

---

## 2. **Command with Multiple Receivers**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <stack>
using namespace std;

// Receivers
class TV {
private:
    string location;
    int volume;
    int channel;
    
public:
    TV(const string& loc) : location(loc), volume(10), channel(1) {}
    
    void turnOn() {
        cout << location << " TV is ON" << endl;
    }
    
    void turnOff() {
        cout << location << " TV is OFF" << endl;
    }
    
    void setVolume(int vol) {
        volume = vol;
        cout << location << " TV volume set to " << volume << endl;
    }
    
    void setChannel(int ch) {
        channel = ch;
        cout << location << " TV channel set to " << channel << endl;
    }
};

class Stereo {
private:
    string location;
    int volume;
    
public:
    Stereo(const string& loc) : location(loc), volume(5) {}
    
    void turnOn() {
        cout << location << " Stereo is ON" << endl;
    }
    
    void turnOff() {
        cout << location << " Stereo is OFF" << endl;
    }
    
    void setVolume(int vol) {
        volume = vol;
        cout << location << " Stereo volume set to " << volume << endl;
    }
    
    void setCD() {
        cout << location << " Stereo set to CD mode" << endl;
    }
};

// Commands
class TVOnCommand : public ICommand {
private:
    TV& tv;
    
public:
    TVOnCommand(TV& t) : tv(t) {}
    
    void execute() override {
        tv.turnOn();
    }
    
    void undo() override {
        tv.turnOff();
    }
};

class TVOffCommand : public ICommand {
private:
    TV& tv;
    
public:
    TVOffCommand(TV& t) : tv(t) {}
    
    void execute() override {
        tv.turnOff();
    }
    
    void undo() override {
        tv.turnOn();
    }
};

class TVSetChannelCommand : public ICommand {
private:
    TV& tv;
    int channel;
    int previousChannel;
    
public:
    TVSetChannelCommand(TV& t, int ch) : tv(t), channel(ch), previousChannel(0) {}
    
    void execute() override {
        previousChannel = tv.getChannel();
        tv.setChannel(channel);
    }
    
    void undo() override {
        tv.setChannel(previousChannel);
    }
};

class StereoOnWithCDCommand : public ICommand {
private:
    Stereo& stereo;
    int previousVolume;
    
public:
    StereoOnWithCDCommand(Stereo& s) : stereo(s), previousVolume(0) {}
    
    void execute() override {
        previousVolume = stereo.getVolume();
        stereo.turnOn();
        stereo.setCD();
        stereo.setVolume(10);
    }
    
    void undo() override {
        stereo.turnOff();
        stereo.setVolume(previousVolume);
    }
};

class MacroCommand : public ICommand {
private:
    vector<ICommand*> commands;
    
public:
    void addCommand(ICommand* cmd) {
        commands.push_back(cmd);
    }
    
    void execute() override {
        for (auto cmd : commands) {
            cmd->execute();
        }
    }
    
    void undo() override {
        for (auto it = commands.rbegin(); it != commands.rend(); ++it) {
            (*it)->undo();
        }
    }
};

int main() {
    cout << "=== Command with Multiple Receivers ===" << endl;
    
    TV livingRoomTV("Living Room");
    Stereo livingRoomStereo("Living Room");
    
    TVOnCommand tvOn(livingRoomTV);
    TVSetChannelCommand tvChannel(livingRoomTV, 5);
    StereoOnWithCDCommand stereoOn(livingRoomStereo);
    
    MacroCommand partyMode;
    partyMode.addCommand(&tvOn);
    partyMode.addCommand(&tvChannel);
    partyMode.addCommand(&stereoOn);
    
    RemoteControl remote;
    
    cout << "\nExecuting party mode macro:" << endl;
    remote.executeCommand(&partyMode);
    
    cout << "\nUndoing party mode:" << endl;
    remote.undo();
    
    return 0;
}
```

---

## 3. **Command with Undo/Redo**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <memory>
using namespace std;

class TextEditor {
private:
    string content;
    
public:
    void insertText(const string& text, int position) {
        content.insert(position, text);
        cout << "Inserted '" << text << "' at position " << position << endl;
    }
    
    void deleteText(int position, int length) {
        content.erase(position, length);
        cout << "Deleted " << length << " characters at position " << position << endl;
    }
    
    string getContent() const {
        return content;
    }
    
    void display() const {
        cout << "Content: \"" << content << "\"" << endl;
    }
};

class InsertCommand : public ICommand {
private:
    TextEditor& editor;
    string text;
    int position;
    
public:
    InsertCommand(TextEditor& e, const string& t, int pos) 
        : editor(e), text(t), position(pos) {}
    
    void execute() override {
        editor.insertText(text, position);
    }
    
    void undo() override {
        editor.deleteText(position, text.length());
    }
};

class DeleteCommand : public ICommand {
private:
    TextEditor& editor;
    string deletedText;
    int position;
    int length;
    
public:
    DeleteCommand(TextEditor& e, int pos, int len) 
        : editor(e), position(pos), length(len) {
        // In real implementation, would need to capture deleted text
        deletedText = editor.getContent().substr(pos, len);
    }
    
    void execute() override {
        editor.deleteText(position, length);
    }
    
    void undo() override {
        editor.insertText(deletedText, position);
    }
};

class CommandManager {
private:
    stack<unique_ptr<ICommand>> undoStack;
    stack<unique_ptr<ICommand>> redoStack;
    
public:
    void executeCommand(ICommand* cmd) {
        cmd->execute();
        undoStack.push(unique_ptr<ICommand>(cmd));
        
        // Clear redo stack
        while (!redoStack.empty()) {
            redoStack.pop();
        }
    }
    
    void undo() {
        if (!undoStack.empty()) {
            auto cmd = move(undoStack.top());
            undoStack.pop();
            cmd->undo();
            redoStack.push(move(cmd));
        } else {
            cout << "Nothing to undo" << endl;
        }
    }
    
    void redo() {
        if (!redoStack.empty()) {
            auto cmd = move(redoStack.top());
            redoStack.pop();
            cmd->execute();
            undoStack.push(move(cmd));
        } else {
            cout << "Nothing to redo" << endl;
        }
    }
};

int main() {
    cout << "=== Command with Undo/Redo ===" << endl;
    
    TextEditor editor;
    CommandManager manager;
    
    cout << "\nInitial state:" << endl;
    editor.display();
    
    cout << "\nInserting text:" << endl;
    manager.executeCommand(new InsertCommand(editor, "Hello", 0));
    editor.display();
    
    manager.executeCommand(new InsertCommand(editor, " World", 5));
    editor.display();
    
    manager.executeCommand(new InsertCommand(editor, " Beautiful", 6));
    editor.display();
    
    cout << "\nUndo last operation:" << endl;
    manager.undo();
    editor.display();
    
    cout << "\nUndo again:" << endl;
    manager.undo();
    editor.display();
    
    cout << "\nRedo:" << endl;
    manager.redo();
    editor.display();
    
    cout << "\nRedo again:" << endl;
    manager.redo();
    editor.display();
    
    return 0;
}
```

---

## 4. **Command Queue (Task Scheduler)**

```cpp
#include <iostream>
#include <string>
#include <queue>
#include <thread>
#include <chrono>
#include <functional>
#include <random>
using namespace std;

class Task : public ICommand {
private:
    string name;
    function<void()> task;
    chrono::steady_clock::time_point startTime;
    
public:
    Task(const string& n, function<void()> t) : name(n), task(t) {}
    
    void execute() override {
        startTime = chrono::steady_clock::now();
        cout << "[START] " << name << endl;
        task();
        auto endTime = chrono::steady_clock::now();
        auto duration = chrono::duration_cast<chrono::milliseconds>(endTime - startTime);
        cout << "[END] " << name << " (took " << duration.count() << " ms)" << endl;
    }
    
    void undo() override {
        cout << "[UNDO] " << name << " - Cannot undo this task" << endl;
    }
    
    string getName() const { return name; }
};

class TaskScheduler {
private:
    queue<unique_ptr<ICommand>> taskQueue;
    bool running;
    
public:
    TaskScheduler() : running(true) {}
    
    void addTask(ICommand* task) {
        taskQueue.emplace(task);
        cout << "Task added to queue: " << dynamic_cast<Task*>(task)->getName() << endl;
    }
    
    void processTasks() {
        while (running && !taskQueue.empty()) {
            auto task = move(taskQueue.front());
            taskQueue.pop();
            task->execute();
            
            // Simulate delay between tasks
            this_thread::sleep_for(chrono::milliseconds(100));
        }
    }
    
    void stop() {
        running = false;
    }
};

int main() {
    cout << "=== Command Queue (Task Scheduler) ===" << endl;
    
    TaskScheduler scheduler;
    
    // Simulate random sleep tasks
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(50, 200);
    
    scheduler.addTask(new Task("Task 1", []() {
        this_thread::sleep_for(chrono::milliseconds(100));
        cout << "  Processing data..." << endl;
    }));
    
    scheduler.addTask(new Task("Task 2", []() {
        this_thread::sleep_for(chrono::milliseconds(150));
        cout << "  Calculating results..." << endl;
    }));
    
    scheduler.addTask(new Task("Task 3", []() {
        this_thread::sleep_for(chrono::milliseconds(80));
        cout << "  Saving to database..." << endl;
    }));
    
    scheduler.addTask(new Task("Task 4", []() {
        this_thread::sleep_for(chrono::milliseconds(120));
        cout << "  Sending notifications..." << endl;
    }));
    
    scheduler.addTask(new Task("Task 5", []() {
        this_thread::sleep_for(chrono::milliseconds(90));
        cout << "  Generating report..." << endl;
    }));
    
    cout << "\nProcessing task queue:" << endl;
    scheduler.processTasks();
    
    return 0;
}
```

---

## 5. **Practical Example: Smart Home Automation**

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <memory>
#include <chrono>
#include <thread>
#include <ctime>
#include <iomanip>
using namespace std;

// Receivers
class Thermostat {
private:
    int temperature;
    
public:
    Thermostat() : temperature(20) {}
    
    void setTemperature(int temp) {
        temperature = temp;
        cout << "Thermostat set to " << temperature << "°C" << endl;
    }
    
    int getTemperature() const { return temperature; }
};

class Sprinkler {
private:
    bool running;
    
public:
    Sprinkler() : running(false) {}
    
    void turnOn() {
        running = true;
        cout << "Sprinklers turned ON" << endl;
    }
    
    void turnOff() {
        running = false;
        cout << "Sprinklers turned OFF" << endl;
    }
    
    bool isRunning() const { return running; }
};

class GarageDoor {
private:
    bool open;
    
public:
    GarageDoor() : open(false) {}
    
    void openDoor() {
        open = true;
        cout << "Garage door OPENED" << endl;
    }
    
    void closeDoor() {
        open = false;
        cout << "Garage door CLOSED" << endl;
    }
};

class SecuritySystem {
private:
    bool armed;
    
public:
    SecuritySystem() : armed(false) {}
    
    void arm() {
        armed = true;
        cout << "Security system ARMED" << endl;
    }
    
    void disarm() {
        armed = false;
        cout << "Security system DISARMED" << endl;
    }
};

// Commands
class ThermostatCommand : public ICommand {
private:
    Thermostat& thermostat;
    int temperature;
    int previousTemp;
    
public:
    ThermostatCommand(Thermostat& t, int temp) 
        : thermostat(t), temperature(temp), previousTemp(0) {}
    
    void execute() override {
        previousTemp = thermostat.getTemperature();
        thermostat.setTemperature(temperature);
    }
    
    void undo() override {
        thermostat.setTemperature(previousTemp);
    }
};

class SprinklerCommand : public ICommand {
private:
    Sprinkler& sprinkler;
    bool turnOn;
    bool previousState;
    
public:
    SprinklerCommand(Sprinkler& s, bool on) : sprinkler(s), turnOn(on) {}
    
    void execute() override {
        previousState = sprinkler.isRunning();
        if (turnOn) sprinkler.turnOn();
        else sprinkler.turnOff();
    }
    
    void undo() override {
        if (previousState) sprinkler.turnOn();
        else sprinkler.turnOff();
    }
};

class GarageDoorCommand : public ICommand {
private:
    GarageDoor& door;
    bool open;
    bool previousState;
    
public:
    GarageDoorCommand(GarageDoor& d, bool o) : door(d), open(o) {}
    
    void execute() override {
        if (open) door.openDoor();
        else door.closeDoor();
    }
    
    void undo() override {
        if (!open) door.openDoor();
        else door.closeDoor();
    }
};

class SecurityCommand : public ICommand {
private:
    SecuritySystem& security;
    bool arm;
    bool previousState;
    
public:
    SecurityCommand(SecuritySystem& s, bool a) : security(s), arm(a) {}
    
    void execute() override {
        if (arm) security.arm();
        else security.disarm();
    }
    
    void undo() override {
        if (!arm) security.arm();
        else security.disarm();
    }
};

class AutomationSystem {
private:
    vector<unique_ptr<ICommand>> history;
    map<string, ICommand*> commands;
    
public:
    void setCommand(const string& name, ICommand* cmd) {
        commands[name] = cmd;
    }
    
    void executeCommand(const string& name) {
        auto it = commands.find(name);
        if (it != commands.end()) {
            it->second->execute();
            history.emplace_back(it->second);
        }
    }
    
    void undoLast() {
        if (!history.empty()) {
            history.back()->undo();
            history.pop_back();
        } else {
            cout << "No commands to undo" << endl;
        }
    }
    
    void executeMacro(const vector<string>& commandNames) {
        for (const auto& name : commandNames) {
            executeCommand(name);
        }
    }
};

int main() {
    cout << "=== Smart Home Automation ===" << endl;
    
    Thermostat thermostat;
    Sprinkler sprinkler;
    GarageDoor garageDoor;
    SecuritySystem security;
    
    AutomationSystem home;
    
    // Setup commands
    home.setCommand("set_temp_22", new ThermostatCommand(thermostat, 22));
    home.setCommand("set_temp_18", new ThermostatCommand(thermostat, 18));
    home.setCommand("sprinkler_on", new SprinklerCommand(sprinkler, true));
    home.setCommand("sprinkler_off", new SprinklerCommand(sprinkler, false));
    home.setCommand("garage_open", new GarageDoorCommand(garageDoor, true));
    home.setCommand("garage_close", new GarageDoorCommand(garageDoor, false));
    home.setCommand("security_arm", new SecurityCommand(security, true));
    home.setCommand("security_disarm", new SecurityCommand(security, false));
    
    cout << "\nExecuting individual commands:" << endl;
    home.executeCommand("set_temp_22");
    home.executeCommand("sprinkler_on");
    home.executeCommand("garage_open");
    
    cout << "\nUndoing last command:" << endl;
    home.undoLast();
    
    cout << "\nExecuting macro (Good Night routine):" << endl;
    vector<string> goodNight = {"set_temp_18", "sprinkler_off", "garage_close", "security_arm"};
    home.executeMacro(goodNight);
    
    cout << "\nUndoing Good Night routine:" << endl;
    home.undoLast();  // Undo security_arm
    home.undoLast();  // Undo garage_close
    home.undoLast();  // Undo sprinkler_off
    home.undoLast();  // Undo set_temp_18
    
    return 0;
}
```

---

## 📊 Command Pattern Summary

| Component | Description |
|-----------|-------------|
| **Command** | Interface for executing operations |
| **Concrete Command** | Binds receiver to action |
| **Receiver** | Knows how to perform operations |
| **Invoker** | Executes commands |
| **Client** | Creates commands and sets receivers |

---

## ✅ Best Practices

1. **Use Command** for undo/redo functionality
2. **Use Command** for queuing and logging operations
3. **Store state** in commands for undo support
4. **Use macro commands** for composite operations
5. **Separate command creation** from execution

---

## 🐛 Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Too many command classes** | Code bloat | Use lambda commands |
| **Memory management** | Leaks with dynamic allocation | Use smart pointers |
| **Undo state size** | Memory consumption | Limit history size |

---

## ✅ Key Takeaways

1. **Command pattern** encapsulates requests as objects
2. **Supports undo/redo** functionality
3. **Enables queuing** and logging of requests
4. **Decouples** invoker from receiver
5. **Macro commands** combine multiple commands
6. **Useful for** transaction systems, editors, automation

---
---

## Next Step

- Go to [Observer.md](Observer.md) to continue with Observer.
