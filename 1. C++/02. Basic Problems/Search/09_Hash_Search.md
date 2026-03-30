# Hash Table Search

## Overview
Hash table search is a highly efficient search algorithm that uses hash functions to map keys to array indices, providing average O(1) time complexity for search operations.

## Algorithm Description

### Theory
Hash tables store key-value pairs in an array where each position is determined by a hash function. The hash function converts the key into an array index, allowing for direct access to the stored value.

### Mathematical Foundation
Hash function: h(key) → index
- Ideal hash function distributes keys uniformly
- Collision occurs when h(key1) = h(key2) for key1 ≠ key2
- Load factor α = number of elements / table size

### Algorithm Steps
1. Compute hash of target key
2. Access bucket at computed index
3. Handle collisions if necessary
4. Search within bucket for exact match

### Pseudocode
```
FUNCTION hashSearch(hashTable, key):
    index = hashFunction(key)
    
    // Handle collisions (chaining example)
    current = hashTable[index]
    WHILE current != null:
        IF current.key == key:
            RETURN current.value
        current = current.next
    
    RETURN null  // Not found
```

## Complexity Analysis

### Time Complexity
- **Average Case**: O(1) - Good hash function, low load factor
- **Worst Case**: O(n) - All elements hash to same bucket
- **Best Case**: O(1) - Direct access, no collisions

### Space Complexity
- **Space**: O(n) - For storing elements plus overhead

## Best Practices
- Choose appropriate hash function for data distribution
- Maintain load factor < 0.75 for performance
- Handle collisions efficiently
- Consider rehashing when table grows

## When to Use
- Fast lookups with keys
- Dynamic data with frequent insertions/deletions
- Caching mechanisms
- Database indexing
- Symbol tables in compilers

## Variants

### 1. Separate Chaining
Uses linked lists to handle collisions.

### 2. Open Addressing
Uses probing sequences to handle collisions.

### 3. Robin Hood Hashing
Optimizes probe sequence lengths.

### 4. Cuckoo Hashing
Uses multiple hash functions.

## Implementation Examples

### Example 1: Basic Hash Table with Separate Chaining
```cpp
#include <iostream>
#include <vector>
#include <list>
#include <string>

template<typename K, typename V>
class HashTable {
private:
    struct Node {
        K key;
        V value;
        Node(K k, V v) : key(k), value(v) {}
    };
    
    std::vector<std::list<Node>> table;
    int size;
    
    int hashFunction(const K& key) const {
        // Simple hash function for integers
        if constexpr (std::is_integral_v<K>) {
            return std::hash<K>{}(key) % size;
        }
        // For strings
        else if constexpr (std::is_same_v<K, std::string>) {
            unsigned long hash = 5381;
            for (char c : key) {
                hash = ((hash << 5) + hash) + c;
            }
            return hash % size;
        }
        return std::hash<K>{}(key) % size;
    }
    
public:
    HashTable(int initialSize = 10) : size(initialSize) {
        table.resize(size);
    }
    
    bool insert(const K& key, const V& value) {
        int index = hashFunction(key);
        
        // Check if key already exists
        for (auto& node : table[index]) {
            if (node.key == key) {
                node.value = value;
                return true;
            }
        }
        
        table[index].emplace_back(key, value);
        return true;
    }
    
    bool search(const K& key, V& value) const {
        int index = hashFunction(key);
        
        for (const auto& node : table[index]) {
            if (node.key == key) {
                value = node.value;
                return true;
            }
        }
        
        return false;
    }
    
    bool remove(const K& key) {
        int index = hashFunction(key);
        
        for (auto it = table[index].begin(); it != table[index].end(); ++it) {
            if (it->key == key) {
                table[index].erase(it);
                return true;
            }
        }
        
        return false;
    }
    
    void display() const {
        for (int i = 0; i < size; i++) {
            std::cout << "Bucket " << i << ": ";
            for (const auto& node : table[i]) {
                std::cout << "[" << node.key << ": " << node.value << "] ";
            }
            std::cout << std::endl;
        }
    }
};
```

### Example 2: Hash Table with Open Addressing (Linear Probing)
```cpp
#include <vector>
#include <optional>

template<typename K, typename V>
class HashTableOpenAddressing {
private:
    enum class State { EMPTY, OCCUPIED, DELETED };
    
    struct Entry {
        K key;
        V value;
        State state;
        
        Entry() : state(State::EMPTY) {}
        Entry(K k, V v) : key(k), value(v), state(State::OCCUPIED) {}
    };
    
    std::vector<Entry> table;
    int capacity;
    int count;
    
    int hashFunction(const K& key) const {
        return std::hash<K>{}(key) % capacity;
    }
    
    int probeFunction(const K& key, int attempt) const {
        return (hashFunction(key) + attempt) % capacity;
    }
    
    double getLoadFactor() const {
        return static_cast<double>(count) / capacity;
    }
    
    void rehash() {
        std::vector<Entry> oldTable = table;
        int oldCapacity = capacity;
        
        capacity *= 2;
        table.clear();
        table.resize(capacity);
        count = 0;
        
        for (const auto& entry : oldTable) {
            if (entry.state == State::OCCUPIED) {
                insert(entry.key, entry.value);
            }
        }
    }
    
public:
    HashTableOpenAddressing(int initialCapacity = 10) : capacity(initialCapacity), count(0) {
        table.resize(capacity);
    }
    
    bool insert(const K& key, const V& value) {
        if (getLoadFactor() > 0.7) {
            rehash();
        }
        
        int attempt = 0;
        int index;
        
        do {
            index = probeFunction(key, attempt);
            
            if (table[index].state == State::EMPTY || 
                table[index].state == State::DELETED) {
                table[index] = Entry(key, value);
                count++;
                return true;
            }
            
            if (table[index].state == State::OCCUPIED && 
                table[index].key == key) {
                table[index].value = value;
                return true;
            }
            
            attempt++;
        } while (attempt < capacity);
        
        return false;  // Table is full
    }
    
    std::optional<V> search(const K& key) const {
        int attempt = 0;
        int index;
        
        do {
            index = probeFunction(key, attempt);
            
            if (table[index].state == State::EMPTY) {
                return std::nullopt;
            }
            
            if (table[index].state == State::OCCUPIED && 
                table[index].key == key) {
                return table[index].value;
            }
            
            attempt++;
        } while (attempt < capacity);
        
        return std::nullopt;
    }
    
    bool remove(const K& key) {
        int attempt = 0;
        int index;
        
        do {
            index = probeFunction(key, attempt);
            
            if (table[index].state == State::EMPTY) {
                return false;
            }
            
            if (table[index].state == State::OCCUPIED && 
                table[index].key == key) {
                table[index].state = State::DELETED;
                count--;
                return true;
            }
            
            attempt++;
        } while (attempt < capacity);
        
        return false;
    }
};
```

### Example 3: Specialized Hash Table for Strings
```cpp
#include <string>
#include <vector>

class StringHashTable {
private:
    struct Node {
        std::string key;
        int value;
        Node* next;
        
        Node(const std::string& k, int v) : key(k), value(v), next(nullptr) {}
    };
    
    std::vector<Node*> table;
    int capacity;
    
    // DJB2 hash function for strings
    unsigned long hashString(const std::string& str) const {
        unsigned long hash = 5381;
        for (char c : str) {
            hash = ((hash << 5) + hash) + c;
        }
        return hash % capacity;
    }
    
public:
    StringHashTable(int cap = 100) : capacity(cap) {
        table.resize(capacity, nullptr);
    }
    
    ~StringHashTable() {
        for (auto bucket : table) {
            while (bucket) {
                Node* temp = bucket;
                bucket = bucket->next;
                delete temp;
            }
        }
    }
    
    bool insert(const std::string& key, int value) {
        unsigned long index = hashString(key);
        Node*& bucket = table[index];
        
        // Check if key already exists
        for (Node* curr = bucket; curr; curr = curr->next) {
            if (curr->key == key) {
                curr->value = value;
                return true;
            }
        }
        
        // Insert at beginning
        Node* newNode = new Node(key, value);
        newNode->next = bucket;
        bucket = newNode;
        return true;
    }
    
    bool search(const std::string& key, int& value) const {
        unsigned long index = hashString(key);
        
        for (Node* curr = table[index]; curr; curr = curr->next) {
            if (curr->key == key) {
                value = curr->value;
                return true;
            }
        }
        
        return false;
    }
    
    bool remove(const std::string& key) {
        unsigned long index = hashString(key);
        Node*& bucket = table[index];
        
        if (!bucket) return false;
        
        if (bucket->key == key) {
            Node* temp = bucket;
            bucket = bucket->next;
            delete temp;
            return true;
        }
        
        for (Node* curr = bucket; curr->next; curr = curr->next) {
            if (curr->next->key == key) {
                Node* temp = curr->next;
                curr->next = temp->next;
                delete temp;
                return true;
            }
        }
        
        return false;
    }
};
```

## Testing and Verification

### Test Cases
1. **Basic operations**: Insert, search, remove
2. **Collision handling**: Multiple keys with same hash
3. **Load factor testing**: Performance at different load factors
4. **Edge cases**: Empty table, single element
5. **Rehashing**: Automatic table expansion

### Performance Tests
1. **Search performance**: Average case O(1) verification
2. **Collision scenarios**: Worst-case O(n) testing
3. **Memory usage**: Space complexity verification
4. **Hash function quality**: Distribution analysis

## Common Pitfalls
1. Poor hash function selection
2. Not handling collisions properly
3. Ignoring load factor management
4. Memory leaks in dynamic implementations
5. Thread safety issues

## Optimization Tips
1. Choose appropriate initial capacity
2. Implement good hash functions
3. Use efficient collision resolution
4. Consider cache performance
5. Implement automatic rehashing

## Real-World Applications
- Database indexes
- Symbol tables in compilers
- Caching systems
- Associative arrays
- Network routing tables
- Memory management

## Advanced Topics

### Collision Resolution Strategies
- Linear probing
- Quadratic probing
- Double hashing
- Cuckoo hashing

### Hash Function Design
- Universal hashing
- Perfect hashing
- Cryptographic hashing
- Rolling hashes

### Concurrent Hash Tables
- Lock-free implementations
- Read-write locks
- Sharding strategies

## Related Data Structures
- Balanced Trees
- Skip Lists
- Bloom Filters
- Tries

## References
- The Art of Computer Programming (Donald Knuth)
- Introduction to Algorithms (CLRS)
- Algorithm Design Manual

---

*This implementation provides a comprehensive guide to hash table search with various collision resolution strategies and optimization techniques.*
