# 12_deque.md - Double-Ended Queue Container

The `deque` header provides `std::deque`, a sequence container that supports efficient insertion and deletion at both ends. It stands for "double-ended queue."

## 📖 Overview

`std::deque` (double-ended queue) is a sequence container that provides fast insertion and deletion at both the beginning and end of the container. Unlike `std::vector`, elements are not stored contiguously, but in multiple blocks of memory.

## 🎯 Key Features

- **Double-ended operations** - O(1) insertion/deletion at both ends
- **Dynamic size** - Can grow and shrink as needed
- **Random access** - O(1) element access with `operator[]`
- **Non-contiguous storage** - Elements stored in multiple memory blocks
- **No iterator invalidation** - When adding/removing from ends
- **Memory efficient** - Better memory utilization than vector for growing/shrinking

## 🔧 Basic Deque Operations

### Creating and Initializing Deques
```cpp
#include <iostream>
#include <deque>
#include <algorithm>

int main() {
    // Different ways to create deques
    
    // Empty deque
    std::deque<int> dq1;
    
    // Deque with initial size
    std::deque<int> dq2(5);  // {0, 0, 0, 0, 0}
    
    // Deque with initial size and value
    std::deque<int> dq3(5, 42);  // {42, 42, 42, 42, 42}
    
    // From initializer list
    std::deque<int> dq4 = {1, 2, 3, 4, 5};
    
    // Copy constructor
    std::deque<int> dq5 = dq4;
    
    // From range
    std::deque<int> dq6(dq4.begin(), dq4.end());
    
    return 0;
}
```

### Adding and Removing Elements
```cpp
void demonstrateBasicOperations() {
    std::deque<int> dq;
    
    // Add elements
    dq.push_back(10);   // {10}
    dq.push_front(5);   // {5, 10}
    dq.push_back(15);   // {5, 10, 15}
    dq.push_front(1);   // {1, 5, 10, 15}
    
    std::cout << "After pushes: ";
    for (int val : dq) std::cout << val << " ";
    std::cout << std::endl;
    
    // Access elements
    std::cout << "Front: " << dq.front() << std::endl;  // 1
    std::cout << "Back: " << dq.back() << std::endl;    // 15
    std::cout << "Element at index 2: " << dq[2] << std::endl;  // 10
    
    // Remove elements
    dq.pop_front();    // {5, 10, 15}
    dq.pop_back();     // {5, 10}
    
    std::cout << "After pops: ";
    for (int val : dq) std::cout << val << " ";
    std::cout << std::endl;
}
```

### Iterator Operations
```cpp
void demonstrateIterators() {
    std::deque<std::string> dq = {"apple", "banana", "cherry", "date"};
    
    // Forward iteration
    std::cout << "Forward: ";
    for (auto it = dq.begin(); it != dq.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    
    // Reverse iteration
    std::cout << "Reverse: ";
    for (auto it = dq.rbegin(); it != dq.rend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    
    // Range-based for loop
    std::cout << "Range-based: ";
    for (const auto& fruit : dq) {
        std::cout << fruit << " ";
    }
    std::cout << std::endl;
}
```

## 🔧 Advanced Deque Operations

### Insertion and Erasure
```cpp
void demonstrateInsertErase() {
    std::deque<int> dq = {1, 2, 4, 5};
    
    // Insert at position
    auto it = std::find(dq.begin(), dq.end(), 4);
    dq.insert(it, 3);  // {1, 2, 3, 4, 5}
    
    // Insert multiple elements
    it = dq.begin() + 2;
    dq.insert(it, 2, 99);  // {1, 2, 99, 99, 3, 4, 5}
    
    // Insert from range
    std::deque<int> more = {10, 20, 30};
    dq.insert(dq.end(), more.begin(), more.end());
    
    std::cout << "After insertions: ";
    for (int val : dq) std::cout << val << " ";
    std::cout << std::endl;
    
    // Erase single element
    it = std::find(dq.begin(), dq.end(), 99);
    dq.erase(it);  // Remove first 99
    
    // Erase range
    auto start = std::find(dq.begin(), dq.end(), 3);
    auto end = std::find(dq.begin(), dq.end(), 20);
    dq.erase(start, end);
    
    std::cout << "After erasures: ";
    for (int val : dq) std::cout << val << " ";
    std::cout << std::endl;
}
```

### Resizing and Assignment
```cpp
void demonstrateResize() {
    std::deque<int> dq = {1, 2, 3};
    
    // Resize larger (fills with default value)
    dq.resize(6);  // {1, 2, 3, 0, 0, 0}
    
    // Resize smaller
    dq.resize(4);  // {1, 2, 3, 0}
    
    // Resize with fill value
    dq.resize(7, 42);  // {1, 2, 3, 0, 42, 42, 42}
    
    std::cout << "After resizes: ";
    for (int val : dq) std::cout << val << " ";
    std::cout << std::endl;
    
    // Assignment
    std::deque<int> new_dq = {10, 20, 30};
    dq.assign(new_dq.begin(), new_dq.end());  // {10, 20, 30}
    
    dq.assign(5, 99);  // {99, 99, 99, 99, 99}
    
    std::cout << "After assignments: ";
    for (int val : dq) std::cout << val << " ";
    std::cout << std::endl;
}
```

## 🎮 Practical Examples

### Example 1: Sliding Window Maximum
```cpp
#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>

class SlidingWindow {
private:
    std::deque<std::pair<int, int>> m_window;  // {value, index}
    size_t m_k;
    
public:
    SlidingWindow(size_t k) : m_k(k) {}
    
    void add(int value, int index) {
        // Remove elements smaller than current value
        while (!m_window.empty() && m_window.back().first <= value) {
            m_window.pop_back();
        }
        
        m_window.emplace_back(value, index);
        
        // Remove elements outside window
        while (!m_window.empty() && m_window.front().second <= index - static_cast<int>(m_k)) {
            m_window.pop_front();
        }
    }
    
    int getMax() const {
        if (m_window.empty()) return 0;
        return m_window.front().first;
    }
    
    std::vector<int> getMaximums(const std::vector<int>& nums) {
        std::vector<int> result;
        
        for (size_t i = 0; i < nums.size(); ++i) {
            add(nums[i], i);
            
            if (i >= m_k - 1) {
                result.push_back(getMax());
            }
        }
        
        return result;
    }
};

int main() {
    std::vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    size_t k = 3;
    
    SlidingWindow sw(k);
    auto maxima = sw.getMaximums(nums);
    
    std::cout << "Array: ";
    for (int num : nums) std::cout << num << " ";
    std::cout << std::endl;
    
    std::cout << "Window size: " << k << std::endl;
    std::cout << "Maximums: ";
    for (int max : maxima) std::cout << max << " ";
    std::cout << std::endl;
    
    return 0;
}
```

### Example 2: Task Scheduler with Priority
```cpp
#include <iostream>
#include <deque>
#include <queue>
#include <string>
#include <functional>

class TaskScheduler {
private:
    struct Task {
        int id;
        std::string description;
        int priority;
        
        Task(int i, std::string desc, int prio) 
            : id(i), description(std::move(desc)), priority(prio) {}
        
        bool operator<(const Task& other) const {
            return priority < other.priority;  // Higher priority first
        }
    };
    
    std::deque<Task> m_pending_tasks;
    std::deque<Task> m_completed_tasks;
    std::priority_queue<Task, std::vector<Task>, std::function<bool(const Task&, const Task&)>> 
        m_priority_queue([](const Task& a, const Task& b) { return a < b; });
    
    int m_next_id;
    
public:
    TaskScheduler() : m_priority_queue([](const Task& a, const Task& b) { return a < b; }), 
                     m_next_id(1) {}
    
    // Add task with priority
    int addTask(const std::string& description, int priority) {
        Task task(m_next_id++, description, priority);
        m_pending_tasks.push_back(task);
        m_priority_queue.push(task);
        
        std::cout << "Added task " << task.id << ": " << task.description 
                  << " (priority: " << task.priority << ")" << std::endl;
        
        return task.id;
    }
    
    // Add urgent task to front
    int addUrgentTask(const std::string& description) {
        Task task(m_next_id++, description, 100);
        m_pending_tasks.push_front(task);
        m_priority_queue.push(task);
        
        std::cout << "Added urgent task " << task.id << ": " << task.description << std::endl;
        
        return task.id;
    }
    
    // Get next task by priority
    bool getNextTask(Task& task) {
        if (m_priority_queue.empty()) return false;
        
        task = m_priority_queue.top();
        m_priority_queue.pop();
        
        // Remove from pending queue
        auto it = std::find_if(m_pending_tasks.begin(), m_pending_tasks.end(),
                              [&task](const Task& t) { return t.id == task.id; });
        if (it != m_pending_tasks.end()) {
            m_pending_tasks.erase(it);
        }
        
        return true;
    }
    
    // Complete task
    bool completeTask(int task_id) {
        auto it = std::find_if(m_pending_tasks.begin(), m_pending_tasks.end(),
                              [task_id](const Task& t) { return t.id == task_id; });
        
        if (it != m_pending_tasks.end()) {
            Task task = *it;
            m_pending_tasks.erase(it);
            m_completed_tasks.push_back(task);
            
            std::cout << "Completed task " << task.id << ": " << task.description << std::endl;
            return true;
        }
        
        return false;
    }
    
    // Process tasks by priority
    void processTasks() {
        std::cout << "\n=== Processing Tasks by Priority ===" << std::endl;
        
        Task task;
        while (getNextTask(task)) {
            std::cout << "Processing task " << task.id << ": " << task.description 
                      << " (priority: " << task.priority << ")" << std::endl;
            
            // Simulate task completion
            m_completed_tasks.push_back(task);
        }
    }
    
    // Display pending tasks
    void displayPending() const {
        std::cout << "\n=== Pending Tasks ===" << std::endl;
        if (m_pending_tasks.empty()) {
            std::cout << "No pending tasks." << std::endl;
            return;
        }
        
        for (const auto& task : m_pending_tasks) {
            std::cout << "Task " << task.id << ": " << task.description 
                      << " (priority: " << task.priority << ")" << std::endl;
        }
    }
    
    // Display completed tasks
    void displayCompleted() const {
        std::cout << "\n=== Completed Tasks ===" << std::endl;
        if (m_completed_tasks.empty()) {
            std::cout << "No completed tasks." << std::endl;
            return;
        }
        
        for (const auto& task : m_completed_tasks) {
            std::cout << "Task " << task.id << ": " << task.description 
                      << " (priority: " << task.priority << ")" << std::endl;
        }
    }
    
    // Get statistics
    struct Statistics {
        size_t pending_count;
        size_t completed_count;
        int highest_priority;
        int lowest_priority;
    };
    
    Statistics getStatistics() const {
        Statistics stats = {0, 0, 0, 0};
        
        stats.pending_count = m_pending_tasks.size();
        stats.completed_count = m_completed_tasks.size();
        
        if (!m_pending_tasks.empty()) {
            auto minmax = std::minmax_element(m_pending_tasks.begin(), m_pending_tasks.end(),
                [](const Task& a, const Task& b) { return a.priority < b.priority; });
            
            stats.lowest_priority = minmax.first->priority;
            stats.highest_priority = minmax.second->priority;
        }
        
        return stats;
    }
};

int main() {
    TaskScheduler scheduler;
    
    // Add tasks with different priorities
    scheduler.addTask("Write documentation", 2);
    scheduler.addTask("Fix bug #123", 5);
    scheduler.addTask("Implement feature X", 3);
    scheduler.addUrgentTask("Critical security fix");
    scheduler.addTask("Code review", 1);
    scheduler.addTask("Optimize performance", 4);
    
    scheduler.displayPending();
    
    // Complete some tasks
    std::cout << "\n=== Completing Some Tasks ===" << std::endl;
    scheduler.completeTask(2);  // Fix bug #123
    scheduler.completeTask(5);  // Optimize performance
    
    scheduler.displayPending();
    scheduler.displayCompleted();
    
    // Show statistics
    auto stats = scheduler.getStatistics();
    std::cout << "\n=== Statistics ===" << std::endl;
    std::cout << "Pending tasks: " << stats.pending_count << std::endl;
    std::cout << "Completed tasks: " << stats.completed_count << std::endl;
    std::cout << "Priority range: " << stats.lowest_priority 
              << " to " << stats.highest_priority << std::endl;
    
    // Process remaining tasks
    scheduler.processTasks();
    
    return 0;
}
```

### Example 3: Palindrome Checker
```cpp
#include <iostream>
#include <deque>
#include <string>
#include <cctype>

class PalindromeChecker {
public:
    // Check if string is palindrome (ignoring case and non-alphanumeric)
    static bool isPalindrome(const std::string& text) {
        std::deque<char> chars;
        
        // Filter and normalize characters
        for (char c : text) {
            if (std::isalnum(c)) {
                chars.push_back(std::tolower(c));
            }
        }
        
        // Check palindrome
        while (chars.size() > 1) {
            if (chars.front() != chars.back()) {
                return false;
            }
            chars.pop_front();
            chars.pop_back();
        }
        
        return true;
    }
    
    // Find longest palindrome substring
    static std::string longestPalindromeSubstring(const std::string& text) {
        if (text.empty()) return "";
        
        std::string longest = "";
        
        for (size_t i = 0; i < text.length(); ++i) {
            // Odd length palindromes
            std::string odd = expandAroundCenter(text, i, i);
            if (odd.length() > longest.length()) {
                longest = odd;
            }
            
            // Even length palindromes
            std::string even = expandAroundCenter(text, i, i + 1);
            if (even.length() > longest.length()) {
                longest = even;
            }
        }
        
        return longest;
    }
    
    // Generate all palindrome substrings
    static std::deque<std::string> findAllPalindromes(const std::string& text) {
        std::deque<std::string> palindromes;
        
        for (size_t i = 0; i < text.length(); ++i) {
            for (size_t j = i; j < text.length(); ++j) {
                std::string substring = text.substr(i, j - i + 1);
                if (isPalindrome(substring) && substring.length() > 1) {
                    palindromes.push_back(substring);
                }
            }
        }
        
        return palindromes;
    }
    
private:
    static std::string expandAroundCenter(const std::string& text, int left, int right) {
        while (left >= 0 && right < static_cast<int>(text.length()) && 
               text[left] == text[right]) {
            left--;
            right++;
        }
        
        return text.substr(left + 1, right - left - 1);
    }
};

int main() {
    std::deque<std::string> test_strings = {
        "racecar",
        "A man, a plan, a canal: Panama",
        "hello",
        "madam",
        "Was it a car or a cat I saw?",
        "programming"
    };
    
    std::cout << "=== Palindrome Tests ===" << std::endl;
    for (const auto& text : test_strings) {
        bool is_pal = PalindromeChecker::isPalindrome(text);
        std::cout << "\"" << text << "\" is " 
                  << (is_pal ? "a palindrome" : "not a palindrome") << std::endl;
    }
    
    // Longest palindrome substring
    std::string text = "babad";
    std::string longest = PalindromeChecker::longestPalindromeSubstring(text);
    std::cout << "\nLongest palindrome in \"" << text << "\": \"" << longest << "\"" << std::endl;
    
    // Find all palindromes
    std::string text2 = "ababa";
    auto palindromes = PalindromeChecker::findAllPalindromes(text2);
    std::cout << "\nAll palindromes in \"" << text2 << "\": ";
    for (const auto& pal : palindromes) {
        std::cout << "\"" << pal << "\" ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

### Example 4: Undo/Redo System
```cpp
#include <iostream>
#include <deque>
#include <string>
#include <functional>

class UndoRedoSystem {
private:
    struct Action {
        std::string description;
        std::function<void()> execute;
        std::function<void()> undo;
        
        Action(std::string desc, std::function<void()> exec, std::function<void()> und)
            : description(std::move(desc)), execute(std::move(exec)), undo(std::move(und)) {}
    };
    
    std::deque<Action> m_undo_stack;
    std::deque<Action> m_redo_stack;
    size_t m_max_history;
    
public:
    UndoRedoSystem(size_t max_history = 50) : m_max_history(max_history) {}
    
    // Perform an action
    void performAction(const std::string& description, 
                      std::function<void()> execute, 
                      std::function<void()> undo) {
        
        // Execute the action
        execute();
        
        // Add to undo stack
        m_undo_stack.emplace_front(description, execute, undo);
        
        // Clear redo stack (new action invalidates redo history)
        m_redo_stack.clear();
        
        // Limit history size
        while (m_undo_stack.size() > m_max_history) {
            m_undo_stack.pop_back();
        }
        
        std::cout << "Performed: " << description << std::endl;
    }
    
    // Undo last action
    bool undo() {
        if (m_undo_stack.empty()) {
            std::cout << "Nothing to undo" << std::endl;
            return false;
        }
        
        Action action = m_undo_stack.front();
        m_undo_stack.pop_front();
        
        // Execute undo
        action.undo();
        
        // Add to redo stack
        m_redo_stack.push_front(action);
        
        std::cout << "Undone: " << action.description << std::endl;
        return true;
    }
    
    // Redo last undone action
    bool redo() {
        if (m_redo_stack.empty()) {
            std::cout << "Nothing to redo" << std::endl;
            return false;
        }
        
        Action action = m_redo_stack.front();
        m_redo_stack.pop_front();
        
        // Execute action
        action.execute();
        
        // Add back to undo stack
        m_undo_stack.push_front(action);
        
        std::cout << "Redone: " << action.description << std::endl;
        return true;
    }
    
    // Get available actions
    struct ActionList {
        std::deque<std::string> undo_actions;
        std::deque<std::string> redo_actions;
    };
    
    ActionList getAvailableActions() const {
        ActionList list;
        
        for (const auto& action : m_undo_stack) {
            list.undo_actions.push_back(action.description);
        }
        
        for (const auto& action : m_redo_stack) {
            list.redo_actions.push_back(action.description);
        }
        
        return list;
    }
    
    // Clear history
    void clearHistory() {
        m_undo_stack.clear();
        m_redo_stack.clear();
        std::cout << "History cleared" << std::endl;
    }
    
    // Display history
    void displayHistory() const {
        auto actions = getAvailableActions();
        
        std::cout << "\n=== Undo Stack (" << actions.undo_actions.size() << ") ===" << std::endl;
        if (actions.undo_actions.empty()) {
            std::cout << "Empty" << std::endl;
        } else {
            for (const auto& desc : actions.undo_actions) {
                std::cout << "  " << desc << std::endl;
            }
        }
        
        std::cout << "\n=== Redo Stack (" << actions.redo_actions.size() << ") ===" << std::endl;
        if (actions.redo_actions.empty()) {
            std::cout << "Empty" << std::endl;
        } else {
            for (const auto& desc : actions.redo_actions) {
                std::cout << "  " << desc << std::endl;
            }
        }
    }
};

// Example usage with a simple text editor
class TextEditor {
private:
    std::string m_text;
    UndoRedoSystem m_undo_redo;
    
public:
    TextEditor() : m_text(""), m_undo_redo(20) {}
    
    void insertText(const std::string& text, size_t position) {
        size_t old_length = m_text.length();
        
        m_undo_redo.performAction(
            "Insert '" + text + "' at position " + std::to_string(position),
            
            // Execute
            [this, text, position]() {
                m_text.insert(position, text);
            },
            
            // Undo
            [this, text, position, old_length]() {
                m_text.erase(position, text.length());
            }
        );
    }
    
    void deleteText(size_t position, size_t length) {
        std::string deleted_text = m_text.substr(position, length);
        
        m_undo_redo.performAction(
            "Delete '" + deleted_text + "' at position " + std::to_string(position),
            
            // Execute
            [this, position, length]() {
                m_text.erase(position, length);
            },
            
            // Undo
            [this, deleted_text, position]() {
                m_text.insert(position, deleted_text);
            }
        );
    }
    
    void replaceText(const std::string& old_text, const std::string& new_text) {
        size_t pos = m_text.find(old_text);
        if (pos != std::string::npos) {
            m_undo_redo.performAction(
                "Replace '" + old_text + "' with '" + new_text + "'",
                
                // Execute
                [this, old_text, new_text, pos]() {
                    m_text.replace(pos, old_text.length(), new_text);
                },
                
                // Undo
                [this, old_text, new_text, pos]() {
                    m_text.replace(pos, new_text.length(), old_text);
                }
            );
        }
    }
    
    void undo() { m_undo_redo.undo(); }
    void redo() { m_undo_redo.redo(); }
    void displayHistory() const { m_undo_redo.displayHistory(); }
    
    void displayText() const {
        std::cout << "\nCurrent text: \"" << m_text << "\"" << std::endl;
    }
};

int main() {
    TextEditor editor;
    
    // Perform some editing operations
    editor.insertText("Hello", 0);
    editor.insertText(" world", 5);
    editor.insertText(" beautiful", 6);
    editor.displayText();
    
    editor.replaceText("world", "universe");
    editor.deleteText(6, 10);  // Delete " beautiful"
    editor.displayText();
    
    // Show history
    editor.displayHistory();
    
    // Test undo/redo
    std::cout << "\n=== Testing Undo/Redo ===" << std::endl;
    editor.undo();
    editor.displayText();
    
    editor.undo();
    editor.displayText();
    
    editor.redo();
    editor.displayText();
    
    editor.undo();
    editor.undo();
    editor.undo();
    editor.displayText();
    
    // Try to undo beyond history
    editor.undo();
    
    // Redo everything
    editor.redo();
    editor.redo();
    editor.redo();
    editor.displayText();
    
    return 0;
}
```

## 📊 Complete Function Reference

### Element Access
| Function | Description | Complexity |
|----------|-------------|------------|
| `operator[]` | Random access (no bounds checking) | O(1) |
| `at()` | Random access with bounds checking | O(1) |
| `front()` | Access first element | O(1) |
| `back()` | Access last element | O(1) |

### Modifiers
| Function | Description | Complexity |
|----------|-------------|------------|
| `push_back()` | Add element to end | O(1) amortized |
| `push_front()` | Add element to beginning | O(1) amortized |
| `pop_back()` | Remove element from end | O(1) |
| `pop_front()` | Remove element from beginning | O(1) |
| `insert()` | Insert element at position | O(n) |
| `erase()` | Remove element at position | O(n) |
| `clear()` | Remove all elements | O(n) |
| `resize()` | Change size | O(n) |
| `assign()` | Assign new values | O(n) |

### Capacity
| Function | Description | Complexity |
|----------|-------------|------------|
| `size()` | Number of elements | O(1) |
| `max_size()` | Maximum possible size | O(1) |
| `empty()` | Check if empty | O(1) |
| `shrink_to_fit()` | Reduce memory usage | O(n) |

## ⚡ Performance Considerations

### Memory Layout
```cpp
// deque uses multiple memory blocks
// Better for frequent insertions/deletions at both ends
// Slightly slower random access than vector due to indirection

std::deque<int> dq = {1, 2, 3, 4, 5};
// Elements might be stored in:
// Block 1: [1, 2, 3]
// Block 2: [4, 5]
```

### Iterator Invalidation
```cpp
// Adding/removing from ends: iterators remain valid
// Adding/removing from middle: iterators to erased elements invalid

std::deque<int> dq = {1, 2, 3, 4, 5};
auto it = dq.begin() + 2;  // Points to 3

dq.push_front(0);  // it still valid, points to 3
dq.pop_back();     // it still valid, points to 3
dq.erase(dq.begin() + 1);  // it might be invalidated
```

## 🎯 Common Patterns

### Pattern 1: Double-Ended Queue Operations
```cpp
class WorkQueue {
private:
    std::deque<Task> m_queue;
    
public:
    void addUrgentTask(const Task& task) {
        m_queue.push_front(task);
    }
    
    void addNormalTask(const Task& task) {
        m_queue.push_back(task);
    }
    
    Task getNextTask() {
        Task task = m_queue.front();
        m_queue.pop_front();
        return task;
    }
};
```

### Pattern 2: Sliding Window
```cpp
template<typename T>
class SlidingWindow {
private:
    std::deque<T> m_window;
    size_t m_size;
    
public:
    SlidingWindow(size_t size) : m_size(size) {}
    
    void add(const T& value) {
        m_window.push_back(value);
        if (m_window.size() > m_size) {
            m_window.pop_front();
        }
    }
    
    T getAverage() const {
        T sum = std::accumulate(m_window.begin(), m_window.end(), T{});
        return sum / m_window.size();
    }
};
```

## 🐛 Common Pitfalls & Solutions

### 1. Iterator Invalidation Confusion
```cpp
// Problem
std::deque<int> dq = {1, 2, 3, 4, 5};
auto it = dq.begin() + 2;
dq.insert(dq.begin() + 1, 99);  // it might be invalidated

// Solution
it = dq.begin() + 2;  // Recalculate after modification
```

### 2. Memory Fragmentation
```cpp
// Problem - many small allocations can fragment memory
std::deque<int> dq;
for (int i = 0; i < 100000; ++i) {
    dq.push_back(i);  // May cause many reallocations
}

// Solution - reserve if possible (implementation-dependent)
// Or use vector if memory layout is critical
```

### 3. Performance Misconception
```cpp
// Problem - assuming deque is always faster for insertions
std::deque<int> dq;
dq.insert(dq.begin() + 1000, 42);  // This is O(n), not O(1)

// Solution - use push_front/push_back for O(1) operations
// Use vector for random insertions if memory locality is important
```

## 📚 Related Headers

- `vector.md` - Contiguous dynamic array
- `queue.md` - Queue adapter
- `stack.md` - Stack adapter
- `list.md` - Doubly-linked list

## 🚀 Best Practices

1. **Use deque** when you need frequent insertions at both ends
2. **Prefer vector** for random access and cache locality
3. **Use push_front/push_back** for O(1) operations
4. **Be careful with iterators** after insertions/erasures
5. **Consider memory usage** for very large deques
6. **Use shrink_to_fit()** to reclaim memory after deletions

## 🎯 When to Use deque

✅ **Use deque when:**
- Frequent insertions/deletions at both ends
- Need queue-like operations
- Memory efficiency is important (no overallocation)
- Iterator stability during end operations is needed

❌ **Avoid when:**
- Need contiguous memory (use `vector`)
- Frequent random insertions in middle
- Cache locality is critical
- Memory is extremely constrained

---

**Examples in this file**: 4 complete programs  
**Key Functions**: `push_front()`, `push_back()`, `pop_front()`, `pop_back()`, `front()`, `back()`  
**Time Complexity**: O(1) end operations, O(n) middle insertions  
**Space Complexity**: O(n) where n is number of elements
