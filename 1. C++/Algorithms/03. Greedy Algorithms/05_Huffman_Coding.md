# 05_Huffman_Coding.md

## Huffman Coding

### Definition

Huffman coding is a lossless data compression algorithm that assigns variable-length codes to characters based on their frequencies. Characters with higher frequency get shorter codes.

### Problem Statement

Input:
- A set of characters and their frequencies

Output:
- Prefix-free binary codes for each character
- Minimum total bits required to encode the text

### Key Property

**Prefix-free:** No code is a prefix of another code. This ensures unambiguous decoding.

### Greedy Strategy

**Strategy:** Repeatedly merge the two characters (or nodes) with the smallest frequencies.

**Why this works:** Placing lower frequency characters deeper in the tree (longer codes) minimizes the weighted path length.

### Algorithm

```
Step 1: Create a leaf node for each character with its frequency
Step 2: Insert all nodes into a min-heap (priority queue)
Step 3: While heap has more than one node:
        Remove two nodes with smallest frequencies
        Create a new internal node with frequency = sum of the two
        Make the two nodes children of the new node
        Insert the new node back into the heap
Step 4: The remaining node is the root of the Huffman tree
Step 5: Traverse the tree to assign codes (0 for left, 1 for right)
```

### Implementation

```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <map>
using namespace std;

struct Node {
    char ch;
    int freq;
    Node* left;
    Node* right;
    
    Node(char c, int f) : ch(c), freq(f), left(nullptr), right(nullptr) {}
    Node(int f, Node* l, Node* r) : ch('\0'), freq(f), left(l), right(r) {}
};

struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq;
    }
};

void generateCodes(Node* root, string code, map<char, string>& codes) {
    if (!root) return;
    
    if (root->ch != '\0') {
        codes[root->ch] = code;
    }
    
    generateCodes(root->left, code + "0", codes);
    generateCodes(root->right, code + "1", codes);
}

void huffmanCoding(map<char, int>& frequencies) {
    priority_queue<Node*, vector<Node*>, Compare> pq;
    
    // Create leaf nodes for each character
    for (auto& pair : frequencies) {
        pq.push(new Node(pair.first, pair.second));
    }
    
    // Build Huffman tree
    while (pq.size() > 1) {
        Node* left = pq.top(); pq.pop();
        Node* right = pq.top(); pq.pop();
        
        Node* parent = new Node(left->freq + right->freq, left, right);
        pq.push(parent);
    }
    
    // Generate codes
    Node* root = pq.top();
    map<char, string> codes;
    generateCodes(root, "", codes);
    
    // Print codes
    cout << "Huffman Codes:" << endl;
    for (auto& pair : codes) {
        cout << pair.first << " : " << pair.second << endl;
    }
    
    // Calculate total bits
    int totalBits = 0;
    for (auto& pair : frequencies) {
        totalBits += pair.second * codes[pair.first].length();
    }
    cout << "Total bits required: " << totalBits << endl;
}

int main() {
    map<char, int> frequencies = {
        {'a', 5},
        {'b', 9},
        {'c', 12},
        {'d', 13},
        {'e', 16},
        {'f', 45}
    };
    
    huffmanCoding(frequencies);
    
    return 0;
}
```

### Example Walkthrough

```
Frequencies: a=5, b=9, c=12, d=13, e=16, f=45

Step 1: Initial heap (min-heap by frequency)
[5:a, 9:b, 12:c, 13:d, 16:e, 45:f]

Step 2: Merge a(5) and b(9) → new node(14)
Heap: [12:c, 13:d, 14:(a,b), 16:e, 45:f]

Step 3: Merge c(12) and d(13) → new node(25)
Heap: [14:(a,b), 16:e, 25:(c,d), 45:f]

Step 4: Merge (a,b)(14) and e(16) → new node(30)
Heap: [25:(c,d), 30:((a,b),e), 45:f]

Step 5: Merge (c,d)(25) and ((a,b),e)(30) → new node(55)
Heap: [45:f, 55:(((c,d),((a,b),e)))]

Step 6: Merge f(45) and (55) → new node(100)
Heap: [100: root]

Final tree structure:

                    root(100)
                   /        \
                 f(45)       (55)
                            /    \
                         (25)     (30)
                        /    \   /    \
                      c(12) d(13) (14) e(16)
                                 /    \
                              a(5)   b(9)

Codes:
f: 0
c: 100
d: 101
a: 1100
b: 1101
e: 111

Total bits = 45*1 + 12*3 + 13*3 + 5*4 + 9*4 + 16*3 = 45 + 36 + 39 + 20 + 36 + 48 = 224
```

### Without Tree Reconstruction (Using Priority Queue Only)

```cpp
int huffmanBits(vector<int>& frequencies) {
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for (int freq : frequencies) {
        pq.push(freq);
    }
    
    int totalBits = 0;
    
    while (pq.size() > 1) {
        int first = pq.top(); pq.pop();
        int second = pq.top(); pq.pop();
        
        int sum = first + second;
        totalBits += sum;
        pq.push(sum);
    }
    
    return totalBits;
}
```

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| Building heap | O(n) |
| Each merge (n-1 merges) | O(log n) |
| Total | O(n log n) |

### Space Complexity

O(n) for storing the tree

### Huffman Coding Properties

| Property | Description |
|----------|-------------|
| Prefix-free | No code is prefix of another |
| Optimal | Minimum weighted path length |
| Variable length | Common characters have shorter codes |
| Lossless | Original data can be perfectly reconstructed |

### Variations

#### 1. Adaptive Huffman Coding

Tree is updated dynamically as data is read (used in streaming).

#### 2. Canonical Huffman Coding

Codes are assigned in a specific order for efficient storage.

#### 3. n-ary Huffman Coding

Merge n smallest nodes at a time instead of 2.

#### 4. Huffman Coding with Equal Frequencies

When all frequencies are equal, all codes have same length.

### Real-World Applications

| Application | Description |
|-------------|-------------|
| ZIP compression | Combines Huffman with LZ77 |
| JPEG images | Uses Huffman after DCT |
| MP3 audio | Part of compression pipeline |
| PKZIP | Huffman coding variant |
| Fax machines | Modified Huffman coding |

### Proof of Optimality

**Greedy Choice Property:** There exists an optimal tree where the two nodes with smallest frequencies are siblings at the deepest level.

**Proof by Contradiction:**
- Let x and y be the two smallest frequency nodes
- Assume they are not siblings in an optimal tree
- Swap them with the deepest siblings
- The total cost does not increase because x and y have smallest frequencies
- Therefore, there exists an optimal tree where they are siblings

**Optimal Substructure:** After merging x and y into a new node with frequency x+y, the problem reduces to building a Huffman tree for n-1 nodes.
---

## Next Step

- Go to [06_Coin_Change_Greedy.md](06_Coin_Change_Greedy.md) to continue with Coin Change Greedy.
