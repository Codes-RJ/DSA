# Linked Lists in C++

## 📖 Overview

A **Linked List** is a fundamental linear data structure in which elements (called **nodes**) are not stored in contiguous memory locations. Instead, each node contains a data field and one or more pointers (or references) linking to other nodes in the sequence.

Unlike arrays, linked lists allow for dynamic memory allocation with **$O(1)$ insertions and deletions** at known positions without reallocating or shifting elements.

---

## 🎯 Key Characteristics & Array Comparison

| Feature | Array / `std::vector` | Singly Linked List | Doubly Linked List |
|:---|:---|:---|:---|
| **Memory Allocation** | Contiguous block | Non-contiguous (heap-allocated nodes) | Non-contiguous (heap-allocated nodes) |
| **Random Access ($k$-th element)**| $O(1)$ | $O(N)$ | $O(N)$ |
| **Insertion / Deletion at Head** | $O(N)$ | $O(1)$ | $O(1)$ |
| **Insertion / Deletion at Tail** | $O(1)$ amortized | $O(1)$ with tail pointer | $O(1)$ |
| **Insertion / Deletion in Middle** | $O(N)$ (requires shifting) | $O(1)$ given node pointer ($O(N)$ to find) | $O(1)$ given node pointer |
| **Memory Overhead** | Minimal (capacity buffer) | 1 pointer per element (`next`) | 2 pointers per element (`prev`, `next`) |
| **Cache Locality** | Excellent (spatial locality) | Poor (scattered heap addresses) | Poor |

---

## 1. Singly Linked List Implementation

### Node Structure & Memory Layout
```
[ Data | Next* ] ---> [ Data | Next* ] ---> [ Data | nullptr ]
```

### Complete Implementation (Modern C++ with RAII)
```cpp
#include <iostream>
#include <initializer_list>
#include <utility>
#include <stdexcept>

template<typename T>
class SinglyLinkedList {
private:
    struct Node {
        T data;
        Node* next;
        explicit Node(const T& val) : data(val), next(nullptr) {}
        explicit Node(T&& val) : data(std::move(val)), next(nullptr) {}
    };

    Node* head_ = nullptr;
    Node* tail_ = nullptr;
    size_t size_ = 0;

public:
    SinglyLinkedList() = default;

    // Initializer list constructor
    SinglyLinkedList(std::initializer_list<T> list) {
        for (const auto& item : list) {
            push_back(item);
        }
    }

    // Destructor - RAII memory cleanup
    ~SinglyLinkedList() {
        clear();
    }

    // Copy Constructor - Deep copy
    SinglyLinkedList(const SinglyLinkedList& other) {
        Node* curr = other.head_;
        while (curr != nullptr) {
            push_back(curr->data);
            curr = curr->next;
        }
    }

    // Move Constructor
    SinglyLinkedList(SinglyLinkedList&& other) noexcept
        : head_(other.head_), tail_(other.tail_), size_(other.size_) {
        other.head_ = nullptr;
        other.tail_ = nullptr;
        other.size_ = 0;
    }

    // Copy Assignment Operator
    SinglyLinkedList& operator=(const SinglyLinkedList& other) {
        if (this != &other) {
            clear();
            Node* curr = other.head_;
            while (curr != nullptr) {
                push_back(curr->data);
                curr = curr->next;
            }
        }
        return *this;
    }

    // Move Assignment Operator
    SinglyLinkedList& operator=(SinglyLinkedList&& other) noexcept {
        if (this != &other) {
            clear();
            head_ = other.head_;
            tail_ = other.tail_;
            size_ = other.size_;
            other.head_ = nullptr;
            other.tail_ = nullptr;
            other.size_ = 0;
        }
        return *this;
    }

    // Capacity
    size_t size() const noexcept { return size_; }
    bool empty() const noexcept { return size_ == 0; }

    // Insert at front - O(1)
    void push_front(const T& val) {
        Node* newNode = new Node(val);
        newNode->next = head_;
        head_ = newNode;
        if (tail_ == nullptr) tail_ = head_;
        ++size_;
    }

    // Insert at back - O(1)
    void push_back(const T& val) {
        Node* newNode = new Node(val);
        if (tail_ != nullptr) {
            tail_->next = newNode;
            tail_ = newNode;
        } else {
            head_ = tail_ = newNode;
        }
        ++size_;
    }

    // Remove from front - O(1)
    void pop_front() {
        if (empty()) throw std::underflow_error("List is empty");
        Node* oldHead = head_;
        head_ = head_->next;
        delete oldHead;
        --size_;
        if (head_ == nullptr) tail_ = nullptr;
    }

    // Remove by value - O(N)
    bool remove(const T& val) {
        if (empty()) return false;
        if (head_->data == val) {
            pop_front();
            return true;
        }

        Node* curr = head_;
        while (curr->next != nullptr && curr->next->data != val) {
            curr = curr->next;
        }

        if (curr->next != nullptr) {
            Node* target = curr->next;
            curr->next = target->next;
            if (target == tail_) tail_ = curr;
            delete target;
            --size_;
            return true;
        }
        return false;
    }

    // Clear all elements
    void clear() noexcept {
        Node* curr = head_;
        while (curr != nullptr) {
            Node* nextNode = curr->next;
            delete curr;
            curr = nextNode;
        }
        head_ = tail_ = nullptr;
        size_ = 0;
    }

    // Print list contents
    void print() const {
        Node* curr = head_;
        std::cout << "[ ";
        while (curr != nullptr) {
            std::cout << curr->data << (curr->next ? " -> " : " ");
            curr = curr->next;
        }
        std::cout << "]\n";
    }
};
```

---

## 2. Doubly Linked List Implementation

### Node Structure
```
nullptr <--- [ Prev* | Data | Next* ] <===> [ Prev* | Data | Next* ] ---> nullptr
```

### Complete Implementation
```cpp
template<typename T>
class DoublyLinkedList {
public:
    struct Node {
        T data;
        Node* prev = nullptr;
        Node* next = nullptr;
        explicit Node(const T& val) : data(val) {}
    };

private:
    Node* head_ = nullptr;
    Node* tail_ = nullptr;
    size_t size_ = 0;

public:
    DoublyLinkedList() = default;

    ~DoublyLinkedList() {
        clear();
    }

    void push_back(const T& val) {
        Node* newNode = new Node(val);
        if (!tail_) {
            head_ = tail_ = newNode;
        } else {
            tail_->next = newNode;
            newNode->prev = tail_;
            tail_ = newNode;
        }
        ++size_;
    }

    void push_front(const T& val) {
        Node* newNode = new Node(val);
        if (!head_) {
            head_ = tail_ = newNode;
        } else {
            newNode->next = head_;
            head_->prev = newNode;
            head_ = newNode;
        }
        ++size_;
    }

    // Delete node directly in O(1) given its pointer
    void eraseNode(Node* node) {
        if (!node) return;
        if (node->prev) node->prev->next = node->next;
        else head_ = node->next;

        if (node->next) node->next->prev = node->prev;
        else tail_ = node->prev;

        delete node;
        --size_;
    }

    void clear() {
        Node* curr = head_;
        while (curr) {
            Node* nextNode = curr->next;
            delete curr;
            curr = nextNode;
        }
        head_ = tail_ = nullptr;
        size_ = 0;
    }

    Node* head() const { return head_; }
    Node* tail() const { return tail_; }
    size_t size() const { return size_; }
};
```

---

## 3. Essential Interview Algorithms & Patterns

### 1. In-Place Reversal of a Linked List
```cpp
struct ListNode {
    int val;
    ListNode* next;
    explicit ListNode(int x) : val(x), next(nullptr) {}
};

// Iterative 3-Pointer Reversal: O(N) time, O(1) space
ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;

    while (curr != nullptr) {
        ListNode* nextTemp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextTemp;
    }
    return prev;
}

// Recursive Reversal: O(N) time, O(N) call stack
ListNode* reverseListRecursive(ListNode* head) {
    if (head == nullptr || head->next == nullptr) {
        return head;
    }
    ListNode* newHead = reverseListRecursive(head->next);
    head->next->next = head;
    head->next = nullptr;
    return newHead;
}
```

### 2. Fast & Slow Pointer (Floyd's Cycle Detection)
```cpp
// 1. Detect if cycle exists
bool hasCycle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}

// 2. Find the starting node of the cycle
ListNode* detectCycleStart(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            // Cycle detected: reset one pointer to head
            ListNode* ptr1 = head;
            ListNode* ptr2 = slow;
            while (ptr1 != ptr2) {
                ptr1 = ptr1->next;
                ptr2 = ptr2->next;
            }
            return ptr1; // Intersection is the cycle entrance
        }
    }
    return nullptr;
}
```

### 3. Find Middle Node (Tortoise and Hare)
```cpp
ListNode* findMiddle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}
```

### 4. Merge Two Sorted Linked Lists in O(1) Extra Space
```cpp
ListNode* mergeTwoSortedLists(ListNode* l1, ListNode* l2) {
    ListNode dummy(0);
    ListNode* tail = &dummy;

    while (l1 != nullptr && l2 != nullptr) {
        if (l1->val <= l2->val) {
            tail->next = l1;
            l1 = l1->next;
        } else {
            tail->next = l2;
            l2 = l2->next;
        }
        tail = tail->next;
    }

    tail->next = (l1 != nullptr) ? l1 : l2;
    return dummy.next;
}
```

---

## 4. Real-World Application: LRU Cache

The **Least Recently Used (LRU) Cache** combines a **Doubly Linked List** (for $O(1)$ removal and insertion at head) with a **Hash Map** (`std::unordered_map`) for $O(1)$ key lookup.

```cpp
#include <unordered_map>
#include <iostream>

class LRUCache {
private:
    struct Node {
        int key;
        int value;
        Node* prev;
        Node* next;
        Node(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr) {}
    };

    int capacity_;
    std::unordered_map<int, Node*> cache_;
    Node* head_; // Dummy head
    Node* tail_; // Dummy tail

    void addNode(Node* node) {
        node->next = head_->next;
        node->prev = head_;
        head_->next->prev = node;
        head_->next = node;
    }

    void removeNode(Node* node) {
        Node* prev = node->prev;
        Node* next = node->next;
        prev->next = next;
        next->prev = prev;
    }

    void moveToHead(Node* node) {
        removeNode(node);
        addNode(node);
    }

    Node* popTail() {
        Node* res = tail_->prev;
        removeNode(res);
        return res;
    }

public:
    explicit LRUCache(int capacity) : capacity_(capacity) {
        head_ = new Node(0, 0);
        tail_ = new Node(0, 0);
        head_->next = tail_;
        tail_->prev = head_;
    }

    ~LRUCache() {
        Node* curr = head_;
        while (curr != nullptr) {
            Node* nextNode = curr->next;
            delete curr;
            curr = nextNode;
        }
    }

    int get(int key) {
        auto it = cache_.find(key);
        if (it == cache_.end()) return -1;
        Node* node = it->second;
        moveToHead(node);
        return node->value;
    }

    void put(int key, int value) {
        auto it = cache_.find(key);
        if (it != cache_.end()) {
            Node* node = it->second;
            node->value = value;
            moveToHead(node);
        } else {
            Node* newNode = new Node(key, value);
            cache_[key] = newNode;
            addNode(newNode);

            if (static_cast<int>(cache_.size()) > capacity_) {
                Node* tailNode = popTail();
                cache_.erase(tailNode->key);
                delete tailNode;
            }
        }
    }
};
```

---

## 💻 Driver & Comprehensive Verification

```cpp
#include <iostream>
#include <cassert>

int main() {
    std::cout << "========== 1. SINGLY LINKED LIST ==========\n";
    SinglyLinkedList<int> list = {10, 20, 30, 40};
    list.push_front(5);
    list.push_back(50);
    list.print();
    assert(list.size() == 6);
    list.remove(30);
    assert(list.size() == 5);

    std::cout << "\n========== 2. REVERSAL & ALGORITHMS ==========\n";
    ListNode* n1 = new ListNode(1);
    ListNode* n2 = new ListNode(2);
    ListNode* n3 = new ListNode(3);
    n1->next = n2;
    n2->next = n3;

    ListNode* reversed = reverseList(n1);
    assert(reversed->val == 3);
    assert(reversed->next->val == 2);
    assert(reversed->next->next->val == 1);
    std::cout << "Reversal verified: 3 -> 2 -> 1\n";

    std::cout << "\n========== 3. LRU CACHE ==========\n";
    LRUCache lru(2);
    lru.put(1, 100);
    lru.put(2, 200);
    assert(lru.get(1) == 100); // 1 becomes most recently used
    lru.put(3, 300);           // Evicts key 2
    assert(lru.get(2) == -1);  // Key 2 evicted
    assert(lru.get(3) == 300);
    std::cout << "LRU Cache operations successfully verified!\n";

    // Clean up temporary nodes
    delete reversed->next->next;
    delete reversed->next;
    delete reversed;

    std::cout << "\n✅ All Linked List implementations verified successfully!\n";
    return 0;
}
```

---

## Next Step

- Go to [10_Custom_Stack_and_Queue.md](10_Custom_Stack_and_Queue.md) to understand Custom Stacks and Queues.
