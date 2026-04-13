# 13_list.md - Doubly Linked List Container

The `list` header provides `std::list`, a doubly linked list container that supports constant-time insertion and removal of elements anywhere in the sequence.

## 📖 Overview

`std::list` is a sequence container that stores elements in non-contiguous memory locations, with each element containing pointers to its previous and next elements. This provides excellent performance for insertions and deletions but slower random access.

## 🎯 Key Features

- **Bidirectional iterators** - Can traverse both forward and backward
- **Constant-time insert/erase** - O(1) insertion/deletion anywhere
- **Stable iterators** - Iterators remain valid when other elements are modified
- **No reallocation** - Elements never move after insertion
- **Efficient splicing** - Can transfer elements between lists efficiently
- **Member-specific algorithms** - Optimized sort, merge, unique operations

## 🔧 Basic List Operations

### Creating and Initializing Lists
```cpp
#include <iostream>
#include <list>
#include <algorithm>

int main() {
    // Different ways to create lists
    
    // Empty list
    std::list<int> lst1;
    
    // List with initial size
    std::list<int> lst2(5);  // {0, 0, 0, 0, 0}
    
    // List with initial size and value
    std::list<int> lst3(5, 42);  // {42, 42, 42, 42, 42}
    
    // From initializer list
    std::list<int> lst4 = {1, 2, 3, 4, 5};
    
    // Copy constructor
    std::list<int> lst5 = lst4;
    
    // From range
    std::list<int> lst6(lst4.begin(), lst4.end());
    
    return 0;
}
```

### Adding and Removing Elements
```cpp
void demonstrateBasicOperations() {
    std::list<int> lst;
    
    // Add elements
    lst.push_back(10);   // {10}
    lst.push_front(5);   // {5, 10}
    lst.push_back(15);   // {5, 10, 15}
    lst.push_front(1);   // {1, 5, 10, 15}
    
    std::cout << "After pushes: ";
    for (int val : lst) std::cout << val << " ";
    std::cout << std::endl;
    
    // Access elements
    std::cout << "Front: " << lst.front() << std::endl;  // 1
    std::cout << "Back: " << lst.back() << std::endl;    // 15
    
    // Remove elements
    lst.pop_front();    // {5, 10, 15}
    lst.pop_back();     // {5, 10}
    
    std::cout << "After pops: ";
    for (int val : lst) std::cout << val << " ";
    std::cout << std::endl;
}
```

### Iterator Operations
```cpp
void demonstrateIterators() {
    std::list<std::string> lst = {"apple", "banana", "cherry", "date"};
    
    // Forward iteration
    std::cout << "Forward: ";
    for (auto it = lst.begin(); it != lst.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    
    // Reverse iteration
    std::cout << "Reverse: ";
    for (auto it = lst.rbegin(); it != lst.rend(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    
    // Range-based for loop
    std::cout << "Range-based: ";
    for (const auto& fruit : lst) {
        std::cout << fruit << " ";
    }
    std::cout << std::endl;
}
```

## 🔧 Advanced List Operations

### Insertion and Erasure
```cpp
void demonstrateInsertErase() {
    std::list<int> lst = {1, 2, 4, 5};
    
    // Insert at position
    auto it = std::find(lst.begin(), lst.end(), 4);
    lst.insert(it, 3);  // {1, 2, 3, 4, 5}
    
    // Insert multiple elements
    it = std::next(lst.begin(), 2);
    lst.insert(it, 2, 99);  // {1, 2, 99, 99, 3, 4, 5}
    
    // Insert from range
    std::list<int> more = {10, 20, 30};
    lst.insert(lst.end(), more.begin(), more.end());
    
    std::cout << "After insertions: ";
    for (int val : lst) std::cout << val << " ";
    std::cout << std::endl;
    
    // Erase single element
    it = std::find(lst.begin(), lst.end(), 99);
    lst.erase(it);  // Remove first 99
    
    // Erase range
    auto start = std::find(lst.begin(), lst.end(), 3);
    auto end = std::find(lst.begin(), lst.end(), 20);
    lst.erase(start, end);
    
    std::cout << "After erasures: ";
    for (int val : lst) std::cout << val << " ";
    std::cout << std::endl;
}
```

### Splicing Operations
```cpp
void demonstrateSplice() {
    std::list<int> list1 = {1, 2, 3};
    std::list<int> list2 = {4, 5, 6};
    std::list<int> list3 = {7, 8, 9};
    
    std::cout << "Initial lists:" << std::endl;
    std::cout << "List1: ";
    for (int val : list1) std::cout << val << " ";
    std::cout << std::endl;
    
    // Move entire list2 to position in list1
    auto pos = std::next(list1.begin());
    list1.splice(pos, list2);  // list1: {1, 4, 5, 6, 2, 3}, list2: {}
    
    std::cout << "After splicing list2 into list1:" << std::endl;
    std::cout << "List1: ";
    for (int val : list1) std::cout << val << " ";
    std::cout << std::endl;
    std::cout << "List2: ";
    for (int val : list2) std::cout << val << " ";
    std::cout << std::endl;
    
    // Move single element from list3 to list1
    auto it = std::next(list3.begin());  // Points to 8
    list1.splice(list1.end(), list3, it);  // Move 8 to end of list1
    
    std::cout << "After moving element from list3:" << std::endl;
    std::cout << "List1: ";
    for (int val : list1) std::cout << val << " ";
    std::cout << std::endl;
    std::cout << "List3: ";
    for (int val : list3) std::cout << val << " ";
    std::cout << std::endl;
}
```

## 🎮 Practical Examples

### Example 1: LRU Cache Implementation
```cpp
#include <iostream>
#include <list>
#include <unordered_map>
#include <optional>

template<typename Key, typename Value>
class LRUCache {
private:
    struct CacheItem {
        Key key;
        Value value;
        
        CacheItem(const Key& k, const Value& v) : key(k), value(v) {}
    };
    
    std::list<CacheItem> m_cache_list;
    std::unordered_map<Key, typename std::list<CacheItem>::iterator> m_cache_map;
    size_t m_capacity;
    
public:
    LRUCache(size_t capacity) : m_capacity(capacity) {}
    
    // Get value by key
    std::optional<Value> get(const Key& key) {
        auto it = m_cache_map.find(key);
        if (it == m_cache_map.end()) {
            return std::nullopt;  // Not found
        }
        
        // Move to front (most recently used)
        m_cache_list.splice(m_cache_list.begin(), m_cache_list, it->second);
        
        return it->second->value;
    }
    
    // Put or update value
    void put(const Key& key, const Value& value) {
        auto it = m_cache_map.find(key);
        
        if (it != m_cache_map.end()) {
            // Update existing item
            it->second->value = value;
            // Move to front
            m_cache_list.splice(m_cache_list.begin(), m_cache_list, it->second);
        } else {
            // Add new item
            if (m_cache_list.size() >= m_capacity) {
                // Remove least recently used (back of list)
                auto lru = m_cache_list.back();
                m_cache_map.erase(lru.key);
                m_cache_list.pop_back();
            }
            
            m_cache_list.emplace_front(key, value);
            m_cache_map[key] = m_cache_list.begin();
        }
    }
    
    // Remove key
    bool remove(const Key& key) {
        auto it = m_cache_map.find(key);
        if (it == m_cache_map.end()) {
            return false;
        }
        
        m_cache_list.erase(it->second);
        m_cache_map.erase(it);
        return true;
    }
    
    // Check if key exists
    bool contains(const Key& key) const {
        return m_cache_map.find(key) != m_cache_map.end();
    }
    
    // Get current size
    size_t size() const {
        return m_cache_list.size();
    }
    
    // Clear cache
    void clear() {
        m_cache_list.clear();
        m_cache_map.clear();
    }
    
    // Display cache contents (from most to least recently used)
    void display() const {
        std::cout << "Cache contents (MRU -> LRU): ";
        for (const auto& item : m_cache_list) {
            std::cout << "[" << item.key << ": " << item.value << "] ";
        }
        std::cout << std::endl;
    }
    
    // Get all keys in order of recency
    std::vector<Key> getKeysInOrder() const {
        std::vector<Key> keys;
        for (const auto& item : m_cache_list) {
            keys.push_back(item.key);
        }
        return keys;
    }
};

int main() {
    LRUCache<std::string, int> cache(3);
    
    std::cout << "=== LRU Cache Test ===" << std::endl;
    
    // Add items
    cache.put("apple", 10);
    cache.put("banana", 20);
    cache.put("cherry", 30);
    cache.display();
    
    // Access existing item (moves to MRU)
    auto value = cache.get("apple");
    if (value) {
        std::cout << "Found apple: " << *value << std::endl;
        cache.display();
    }
    
    // Add new item (should evict LRU)
    cache.put("date", 40);
    cache.display();
    
    // Try to access evicted item
    value = cache.get("banana");
    if (!value) {
        std::cout << "banana was evicted from cache" << std::endl;
    }
    
    // Update existing item
    cache.put("apple", 15);
    cache.display();
    
    // Remove item
    cache.remove("cherry");
    cache.display();
    
    return 0;
}
```

### Example 2: Text Editor with Undo/Redo
```cpp
#include <iostream>
#include <list>
#include <string>
#include <vector>

class TextEditor {
private:
    struct EditAction {
        enum Type { INSERT, DELETE, REPLACE };
        
        Type type;
        std::string text;
        size_t position;
        size_t length;  // For delete and replace
        
        EditAction(Type t, const std::string& txt, size_t pos, size_t len = 0)
            : type(t), text(txt), position(pos), length(len) {}
    };
    
    std::list<char> m_text;
    std::list<EditAction> m_undo_stack;
    std::list<EditAction> m_redo_stack;
    size_t m_max_history;
    
public:
    TextEditor(size_t max_history = 50) : m_max_history(max_history) {}
    
    // Insert text at position
    void insert(const std::string& text, size_t position) {
        if (position > m_text.size()) position = m_text.size();
        
        auto it = std::next(m_text.begin(), position);
        for (char c : text) {
            m_text.insert(it, c);
        }
        
        // Add to undo stack
        m_undo_stack.emplace_front(EditAction::INSERT, text, position);
        m_redo_stack.clear();
        
        // Limit history
        while (m_undo_stack.size() > m_max_history) {
            m_undo_stack.pop_back();
        }
    }
    
    // Delete text at position
    void erase(size_t position, size_t length) {
        if (position >= m_text.size()) return;
        
        auto it = std::next(m_text.begin(), position);
        std::string deleted_text;
        
        for (size_t i = 0; i < length && it != m_text.end(); ++i) {
            deleted_text += *it;
            it = m_text.erase(it);
        }
        
        if (!deleted_text.empty()) {
            m_undo_stack.emplace_front(EditAction::DELETE, deleted_text, position, length);
            m_redo_stack.clear();
            
            while (m_undo_stack.size() > m_max_history) {
                m_undo_stack.pop_back();
            }
        }
    }
    
    // Replace text at position
    void replace(const std::string& old_text, const std::string& new_text, size_t position) {
        // Find old_text at position
        auto it = std::next(m_text.begin(), position);
        std::string found_text;
        
        for (size_t i = 0; i < old_text.length() && it != m_text.end(); ++i) {
            found_text += *it++;
        }
        
        if (found_text == old_text) {
            erase(position, old_text.length());
            insert(new_text, position);
            
            m_undo_stack.emplace_front(EditAction::REPLACE, old_text + "|" + new_text, position, old_text.length());
            m_redo_stack.clear();
        }
    }
    
    // Undo last action
    bool undo() {
        if (m_undo_stack.empty()) return false;
        
        EditAction action = m_undo_stack.front();
        m_undo_stack.pop_front();
        
        switch (action.type) {
            case EditAction::INSERT:
                erase(action.position, action.text.length());
                break;
            case EditAction::DELETE:
                insert(action.text, action.position);
                break;
            case EditAction::REPLACE: {
                size_t sep = action.text.find('|');
                std::string old_text = action.text.substr(0, sep);
                std::string new_text = action.text.substr(sep + 1);
                replace(new_text, old_text, action.position);
                break;
            }
        }
        
        m_redo_stack.push_front(action);
        return true;
    }
    
    // Redo last undone action
    bool redo() {
        if (m_redo_stack.empty()) return false;
        
        EditAction action = m_redo_stack.front();
        m_redo_stack.pop_front();
        
        switch (action.type) {
            case EditAction::INSERT:
                insert(action.text, action.position);
                break;
            case EditAction::DELETE:
                erase(action.position, action.length);
                break;
            case EditAction::REPLACE: {
                size_t sep = action.text.find('|');
                std::string old_text = action.text.substr(0, sep);
                std::string new_text = action.text.substr(sep + 1);
                replace(old_text, new_text, action.position);
                break;
            }
        }
        
        return true;
    }
    
    // Get text as string
    std::string getText() const {
        std::string result;
        for (char c : m_text) {
            result += c;
        }
        return result;
    }
    
    // Display text
    void display() const {
        std::cout << "Text: \"" << getText() << "\"" << std::endl;
    }
    
    // Display history
    void displayHistory() const {
        std::cout << "\nUndo stack (" << m_undo_stack.size() << "): ";
        for (const auto& action : m_undo_stack) {
            std::cout << "[" << action.type << ":" << action.text << "] ";
        }
        std::cout << "\nRedo stack (" << m_redo_stack.size() << "): ";
        for (const auto& action : m_redo_stack) {
            std::cout << "[" << action.type << ":" << action.text << "] ";
        }
        std::cout << std::endl;
    }
};

int main() {
    TextEditor editor;
    
    std::cout << "=== Text Editor Test ===" << std::endl;
    
    // Initial text
    editor.insert("Hello", 0);
    editor.insert(" world", 5);
    editor.display();
    
    // More edits
    editor.insert(" beautiful", 6);
    editor.replace("world", "universe", 6);
    editor.display();
    
    editor.displayHistory();
    
    // Undo operations
    std::cout << "\n=== Undo Operations ===" << std::endl;
    editor.undo();
    editor.display();
    
    editor.undo();
    editor.display();
    
    editor.undo();
    editor.display();
    
    // Redo operations
    std::cout << "\n=== Redo Operations ===" << std::endl;
    editor.redo();
    editor.display();
    
    editor.redo();
    editor.display();
    
    return 0;
}
```

### Example 3: Graph Traversal with Adjacency List
```cpp
#include <iostream>
#include <list>
#include <vector>
#include <queue>
#include <stack>
#include <unordered_set>
#include <algorithm>

class Graph {
private:
    std::vector<std::list<int>> m_adjacency;
    int m_vertices;
    
public:
    Graph(int vertices) : m_vertices(vertices), m_adjacency(vertices) {}
    
    // Add edge
    void addEdge(int from, int to, bool directed = false) {
        m_adjacency[from].push_back(to);
        if (!directed) {
            m_adjacency[to].push_back(from);
        }
    }
    
    // Remove edge
    void removeEdge(int from, int to, bool directed = false) {
        auto& list = m_adjacency[from];
        list.remove(to);
        
        if (!directed) {
            m_adjacency[to].remove(from);
        }
    }
    
    // Get neighbors
    const std::list<int>& getNeighbors(int vertex) const {
        return m_adjacency[vertex];
    }
    
    // BFS traversal
    std::vector<int> bfs(int start) const {
        std::vector<int> result;
        std::queue<int> q;
        std::vector<bool> visited(m_vertices, false);
        
        q.push(start);
        visited[start] = true;
        
        while (!q.empty()) {
            int current = q.front();
            q.pop();
            result.push_back(current);
            
            for (int neighbor : m_adjacency[current]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        
        return result;
    }
    
    // DFS traversal (iterative)
    std::vector<int> dfs(int start) const {
        std::vector<int> result;
        std::stack<int> s;
        std::vector<bool> visited(m_vertices, false);
        
        s.push(start);
        visited[start] = true;
        
        while (!s.empty()) {
            int current = s.top();
            s.pop();
            result.push_back(current);
            
            for (int neighbor : m_adjacency[current]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    s.push(neighbor);
                }
            }
        }
        
        return result;
    }
    
    // Detect cycle using DFS
    bool hasCycle() const {
        std::vector<bool> visited(m_vertices, false);
        std::vector<bool> recStack(m_vertices, false);
        
        for (int i = 0; i < m_vertices; ++i) {
            if (!visited[i] && hasCycleUtil(i, visited, recStack)) {
                return true;
            }
        }
        
        return false;
    }
    
    // Find shortest path using BFS
    std::vector<int> shortestPath(int start, int end) const {
        std::vector<int> parent(m_vertices, -1);
        std::vector<bool> visited(m_vertices, false);
        std::queue<int> q;
        
        q.push(start);
        visited[start] = true;
        
        while (!q.empty()) {
            int current = q.front();
            q.pop();
            
            if (current == end) break;
            
            for (int neighbor : m_adjacency[current]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    parent[neighbor] = current;
                    q.push(neighbor);
                }
            }
        }
        
        // Reconstruct path
        std::vector<int> path;
        if (parent[end] == -1 && start != end) return path;  // No path
        
        for (int at = end; at != -1; at = parent[at]) {
            path.push_back(at);
        }
        std::reverse(path.begin(), path.end());
        
        return path;
    }
    
    // Display graph
    void display() const {
        std::cout << "Graph adjacency list:" << std::endl;
        for (int i = 0; i < m_vertices; ++i) {
            std::cout << i << " -> ";
            for (int neighbor : m_adjacency[i]) {
                std::cout << neighbor << " ";
            }
            std::cout << std::endl;
        }
    }
    
private:
    bool hasCycleUtil(int vertex, std::vector<bool>& visited, 
                     std::vector<bool>& recStack) const {
        visited[vertex] = true;
        recStack[vertex] = true;
        
        for (int neighbor : m_adjacency[vertex]) {
            if (!visited[neighbor] && hasCycleUtil(neighbor, visited, recStack)) {
                return true;
            } else if (recStack[neighbor]) {
                return true;
            }
        }
        
        recStack[vertex] = false;
        return false;
    }
};

int main() {
    Graph g(6);
    
    // Build graph
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 4);
    g.addEdge(3, 4);
    g.addEdge(3, 5);
    g.addEdge(4, 5);
    
    g.display();
    
    // BFS traversal
    std::cout << "\nBFS from vertex 0: ";
    auto bfs_result = g.bfs(0);
    for (int vertex : bfs_result) {
        std::cout << vertex << " ";
    }
    std::cout << std::endl;
    
    // DFS traversal
    std::cout << "DFS from vertex 0: ";
    auto dfs_result = g.dfs(0);
    for (int vertex : dfs_result) {
        std::cout << vertex << " ";
    }
    std::cout << std::endl;
    
    // Shortest path
    std::cout << "Shortest path from 0 to 5: ";
    auto path = g.shortestPath(0, 5);
    for (int vertex : path) {
        std::cout << vertex << " ";
    }
    std::cout << std::endl;
    
    // Check for cycles
    std::cout << "Graph has cycle: " << (g.hasCycle() ? "Yes" : "No") << std::endl;
    
    return 0;
}
```

### Example 4: Task Queue with Priority Management
```cpp
#include <iostream>
#include <list>
#include <queue>
#include <string>
#include <functional>
#include <algorithm>

class TaskQueue {
private:
    struct Task {
        int id;
        std::string description;
        int priority;
        std::chrono::steady_clock::time_point created_at;
        
        Task(int i, std::string desc, int prio) 
            : id(i), description(std::move(desc)), priority(prio),
              created_at(std::chrono::steady_clock::now()) {}
        
        bool operator<(const Task& other) const {
            if (priority != other.priority) {
                return priority < other.priority;  // Higher priority first
            }
            return created_at > other.created_at;  // Earlier tasks first
        }
    };
    
    std::list<Task> m_pending_tasks;
    std::list<Task> m_completed_tasks;
    std::priority_queue<Task, std::vector<Task>, std::function<bool(const Task&, const Task&)>> 
        m_priority_queue([](const Task& a, const Task& b) { return a < b; });
    
    int m_next_id;
    
public:
    TaskQueue() : m_priority_queue([](const Task& a, const Task& b) { return a < b; }), 
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
    
    // Add high-priority task to front
    int addHighPriorityTask(const std::string& description) {
        Task task(m_next_id++, description, 10);
        m_pending_tasks.push_front(task);
        m_priority_queue.push(task);
        
        std::cout << "Added high-priority task " << task.id << ": " << task.description << std::endl;
        
        return task.id;
    }
    
    // Get next task by priority
    bool getNextTask(Task& task) {
        if (m_priority_queue.empty()) return false;
        
        task = m_priority_queue.top();
        m_priority_queue.pop();
        
        // Remove from pending list
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
    
    // Promote task (increase priority)
    bool promoteTask(int task_id, int new_priority) {
        auto it = std::find_if(m_pending_tasks.begin(), m_pending_tasks.end(),
                              [task_id](const Task& t) { return t.id == task_id; });
        
        if (it != m_pending_tasks.end()) {
            it->priority = new_priority;
            
            // Rebuild priority queue
            rebuildPriorityQueue();
            
            std::cout << "Promoted task " << task_id << " to priority " << new_priority << std::endl;
            return true;
        }
        
        return false;
    }
    
    // Process all tasks by priority
    void processAllTasks() {
        std::cout << "\n=== Processing All Tasks ===" << std::endl;
        
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
    
private:
    void rebuildPriorityQueue() {
        // Clear and rebuild priority queue
        std::priority_queue<Task, std::vector<Task>, std::function<bool(const Task&, const Task&)>> 
            new_queue([](const Task& a, const Task& b) { return a < b; });
        
        for (const auto& task : m_pending_tasks) {
            new_queue.push(task);
        }
        
        m_priority_queue = std::move(new_queue);
    }
};

int main() {
    TaskQueue queue;
    
    // Add tasks with different priorities
    queue.addTask("Write documentation", 2);
    queue.addTask("Fix bug #123", 5);
    queue.addTask("Implement feature X", 3);
    queue.addHighPriorityTask("Critical security fix");
    queue.addTask("Code review", 1);
    queue.addTask("Optimize performance", 4);
    
    queue.displayPending();
    
    // Promote some tasks
    std::cout << "\n=== Promoting Tasks ===" << std::endl;
    queue.promoteTask(2, 8);  // Fix bug #123
    queue.promoteTask(6, 7);  // Optimize performance
    
    // Complete some tasks
    std::cout << "\n=== Completing Tasks ===" << std::endl;
    queue.completeTask(3);  // Implement feature X
    queue.completeTask(5);  // Code review
    
    // Show statistics
    auto stats = queue.getStatistics();
    std::cout << "\n=== Statistics ===" << std::endl;
    std::cout << "Pending tasks: " << stats.pending_count << std::endl;
    std::cout << "Completed tasks: " << stats.completed_count << std::endl;
    std::cout << "Priority range: " << stats.lowest_priority 
              << " to " << stats.highest_priority << std::endl;
    
    // Process remaining tasks
    queue.processAllTasks();
    
    return 0;
}
```

## 📊 Complete Function Reference

### Element Access
| Function | Description | Complexity |
|----------|-------------|------------|
| `front()` | Access first element | O(1) |
| `back()` | Access last element | O(1) |

### Modifiers
| Function | Description | Complexity |
|----------|-------------|------------|
| `push_front()` | Add element to beginning | O(1) |
| `push_back()` | Add element to end | O(1) |
| `pop_front()` | Remove element from beginning | O(1) |
| `pop_back()` | Remove element from end | O(1) |
| `insert()` | Insert element at position | O(1) |
| `erase()` | Remove element at position | O(1) |
| `clear()` | Remove all elements | O(n) |
| `resize()` | Change size | O(n) |
| `assign()` | Assign new values | O(n) |
| `swap()` | Swap contents | O(1) |

### Operations
| Function | Description | Complexity |
|----------|-------------|------------|
| `splice()` | Transfer elements from another list | O(1) |
| `remove()` | Remove all elements with value | O(n) |
| `remove_if()` | Remove elements satisfying condition | O(n) |
| `unique()` | Remove consecutive duplicates | O(n) |
| `merge()` | Merge sorted lists | O(n) |
| `sort()` | Sort list | O(n log n) |
| `reverse()` | Reverse order | O(n) |

## ⚡ Performance Considerations

### Memory Layout
```cpp
// List elements are non-contiguous
// Each element contains: value, prev_ptr, next_ptr
// Good for insertions/deletions, poor for cache locality

std::list<int> lst = {1, 2, 3};
// Memory might be:
// [1][next][prev] -> [2][next][prev] -> [3][next][prev]
```

### Iterator Stability
```cpp
// List iterators remain valid when other elements are modified
// This is a key advantage over vector/deque

std::list<int> lst = {1, 2, 3, 4, 5};
auto it = std::next(lst.begin(), 2);  // Points to 3

lst.push_front(0);    // it still valid
lst.erase(lst.begin()); // it still valid
lst.push_back(6);     // it still valid
```

## 🎯 Common Patterns

### Pattern 1: Stable Container for Moving Elements
```cpp
class MovingObjectManager {
private:
    std::list<GameObject> m_objects;
    
public:
    void addObject(const GameObject& obj) {
        m_objects.push_back(obj);
    }
    
    void removeObject(std::list<GameObject>::iterator it) {
        m_objects.erase(it);
    }
    
    void updatePositions() {
        for (auto it = m_objects.begin(); it != m_objects.end(); ++it) {
            // Can safely modify other objects while iterating
            it->update();
        }
    }
};
```

### Pattern 2: Efficient Splicing Operations
```cpp
void moveItemsBetweenLists(std::list<int>& source, std::list<int>& dest, 
                          std::list<int>::iterator start, std::list<int>::iterator end) {
    // Move range without copying
    dest.splice(dest.end(), source, start, end);
}
```

## 🐛 Common Pitfalls & Solutions

### 1. No Random Access
```cpp
// Problem
std::list<int> lst = {1, 2, 3, 4, 5};
int val = lst[2];  // Error: no operator[]

// Solution
auto it = std::next(lst.begin(), 2);
int val = *it;
```

### 2. Inefficient Search Operations
```cpp
// Problem - linear search is O(n)
std::list<int> lst = {1, 2, 3, 4, 5};
auto it = std::find(lst.begin(), lst.end(), 3);  // O(n)

// Solution - use appropriate container for frequent searches
// or maintain auxiliary data structures
```

### 3. Memory Overhead
```cpp
// Problem - each element has overhead
struct Node {
    int value;      // 4 bytes
    Node* next;     // 8 bytes
    Node* prev;     // 8 bytes
    // Total: 20 bytes per int (4x overhead)
};

// Solution - consider memory efficiency vs. performance needs
```

## 📚 Related Headers

- `forward_list.md` - Singly linked list
- `vector.md` - Contiguous dynamic array
- `deque.md` - Double-ended queue
- `algorithm.md` - Generic algorithms

## 🚀 Best Practices

1. **Use list** when you need stable iterators
2. **Prefer list** for frequent insertions/deletions in middle
3. **Use splice** for efficient element transfer between lists
4. **Avoid list** for random access patterns
5. **Consider vector** for better cache locality
6. **Use member algorithms** (sort, merge) for better performance

## 🎯 When to Use list

✅ **Use list when:**
- Need stable iterators/pointers
- Frequent insertions/deletions in middle
- Need to splice between containers
- Elements are large/expensive to move
- Iterator invalidation must be avoided

❌ **Avoid when:**
- Need random access (use `vector`/`deque`)
- Cache locality is critical
- Memory is constrained
- Frequent searches needed
- Small elements with high overhead concerns
---

## Next Step

- Go to [14_forward_list.md](14_forward_list.md) to continue with forward list.
