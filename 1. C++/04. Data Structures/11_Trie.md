# Trie (Prefix Tree) in C++

## 📖 Overview

A **Trie** (pronounced *"try"*, from re**trie**val) is an efficient tree-like data structure used for storing and searching dynamic collections of strings over a specific alphabet.

Unlike a Binary Search Tree, no node in a Trie stores the full key it represents. Instead, a node's position in the tree defines the key with which it is associated. All descendants of a node share a common prefix.

---

## 🎯 Key Characteristics & Complexity

| Operation | Trie | Hash Table (`std::unordered_set`) | Balanced BST (`std::set`) |
|:---|:---|:---|:---|
| **Insert** | $O(L)$ | $O(L)$ average | $O(L \log N)$ |
| **Search (Exact)** | $O(L)$ | $O(L)$ average, $O(L \cdot N)$ worst | $O(L \log N)$ |
| **Prefix Search (`startsWith`)** | $O(L)$ | $O(N \cdot L)$ (must check all keys) | $O(L \log N)$ |
| **Memory Overhead** | $O(N \cdot L \cdot |\Sigma|)$ | $O(N \cdot L)$ | $O(N \cdot L)$ |
| **Lexicographical Ordering** | Natural (in-order DFS) | No | Yes |

*Where $L$ is the length of the string, $N$ is the number of words, and $|\Sigma|$ is the alphabet size (e.g., 26).*

---

## 1. Complete Trie Implementation

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <memory>
#include <stdexcept>

class Trie {
private:
    struct TrieNode {
        TrieNode* children[26];
        bool isEndOfWord;
        int countPrefix; // Number of words sharing this prefix
        int countEnd;    // Number of duplicate words ending here

        TrieNode() : isEndOfWord(false), countPrefix(0), countEnd(0) {
            for (int i = 0; i < 26; ++i) {
                children[i] = nullptr;
            }
        }

        ~TrieNode() {
            for (int i = 0; i < 26; ++i) {
                delete children[i];
            }
        }
    };

    TrieNode* root_;

    // Recursive helper for deletion that frees unused nodes
    bool removeHelper(TrieNode* curr, const std::string& word, int depth) {
        if (curr == nullptr) return false;

        if (depth == static_cast<int>(word.size())) {
            if (!curr->isEndOfWord) return false; // Word does not exist

            --curr->countEnd;
            --curr->countPrefix;
            if (curr->countEnd == 0) {
                curr->isEndOfWord = false;
            }
            return true;
        }

        int index = word[depth] - 'a';
        if (curr->children[index] == nullptr) return false;

        bool removed = removeHelper(curr->children[index], word, depth + 1);
        if (removed) {
            --curr->countPrefix;
            // If child has no words passing through it, delete it
            if (curr->children[index]->countPrefix == 0) {
                delete curr->children[index];
                curr->children[index] = nullptr;
            }
        }
        return removed;
    }

    // DFS helper to collect autocomplete suggestions
    void collect(TrieNode* curr, std::string& prefix, std::vector<std::string>& results) const {
        if (curr == nullptr) return;

        if (curr->isEndOfWord) {
            results.push_back(prefix);
        }

        for (int i = 0; i < 26; ++i) {
            if (curr->children[i] != nullptr) {
                prefix.push_back('a' + i);
                collect(curr->children[i], prefix, results);
                prefix.pop_back();
            }
        }
    }

public:
    Trie() : root_(new TrieNode()) {}

    ~Trie() {
        delete root_;
    }

    // Insert a word into the Trie: O(L)
    void insert(const std::string& word) {
        TrieNode* curr = root_;
        ++curr->countPrefix;

        for (char c : word) {
            int index = c - 'a';
            if (curr->children[index] == nullptr) {
                curr->children[index] = new TrieNode();
            }
            curr = curr->children[index];
            ++curr->countPrefix;
        }
        curr->isEndOfWord = true;
        ++curr->countEnd;
    }

    // Search exact word: O(L)
    bool search(const std::string& word) const {
        TrieNode* curr = root_;
        for (char c : word) {
            int index = c - 'a';
            if (curr->children[index] == nullptr) return false;
            curr = curr->children[index];
        }
        return curr != nullptr && curr->isEndOfWord;
    }

    // Check if any word starts with prefix: O(L)
    bool startsWith(const std::string& prefix) const {
        TrieNode* curr = root_;
        for (char c : prefix) {
            int index = c - 'a';
            if (curr->children[index] == nullptr) return false;
            curr = curr->children[index];
        }
        return curr != nullptr;
    }

    // Count words starting with prefix: O(L)
    int countWordsStartingWith(const std::string& prefix) const {
        TrieNode* curr = root_;
        for (char c : prefix) {
            int index = c - 'a';
            if (curr->children[index] == nullptr) return 0;
            curr = curr->children[index];
        }
        return curr->countPrefix;
    }

    // Delete a word from the Trie: O(L)
    bool remove(const std::string& word) {
        return removeHelper(root_, word, 0);
    }

    // Autocomplete: Return all words matching prefix
    std::vector<std::string> autocomplete(const std::string& prefix) const {
        std::vector<std::string> results;
        TrieNode* curr = root_;

        for (char c : prefix) {
            int index = c - 'a';
            if (curr->children[index] == nullptr) return results;
            curr = curr->children[index];
        }

        std::string currentPrefix = prefix;
        collect(curr, currentPrefix, results);
        return results;
    }
};
```

---

## 2. Binary / Bitwise Trie (Maximum XOR Pair Problem)

### Problem
Given an array of integers $A$, find two elements $A[i]$ and $A[j]$ such that $A[i] \oplus A[j]$ is maximized.
- **Naive approach**: $O(N^2)$ checks.
- **Bitwise Trie approach**: Insert all binary representations (32 bits) into a 2-child Trie. For each number, query the branch with the inverted bit to greedily maximize the XOR. Total time: strictly **$O(32 \cdot N) = O(N)$**.

```cpp
class BinaryTrie {
private:
    struct Node {
        Node* children[2] = {nullptr, nullptr};
        ~Node() {
            delete children[0];
            delete children[1];
        }
    };

    Node* root_;

public:
    BinaryTrie() : root_(new Node()) {}
    ~BinaryTrie() { delete root_; }

    // Insert 32-bit integer into Bitwise Trie
    void insert(int num) {
        Node* curr = root_;
        for (int i = 31; i >= 0; --i) {
            int bit = (num >> i) & 1;
            if (curr->children[bit] == nullptr) {
                curr->children[bit] = new Node();
            }
            curr = curr->children[bit];
        }
    }

    // Query maximum XOR achievable with num
    int queryMaxXOR(int num) const {
        Node* curr = root_;
        int maxXor = 0;

        for (int i = 31; i >= 0; --i) {
            int bit = (num >> i) & 1;
            int oppositeBit = 1 - bit;

            // Greedily choose the opposite bit if present
            if (curr->children[oppositeBit] != nullptr) {
                maxXor |= (1 << i);
                curr = curr->children[oppositeBit];
            } else {
                curr = curr->children[bit];
            }
        }
        return maxXor;
    }

    // Solve Maximum XOR of Two Numbers in Array: O(N)
    static int findMaximumXOR(const std::vector<int>& nums) {
        BinaryTrie trie;
        for (int x : nums) {
            trie.insert(x);
        }

        int maxResult = 0;
        for (int x : nums) {
            maxResult = std::max(maxResult, trie.queryMaxXOR(x));
        }
        return maxResult;
    }
};
```

---

## 💻 Driver & Comprehensive Verification

```cpp
#include <iostream>
#include <cassert>

int main() {
    std::cout << "========== 1. STRING TRIE ==========\n";
    Trie trie;
    trie.insert("apple");
    trie.insert("app");
    trie.insert("application");
    trie.insert("aptitude");
    trie.insert("bat");

    assert(trie.search("apple") == true);
    assert(trie.search("app") == true);
    assert(trie.search("appl") == false);
    assert(trie.startsWith("app") == true);
    assert(trie.countWordsStartingWith("app") == 3); // apple, app, application

    std::cout << "Autocomplete for \"app\":\n";
    auto suggestions = trie.autocomplete("app");
    for (const auto& word : suggestions) {
        std::cout << "  - " << word << "\n";
    }
    assert(suggestions.size() == 3);

    trie.remove("app");
    assert(trie.search("app") == false);
    assert(trie.search("apple") == true); // Prefix deletion preserves descendants
    assert(trie.countWordsStartingWith("app") == 2);

    std::cout << "\n========== 2. BINARY TRIE (MAX XOR) ==========\n";
    std::vector<int> nums = {3, 10, 5, 25, 2, 8};
    // 5 (00101) ^ 25 (11001) = 28 (11100)
    int maxXor = BinaryTrie::findMaximumXOR(nums);
    std::cout << "Maximum XOR Pair in {3, 10, 5, 25, 2, 8}: " << maxXor << "\n";
    assert(maxXor == 28);

    std::cout << "\n✅ All Trie implementations verified successfully!\n";
    return 0;
}
```

---

## Next Step

- Go to [12_Disjoint_Set_Union.md](12_Disjoint_Set_Union.md) to understand Disjoint Set Union (Union-Find).
