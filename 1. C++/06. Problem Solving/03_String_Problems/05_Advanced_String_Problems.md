# Advanced String Algorithms in C++

## 📖 Overview

Advanced string algorithms address complex queries across massive texts: searching thousands of patterns simultaneously, finding longest palindromic substrings in strictly linear time, indexing all substrings of a text, and performing $O(1)$ substring comparisons without collisions.

This guide provides complete, production-grade C++ implementations, mathematical explanations, and complexity proofs for:
1. **Manacher’s Algorithm** (Linear-time $O(N)$ Longest Palindromic Substring)
2. **Aho-Corasick Automaton** (Simultaneous Multi-Pattern Search in $O(N + M + \text{matches})$)
3. **Suffix Array & LCP Array (Kasai’s Algorithm)** ($O(N \log^2 N)$ construction and $O(N)$ LCP)
4. **Double Polynomial String Hashing** ($O(1)$ substring equality queries with collision immunity)

---

## 1. Manacher's Algorithm (Linear-Time Palindromic Substring)

### The Problem
Given a string $S$ of length $N$, find its longest palindromic substring. Standard expansion around centers takes $O(N^2)$ worst-case (e.g., `"aaaaa"`). Dynamic programming also takes $O(N^2)$ time and $O(N^2)$ space. Manacher's algorithm solves this in strictly **$O(N)$ time and $O(N)$ space**.

### Key Insights
1. **Handling Odd and Even Lengths Uniformly**: Insert a delimiter character `#` between all characters, and add start/end boundary guards `^` and `$`.
   - Original: `"aba"` $\rightarrow$ Transformed: `"^#a#b#a#$"` (odd length 3 $\rightarrow$ length 7)
   - Original: `"abba"` $\rightarrow$ Transformed: `"^#a#b#b#a#$"` (even length 4 $\rightarrow$ length 9)
   Now every palindrome in the transformed string has an odd length.
2. **Symmetry Utilization**: Maintain the center $C$ and right boundary $R$ of the palindrome that extends furthest to the right. For a current index $i$:
   - Let mirror $i' = 2C - i$.
   - If $i < R$, the palindrome radius $P[i]$ is at least $\min(R - i, P[i'])$.
   - Expand beyond this lower bound only when necessary.

### Implementation
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class Manacher {
public:
    // Returns the longest palindromic substring in O(N)
    static std::string longestPalindrome(const std::string& s) {
        if (s.empty()) return "";

        // Transform: "aba" -> "^#a#b#a#$"
        std::string t = "^";
        for (char c : s) {
            t += '#';
            t += c;
        }
        t += "#$";

        int n = static_cast<int>(t.size());
        std::vector<int> p(n, 0); // Palindrome radius array
        int c = 0; // Current center
        int r = 0; // Current right boundary

        int maxLen = 0;
        int centerIndex = 0;

        for (int i = 1; i < n - 1; ++i) {
            int iMirror = 2 * c - i; // Mirror of i around center c

            if (r > i) {
                p[i] = std::min(r - i, p[iMirror]);
            } else {
                p[i] = 0;
            }

            // Attempt to expand palindrome centered at i
            while (t[i + 1 + p[i]] == t[i - 1 - p[i]]) {
                ++p[i];
            }

            // Update center and right boundary if expanded past r
            if (i + p[i] > r) {
                c = i;
                r = i + p[i];
            }

            // Track maximum palindrome
            if (p[i] > maxLen) {
                maxLen = p[i];
                centerIndex = i;
            }
        }

        // Map back to original string indices
        int start = (centerIndex - maxLen) / 2;
        return s.substr(start, maxLen);
    }
};
```

---

## 2. Aho-Corasick Automaton (Multi-Pattern String Matching)

### The Problem
Given a text $T$ of length $N$ and a dictionary of $K$ patterns $\{P_1, P_2, \dots, P_K\}$ with total length $M$, find all occurrences of all patterns in $T$. Running KMP for each pattern takes $O(K \cdot N)$. Aho-Corasick solves this in **$O(N + M + \text{occurrences})$**.

### Architecture
1. **Trie Construction**: Insert all patterns into a standard Trie.
2. **Failure Links (BFS)**: Similar to KMP's LPS array, each node $u$ has a failure link pointing to the node representing the longest proper suffix of the string ending at $u$.
3. **Dictionary/Output Links**: Points to the nearest ancestor with an end-of-word flag to collect all matching patterns ending at the current state in $O(1)$ amortized time.

### Implementation
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <map>

class AhoCorasick {
private:
    struct Node {
        std::map<char, int> children;
        int fail = 0;
        int dictLink = 0;
        std::vector<int> patternIndices; // Indices of patterns ending here
    };

    std::vector<Node> trie;
    std::vector<std::string> patterns;

public:
    AhoCorasick() {
        trie.emplace_back(); // Root node at index 0
    }

    void insert(const std::string& pattern, int patternIdx) {
        int curr = 0;
        for (char c : pattern) {
            if (!trie[curr].children.count(c)) {
                trie[curr].children[c] = static_cast<int>(trie.size());
                trie.emplace_back();
            }
            curr = trie[curr].children[c];
        }
        trie[curr].patternIndices.push_back(patternIdx);
    }

    void build() {
        std::queue<int> q;

        // Initialize root's immediate children
        for (const auto& entry : trie[0].children) {
            int nextNode = entry.second;
            trie[nextNode].fail = 0;
            q.push(nextNode);
        }

        // BFS to build failure and dictionary links
        while (!q.empty()) {
            int curr = q.front();
            q.pop();

            for (const auto& entry : trie[curr].children) {
                char ch = entry.first;
                int nextNode = entry.second;
                int f = trie[curr].fail;
                while (f > 0 && !trie[f].children.count(ch)) {
                    f = trie[f].fail;
                }
                if (trie[f].children.count(ch) && trie[f].children[ch] != nextNode) {
                    trie[nextNode].fail = trie[f].children[ch];
                } else {
                    trie[nextNode].fail = 0;
                }

                // Dictionary link: shortcut to nearest pattern match
                int failTarget = trie[nextNode].fail;
                if (!trie[failTarget].patternIndices.empty()) {
                    trie[nextNode].dictLink = failTarget;
                } else {
                    trie[nextNode].dictLink = trie[failTarget].dictLink;
                }

                q.push(nextNode);
            }
        }
    }

    // Returns map of pattern index -> list of end positions in text
    std::map<int, std::vector<int>> search(const std::string& text) {
        std::map<int, std::vector<int>> matches;
        int curr = 0;

        for (int i = 0; i < static_cast<int>(text.size()); ++i) {
            char c = text[i];
            while (curr > 0 && !trie[curr].children.count(c)) {
                curr = trie[curr].fail;
            }
            if (trie[curr].children.count(c)) {
                curr = trie[curr].children[c];
            } else {
                curr = 0;
            }

            // Traverse matches at current node and via dictionary links
            int matchNode = curr;
            while (matchNode > 0) {
                for (int pIdx : trie[matchNode].patternIndices) {
                    matches[pIdx].push_back(i);
                }
                matchNode = trie[matchNode].dictLink;
            }
        }
        return matches;
    }
};
```

---

## 3. Suffix Array & LCP Array (Kasai's Algorithm)

### Key Concepts
- **Suffix Array ($SA$)**: An array of integers giving the starting indices of the suffixes of a string, sorted in lexicographical order.
- **LCP Array**: $\text{LCP}[i]$ stores the length of the Longest Common Prefix between $SA[i]$ and $SA[i-1]$.

### Construction Algorithm (Prefix Doubling)
1. Sort suffixes by their first $2^0 = 1$ character.
2. In iteration $k$, sort suffixes using a rank pair $(R[i], R[i + 2^{k-1}])$.
3. Terminate when $2^k \ge N$. Time complexity: $O(N \log^2 N)$ (or $O(N \log N)$ with radix sort).

### Kasai's Algorithm for LCP in $O(N)$
If suffix $i$ and its preceding suffix in $SA$ have an LCP of $h$, then suffix $i+1$ and its preceding suffix in $SA$ must have an LCP of at least $h - 1$. This allows computing the entire LCP array in strictly $O(N)$ time.

### Complete Implementation
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class SuffixArray {
public:
    // Build Suffix Array using prefix doubling in O(N log^2 N)
    static std::vector<int> buildSA(const std::string& s) {
        int n = static_cast<int>(s.size());
        std::vector<int> sa(n);
        std::vector<int> rank(n);

        for (int i = 0; i < n; ++i) {
            sa[i] = i;
            rank[i] = static_cast<unsigned char>(s[i]);
        }

        for (int k = 1; k < n; k *= 2) {
            auto cmp = [&](int i, int j) {
                if (rank[i] != rank[j]) return rank[i] < rank[j];
                int ri = (i + k < n) ? rank[i + k] : -1;
                int rj = (j + k < n) ? rank[j + k] : -1;
                return ri < rj;
            };

            std::sort(sa.begin(), sa.end(), cmp);

            std::vector<int> tempRank(n, 0);
            for (int i = 1; i < n; ++i) {
                tempRank[sa[i]] = tempRank[sa[i - 1]] + (cmp(sa[i - 1], sa[i]) ? 1 : 0);
            }
            rank = tempRank;
            if (rank[sa[n - 1]] == n - 1) break; // All ranks unique
        }
        return sa;
    }

    // Build LCP Array using Kasai's Algorithm in O(N)
    static std::vector<int> buildLCP(const std::string& s, const std::vector<int>& sa) {
        int n = static_cast<int>(s.size());
        std::vector<int> rank(n, 0);
        for (int i = 0; i < n; ++i) {
            rank[sa[i]] = i;
        }

        std::vector<int> lcp(n, 0);
        int h = 0; // Current LCP length

        for (int i = 0; i < n; ++i) {
            if (rank[i] > 0) {
                int j = sa[rank[i] - 1]; // Preceding suffix in SA
                while (i + h < n && j + h < n && s[i + h] == s[j + h]) {
                    ++h;
                }
                lcp[rank[i]] = h;
                if (h > 0) --h;
            }
        }
        return lcp;
    }

    // Classic Application: Count Distinct Substrings in O(N log^2 N)
    // Formula: Total substrings - duplicates = N*(N+1)/2 - sum(LCP)
    static long long countDistinctSubstrings(const std::string& s) {
        int n = static_cast<int>(s.size());
        auto sa = buildSA(s);
        auto lcp = buildLCP(s, sa);

        long long total = static_cast<long long>(n) * (n + 1) / 2;
        for (int x : lcp) {
            total -= x;
        }
        return total;
    }
};
```

---

## 4. Double Polynomial String Hashing

### The Problem
Comparing two strings of length $L$ takes $O(L)$ time. With polynomial rolling hashing, we can precompute prefix hashes in $O(N)$ and compare any two substrings $S[L_1 \dots R_1]$ and $S[L_2 \dots R_2]$ in **$O(1)$ time**.
Using a single 32-bit modulo invites hash collision attacks (Birthday Paradox guarantees collisions around $10^5$ queries). **Double Hashing** with two distinct large prime moduli reduces the collision probability to less than $10^{-18}$.

### Implementation
```cpp
#include <iostream>
#include <vector>
#include <string>

class DoubleHash {
private:
    static constexpr long long B1 = 313, MOD1 = 1000000007;
    static constexpr long long B2 = 317, MOD2 = 1000000009;

    std::vector<long long> h1, h2;
    std::vector<long long> p1, p2;

public:
    explicit DoubleHash(const std::string& s) {
        int n = static_cast<int>(s.size());
        h1.assign(n + 1, 0);
        h2.assign(n + 1, 0);
        p1.assign(n + 1, 1);
        p2.assign(n + 1, 1);

        for (int i = 0; i < n; ++i) {
            long long val = static_cast<unsigned char>(s[i]);
            h1[i + 1] = (h1[i] * B1 + val) % MOD1;
            h2[i + 1] = (h2[i] * B2 + val) % MOD2;
            p1[i + 1] = (p1[i] * B1) % MOD1;
            p2[i + 1] = (p2[i] * B2) % MOD2;
        }
    }

    // Get combined hash of substring s[l ... r] (0-indexed) in O(1)
    std::pair<long long, long long> getHash(int l, int r) const {
        long long hash1 = (h1[r + 1] - h1[l] * p1[r - l + 1]) % MOD1;
        if (hash1 < 0) hash1 += MOD1;

        long long hash2 = (h2[r + 1] - h2[l] * p2[r - l + 1]) % MOD2;
        if (hash2 < 0) hash2 += MOD2;

        return {hash1, hash2};
    }

    // Check if substring s[l1 ... r1] == s[l2 ... r2] in O(1)
    bool isEqual(int l1, int r1, int l2, int r2) const {
        if ((r1 - l1) != (r2 - l2)) return false;
        return getHash(l1, r1) == getHash(l2, r2);
    }
};
```

---

## 💻 Driver & Comprehensive Verification

```cpp
#include <iostream>
#include <cassert>

int main() {
    std::cout << "========== 1. MANACHER'S ALGORITHM ==========\n";
    std::string palStr = "babad";
    std::string lps = Manacher::longestPalindrome(palStr);
    std::cout << "String: \"" << palStr << "\" -> Longest Palindrome: \"" << lps << "\"\n";
    assert(lps == "bab" || lps == "aba");

    std::cout << "\n========== 2. AHO-CORASICK AUTOMATON ==========\n";
    AhoCorasick ac;
    std::vector<std::string> patterns = {"he", "she", "his", "hers"};
    for (size_t i = 0; i < patterns.size(); ++i) {
        ac.insert(patterns[i], static_cast<int>(i));
    }
    ac.build();

    std::string text = "ushers";
    auto acMatches = ac.search(text);
    std::cout << "Text: \"" << text << "\"\n";
    for (const auto& entry : acMatches) {
        int pIdx = entry.first;
        const auto& endPositions = entry.second;
        std::cout << "  Pattern \"" << patterns[pIdx] << "\" ends at indices: [";
        for (int pos : endPositions) std::cout << pos << " ";
        std::cout << "]\n";
    }

    std::cout << "\n========== 3. SUFFIX ARRAY & LCP ==========\n";
    std::string s = "banana";
    auto sa = SuffixArray::buildSA(s);
    auto lcp = SuffixArray::buildLCP(s, sa);
    std::cout << "String: \"" << s << "\"\nSuffix Array: [";
    for (int idx : sa) std::cout << idx << " ";
    std::cout << "]\nLCP Array:    [";
    for (int val : lcp) std::cout << val << " ";
    std::cout << "]\nDistinct Substrings: " << SuffixArray::countDistinctSubstrings(s) << "\n";
    assert(SuffixArray::countDistinctSubstrings(s) == 15);

    std::cout << "\n========== 4. DOUBLE POLYNOMIAL HASHING ==========\n";
    std::string repeatStr = "abcdeabcde";
    DoubleHash dh(repeatStr);
    bool match = dh.isEqual(0, 4, 5, 9); // "abcde" == "abcde"
    std::cout << "Comparing s[0..4] with s[5..9]: " << (match ? "EQUAL" : "NOT EQUAL") << "\n";
    assert(match == true);

    std::cout << "\n✅ All advanced string algorithms successfully compiled and verified!\n";
    return 0;
}
```

---

## Next Step

- Go to [README.md](README.md) to continue with Problem Solving.
