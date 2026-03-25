# 21_priority_queue.md - Ordered Access Container Adapter

The `priority_queue` header provides `std::priority_queue`, a container adapter that provides access to the highest priority element first (max-heap by default).

## 📖 Overview

`std::priority_queue` is a container adapter that provides constant-time access to the highest priority element (by default, the largest element). It's implemented as a heap and provides efficient insertion and extraction of the top element.

## 🎯 Key Features

- **Priority access** - Always access the highest priority element first
- **Heap implementation** - Efficient O(log n) insertions and deletions
- **Restricted interface** - Only top element access
- **Customizable comparison** - Can be configured for min-heap
- **Container adapter** - Works with different underlying containers
- **No iteration** - Cannot iterate through elements directly

## 🔧 Basic Priority Queue Operations

### Creating and Initializing Priority Queues
```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <functional>

int main() {
    // Different ways to create priority queues
    
    // Default max-heap (largest element first)
    std::priority_queue<int> max_heap;
    
    // Min-heap (smallest element first)
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
    
    // Custom comparator
    auto cmp = [](int a, int b) { return a > b; };  // Reverse order
    std::priority_queue<int, std::vector<int>, decltype(cmp)> custom_heap(cmp);
    
    // From initializer list
    std::priority_queue<int> heap_from_list({3, 1, 4, 1, 5, 9});
    
    // Copy constructor
    std::priority_queue<int> heap_copy = max_heap;
    
    return 0;
}
```

### Push and Pop Operations
```cpp
void demonstrateBasicOperations() {
    std::priority_queue<int> pq;
    
    // Push elements
    pq.push(10);
    pq.push(30);
    pq.push(20);
    pq.push(50);
    pq.push(40);
    
    std::cout << "Priority queue size: " << pq.size() << std::endl;
    std::cout << "Top element: " << pq.top() << std::endl;
    
    // Pop elements (in priority order)
    std::cout << "Elements in priority order: ";
    while (!pq.empty()) {
        std::cout << pq.top() << " ";
        pq.pop();
    }
    std::cout << std::endl;
    
    std::cout << "Priority queue is now empty: " << (pq.empty() ? "Yes" : "No") << std::endl;
}
```

### Min-Heap Example
```cpp
void demonstrateMinHeap() {
    // Min-heap using std::greater
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_pq;
    
    min_pq.push(10);
    min_pq.push(30);
    min_pq.push(20);
    min_pq.push(50);
    min_pq.push(40);
    
    std::cout << "Min-heap elements (smallest first): ";
    while (!min_pq.empty()) {
        std::cout << min_pq.top() << " ";
        min_pq.pop();
    }
    std::cout << std::endl;
}
```

## 🔧 Advanced Priority Queue Operations

### Custom Comparator
```cpp
void demonstrateCustomComparator() {
    // Custom comparator for strings (by length)
    auto length_cmp = [](const std::string& a, const std::string& b) {
        return a.length() > b.length();  // Shorter strings have higher priority
    };
    
    std::priority_queue<std::string, std::vector<std::string>, decltype(length_cmp)> string_pq(length_cmp);
    
    string_pq.push("apple");
    string_pq.push("banana");
    string_pq.push("kiwi");
    string_pq.push("strawberry");
    string_pq.push("fig");
    
    std::cout << "Strings by length (shortest first): ";
    while (!string_pq.empty()) {
        std::cout << string_pq.top() << "(" << string_pq.top().length() << ") ";
        string_pq.pop();
    }
    std::cout << std::endl;
}
```

### Priority Queue with Custom Objects
```cpp
struct Task {
    std::string name;
    int priority;
    int duration;
    
    Task(const std::string& n, int p, int d) : name(n), priority(p), duration(d) {}
    
    // Overload < for max-heap (higher priority first)
    bool operator<(const Task& other) const {
        if (priority != other.priority) {
            return priority < other.priority;  // Higher priority first
        }
        return duration > other.duration;  // Shorter duration first for same priority
    }
};

void demonstrateCustomObjects() {
    std::priority_queue<Task> task_pq;
    
    task_pq.emplace("Low Priority Task", 1, 30);
    task_pq.emplace("High Priority Task", 5, 10);
    task_pq.emplace("Medium Priority Task", 3, 20);
    task_pq.emplace("Urgent Task", 5, 5);  // Same priority, shorter duration
    
    std::cout << "Tasks in priority order:" << std::endl;
    while (!task_pq.empty()) {
        const Task& task = task_pq.top();
        std::cout << "  " << task.name << " (priority: " << task.priority 
                  << ", duration: " << task.duration << ")" << std::endl;
        task_pq.pop();
    }
}
```

## 🎮 Practical Examples

### Example 1: Dijkstra's Shortest Path Algorithm
```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <unordered_map>
#include <climits>
#include <string>

class Graph {
private:
    struct Edge {
        int to;
        int weight;
    };
    
    std::vector<std::vector<Edge>> adjacency_list;
    std::vector<std::string> node_names;
    
public:
    Graph(int size) {
        adjacency_list.resize(size);
        node_names.resize(size);
    }
    
    void setNodeName(int node, const std::string& name) {
        node_names[node] = name;
    }
    
    void addEdge(int from, int to, int weight) {
        adjacency_list[from].push_back({to, weight});
        adjacency_list[to].push_back({from, weight});  // Undirected
    }
    
    // Dijkstra's algorithm using priority queue
    std::vector<int> dijkstra(int start) {
        std::vector<int> distance(adjacency_list.size(), INT_MAX);
        distance[start] = 0;
        
        // Min-heap: {distance, node}
        std::priority_queue<std::pair<int, int>, 
                           std::vector<std::pair<int, int>>, 
                           std::greater<std::pair<int, int>>> pq;
        
        pq.push({0, start});
        
        while (!pq.empty()) {
            auto [dist, node] = pq.top();
            pq.pop();
            
            // Skip if we already found a better path
            if (dist > distance[node]) {
                continue;
            }
            
            // Relax edges
            for (const auto& edge : adjacency_list[node]) {
                int new_dist = dist + edge.weight;
                if (new_dist < distance[edge.to]) {
                    distance[edge.to] = new_dist;
                    pq.push({new_dist, edge.to});
                }
            }
        }
        
        return distance;
    }
    
    // Get shortest path
    std::vector<int> getShortestPath(int start, int end) {
        std::vector<int> distance = dijkstra(start);
        std::vector<int> parent(adjacency_list.size(), -1);
        
        // Reconstruct parents (simplified - would need to store during Dijkstra)
        // For demo purposes, we'll just return the distance
        if (distance[end] == INT_MAX) {
            return {};  // No path
        }
        
        return distance;
    }
    
    void displayDistances(int start, const std::vector<int>& distances) const {
        std::cout << "Shortest distances from " << node_names[start] << ":" << std::endl;
        for (size_t i = 0; i < distances.size(); ++i) {
            if (distances[i] != INT_MAX) {
                std::cout << "  to " << node_names[i] << ": " << distances[i] << std::endl;
            } else {
                std::cout << "  to " << node_names[i] << ": unreachable" << std::endl;
            }
        }
    }
};

int main() {
    std::cout << "=== Dijkstra's Algorithm Demo ===" << std::endl;
    
    // Create a graph
    Graph graph(6);
    
    // Set node names
    graph.setNodeName(0, "A");
    graph.setNodeName(1, "B");
    graph.setNodeName(2, "C");
    graph.setNodeName(3, "D");
    graph.setNodeName(4, "E");
    graph.setNodeName(5, "F");
    
    // Add edges with weights
    graph.addEdge(0, 1, 4);  // A-B (4)
    graph.addEdge(0, 2, 2);  // A-C (2)
    graph.addEdge(1, 2, 1);  // B-C (1)
    graph.addEdge(1, 3, 5);  // B-D (5)
    graph.addEdge(2, 3, 8);  // C-D (8)
    graph.addEdge(2, 4, 10); // C-E (10)
    graph.addEdge(3, 4, 2);  // D-E (2)
    graph.addEdge(3, 5, 6);  // D-F (6)
    graph.addEdge(4, 5, 3);  // E-F (3)
    
    // Run Dijkstra's algorithm
    int start_node = 0;  // Start from A
    auto distances = graph.dijkstra(start_node);
    
    // Display results
    graph.displayDistances(start_node, distances);
    
    // Test from different start node
    std::cout << "\n=== Starting from D ===" << std::endl;
    auto distances2 = graph.dijkstra(3);
    graph.displayDistances(3, distances2);
    
    return 0;
}
```

### Example 2: Huffman Coding
```cpp
#include <iostream>
#include <queue>
#include <unordered_map>
#include <string>
#include <memory>

class HuffmanNode {
public:
    char character;
    int frequency;
    std::shared_ptr<HuffmanNode> left;
    std::shared_ptr<HuffmanNode> right;
    
    HuffmanNode(char ch, int freq) 
        : character(ch), frequency(freq), left(nullptr), right(nullptr) {}
    
    HuffmanNode(int freq, std::shared_ptr<HuffmanNode> l, std::shared_ptr<HuffmanNode> r)
        : character('\0'), frequency(freq), left(l), right(r) {}
    
    // For priority queue (min-heap based on frequency)
    bool operator>(const HuffmanNode& other) const {
        return frequency > other.frequency;
    }
};

class HuffmanCoding {
private:
    std::shared_ptr<HuffmanNode> root;
    std::unordered_map<char, std::string> codes;
    
    void buildCodes(std::shared_ptr<HuffmanNode> node, std::string code) {
        if (!node) return;
        
        if (node->character != '\0') {
            codes[node->character] = code;
            return;
        }
        
        buildCodes(node->left, code + "0");
        buildCodes(node->right, code + "1");
    }
    
public:
    // Build Huffman tree from frequency map
    void buildTree(const std::unordered_map<char, int>& frequencies) {
        // Min-heap based on frequency
        std::priority_queue<HuffmanNode, std::vector<HuffmanNode>, std::greater<HuffmanNode>> pq;
        
        // Create leaf nodes
        for (const auto& [ch, freq] : frequencies) {
            pq.emplace(ch, freq);
        }
        
        // Build tree
        while (pq.size() > 1) {
            auto right = std::make_shared<HuffmanNode>(pq.top());
            pq.pop();
            
            auto left = std::make_shared<HuffmanNode>(pq.top());
            pq.pop();
            
            pq.emplace(left->frequency + right->frequency, left, right);
        }
        
        if (!pq.empty()) {
            root = std::make_shared<HuffmanNode>(pq.top());
        }
        
        // Build codes
        codes.clear();
        buildCodes(root, "");
    }
    
    // Get Huffman codes
    const std::unordered_map<char, std::string>& getCodes() const {
        return codes;
    }
    
    // Encode text
    std::string encode(const std::string& text) const {
        std::string encoded;
        for (char ch : text) {
            auto it = codes.find(ch);
            if (it != codes.end()) {
                encoded += it->second;
            }
        }
        return encoded;
    }
    
    // Decode text
    std::string decode(const std::string& encoded) const {
        std::string decoded;
        auto current = root;
        
        for (char bit : encoded) {
            if (bit == '0') {
                current = current->left;
            } else {
                current = current->right;
            }
            
            if (current->character != '\0') {
                decoded += current->character;
                current = root;
            }
        }
        
        return decoded;
    }
    
    // Display codes
    void displayCodes() const {
        std::cout << "Huffman Codes:" << std::endl;
        for (const auto& [ch, code] : codes) {
            std::cout << "  '" << ch << "': " << code << std::endl;
        }
    }
    
    // Calculate compression ratio
    double calculateCompressionRatio(const std::string& original) const {
        size_t original_bits = original.length() * 8;  // 8 bits per char
        size_t compressed_bits = 0;
        
        for (char ch : original) {
            auto it = codes.find(ch);
            if (it != codes.end()) {
                compressed_bits += it->second.length();
            }
        }
        
        return (double)compressed_bits / original_bits * 100;
    }
};

int main() {
    std::cout << "=== Huffman Coding Demo ===" << std::endl;
    
    // Sample text and calculate frequencies
    std::string text = "this is an example for huffman encoding";
    std::unordered_map<char, int> frequencies;
    
    for (char ch : text) {
        if (ch != ' ') {  // Ignore spaces for this example
            frequencies[ch]++;
        }
    }
    
    std::cout << "Character frequencies:" << std::endl;
    for (const auto& [ch, freq] : frequencies) {
        std::cout << "  '" << ch << "': " << freq << std::endl;
    }
    
    // Build Huffman tree
    HuffmanCoding huffman;
    huffman.buildTree(frequencies);
    
    // Display codes
    huffman.displayCodes();
    
    // Encode and decode
    std::string text_no_spaces;
    for (char ch : text) {
        if (ch != ' ') {
            text_no_spaces += ch;
        }
    }
    
    std::string encoded = huffman.encode(text_no_spaces);
    std::string decoded = huffman.decode(encoded);
    
    std::cout << "\nOriginal: " << text_no_spaces << std::endl;
    std::cout << "Encoded:  " << encoded << std::endl;
    std::cout << "Decoded:  " << decoded << std::endl;
    
    // Calculate compression ratio
    double ratio = huffman.calculateCompressionRatio(text_no_spaces);
    std::cout << "Compression ratio: " << std::fixed << std::setprecision(1) 
              << ratio << "%" << std::endl;
    
    std::cout << "Original size: " << text_no_spaces.length() * 8 << " bits" << std::endl;
    std::cout << "Compressed size: " << encoded.length() << " bits" << std::endl;
    
    return 0;
}
```

### Example 3: Event Simulation System
```cpp
#include <iostream>
#include <queue>
#include <string>
#include <functional>
#include <chrono>
#include <random>

class Event {
private:
    std::string description;
    double time;
    int priority;
    std::function<void()> action;
    
public:
    Event(const std::string& desc, double t, int prio, std::function<void()> act)
        : description(desc), time(t), priority(prio), action(act) {}
    
    // For priority queue (earliest time first, then higher priority)
    bool operator<(const Event& other) const {
        if (time != other.time) {
            return time > other.time;  // Earlier time has higher priority
        }
        return priority < other.priority;  // Higher priority number first
    }
    
    void execute() const {
        std::cout << "[" << time << "] " << description << std::endl;
        action();
    }
    
    double getTime() const { return time; }
    const std::string& getDescription() const { return description; }
    int getPriority() const { return priority; }
};

class EventScheduler {
private:
    std::priority_queue<Event> event_queue;
    double current_time;
    bool is_running;
    
public:
    EventScheduler() : current_time(0.0), is_running(false) {}
    
    // Add event to schedule
    void scheduleEvent(const std::string& description, double time, int priority, 
                      std::function<void()> action) {
        Event event(description, time, priority, action);
        event_queue.push(event);
        
        std::cout << "Scheduled: " << description << " at time " << time 
                  << " (priority: " << priority << ")" << std::endl;
    }
    
    // Run simulation
    void run() {
        is_running = true;
        std::cout << "\n=== Starting Simulation ===" << std::endl;
        
        while (!event_queue.empty() && is_running) {
            Event event = event_queue.top();
            event_queue.pop();
            
            // Update current time
            current_time = event.getTime();
            
            // Execute event
            event.execute();
            
            // Small delay for demo purposes
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
        }
        
        std::cout << "=== Simulation Complete ===" << std::endl;
    }
    
    // Stop simulation
    void stop() {
        is_running = false;
        std::cout << "Simulation stopped" << std::endl;
    }
    
    // Get current simulation time
    double getCurrentTime() const { return current_time; }
    
    // Get queue statistics
    struct QueueStats {
        size_t pending_events;
        double current_time;
        bool is_running;
    };
    
    QueueStats getStatistics() const {
        return {event_queue.size(), current_time, is_running};
    }
    
    // Display upcoming events
    void displayUpcomingEvents() const {
        std::cout << "\n=== Upcoming Events ===" << std::endl;
        
        // Create copy to display
        std::priority_queue<Event> temp = event_queue;
        std::vector<Event> events;
        
        while (!temp.empty()) {
            events.push_back(temp.top());
            temp.pop();
        }
        
        // Sort by time for display
        std::sort(events.begin(), events.end(), 
                 [](const Event& a, const Event& b) {
                     if (a.getTime() != b.getTime()) {
                         return a.getTime() < b.getTime();
                     }
                     return a.getPriority() > b.getPriority();
                 });
        
        for (const auto& event : events) {
            std::cout << "  [" << event.getTime() << "] " << event.getDescription()
                      << " (priority: " << event.getPriority() << ")" << std::endl;
        }
    }
    
    // Clear all events
    void clear() {
        while (!event_queue.empty()) {
            event_queue.pop();
        }
        std::cout << "Event queue cleared" << std::endl;
    }
};

int main() {
    EventScheduler scheduler;
    
    std::cout << "=== Event Simulation System Demo ===" << std::endl;
    
    // Schedule some events
    scheduler.scheduleEvent("System Initialize", 0.0, 1, []() {
        std::cout << "  → System initialized" << std::endl;
    });
    
    scheduler.scheduleEvent("Load Configuration", 1.0, 2, []() {
        std::cout << "  → Configuration loaded" << std::endl;
    });
    
    scheduler.scheduleEvent("Start Services", 2.0, 3, []() {
        std::cout << "  → Services started" << std::endl;
    });
    
    scheduler.scheduleEvent("Connect to Database", 1.5, 2, []() {
        std::cout << "  → Database connected" << std::endl;
    });
    
    scheduler.scheduleEvent("Run Health Check", 3.0, 1, []() {
        std::cout << "  → Health check completed" << std::endl;
    });
    
    // Add some overlapping events with different priorities
    scheduler.scheduleEvent("Urgent Alert", 2.0, 10, []() {
        std::cout << "  → Urgent alert processed!" << std::endl;
    });
    
    scheduler.scheduleEvent("Background Task", 2.5, 1, []() {
        std::cout << "  → Background task completed" << std::endl;
    });
    
    // Display upcoming events
    scheduler.displayUpcomingEvents();
    
    // Run simulation
    scheduler.run();
    
    // Show final statistics
    auto stats = scheduler.getStatistics();
    std::cout << "\nFinal statistics:" << std::endl;
    std::cout << "  Pending events: " << stats.pending_events << std::endl;
    std::cout << "  Current time: " << stats.current_time << std::endl;
    std::cout << "  Running: " << (stats.is_running ? "Yes" : "No") << std::endl;
    
    return 0;
}
```

### Example 4: K-Way Merge
```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

class KWayMerger {
private:
    struct ArrayElement {
        int value;
        int array_index;
        int element_index;
        
        ArrayElement(int val, int arr_idx, int elem_idx) 
            : value(val), array_index(arr_idx), element_index(elem_idx) {}
        
        // For min-heap (smallest value first)
        bool operator>(const ArrayElement& other) const {
            return value > other.value;
        }
    };
    
public:
    // Merge k sorted arrays
    std::vector<int> mergeKArrays(const std::vector<std::vector<int>>& arrays) {
        std::vector<int> result;
        
        // Min-heap to store current elements from each array
        std::priority_queue<ArrayElement, std::vector<ArrayElement>, std::greater<ArrayElement>> min_heap;
        
        // Initialize heap with first element from each array
        for (size_t i = 0; i < arrays.size(); ++i) {
            if (!arrays[i].empty()) {
                min_heap.emplace(arrays[i][0], i, 0);
            }
        }
        
        // Merge process
        while (!min_heap.empty()) {
            ArrayElement current = min_heap.top();
            min_heap.pop();
            
            result.push_back(current.value);
            
            // Add next element from the same array
            if (current.element_index + 1 < arrays[current.array_index].size()) {
                int next_value = arrays[current.array_index][current.element_index + 1];
                min_heap.emplace(next_value, current.array_index, current.element_index + 1);
            }
        }
        
        return result;
    }
    
    // Find k smallest elements from multiple sorted arrays
    std::vector<int> findKSmallest(const std::vector<std::vector<int>>& arrays, int k) {
        std::vector<int> result;
        
        std::priority_queue<ArrayElement, std::vector<ArrayElement>, std::greater<ArrayElement>> min_heap;
        
        // Initialize heap
        for (size_t i = 0; i < arrays.size(); ++i) {
            if (!arrays[i].empty()) {
                min_heap.emplace(arrays[i][0], i, 0);
            }
        }
        
        // Extract k smallest elements
        while (!min_heap.empty() && result.size() < k) {
            ArrayElement current = min_heap.top();
            min_heap.pop();
            
            result.push_back(current.value);
            
            // Add next element from the same array
            if (current.element_index + 1 < arrays[current.array_index].size()) {
                int next_value = arrays[current.array_index][current.element_index + 1];
                min_heap.emplace(next_value, current.array_index, current.element_index + 1);
            }
        }
        
        return result;
    }
    
    // Find k largest elements from multiple sorted arrays
    std::vector<int> findKLargest(const std::vector<std::vector<int>>& arrays, int k) {
        std::vector<int> result;
        
        // Max-heap to store current candidates
        std::priority_queue<ArrayElement> max_heap;
        
        // Initialize heap with last element from each array
        for (size_t i = 0; i < arrays.size(); ++i) {
            if (!arrays[i].empty()) {
                int last_idx = arrays[i].size() - 1;
                max_heap.emplace(arrays[i][last_idx], i, last_idx);
            }
        }
        
        // Extract k largest elements
        while (!max_heap.empty() && result.size() < k) {
            ArrayElement current = max_heap.top();
            max_heap.pop();
            
            result.push_back(current.value);
            
            // Add previous element from the same array
            if (current.element_index > 0) {
                int prev_value = arrays[current.array_index][current.element_index - 1];
                max_heap.emplace(prev_value, current.array_index, current.element_index - 1);
            }
        }
        
        return result;
    }
    
    // Display array
    void displayArray(const std::vector<int>& arr, const std::string& name) const {
        std::cout << name << ": [";
        for (size_t i = 0; i < arr.size(); ++i) {
            if (i > 0) std::cout << ", ";
            std::cout << arr[i];
        }
        std::cout << "]" << std::endl;
    }
};

int main() {
    std::cout << "=== K-Way Merge Demo ===" << std::endl;
    
    KWayMerger merger;
    
    // Create sample sorted arrays
    std::vector<std::vector<int>> arrays = {
        {1, 4, 7, 10},
        {2, 5, 8, 11, 14},
        {3, 6, 9, 12, 15, 18},
        {0, 13, 16, 19, 20}
    };
    
    std::cout << "Input arrays:" << std::endl;
    for (size_t i = 0; i < arrays.size(); ++i) {
        merger.displayArray(arrays[i], "Array " + std::to_string(i + 1));
    }
    
    // Test k-way merge
    std::cout << "\n=== K-Way Merge ===" << std::endl;
    auto merged = merger.mergeKArrays(arrays);
    merger.displayArray(merged, "Merged array");
    
    // Test finding k smallest
    std::cout << "\n=== Finding 5 Smallest Elements ===" << std::endl;
    auto smallest_5 = merger.findKSmallest(arrays, 5);
    merger.displayArray(smallest_5, "5 smallest");
    
    // Test finding k largest
    std::cout << "\n=== Finding 5 Largest Elements ===" << std::endl;
    auto largest_5 = merger.findKLargest(arrays, 5);
    merger.displayArray(largest_5, "5 largest");
    
    // Verify result is sorted
    bool is_sorted = std::is_sorted(merged.begin(), merged.end());
    std::cout << "\nMerged array is sorted: " << (is_sorted ? "Yes" : "No") << std::endl;
    
    // Count total elements
    size_t total_elements = 0;
    for (const auto& arr : arrays) {
        total_elements += arr.size();
    }
    
    std::cout << "Total input elements: " << total_elements << std::endl;
    std::cout << "Merged elements: " << merged.size() << std::endl;
    std::cout << "Merge successful: " << (total_elements == merged.size() ? "Yes" : "No") << std::endl;
    
    return 0;
}
```

## 📊 Complete Function Reference

### Element Access
| Function | Description | Complexity |
|----------|-------------|------------|
| `top()` | Access top (highest priority) element | O(1) |

### Capacity
| Function | Description | Complexity |
|----------|-------------|------------|
| `empty()` | Check if empty | O(1) |
| `size()` | Get number of elements | O(1) |

### Modifiers
| Function | Description | Complexity |
|----------|-------------|------------|
| `push()` | Insert element | O(log n) |
| `emplace()` | Construct element in place | O(log n) |
| `pop()` | Remove top element | O(log n) |
| `swap()` | Swap contents | O(1) |

## ⚡ Performance Considerations

### Heap Properties
```cpp
// Priority queue maintains heap properties:
// - Parent is always >= children (max-heap)
// - Complete binary tree structure
// - O(log n) insertion and deletion
// - O(1) access to top element
```

### Container Choice
```cpp
// Different underlying containers have different characteristics

// std::vector (default) - good for most cases
std::priority_queue<int> vector_pq;  // O(log n) operations, good cache locality

// std::deque - alternative with similar performance
std::priority_queue<int, std::deque<int>> deque_pq;
```

## 🎯 Common Patterns

### Pattern 1: Top K Elements
```cpp
std::vector<int> findTopK(const std::vector<int>& nums, int k) {
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
    
    for (int num : nums) {
        min_heap.push(num);
        if (min_heap.size() > k) {
            min_heap.pop();
        }
    }
    
    std::vector<int> result;
    while (!min_heap.empty()) {
        result.push_back(min_heap.top());
        min_heap.pop();
    }
    
    return result;
}
```

### Pattern 2: Median Maintenance
```cpp
class MedianFinder {
private:
    std::priority_queue<int> max_heap;  // Lower half
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;  // Upper half
    
public:
    void addNum(int num) {
        if (max_heap.empty() || num <= max_heap.top()) {
            max_heap.push(num);
        } else {
            min_heap.push(num);
        }
        
        // Balance heaps
        if (max_heap.size() > min_heap.size() + 1) {
            min_heap.push(max_heap.top());
            max_heap.pop();
        } else if (min_heap.size() > max_heap.size()) {
            max_heap.push(min_heap.top());
            min_heap.pop();
        }
    }
    
    double findMedian() const {
        if (max_heap.size() == min_heap.size()) {
            return (max_heap.top() + min_heap.top()) / 2.0;
        }
        return max_heap.top();
    }
};
```

## 🐛 Common Pitfalls & Solutions

### 1. Wrong Heap Type
```cpp
// Problem - default is max-heap when you need min-heap
std::priority_queue<int> pq;  // Max-heap
pq.push(5);
pq.push(1);
pq.push(3);
int smallest = pq.top();  // Gets 5, not 1!

// Solution - use std::greater for min-heap
std::priority_queue<int, std::vector<int>, std::greater<int>> min_pq;
min_pq.push(5);
min_pq.push(1);
min_pq.push(3);
int smallest = min_pq.top();  // Gets 1
```

### 2. Invalid Comparator
```cpp
// Problem - using wrong comparator type
std::priority_queue<int, std::vector<int>, std::less<int>> pq;  // Same as default

// Solution - use appropriate comparator
std::priority_queue<int, std::vector<int>, std::greater<int>> min_pq;  // Min-heap
```

### 3. Accessing Empty Priority Queue
```cpp
// Problem - accessing top of empty priority queue
std::priority_queue<int> pq;
int value = pq.top();  // Undefined behavior!

// Solution - always check if empty
if (!pq.empty()) {
    int value = pq.top();
    // Use value safely
}
```

## 📚 Related Headers

- `queue.md` - FIFO container adapter
- `stack.md` - LIFO container adapter
- `vector.md` - Dynamic array (default underlying container)
- `deque.md` - Double-ended queue (alternative underlying container)
- `algorithm.md` - Heap operations (make_heap, push_heap, pop_heap)

## 🚀 Best Practices

1. **Choose correct heap type** - max-heap (default) or min-heap (std::greater)
2. **Use emplace()** for complex types to avoid unnecessary copies
3. **Consider custom comparators** for specialized ordering requirements
4. **Use std::vector** as underlying container for best performance (default)
5. **Check empty()** before calling top() or pop()
6. **Use make_heap** algorithms for existing containers when needed

## 🎯 When to Use priority_queue

✅ **Use priority_queue when:**
- Need quick access to highest/lowest priority element
- Implementing greedy algorithms
- Dijkstra's or Prim's algorithms
- Huffman coding
- Event simulation systems
- Task scheduling with priorities
- Finding top K elements
- Median maintenance

❌ **Avoid when:**
- Need to access all elements in sorted order (use `std::multiset`)
- Need to iterate through elements
- Need to modify arbitrary elements
- Need to find elements by value
- Need FIFO or LIFO behavior (use `queue` or `stack`)

---

**Examples in this file**: 4 complete programs  
**Key Functions**: `push()`, `pop()`, `top()`, `empty()`, `size()`, `emplace()`  
**Time Complexity**: O(1) for top(), O(log n) for push/pop  
**Space Complexity**: O(n) where n is number of elements
