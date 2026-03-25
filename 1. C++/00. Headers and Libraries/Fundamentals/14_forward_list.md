# 14_forward_list.md - Singly Linked List

The `forward_list` header provides `std::forward_list`, a singly linked list container that supports only forward iteration with minimal memory overhead.

## 📖 Overview

`std::forward_list` is a container that supports fast insertion and removal of elements anywhere in the sequence, but only allows forward iteration. It's more memory-efficient than `std::list` as it uses only one pointer per node instead of two.

## 🎯 Key Features

- **Singly linked** - Each node has only one pointer (to next node)
- **Forward only iteration** - Cannot traverse backwards
- **Memory efficient** - Uses less memory than `std::list`
- **Fast insertion/deletion** - O(1) after finding position
- **No size tracking** - No `size()` member function for efficiency
- **Constant-time front operations** - `push_front()` and `pop_front()` are O(1)

## 🔧 Basic Forward List Operations

### Creating and Initializing Forward Lists
```cpp
#include <iostream>
#include <forward_list>
#include <algorithm>

int main() {
    // Different ways to create forward lists
    
    // Empty list
    std::forward_list<int> list1;
    
    // From initializer list
    std::forward_list<int> list2 = {1, 2, 3, 4, 5};
    
    // Copy constructor
    std::forward_list<int> list3 = list2;
    
    // Move constructor
    std::forward_list<int> list4 = std::move(list3);
    
    // From range
    std::vector<int> vec = {10, 20, 30};
    std::forward_list<int> list5(vec.begin(), vec.end());
    
    // With default values
    std::forward_list<int> list6(5, 42);  // 5 elements, all value 42
    
    return 0;
}
```

### Front Operations
```cpp
void demonstrateFrontOperations() {
    std::forward_list<int> flist;
    
    // Add elements to front
    flist.push_front(30);
    flist.push_front(20);
    flist.push_front(10);
    
    std::cout << "After push_front operations: ";
    for (int val : flist) std::cout << val << " ";
    std::cout << std::endl;
    
    // Access front element
    std::cout << "Front element: " << flist.front() << std::endl;
    
    // Modify front element
    flist.front() = 99;
    std::cout << "After modifying front: ";
    for (int val : flist) std::cout << val << " ";
    std::cout << std::endl;
    
    // Remove front element
    flist.pop_front();
    std::cout << "After pop_front: ";
    for (int val : flist) std::cout << val << " ";
    std::cout << std::endl;
}
```

### Insertion and Erasure After Position
```cpp
void demonstrateInsertEraseAfter() {
    std::forward_list<int> flist = {10, 20, 40, 50};
    
    std::cout << "Original list: ";
    for (int val : flist) std::cout << val << " ";
    std::cout << std::endl;
    
    // Insert after position
    auto pos = flist.begin();  // Points to 10
    ++pos;  // Points to 20
    flist.insert_after(pos, 30);  // Insert after 20
    
    std::cout << "After insert_after: ";
    for (int val : flist) std::cout << val << " ";
    std::cout << std::endl;
    
    // Insert multiple elements
    pos = flist.begin();
    flist.insert_after(pos, {5, 6, 7});  // Insert after first element
    
    std::cout << "After inserting multiple: ";
    for (int val : flist) std::cout << val << " ";
    std::cout << std::endl;
    
    // Erase after position
    pos = flist.begin();
    ++pos;  // Points to 6
    flist.erase_after(pos);  // Erase element after 6 (which is 7)
    
    std::cout << "After erase_after: ";
    for (int val : flist) std::cout << val << " ";
    std::cout << std::endl;
    
    // Erase range
    auto start = flist.begin();
    auto end = flist.begin();
    std::advance(end, 4);  // Point to 4th element
    flist.erase_after(start, end);  // Erase elements after start up to end
    
    std::cout << "After erase range: ";
    for (int val : flist) std::cout << val << " ";
    std::cout << std::endl;
}
```

## 🔧 Advanced Forward List Operations

### Special Iterators
```cpp
void demonstrateSpecialIterators() {
    std::forward_list<int> flist = {10, 20, 30, 40, 50};
    
    // before_begin() - iterator before first element
    auto before_first = flist.before_begin();
    flist.insert_after(before_first, 5);  // Insert at beginning
    
    std::cout << "After using before_begin: ";
    for (int val : flist) std::cout << val << " ";
    std::cout << std::endl;
    
    // cbefore_begin() - const version
    auto const_before_first = flist.cbefore_begin();
    
    // erase_after with before_begin
    flist.erase_after(flist.before_begin());  // Remove first element
    
    std::cout << "After erase_after(before_begin): ";
    for (int val : flist) std::cout << val << " ";
    std::cout << std::endl;
}
```

### Splicing Operations
```cpp
void demonstrateSplicing() {
    std::forward_list<int> list1 = {1, 2, 3};
    std::forward_list<int> list2 = {4, 5, 6};
    std::forward_list<int> list3 = {7, 8, 9};
    
    std::cout << "List1: ";
    for (int val : list1) std::cout << val << " ";
    std::cout << std::endl;
    
    std::cout << "List2: ";
    for (int val : list2) std::cout << val << " ";
    std::cout << std::endl;
    
    // Splice entire list2 after first element of list1
    auto pos = list1.begin();
    list1.splice_after(pos, list2);  // list2 becomes empty
    
    std::cout << "After splice_after (entire list2):" << std::endl;
    std::cout << "List1: ";
    for (int val : list1) std::cout << val << " ";
    std::cout << std::endl;
    std::cout << "List2 (should be empty): ";
    for (int val : list2) std::cout << val << " ";
    std::cout << std::endl;
    
    // Splice single element
    auto pos3 = list1.begin();
    std::advance(pos3, 2);  // Point to 3rd element
    auto elem_pos = list3.begin();
    list1.splice_after(pos3, list3, elem_pos);  // Move first element of list3
    
    std::cout << "After splice_after (single element):" << std::endl;
    std::cout << "List1: ";
    for (int val : list1) std::cout << val << " ";
    std::cout << std::endl;
    std::cout << "List3: ";
    for (int val : list3) std::cout << val << " ";
    std::cout << std::endl;
}
```

### Size and Operations
```cpp
void demonstrateSizeOperations() {
    std::forward_list<int> flist = {1, 2, 3, 4, 5};
    
    // Calculate size (no size() member function)
    size_t count = std::distance(flist.begin(), flist.end());
    std::cout << "Size using distance: " << count << std::endl;
    
    // Check if empty
    std::cout << "Is empty: " << (flist.empty() ? "Yes" : "No") << std::endl;
    
    // Resize
    flist.resize(3);  // Resize to 3 elements
    std::cout << "After resize(3): ";
    for (int val : flist) std::cout << val << " ";
    std::cout << std::endl;
    
    flist.resize(5, 99);  // Resize to 5, fill new elements with 99
    std::cout << "After resize(5, 99): ";
    for (int val : flist) std::cout << val << " ";
    std::cout << std::endl;
    
    // Clear
    flist.clear();
    std::cout << "After clear - is empty: " << (flist.empty() ? "Yes" : "No") << std::endl;
}
```

## 🎮 Practical Examples

### Example 1: Simple Task Queue
```cpp
#include <iostream>
#include <forward_list>
#include <string>
#include <functional>

class TaskQueue {
private:
    struct Task {
        std::string name;
        std::function<void()> action;
        int priority;
        
        Task(const std::string& n, std::function<void()> a, int p)
            : name(n), action(a), priority(p) {}
    };
    
    std::forward_list<Task> m_tasks;
    
public:
    // Add task to front (highest priority)
    void addTask(const std::string& name, std::function<void()> action, int priority = 0) {
        m_tasks.emplace_front(name, action, priority);
    }
    
    // Add task with priority (insert in correct position)
    void addTaskWithPriority(const std::string& name, std::function<void()> action, int priority) {
        Task new_task(name, action, priority);
        
        if (m_tasks.empty() || m_tasks.front().priority <= priority) {
            m_tasks.emplace_front(name, action, priority);
            return;
        }
        
        // Find correct position
        auto prev = m_tasks.before_begin();
        auto curr = m_tasks.begin();
        
        while (curr != m_tasks.end() && curr->priority > priority) {
            prev = curr;
            ++curr;
        }
        
        m_tasks.insert_after(prev, new_task);
    }
    
    // Execute next task
    bool executeNext() {
        if (m_tasks.empty()) {
            std::cout << "No tasks to execute" << std::endl;
            return false;
        }
        
        Task& task = m_tasks.front();
        std::cout << "Executing task: " << task.name << " (priority: " << task.priority << ")" << std::endl;
        
        try {
            task.action();
            m_tasks.pop_front();
            return true;
        } catch (const std::exception& e) {
            std::cout << "Task failed: " << e.what() << std::endl;
            m_tasks.pop_front();
            return false;
        }
    }
    
    // Execute all tasks
    void executeAll() {
        std::cout << "=== Executing All Tasks ===" << std::endl;
        int executed = 0;
        
        while (executeNext()) {
            executed++;
        }
        
        std::cout << "Executed " << executed << " tasks" << std::endl;
    }
    
    // Remove task by name
    bool removeTask(const std::string& name) {
        auto prev = m_tasks.before_begin();
        auto curr = m_tasks.begin();
        
        while (curr != m_tasks.end()) {
            if (curr->name == name) {
                m_tasks.erase_after(prev);
                std::cout << "Removed task: " << name << std::endl;
                return true;
            }
            prev = curr;
            ++curr;
        }
        
        return false;
    }
    
    // Get number of tasks
    size_t getTaskCount() const {
        return std::distance(m_tasks.begin(), m_tasks.end());
    }
    
    // Display tasks
    void displayTasks() const {
        std::cout << "Task Queue (" << getTaskCount() << " tasks):" << std::endl;
        
        for (const auto& task : m_tasks) {
            std::cout << "  " << task.name << " (priority: " << task.priority << ")" << std::endl;
        }
    }
    
    // Clear all tasks
    void clear() {
        m_tasks.clear();
    }
};

int main() {
    TaskQueue queue;
    
    std::cout << "=== Task Queue Demo ===" << std::endl;
    
    // Add some tasks
    queue.addTask("Initialize", []() {
        std::cout << "  Initializing system..." << std::endl;
    }, 1);
    
    queue.addTask("Load Data", []() {
        std::cout << "  Loading data from file..." << std::endl;
    }, 2);
    
    queue.addTask("Process", []() {
        std::cout << "  Processing data..." << std::endl;
    }, 3);
    
    queue.addTaskWithPriority("Critical Task", []() {
        std::cout << "  Executing critical task!" << std::endl;
    }, 10);
    
    queue.displayTasks();
    
    // Execute one task
    std::cout << "\n=== Execute One Task ===" << std::endl;
    queue.executeNext();
    queue.displayTasks();
    
    // Remove a task
    std::cout << "\n=== Remove Task ===" << std::endl;
    queue.removeTask("Load Data");
    queue.displayTasks();
    
    // Execute all remaining tasks
    std::cout << "\n=== Execute All Tasks ===" << std::endl;
    queue.executeAll();
    
    return 0;
}
```

### Example 2: Simple Hash Table with Chaining
```cpp
#include <iostream>
#include <forward_list>
#include <vector>
#include <functional>
#include <string>

template<typename K, typename V>
class SimpleHashTable {
private:
    struct Entry {
        K key;
        V value;
        
        Entry(const K& k, const V& v) : key(k), value(v) {}
    };
    
    std::vector<std::forward_list<Entry>> m_buckets;
    size_t m_size;
    std::hash<K> m_hasher;
    
    size_t getBucketIndex(const K& key) const {
        return m_hasher(key) % m_buckets.size();
    }
    
public:
    SimpleHashTable(size_t initial_capacity = 16) : m_size(0) {
        m_buckets.resize(initial_capacity);
    }
    
    // Insert or update key-value pair
    void insert(const K& key, const V& value) {
        size_t bucket_idx = getBucketIndex(key);
        auto& bucket = m_buckets[bucket_idx];
        
        // Check if key already exists
        for (Entry& entry : bucket) {
            if (entry.key == key) {
                entry.value = value;
                return;
            }
        }
        
        // Insert new entry
        bucket.emplace_front(key, value);
        m_size++;
        
        // Check if rehashing is needed
        if (static_cast<double>(m_size) / m_buckets.size() > 0.75) {
            rehash(m_buckets.size() * 2);
        }
    }
    
    // Find value by key
    std::optional<V> find(const K& key) const {
        size_t bucket_idx = getBucketIndex(key);
        const auto& bucket = m_buckets[bucket_idx];
        
        for (const Entry& entry : bucket) {
            if (entry.key == key) {
                return entry.value;
            }
        }
        
        return std::nullopt;
    }
    
    // Remove key-value pair
    bool remove(const K& key) {
        size_t bucket_idx = getBucketIndex(key);
        auto& bucket = m_buckets[bucket_idx];
        
        auto prev = bucket.before_begin();
        auto curr = bucket.begin();
        
        while (curr != bucket.end()) {
            if (curr->key == key) {
                bucket.erase_after(prev);
                m_size--;
                return true;
            }
            prev = curr;
            ++curr;
        }
        
        return false;
    }
    
    // Check if key exists
    bool contains(const K& key) const {
        return find(key).has_value();
    }
    
    // Get number of elements
    size_t size() const {
        return m_size;
    }
    
    // Check if empty
    bool empty() const {
        return m_size == 0;
    }
    
    // Rehash to new capacity
    void rehash(size_t new_capacity) {
        std::vector<std::forward_list<Entry>> new_buckets(new_capacity);
        std::hash<K> new_hasher;
        
        // Move all entries to new buckets
        for (auto& bucket : m_buckets) {
            for (Entry& entry : bucket) {
                size_t new_bucket_idx = new_hasher(entry.key) % new_capacity;
                new_buckets[new_bucket_idx].emplace_front(entry.key, entry.value);
            }
        }
        
        m_buckets = std::move(new_buckets);
        m_hasher = new_hasher;
    }
    
    // Get statistics
    struct Statistics {
        size_t total_elements;
        size_t bucket_count;
        size_t used_buckets;
        double load_factor;
        size_t max_chain_length;
        double average_chain_length;
    };
    
    Statistics getStatistics() const {
        Statistics stats = {0, 0, 0, 0.0, 0, 0.0};
        
        stats.total_elements = m_size;
        stats.bucket_count = m_buckets.size();
        stats.load_factor = static_cast<double>(m_size) / m_buckets.size();
        
        size_t total_chain_length = 0;
        
        for (const auto& bucket : m_buckets) {
            size_t chain_length = std::distance(bucket.begin(), bucket.end());
            if (chain_length > 0) {
                stats.used_buckets++;
                total_chain_length += chain_length;
                stats.max_chain_length = std::max(stats.max_chain_length, chain_length);
            }
        }
        
        if (stats.used_buckets > 0) {
            stats.average_chain_length = static_cast<double>(total_chain_length) / stats.used_buckets;
        }
        
        return stats;
    }
    
    // Display hash table
    void display() const {
        std::cout << "Hash Table (size: " << m_size << ", buckets: " << m_buckets.size() << ")" << std::endl;
        
        for (size_t i = 0; i < m_buckets.size(); ++i) {
            const auto& bucket = m_buckets[i];
            if (!bucket.empty()) {
                std::cout << "Bucket " << i << ": ";
                for (const Entry& entry : bucket) {
                    std::cout << "[" << entry.key << ": " << entry.value << "] ";
                }
                std::cout << std::endl;
            }
        }
    }
    
    // Clear all elements
    void clear() {
        for (auto& bucket : m_buckets) {
            bucket.clear();
        }
        m_size = 0;
    }
};

int main() {
    SimpleHashTable<std::string, int> hash_table;
    
    std::cout << "=== Simple Hash Table Demo ===" << std::endl;
    
    // Insert some key-value pairs
    hash_table.insert("apple", 5);
    hash_table.insert("banana", 3);
    hash_table.insert("cherry", 8);
    hash_table.insert("date", 2);
    hash_table.insert("elderberry", 7);
    
    hash_table.display();
    
    // Test lookups
    std::cout << "\n=== Lookup Tests ===" << std::endl;
    
    std::vector<std::string> test_keys = {"apple", "banana", "fig"};
    for (const auto& key : test_keys) {
        auto value = hash_table.find(key);
        if (value) {
            std::cout << key << " -> " << *value << std::endl;
        } else {
            std::cout << key << " not found" << std::endl;
        }
    }
    
    // Test update
    std::cout << "\n=== Update Test ===" << std::endl;
    hash_table.insert("apple", 10);  // Update existing key
    auto updated_value = hash_table.find("apple");
    if (updated_value) {
        std::cout << "Updated apple -> " << *updated_value << std::endl;
    }
    
    // Test removal
    std::cout << "\n=== Removal Test ===" << std::endl;
    bool removed = hash_table.remove("banana");
    std::cout << "Removed banana: " << (removed ? "Yes" : "No") << std::endl;
    
    removed = hash_table.remove("fig");  // Non-existent
    std::cout << "Removed fig: " << (removed ? "Yes" : "No") << std::endl;
    
    hash_table.display();
    
    // Show statistics
    auto stats = hash_table.getStatistics();
    std::cout << "\n=== Statistics ===" << std::endl;
    std::cout << "Total elements: " << stats.total_elements << std::endl;
    std::cout << "Bucket count: " << stats.bucket_count << std::endl;
    std::cout << "Used buckets: " << stats.used_buckets << std::endl;
    std::cout << "Load factor: " << std::fixed << std::setprecision(2) << stats.load_factor << std::endl;
    std::cout << "Max chain length: " << stats.max_chain_length << std::endl;
    std::cout << "Average chain length: " << std::fixed << std::setprecision(2) << stats.average_chain_length << std::endl;
    
    // Test with many elements to trigger rehashing
    std::cout << "\n=== Stress Test ===" << std::endl;
    for (int i = 0; i < 50; ++i) {
        hash_table.insert("key_" + std::to_string(i), i);
    }
    
    auto final_stats = hash_table.getStatistics();
    std::cout << "After adding 50 elements:" << std::endl;
    std::cout << "Total elements: " << final_stats.total_elements << std::endl;
    std::cout << "Bucket count: " << final_stats.bucket_count << std::endl;
    std::cout << "Load factor: " << std::fixed << std::setprecision(2) << final_stats.load_factor << std::endl;
    
    return 0;
}
```

### Example 3: Undo/Redo System
```cpp
#include <iostream>
#include <forward_list>
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
    
    std::forward_list<Action> m_undo_stack;
    std::forward_list<Action> m_redo_stack;
    size_t m_max_history;
    
public:
    UndoRedoSystem(size_t max_history = 50) : m_max_history(max_history) {}
    
    // Add action to history
    void addAction(const std::string& description, 
                  std::function<void()> execute, 
                  std::function<void()> undo) {
        
        // Execute the action
        execute();
        
        // Add to undo stack
        m_undo_stack.emplace_front(description, execute, undo);
        
        // Clear redo stack (new action invalidates redo history)
        m_redo_stack.clear();
        
        // Limit history size
        limitHistorySize();
        
        std::cout << "Executed: " << description << std::endl;
    }
    
    // Undo last action
    bool undo() {
        if (m_undo_stack.empty()) {
            std::cout << "Nothing to undo" << std::endl;
            return false;
        }
        
        Action& action = m_undo_stack.front();
        
        try {
            action.undo();
            std::cout << "Undone: " << action.description << std::endl;
            
            // Move to redo stack
            m_redo_stack.emplace_front(action.description, action.execute, action.undo);
            m_undo_stack.pop_front();
            
            return true;
        } catch (const std::exception& e) {
            std::cout << "Undo failed: " << e.what() << std::endl;
            return false;
        }
    }
    
    // Redo last undone action
    bool redo() {
        if (m_redo_stack.empty()) {
            std::cout << "Nothing to redo" << std::endl;
            return false;
        }
        
        Action& action = m_redo_stack.front();
        
        try {
            action.execute();
            std::cout << "Redone: " << action.description << std::endl;
            
            // Move back to undo stack
            m_undo_stack.emplace_front(action.description, action.execute, action.undo);
            m_redo_stack.pop_front();
            
            return true;
        } catch (const std::exception& e) {
            std::cout << "Redo failed: " << e.what() << std::endl;
            return false;
        }
    }
    
    // Get undo history size
    size_t getUndoCount() const {
        return std::distance(m_undo_stack.begin(), m_undo_stack.end());
    }
    
    // Get redo history size
    size_t getRedoCount() const {
        return std::distance(m_redo_stack.begin(), m_redo_stack.end());
    }
    
    // Display history
    void displayHistory() const {
        std::cout << "\n=== History ===" << std::endl;
        std::cout << "Undo stack (" << getUndoCount() << " items):" << std::endl;
        
        int count = 0;
        for (const auto& action : m_undo_stack) {
            std::cout << "  " << count++ << ". " << action.description << std::endl;
        }
        
        std::cout << "Redo stack (" << getRedoCount() << " items):" << std::endl;
        count = 0;
        for (const auto& action : m_redo_stack) {
            std::cout << "  " << count++ << ". " << action.description << std::endl;
        }
    }
    
    // Clear all history
    void clear() {
        m_undo_stack.clear();
        m_redo_stack.clear();
        std::cout << "History cleared" << std::endl;
    }
    
private:
    void limitHistorySize() {
        size_t current_size = std::distance(m_undo_stack.begin(), m_undo_stack.end());
        
        while (current_size > m_max_history) {
            // Find the last element and remove it
            auto prev = m_undo_stack.before_begin();
            auto curr = m_undo_stack.begin();
            auto next = curr;
            ++next;
            
            while (next != m_undo_stack.end()) {
                prev = curr;
                curr = next;
                ++next;
            }
            
            m_undo_stack.erase_after(prev);
            current_size--;
        }
    }
};

int main() {
    UndoRedoSystem undo_redo;
    
    std::cout << "=== Undo/Redo System Demo ===" << std::endl;
    
    // Simulate a text editor with undo/redo
    std::string text = "";
    
    // Add some actions
    undo_redo.addAction("Type 'Hello'", 
        [&text]() { text += "Hello"; },
        [&text]() { text = text.substr(0, text.length() - 5); });
    
    undo_redo.addAction("Type ' World'", 
        [&text]() { text += " World"; },
        [&text]() { text = text.substr(0, text.length() - 6); });
    
    undo_redo.addAction("Type '!'", 
        [&text]() { text += "!"; },
        [&text]() { text = text.substr(0, text.length() - 1); });
    
    std::cout << "Current text: \"" << text << "\"" << std::endl;
    undo_redo.displayHistory();
    
    // Test undo
    std::cout << "\n=== Testing Undo ===" << std::endl;
    undo_redo.undo();
    std::cout << "Current text: \"" << text << "\"" << std::endl;
    
    undo_redo.undo();
    std::cout << "Current text: \"" << text << "\"" << std::endl;
    
    // Test redo
    std::cout << "\n=== Testing Redo ===" << std::endl;
    undo_redo.redo();
    std::cout << "Current text: \"" << text << "\"" << std::endl;
    
    // Add new action (should clear redo stack)
    std::cout << "\n=== Adding New Action ===" << std::endl;
    undo_redo.addAction("Type ' C++'", 
        [&text]() { text += " C++"; },
        [&text]() { text = text.substr(0, text.length() - 4); });
    
    std::cout << "Current text: \"" << text << "\"" << std::endl;
    undo_redo.displayHistory();
    
    // Try to redo (should fail)
    std::cout << "\n=== Testing Redo After New Action ===" << std::endl;
    undo_redo.redo();
    
    // Undo all
    std::cout << "\n=== Undo All ===" << std::endl;
    while (undo_redo.undo()) {
        // Continue undoing
    }
    std::cout << "Current text: \"" << text << "\"" << std::endl;
    
    // Redo all
    std::cout << "\n=== Redo All ===" << std::endl;
    while (undo_redo.redo()) {
        // Continue redoing
    }
    std::cout << "Current text: \"" << text << "\"" << std::endl;
    
    return 0;
}
```

### Example 4: Memory Pool Allocator
```cpp
#include <iostream>
#include <forward_list>
#include <memory>
#include <vector>

template<typename T>
class MemoryPool {
private:
    struct Block {
        alignas(T) char data[sizeof(T)];
        Block* next;
    };
    
    std::forward_list<Block> m_blocks;
    std::forward_list<Block*> m_free_blocks;
    size_t m_pool_size;
    
public:
    MemoryPool(size_t initial_size = 64) : m_pool_size(initial_size) {
        // Allocate initial blocks
        for (size_t i = 0; i < initial_size; ++i) {
            m_blocks.emplace_front();
            m_free_blocks.emplace_front(&m_blocks.front());
        }
    }
    
    // Allocate memory for one object
    T* allocate() {
        if (m_free_blocks.empty()) {
            // Expand pool if no free blocks
            expandPool();
        }
        
        Block* block = m_free_blocks.front();
        m_free_blocks.pop_front();
        
        return reinterpret_cast<T*>(block->data);
    }
    
    // Deallocate memory
    void deallocate(T* ptr) {
        if (!ptr) return;
        
        Block* block = reinterpret_cast<Block*>(ptr);
        m_free_blocks.emplace_front(block);
    }
    
    // Get pool statistics
    struct Statistics {
        size_t total_blocks;
        size_t free_blocks;
        size_t used_blocks;
        double utilization;
    };
    
    Statistics getStatistics() const {
        Statistics stats = {0, 0, 0, 0.0};
        
        stats.total_blocks = m_pool_size;
        stats.free_blocks = std::distance(m_free_blocks.begin(), m_free_blocks.end());
        stats.used_blocks = stats.total_blocks - stats.free_blocks;
        
        if (stats.total_blocks > 0) {
            stats.utilization = static_cast<double>(stats.used_blocks) / stats.total_blocks;
        }
        
        return stats;
    }
    
    // Reset pool (deallocate all objects)
    void reset() {
        m_free_blocks.clear();
        
        // Add all blocks back to free list
        for (Block& block : m_blocks) {
            m_free_blocks.emplace_front(&block);
        }
    }
    
private:
    void expandPool() {
        size_t expand_size = m_pool_size / 2;  // Expand by 50%
        if (expand_size == 0) expand_size = 1;
        
        for (size_t i = 0; i < expand_size; ++i) {
            m_blocks.emplace_front();
            m_free_blocks.emplace_front(&m_blocks.front());
        }
        
        m_pool_size += expand_size;
        std::cout << "Expanded pool by " << expand_size << " blocks" << std::endl;
    }
};

// Custom allocator using memory pool
template<typename T>
class PoolAllocator {
private:
    MemoryPool<T>* m_pool;
    
public:
    using value_type = T;
    
    PoolAllocator(MemoryPool<T>& pool) : m_pool(&pool) {}
    
    template<typename U>
    PoolAllocator(const PoolAllocator<U>& other) : m_pool(other.getPool()) {}
    
    T* allocate(size_t n) {
        if (n != 1) {
            throw std::bad_alloc();
        }
        return m_pool->allocate();
    }
    
    void deallocate(T* ptr, size_t n) {
        m_pool->deallocate(ptr);
    }
    
    MemoryPool<T>* getPool() const { return m_pool; }
};

int main() {
    std::cout << "=== Memory Pool Demo ===" << std::endl;
    
    MemoryPool<int> pool(10);
    
    // Test basic allocation/deallocation
    std::cout << "\n=== Basic Allocation Test ===" << std::endl;
    
    std::vector<int*> pointers;
    
    // Allocate some objects
    for (int i = 0; i < 15; ++i) {  // More than initial pool size
        int* ptr = pool.allocate();
        *ptr = i * 10;
        pointers.push_back(ptr);
    }
    
    auto stats = pool.getStatistics();
    std::cout << "After allocating 15 objects:" << std::endl;
    std::cout << "Total blocks: " << stats.total_blocks << std::endl;
    std::cout << "Used blocks: " << stats.used_blocks << std::endl;
    std::cout << "Utilization: " << (stats.utilization * 100) << "%" << std::endl;
    
    // Display allocated values
    std::cout << "Allocated values: ";
    for (int* ptr : pointers) {
        std::cout << *ptr << " ";
    }
    std::cout << std::endl;
    
    // Deallocate some objects
    std::cout << "\n=== Deallocation Test ===" << std::endl;
    
    for (int i = 0; i < 5; ++i) {
        pool.deallocate(pointers[i]);
    }
    
    pointers.erase(pointers.begin(), pointers.begin() + 5);
    
    stats = pool.getStatistics();
    std::cout << "After deallocating 5 objects:" << std::endl;
    std::cout << "Used blocks: " << stats.used_blocks << std::endl;
    std::cout << "Free blocks: " << stats.free_blocks << std::endl;
    std::cout << "Utilization: " << (stats.utilization * 100) << "%" << std::endl;
    
    // Test with STL container
    std::cout << "\n=== STL Container Test ===" << std::endl;
    
    // Reset pool
    pool.reset();
    
    // Create forward_list with custom allocator
    std::forward_list<int, PoolAllocator<int>> flist(PoolAllocator<int>(pool));
    
    // Add elements
    for (int i = 0; i < 10; ++i) {
        flist.push_front(i * 100);
    }
    
    std::cout << "Forward list elements: ";
    for (int val : flist) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    
    stats = pool.getStatistics();
    std::cout << "Pool utilization after STL use: " << (stats.utilization * 100) << "%" << std::endl;
    
    // Test performance comparison
    std::cout << "\n=== Performance Comparison ===" << std::endl;
    
    const int iterations = 10000;
    
    // Test with memory pool
    auto start = std::chrono::high_resolution_clock::now();
    
    std::vector<int*> pool_pointers;
    for (int i = 0; i < iterations; ++i) {
        int* ptr = pool.allocate();
        *ptr = i;
        pool_pointers.push_back(ptr);
    }
    
    for (int* ptr : pool_pointers) {
        pool.deallocate(ptr);
    }
    
    auto end = std::chrono::high_resolution_clock::now();
    auto pool_duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    std::cout << "Memory pool: " << pool_duration.count() << " microseconds" << std::endl;
    
    return 0;
}
```

## 📊 Complete Function Reference

### Element Access
| Function | Description | Complexity |
|----------|-------------|------------|
| `front()` | Access first element | O(1) |

### Modifiers
| Function | Description | Complexity |
|----------|-------------|------------|
| `push_front()` | Insert element at beginning | O(1) |
| `pop_front()` | Remove first element | O(1) |
| `insert_after()` | Insert after position | O(1) |
| `emplace_front()` | Construct element at beginning | O(1) |
| `emplace_after()` | Construct element after position | O(1) |
| `erase_after()` | Erase element after position | O(1) |
| `resize()` | Change size | O(n) |
| `clear()` | Clear all elements | O(n) |
| `swap()` | Swap contents | O(1) |

### Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `splice_after()` | Transfer elements from another list | O(1) |
| `remove()` | Remove elements equal to value | O(n) |
| `remove_if()` | Remove elements satisfying condition | O(n) |
| `unique()` | Remove consecutive duplicates | O(n) |
| `merge()` | Merge sorted lists | O(n) |
| `sort()` | Sort elements | O(n log n) |
| `reverse()` | Reverse order | O(n) |

### Iterators
| Function | Description | Complexity |
|----------|-------------|------------|
| `before_begin()` | Iterator before first element | O(1) |
| `cbefore_begin()` | Const iterator before first element | O(1) |

## ⚡ Performance Considerations

### Memory Layout
```cpp
// Forward list node structure (simplified)
template<typename T>
struct ForwardListNode {
    T value;
    ForwardListNode* next;  // Only one pointer!
};

// Memory usage comparison:
// std::list:     value + prev_ptr + next_ptr
// std::forward_list: value + next_ptr  (saves one pointer per node)
```

### Iterator Invalidation
```cpp
// Forward list iterators remain valid except for erased elements
std::forward_list<int> flist = {1, 2, 3, 4};
auto it = flist.begin();
++it;  // Points to 2

flist.erase_after(flist.begin());  // Removes 2
// it is now invalid

flist.push_front(0);  // it still invalid
```

## 🎯 Common Patterns

### Pattern 1: LIFO Stack
```cpp
template<typename T>
class Stack {
private:
    std::forward_list<T> m_data;
    
public:
    void push(const T& value) {
        m_data.push_front(value);
    }
    
    void pop() {
        m_data.pop_front();
    }
    
    T& top() {
        return m_data.front();
    }
    
    bool empty() const {
        return m_data.empty();
    }
};
```

### Pattern 2: Singly Linked List Implementation
```cpp
template<typename T>
class SinglyLinkedList {
private:
    struct Node {
        T data;
        Node* next;
    };
    
    Node* head;
    
public:
    void insert_front(const T& value) {
        Node* new_node = new Node{value, head};
        head = new_node;
    }
    
    void remove_front() {
        if (head) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }
};
```

## 🐛 Common Pitfalls & Solutions

### 1. No size() Member Function
```cpp
// Problem - trying to get size directly
std::forward_list<int> flist = {1, 2, 3};
size_t size = flist.size();  // Error: no size() member

// Solution - use distance()
size_t size = std::distance(flist.begin(), flist.end());

// Or maintain size separately
class SizedForwardList {
    std::forward_list<int> m_list;
    size_t m_size = 0;
public:
    void push_front(int value) {
        m_list.push_front(value);
        ++m_size;
    }
    
    size_t size() const { return m_size; }
};
```

### 2. Cannot Insert at Arbitrary Position
```cpp
// Problem - trying to insert at position
std::forward_list<int> flist = {1, 2, 4};
auto it = flist.begin();
std::advance(it, 2);  // Points to 4
flist.insert(it, 3);  // Error: no insert() member

// Solution - use insert_after()
auto pos = flist.begin();
std::advance(pos, 1);  // Points to 2
flist.insert_after(pos, 3);  // Insert after 2
```

### 3. No Backward Iteration
```cpp
// Problem - trying to go backwards
std::forward_list<int> flist = {1, 2, 3};
auto it = flist.end();
--it;  // Error: bidirectional iterator required

// Solution - use std::list or store previous positions
// Or use algorithms that work with forward iterators
```

## 📚 Related Headers

- `list.md` - Doubly linked list
- `vector.md` - Dynamic array
- `deque.md` - Double-ended queue
- `iterator.md` - Iterator utilities

## 🚀 Best Practices

1. **Use forward_list** when memory is constrained and only forward iteration is needed
2. **Prefer push_front/pop_front** for O(1) operations
3. **Use insert_after/erase_after** instead of trying to insert/erase at positions
4. **Calculate size with distance()** when needed
5. **Consider std::list** if you need bidirectional iteration
6. **Use before_begin()** for efficient insertion at the front

## 🎯 When to Use forward_list

✅ **Use forward_list when:**
- Memory usage is critical
- Only forward iteration is needed
- Frequent insertions/deletions at the front
- LIFO (stack) behavior is required
- Cache-friendly memory access is important

❌ **Avoid when:**
- Need bidirectional iteration (use `list`)
- Need random access (use `vector`)
- Need size() frequently (use `list` or track manually)
- Need to insert/erase at arbitrary positions frequently

---

**Examples in this file**: 4 complete programs  
**Key Functions**: `push_front()`, `pop_front()`, `insert_after()`, `erase_after()`, `before_begin()`, `splice_after()`  
**Time Complexity**: O(1) for front operations, O(n) for search  
**Space Complexity**: O(n) where n is number of elements
