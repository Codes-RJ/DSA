# 20_queue.md - FIFO Container Adapter

The `queue` header provides `std::queue`, a container adapter that provides first-in, first-out (FIFO) access to elements.

## 📖 Overview

`std::queue` is a container adapter that gives the functionality of a queue - specifically, a FIFO (first-in, first-out) data structure. It wraps an underlying container (by default `std::deque`) and provides a restricted interface with queue operations.

## 🎯 Key Features

- **FIFO access** - First element pushed is first element popped
- **Restricted interface** - Only queue operations are available
- **Container adapter** - Works with different underlying containers
- **Constant-time operations** - All operations are O(1)
- **No iteration** - Cannot iterate through elements directly
- **Default container** - Uses `std::deque` by default

## 🔧 Basic Queue Operations

### Creating and Initializing Queues
```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <list>

int main() {
    // Different ways to create queues
    
    // Default queue (uses deque)
    std::queue<int> queue1;
    
    // Queue with vector as underlying container
    std::queue<int, std::vector<int>> queue2;
    
    // Queue with list as underlying container
    std::queue<int, std::list<int>> queue3;
    
    // Queue from existing container
    std::deque<int> deq = {1, 2, 3, 4, 5};
    std::queue<int> queue4(deq);
    
    // Copy constructor
    std::queue<int> queue5 = queue1;
    
    return 0;
}
```

### Push and Pop Operations
```cpp
void demonstrateBasicOperations() {
    std::queue<int> q;
    
    // Push elements
    q.push(10);
    q.push(20);
    q.push(30);
    
    std::cout << "Queue size: " << q.size() << std::endl;
    std::cout << "Front element: " << q.front() << std::endl;
    std::cout << "Back element: " << q.back() << std::endl;
    
    // Pop elements
    while (!q.empty()) {
        std::cout << "Popping: " << q.front() << std::endl;
        q.pop();
    }
    
    std::cout << "Queue is now empty: " << (q.empty() ? "Yes" : "No") << std::endl;
}
```

### Emplace Operations
```cpp
void demonstrateEmplace() {
    std::queue<std::pair<int, std::string>> q;
    
    // Push with emplace (constructs in place)
    q.emplace(1, "First");
    q.emplace(2, "Second");
    q.emplace(3, "Third");
    
    while (!q.empty()) {
        auto& pair = q.front();
        std::cout << pair.first << ": " << pair.second << std::endl;
        q.pop();
    }
}
```

## 🔧 Advanced Queue Operations

### Queue with Custom Container
```cpp
void demonstrateCustomContainers() {
    // Queue using deque (default)
    std::queue<int> deque_queue;
    deque_queue.push(1);
    deque_queue.push(2);
    deque_queue.push(3);
    
    std::cout << "Deque-based queue size: " << deque_queue.size() << std::endl;
    
    // Queue using list
    std::queue<int, std::list<int>> list_queue;
    list_queue.push(4);
    list_queue.push(5);
    list_queue.push(6);
    
    std::cout << "List-based queue size: " << list_queue.size() << std::endl;
}
```

### Accessing Underlying Container
```cpp
void demonstrateUnderlyingAccess() {
    std::queue<int, std::deque<int>> q;
    
    // Push some elements
    for (int i = 1; i <= 5; ++i) {
        q.push(i * 10);
    }
    
    // Access underlying container (non-standard but commonly supported)
    // Note: This is implementation-specific and not portable
    #ifdef __GNUC__
    auto& container = q._Get_container();
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

### Example 1: Task Scheduler
```cpp
#include <iostream>
#include <queue>
#include <string>
#include <functional>
#include <chrono>
#include <thread>

class Task {
private:
    std::string name;
    std::function<void()> action;
    std::chrono::time_point<std::chrono::steady_clock> created_at;
    
public:
    Task(const std::string& task_name, std::function<void()> task_action)
        : name(task_name), action(task_action), created_at(std::chrono::steady_clock::now()) {}
    
    void execute() const {
        std::cout << "Executing task: " << name << std::endl;
        action();
    }
    
    const std::string& getName() const { return name; }
    
    auto getWaitTime() const {
        auto now = std::chrono::steady_clock::now();
        return std::chrono::duration_cast<std::chrono::milliseconds>(now - created_at);
    }
};

class TaskScheduler {
private:
    std::queue<Task> task_queue;
    bool is_running;
    
public:
    TaskScheduler() : is_running(false) {}
    
    // Add task to queue
    void addTask(const std::string& name, std::function<void()> action) {
        Task task(name, action);
        task_queue.push(task);
        std::cout << "Added task to queue: " << name << std::endl;
    }
    
    // Process next task
    bool processNextTask() {
        if (task_queue.empty()) {
            std::cout << "No tasks in queue" << std::endl;
            return false;
        }
        
        Task& task = task_queue.front();
        auto wait_time = task.getWaitTime();
        
        std::cout << "Processing task after " << wait_time.count() << "ms wait" << std::endl;
        task.execute();
        
        task_queue.pop();
        return true;
    }
    
    // Process all tasks
    void processAllTasks() {
        std::cout << "\n=== Processing All Tasks ===" << std::endl;
        int processed = 0;
        
        while (processNextTask()) {
            processed++;
            // Simulate some processing time
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
        }
        
        std::cout << "Processed " << processed << " tasks" << std::endl;
    }
    
    // Get queue status
    struct QueueStatus {
        size_t pending_tasks;
        bool is_empty;
    };
    
    QueueStatus getStatus() const {
        return {task_queue.size(), task_queue.empty()};
    }
    
    // Display queue contents
    void displayQueue() const {
        std::cout << "\n=== Current Queue ===" << std::endl;
        if (task_queue.empty()) {
            std::cout << "<empty>" << std::endl;
            return;
        }
        
        // Create a copy to display
        std::queue<Task> temp = task_queue;
        int position = 1;
        
        while (!temp.empty()) {
            const Task& task = temp.front();
            auto wait_time = task.getWaitTime();
            std::cout << position++ << ". " << task.getName() 
                      << " (waiting " << wait_time.count() << "ms)" << std::endl;
            temp.pop();
        }
    }
    
    // Clear queue
    void clear() {
        while (!task_queue.empty()) {
            task_queue.pop();
        }
        std::cout << "Queue cleared" << std::endl;
    }
    
    // Check if empty
    bool isEmpty() const {
        return task_queue.empty();
    }
    
    // Get size
    size_t size() const {
        return task_queue.size();
    }
};

int main() {
    TaskScheduler scheduler;
    
    std::cout << "=== Task Scheduler Demo ===" << std::endl;
    
    // Add some tasks
    scheduler.addTask("Initialize System", []() {
        std::cout << "  System initialized" << std::endl;
    });
    
    scheduler.addTask("Load Configuration", []() {
        std::cout << "  Configuration loaded" << std::endl;
    });
    
    scheduler.addTask("Connect to Database", []() {
        std::cout << "  Database connected" << std::endl;
    });
    
    scheduler.addTask("Start Services", []() {
        std::cout << "  Services started" << std::endl;
    });
    
    // Wait a bit before adding more tasks
    std::this_thread::sleep_for(std::chrono::milliseconds(500));
    
    scheduler.addTask("Run Health Check", []() {
        std::cout << "  Health check completed" << std::endl;
    });
    
    // Display queue
    scheduler.displayQueue();
    
    // Process one task
    std::cout << "\n=== Processing One Task ===" << std::endl;
    scheduler.processNextTask();
    scheduler.displayQueue();
    
    // Process all remaining tasks
    scheduler.processAllTasks();
    
    // Show final status
    auto status = scheduler.getStatus();
    std::cout << "\nFinal status: " << status.pending_tasks << " pending tasks" << std::endl;
    
    return 0;
}
```

### Example 2: Breadth-First Search
```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <unordered_set>
#include <string>

class Graph {
private:
    std::vector<std::vector<int>> adjacency_list;
    std::vector<std::string> node_names;
    
public:
    Graph(int size) {
        adjacency_list.resize(size);
        node_names.resize(size);
    }
    
    void setNodeName(int node, const std::string& name) {
        node_names[node] = name;
    }
    
    void addEdge(int from, int to) {
        adjacency_list[from].push_back(to);
        adjacency_list[to].push_back(from);  // Undirected graph
    }
    
    // BFS traversal
    std::vector<int> bfs(int start_node) {
        std::vector<int> traversal_order;
        std::queue<int> queue;
        std::unordered_set<int> visited;
        
        queue.push(start_node);
        visited.insert(start_node);
        
        while (!queue.empty()) {
            int current = queue.front();
            queue.pop();
            
            traversal_order.push_back(current);
            
            // Add unvisited neighbors to queue
            for (int neighbor : adjacency_list[current]) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    queue.push(neighbor);
                }
            }
        }
        
        return traversal_order;
    }
    
    // Find shortest path
    std::vector<int> shortestPath(int start, int end) {
        if (start == end) {
            return {start};
        }
        
        std::queue<int> queue;
        std::unordered_set<int> visited;
        std::vector<int> parent(adjacency_list.size(), -1);
        
        queue.push(start);
        visited.insert(start);
        
        while (!queue.empty()) {
            int current = queue.front();
            queue.pop();
            
            if (current == end) {
                // Reconstruct path
                std::vector<int> path;
                int node = end;
                
                while (node != -1) {
                    path.push_back(node);
                    node = parent[node];
                }
                
                std::reverse(path.begin(), path.end());
                return path;
            }
            
            for (int neighbor : adjacency_list[current]) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    parent[neighbor] = current;
                    queue.push(neighbor);
                }
            }
        }
        
        return {};  // No path found
    }
    
    // Display traversal with names
    void displayTraversal(const std::vector<int>& traversal) const {
        std::cout << "Traversal order: ";
        for (size_t i = 0; i < traversal.size(); ++i) {
            if (i > 0) std::cout << " -> ";
            std::cout << node_names[traversal[i]];
        }
        std::cout << std::endl;
    }
    
    // Display path with names
    void displayPath(const std::vector<int>& path) const {
        if (path.empty()) {
            std::cout << "No path found" << std::endl;
            return;
        }
        
        std::cout << "Path: ";
        for (size_t i = 0; i < path.size(); ++i) {
            if (i > 0) std::cout << " -> ";
            std::cout << node_names[path[i]];
        }
        std::cout << " (length: " << path.size() - 1 << ")" << std::endl;
    }
    
    // Get graph statistics
    struct Statistics {
        int node_count;
        int edge_count;
        bool is_connected;
    };
    
    Statistics getStatistics() {
        Statistics stats = {0, 0, false};
        
        stats.node_count = adjacency_list.size();
        
        for (const auto& neighbors : adjacency_list) {
            stats.edge_count += neighbors.size();
        }
        stats.edge_count /= 2;  // Each edge counted twice in undirected graph
        
        // Check connectivity
        if (stats.node_count > 0) {
            auto traversal = bfs(0);
            stats.is_connected = (traversal.size() == stats.node_count);
        }
        
        return stats;
    }
};

int main() {
    std::cout << "=== BFS Graph Traversal Demo ===" << std::endl;
    
    // Create a graph
    Graph graph(8);
    
    // Set node names
    graph.setNodeName(0, "A");
    graph.setNodeName(1, "B");
    graph.setNodeName(2, "C");
    graph.setNodeName(3, "D");
    graph.setNodeName(4, "E");
    graph.setNodeName(5, "F");
    graph.setNodeName(6, "G");
    graph.setNodeName(7, "H");
    
    // Add edges
    graph.addEdge(0, 1);  // A-B
    graph.addEdge(0, 2);  // A-C
    graph.addEdge(1, 3);  // B-D
    graph.addEdge(1, 4);  // B-E
    graph.addEdge(2, 5);  // C-F
    graph.addEdge(2, 6);  // C-G
    graph.addEdge(3, 7);  // D-H
    graph.addEdge(4, 5);  // E-F
    
    // Test BFS traversal
    std::cout << "\n=== BFS Traversal ===" << std::endl;
    auto traversal = graph.bfs(0);
    graph.displayTraversal(traversal);
    
    // Test shortest path
    std::cout << "\n=== Shortest Path Tests ===" << std::endl;
    
    std::vector<std::pair<int, int>> path_tests = {
        {0, 7},  // A to H
        {4, 6},  // E to G
        {3, 5},  // D to F
        {0, 0}   // A to A
    };
    
    for (const auto& [start, end] : path_tests) {
        std::cout << "Path from " << graph.getNodeName(start) 
                  << " to " << graph.getNodeName(end) << ": ";
        auto path = graph.shortestPath(start, end);
        graph.displayPath(path);
    }
    
    // Test with disconnected node
    std::cout << "\n=== Testing Disconnected Node ===" << std::endl;
    graph.setNodeName(7, "H");
    graph.addEdge(7, 7);  // Self-loop
    
    auto traversal2 = graph.bfs(0);
    graph.displayTraversal(traversal2);
    
    // Show statistics
    auto stats = graph.getStatistics();
    std::cout << "\n=== Graph Statistics ===" << std::endl;
    std::cout << "Nodes: " << stats.node_count << std::endl;
    std::cout << "Edges: " << stats.edge_count << std::endl;
    std::cout << "Connected: " << (stats.is_connected ? "Yes" : "No") << std::endl;
    
    return 0;
}
```

### Example 3: Print Queue System
```cpp
#include <iostream>
#include <queue>
#include <string>
#include <chrono>
#include <random>

enum class PrintPriority {
    LOW = 1,
    MEDIUM = 2,
    HIGH = 3,
    URGENT = 4
};

class PrintJob {
private:
    std::string document_name;
    int pages;
    PrintPriority priority;
    std::chrono::time_point<std::chrono::steady_clock> submitted_at;
    int job_id;
    
public:
    PrintJob(int id, const std::string& name, int page_count, PrintPriority prio)
        : job_id(id), document_name(name), pages(page_count), priority(prio),
          submitted_at(std::chrono::steady_clock::now()) {}
    
    // For priority queue (higher priority first)
    bool operator<(const PrintJob& other) const {
        if (priority != other.priority) {
            return priority < other.priority;  // Higher priority first
        }
        return submitted_at > other.submitted_at;  // Earlier submission first
    }
    
    void execute() const {
        std::cout << "Printing: " << document_name << " (" << pages << " pages, ";
        
        switch (priority) {
            case PrintPriority::LOW: std::cout << "LOW"; break;
            case PrintPriority::MEDIUM: std::cout << "MEDIUM"; break;
            case PrintPriority::HIGH: std::cout << "HIGH"; break;
            case PrintPriority::URGENT: std::cout << "URGENT"; break;
        }
        
        std::cout << ")" << std::endl;
        
        // Simulate printing time
        std::this_thread::sleep_for(std::chrono::milliseconds(pages * 10));
    }
    
    // Getters
    int getId() const { return job_id; }
    const std::string& getDocumentName() const { return document_name; }
    int getPages() const { return pages; }
    PrintPriority getPriority() const { return priority; }
    
    auto getWaitTime() const {
        auto now = std::chrono::steady_clock::now();
        return std::chrono::duration_cast<std::chrono::seconds>(now - submitted_at);
    }
};

class PrintQueue {
private:
    std::queue<PrintJob> regular_queue;
    std::priority_queue<PrintJob> priority_queue;
    int next_job_id;
    
public:
    PrintQueue() : next_job_id(1) {}
    
    // Add regular job
    int addJob(const std::string& document_name, int pages) {
        PrintJob job(next_job_id++, document_name, pages, PrintPriority::MEDIUM);
        regular_queue.push(job);
        
        std::cout << "Added job #" << job.getId() << ": " << document_name 
                  << " (" << pages << " pages)" << std::endl;
        
        return job.getId();
    }
    
    // Add priority job
    int addPriorityJob(const std::string& document_name, int pages, PrintPriority priority) {
        PrintJob job(next_job_id++, document_name, pages, priority);
        priority_queue.push(job);
        
        std::cout << "Added priority job #" << job.getId() << ": " << document_name 
                  << " (" << pages << " pages, ";
        
        switch (priority) {
            case PrintPriority::LOW: std::cout << "LOW"; break;
            case PrintPriority::MEDIUM: std::cout << "MEDIUM"; break;
            case PrintPriority::HIGH: std::cout << "HIGH"; break;
            case PrintPriority::URGENT: std::cout << "URGENT"; break;
        }
        
        std::cout << ")" << std::endl;
        
        return job.getId();
    }
    
    // Process next job (priority jobs first)
    bool processNextJob() {
        if (!priority_queue.empty()) {
            const PrintJob& job = priority_queue.top();
            auto wait_time = job.getWaitTime();
            
            std::cout << "Processing priority job #" << job.getId() 
                      << " after " << wait_time.count() << "s wait" << std::endl;
            job.execute();
            priority_queue.pop();
            return true;
        }
        
        if (!regular_queue.empty()) {
            PrintJob& job = regular_queue.front();
            auto wait_time = job.getWaitTime();
            
            std::cout << "Processing regular job #" << job.getId() 
                      << " after " << wait_time.count() << "s wait" << std::endl;
            job.execute();
            regular_queue.pop();
            return true;
        }
        
        std::cout << "No jobs in queue" << std::endl;
        return false;
    }
    
    // Process all jobs
    void processAllJobs() {
        std::cout << "\n=== Processing All Jobs ===" << std::endl;
        int processed = 0;
        
        while (processNextJob()) {
            processed++;
        }
        
        std::cout << "Processed " << processed << " jobs" << std::endl;
    }
    
    // Get queue statistics
    struct QueueStats {
        size_t regular_jobs;
        size_t priority_jobs;
        size_t total_jobs;
    };
    
    QueueStats getStatistics() const {
        return {
            regular_queue.size(),
            priority_queue.size(),
            regular_queue.size() + priority_queue.size()
        };
    }
    
    // Display queue contents
    void displayQueue() const {
        auto stats = getStatistics();
        
        std::cout << "\n=== Print Queue Status ===" << std::endl;
        std::cout << "Regular jobs: " << stats.regular_jobs << std::endl;
        std::cout << "Priority jobs: " << stats.priority_jobs << std::endl;
        std::cout << "Total jobs: " << stats.total_jobs << std::endl;
        
        if (stats.priority_jobs > 0) {
            std::cout << "\nPriority queue:" << std::endl;
            
            // Create copy to display
            std::priority_queue<PrintJob> temp = priority_queue;
            std::vector<PrintJob> jobs;
            
            while (!temp.empty()) {
                jobs.push_back(temp.top());
                temp.pop();
            }
            
            // Display in order
            std::reverse(jobs.begin(), jobs.end());
            for (const auto& job : jobs) {
                auto wait_time = job.getWaitTime();
                std::cout << "  #" << job.getId() << ": " << job.getDocumentName()
                          << " (wait " << wait_time.count() << "s)" << std::endl;
            }
        }
        
        if (stats.regular_jobs > 0) {
            std::cout << "\nRegular queue:" << std::endl;
            
            // Create copy to display
            std::queue<PrintJob> temp = regular_queue;
            int position = 1;
            
            while (!temp.empty()) {
                const PrintJob& job = temp.front();
                auto wait_time = job.getWaitTime();
                std::cout << "  " << position++ << ". #" << job.getId() << ": " 
                          << job.getDocumentName() << " (wait " << wait_time.count() << "s)" << std::endl;
                temp.pop();
            }
        }
    }
    
    // Clear all jobs
    void clear() {
        while (!regular_queue.empty()) {
            regular_queue.pop();
        }
        while (!priority_queue.empty()) {
            priority_queue.pop();
        }
        std::cout << "Queue cleared" << std::endl;
    }
};

int main() {
    PrintQueue print_queue;
    
    std::cout << "=== Print Queue System Demo ===" << std::endl;
    
    // Add some regular jobs
    print_queue.addJob("Document1.pdf", 5);
    print_queue.addJob("Report.docx", 12);
    print_queue.addJob("Presentation.pptx", 20);
    
    // Wait a bit
    std::this_thread::sleep_for(std::chrono::milliseconds(500));
    
    // Add priority jobs
    print_queue.addPriorityJob("Urgent_Memo.pdf", 2, PrintPriority::URGENT);
    print_queue.addPriorityJob("Invoice.pdf", 1, PrintPriority::HIGH);
    print_queue.addPriorityJob("Meeting_Notes.pdf", 3, PrintPriority::MEDIUM);
    
    // Add more regular jobs
    print_queue.addJob("Spreadsheet.xlsx", 8);
    print_queue.addJob("Email_Eml.eml", 1);
    
    // Display queue
    print_queue.displayQueue();
    
    // Process a few jobs
    std::cout << "\n=== Processing Some Jobs ===" << std::endl;
    print_queue.processNextJob();
    print_queue.processNextJob();
    print_queue.processNextJob();
    
    print_queue.displayQueue();
    
    // Process remaining jobs
    std::cout << "\n=== Processing Remaining Jobs ===" << std::endl;
    print_queue.processAllJobs();
    
    // Show final statistics
    auto final_stats = print_queue.getStatistics();
    std::cout << "\nFinal queue status: " << final_stats.total_jobs << " jobs remaining" << std::endl;
    
    return 0;
}
```

### Example 4: Message Queue System
```cpp
#include <iostream>
#include <queue>
#include <string>
#include <functional>
#include <mutex>
#include <condition_variable>
#include <thread>
#include <atomic>

enum class MessageType {
    INFO,
    WARNING,
    ERROR,
    COMMAND
};

class Message {
private:
    MessageType type;
    std::string content;
    std::string sender;
    std::chrono::time_point<std::chrono::steady_clock> timestamp;
    
public:
    Message(MessageType msg_type, const std::string& msg_content, const std::string& msg_sender)
        : type(msg_type), content(msg_content), sender(msg_sender),
          timestamp(std::chrono::steady_clock::now()) {}
    
    MessageType getType() const { return type; }
    const std::string& getContent() const { return content; }
    const std::string& getSender() const { return sender; }
    
    auto getAge() const {
        auto now = std::chrono::steady_clock::now();
        return std::chrono::duration_cast<std::chrono::milliseconds>(now - timestamp);
    }
    
    std::string getTypeString() const {
        switch (type) {
            case MessageType::INFO: return "INFO";
            case MessageType::WARNING: return "WARNING";
            case MessageType::ERROR: return "ERROR";
            case MessageType::COMMAND: return "COMMAND";
            default: return "UNKNOWN";
        }
    }
};

class MessageQueue {
private:
    std::queue<Message> message_queue;
    mutable std::mutex queue_mutex;
    std::condition_variable condition_var;
    std::atomic<bool> is_running{true};
    
    // Message handlers
    std::function<void(const Message&)> info_handler;
    std::function<void(const Message&)> warning_handler;
    std::function<void(const Message&)> error_handler;
    std::function<void(const Message&)> command_handler;
    
public:
    // Set message handlers
    void setInfoHandler(std::function<void(const Message&)> handler) {
        info_handler = handler;
    }
    
    void setWarningHandler(std::function<void(const Message&)> handler) {
        warning_handler = handler;
    }
    
    void setErrorHandler(std::function<void(const Message&)> handler) {
        error_handler = handler;
    }
    
    void setCommandHandler(std::function<void(const Message&)> handler) {
        command_handler = handler;
    }
    
    // Post message to queue
    void postMessage(MessageType type, const std::string& content, const std::string& sender) {
        std::lock_guard<std::mutex> lock(queue_mutex);
        message_queue.emplace(type, content, sender);
        condition_var.notify_one();
    }
    
    // Process next message (blocking)
    bool processNextMessage() {
        std::unique_lock<std::mutex> lock(queue_mutex);
        
        // Wait for message or shutdown
        condition_var.wait(lock, [this] { return !message_queue.empty() || !is_running; });
        
        if (!is_running && message_queue.empty()) {
            return false;
        }
        
        Message message = message_queue.front();
        message_queue.pop();
        lock.unlock();
        
        // Process message
        handleMessage(message);
        return true;
    }
    
    // Process messages asynchronously
    void startProcessing() {
        std::thread processor([this]() {
            while (processNextMessage()) {
                // Continue processing
            }
            std::cout << "Message processor stopped" << std::endl;
        });
        processor.detach();
    }
    
    // Stop processing
    void stop() {
        is_running = false;
        condition_var.notify_all();
    }
    
    // Get queue statistics
    struct QueueStats {
        size_t message_count;
        bool is_active;
    };
    
    QueueStats getStatistics() const {
        std::lock_guard<std::mutex> lock(queue_mutex);
        return {message_queue.size(), is_running};
    }
    
    // Clear queue
    void clear() {
        std::lock_guard<std::mutex> lock(queue_mutex);
        while (!message_queue.empty()) {
            message_queue.pop();
        }
        std::cout << "Message queue cleared" << std::endl;
    }
    
private:
    void handleMessage(const Message& message) {
        auto age = message.getAge();
        
        std::cout << "[" << message.getTypeString() << "] " 
                  << message.getSender() << ": " << message.getContent()
                  << " (age: " << age.count() << "ms)" << std::endl;
        
        // Call appropriate handler
        switch (message.getType()) {
            case MessageType::INFO:
                if (info_handler) info_handler(message);
                break;
            case MessageType::WARNING:
                if (warning_handler) warning_handler(message);
                break;
            case MessageType::ERROR:
                if (error_handler) error_handler(message);
                break;
            case MessageType::COMMAND:
                if (command_handler) command_handler(message);
                break;
        }
    }
};

// Demo application
class ChatSystem {
private:
    MessageQueue message_queue;
    std::string username;
    
public:
    ChatSystem(const std::string& user) : username(user) {
        // Set up message handlers
        message_queue.setInfoHandler([this](const Message& msg) {
            std::cout << "  → Displayed info message" << std::endl;
        });
        
        message_queue.setWarningHandler([this](const Message& msg) {
            std::cout << "  ⚠ Displayed warning message" << std::endl;
        });
        
        message_queue.setErrorHandler([this](const Message& msg) {
            std::cout << "  ✗ Displayed error message" << std::endl;
        });
        
        message_queue.setCommandHandler([this](const Message& msg) {
            std::cout << "  → Executed command: " << msg.getContent() << std::endl;
        });
    }
    
    void start() {
        message_queue.startProcessing();
        std::cout << "Chat system started for " << username << std::endl;
    }
    
    void sendMessage(MessageType type, const std::string& content) {
        message_queue.postMessage(type, content, username);
    }
    
    void simulateIncomingMessages() {
        // Simulate messages from other users
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        message_queue.postMessage(MessageType::INFO, "Hello everyone!", "Alice");
        
        std::this_thread::sleep_for(std::chrono::milliseconds(200));
        message_queue.postMessage(MessageType::WARNING, "Server will restart in 5 minutes", "System");
        
        std::this_thread::sleep_for(std::chrono::milliseconds(150));
        message_queue.postMessage(MessageType::ERROR, "Connection lost", "Bob");
        
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        message_queue.postMessage(MessageType::COMMAND, "help", "Charlie");
        
        std::this_thread::sleep_for(std::chrono::milliseconds(200));
        message_queue.postMessage(MessageType::INFO, "Connection restored", "System");
    }
    
    void stop() {
        message_queue.stop();
        std::cout << "Chat system stopped" << std::endl;
    }
    
    MessageQueue& getQueue() { return message_queue; }
};

int main() {
    std::cout << "=== Message Queue System Demo ===" << std::endl;
    
    ChatSystem chat("User123");
    chat.start();
    
    // Send some messages
    chat.sendMessage(MessageType::INFO, "Hi there!");
    chat.sendMessage(MessageType::WARNING, "Running low on memory");
    chat.sendMessage(MessageType::ERROR, "File not found");
    chat.sendMessage(MessageType::COMMAND, "status");
    
    // Simulate incoming messages
    std::thread incoming(&ChatSystem::simulateIncomingMessages, &chat);
    
    // Wait a bit
    std::this_thread::sleep_for(std::chrono::seconds(2));
    
    // Show statistics
    auto stats = chat.getQueue().getStatistics();
    std::cout << "\nQueue statistics: " << stats.message_count 
              << " messages, active: " << (stats.is_active ? "Yes" : "No") << std::endl;
    
    // Send more messages
    chat.sendMessage(MessageType::INFO, "Still here!");
    chat.sendMessage(MessageType::COMMAND, "shutdown");
    
    // Wait for processing
    std::this_thread::sleep_for(std::chrono::seconds(1));
    
    // Stop system
    chat.stop();
    incoming.join();
    
    return 0;
}
```

## 📊 Complete Function Reference

### Element Access
| Function | Description | Complexity |
|----------|-------------|------------|
| `front()` | Access front element | O(1) |
| `back()` | Access back element | O(1) |

### Capacity
| Function | Description | Complexity |
|----------|-------------|------------|
| `empty()` | Check if empty | O(1) |
| `size()` | Get number of elements | O(1) |

### Modifiers
| Function | Description | Complexity |
|----------|-------------|------------|
| `push()` | Insert element at back | O(1) |
| `emplace()` | Construct element in place | O(1) |
| `pop()` | Remove front element | O(1) |
| `swap()` | Swap contents | O(1) |

## ⚡ Performance Considerations

### Container Choice
```cpp
// Different underlying containers have different performance characteristics

// std::deque (default) - good all-around performance
std::queue<int> deque_queue;  // O(1) push/pop, good memory locality

// std::list - no reallocation, but poor cache locality
std::queue<int, std::list<int>> list_queue;  // O(1) push/pop, scattered memory
```

### Memory Usage
```cpp
// Queue memory usage depends on underlying container
// deque: segmented blocks, good for large queues
// list: per-node overhead, highest memory usage per element
```

## 🎯 Common Patterns

### Pattern 1: Level Order Traversal
```cpp
template<typename T>
void levelOrderTraversal(const std::vector<std::vector<T>>& tree, int root) {
    std::queue<int> queue;
    queue.push(root);
    
    while (!queue.empty()) {
        int current = queue.front();
        queue.pop();
        
        std::cout << tree[current][0] << " ";  // Visit node
        
        // Add children to queue
        for (size_t i = 1; i < tree[current].size(); ++i) {
            queue.push(tree[current][i]);
        }
    }
}
```

### Pattern 2: Sliding Window Maximum
```cpp
std::vector<int> slidingWindowMaximum(const std::vector<int>& nums, int k) {
    std::deque<int> window;  // Store indices
    std::vector<int> result;
    
    for (int i = 0; i < nums.size(); ++i) {
        // Remove indices out of window
        while (!window.empty() && window.front() <= i - k) {
            window.pop_front();
        }
        
        // Remove smaller elements
        while (!window.empty() && nums[window.back()] <= nums[i]) {
            window.pop_back();
        }
        
        window.push_back(i);
        
        // Add maximum to result
        if (i >= k - 1) {
            result.push_back(nums[window.front()]);
        }
    }
    
    return result;
}
```

## 🐛 Common Pitfalls & Solutions

### 1. Accessing Empty Queue
```cpp
// Problem - accessing front/back of empty queue
std::queue<int> q;
int value = q.front();  // Undefined behavior!

// Solution - always check if empty
if (!q.empty()) {
    int value = q.front();
    // Use value safely
}
```

### 2. No Direct Iteration
```cpp
// Problem - trying to iterate through queue
std::queue<int> q;
for (const auto& item : q) {  // Error: no begin/end
    std::cout << item << std::endl;
}

// Solution - use a copy or different container
std::queue<int> temp = q;
while (!temp.empty()) {
    std::cout << temp.front() << std::endl;
    temp.pop();
}
```

### 3. Using Wrong Container
```cpp
// Problem - using vector as underlying container
std::queue<int, std::vector<int>> q;  // Inefficient pop_front

// Solution - use deque or list
std::queue<int> q;  // Uses deque by default - good choice
// Or explicitly:
std::queue<int, std::list<int>> q;  // Good for frequent pops
```

## 📚 Related Headers

- `stack.md` - LIFO container adapter
- `deque.md` - Double-ended queue (default underlying container)
- `vector.md` - Dynamic array (inefficient underlying container)
- `list.md` - Doubly linked list (alternative underlying container)
- `priority_queue.md` - Priority queue adapter

## 🚀 Best Practices

1. **Use default queue** unless you have specific performance requirements
2. **Always check empty()** before calling front(), back(), or pop()
3. **Choose appropriate underlying container** based on usage patterns
4. **Use emplace()** for complex types to avoid unnecessary copies
5. **Use std::deque** for balanced performance (default choice)
6. **Use std::list** if you need frequent pops from front

## 🎯 When to Use queue

✅ **Use queue when:**
- Need FIFO (First-In, First-Out) behavior
- Implementing BFS algorithms
- Task scheduling and job processing
- Message passing systems
- Buffering data streams
- Print queue management
- Need restricted interface (front/back only)

❌ **Avoid when:**
- Need random access to elements (use `vector`)
- Need LIFO behavior (use `stack`)
- Need priority-based processing (use `priority_queue`)
- Need to access elements in middle
- Need to iterate through all elements
---

## Next Step

- Go to [21_priority_queue.md](21_priority_queue.md) to continue with priority queue.
