# 19_stack.md - LIFO Container Adapter

The `stack` header provides `std::stack`, a container adapter that provides last-in, first-out (LIFO) access to elements.

## 📖 Overview

`std::stack` is a container adapter that gives the functionality of a stack - specifically, a LIFO (last-in, first-out) data structure. It wraps an underlying container (by default `std::deque`) and provides a restricted interface with stack operations.

## 🎯 Key Features

- **LIFO access** - Last element pushed is first element popped
- **Restricted interface** - Only stack operations are available
- **Container adapter** - Works with different underlying containers
- **Constant-time operations** - All operations are O(1)
- **No iteration** - Cannot iterate through elements directly
- **Default container** - Uses `std::deque` by default

## 🔧 Basic Stack Operations

### Creating and Initializing Stacks
```cpp
#include <iostream>
#include <stack>
#include <vector>
#include <list>

int main() {
    // Different ways to create stacks
    
    // Default stack (uses deque)
    std::stack<int> stack1;
    
    // Stack with vector as underlying container
    std::stack<int, std::vector<int>> stack2;
    
    // Stack with list as underlying container
    std::stack<int, std::list<int>> stack3;
    
    // Stack from existing container
    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::stack<int, std::vector<int>> stack4(vec);
    
    // Copy constructor
    std::stack<int> stack5 = stack1;
    
    return 0;
}
```

### Push and Pop Operations
```cpp
void demonstrateBasicOperations() {
    std::stack<int> s;
    
    // Push elements
    s.push(10);
    s.push(20);
    s.push(30);
    
    std::cout << "Stack size: " << s.size() << std::endl;
    std::cout << "Top element: " << s.top() << std::endl;
    
    // Pop elements
    while (!s.empty()) {
        std::cout << "Popping: " << s.top() << std::endl;
        s.pop();
    }
    
    std::cout << "Stack is now empty: " << (s.empty() ? "Yes" : "No") << std::endl;
}
```

### Emplace Operations
```cpp
void demonstrateEmplace() {
    std::stack<std::pair<int, std::string>> s;
    
    // Push with emplace (constructs in place)
    s.emplace(1, "First");
    s.emplace(2, "Second");
    s.emplace(3, "Third");
    
    while (!s.empty()) {
        auto& pair = s.top();
        std::cout << pair.first << ": " << pair.second << std::endl;
        s.pop();
    }
}
```

## 🔧 Advanced Stack Operations

### Stack with Custom Container
```cpp
void demonstrateCustomContainers() {
    // Stack using vector (good for random access)
    std::stack<int, std::vector<int>> vector_stack;
    vector_stack.push(1);
    vector_stack.push(2);
    vector_stack.push(3);
    
    std::cout << "Vector-based stack size: " << vector_stack.size() << std::endl;
    
    // Stack using list (good for splicing)
    std::stack<int, std::list<int>> list_stack;
    list_stack.push(4);
    list_stack.push(5);
    list_stack.push(6);
    
    std::cout << "List-based stack size: " << list_stack.size() << std::endl;
}
```

### Accessing Underlying Container
```cpp
void demonstrateUnderlyingAccess() {
    std::stack<int, std::vector<int>> s;
    
    // Push some elements
    for (int i = 1; i <= 5; ++i) {
        s.push(i * 10);
    }
    
    // Access underlying container (non-standard but commonly supported)
    // Note: This is implementation-specific and not portable
    #ifdef __GNUC__
    auto& container = s._Get_container();
    std::cout << "Underlying container size: " << container.size() << std::endl;
    
    // Access elements through underlying container
    for (const auto& elem : container) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;
    #endif
}
```

## 🎮 Practical Examples

### Example 1: Expression Evaluator
```cpp
#include <iostream>
#include <stack>
#include <string>
#include <sstream>
#include <cctype>
#include <cmath>

class ExpressionEvaluator {
private:
    // Helper function to check if character is operator
    bool isOperator(char c) const {
        return c == '+' || c == '-' || c == '*' || c == '/' || c == '^';
    }
    
    // Helper function to get operator precedence
    int getPrecedence(char op) const {
        if (op == '^') return 3;
        if (op == '*' || op == '/') return 2;
        if (op == '+' || op == '-') return 1;
        return 0;
    }
    
    // Helper function to apply operator
    double applyOperator(double a, double b, char op) const {
        switch (op) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/': 
                if (b == 0) throw std::runtime_error("Division by zero");
                return a / b;
            case '^': return std::pow(a, b);
            default: throw std::runtime_error("Invalid operator");
        }
    }
    
public:
    // Evaluate postfix expression
    double evaluatePostfix(const std::string& expression) {
        std::stack<double> operands;
        std::istringstream iss(expression);
        std::string token;
        
        while (iss >> token) {
            if (std::isdigit(token[0]) || (token[0] == '-' && token.length() > 1)) {
                // Token is a number
                operands.push(std::stod(token));
            } else if (isOperator(token[0])) {
                // Token is an operator
                if (operands.size() < 2) {
                    throw std::runtime_error("Invalid postfix expression");
                }
                
                double b = operands.top(); operands.pop();
                double a = operands.top(); operands.pop();
                
                double result = applyOperator(a, b, token[0]);
                operands.push(result);
            }
        }
        
        if (operands.size() != 1) {
            throw std::runtime_error("Invalid postfix expression");
        }
        
        return operands.top();
    }
    
    // Evaluate infix expression
    double evaluateInfix(const std::string& expression) {
        // Convert infix to postfix first
        std::string postfix = infixToPostfix(expression);
        std::cout << "Postfix: " << postfix << std::endl;
        
        // Then evaluate postfix
        return evaluatePostfix(postfix);
    }
    
private:
    // Convert infix to postfix notation
    std::string infixToPostfix(const std::string& expression) {
        std::stack<char> operators;
        std::string postfix;
        std::istringstream iss(expression);
        std::string token;
        
        while (iss >> token) {
            if (std::isdigit(token[0]) || (token[0] == '-' && token.length() > 1)) {
                // Token is a number
                postfix += token + " ";
            } else if (token[0] == '(') {
                operators.push('(');
            } else if (token[0] == ')') {
                while (!operators.empty() && operators.top() != '(') {
                    postfix += operators.top();
                    postfix += " ";
                    operators.pop();
                }
                if (!operators.empty()) {
                    operators.pop(); // Remove '('
                }
            } else if (isOperator(token[0])) {
                while (!operators.empty() && operators.top() != '(' &&
                       getPrecedence(operators.top()) >= getPrecedence(token[0])) {
                    postfix += operators.top();
                    postfix += " ";
                    operators.pop();
                }
                operators.push(token[0]);
            }
        }
        
        // Pop remaining operators
        while (!operators.empty()) {
            postfix += operators.top();
            postfix += " ";
            operators.pop();
        }
        
        return postfix;
    }
    
public:
    // Check if parentheses are balanced
    bool areParenthesesBalanced(const std::string& expression) {
        std::stack<char> parentheses;
        
        for (char c : expression) {
            if (c == '(' || c == '[' || c == '{') {
                parentheses.push(c);
            } else if (c == ')' || c == ']' || c == '}') {
                if (parentheses.empty()) return false;
                
                char top = parentheses.top();
                parentheses.pop();
                
                if ((c == ')' && top != '(') ||
                    (c == ']' && top != '[') ||
                    (c == '}' && top != '{')) {
                    return false;
                }
            }
        }
        
        return parentheses.empty();
    }
};

int main() {
    ExpressionEvaluator evaluator;
    
    std::cout << "=== Expression Evaluator ===" << std::endl;
    
    // Test postfix evaluation
    std::cout << "\n=== Postfix Evaluation ===" << std::endl;
    std::string postfix1 = "3 4 + 2 * 7 /";
    std::cout << "Postfix: " << postfix1 << std::endl;
    try {
        double result1 = evaluator.evaluatePostfix(postfix1);
        std::cout << "Result: " << result1 << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
    
    // Test infix evaluation
    std::cout << "\n=== Infix Evaluation ===" << std::endl;
    std::string infix1 = "( 3 + 4 ) * 2 / 7";
    std::cout << "Infix: " << infix1 << std::endl;
    try {
        double result2 = evaluator.evaluateInfix(infix1);
        std::cout << "Result: " << result2 << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
    
    // Test complex expression
    std::cout << "\n=== Complex Expression ===" << std::endl;
    std::string infix2 = "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3";
    std::cout << "Infix: " << infix2 << std::endl;
    try {
        double result3 = evaluator.evaluateInfix(infix2);
        std::cout << "Result: " << result3 << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
    
    // Test parentheses balancing
    std::cout << "\n=== Parentheses Balancing ===" << std::endl;
    std::vector<std::string> expressions = {
        "(a + b) * (c - d)",
        "([{}])",
        "((())",
        "{[()]}",
        "([)]"
    };
    
    for (const auto& expr : expressions) {
        bool balanced = evaluator.areParenthesesBalanced(expr);
        std::cout << "\"" << expr << "\" - " << (balanced ? "Balanced" : "Not balanced") << std::endl;
    }
    
    return 0;
}
```

### Example 2: Undo/Redo System
```cpp
#include <iostream>
#include <stack>
#include <string>
#include <functional>

class UndoRedoSystem {
private:
    struct Action {
        std::string description;
        std::function<void()> execute;
        std::function<void()> undo;
        
        Action(const std::string& desc, std::function<void()> exec, std::function<void()> und)
            : description(desc), execute(exec), undo(und) {}
    };
    
    std::stack<Action> undo_stack;
    std::stack<Action> redo_stack;
    
public:
    // Perform an action and add it to undo stack
    void performAction(const std::string& description, 
                      std::function<void()> execute, 
                      std::function<void()> undo) {
        execute();
        undo_stack.emplace(description, execute, undo);
        
        // Clear redo stack when new action is performed
        while (!redo_stack.empty()) {
            redo_stack.pop();
        }
        
        std::cout << "Performed: " << description << std::endl;
    }
    
    // Undo last action
    bool undo() {
        if (undo_stack.empty()) {
            std::cout << "Nothing to undo" << std::endl;
            return false;
        }
        
        Action& action = undo_stack.top();
        action.undo();
        
        // Move to redo stack
        redo_stack.push(action);
        undo_stack.pop();
        
        std::cout << "Undone: " << action.description << std::endl;
        return true;
    }
    
    // Redo last undone action
    bool redo() {
        if (redo_stack.empty()) {
            std::cout << "Nothing to redo" << std::endl;
            return false;
        }
        
        Action& action = redo_stack.top();
        action.execute();
        
        // Move back to undo stack
        undo_stack.push(action);
        redo_stack.pop();
        
        std::cout << "Redone: " << action.description << std::endl;
        return true;
    }
    
    // Get history sizes
    size_t getUndoCount() const { return undo_stack.size(); }
    size_t getRedoCount() const { return redo_stack.size(); }
    
    // Display history
    void displayHistory() const {
        std::cout << "\n=== History ===" << std::endl;
        std::cout << "Undo stack (" << getUndoCount() << " items):" << std::endl;
        
        // Create a copy to display (since we can't iterate through stack)
        std::stack<Action> temp_undo = undo_stack;
        std::vector<std::string> undo_items;
        
        while (!temp_undo.empty()) {
            undo_items.push_back(temp_undo.top().description);
            temp_undo.pop();
        }
        
        // Display in reverse order (oldest first)
        for (auto it = undo_items.rbegin(); it != undo_items.rend(); ++it) {
            std::cout << "  " << *it << std::endl;
        }
        
        std::cout << "Redo stack (" << getRedoCount() << " items):" << std::endl;
        
        std::stack<Action> temp_redo = redo_stack;
        std::vector<std::string> redo_items;
        
        while (!temp_redo.empty()) {
            redo_items.push_back(temp_redo.top().description);
            temp_redo.pop();
        }
        
        for (auto it = redo_items.rbegin(); it != redo_items.rend(); ++it) {
            std::cout << "  " << *it << std::endl;
        }
    }
    
    // Clear all history
    void clear() {
        while (!undo_stack.empty()) undo_stack.pop();
        while (!redo_stack.empty()) redo_stack.pop();
        std::cout << "History cleared" << std::endl;
    }
};

int main() {
    UndoRedoSystem system;
    
    std::cout << "=== Undo/Redo System Demo ===" << std::endl;
    
    // Simulate a text editor
    std::string text = "";
    
    // Add some actions
    system.performAction("Type 'Hello'", 
        [&text]() { text += "Hello"; },
        [&text]() { text = text.substr(0, text.length() - 5); });
    
    system.performAction("Type ' World'", 
        [&text]() { text += " World"; },
        [&text]() { text = text.substr(0, text.length() - 6); });
    
    system.performAction("Type '!'", 
        [&text]() { text += "!"; },
        [&text]() { text = text.substr(0, text.length() - 1); });
    
    std::cout << "Current text: \"" << text << "\"" << std::endl;
    system.displayHistory();
    
    // Test undo
    std::cout << "\n=== Testing Undo ===" << std::endl;
    system.undo();
    std::cout << "Current text: \"" << text << "\"" << std::endl;
    
    system.undo();
    std::cout << "Current text: \"" << text << "\"" << std::endl;
    
    // Test redo
    std::cout << "\n=== Testing Redo ===" << std::endl;
    system.redo();
    std::cout << "Current text: \"" << text << "\"" << std::endl;
    
    // Add new action (should clear redo stack)
    std::cout << "\n=== Adding New Action ===" << std::endl;
    system.performAction("Type ' C++'", 
        [&text]() { text += " C++"; },
        [&text]() { text = text.substr(0, text.length() - 4); });
    
    std::cout << "Current text: \"" << text << "\"" << std::endl;
    system.displayHistory();
    
    // Try to redo (should fail)
    std::cout << "\n=== Testing Redo After New Action ===" << std::endl;
    system.redo();
    
    return 0;
}
```

### Example 3: Function Call Stack Simulator
```cpp
#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <chrono>

class FunctionCall {
private:
    std::string name;
    std::chrono::time_point<std::chrono::high_resolution_clock> start_time;
    
public:
    FunctionCall(const std::string& func_name) 
        : name(func_name), start_time(std::chrono::high_resolution_clock::now()) {}
    
    const std::string& getName() const { return name; }
    
    auto getDuration() const {
        auto end_time = std::chrono::high_resolution_clock::now();
        return std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
    }
};

class CallStackSimulator {
private:
    std::stack<FunctionCall> call_stack;
    std::vector<std::string> call_history;
    
public:
    // Enter a function
    void enterFunction(const std::string& function_name) {
        call_stack.emplace(function_name);
        call_history.push_back("ENTER: " + function_name);
        
        std::cout << std::string(call_stack.size() * 2, ' ') 
                  << "-> Entering " << function_name << std::endl;
    }
    
    // Exit current function
    void exitFunction() {
        if (call_stack.empty()) {
            std::cout << "Error: Cannot exit - call stack is empty" << std::endl;
            return;
        }
        
        FunctionCall& current = call_stack.top();
        auto duration = current.getDuration();
        
        std::cout << std::string(call_stack.size() * 2, ' ') 
                  << "<- Exiting " << current.getName() 
                  << " (took " << duration.count() << " μs)" << std::endl;
        
        call_history.push_back("EXIT: " + current.getName());
        call_stack.pop();
    }
    
    // Get current function depth
    size_t getCurrentDepth() const {
        return call_stack.size();
    }
    
    // Get current function name
    std::string getCurrentFunction() const {
        if (call_stack.empty()) {
            return "<none>";
        }
        return call_stack.top().getName();
    }
    
    // Check if stack is empty
    bool isEmpty() const {
        return call_stack.empty();
    }
    
    // Display call history
    void displayHistory() const {
        std::cout << "\n=== Call History ===" << std::endl;
        for (size_t i = 0; i < call_history.size(); ++i) {
            std::cout << (i + 1) << ". " << call_history[i] << std::endl;
        }
    }
    
    // Display current stack
    void displayCurrentStack() const {
        std::cout << "\n=== Current Call Stack ===" << std::endl;
        if (call_stack.empty()) {
            std::cout << "<empty>" << std::endl;
            return;
        }
        
        // Create a copy to display
        std::stack<FunctionCall> temp = call_stack;
        std::vector<std::string> stack_items;
        
        while (!temp.empty()) {
            stack_items.push_back(temp.top().getName());
            temp.pop();
        }
        
        // Display from bottom to top
        for (auto it = stack_items.rbegin(); it != stack_items.rend(); ++it) {
            std::cout << "  " << *it << std::endl;
        }
    }
    
    // Clear all
    void clear() {
        while (!call_stack.empty()) {
            call_stack.pop();
        }
        call_history.clear();
    }
};

// Simulate some recursive functions
void fibonacci(CallStackSimulator& simulator, int n) {
    simulator.enterFunction("fibonacci(" + std::to_string(n) + ")");
    
    // Simulate some work
    std::this_thread::sleep_for(std::chrono::milliseconds(10));
    
    if (n <= 1) {
        simulator.exitFunction();
        return;
    }
    
    fibonacci(simulator, n - 1);
    fibonacci(simulator, n - 2);
    
    simulator.exitFunction();
}

void quickSort(CallStackSimulator& simulator, int arr[], int low, int high) {
    simulator.enterFunction("quickSort([" + std::to_string(low) + ", " + std::to_string(high) + "])");
    
    // Simulate some work
    std::this_thread::sleep_for(std::chrono::milliseconds(5));
    
    if (low < high) {
        // Partition logic would go here
        int pi = low + (high - low) / 2;  // Simplified
        
        quickSort(simulator, arr, low, pi - 1);
        quickSort(simulator, arr, pi + 1, high);
    }
    
    simulator.exitFunction();
}

int main() {
    CallStackSimulator simulator;
    
    std::cout << "=== Function Call Stack Simulator ===" << std::endl;
    
    // Test with fibonacci
    std::cout << "\n=== Fibonacci(4) ===" << std::endl;
    fibonacci(simulator, 4);
    
    simulator.displayCurrentStack();
    simulator.displayHistory();
    
    // Clear and test with quicksort
    simulator.clear();
    
    std::cout << "\n=== QuickSort Simulation ===" << std::endl;
    int arr[] = {3, 6, 8, 10, 1, 2, 1};
    quickSort(simulator, arr, 0, 6);
    
    simulator.displayCurrentStack();
    
    // Test stack operations
    std::cout << "\n=== Manual Stack Operations ===" << std::endl;
    simulator.enterFunction("main()");
    simulator.enterFunction("initialize()");
    simulator.enterFunction("loadConfig()");
    
    std::cout << "Current depth: " << simulator.getCurrentDepth() << std::endl;
    std::cout << "Current function: " << simulator.getCurrentFunction() << std::endl;
    
    simulator.exitFunction();
    std::cout << "Current function: " << simulator.getCurrentFunction() << std::endl;
    
    simulator.enterFunction("setupDatabase()");
    simulator.enterFunction("connect()");
    
    simulator.displayCurrentStack();
    
    // Exit all functions
    std::cout << "\n=== Exiting All Functions ===" << std::endl;
    while (!simulator.isEmpty()) {
        simulator.exitFunction();
    }
    
    return 0;
}
```

### Example 4: Browser History Manager
```cpp
#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>

class BrowserHistory {
private:
    std::stack<std::string> back_stack;
    std::stack<std::string> forward_stack;
    std::string current_page;
    
public:
    BrowserHistory(const std::string& home_page = "about:blank") 
        : current_page(home_page) {}
    
    // Visit a new page
    void visit(const std::string& url) {
        if (!current_page.empty()) {
            back_stack.push(current_page);
        }
        
        current_page = url;
        
        // Clear forward history when visiting new page
        while (!forward_stack.empty()) {
            forward_stack.pop();
        }
        
        std::cout << "Visited: " << url << std::endl;
    }
    
    // Go back to previous page
    bool goBack() {
        if (back_stack.empty()) {
            std::cout << "Cannot go back - no previous pages" << std::endl;
            return false;
        }
        
        // Move current page to forward stack
        forward_stack.push(current_page);
        
        // Move page from back stack to current
        current_page = back_stack.top();
        back_stack.pop();
        
        std::cout << "Went back to: " << current_page << std::endl;
        return true;
    }
    
    // Go forward to next page
    bool goForward() {
        if (forward_stack.empty()) {
            std::cout << "Cannot go forward - no next pages" << std::endl;
            return false;
        }
        
        // Move current page to back stack
        back_stack.push(current_page);
        
        // Move page from forward stack to current
        current_page = forward_stack.top();
        forward_stack.pop();
        
        std::cout << "Went forward to: " << current_page << std::endl;
        return true;
    }
    
    // Get current page
    std::string getCurrentPage() const {
        return current_page;
    }
    
    // Get history sizes
    size_t getBackHistorySize() const { return back_stack.size(); }
    size_t getForwardHistorySize() const { return forward_stack.size(); }
    
    // Get full history as vector
    std::vector<std::string> getFullHistory() const {
        std::vector<std::string> history;
        
        // Get back history (oldest to newest)
        std::stack<std::string> temp_back = back_stack;
        std::vector<std::string> back_items;
        
        while (!temp_back.empty()) {
            back_items.push_back(temp_back.top());
            temp_back.pop();
        }
        
        // Reverse to get correct order
        std::reverse(back_items.begin(), back_items.end());
        
        // Combine all parts
        history.insert(history.end(), back_items.begin(), back_items.end());
        history.push_back(current_page);
        
        // Get forward history
        std::stack<std::string> temp_forward = forward_stack;
        std::vector<std::string> forward_items;
        
        while (!temp_forward.empty()) {
            forward_items.push_back(temp_forward.top());
            temp_forward.pop();
        }
        
        std::reverse(forward_items.begin(), forward_items.end());
        history.insert(history.end(), forward_items.begin(), forward_items.end());
        
        return history;
    }
    
    // Display current state
    void displayState() const {
        std::cout << "\n=== Browser State ===" << std::endl;
        std::cout << "Current page: " << current_page << std::endl;
        std::cout << "Back history: " << getBackHistorySize() << " pages" << std::endl;
        std::cout << "Forward history: " << getForwardHistorySize() << " pages" << std::endl;
    }
    
    // Display full history
    void displayHistory() const {
        auto history = getFullHistory();
        
        std::cout << "\n=== Full History ===" << std::endl;
        for (size_t i = 0; i < history.size(); ++i) {
            std::cout << (i + 1) << ". " << history[i] << std::endl;
        }
    }
    
    // Clear all history
    void clearHistory() {
        while (!back_stack.empty()) back_stack.pop();
        while (!forward_stack.empty()) forward_stack.pop();
        current_page = "about:blank";
        std::cout << "History cleared" << std::endl;
    }
    
    // Check if can go back/forward
    bool canGoBack() const { return !back_stack.empty(); }
    bool canGoForward() const { return !forward_stack.empty(); }
};

int main() {
    BrowserHistory browser("https://example.com");
    
    std::cout << "=== Browser History Manager ===" << std::endl;
    
    // Simulate browsing
    std::cout << "\n=== Simulating Browsing Session ===" << std::endl;
    
    std::vector<std::string> pages = {
        "https://google.com",
        "https://github.com",
        "https://stackoverflow.com",
        "https://cppreference.com"
    };
    
    for (const auto& page : pages) {
        browser.visit(page);
    }
    
    browser.displayState();
    browser.displayHistory();
    
    // Test navigation
    std::cout << "\n=== Testing Navigation ===" << std::endl;
    
    // Go back multiple times
    std::cout << "Going back 3 times:" << std::endl;
    for (int i = 0; i < 3; ++i) {
        browser.goBack();
    }
    
    browser.displayState();
    
    // Go forward
    std::cout << "\nGoing forward 2 times:" << std::endl;
    for (int i = 0; i < 2; ++i) {
        browser.goForward();
    }
    
    browser.displayState();
    
    // Visit new page (should clear forward history)
    std::cout << "\nVisiting new page:" << std::endl;
    browser.visit("https://reddit.com");
    
    std::cout << "Can go forward: " << (browser.canGoForward() ? "Yes" : "No") << std::endl;
    std::cout << "Can go back: " << (browser.canGoBack() ? "Yes" : "No") << std::endl;
    
    browser.displayHistory();
    
    // Test edge cases
    std::cout << "\n=== Testing Edge Cases ===" << std::endl;
    
    // Try to go back beyond history
    std::cout << "Trying to go back beyond history:" << std::endl;
    while (browser.canGoBack()) {
        browser.goBack();
    }
    browser.goBack();  // Should fail
    
    // Try to go forward beyond history
    std::cout << "\nTrying to go forward beyond history:" << std::endl;
    while (browser.canGoForward()) {
        browser.goForward();
    }
    browser.goForward();  // Should fail
    
    return 0;
}
```

## 📊 Complete Function Reference

### Element Access
| Function | Description | Complexity |
|----------|-------------|------------|
| `top()` | Access top element | O(1) |

### Capacity
| Function | Description | Complexity |
|----------|-------------|------------|
| `empty()` | Check if empty | O(1) |
| `size()` | Get number of elements | O(1) |

### Modifiers
| Function | Description | Complexity |
|----------|-------------|------------|
| `push()` | Insert element at top | O(1) |
| `emplace()` | Construct element in place | O(1) |
| `pop()` | Remove top element | O(1) |
| `swap()` | Swap contents | O(1) |

## ⚡ Performance Considerations

### Container Choice
```cpp
// Different underlying containers have different performance characteristics

// std::deque (default) - good all-around performance
std::stack<int> deque_stack;  // O(1) push/pop, good memory locality

// std::vector - better cache locality, may reallocate
std::stack<int, std::vector<int>> vector_stack;  // O(1) amortized push/pop

// std::list - no reallocation, but poor cache locality
std::stack<int, std::list<int>> list_stack;  // O(1) push/pop, scattered memory
```

### Memory Usage
```cpp
// Stack memory usage depends on underlying container
// deque: segmented blocks, good for large stacks
// vector: contiguous memory, may waste space when shrinking
// list: per-node overhead, highest memory usage per element
```

## 🎯 Common Patterns

### Pattern 1: Depth-First Search
```cpp
template<typename T>
void dfsStack(const std::vector<std::vector<T>>& graph, T start) {
    std::stack<T> stack;
    std::unordered_set<T> visited;
    
    stack.push(start);
    
    while (!stack.empty()) {
        T current = stack.top();
        stack.pop();
        
        if (visited.find(current) == visited.end()) {
            visited.insert(current);
            std::cout << "Visited: " << current << std::endl;
            
            // Add neighbors to stack
            for (const T& neighbor : graph[current]) {
                stack.push(neighbor);
            }
        }
    }
}
```

### Pattern 2: Monotonic Stack
```cpp
std::vector<int> nextGreaterElement(const std::vector<int>& nums) {
    std::stack<int> stack;
    std::vector<int> result(nums.size(), -1);
    
    for (int i = nums.size() - 1; i >= 0; --i) {
        while (!stack.empty() && stack.top() <= nums[i]) {
            stack.pop();
        }
        
        if (!stack.empty()) {
            result[i] = stack.top();
        }
        
        stack.push(nums[i]);
    }
    
    return result;
}
```

## 🐛 Common Pitfalls & Solutions

### 1. Accessing Empty Stack
```cpp
// Problem - accessing top of empty stack
std::stack<int> s;
int value = s.top();  // Undefined behavior!

// Solution - always check if empty
if (!s.empty()) {
    int value = s.top();
    // Use value safely
}
```

### 2. No Direct Iteration
```cpp
// Problem - trying to iterate through stack
std::stack<int> s;
for (const auto& item : s) {  // Error: no begin/end
    std::cout << item << std::endl;
}

// Solution - use a copy or different container
std::stack<int> temp = s;
while (!temp.empty()) {
    std::cout << temp.top() << std::endl;
    temp.pop();
}

// Or use the underlying container directly
std::stack<int, std::vector<int>> s;
auto& container = s._Get_container();  // Non-standard
for (const auto& item : container) {
    std::cout << item << std::endl;
}
```

### 3. Choosing Wrong Underlying Container
```cpp
// Problem - using list when vector would be better
std::stack<int, std::list<int>> s;  // Poor cache locality

// Solution - choose appropriate container
std::stack<int> s;  // Uses deque by default - good choice
// Or explicitly:
std::stack<int, std::vector<int>> s;  // Better for cache locality
```

## 📚 Related Headers

- `queue.md` - FIFO container adapter
- `deque.md` - Double-ended queue (default underlying container)
- `vector.md` - Dynamic array (alternative underlying container)
- `list.md` - Doubly linked list (alternative underlying container)

## 🚀 Best Practices

1. **Use default stack** unless you have specific performance requirements
2. **Always check empty()** before calling top() or pop()
3. **Choose underlying container** based on access patterns
4. **Use emplace()** for complex types to avoid unnecessary copies
5. **Consider std::vector** as underlying container for better cache locality
6. **Use std::deque** for balanced performance (default choice)

## 🎯 When to Use stack

✅ **Use stack when:**
- Need LIFO (Last-In, First-Out) behavior
- Implementing algorithms like DFS, backtracking
- Managing function calls or undo/redo systems
- Expression evaluation and parsing
- Browser history navigation
- Need restricted interface (only top access)

❌ **Avoid when:**
- Need random access to elements (use `vector`)
- Need FIFO behavior (use `queue`)
- Need to iterate through all elements
- Need to access elements other than top
- Need to remove elements from middle
---

## Next Step

- Go to [20_queue.md](20_queue.md) to continue with queue.
