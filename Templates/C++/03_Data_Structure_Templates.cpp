#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <bitset>
#include <numeric>
#include <iomanip>
#include <climits>
#include <unordered_map>
#include <unordered_set>
#include <memory>

using namespace std;

// Fast I/O
void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}

// Common type definitions
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;

// Constants
const int MOD = 1e9 + 7;
const int INF = INT_MAX;
const ll LINF = LLONG_MAX;

// =============================================
// LINKED LIST IMPLEMENTATIONS
// =============================================

// Singly Linked List Node
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Singly Linked List Class
class LinkedList {
private:
    ListNode* head;
    int size;

public:
    LinkedList() : head(nullptr), size(0) {}
    
    ~LinkedList() {
        ListNode* current = head;
        while (current) {
            ListNode* next = current->next;
            delete current;
            current = next;
        }
    }
    
    void insertAtHead(int val) {
        ListNode* newNode = new ListNode(val);
        newNode->next = head;
        head = newNode;
        size++;
    }
    
    void insertAtTail(int val) {
        ListNode* newNode = new ListNode(val);
        if (!head) {
            head = newNode;
        } else {
            ListNode* current = head;
            while (current->next) {
                current = current->next;
            }
            current->next = newNode;
        }
        size++;
    }
    
    void deleteAtHead() {
        if (!head) return;
        ListNode* temp = head;
        head = head->next;
        delete temp;
        size--;
    }
    
    void deleteAtTail() {
        if (!head) return;
        if (!head->next) {
            delete head;
            head = nullptr;
        } else {
            ListNode* current = head;
            while (current->next->next) {
                current = current->next;
            }
            delete current->next;
            current->next = nullptr;
        }
        size--;
    }
    
    bool search(int val) {
        ListNode* current = head;
        while (current) {
            if (current->val == val) return true;
            current = current->next;
        }
        return false;
    }
    
    void printList() {
        ListNode* current = head;
        while (current) {
            cout << current->val << " -> ";
            current = current->next;
        }
        cout << "NULL\n";
    }
    
    vector<int> toVector() {
        vector<int> result;
        ListNode* current = head;
        while (current) {
            result.push_back(current->val);
            current = current->next;
        }
        return result;
    }
    
    int getSize() { return size; }
    bool isEmpty() { return size == 0; }
};

// Doubly Linked List Node
struct DoublyListNode {
    int val;
    DoublyListNode* prev;
    DoublyListNode* next;
    DoublyListNode(int x) : val(x), prev(nullptr), next(nullptr) {}
};

// Doubly Linked List Class
class DoublyLinkedList {
private:
    DoublyListNode* head;
    DoublyListNode* tail;
    int size;

public:
    DoublyLinkedList() : head(nullptr), tail(nullptr), size(0) {}
    
    ~DoublyLinkedList() {
        DoublyListNode* current = head;
        while (current) {
            DoublyListNode* next = current->next;
            delete current;
            current = next;
        }
    }
    
    void insertAtHead(int val) {
        DoublyListNode* newNode = new DoublyListNode(val);
        if (!head) {
            head = tail = newNode;
        } else {
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
        }
        size++;
    }
    
    void insertAtTail(int val) {
        DoublyListNode* newNode = new DoublyListNode(val);
        if (!tail) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
        size++;
    }
    
    void deleteAtHead() {
        if (!head) return;
        DoublyListNode* temp = head;
        head = head->next;
        if (head) head->prev = nullptr;
        else tail = nullptr;
        delete temp;
        size--;
    }
    
    void deleteAtTail() {
        if (!tail) return;
        DoublyListNode* temp = tail;
        tail = tail->prev;
        if (tail) tail->next = nullptr;
        else head = nullptr;
        delete temp;
        size--;
    }
    
    void printList() {
        DoublyListNode* current = head;
        while (current) {
            cout << current->val << " <-> ";
            current = current->next;
        }
        cout << "NULL\n";
    }
    
    vector<int> toVector() {
        vector<int> result;
        DoublyListNode* current = head;
        while (current) {
            result.push_back(current->val);
            current = current->next;
        }
        return result;
    }
    
    int getSize() { return size; }
    bool isEmpty() { return size == 0; }
};

// =============================================
// STACK IMPLEMENTATIONS
// =============================================

// Array-based Stack
template<typename T>
class ArrayStack {
private:
    vector<T> elements;
    int capacity;

public:
    ArrayStack(int cap = 1000) : capacity(cap) {
        elements.reserve(capacity);
    }
    
    void push(T element) {
        if (elements.size() < capacity) {
            elements.push_back(element);
        } else {
            throw runtime_error("Stack is full");
        }
    }
    
    T pop() {
        if (empty()) {
            throw runtime_error("Stack is empty");
        }
        T element = elements.back();
        elements.pop_back();
        return element;
    }
    
    T top() {
        if (empty()) {
            throw runtime_error("Stack is empty");
        }
        return elements.back();
    }
    
    bool empty() {
        return elements.empty();
    }
    
    int size() {
        return elements.size();
    }
    
    void clear() {
        elements.clear();
    }
};

// Linked List-based Stack
template<typename T>
class LinkedListStack {
private:
    struct Node {
        T data;
        Node* next;
        Node(T val) : data(val), next(nullptr) {}
    };
    
    Node* topNode;
    int stackSize;

public:
    LinkedListStack() : topNode(nullptr), stackSize(0) {}
    
    ~LinkedListStack() {
        while (topNode) {
            Node* temp = topNode;
            topNode = topNode->next;
            delete temp;
        }
    }
    
    void push(T element) {
        Node* newNode = new Node(element);
        newNode->next = topNode;
        topNode = newNode;
        stackSize++;
    }
    
    T pop() {
        if (empty()) {
            throw runtime_error("Stack is empty");
        }
        Node* temp = topNode;
        T element = temp->data;
        topNode = topNode->next;
        delete temp;
        stackSize--;
        return element;
    }
    
    T top() {
        if (empty()) {
            throw runtime_error("Stack is empty");
        }
        return topNode->data;
    }
    
    bool empty() {
        return topNode == nullptr;
    }
    
    int size() {
        return stackSize;
    }
};

// =============================================
// QUEUE IMPLEMENTATIONS
// =============================================

// Array-based Queue (Circular Queue)
template<typename T>
class ArrayQueue {
private:
    vector<T> elements;
    int front;
    int rear;
    int capacity;
    int queueSize;

public:
    ArrayQueue(int cap = 1000) : capacity(cap), front(0), rear(-1), queueSize(0) {
        elements.resize(capacity);
    }
    
    void enqueue(T element) {
        if (queueSize == capacity) {
            throw runtime_error("Queue is full");
        }
        rear = (rear + 1) % capacity;
        elements[rear] = element;
        queueSize++;
    }
    
    T dequeue() {
        if (empty()) {
            throw runtime_error("Queue is empty");
        }
        T element = elements[front];
        front = (front + 1) % capacity;
        queueSize--;
        return element;
    }
    
    T frontElement() {
        if (empty()) {
            throw runtime_error("Queue is empty");
        }
        return elements[front];
    }
    
    bool empty() {
        return queueSize == 0;
    }
    
    int size() {
        return queueSize;
    }
    
    bool isFull() {
        return queueSize == capacity;
    }
};

// Linked List-based Queue
template<typename T>
class LinkedListQueue {
private:
    struct Node {
        T data;
        Node* next;
        Node(T val) : data(val), next(nullptr) {}
    };
    
    Node* frontNode;
    Node* rearNode;
    int queueSize;

public:
    LinkedListQueue() : frontNode(nullptr), rearNode(nullptr), queueSize(0) {}
    
    ~LinkedListQueue() {
        while (frontNode) {
            Node* temp = frontNode;
            frontNode = frontNode->next;
            delete temp;
        }
    }
    
    void enqueue(T element) {
        Node* newNode = new Node(element);
        if (empty()) {
            frontNode = rearNode = newNode;
        } else {
            rearNode->next = newNode;
            rearNode = newNode;
        }
        queueSize++;
    }
    
    T dequeue() {
        if (empty()) {
            throw runtime_error("Queue is empty");
        }
        Node* temp = frontNode;
        T element = temp->data;
        frontNode = frontNode->next;
        if (!frontNode) rearNode = nullptr;
        delete temp;
        queueSize--;
        return element;
    }
    
    T frontElement() {
        if (empty()) {
            throw runtime_error("Queue is empty");
        }
        return frontNode->data;
    }
    
    bool empty() {
        return frontNode == nullptr;
    }
    
    int size() {
        return queueSize;
    }
};

// =============================================
// BINARY TREE IMPLEMENTATIONS
// =============================================

// Binary Tree Node
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// Binary Tree Class
class BinaryTree {
private:
    TreeNode* root;

public:
    BinaryTree() : root(nullptr) {}
    
    ~BinaryTree() {
        destroyTree(root);
    }
    
    void destroyTree(TreeNode* node) {
        if (node) {
            destroyTree(node->left);
            destroyTree(node->right);
            delete node;
        }
    }
    
    void insert(int val) {
        root = insertRecursive(root, val);
    }
    
    TreeNode* insertRecursive(TreeNode* node, int val) {
        if (!node) {
            return new TreeNode(val);
        }
        
        if (val < node->val) {
            node->left = insertRecursive(node->left, val);
        } else {
            node->right = insertRecursive(node->right, val);
        }
        
        return node;
    }
    
    bool search(int val) {
        return searchRecursive(root, val);
    }
    
    bool searchRecursive(TreeNode* node, int val) {
        if (!node) return false;
        if (node->val == val) return true;
        if (val < node->val) return searchRecursive(node->left, val);
        return searchRecursive(node->right, val);
    }
    
    void inorderTraversal() {
        inorderRecursive(root);
        cout << "\n";
    }
    
    void inorderRecursive(TreeNode* node) {
        if (node) {
            inorderRecursive(node->left);
            cout << node->val << " ";
            inorderRecursive(node->right);
        }
    }
    
    void preorderTraversal() {
        preorderRecursive(root);
        cout << "\n";
    }
    
    void preorderRecursive(TreeNode* node) {
        if (node) {
            cout << node->val << " ";
            preorderRecursive(node->left);
            preorderRecursive(node->right);
        }
    }
    
    void postorderTraversal() {
        postorderRecursive(root);
        cout << "\n";
    }
    
    void postorderRecursive(TreeNode* node) {
        if (node) {
            postorderRecursive(node->left);
            postorderRecursive(node->right);
            cout << node->val << " ";
        }
    }
    
    int getHeight() {
        return getHeightRecursive(root);
    }
    
    int getHeightRecursive(TreeNode* node) {
        if (!node) return 0;
        return 1 + max(getHeightRecursive(node->left), getHeightRecursive(node->right));
    }
    
    int getSize() {
        return getSizeRecursive(root);
    }
    
    int getSizeRecursive(TreeNode* node) {
        if (!node) return 0;
        return 1 + getSizeRecursive(node->left) + getSizeRecursive(node->right);
    }
    
    bool isBST() {
        return isBSTRecursive(root, INT_MIN, INT_MAX);
    }
    
    bool isBSTRecursive(TreeNode* node, int min, int max) {
        if (!node) return true;
        if (node->val < min || node->val > max) return false;
        return isBSTRecursive(node->left, min, node->val - 1) &&
               isBSTRecursive(node->right, node->val + 1, max);
    }
};

// Binary Search Tree Class
class BST {
private:
    TreeNode* root;

public:
    BST() : root(nullptr) {}
    
    ~BST() {
        destroyTree(root);
    }
    
    void destroyTree(TreeNode* node) {
        if (node) {
            destroyTree(node->left);
            destroyTree(node->right);
            delete node;
        }
    }
    
    void insert(int val) {
        root = insertRecursive(root, val);
    }
    
    TreeNode* insertRecursive(TreeNode* node, int val) {
        if (!node) {
            return new TreeNode(val);
        }
        
        if (val < node->val) {
            node->left = insertRecursive(node->left, val);
        } else if (val > node->val) {
            node->right = insertRecursive(node->right, val);
        }
        
        return node;
    }
    
    bool search(int val) {
        return searchRecursive(root, val);
    }
    
    bool searchRecursive(TreeNode* node, int val) {
        if (!node) return false;
        if (node->val == val) return true;
        if (val < node->val) return searchRecursive(node->left, val);
        return searchRecursive(node->right, val);
    }
    
    void remove(int val) {
        root = removeRecursive(root, val);
    }
    
    TreeNode* removeRecursive(TreeNode* node, int val) {
        if (!node) return node;
        
        if (val < node->val) {
            node->left = removeRecursive(node->left, val);
        } else if (val > node->val) {
            node->right = removeRecursive(node->right, val);
        } else {
            // Node with one child or no child
            if (!node->left) {
                TreeNode* temp = node->right;
                delete node;
                return temp;
            } else if (!node->right) {
                TreeNode* temp = node->left;
                delete node;
                return temp;
            }
            
            // Node with two children
            TreeNode* temp = findMin(node->right);
            node->val = temp->val;
            node->right = removeRecursive(node->right, temp->val);
        }
        
        return node;
    }
    
    TreeNode* findMin(TreeNode* node) {
        TreeNode* current = node;
        while (current && current->left) {
            current = current->left;
        }
        return current;
    }
    
    void inorderTraversal() {
        inorderRecursive(root);
        cout << "\n";
    }
    
    void inorderRecursive(TreeNode* node) {
        if (node) {
            inorderRecursive(node->left);
            cout << node->val << " ";
            inorderRecursive(node->right);
        }
    }
};

// =============================================
// HASH TABLE IMPLEMENTATIONS
// =============================================

// Hash Node for Separate Chaining
template<typename K, typename V>
class HashNode {
public:
    K key;
    V value;
    HashNode* next;
    
    HashNode(K k, V v) : key(k), value(v), next(nullptr) {}
};

// Hash Table with Separate Chaining
template<typename K, typename V>
class HashTable {
private:
    static const int TABLE_SIZE = 10007;
    HashNode<K, V>** table;
    
    int hashFunction(K key) {
        return hash<K>{}(key) % TABLE_SIZE;
    }

public:
    HashTable() {
        table = new HashNode<K, V>*[TABLE_SIZE]();
        for (int i = 0; i < TABLE_SIZE; i++) {
            table[i] = nullptr;
        }
    }
    
    ~HashTable() {
        for (int i = 0; i < TABLE_SIZE; i++) {
            HashNode<K, V>* current = table[i];
            while (current) {
                HashNode<K, V>* temp = current;
                current = current->next;
                delete temp;
            }
        }
        delete[] table;
    }
    
    void put(K key, V value) {
        int hashIndex = hashFunction(key);
        HashNode<K, V>* newNode = new HashNode<K, V>(key, value);
        
        if (!table[hashIndex]) {
            table[hashIndex] = newNode;
        } else {
            HashNode<K, V>* current = table[hashIndex];
            while (current->next) {
                if (current->key == key) {
                    current->value = value;
                    delete newNode;
                    return;
                }
                current = current->next;
            }
            current->next = newNode;
        }
    }
    
    V get(K key) {
        int hashIndex = hashFunction(key);
        HashNode<K, V>* current = table[hashIndex];
        
        while (current) {
            if (current->key == key) {
                return current->value;
            }
            current = current->next;
        }
        
        throw runtime_error("Key not found");
    }
    
    void remove(K key) {
        int hashIndex = hashFunction(key);
        HashNode<K, V>* current = table[hashIndex];
        HashNode<K, V>* prev = nullptr;
        
        while (current) {
            if (current->key == key) {
                if (prev) {
                    prev->next = current->next;
                } else {
                    table[hashIndex] = current->next;
                }
                delete current;
                return;
            }
            prev = current;
            current = current->next;
        }
    }
    
    bool contains(K key) {
        int hashIndex = hashFunction(key);
        HashNode<K, V>* current = table[hashIndex];
        
        while (current) {
            if (current->key == key) {
                return true;
            }
            current = current->next;
        }
        return false;
    }
};

// =============================================
// GRAPH IMPLEMENTATIONS
// =============================================

// Graph Node for Adjacency List
struct GraphNode {
    int val;
    vector<GraphNode*> neighbors;
    GraphNode(int x) : val(x) {}
};

// Graph Class (Adjacency List)
class Graph {
private:
    unordered_map<int, GraphNode*> nodes;
    bool directed;

public:
    Graph(bool isDirected = false) : directed(isDirected) {}
    
    ~Graph() {
        for (auto& pair : nodes) {
            delete pair.second;
        }
    }
    
    void addNode(int val) {
        if (nodes.find(val) == nodes.end()) {
            nodes[val] = new GraphNode(val);
        }
    }
    
    void addEdge(int from, int to) {
        if (nodes.find(from) == nodes.end()) addNode(from);
        if (nodes.find(to) == nodes.end()) addNode(to);
        
        nodes[from]->neighbors.push_back(nodes[to]);
        if (!directed) {
            nodes[to]->neighbors.push_back(nodes[from]);
        }
    }
    
    void removeEdge(int from, int to) {
        if (nodes.find(from) != nodes.end() && nodes.find(to) != nodes.end()) {
            auto& neighbors = nodes[from]->neighbors;
            neighbors.erase(remove(neighbors.begin(), neighbors.end(), nodes[to]), neighbors.end());
            
            if (!directed) {
                auto& neighborsRev = nodes[to]->neighbors;
                neighborsRev.erase(remove(neighborsRev.begin(), neighborsRev.end(), nodes[from]), neighborsRev.end());
            }
        }
    }
    
    bool hasNode(int val) {
        return nodes.find(val) != nodes.end();
    }
    
    bool hasEdge(int from, int to) {
        if (nodes.find(from) != nodes.end()) {
            for (GraphNode* neighbor : nodes[from]->neighbors) {
                if (neighbor->val == to) return true;
            }
        }
        return false;
    }
    
    vector<int> getNeighbors(int val) {
        vector<int> result;
        if (nodes.find(val) != nodes.end()) {
            for (GraphNode* neighbor : nodes[val]->neighbors) {
                result.push_back(neighbor->val);
            }
        }
        return result;
    }
    
    void printGraph() {
        for (auto& pair : nodes) {
            cout << "Node " << pair.first << ": ";
            for (GraphNode* neighbor : pair.second->neighbors) {
                cout << neighbor->val << " ";
            }
            cout << "\n";
        }
    }
    
    // BFS Traversal
    vector<int> bfs(int start) {
        vector<int> result;
        if (nodes.find(start) == nodes.end()) return result;
        
        unordered_set<int> visited;
        queue<GraphNode*> q;
        
        visited.insert(start);
        q.push(nodes[start]);
        
        while (!q.empty()) {
            GraphNode* current = q.front();
            q.pop();
            result.push_back(current->val);
            
            for (GraphNode* neighbor : current->neighbors) {
                if (visited.find(neighbor->val) == visited.end()) {
                    visited.insert(neighbor->val);
                    q.push(neighbor);
                }
            }
        }
        return result;
    }
    
    // DFS Traversal
    vector<int> dfs(int start) {
        vector<int> result;
        if (nodes.find(start) == nodes.end()) return result;
        
        unordered_set<int> visited;
        stack<GraphNode*> st;
        
        st.push(nodes[start]);
        visited.insert(start);
        
        while (!st.empty()) {
            GraphNode* current = st.top();
            st.pop();
            result.push_back(current->val);
            
            for (GraphNode* neighbor : current->neighbors) {
                if (visited.find(neighbor->val) == visited.end()) {
                    visited.insert(neighbor->val);
                    st.push(neighbor);
                }
            }
        }
        return result;
    }
};

// =============================================
// PRIORITY QUEUE (HEAP) IMPLEMENTATIONS
// =============================================

// Min-Heap
template<typename T>
class MinHeap {
private:
    vector<T> heap;
    
    void heapifyUp(int index) {
        while (index > 0) {
            int parent = (index - 1) / 2;
            if (heap[parent] <= heap[index]) break;
            swap(heap[parent], heap[index]);
            index = parent;
        }
    }
    
    void heapifyDown(int index) {
        int n = heap.size();
        while (true) {
            int left = 2 * index + 1;
            int right = 2 * index + 2;
            int smallest = index;
            
            if (left < n && heap[left] < heap[smallest]) smallest = left;
            if (right < n && heap[right] < heap[smallest]) smallest = right;
            
            if (smallest == index) break;
            swap(heap[index], heap[smallest]);
            index = smallest;
        }
    }

public:
    void push(T element) {
        heap.push_back(element);
        heapifyUp(heap.size() - 1);
    }
    
    T pop() {
        if (empty()) {
            throw runtime_error("Heap is empty");
        }
        T minElement = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        if (!empty()) {
            heapifyDown(0);
        }
        return minElement;
    }
    
    T top() {
        if (empty()) {
            throw runtime_error("Heap is empty");
        }
        return heap[0];
    }
    
    bool empty() {
        return heap.empty();
    }
    
    int size() {
        return heap.size();
    }
};

// Max-Heap
template<typename T>
class MaxHeap {
private:
    vector<T> heap;
    
    void heapifyUp(int index) {
        while (index > 0) {
            int parent = (index - 1) / 2;
            if (heap[parent] >= heap[index]) break;
            swap(heap[parent], heap[index]);
            index = parent;
        }
    }
    
    void heapifyDown(int index) {
        int n = heap.size();
        while (true) {
            int left = 2 * index + 1;
            int right = 2 * index + 2;
            int largest = index;
            
            if (left < n && heap[left] > heap[largest]) largest = left;
            if (right < n && heap[right] > heap[largest]) largest = right;
            
            if (largest == index) break;
            swap(heap[index], heap[largest]);
            index = largest;
        }
    }

public:
    void push(T element) {
        heap.push_back(element);
        heapifyUp(heap.size() - 1);
    }
    
    T pop() {
        if (empty()) {
            throw runtime_error("Heap is empty");
        }
        T maxElement = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        if (!empty()) {
            heapifyDown(0);
        }
        return maxElement;
    }
    
    T top() {
        if (empty()) {
            throw runtime_error("Heap is empty");
        }
        return heap[0];
    }
    
    bool empty() {
        return heap.empty();
    }
    
    int size() {
        return heap.size();
    }
};

// =============================================
// DISJOINT SET UNION (UNION-FIND)
// =============================================

class DSU {
private:
    vector<int> parent;
    vector<int> rank;

public:
    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    void unionSets(int x, int y) {
        int xRoot = find(x);
        int yRoot = find(y);
        
        if (xRoot == yRoot) return;
        
        if (rank[xRoot] < rank[yRoot]) {
            parent[xRoot] = yRoot;
        } else if (rank[xRoot] > rank[yRoot]) {
            parent[yRoot] = xRoot;
        } else {
            parent[yRoot] = xRoot;
            rank[xRoot]++;
        }
    }
    
    bool isConnected(int x, int y) {
        return find(x) == find(y);
    }
};

// =============================================
// TRIE IMPLEMENTATION
// =============================================

class TrieNode {
public:
    map<char, TrieNode*> children;
    bool isEndOfWord;
    
    TrieNode() : isEndOfWord(false) {}
};

class Trie {
private:
    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* current = root;
        for (char c : word) {
            if (current->children.find(c) == current->children.end()) {
                current->children[c] = new TrieNode();
            }
            current = current->children[c];
        }
        current->isEndOfWord = true;
    }
    
    bool search(string word) {
        TrieNode* current = root;
        for (char c : word) {
            if (current->children.find(c) == current->children.end()) {
                return false;
            }
            current = current->children[c];
        }
        return current->isEndOfWord;
    }
    
    bool startsWith(string prefix) {
        TrieNode* current = root;
        for (char c : prefix) {
            if (current->children.find(c) == current->children.end()) {
                return false;
            }
            current = current->children[c];
        }
        return true;
    }
    
    void remove(string word) {
        remove(root, word, 0);
    }
    
    bool remove(TrieNode* node, string word, int depth) {
        if (depth == word.length()) {
            if (!node->isEndOfWord) return false;
            node->isEndOfWord = false;
            return node->children.empty();
        }
        
        char c = word[depth];
        if (node->children.find(c) == node->children.end()) {
            return false;
        }
        
        TrieNode* childNode = node->children[c];
        bool shouldDeleteChild = remove(childNode, word, depth + 1);
        
        if (shouldDeleteChild) {
            delete childNode;
            node->children.erase(c);
            return node->children.empty() && !node->isEndOfWord;
        }
        
        return false;
    }
};

// =============================================
// UTILITY FUNCTIONS
// =============================================

template<typename T>
void printVector(const vector<T>& vec) {
    for (const auto& elem : vec) {
        cout << elem << " ";
    }
    cout << "\n";
}

template<typename T>
void print2DVector(const vector<vector<T>>& mat) {
    for (const auto& row : mat) {
        for (const auto& elem : row) {
            cout << elem << " ";
        }
        cout << "\n";
    }
}

// =============================================
// MAIN SOLVE FUNCTION
// =============================================

void solve() {
    fastIO();
    
    cout << "=== DATA STRUCTURE DEMONSTRATIONS ===\n\n";
    
    // Linked List Demo
    cout << "1. Linked List Demo:\n";
    LinkedList list;
    list.insertAtHead(10);
    list.insertAtTail(20);
    list.insertAtHead(5);
    list.insertAtTail(25);
    cout << "Linked List: ";
    list.printList();
    cout << "Search 20: " << (list.search(20) ? "Found" : "Not Found") << "\n";
    list.deleteAtHead();
    list.deleteAtTail();
    cout << "After deletions: ";
    list.printList();
    cout << "Size: " << list.getSize() << "\n\n";
    
    // Stack Demo
    cout << "2. Stack Demo:\n";
    ArrayStack<int> stack;
    stack.push(10);
    stack.push(20);
    stack.push(30);
    cout << "Stack elements: ";
    while (!stack.empty()) {
        cout << stack.top() << " ";
        stack.pop();
    }
    cout << "\n\n";
    
    // Queue Demo
    cout << "3. Queue Demo:\n";
    ArrayQueue<int> queue;
    queue.enqueue(10);
    queue.enqueue(20);
    queue.enqueue(30);
    cout << "Queue elements: ";
    while (!queue.empty()) {
        cout << queue.frontElement() << " ";
        queue.dequeue();
    }
    cout << "\n\n";
    
    // Binary Tree Demo
    cout << "4. Binary Tree Demo:\n";
    BinaryTree tree;
    tree.insert(50);
    tree.insert(30);
    tree.insert(70);
    tree.insert(20);
    tree.insert(40);
    tree.insert(60);
    tree.insert(80);
    cout << "Inorder traversal: ";
    tree.inorderTraversal();
    cout << "Preorder traversal: ";
    tree.preorderTraversal();
    cout << "Postorder traversal: ";
    tree.postorderTraversal();
    cout << "Tree height: " << tree.getHeight() << "\n";
    cout << "Tree size: " << tree.getSize() << "\n";
    cout << "Is BST: " << (tree.isBST() ? "Yes" : "No") << "\n\n";
    
    // BST Demo
    cout << "5. Binary Search Tree Demo:\n";
    BST bst;
    bst.insert(50);
    bst.insert(30);
    bst.insert(70);
    bst.insert(20);
    bst.insert(40);
    bst.insert(60);
    bst.insert(80);
    cout << "BST inorder: ";
    bst.inorderTraversal();
    cout << "Search 40: " << (bst.search(40) ? "Found" : "Not Found") << "\n";
    bst.remove(20);
    bst.remove(70);
    cout << "After removing 20 and 70: ";
    bst.inorderTraversal();
    cout << "\n";
    
    // Hash Table Demo
    cout << "6. Hash Table Demo:\n";
    HashTable<string, int> hashTable;
    hashTable.put("apple", 5);
    hashTable.put("banana", 3);
    hashTable.put("orange", 8);
    cout << "Get apple: " << hashTable.get("apple") << "\n";
    cout << "Contains banana: " << (hashTable.contains("banana") ? "Yes" : "No") << "\n";
    hashTable.remove("apple");
    cout << "Contains apple after removal: " << (hashTable.contains("apple") ? "Yes" : "No") << "\n\n";
    
    // Graph Demo
    cout << "7. Graph Demo:\n";
    Graph graph(true); // Directed graph
    graph.addNode(1);
    graph.addNode(2);
    graph.addNode(3);
    graph.addNode(4);
    graph.addEdge(1, 2);
    graph.addEdge(2, 3);
    graph.addEdge(3, 4);
    graph.addEdge(4, 1);
    cout << "Graph adjacency list:\n";
    graph.printGraph();
    cout << "BFS from 1: ";
    vector<int> bfsResult = graph.bfs(1);
    printVector(bfsResult);
    cout << "DFS from 1: ";
    vector<int> dfsResult = graph.dfs(1);
    printVector(dfsResult);
    cout << "Has edge 1->2: " << (graph.hasEdge(1, 2) ? "Yes" : "No") << "\n\n";
    
    // Heap Demo
    cout << "8. Heap Demo:\n";
    MinHeap<int> minHeap;
    minHeap.push(30);
    minHeap.push(10);
    minHeap.push(20);
    minHeap.push(40);
    cout << "Min-heap elements: ";
    while (!minHeap.empty()) {
        cout << minHeap.top() << " ";
        minHeap.pop();
    }
    cout << "\n";
    
    MaxHeap<int> maxHeap;
    maxHeap.push(30);
    maxHeap.push(10);
    maxHeap.push(20);
    maxHeap.push(40);
    cout << "Max-heap elements: ";
    while (!maxHeap.empty()) {
        cout << maxHeap.top() << " ";
        maxHeap.pop();
    }
    cout << "\n\n";
    
    // DSU Demo
    cout << "9. Disjoint Set Union Demo:\n";
    DSU dsu(5);
    dsu.unionSets(0, 1);
    dsu.unionSets(1, 2);
    dsu.unionSets(3, 4);
    cout << "Is 0 connected to 2: " << (dsu.isConnected(0, 2) ? "Yes" : "No") << "\n";
    cout << "Is 0 connected to 3: " << (dsu.isConnected(0, 3) ? "Yes" : "No") << "\n\n";
    
    // Trie Demo
    cout << "10. Trie Demo:\n";
    Trie trie;
    trie.insert("hello");
    trie.insert("world");
    trie.insert("help");
    cout << "Search 'hello': " << (trie.search("hello") ? "Found" : "Not Found") << "\n";
    cout << "Search 'hell': " << (trie.search("hell") ? "Found" : "Not Found") << "\n";
    cout << "Starts with 'hel': " << (trie.startsWith("hel") ? "Yes" : "No") << "\n";
    trie.remove("hello");
    cout << "Search 'hello' after removal: " << (trie.search("hello") ? "Found" : "Not Found") << "\n";
}

int main() {
    try {
        solve();
    } catch (const exception& e) {
        cerr << "Error: " << e.what() << "\n";
        return 1;
    }

    return 0;
}
