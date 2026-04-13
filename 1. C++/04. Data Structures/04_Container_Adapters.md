# Container Adapters in C++

## Overview
Container adapters are specialized containers that provide restricted interfaces to underlying containers. They are not full-fledged containers but rather wrappers that modify the behavior of sequence containers to implement specific data structures. C++ provides three container adapters: `std::stack` (LIFO), `std::queue` (FIFO), and `std::priority_queue` (heap-based priority queue).

## Key Characteristics

| Adapter | Underlying Container | Access Pattern | Key Operations |
|---------|---------------------|----------------|----------------|
| stack | deque (default) | LIFO (Last In, First Out) | push, pop, top |
| queue | deque (default) | FIFO (First In, First Out) | push, pop, front, back |
| priority_queue | vector (default) | Highest priority first | push, pop, top |

---

## 1. std::stack (LIFO - Last In, First Out)

### Theory
`std::stack` implements a stack data structure where elements are inserted and removed only from the top. It follows the LIFO (Last In, First Out) principle. The underlying container can be `std::deque` (default), `std::vector`, or `std::list`.

**Use Cases:**
- Function call stack management
- Expression evaluation (postfix/infix conversion)
- Undo/Redo operations
- Backtracking algorithms
- Depth-First Search (DFS)
- Parsing and syntax checking

**Time Complexity:**
- push: O(1)
- pop: O(1)
- top: O(1)
- size: O(1)

### All Functions and Operations

```cpp
#include <iostream>
#include <stack>
#include <vector>
#include <list>
#include <string>

void demonstrateStack() {
    std::cout << "\n========== STD::STACK ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default stack (uses deque)
    std::stack<int> s1;
    
    // Stack with different underlying container
    std::stack<int, std::vector<int>> s2;           // Using vector
    std::stack<int, std::list<int>> s3;             // Using list
    
    // Stack from existing container
    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::stack<int, std::vector<int>> s4(vec);      // Copy from vector
    
    // ==================== PUSHING ELEMENTS ====================
    std::cout << "\n--- Pushing Elements ---\n";
    
    std::stack<int> push_stack;
    
    // push - add element to top
    push_stack.push(10);
    push_stack.push(20);
    push_stack.push(30);
    
    std::cout << "Stack after pushes: ";
    std::stack<int> temp = push_stack;              // Copy for display
    while (!temp.empty()) {
        std::cout << temp.top() << " ";
        temp.pop();
    }
    std::cout << "\n";
    
    // emplace (C++11) - construct in place
    struct Person {
        std::string name;
        int age;
        Person(std::string n, int a) : name(std::move(n)), age(a) {}
    };
    
    std::stack<Person> person_stack;
    person_stack.emplace("Alice", 25);              // Constructs in place
    person_stack.emplace("Bob", 30);
    std::cout << "Top person: " << person_stack.top().name << "\n";
    
    // ==================== POPPING ELEMENTS ====================
    std::cout << "\n--- Popping Elements ---\n";
    
    std::stack<int> pop_stack;
    for (int i = 1; i <= 5; i++) {
        pop_stack.push(i * 10);
    }
    
    std::cout << "Popping all elements: ";
    while (!pop_stack.empty()) {
        std::cout << pop_stack.top() << " ";
        pop_stack.pop();
    }
    std::cout << "\n";
    std::cout << "Stack empty? " << (pop_stack.empty() ? "Yes" : "No") << "\n";
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::stack<int> access_stack;
    access_stack.push(100);
    access_stack.push(200);
    access_stack.push(300);
    
    std::cout << "Top element: " << access_stack.top() << "\n";
    
    // Note: No direct access to bottom elements
    // Must pop to access lower elements
    
    // ==================== SIZE OPERATIONS ====================
    std::cout << "\n--- Size Operations ---\n";
    
    std::stack<int> size_stack;
    std::cout << "Initial size: " << size_stack.size() << "\n";
    
    size_stack.push(1);
    size_stack.push(2);
    size_stack.push(3);
    std::cout << "After pushes - Size: " << size_stack.size() << "\n";
    
    size_stack.pop();
    std::cout << "After pop - Size: " << size_stack.size() << "\n";
    
    // ==================== SWAPPING ====================
    std::cout << "\n--- Swapping ---\n";
    
    std::stack<int> swap1;
    std::stack<int> swap2;
    
    for (int i = 1; i <= 3; i++) swap1.push(i);
    for (int i = 10; i <= 13; i++) swap2.push(i);
    
    std::cout << "Before swap - swap1 top: " << swap1.top() << ", swap2 top: " << swap2.top() << "\n";
    
    swap1.swap(swap2);
    
    std::cout << "After swap - swap1 top: " << swap1.top() << ", swap2 top: " << swap2.top() << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Browser History (Back/Forward)
    std::cout << "\n--- Example 1: Browser History ---\n";
    
    std::stack<std::string> back_stack;
    std::stack<std::string> forward_stack;
    std::string current_page = "Home";
    
    auto visitPage = [&](const std::string& page) {
        back_stack.push(current_page);
        current_page = page;
        // Clear forward stack on new visit
        while (!forward_stack.empty()) forward_stack.pop();
        std::cout << "Visited: " << current_page << "\n";
    };
    
    auto goBack = [&]() {
        if (!back_stack.empty()) {
            forward_stack.push(current_page);
            current_page = back_stack.top();
            back_stack.pop();
            std::cout << "Back to: " << current_page << "\n";
        } else {
            std::cout << "No back history\n";
        }
    };
    
    auto goForward = [&]() {
        if (!forward_stack.empty()) {
            back_stack.push(current_page);
            current_page = forward_stack.top();
            forward_stack.pop();
            std::cout << "Forward to: " << current_page << "\n";
        } else {
            std::cout << "No forward history\n";
        }
    };
    
    visitPage("Google");
    visitPage("GitHub");
    visitPage("StackOverflow");
    goBack();
    goBack();
    goForward();
    
    // Example 2: Balanced Parentheses Check
    std::cout << "\n--- Example 2: Balanced Parentheses ---\n";
    
    auto isBalanced = [](const std::string& expr) -> bool {
        std::stack<char> st;
        
        for (char c : expr) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
                if (st.empty()) return false;
                
                char top = st.top();
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
                st.pop();
            }
        }
        
        return st.empty();
    };
    
    std::string expr1 = "{[()]}";
    std::string expr2 = "{[(])}";
    std::string expr3 = "((()))";
    
    std::cout << expr1 << " is balanced? " << (isBalanced(expr1) ? "Yes" : "No") << "\n";
    std::cout << expr2 << " is balanced? " << (isBalanced(expr2) ? "Yes" : "No") << "\n";
    std::cout << expr3 << " is balanced? " << (isBalanced(expr3) ? "Yes" : "No") << "\n";
    
    // Example 3: Postfix Expression Evaluation
    std::cout << "\n--- Example 3: Postfix Evaluation ---\n";
    
    auto evaluatePostfix = [](const std::string& expr) -> int {
        std::stack<int> st;
        
        for (char c : expr) {
            if (isdigit(c)) {
                st.push(c - '0');
            } else {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                
                switch (c) {
                    case '+': st.push(a + b); break;
                    case '-': st.push(a - b); break;
                    case '*': st.push(a * b); break;
                    case '/': st.push(a / b); break;
                }
            }
        }
        
        return st.top();
    };
    
    std::cout << "Postfix '23+': " << evaluatePostfix("23+") << "\n";
    std::cout << "Postfix '23*5+': " << evaluatePostfix("23*5+") << "\n";
    std::cout << "Postfix '45+7*': " << evaluatePostfix("45+7*") << "\n";
    
    // Example 4: Stack using different underlying containers
    std::cout << "\n--- Example 4: Different Underlying Containers ---\n";
    
    // Using vector (faster, but reallocation may occur)
    std::stack<int, std::vector<int>> vec_stack;
    vec_stack.push(1);
    vec_stack.push(2);
    vec_stack.push(3);
    std::cout << "Vector-based stack top: " << vec_stack.top() << "\n";
    
    // Using list (no reallocation, but more memory overhead)
    std::stack<int, std::list<int>> list_stack;
    list_stack.push(10);
    list_stack.push(20);
    list_stack.push(30);
    std::cout << "List-based stack top: " << list_stack.top() << "\n";
}
```

---

## 2. std::queue (FIFO - First In, First Out)

### Theory
`std::queue` implements a queue data structure where elements are inserted at the back and removed from the front. It follows the FIFO (First In, First Out) principle. The underlying container can be `std::deque` (default) or `std::list`.

**Use Cases:**
- Task scheduling (printer queue, CPU scheduling)
- Breadth-First Search (BFS)
- Buffer management
- Message passing systems
- Request handling

**Time Complexity:**
- push: O(1)
- pop: O(1)
- front: O(1)
- back: O(1)
- size: O(1)

### All Functions and Operations

```cpp
#include <iostream>
#include <queue>
#include <list>
#include <string>
#include <chrono>
#include <thread>

void demonstrateQueue() {
    std::cout << "\n========== STD::QUEUE ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default queue (uses deque)
    std::queue<int> q1;
    
    // Queue with different underlying container
    std::queue<int, std::list<int>> q2;                 // Using list
    
    // Queue from existing container
    std::list<int> lst = {1, 2, 3, 4, 5};
    std::queue<int, std::list<int>> q3(lst);            // Copy from list
    
    // ==================== PUSHING ELEMENTS ====================
    std::cout << "\n--- Pushing Elements ---\n";
    
    std::queue<int> push_queue;
    
    // push - add element to back
    push_queue.push(10);
    push_queue.push(20);
    push_queue.push(30);
    
    std::cout << "Queue after pushes (front to back): ";
    std::queue<int> temp = push_queue;
    while (!temp.empty()) {
        std::cout << temp.front() << " ";
        temp.pop();
    }
    std::cout << "\n";
    
    // emplace (C++11) - construct in place
    struct Task {
        std::string name;
        int priority;
        Task(std::string n, int p) : name(std::move(n)), priority(p) {}
    };
    
    std::queue<Task> task_queue;
    task_queue.emplace("Task 1", 1);
    task_queue.emplace("Task 2", 2);
    std::cout << "Front task: " << task_queue.front().name << "\n";
    
    // ==================== POPPING ELEMENTS ====================
    std::cout << "\n--- Popping Elements ---\n";
    
    std::queue<int> pop_queue;
    for (int i = 1; i <= 5; i++) {
        pop_queue.push(i * 10);
    }
    
    std::cout << "Popping all elements: ";
    while (!pop_queue.empty()) {
        std::cout << pop_queue.front() << " ";
        pop_queue.pop();
    }
    std::cout << "\n";
    std::cout << "Queue empty? " << (pop_queue.empty() ? "Yes" : "No") << "\n";
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::queue<int> access_queue;
    access_queue.push(100);
    access_queue.push(200);
    access_queue.push(300);
    
    std::cout << "Front element: " << access_queue.front() << "\n";
    std::cout << "Back element: " << access_queue.back() << "\n";
    
    // ==================== SIZE OPERATIONS ====================
    std::cout << "\n--- Size Operations ---\n";
    
    std::queue<int> size_queue;
    std::cout << "Initial size: " << size_queue.size() << "\n";
    
    size_queue.push(1);
    size_queue.push(2);
    size_queue.push(3);
    std::cout << "After pushes - Size: " << size_queue.size() << "\n";
    
    size_queue.pop();
    std::cout << "After pop - Size: " << size_queue.size() << "\n";
    
    // ==================== SWAPPING ====================
    std::cout << "\n--- Swapping ---\n";
    
    std::queue<int> swap1;
    std::queue<int> swap2;
    
    for (int i = 1; i <= 3; i++) swap1.push(i);
    for (int i = 10; i <= 13; i++) swap2.push(i);
    
    std::cout << "Before swap - swap1 front: " << swap1.front() 
              << ", swap2 front: " << swap2.front() << "\n";
    
    swap1.swap(swap2);
    
    std::cout << "After swap - swap1 front: " << swap1.front() 
              << ", swap2 front: " << swap2.front() << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Printer Queue Simulation
    std::cout << "\n--- Example 1: Printer Queue ---\n";
    
    struct PrintJob {
        std::string document;
        int pages;
        PrintJob(std::string doc, int p) : document(doc), pages(p) {}
    };
    
    std::queue<PrintJob> printer_queue;
    
    auto addJob = [&](const std::string& doc, int pages) {
        printer_queue.emplace(doc, pages);
        std::cout << "Added: " << doc << " (" << pages << " pages)\n";
    };
    
    auto processJob = [&]() {
        if (!printer_queue.empty()) {
            PrintJob job = printer_queue.front();
            printer_queue.pop();
            std::cout << "Printing: " << job.document << " (" << job.pages << " pages)\n";
            return true;
        }
        std::cout << "No jobs to print\n";
        return false;
    };
    
    addJob("Resume.pdf", 2);
    addJob("Report.docx", 5);
    addJob("Photo.jpg", 1);
    
    std::cout << "\nProcessing queue:\n";
    while (!printer_queue.empty()) {
        processJob();
    }
    
    // Example 2: BFS for Graph Traversal
    std::cout << "\n--- Example 2: BFS Traversal ---\n";
    
    // Adjacency list representation
    std::vector<std::vector<int>> graph = {
        {1, 2},     // Node 0 connected to 1, 2
        {0, 3, 4},  // Node 1 connected to 0, 3, 4
        {0, 5},     // Node 2 connected to 0, 5
        {1},        // Node 3 connected to 1
        {1},        // Node 4 connected to 1
        {2}         // Node 5 connected to 2
    };
    
    auto bfs = [&](int start) {
        std::queue<int> q;
        std::vector<bool> visited(graph.size(), false);
        
        q.push(start);
        visited[start] = true;
        
        std::cout << "BFS starting from node " << start << ": ";
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            std::cout << node << " ";
            
            for (int neighbor : graph[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        std::cout << "\n";
    };
    
    bfs(0);
    
    // Example 3: Circular Buffer / Ring Buffer using Queue
    std::cout << "\n--- Example 3: Circular Buffer Simulation ---\n";
    
    class CircularBuffer {
    private:
        std::queue<int> buffer;
        size_t max_size;
        
    public:
        CircularBuffer(size_t size) : max_size(size) {}
        
        void push(int value) {
            if (buffer.size() >= max_size) {
                buffer.pop();  // Remove oldest
            }
            buffer.push(value);
        }
        
        void display() {
            std::queue<int> temp = buffer;
            std::cout << "Buffer: ";
            while (!temp.empty()) {
                std::cout << temp.front() << " ";
                temp.pop();
            }
            std::cout << "\n";
        }
        
        double average() {
            if (buffer.empty()) return 0;
            double sum = 0;
            std::queue<int> temp = buffer;
            while (!temp.empty()) {
                sum += temp.front();
                temp.pop();
            }
            return sum / buffer.size();
        }
    };
    
    CircularBuffer circ_buf(5);
    for (int i = 1; i <= 7; i++) {
        circ_buf.push(i);
        circ_buf.display();
        std::cout << "Average: " << circ_buf.average() << "\n";
    }
    
    // Example 4: Queue using different underlying containers
    std::cout << "\n--- Example 4: Different Underlying Containers ---\n";
    
    // Using list (no reallocation, but more memory overhead)
    std::queue<int, std::list<int>> list_queue;
    list_queue.push(10);
    list_queue.push(20);
    list_queue.push(30);
    std::cout << "List-based queue front: " << list_queue.front() 
              << ", back: " << list_queue.back() << "\n";
}
```

---

## 3. std::priority_queue (Heap-Based Priority Queue)

### Theory
`std::priority_queue` implements a priority queue where the element with the highest priority (largest value by default) is always at the top. It's typically implemented as a binary heap. The underlying container is usually `std::vector` (default) or `std::deque`.

**Use Cases:**
- Dijkstra's shortest path algorithm
- Huffman coding
- Task scheduling with priorities
- Event-driven simulation
- K-way merge algorithms
- Median maintenance

**Time Complexity:**
- push: O(log n)
- pop: O(log n)
- top: O(1)
- size: O(1)

### All Functions and Operations

```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <functional>
#include <string>
#include <chrono>
#include <random>

void demonstratePriorityQueue() {
    std::cout << "\n========== STD::PRIORITY_QUEUE ==========\n";
    
    // ==================== CONSTRUCTORS & INITIALIZATION ====================
    std::cout << "\n--- Constructors & Initialization ---\n";
    
    // Default max-heap (largest element on top)
    std::priority_queue<int> pq1;
    
    // Min-heap using greater comparator
    std::priority_queue<int, std::vector<int>, std::greater<int>> pq2;
    
    // With custom comparator
    auto cmp = [](int left, int right) { return left > right; };
    std::priority_queue<int, std::vector<int>, decltype(cmp)> pq3(cmp);
    
    // Initialize from vector
    std::vector<int> vec = {3, 1, 4, 1, 5, 9, 2, 6};
    std::priority_queue<int> pq4(vec.begin(), vec.end());
    
    // ==================== MAX-HEAP (Default) ====================
    std::cout << "\n--- Max-Heap (Largest on Top) ---\n";
    
    std::priority_queue<int> max_heap;
    
    // push elements
    max_heap.push(10);
    max_heap.push(30);
    max_heap.push(20);
    max_heap.push(50);
    max_heap.push(40);
    
    std::cout << "Max-heap elements in order: ";
    while (!max_heap.empty()) {
        std::cout << max_heap.top() << " ";
        max_heap.pop();
    }
    std::cout << "\n";
    
    // ==================== MIN-HEAP ====================
    std::cout << "\n--- Min-Heap (Smallest on Top) ---\n";
    
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
    
    min_heap.push(10);
    min_heap.push(30);
    min_heap.push(20);
    min_heap.push(50);
    min_heap.push(40);
    
    std::cout << "Min-heap elements in order: ";
    while (!min_heap.empty()) {
        std::cout << min_heap.top() << " ";
        min_heap.pop();
    }
    std::cout << "\n";
    
    // ==================== PUSHING ELEMENTS ====================
    std::cout << "\n--- Pushing Elements ---\n";
    
    std::priority_queue<int> push_pq;
    push_pq.push(5);
    push_pq.push(3);
    push_pq.push(8);
    push_pq.push(1);
    push_pq.push(9);
    
    std::cout << "After pushes, top: " << push_pq.top() << "\n";
    
    // emplace (C++11) - construct in place
    struct Task {
        std::string name;
        int priority;
        Task(std::string n, int p) : name(std::move(n)), priority(p) {}
        
        // For priority_queue, we need comparison operators
        bool operator<(const Task& other) const {
            return priority < other.priority;  // Higher priority = larger value
        }
    };
    
    std::priority_queue<Task> task_pq;
    task_pq.emplace("Critical", 10);
    task_pq.emplace("Normal", 5);
    task_pq.emplace("Low", 1);
    task_pq.emplace("High", 8);
    
    std::cout << "Top priority task: " << task_pq.top().name 
              << " (priority " << task_pq.top().priority << ")\n";
    
    // ==================== POPPING ELEMENTS ====================
    std::cout << "\n--- Popping Elements ---\n";
    
    std::priority_queue<int> pop_pq;
    for (int i : {5, 2, 8, 1, 9, 3, 7, 4, 6}) {
        pop_pq.push(i);
    }
    
    std::cout << "Popping in priority order: ";
    while (!pop_pq.empty()) {
        std::cout << pop_pq.top() << " ";
        pop_pq.pop();
    }
    std::cout << "\n";
    
    // ==================== ACCESSING ELEMENTS ====================
    std::cout << "\n--- Accessing Elements ---\n";
    
    std::priority_queue<int> access_pq;
    access_pq.push(100);
    access_pq.push(200);
    access_pq.push(300);
    
    std::cout << "Top element (highest priority): " << access_pq.top() << "\n";
    
    // ==================== SIZE OPERATIONS ====================
    std::cout << "\n--- Size Operations ---\n";
    
    std::priority_queue<int> size_pq;
    std::cout << "Initial size: " << size_pq.size() << "\n";
    std::cout << "Empty? " << (size_pq.empty() ? "Yes" : "No") << "\n";
    
    size_pq.push(1);
    size_pq.push(2);
    size_pq.push(3);
    std::cout << "After pushes - Size: " << size_pq.size() << "\n";
    std::cout << "Empty? " << (size_pq.empty() ? "Yes" : "No") << "\n";
    
    size_pq.pop();
    std::cout << "After pop - Size: " << size_pq.size() << "\n";
    
    // ==================== SWAPPING ====================
    std::cout << "\n--- Swapping ---\n";
    
    std::priority_queue<int> swap1;
    std::priority_queue<int> swap2;
    
    for (int i = 1; i <= 3; i++) swap1.push(i);
    for (int i = 10; i <= 13; i++) swap2.push(i);
    
    std::cout << "Before swap - swap1 top: " << swap1.top() 
              << ", swap2 top: " << swap2.top() << "\n";
    
    swap1.swap(swap2);
    
    std::cout << "After swap - swap1 top: " << swap1.top() 
              << ", swap2 top: " << swap2.top() << "\n";
    
    // ==================== PRACTICAL EXAMPLES ====================
    
    // Example 1: Task Scheduler with Priorities
    std::cout << "\n--- Example 1: Task Scheduler ---\n";
    
    struct ScheduledTask {
        std::string name;
        int priority;
        std::chrono::steady_clock::time_point enqueue_time;
        
        ScheduledTask(std::string n, int p) 
            : name(std::move(n)), priority(p), 
              enqueue_time(std::chrono::steady_clock::now()) {}
        
        // Higher priority = larger value
        bool operator<(const ScheduledTask& other) const {
            return priority < other.priority;
        }
        
        void execute() const {
            auto now = std::chrono::steady_clock::now();
            auto wait_time = std::chrono::duration_cast<std::chrono::milliseconds>
                            (now - enqueue_time).count();
            std::cout << "Executing: " << name << " (priority " << priority 
                      << ", waited " << wait_time << "ms)\n";
        }
    };
    
    std::priority_queue<ScheduledTask> scheduler;
    
    scheduler.emplace("Critical System Update", 10);
    scheduler.emplace("User Interface Refresh", 3);
    scheduler.emplace("Background Logging", 1);
    scheduler.emplace("Data Processing", 5);
    scheduler.emplace("Network Request", 7);
    
    std::cout << "\nProcessing tasks by priority:\n";
    while (!scheduler.empty()) {
        auto task = scheduler.top();
        task.execute();
        scheduler.pop();
    }
    
    // Example 2: Find K Largest Elements
    std::cout << "\n--- Example 2: Find K Largest Elements ---\n";
    
    auto findKLargest = [](const std::vector<int>& nums, int k) {
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
    };
    
    std::vector<int> numbers = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5};
    int k = 3;
    
    auto largest = findKLargest(numbers, k);
    std::cout << "Top " << k << " largest elements: ";
    for (int num : largest) std::cout << num << " ";
    std::cout << "\n";
    
    // Example 3: Merge K Sorted Lists
    std::cout << "\n--- Example 3: Merge K Sorted Lists ---\n";
    
    struct ListElement {
        int value;
        int list_index;
        int element_index;
        
        bool operator>(const ListElement& other) const {
            return value > other.value;
        }
    };
    
    auto mergeKSorted = [](const std::vector<std::vector<int>>& lists) {
        std::priority_queue<ListElement, std::vector<ListElement>, 
                           std::greater<ListElement>> min_heap;
        
        // Push first element from each list
        for (size_t i = 0; i < lists.size(); i++) {
            if (!lists[i].empty()) {
                min_heap.push({lists[i][0], static_cast<int>(i), 0});
            }
        }
        
        std::vector<int> result;
        while (!min_heap.empty()) {
            auto elem = min_heap.top();
            min_heap.pop();
            result.push_back(elem.value);
            
            // Push next element from the same list
            if (elem.element_index + 1 < lists[elem.list_index].size()) {
                min_heap.push({lists[elem.list_index][elem.element_index + 1],
                              elem.list_index, elem.element_index + 1});
            }
        }
        
        return result;
    };
    
    std::vector<std::vector<int>> sorted_lists = {
        {1, 4, 7, 10},
        {2, 5, 8, 11},
        {3, 6, 9, 12}
    };
    
    auto merged = mergeKSorted(sorted_lists);
    std::cout << "Merged sorted lists: ";
    for (int num : merged) std::cout << num << " ";
    std::cout << "\n";
    
    // Example 4: Median in a Data Stream
    std::cout << "\n--- Example 4: Median in Data Stream ---\n";
    
    class MedianFinder {
    private:
        std::priority_queue<int> max_heap;  // Stores smaller half
        std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;  // Stores larger half
        
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
        
        double findMedian() {
            if (max_heap.size() > min_heap.size()) {
                return max_heap.top();
            }
            return (max_heap.top() + min_heap.top()) / 2.0;
        }
    };
    
    MedianFinder mf;
    std::vector<int> stream = {5, 15, 1, 3, 2, 8, 7, 9, 4, 6};
    
    std::cout << "Adding numbers to stream:\n";
    for (int num : stream) {
        mf.addNum(num);
        std::cout << "Added: " << num << ", Median: " << mf.findMedian() << "\n";
    }
    
    // Example 5: Dijkstra's Algorithm Simulation
    std::cout << "\n--- Example 5: Dijkstra's Algorithm ---\n";
    
    struct Edge {
        int to;
        int weight;
    };
    
    auto dijkstra = [](const std::vector<std::vector<Edge>>& graph, int start) {
        const int INF = 1e9;
        std::vector<int> dist(graph.size(), INF);
        dist[start] = 0;
        
        // Min-heap: {distance, node}
        std::priority_queue<std::pair<int, int>, 
                           std::vector<std::pair<int, int>>,
                           std::greater<std::pair<int, int>>> pq;
        pq.push({0, start});
        
        while (!pq.empty()) {
            auto [current_dist, node] = pq.top();
            pq.pop();
            
            if (current_dist > dist[node]) continue;
            
            for (const auto& edge : graph[node]) {
                int new_dist = current_dist + edge.weight;
                if (new_dist < dist[edge.to]) {
                    dist[edge.to] = new_dist;
                    pq.push({new_dist, edge.to});
                }
            }
        }
        
        return dist;
    };
    
    // Graph: 0-1 (4), 0-2 (2), 1-2 (1), 1-3 (5), 2-3 (8)
    std::vector<std::vector<Edge>> graph = {
        {{1, 4}, {2, 2}},
        {{0, 4}, {2, 1}, {3, 5}},
        {{0, 2}, {1, 1}, {3, 8}},
        {{1, 5}, {2, 8}}
    };
    
    auto distances = dijkstra(graph, 0);
    std::cout << "Shortest distances from node 0:\n";
    for (size_t i = 0; i < distances.size(); i++) {
        std::cout << "  To node " << i << ": " << distances[i] << "\n";
    }
    
    // Example 6: Custom Comparator for Complex Objects
    std::cout << "\n--- Example 6: Custom Comparator ---\n";
    
    struct Employee {
        std::string name;
        int salary;
        int years_of_experience;
        
        Employee(std::string n, int s, int y) 
            : name(std::move(n)), salary(s), years_of_experience(y) {}
    };
    
    // Custom comparator: higher salary has higher priority
    auto compareBySalary = [](const Employee& a, const Employee& b) {
        return a.salary < b.salary;
    };
    
    std::priority_queue<Employee, std::vector<Employee>, decltype(compareBySalary)> 
        emp_pq(compareBySalary);
    
    emp_pq.emplace("Alice", 75000, 5);
    emp_pq.emplace("Bob", 85000, 7);
    emp_pq.emplace("Charlie", 65000, 3);
    emp_pq.emplace("Diana", 95000, 10);
    
    std::cout << "Employees by salary (highest first):\n";
    while (!emp_pq.empty()) {
        auto emp = emp_pq.top();
        std::cout << "  " << emp.name << " - $" << emp.salary 
                  << " (" << emp.years_of_experience << " years)\n";
        emp_pq.pop();
    }
}
```

---

## Performance Comparison

| Operation | stack | queue | priority_queue |
|-----------|-------|-------|----------------|
| push (insert) | O(1) | O(1) | O(log n) |
| pop (remove) | O(1) | O(1) | O(log n) |
| top/front/back | O(1) | O(1) | O(1) |
| size | O(1) | O(1) | O(1) |
| empty | O(1) | O(1) | O(1) |
| Memory Overhead | Low | Low | Medium |

---

## Best Practices

1. **Choose the right adapter** based on your access pattern (LIFO vs FIFO vs priority)
2. **Use `emplace()` over `push()`** for complex objects to avoid unnecessary copies
3. **Consider underlying container** - `deque` is default for stack/queue, `vector` for priority_queue
4. **Use `std::greater` for min-heap** in priority_queue
5. **Check `empty()` before accessing** `top()`/`front()`/`back()` to avoid undefined behavior
6. **Use `const` references** when passing adapters to functions
7. **Consider `std::priority_queue` for scheduling** problems requiring dynamic priorities

---

## Common Pitfalls

1. **Accessing empty container** - Always check `empty()` before `top()`/`front()`/`back()`
2. **Assuming priority_queue is sorted** - Only the top element is guaranteed to be the largest
3. **Using `priority_queue` for sorting** - Use `std::sort` instead
4. **Not understanding comparator** - Default is `std::less` (max-heap)
5. **Using `priority_queue` with complex objects** - Must define comparison operators
6. **Not reserving capacity** - Underlying container may reallocate (but adapters don't expose reserve)

---
---

## Next Step

- Go to [05_Associative_Container.md](05_Associative_Container.md) to continue with Associative Container.
