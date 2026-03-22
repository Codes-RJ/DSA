#!/usr/bin/env python3
"""
Data Structure Templates for Competitive Programming and DSA Practice
Includes comprehensive implementations of common data structures
"""

import sys
import math
import random
import bisect
import heapq
from collections import defaultdict, Counter, deque, OrderedDict
from typing import List, Dict, Set, Tuple, Optional, Any, Union, Callable
from itertools import permutations, combinations, product, accumulate
from functools import reduce, lru_cache
import time

# Fast I/O
def fast_input():
    """Fast input function for competitive programming"""
    return sys.stdin.readline().strip()

def fast_print(*args, **kwargs):
    """Fast print function for competitive programming"""
    print(*args, **kwargs)
    sys.stdout.flush()

# Constants
MOD = 10**9 + 7
INF = float('inf')
LINF = float('-inf')

# =============================================
# LINKED LIST IMPLEMENTATIONS
# =============================================

class ListNode:
    """Singly Linked List Node"""
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
        self.val = val
        self.next = next_node

class LinkedList:
    """Singly Linked List Implementation"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_at_head(self, val: int) -> None:
        """Insert node at the beginning of the list"""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_tail(self, val: int) -> None:
        """Insert node at the end of the list"""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def delete_at_head(self) -> None:
        """Delete node from the beginning of the list"""
        if not self.head:
            return
        self.head = self.head.next
        self.size -= 1
    
    def delete_at_tail(self) -> None:
        """Delete node from the end of the list"""
        if not self.head:
            return
        if not self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
        self.size -= 1
    
    def search(self, val: int) -> bool:
        """Search for a value in the list"""
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False
    
    def get_middle(self) -> Optional[ListNode]:
        """Get middle node using slow and fast pointers"""
        if not self.head:
            return None
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def reverse(self) -> None:
        """Reverse the linked list"""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def has_cycle(self) -> bool:
        """Detect cycle using Floyd's algorithm"""
        if not self.head:
            return False
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
    
    def print_list(self) -> None:
        """Print the linked list"""
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("NULL")
    
    def to_list(self) -> List[int]:
        """Convert linked list to Python list"""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def get_size(self) -> int:
        """Get the size of the list"""
        return self.size
    
    def is_empty(self) -> bool:
        """Check if the list is empty"""
        return self.size == 0

class DoublyListNode:
    """Doubly Linked List Node"""
    def __init__(self, val: int = 0, prev_node: 'DoublyListNode' = None, next_node: 'DoublyListNode' = None):
        self.val = val
        self.prev = prev_node
        self.next = next_node

class DoublyLinkedList:
    """Doubly Linked List Implementation"""
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert_at_head(self, val: int) -> None:
        """Insert node at the beginning of the list"""
        new_node = DoublyListNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def insert_at_tail(self, val: int) -> None:
        """Insert node at the end of the list"""
        new_node = DoublyListNode(val)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def delete_at_head(self) -> None:
        """Delete node from the beginning of the list"""
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
    
    def delete_at_tail(self) -> None:
        """Delete node from the end of the list"""
        if not self.tail:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
    
    def print_list(self) -> None:
        """Print the doubly linked list"""
        current = self.head
        while current:
            print(current.val, end=" <-> ")
            current = current.next
        print("NULL")
    
    def to_list(self) -> List[int]:
        """Convert doubly linked list to Python list"""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def get_size(self) -> int:
        """Get the size of the list"""
        return self.size
    
    def is_empty(self) -> bool:
        """Check if the list is empty"""
        return self.size == 0

# =============================================
# STACK IMPLEMENTATIONS
# =============================================

class ArrayStack:
    """Stack implementation using list"""
    
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.items = []
    
    def push(self, item) -> None:
        """Push item onto stack"""
        if len(self.items) >= self.capacity:
            raise OverflowError("Stack is full")
        self.items.append(item)
    
    def pop(self):
        """Pop item from stack"""
        if self.empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Peek at top item"""
        if self.empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def empty(self) -> bool:
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self) -> int:
        """Get stack size"""
        return len(self.items)
    
    def clear(self) -> None:
        """Clear the stack"""
        self.items.clear()
    
    def __str__(self):
        return str(self.items)

class LinkedListStack:
    """Stack implementation using linked list"""
    
    def __init__(self):
        self.top = None
        self.stack_size = 0
    
    def push(self, item) -> None:
        """Push item onto stack"""
        new_node = ListNode(item)
        new_node.next = self.top
        self.top = new_node
        self.stack_size += 1
    
    def pop(self):
        """Pop item from stack"""
        if self.empty():
            raise IndexError("Stack is empty")
        item = self.top.val
        self.top = self.top.next
        self.stack_size -= 1
        return item
    
    def peek(self):
        """Peek at top item"""
        if self.empty():
            raise IndexError("Stack is empty")
        return self.top.val
    
    def empty(self) -> bool:
        """Check if stack is empty"""
        return self.top is None
    
    def size(self) -> int:
        """Get stack size"""
        return self.stack_size
    
    def __str__(self):
        result = []
        current = self.top
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

# =============================================
# QUEUE IMPLEMENTATIONS
# =============================================

class ArrayQueue:
    """Queue implementation using list (circular queue)"""
    
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.queue_size = 0
    
    def enqueue(self, item) -> None:
        """Add item to queue"""
        if self.is_full():
            raise OverflowError("Queue is full")
        
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        self.queue_size += 1
    
    def dequeue(self):
        """Remove item from queue"""
        if self.empty():
            raise IndexError("Queue is empty")
        
        item = self.items[self.front]
        self.front = (self.front + 1) % self.capacity
        self.queue_size -= 1
        return item
    
    def front_element(self):
        """Get front element"""
        if self.empty():
            raise IndexError("Queue is empty")
        return self.items[self.front]
    
    def empty(self) -> bool:
        """Check if queue is empty"""
        return self.queue_size == 0
    
    def is_full(self) -> bool:
        """Check if queue is full"""
        return self.queue_size == self.capacity
    
    def size(self) -> int:
        """Get queue size"""
        return self.queue_size
    
    def __str__(self):
        if self.empty():
            return "Queue is empty"
        
        result = []
        i = self.front
        for _ in range(self.queue_size):
            result.append(str(self.items[i]))
            i = (i + 1) % self.capacity
        return " -> ".join(result)

class LinkedListQueue:
    """Queue implementation using linked list"""
    
    def __init__(self):
        self.front = None
        self.rear = None
        self.queue_size = 0
    
    def enqueue(self, item) -> None:
        """Add item to queue"""
        new_node = ListNode(item)
        if self.empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.queue_size += 1
    
    def dequeue(self):
        """Remove item from queue"""
        if self.empty():
            raise IndexError("Queue is empty")
        
        item = self.front.val
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.queue_size -= 1
        return item
    
    def front_element(self):
        """Get front element"""
        if self.empty():
            raise IndexError("Queue is empty")
        return self.front.val
    
    def empty(self) -> bool:
        """Check if queue is empty"""
        return self.front is None
    
    def size(self) -> int:
        """Get queue size"""
        return self.queue_size
    
    def __str__(self):
        result = []
        current = self.front
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

# =============================================
# BINARY TREE IMPLEMENTATIONS
# =============================================

class TreeNode:
    """Binary Tree Node"""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    """Binary Tree Implementation"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, val: int) -> None:
        """Insert value into BST"""
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node: TreeNode, val: int) -> TreeNode:
        """Helper function for recursive insertion"""
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        else:
            node.right = self._insert_recursive(node.right, val)
        
        return node
    
    def search(self, val: int) -> bool:
        """Search for value in BST"""
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node: TreeNode, val: int) -> bool:
        """Helper function for recursive search"""
        if not node:
            return False
        
        if node.val == val:
            return True
        elif val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
    
    def delete(self, val: int) -> None:
        """Delete value from BST"""
        self.root = self._delete_recursive(self.root, val)
    
    def _delete_recursive(self, node: TreeNode, val: int) -> TreeNode:
        """Helper function for recursive deletion"""
        if not node:
            return node
        
        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            # Node with one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node with two children
            node.val = self._find_min(node.right).val
            node.right = self._delete_recursive(node.right, node.val)
        
        return node
    
    def _find_min(self, node: TreeNode) -> TreeNode:
        """Find minimum value node"""
        current = node
        while current and current.left:
            current = current.left
        return current
    
    def inorder_traversal(self) -> List[int]:
        """Inorder traversal"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: TreeNode, result: List[int]) -> None:
        """Helper function for inorder traversal"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self) -> List[int]:
        """Preorder traversal"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node: TreeNode, result: List[int]) -> None:
        """Helper function for preorder traversal"""
        if node:
            result.append(node.val)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self) -> List[int]:
        """Postorder traversal"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node: TreeNode, result: List[int]) -> None:
        """Helper function for postorder traversal"""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.val)
    
    def level_order_traversal(self) -> List[List[int]]:
        """Level order traversal"""
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result
    
    def get_height(self) -> int:
        """Get height of the tree"""
        return self._get_height_recursive(self.root)
    
    def _get_height_recursive(self, node: TreeNode) -> int:
        """Helper function for height calculation"""
        if not node:
            return 0
        return 1 + max(self._get_height_recursive(node.left), self._get_height_recursive(node.right))
    
    def get_size(self) -> int:
        """Get size of the tree"""
        return self._get_size_recursive(self.root)
    
    def _get_size_recursive(self, node: TreeNode) -> int:
        """Helper function for size calculation"""
        if not node:
            return 0
        return 1 + self._get_size_recursive(node.left) + self._get_size_recursive(node.right)
    
    def is_bst(self) -> bool:
        """Check if tree is a valid BST"""
        return self._is_bst_helper(self.root, None, None)
    
    def _is_bst_helper(self, node: TreeNode, min_val: int, max_val: int) -> bool:
        """Helper function for BST validation"""
        if not node:
            return True
        
        if (min_val is not None and node.val <= min_val) or (max_val is not None and node.val >= max_val):
            return False
        
        return (self._is_bst_helper(node.left, min_val, node.val) and
                self._is_bst_helper(node.right, node.val, max_val))
    
    def lowest_common_ancestor(self, p: int, q: int) -> Optional[int]:
        """Find lowest common ancestor of two values"""
        return self._lca_helper(self.root, p, q)
    
    def _lca_helper(self, node: TreeNode, p: int, q: int) -> Optional[int]:
        """Helper function for LCA"""
        if not node:
            return None
        
        if node.val == p or node.val == q:
            return node.val
        
        left_lca = self._lca_helper(node.left, p, q)
        right_lca = self._lca_helper(node.right, p, q)
        
        if left_lca and right_lca:
            return node.val
        
        return left_lca if left_lca else right_lca

# =============================================
# GRAPH IMPLEMENTATIONS
# =============================================

class GraphNode:
    """Graph Node"""
    def __init__(self, val: int = 0):
        self.val = val
        self.neighbors = []

class Graph:
    """Graph implementation using adjacency list"""
    
    def __init__(self, directed: bool = False):
        self.adjacency_list = {}
        self.directed = directed
    
    def add_node(self, val: int) -> None:
        """Add node to graph"""
        if val not in self.adjacency_list:
            self.adjacency_list[val] = []
    
    def add_edge(self, from_node: int, to_node: int) -> None:
        """Add edge to graph"""
        self.add_node(from_node)
        self.add_node(to_node)
        self.adjacency_list[from_node].append(to_node)
        if not self.directed:
            self.adjacency_list[to_node].append(from_node)
    
    def remove_edge(self, from_node: int, to_node: int) -> None:
        """Remove edge from graph"""
        if from_node in self.adjacency_list and to_node in self.adjacency_list:
            if to_node in self.adjacency_list[from_node]:
                self.adjacency_list[from_node].remove(to_node)
            if not self.directed and from_node in self.adjacency_list[to_node]:
                self.adjacency_list[to_node].remove(from_node)
    
    def has_node(self, val: int) -> bool:
        """Check if node exists"""
        return val in self.adjacency_list
    
    def has_edge(self, from_node: int, to_node: int) -> bool:
        """Check if edge exists"""
        return (from_node in self.adjacency_list and 
                to_node in self.adjacency_list[from_node])
    
    def get_neighbors(self, val: int) -> List[int]:
        """Get neighbors of a node"""
        return self.adjacency_list.get(val, [])
    
    def bfs(self, start: int) -> List[int]:
        """Breadth-First Search"""
        result = []
        if start not in self.adjacency_list:
            return result
        
        queue = deque([start])
        visited = set([start])
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start: int) -> List[int]:
        """Depth-First Search"""
        result = []
        visited = set()
        self._dfs_helper(start, visited, result)
        return result
    
    def _dfs_helper(self, node: int, visited: Set[int], result: List[int]) -> None:
        """Helper function for DFS"""
        if node not in self.adjacency_list or node in visited:
            return
        
        visited.add(node)
        result.append(node)
        
        for neighbor in self.adjacency_list[node]:
            self._dfs_helper(neighbor, visited, result)
    
    def dfs_iterative(self, start: int) -> List[int]:
        """DFS (Iterative)"""
        result = []
        if start not in self.adjacency_list:
            return result
        
        stack = [start]
        visited = set([start])
        
        while stack:
            node = stack.pop()
            result.append(node)
            
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        
        return result
    
    def print_graph(self) -> None:
        """Print the graph"""
        for node, neighbors in self.adjacency_list.items():
            print(f"Node {node}: {neighbors}")
    
    def get_vertex_count(self) -> int:
        """Get number of vertices"""
        return len(self.adjacency_list)
    
    def get_edge_count(self) -> int:
        """Get number of edges"""
        count = sum(len(neighbors) for neighbors in self.adjacency_list.values())
        return count // 2 if not self.directed else count

# =============================================
# PRIORITY QUEUE (HEAP) IMPLEMENTATIONS
# =============================================

class MinHeap:
    """Min-Heap implementation"""
    
    def __init__(self):
        self.heap = []
    
    def push(self, item) -> None:
        """Add item to heap"""
        heapq.heappush(self.heap, item)
    
    def pop(self):
        """Remove and return smallest item"""
        if self.empty():
            raise IndexError("Heap is empty")
        return heapq.heappop(self.heap)
    
    def peek(self):
        """Peek at smallest item"""
        if self.empty():
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def empty(self) -> bool:
        """Check if heap is empty"""
        return len(self.heap) == 0
    
    def size(self) -> int:
        """Get heap size"""
        return len(self.heap)
    
    def __str__(self):
        return str(self.heap)

class MaxHeap:
    """Max-Heap implementation"""
    
    def __init__(self):
        self.heap = []
    
    def push(self, item) -> None:
        """Add item to heap"""
        heapq.heappush(self.heap, -item)
    
    def pop(self):
        """Remove and return largest item"""
        if self.empty():
            raise IndexError("Heap is empty")
        return -heapq.heappop(self.heap)
    
    def peek(self):
        """Peek at largest item"""
        if self.empty():
            raise IndexError("Heap is empty")
        return -self.heap[0]
    
    def empty(self) -> bool:
        """Check if heap is empty"""
        return len(self.heap) == 0
    
    def size(self) -> int:
        """Get heap size"""
        return len(self.heap)
    
    def __str__(self):
        return str([-x for x in self.heap])

# =============================================
# HASH TABLE IMPLEMENTATION
# =============================================

class HashTable:
    """Hash Table implementation with separate chaining"""
    
    def __init__(self, capacity: int = 16):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0
    
    def _hash(self, key) -> int:
        """Hash function"""
        return hash(key) % self.capacity
    
    def put(self, key, value) -> None:
        """Add key-value pair"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
        self.size += 1
    
    def get(self, key):
        """Get value by key"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return None
    
    def remove(self, key) -> None:
        """Remove key-value pair"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return
    
    def contains_key(self, key) -> bool:
        """Check if key exists"""
        return self.get(key) is not None
    
    def get_size(self) -> int:
        """Get table size"""
        return self.size
    
    def is_empty(self) -> bool:
        """Check if table is empty"""
        return self.size == 0
    
    def keys(self) -> List:
        """Get all keys"""
        keys = []
        for bucket in self.table:
            for k, v in bucket:
                keys.append(k)
        return keys
    
    def values(self) -> List:
        """Get all values"""
        values = []
        for bucket in self.table:
            for k, v in bucket:
                values.append(v)
        return values
    
    def items(self) -> List[Tuple]:
        """Get all key-value pairs"""
        items = []
        for bucket in self.table:
            for k, v in bucket:
                items.append((k, v))
        return items

# =============================================
# DISJOINT SET UNION (UNION-FIND)
# =============================================

class DisjointSetUnion:
    """Disjoint Set Union (Union-Find) implementation"""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x: int) -> int:
        """Find with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        """Union with rank optimization"""
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root == y_root:
            return
        
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
        
        self.components -= 1
    
    def connected(self, x: int, y: int) -> bool:
        """Check if two elements are connected"""
        return self.find(x) == self.find(y)
    
    def get_components(self) -> int:
        """Get number of components"""
        return self.components

# =============================================
# TRIE IMPLEMENTATION
# =============================================

class TrieNode:
    """Trie node"""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """Trie implementation"""
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """Insert word into trie"""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """Search word in trie"""
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word
    
    def starts_with(self, prefix: str) -> bool:
        """Check if any word starts with prefix"""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
    
    def remove(self, word: str) -> None:
        """Remove word from trie"""
        self._remove(self.root, word, 0)
    
    def _remove(self, node: TrieNode, word: str, depth: int) -> bool:
        """Helper function for remove"""
        if depth == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            return len(node.children) == 0
        
        char = word[depth]
        if char not in node.children:
            return False
        
        child_node = node.children[char]
        should_delete_child = self._remove(child_node, word, depth + 1)
        
        if should_delete_child:
            del node.children[char]
            return len(node.children) == 0 and not node.is_end_of_word
        
        return False
    
    def get_all_words(self) -> List[str]:
        """Get all words in trie"""
        words = []
        self._get_all_words_helper(self.root, "", words)
        return words
    
    def _get_all_words_helper(self, node: TrieNode, prefix: str, words: List[str]) -> None:
        """Helper function for getting all words"""
        if node.is_end_of_word:
            words.append(prefix)
        
        for char, child in node.children.items():
            self._get_all_words_helper(child, prefix + char, words)
    
    def count_words_with_prefix(self, prefix: str) -> int:
        """Count words with given prefix"""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        
        words = []
        self._get_all_words_helper(current, prefix, words)
        return len(words)

# =============================================
# ADVANCED DATA STRUCTURES
# =============================================

class SegmentTree:
    """Segment Tree implementation"""
    
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build_tree(arr, 0, 0, self.n - 1)
    
    def _build_tree(self, arr: List[int], node: int, start: int, end: int) -> None:
        """Build segment tree"""
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build_tree(arr, 2 * node + 1, start, mid)
            self._build_tree(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def update(self, index: int, value: int) -> None:
        """Update value at index"""
        self._update(0, 0, self.n - 1, index, value)
    
    def _update(self, node: int, start: int, end: int, index: int, value: int) -> None:
        """Helper function for update"""
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if index <= mid:
                self._update(2 * node + 1, start, mid, index, value)
            else:
                self._update(2 * node + 2, mid + 1, end, index, value)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def query(self, left: int, right: int) -> int:
        """Query range [left, right]"""
        return self._query(0, 0, self.n - 1, left, right)
    
    def _query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        """Helper function for query"""
        if right < start or end < left:
            return float('-inf')
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        return max(self._query(2 * node + 1, start, mid, left, right),
                  self._query(2 * node + 2, mid + 1, end, left, right))

class FenwickTree:
    """Fenwick Tree (Binary Indexed Tree) implementation"""
    
    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (self.n + 1)
    
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.tree = [0] * (self.n + 1)
        for i in range(self.n):
            self.update(i + 1, arr[i])
    
    def update(self, index: int, delta: int) -> None:
        """Update value at index (1-based)"""
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index: int) -> int:
        """Query prefix sum up to index (1-based)"""
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result
    
    def range_query(self, left: int, right: int) -> int:
        """Query range sum [left, right] (1-based)"""
        return self.query(right) - self.query(left - 1)

class LRUCache:
    """LRU Cache implementation"""
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()
    
    def get(self, key):
        """Get value by key"""
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return None
    
    def put(self, key, value) -> None:
        """Put key-value pair"""
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest = self.order.popleft()
            del self.cache[oldest]
        
        self.cache[key] = value
        self.order.append(key)
    
    def size(self) -> int:
        """Get cache size"""
        return len(self.cache)

class AVLNode:
    """AVL Tree Node"""
    def __init__(self, key: int, val: int = None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """AVL Tree implementation"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, key: int, val: int = None) -> None:
        """Insert key-value pair"""
        self.root = self._insert(self.root, key, val)
    
    def _insert(self, node: AVLNode, key: int, val: int) -> AVLNode:
        """Helper function for insert"""
        if not node:
            return AVLNode(key, val)
        
        if key < node.key:
            node.left = self._insert(node.left, key, val)
        elif key > node.key:
            node.right = self._insert(node.right, key, val)
        else:
            node.val = val
            return node
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        balance = self._get_balance(node)
        
        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        
        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        
        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        
        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node
    
    def _left_rotate(self, z: AVLNode) -> AVLNode:
        """Left rotation"""
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        return y
    
    def _right_rotate(self, z: AVLNode) -> AVLNode:
        """Right rotation"""
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        return y
    
    def _get_height(self, node: AVLNode) -> int:
        """Get height of node"""
        if not node:
            return 0
        return node.height
    
    def _get_balance(self, node: AVLNode) -> int:
        """Get balance factor of node"""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def search(self, key: int):
        """Search for key"""
        return self._search(self.root, key)
    
    def _search(self, node: AVLNode, key: int):
        """Helper function for search"""
        if not node:
            return None
        
        if key == node.key:
            return node.val
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
    
    def inorder_traversal(self) -> List[int]:
        """Inorder traversal"""
        result = []
        self._inorder_helper(self.root, result)
        return result
    
    def _inorder_helper(self, node: AVLNode, result: List[int]) -> None:
        """Helper function for inorder traversal"""
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.key)
            self._inorder_helper(node.right, result)

# =============================================
# UTILITY FUNCTIONS
# =============================================

def print_list(lst: List[Any]) -> None:
    """Print list elements"""
    print(' '.join(map(str, lst)))

def print_2d_list(matrix: List[List[Any]]) -> None:
    """Print 2D list"""
    for row in matrix:
        print(' '.join(map(str, row)))

def generate_random_array(n: int, min_val: int, max_val: int) -> List[int]:
    """Generate random array"""
    return [random.randint(min_val, max_val) for _ in range(n)]

def generate_random_list(n: int, min_val: int, max_val: int) -> List[int]:
    """Generate random list"""
    return [random.randint(min_val, max_val) for _ in range(n)]

# =============================================
# MAIN SOLVE FUNCTION
# =============================================

def solve():
    """Main solve function - modify this for each problem"""
    fast_print("=== Data Structure Templates Demonstration ===\n")
    
    # Linked List Demo
    fast_print("1. Linked List Demo:")
    linked_list = LinkedList()
    linked_list.insert_at_head(10)
    linked_list.insert_at_tail(20)
    linked_list.insert_at_head(5)
    linked_list.insert_at_tail(25)
    fast_print("Linked List:")
    linked_list.print_list()
    fast_print(f"Search 20: {linked_list.search(20)}")
    linked_list.delete_at_head()
    linked_list.delete_at_tail()
    fast_print("After deletions:")
    linked_list.print_list()
    fast_print(f"Size: {linked_list.get_size()}")
    fast_print(f"Is empty: {linked_list.is_empty()}")
    
    # Doubly Linked List Demo
    fast_print("\n2. Doubly Linked List Demo:")
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert_at_head(10)
    doubly_linked_list.insert_at_tail(20)
    doubly_linked_list.insert_at_head(5)
    doubly_linked_list.insert_at_tail(25)
    fast_print("Doubly Linked List:")
    doubly_linked_list.print_list()
    
    # Stack Demo
    fast_print("\n3. Stack Demo:")
    stack = ArrayStack()
    for i in [10, 20, 30]:
        stack.push(i)
    
    fast_print("Array Stack elements:")
    while not stack.empty():
        fast_print(stack.peek(), end=" ")
        stack.pop()
    fast_print()
    
    linked_stack = LinkedListStack()
    for i in [10, 20, 30]:
        linked_stack.push(i)
    
    fast_print("Linked List Stack elements:")
    while not linked_stack.empty():
        fast_print(linked_stack.peek(), end=" ")
        linked_stack.pop()
    fast_print()
    
    # Queue Demo
    fast_print("\n4. Queue Demo:")
    queue = ArrayQueue()
    for i in [10, 20, 30]:
        queue.enqueue(i)
    
    fast_print("Array Queue elements:")
    while not queue.empty():
        fast_print(queue.front_element(), end=" ")
        queue.dequeue()
    fast_print()
    
    linked_queue = LinkedListQueue()
    for i in [10, 20, 30]:
        linked_queue.enqueue(i)
    
    fast_print("Linked List Queue elements:")
    while not linked_queue.empty():
        fast_print(linked_queue.front_element(), end=" ")
        linked_queue.dequeue()
    fast_print()
    
    # Binary Tree Demo
    fast_print("\n5. Binary Tree Demo:")
    binary_tree = BinaryTree()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        binary_tree.insert(val)
    
    fast_print(f"Inorder traversal: {binary_tree.inorder_traversal()}")
    fast_print(f"Preorder traversal: {binary_tree.preorder_traversal()}")
    fast_print(f"Postorder traversal: {binary_tree.postorder_traversal()}")
    fast_print(f"Level order traversal: {binary_tree.level_order_traversal()}")
    fast_print(f"Tree height: {binary_tree.get_height()}")
    fast_print(f"Tree size: {binary_tree.get_size()}")
    fast_print(f"Is BST: {binary_tree.is_bst()}")
    fast_print(f"LCA of 20 and 40: {binary_tree.lowest_common_ancestor(20, 40)}")
    
    # Graph Demo
    fast_print("\n6. Graph Demo:")
    graph = Graph(directed=True)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 1)
    fast_print("Graph adjacency list:")
    graph.print_graph()
    fast_print(f"BFS from 1: {graph.bfs(1)}")
    fast_print(f"DFS from 1: {graph.dfs(1)}")
    fast_print(f"DFS (iterative) from 1: {graph.dfs_iterative(1)}")
    fast_print(f"Has edge 1->2: {graph.has_edge(1, 2)}")
    fast_print(f"Vertex count: {graph.get_vertex_count()}")
    fast_print(f"Edge count: {graph.get_edge_count()}")
    
    # Heap Demo
    fast_print("\n7. Heap Demo:")
    min_heap = MinHeap()
    for i in [30, 10, 20, 40]:
        min_heap.push(i)
    
    fast_print("Min-Heap elements:")
    while not min_heap.empty():
        fast_print(min_heap.peek(), end=" ")
        min_heap.pop()
    fast_print()
    
    max_heap = MaxHeap()
    for i in [30, 10, 20, 40]:
        max_heap.push(i)
    
    fast_print("Max-Heap elements:")
    while not max_heap.empty():
        fast_print(max_heap.peek(), end=" ")
        max_heap.pop()
    fast_print()
    
    # Hash Table Demo
    fast_print("\n8. Hash Table Demo:")
    hash_table = HashTable()
    hash_table.put("apple", 5)
    hash_table.put("banana", 3)
    hash_table.put("orange", 8)
    fast_print(f"Get apple: {hash_table.get('apple')}")
    fast_print(f"Contains banana: {hash_table.contains_key('banana')}")
    hash_table.remove("apple")
    fast_print(f"Contains apple after removal: {hash_table.contains_key('apple')}")
    fast_print(f"Keys: {hash_table.keys()}")
    fast_print(f"Values: {hash_table.values()}")
    fast_print(f"Size: {hash_table.get_size()}")
    
    # DSU Demo
    fast_print("\n9. Disjoint Set Union Demo:")
    dsu = DisjointSetUnion(5)
    dsu.union(0, 1)
    dsu.union(1, 2)
    dsu.union(3, 4)
    fast_print(f"Is 0 connected to 2: {dsu.connected(0, 2)}")
    fast_print(f"Is 0 connected to 3: {dsu.connected(0, 3)}")
    fast_print(f"Number of components: {dsu.get_components()}")
    
    # Trie Demo
    fast_print("\n10. Trie Demo:")
    trie = Trie()
    for word in ["hello", "world", "help", "helium"]:
        trie.insert(word)
    
    fast_print(f"Search 'hello': {trie.search('hello')}")
    fast_print(f"Search 'hell': {trie.search('hell')}")
    fast_print(f"Starts with 'hel': {trie.starts_with('hel')}")
    fast_print(f"All words: {trie.get_all_words()}")
    fast_print(f"Words with prefix 'hel': {trie.count_words_with_prefix('hel')}")
    trie.remove("hello")
    fast_print(f"Search 'hello' after removal: {trie.search('hello')}")
    
    # Segment Tree Demo
    fast_print("\n11. Segment Tree Demo:")
    arr = [1, 3, 2, 7, 9, 11]
    segment_tree = SegmentTree(arr)
    fast_print(f"Range query (1, 4): {segment_tree.query(1, 4)}")
    segment_tree.update(2, 5)
    fast_print(f"After updating index 2 to 5:")
    fast_print(f"Range query (1, 4): {segment_tree.query(1, 4)}")
    
    # Fenwick Tree Demo
    fast_print("\n12. Fenwick Tree Demo:")
    fenwick_arr = [1, 2, 3, 4, 5]
    fenwick_tree = FenwickTree(fenwick_arr)
    fast_print(f"Prefix sum up to index 3: {fenwick_tree.query(3)}")
    fast_print(f"Range sum (2, 4): {fenwick_tree.range_query(2, 4)}")
    fenwick_tree.update(3, 2)  # Add 2 to index 3
    fast_print(f"After updating index 3 by +2:")
    fast_print(f"Prefix sum up to index 3: {fenwick_tree.query(3)}")
    
    # LRU Cache Demo
    fast_print("\n13. LRU Cache Demo:")
    lru_cache = LRUCache(3)
    lru_cache.put(1, "one")
    lru_cache.put(2, "two")
    lru_cache.put(3, "three")
    fast_print(f"Get 1: {lru_cache.get(1)}")
    lru_cache.put(4, "four")  # This should evict key 2
    fast_print(f"Get 2: {lru_cache.get(2)}")  # Should return None
    fast_print(f"Get 3: {lru_cache.get(3)}")
    fast_print(f"Cache size: {lru_cache.size()}")
    
    # AVL Tree Demo
    fast_print("\n14. AVL Tree Demo:")
    avl_tree = AVLTree()
    for val in [10, 20, 30, 40, 50, 25]:
        avl_tree.insert(val)
    
    fast_print(f"Inorder traversal: {avl_tree.inorder_traversal()}")
    fast_print(f"Search 25: {avl_tree.search(25)}")
    fast_print(f"Search 35: {avl_tree.search(35)}")

if __name__ == "__main__":
    try:
        solve()
    except Exception as e:
        fast_print(f"Error: {e}")
        sys.exit(1)
