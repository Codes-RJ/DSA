import java.util.*;
import java.io.*;
import java.math.*;
import java.text.*;
import java.time.*;
import java.util.function.*;
import java.util.stream.*;

/**
 * Data Structure Templates for Competitive Programming and DSA Practice
 * Includes comprehensive implementations of common data structures
 */
public class DataStructureTemplates {
    
    // Fast I/O setup
    private static final FastScanner fs = new FastScanner(System.in);
    private static final PrintWriter out = new PrintWriter(System.out);
    
    // Constants
    private static final int MOD = 1000000007;
    private static final int INF = Integer.MAX_VALUE;
    private static final long LINF = Long.MAX_VALUE;
    
    // Fast Scanner class
    static class FastScanner {
        private final BufferedReader br;
        private StringTokenizer st;
        
        public FastScanner(InputStream in) {
            br = new BufferedReader(new InputStreamReader(in));
        }
        
        public String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        
        public int nextInt() {
            return Integer.parseInt(next());
        }
        
        public long nextLong() {
            return Long.parseLong(next());
        }
        
        public double nextDouble() {
            return Double.parseDouble(next());
        }
        
        public String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
        
        public int[] readIntArray(int n) {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = nextInt();
            }
            return arr;
        }
        
        public long[] readLongArray(int n) {
            long[] arr = new long[n];
            for (int i = 0; i < n; i++) {
                arr[i] = nextLong();
            }
            return arr;
        }
    }
    
    // =============================================
    // LINKED LIST IMPLEMENTATIONS
    // =============================================
    
    // Singly Linked List Node
    static class ListNode {
        int val;
        ListNode next;
        
        ListNode(int val) {
            this.val = val;
            this.next = null;
        }
    }
    
    // Singly Linked List
    static class LinkedList {
        private ListNode head;
        private int size;
        
        public LinkedList() {
            head = null;
            size = 0;
        }
        
        public void insertAtHead(int val) {
            ListNode newNode = new ListNode(val);
            newNode.next = head;
            head = newNode;
            size++;
        }
        
        public void insertAtTail(int val) {
            ListNode newNode = new ListNode(val);
            if (head == null) {
                head = newNode;
            } else {
                ListNode current = head;
                while (current.next != null) {
                    current = current.next;
                }
                current.next = newNode;
            }
            size++;
        }
        
        public void deleteAtHead() {
            if (head == null) return;
            head = head.next;
            size--;
        }
        
        public void deleteAtTail() {
            if (head == null) return;
            if (head.next == null) {
                head = null;
            } else {
                ListNode current = head;
                while (current.next.next != null) {
                    current = current.next;
                }
                current.next = null;
            }
            size--;
        }
        
        public boolean search(int val) {
            ListNode current = head;
            while (current != null) {
                if (current.val == val) return true;
                current = current.next;
            }
            return false;
        }
        
        public void printList() {
            ListNode current = head;
            while (current != null) {
                out.print(current.val + " -> ");
                current = current.next;
            }
            out.println("NULL");
        }
        
        public List<Integer> toList() {
            List<Integer> result = new ArrayList<>();
            ListNode current = head;
            while (current != null) {
                result.add(current.val);
                current = current.next;
            }
            return result;
        }
        
        public int getSize() { return size; }
        public boolean isEmpty() { return size == 0; }
    }
    
    // Doubly Linked List Node
    static class DoublyListNode {
        int val;
        DoublyListNode prev;
        DoublyListNode next;
        
        DoublyListNode(int val) {
            this.val = val;
            this.prev = null;
            this.next = null;
        }
    }
    
    // Doubly Linked List
    static class DoublyLinkedList {
        private DoublyListNode head;
        private DoublyListNode tail;
        private int size;
        
        public DoublyLinkedList() {
            head = null;
            tail = null;
            size = 0;
        }
        
        public void insertAtHead(int val) {
            DoublyListNode newNode = new DoublyListNode(val);
            if (head == null) {
                head = tail = newNode;
            } else {
                newNode.next = head;
                head.prev = newNode;
                head = newNode;
            }
            size++;
        }
        
        public void insertAtTail(int val) {
            DoublyListNode newNode = new DoublyListNode(val);
            if (tail == null) {
                head = tail = newNode;
            } else {
                tail.next = newNode;
                newNode.prev = tail;
                tail = newNode;
            }
            size++;
        }
        
        public void deleteAtHead() {
            if (head == null) return;
            DoublyListNode temp = head;
            head = head.next;
            if (head != null) head.prev = null;
            else tail = null;
            size--;
        }
        
        public void deleteAtTail() {
            if (tail == null) return;
            DoublyListNode temp = tail;
            tail = tail.prev;
            if (tail != null) tail.next = null;
            else head = null;
            size--;
        }
        
        public void printList() {
            DoublyListNode current = head;
            while (current != null) {
                out.print(current.val + " <-> ");
                current = current.next;
            }
            out.println("NULL");
        }
        
        public List<Integer> toList() {
            List<Integer> result = new ArrayList<>();
            DoublyListNode current = head;
            while (current != null) {
                result.add(current.val);
                current = current.next;
            }
            return result;
        }
        
        public int getSize() { return size; }
        public boolean isEmpty() { return size == 0; }
    }
    
    // =============================================
    // STACK IMPLEMENTATIONS
    // =============================================
    
    // Array-based Stack
    static class ArrayStack<T> {
        private List<T> elements;
        private int capacity;
        
        public ArrayStack(int capacity) {
            this.capacity = capacity;
            this.elements = new ArrayList<>(capacity);
        }
        
        public void push(T element) {
            if (elements.size() < capacity) {
                elements.add(element);
            } else {
                throw new RuntimeException("Stack is full");
            }
        }
        
        public T pop() {
            if (empty()) {
                throw new RuntimeException("Stack is empty");
            }
            return elements.remove(elements.size() - 1);
        }
        
        public T peek() {
            if (empty()) {
                throw new RuntimeException("Stack is empty");
            }
            return elements.get(elements.size() - 1);
        }
        
        public boolean empty() {
            return elements.isEmpty();
        }
        
        public int size() {
            return elements.size();
        }
        
        public void clear() {
            elements.clear();
        }
    }
    
    // Linked List-based Stack
    static class LinkedListStack<T> {
        private static class Node<T> {
            T data;
            Node<T> next;
            
            Node(T data) {
                this.data = data;
                this.next = null;
            }
        }
        
        private Node<T> top;
        private int stackSize;
        
        public LinkedListStack() {
            top = null;
            stackSize = 0;
        }
        
        public void push(T element) {
            Node<T> newNode = new Node<>(element);
            newNode.next = top;
            top = newNode;
            stackSize++;
        }
        
        public T pop() {
            if (empty()) {
                throw new RuntimeException("Stack is empty");
            }
            T element = top.data;
            top = top.next;
            stackSize--;
            return element;
        }
        
        public T peek() {
            if (empty()) {
                throw new RuntimeException("Stack is empty");
            }
            return top.data;
        }
        
        public boolean empty() {
            return top == null;
        }
        
        public int size() {
            return stackSize;
        }
    }
    
    // =============================================
    // QUEUE IMPLEMENTATIONS
    // =============================================
    
    // Array-based Queue (Circular Queue)
    static class ArrayQueue<T> {
        private List<T> elements;
        private int front;
        private int rear;
        private int capacity;
        private int queueSize;
        
        public ArrayQueue(int capacity) {
            this.capacity = capacity;
            this.elements = new ArrayList<>(capacity);
            this.front = 0;
            this.rear = -1;
            this.queueSize = 0;
        }
        
        public void enqueue(T element) {
            if (queueSize == capacity) {
                throw new RuntimeException("Queue is full");
            }
            rear = (rear + 1) % capacity;
            elements.add(rear, element);
            queueSize++;
        }
        
        public T dequeue() {
            if (empty()) {
                throw new RuntimeException("Queue is empty");
            }
            T element = elements.get(front);
            front = (front + 1) % capacity;
            queueSize--;
            return element;
        }
        
        public T front() {
            if (empty()) {
                throw new RuntimeException("Queue is empty");
            }
            return elements.get(front);
        }
        
        public boolean empty() {
            return queueSize == 0;
        }
        
        public int size() {
            return queueSize;
        }
        
        public boolean isFull() {
            return queueSize == capacity;
        }
    }
    
    // Linked List-based Queue
    static class LinkedListQueue<T> {
        private static class Node<T> {
            T data;
            Node<T> next;
            
            Node(T data) {
                this.data = data;
                this.next = null;
            }
        }
        
        private Node<T> front;
        private Node<T> rear;
        private int queueSize;
        
        public LinkedListQueue() {
            front = null;
            rear = null;
            queueSize = 0;
        }
        
        public void enqueue(T element) {
            Node<T> newNode = new Node<>(element);
            if (empty()) {
                front = rear = newNode;
            } else {
                rear.next = newNode;
                rear = newNode;
            }
            queueSize++;
        }
        
        public T dequeue() {
            if (empty()) {
                throw new RuntimeException("Queue is empty");
            }
            T element = front.data;
            front = front.next;
            if (front == null) rear = null;
            queueSize--;
            return element;
        }
        
        public T front() {
            if (empty()) {
                throw new RuntimeException("Queue is empty");
            }
            return front.data;
        }
        
        public boolean empty() {
            return front == null;
        }
        
        public int size() {
            return queueSize;
        }
    }
    
    // =============================================
    // BINARY TREE IMPLEMENTATIONS
    // =============================================
    
    // Binary Tree Node
    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        
        TreeNode(int val) {
            this.val = val;
            this.left = null;
            this.right = null;
        }
    }
    
    // Binary Tree
    static class BinaryTree {
        private TreeNode root;
        
        public BinaryTree() {
            root = null;
        }
        
        public void insert(int val) {
            root = insertRecursive(root, val);
        }
        
        private TreeNode insertRecursive(TreeNode node, int val) {
            if (node == null) {
                return new TreeNode(val);
            }
            
            if (val < node.val) {
                node.left = insertRecursive(node.left, val);
            } else {
                node.right = insertRecursive(node.right, val);
            }
            
            return node;
        }
        
        public boolean search(int val) {
            return searchRecursive(root, val);
        }
        
        private boolean searchRecursive(TreeNode node, int val) {
            if (node == null) return false;
            if (node.val == val) return true;
            if (val < node.val) return searchRecursive(node.left, val);
            return searchRecursive(node.right, val);
        }
        
        public void inorderTraversal() {
            inorderRecursive(root);
            out.println();
        }
        
        private void inorderRecursive(TreeNode node) {
            if (node != null) {
                inorderRecursive(node.left);
                out.print(node.val + " ");
                inorderRecursive(node.right);
            }
        }
        
        public void preorderTraversal() {
            preorderRecursive(root);
            out.println();
        }
        
        private void preorderRecursive(TreeNode node) {
            if (node != null) {
                out.print(node.val + " ");
                preorderRecursive(node.left);
                preorderRecursive(node.right);
            }
        }
        
        public void postorderTraversal() {
            postorderRecursive(root);
            out.println();
        }
        
        private void postorderRecursive(TreeNode node) {
            if (node != null) {
                postorderRecursive(node.left);
                postorderRecursive(node.right);
                out.print(node.val + " ");
            }
        }
        
        public int getHeight() {
            return getHeightRecursive(root);
        }
        
        private int getHeightRecursive(TreeNode node) {
            if (node == null) return 0;
            return 1 + Math.max(getHeightRecursive(node.left), getHeightRecursive(node.right));
        }
        
        public int getSize() {
            return getSizeRecursive(root);
        }
        
        private int getSizeRecursive(TreeNode node) {
            if (node == null) return 0;
            return 1 + getSizeRecursive(node.left) + getSizeRecursive(node.right);
        }
        
        public boolean isBST() {
            return isBSTRecursive(root, null, null);
        }
        
        private boolean isBSTRecursive(TreeNode node, Integer min, Integer max) {
            if (node == null) return true;
            if ((min != null && node.val <= min) || (max != null && node.val >= max)) {
                return false;
            }
            return isBSTRecursive(node.left, min, node.val - 1) &&
                   isBSTRecursive(node.right, node.val + 1, max);
        }
    }
    
    // Binary Search Tree
    static class BST {
        private TreeNode root;
        
        public BST() {
            root = null;
        }
        
        public void insert(int val) {
            root = insertRecursive(root, val);
        }
        
        private TreeNode insertRecursive(TreeNode node, int val) {
            if (node == null) {
                return new TreeNode(val);
            }
            
            if (val < node.val) {
                node.left = insertRecursive(node.left, val);
            } else if (val > node.val) {
                node.right = insertRecursive(node.right, val);
            }
            
            return node;
        }
        
        public boolean search(int val) {
            return searchRecursive(root, val);
        }
        
        private boolean searchRecursive(TreeNode node, int val) {
            if (node == null) return false;
            if (node.val == val) return true;
            if (val < node.val) return searchRecursive(node.left, val);
            return searchRecursive(node.right, val);
        }
        
        public void remove(int val) {
            root = removeRecursive(root, val);
        }
        
        private TreeNode removeRecursive(TreeNode node, int val) {
            if (node == null) return node;
            
            if (val < node.val) {
                node.left = removeRecursive(node.left, val);
            } else if (val > node.val) {
                node.right = removeRecursive(node.right, val);
            } else {
                // Node with one child or no child
                if (node.left == null) {
                    return node.right;
                } else if (node.right == null) {
                    return node.left;
                }
                
                // Node with two children
                TreeNode temp = findMin(node.right);
                node.val = temp.val;
                node.right = removeRecursive(node.right, temp.val);
            }
            
            return node;
        }
        
        private TreeNode findMin(TreeNode node) {
            TreeNode current = node;
            while (current != null && current.left != null) {
                current = current.left;
            }
            return current;
        }
        
        public void inorderTraversal() {
            inorderRecursive(root);
            out.println();
        }
        
        private void inorderRecursive(TreeNode node) {
            if (node != null) {
                inorderRecursive(node.left);
                out.print(node.val + " ");
                inorderRecursive(node.right);
            }
        }
    }
    
    // =============================================
    // GRAPH IMPLEMENTATIONS
    // =============================================
    
    // Graph Node
    static class GraphNode {
        int val;
        List<GraphNode> neighbors;
        
        GraphNode(int val) {
            this.val = val;
            this.neighbors = new ArrayList<>();
        }
    }
    
    // Graph (Adjacency List)
    static class Graph {
        private Map<Integer, List<Integer>> adjacencyList;
        private boolean directed;
        
        public Graph(boolean directed) {
            this.adjacencyList = new HashMap<>();
            this.directed = directed;
        }
        
        public void addNode(int val) {
            adjacencyList.putIfAbsent(val, new ArrayList<>());
        }
        
        public void addEdge(int from, int to) {
            addNode(from);
            addNode(to);
            adjacencyList.get(from).add(to);
            if (!directed) {
                adjacencyList.get(to).add(from);
            }
        }
        
        public void removeEdge(int from, int to) {
            if (adjacencyList.containsKey(from) && adjacencyList.containsKey(to)) {
                adjacencyList.get(from).remove(Integer.valueOf(to));
                if (!directed) {
                    adjacencyList.get(to).remove(Integer.valueOf(from));
                }
            }
        }
        
        public boolean hasNode(int val) {
            return adjacencyList.containsKey(val);
        }
        
        public boolean hasEdge(int from, int to) {
            if (!adjacencyList.containsKey(from)) return false;
            return adjacencyList.get(from).contains(to);
        }
        
        public List<Integer> getNeighbors(int val) {
            return adjacencyList.getOrDefault(val, new ArrayList<>());
        }
        
        public void printGraph() {
            for (Map.Entry<Integer, List<Integer>> entry : adjacencyList.entrySet()) {
                out.print("Node " + entry.getKey() + ": ");
                for (int neighbor : entry.getValue()) {
                    out.print(neighbor + " ");
                }
                out.println();
            }
        }
        
        // BFS Traversal
        public List<Integer> bfs(int start) {
            List<Integer> result = new ArrayList<>();
            if (!adjacencyList.containsKey(start)) return result;
            
            Queue<Integer> queue = new LinkedList<>();
            Set<Integer> visited = new HashSet<>();
            
            queue.offer(start);
            visited.add(start);
            
            while (!queue.isEmpty()) {
                int current = queue.poll();
                result.add(current);
                
                for (int neighbor : adjacencyList.get(current)) {
                    if (!visited.contains(neighbor)) {
                        visited.add(neighbor);
                        queue.offer(neighbor);
                    }
                }
            }
            
            return result;
        }
        
        // DFS Traversal
        public List<Integer> dfs(int start) {
            List<Integer> result = new ArrayList<>();
            if (!adjacencyList.containsKey(start)) return result;
            
            Set<Integer> visited = new HashSet<>();
            Stack<Integer> stack = new Stack<>();
            
            stack.push(start);
            visited.add(start);
            
            while (!stack.isEmpty()) {
                int current = stack.pop();
                result.add(current);
                
                for (int neighbor : adjacencyList.get(current)) {
                    if (!visited.contains(neighbor)) {
                        visited.add(neighbor);
                        stack.push(neighbor);
                    }
                }
            }
            
            return result;
        }
        
        public int getVertexCount() {
            return adjacencyList.size();
        }
        
        public Map<Integer, List<Integer>> getAdjacencyList() {
            return adjacencyList;
        }
    }
    
    // =============================================
    // PRIORITY QUEUE (HEAP) IMPLEMENTATIONS
    // =============================================
    
    // Min-Heap
    static class MinHeap<T extends Comparable<T>> {
        private List<T> heap;
        
        public MinHeap() {
            heap = new ArrayList<>();
        }
        
        public void add(T item) {
            heap.add(item);
            heapifyUp(heap.size() - 1);
        }
        
        public T remove() {
            if (empty()) {
                throw new RuntimeException("Heap is empty");
            }
            T item = heap.get(0);
            T lastItem = heap.remove(heap.size() - 1);
            if (!empty()) {
                heap.set(0, lastItem);
                heapifyDown(0);
            }
            return item;
        }
        
        public T peek() {
            if (empty()) {
                throw new RuntimeException("Heap is empty");
            }
            return heap.get(0);
        }
        
        public boolean empty() {
            return heap.isEmpty();
        }
        
        public int size() {
            return heap.size();
        }
        
        private void heapifyUp(int index) {
            while (index > 0) {
                int parent = (index - 1) / 2;
                if (heap.get(parent).compareTo(heap.get(index)) <= 0) break;
                Collections.swap(heap, parent, index);
                index = parent;
            }
        }
        
        private void heapifyDown(int index) {
            int n = heap.size();
            while (true) {
                int left = 2 * index + 1;
                int right = 2 * index + 2;
                int smallest = index;
                
                if (left < n && heap.get(left).compareTo(heap.get(smallest)) < 0) {
                    smallest = left;
                }
                if (right < n && heap.get(right).compareTo(heap.get(smallest)) < 0) {
                    smallest = right;
                }
                
                if (smallest == index) break;
                Collections.swap(heap, index, smallest);
                index = smallest;
            }
        }
    }
    
    // Max-Heap
    static class MaxHeap<T extends Comparable<T>> {
        private List<T> heap;
        
        public MaxHeap() {
            heap = new ArrayList<>();
        }
        
        public void add(T item) {
            heap.add(item);
            heapifyUp(heap.size() - 1);
        }
        
        public T remove() {
            if (empty()) {
                throw new RuntimeException("Heap is empty");
            }
            T item = heap.get(0);
            T lastItem = heap.remove(heap.size() - 1);
            if (!empty()) {
                heap.set(0, lastItem);
                heapifyDown(0);
            }
            return item;
        }
        
        public T peek() {
            if (empty()) {
                throw new RuntimeException("Heap is empty");
            }
            return heap.get(0);
        }
        
        public boolean empty() {
            return heap.isEmpty();
        }
        
        public int size() {
            return heap.size();
        }
        
        private void heapifyUp(int index) {
            while (index > 0) {
                int parent = (index - 1) / 2;
                if (heap.get(parent).compareTo(heap.get(index)) >= 0) break;
                Collections.swap(heap, parent, index);
                index = parent;
            }
        }
        
        private void heapifyDown(int index) {
            int n = heap.size();
            while (true) {
                int left = 2 * index + 1;
                int right = 2 * index + 2;
                int largest = index;
                
                if (left < n && heap.get(left).compareTo(heap.get(largest)) > 0) {
                    largest = left;
                }
                if (right < n && heap.get(right).compareTo(heap.get(largest)) > 0) {
                    largest = right;
                }
                
                if (largest == index) break;
                Collections.swap(heap, index, largest);
                index = largest;
            }
        }
    }
    
    // =============================================
    // HASH TABLE IMPLEMENTATION
    // =============================================
    
    // Hash Table with Separate Chaining
    static class HashTable<K, V> {
        private static final int DEFAULT_CAPACITY = 16;
        private LinkedList<Entry<K, V>>[] table;
        private int size;
        
        static class Entry<K, V> {
            K key;
            V value;
            
            Entry(K key, V value) {
                this.key = key;
                this.value = value;
            }
        }
        
        @SuppressWarnings("unchecked")
        public HashTable() {
            table = new LinkedList[DEFAULT_CAPACITY];
            size = 0;
        }
        
        @SuppressWarnings("unchecked")
        public HashTable(int capacity) {
            table = new LinkedList[capacity];
            size = 0;
        }
        
        private int hash(K key) {
            return Math.abs(key.hashCode()) % table.length;
        }
        
        public void put(K key, V value) {
            int index = hash(key);
            if (table[index] == null) {
                table[index] = new LinkedList<>();
            }
            
            // Check if key already exists
            for (Entry<K, V> entry : table[index]) {
                if (entry.key.equals(key)) {
                    entry.value = value;
                    return;
                }
            }
            
            table[index].add(new Entry<>(key, value));
            size++;
        }
        
        public V get(K key) {
            int index = hash(key);
            if (table[index] == null) return null;
            
            for (Entry<K, V> entry : table[index]) {
                if (entry.key.equals(key)) {
                    return entry.value;
                }
            }
            
            return null;
        }
        
        public V remove(K key) {
            int index = hash(key);
            if (table[index] == null) return null;
            
            Iterator<Entry<K, V>> iterator = table[index].iterator();
            while (iterator.hasNext()) {
                Entry<K, V> entry = iterator.next();
                if (entry.key.equals(key)) {
                    iterator.remove();
                    size--;
                    return entry.value;
                }
            }
            
            return null;
        }
        
        public boolean containsKey(K key) {
            return get(key) != null;
        }
        
        public int size() {
            return size;
        }
        
        public boolean isEmpty() {
            return size == 0;
        }
    }
    
    // =============================================
    // DISJOINT SET UNION (UNION-FIND)
    // =============================================
    
    static class DSU {
        private int[] parent;
        private int[] rank;
        
        public DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }
        
        public int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }
        
        public void union(int x, int y) {
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
        
        public boolean isConnected(int x, int y) {
            return find(x) == find(y);
        }
    }
    
    // =============================================
    // TRIE IMPLEMENTATION
    // =============================================
    
    static class TrieNode {
        Map<Character, TrieNode> children;
        boolean isEndOfWord;
        
        TrieNode() {
            children = new HashMap<>();
            isEndOfWord = false;
        }
    }
    
    static class Trie {
        private TrieNode root;
        
        public Trie() {
            root = new TrieNode();
        }
        
        public void insert(String word) {
            TrieNode current = root;
            for (char c : word.toCharArray()) {
                current.children.putIfAbsent(c, new TrieNode());
                current = current.children.get(c);
            }
            current.isEndOfWord = true;
        }
        
        public boolean search(String word) {
            TrieNode current = root;
            for (char c : word.toCharArray()) {
                if (!current.children.containsKey(c)) {
                    return false;
                }
                current = current.children.get(c);
            }
            return current.isEndOfWord;
        }
        
        public boolean startsWith(String prefix) {
            TrieNode current = root;
            for (char c : prefix.toCharArray()) {
                if (!current.children.containsKey(c)) {
                    return false;
                }
                current = current.children.get(c);
            }
            return true;
        }
        
        public void remove(String word) {
            remove(root, word, 0);
        }
        
        private boolean remove(TrieNode node, String word, int depth) {
            if (depth == word.length()) {
                if (!node.isEndOfWord) return false;
                node.isEndOfWord = false;
                return node.children.isEmpty();
            }
            
            char c = word.charAt(depth);
            if (!node.children.containsKey(c)) {
                return false;
            }
            
            TrieNode childNode = node.children.get(c);
            boolean shouldDeleteChild = remove(childNode, word, depth + 1);
            
            if (shouldDeleteChild) {
                node.children.remove(c);
                return node.children.isEmpty() && !node.isEndOfWord;
            }
            
            return false;
        }
    }
    
    // =============================================
    // ADVANCED DATA STRUCTURES
    // =============================================
    
    // Segment Tree
    static class SegmentTree {
        private int[] tree;
        private int n;
        
        public SegmentTree(int[] arr) {
            n = arr.length;
            tree = new int[4 * n];
            buildTree(arr, 0, 0, n - 1);
        }
        
        private void buildTree(int[] arr, int node, int start, int end) {
            if (start == end) {
                tree[node] = arr[start];
            } else {
                int mid = (start + end) / 2;
                buildTree(arr, 2 * node + 1, start, mid);
                buildTree(arr, 2 * node + 2, mid + 1, end);
                tree[node] = Math.max(tree[2 * node + 1], tree[2 * node + 2]);
            }
        }
        
        public void update(int index, int value) {
            update(0, 0, n - 1, index, value);
        }
        
        private void update(int node, int start, int end, int index, int value) {
            if (start == end) {
                tree[node] = value;
            } else {
                int mid = (start + end) / 2;
                if (index <= mid) {
                    update(2 * node + 1, start, mid, index, value);
                } else {
                    update(2 * node + 2, mid + 1, end, index, value);
                }
                tree[node] = Math.max(tree[2 * node + 1], tree[2 * node + 2]);
            }
        }
        
        public int query(int left, int right) {
            return query(0, 0, n - 1, left, right);
        }
        
        private int query(int node, int start, int end, int left, int right) {
            if (right < start || end < left) {
                return Integer.MIN_VALUE;
            }
            if (left <= start && end <= right) {
                return tree[node];
            }
            
            int mid = (start + end) / 2;
            return Math.max(query(2 * node + 1, start, mid, left, right),
                           query(2 * node + 2, mid + 1, end, left, right));
        }
    }
    
    // Fenwick Tree (Binary Indexed Tree)
    static class FenwickTree {
        private int[] tree;
        private int n;
        
        public FenwickTree(int size) {
            n = size;
            tree = new int[n + 1];
        }
        
        public FenwickTree(int[] arr) {
            n = arr.length;
            tree = new int[n + 1];
            for (int i = 0; i < n; i++) {
                update(i + 1, arr[i]);
            }
        }
        
        public void update(int index, int delta) {
            while (index <= n) {
                tree[index] += delta;
                index += index & -index;
            }
        }
        
        public int query(int index) {
            int sum = 0;
            while (index > 0) {
                sum += tree[index];
                index -= index & -index;
            }
            return sum;
        }
        
        public int query(int left, int right) {
            return query(right) - query(left - 1);
        }
    }
    
    // =============================================
    // UTILITY METHODS
    // =============================================
    
    static class Utils {
        
        // Print list
        public static void printList(List<?> list) {
            for (Object x : list) {
                out.print(x + " ");
            }
            out.println();
        }
        
        // Print 2D list
        public static void print2DList(List<List<?>> list) {
            for (List<?> row : list) {
                for (Object x : row) {
                    out.print(x + " ");
                }
                out.println();
            }
        }
        
        // Generate random array
        public static int[] generateRandomArray(int n, int min, int max) {
            Random rand = new Random();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = rand.nextInt(max - min + 1) + min;
            }
            return arr;
        }
        
        // Generate random list
        public static List<Integer> generateRandomList(int n, int min, int max) {
            Random rand = new Random();
            List<Integer> list = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                list.add(rand.nextInt(max - min + 1) + min);
            }
            return list;
        }
    }
    
    // =============================================
    // MAIN SOLVE FUNCTION
    // =============================================
    
    public static void solve() {
        out.println("=== Data Structure Templates Demonstration ===\n");
        
        // Linked List Demo
        out.println("1. Linked List Demo:");
        LinkedList list = new LinkedList();
        list.insertAtHead(10);
        list.insertAtTail(20);
        list.insertAtHead(5);
        list.insertAtTail(25);
        out.print("Linked List: ");
        list.printList();
        out.println("Search 20: " + (list.search(20) ? "Found" : "Not Found"));
        list.deleteAtHead();
        list.deleteAtTail();
        out.print("After deletions: ");
        list.printList();
        out.println("Size: " + list.getSize() + "\n");
        
        // Stack Demo
        out.println("2. Stack Demo:");
        ArrayStack<Integer> stack = new ArrayStack<>(10);
        stack.push(10);
        stack.push(20);
        stack.push(30);
        out.print("Stack elements: ");
        while (!stack.empty()) {
            out.print(stack.peek() + " ");
            stack.pop();
        }
        out.println("\n");
        
        // Queue Demo
        out.println("3. Queue Demo:");
        LinkedListQueue<Integer> queue = new LinkedListQueue<>();
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        out.print("Queue elements: ");
        while (!queue.empty()) {
            out.print(queue.front() + " ");
            queue.dequeue();
        }
        out.println("\n");
        
        // Binary Tree Demo
        out.println("4. Binary Tree Demo:");
        BinaryTree tree = new BinaryTree();
        tree.insert(50);
        tree.insert(30);
        tree.insert(70);
        tree.insert(20);
        tree.insert(40);
        tree.insert(60);
        tree.insert(80);
        out.print("Inorder traversal: ");
        tree.inorderTraversal();
        out.print("Preorder traversal: ");
        tree.preorderTraversal();
        out.print("Postorder traversal: ");
        tree.postorderTraversal();
        out.println("Tree height: " + tree.getHeight());
        out.println("Tree size: " + tree.getSize());
        out.println("Is BST: " + (tree.isBST() ? "Yes" : "No") + "\n");
        
        // BST Demo
        out.println("5. Binary Search Tree Demo:");
        BST bst = new BST();
        bst.insert(50);
        bst.insert(30);
        bst.insert(70);
        bst.insert(20);
        bst.insert(40);
        bst.insert(60);
        bst.insert(80);
        out.print("BST inorder: ");
        bst.inorderTraversal();
        out.println("Search 40: " + (bst.search(40) ? "Found" : "Not Found"));
        bst.remove(20);
        bst.remove(70);
        out.print("After removing 20 and 70: ");
        bst.inorderTraversal();
        out.println();
        
        // Graph Demo
        out.println("6. Graph Demo:");
        Graph graph = new Graph(true); // Directed graph
        graph.addEdge(1, 2);
        graph.addEdge(2, 3);
        graph.addEdge(3, 4);
        graph.addEdge(4, 1);
        out.println("Graph adjacency list:");
        graph.printGraph();
        out.print("BFS from 1: ");
        Utils.printList(graph.bfs(1));
        out.print("DFS from 1: ");
        Utils.printList(graph.dfs(1));
        out.println("Has edge 1->2: " + (graph.hasEdge(1, 2) ? "Yes" : "No") + "\n");
        
        // Heap Demo
        out.println("7. Heap Demo:");
        MinHeap<Integer> minHeap = new MinHeap<>();
        minHeap.add(30);
        minHeap.add(10);
        minHeap.add(20);
        minHeap.add(40);
        out.print("Min-heap elements: ");
        while (!minHeap.empty()) {
            out.print(minHeap.peek() + " ");
            minHeap.remove();
        }
        out.println();
        
        MaxHeap<Integer> maxHeap = new MaxHeap<>();
        maxHeap.add(30);
        maxHeap.add(10);
        maxHeap.add(20);
        maxHeap.add(40);
        out.print("Max-heap elements: ");
        while (!maxHeap.empty()) {
            out.print(maxHeap.peek() + " ");
            maxHeap.remove();
        }
        out.println("\n");
        
        // Hash Table Demo
        out.println("8. Hash Table Demo:");
        HashTable<String, Integer> hashTable = new HashTable<>();
        hashTable.put("apple", 5);
        hashTable.put("banana", 3);
        hashTable.put("orange", 8);
        out.println("Get apple: " + hashTable.get("apple"));
        out.println("Contains banana: " + (hashTable.containsKey("banana") ? "Yes" : "No"));
        hashTable.remove("apple");
        out.println("Contains apple after removal: " + (hashTable.containsKey("apple") ? "Yes" : "No") + "\n");
        
        // DSU Demo
        out.println("9. Disjoint Set Union Demo:");
        DSU dsu = new DSU(5);
        dsu.union(0, 1);
        dsu.union(1, 2);
        dsu.union(3, 4);
        out.println("Is 0 connected to 2: " + (dsu.isConnected(0, 2) ? "Yes" : "No"));
        out.println("Is 0 connected to 3: " + (dsu.isConnected(0, 3) ? "Yes" : "No") + "\n");
        
        // Trie Demo
        out.println("10. Trie Demo:");
        Trie trie = new Trie();
        trie.insert("hello");
        trie.insert("world");
        trie.insert("help");
        out.println("Search 'hello': " + (trie.search("hello") ? "Found" : "Not Found"));
        out.println("Search 'hell': " + (trie.search("hell") ? "Found" : "Not Found"));
        out.println("Starts with 'hel': " + (trie.startsWith("hel") ? "Yes" : "No"));
        trie.remove("hello");
        out.println("Search 'hello' after removal: " + (trie.search("hello") ? "Found" : "Not Found") + "\n");
        
        // Segment Tree Demo
        out.println("11. Segment Tree Demo:");
        int[] arr = {1, 3, 2, 7, 9, 11};
        SegmentTree segmentTree = new SegmentTree(arr);
        out.println("Range query (1, 4): " + segmentTree.query(1, 4));
        segmentTree.update(2, 5);
        out.println("After updating index 2 to 5:");
        out.println("Range query (1, 4): " + segmentTree.query(1, 4) + "\n");
        
        // Fenwick Tree Demo
        out.println("12. Fenwick Tree Demo:");
        int[] fenwickArr = {1, 2, 3, 4, 5};
        FenwickTree fenwickTree = new FenwickTree(fenwickArr);
        out.println("Prefix sum up to index 3: " + fenwickTree.query(3));
        out.println("Range sum (2, 4): " + fenwickTree.query(2, 4));
        fenwickTree.update(3, 2); // Add 2 to index 3
        out.println("After updating index 3 by +2:");
        out.println("Prefix sum up to index 3: " + fenwickTree.query(3));
    }
    
    // Main method
    public static void main(String[] args) {
        try {
            solve();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            out.close();
        }
    }
}
