# 12_Word_Search.md

## Word Search

### Definition

Given a 2D grid of characters and a word, determine if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically adjacent). The same letter cell may not be used more than once.

### Problem Statement

Input:
- A 2D board of characters (m × n)
- A target word

Output:
- True if the word exists in the board, false otherwise

### Visual Example

```
Board:
A B C E
S F C S
A D E E

Word = "ABCCED"

Path: (0,0)A → (0,1)B → (0,2)C → (1,2)C → (2,2)E → (2,1)D
Returns: True
```

### Backtracking Approach

```
Step 1: Search for the first character in the board
Step 2: For each cell matching first character, start DFS
Step 3: At each step, check if current cell matches current character
Step 4: Mark current cell as visited (temporarily)
Step 5: Try all 4 directions (up, down, left, right)
Step 6: If any direction leads to completion, return true
Step 7: Unmark the cell (backtrack) and try other starting positions
```

### Implementation

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool dfs(vector<vector<char>>& board, string& word, int i, int j, int index) {
    // Base case: all characters matched
    if (index == word.length()) {
        return true;
    }
    
    // Check bounds and character match
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || 
        board[i][j] != word[index]) {
        return false;
    }
    
    // Mark as visited
    char temp = board[i][j];
    board[i][j] = '#';
    
    // Try all four directions
    bool found = dfs(board, word, i + 1, j, index + 1) ||
                 dfs(board, word, i - 1, j, index + 1) ||
                 dfs(board, word, i, j + 1, index + 1) ||
                 dfs(board, word, i, j - 1, index + 1);
    
    // Backtrack: restore original character
    board[i][j] = temp;
    
    return found;
}

bool exist(vector<vector<char>>& board, string word) {
    if (board.empty() || board[0].empty() || word.empty()) {
        return false;
    }
    
    int m = board.size();
    int n = board[0].size();
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == word[0] && dfs(board, word, i, j, 0)) {
                return true;
            }
        }
    }
    
    return false;
}

int main() {
    vector<vector<char>> board = {
        {'A', 'B', 'C', 'E'},
        {'S', 'F', 'C', 'S'},
        {'A', 'D', 'E', 'E'}
    };
    string word = "ABCCED";
    
    bool result = exist(board, word);
    cout << "Word exists: " << (result ? "Yes" : "No") << endl;
    
    return 0;
}
```

### Example Walkthrough

```
Board:
(0,0)A (0,1)B (0,2)C (0,3)E
(1,0)S (1,1)F (1,2)C (1,3)S
(2,0)A (2,1)D (2,2)E (2,3)E

Word: "ABCCED"

Start at (0,0) matching 'A'
    Mark (0,0) as visited
    index=1, need 'B'
    Try right (0,1): 'B' matches
        Mark (0,1) visited
        index=2, need 'C'
        Try right (0,2): 'C' matches
            Mark (0,2) visited
            index=3, need 'C'
            Try right (0,3): 'E' no match
            Try down (1,2): 'C' matches
                Mark (1,2) visited
                index=4, need 'E'
                Try right (1,3): 'S' no
                Try down (2,2): 'E' matches
                    Mark (2,2) visited
                    index=5, need 'D'
                    Try left (2,1): 'D' matches
                        index=6, word found! Return true
```

### Optimization: Early Pruning

```cpp
bool existOptimized(vector<vector<char>>& board, string word) {
    // Count characters in board and word for early pruning
    vector<int> boardCount(26, 0);
    vector<int> wordCount(26, 0);
    
    for (auto& row : board) {
        for (char c : row) {
            boardCount[c - 'A']++;
        }
    }
    
    for (char c : word) {
        wordCount[c - 'A']++;
        if (wordCount[c - 'A'] > boardCount[c - 'A']) {
            return false;
        }
    }
    
    // Reverse word if first character appears less than last character
    if (boardCount[word[0] - 'A'] > boardCount[word.back() - 'A']) {
        reverse(word.begin(), word.end());
    }
    
    // Rest of the algorithm...
}
```

### Time Complexity

| Complexity | Value |
|------------|-------|
| Time | O(m × n × 3^L) where L is word length |
| Space | O(L) for recursion stack |

### Variations

#### 1. Word Search II (Multiple Words)

Find all words from a dictionary that exist in the board. Use Trie for efficiency.

```cpp
struct TrieNode {
    TrieNode* children[26];
    string word;
    TrieNode() : word("") {
        for (int i = 0; i < 26; i++) children[i] = nullptr;
    }
};

void insertWord(TrieNode* root, string& word) {
    TrieNode* node = root;
    for (char c : word) {
        int idx = c - 'a';
        if (!node->children[idx]) {
            node->children[idx] = new TrieNode();
        }
        node = node->children[idx];
    }
    node->word = word;
}

void dfs(vector<vector<char>>& board, int i, int j, TrieNode* node, vector<string>& result) {
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || 
        board[i][j] == '#') {
        return;
    }
    
    char c = board[i][j];
    int idx = c - 'a';
    
    if (!node->children[idx]) return;
    
    node = node->children[idx];
    
    if (node->word != "") {
        result.push_back(node->word);
        node->word = "";  // avoid duplicates
    }
    
    board[i][j] = '#';
    
    dfs(board, i+1, j, node, result);
    dfs(board, i-1, j, node, result);
    dfs(board, i, j+1, node, result);
    dfs(board, i, j-1, node, result);
    
    board[i][j] = c;
}
```

#### 2. Word Search with Diagonal Moves

Allow diagonal moves in addition to up/down/left/right.

```cpp
// Add 4 diagonal directions
int dirs[8][2] = {{-1,0},{1,0},{0,-1},{0,1},{-1,-1},{-1,1},{1,-1},{1,1}};
```

#### 3. Word Search with Path Printing

```cpp
vector<pair<int,int>> path;

bool dfsWithPath(vector<vector<char>>& board, string& word, int i, int j, int index) {
    if (index == word.length()) {
        // Print path
        for (auto& p : path) {
            cout << "(" << p.first << "," << p.second << ") ";
        }
        cout << endl;
        return true;
    }
    // ... rest of DFS
}
```

### Practice Problems

1. Determine if a word exists in a grid
2. Find all words from a dictionary in a grid (Word Search II)
3. Count number of occurrences of a word in a grid
4. Find the longest word in a grid from a dictionary
5. Word search with diagonal moves allowed