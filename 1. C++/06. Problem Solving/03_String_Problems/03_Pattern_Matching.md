# Pattern Matching Algorithms in C++

## 📖 Overview

Pattern matching is one of the most fundamental computational problems in computer science: given a **text** string $T$ of length $N$ and a **pattern** string $P$ of length $M$ ($M \le N$), find all occurrences (starting indices) of $P$ in $T$.

This guide covers complete, robust C++ implementations, mathematical proofs, step-by-step dry runs, and complexity analyses for the primary string matching algorithms:
1. **Naive (Brute-Force) Pattern Search**
2. **Knuth-Morris-Pratt (KMP) Algorithm**
3. **Rabin-Karp Rolling Hash Algorithm**
4. **Z-Algorithm**
5. **Boyer-Moore Algorithm (Bad Character Rule)**

---

## 📊 Summary Comparison

| Algorithm | Preprocessing Time | Search Time | Total Time (Worst) | Total Time (Average) | Auxiliary Space | Best Suited For |
|:---|:---|:---|:---|:---|:---|:---|
| **Naive** | None | $O((N - M + 1) \cdot M)$ | $O(N \cdot M)$ | $O(N)$ | $O(1)$ | Short texts, rare matches, quick prototyping |
| **KMP** | $O(M)$ | $O(N)$ | $O(N + M)$ | $O(N + M)$ | $O(M)$ | Guaranteed worst-case performance, streaming input |
| **Rabin-Karp** | $O(M)$ | $O(N)$ | $O(N \cdot M)$ | $O(N + M)$ | $O(1)$ | Multi-pattern matching, 2D pattern matching |
| **Z-Algorithm** | None ($P + \$ + T$) | $O(N + M)$ | $O(N + M)$ | $O(N + M)$ | $O(N + M)$ | Finding prefixes, period finding, exact matching |
| **Boyer-Moore** | $O(M + |\Sigma|)$ | $O(N / M)$ | $O(N \cdot M)$ | $O(N / M)$ | $O(|\Sigma|)$ | Large alphabets, long patterns, text editor searches |

---

## 1. Naive Pattern Search

### Concept
Slide the pattern $P$ over the text $T$ one character at a time. At each position $i \in [0, N - M]$, compare characters of $P$ and $T$. If all $M$ characters match, record index $i$.

### Implementation
```cpp
#include <iostream>
#include <vector>
#include <string>

std::vector<int> searchNaive(const std::string& text, const std::string& pattern) {
    std::vector<int> matches;
    int n = static_cast<int>(text.size());
    int m = static_cast<int>(pattern.size());

    if (m == 0 || m > n) return matches;

    for (int i = 0; i <= n - m; ++i) {
        int j = 0;
        while (j < m && text[i + j] == pattern[j]) {
            ++j;
        }
        if (j == m) {
            matches.push_back(i);
        }
    }
    return matches;
}
```

### Complexity
- **Time**: Worst-case $O(N \cdot M)$ (e.g., $T = \text{"AAAAAAAAAB"}$, $P = \text{"AAAB"}$). Best-case $O(N)$.
- **Space**: $O(1)$ auxiliary space.

---

## 2. Knuth-Morris-Pratt (KMP) Algorithm

### Key Insight
When a mismatch occurs after several matched characters, the naive algorithm restarts comparison from index $i+1$ of the text. KMP utilizes knowledge of the matched prefix to **never regress the text pointer**. It jumps the pattern pointer forward using a precomputed **$\pi$ array** (also called **LPS - Longest Prefix which is also Suffix**).

### Understanding the LPS Array
$\text{lps}[i]$ stores the length of the longest proper prefix of $P[0 \dots i]$ that is also a suffix of $P[0 \dots i]$.

**Example: $P = \text{"ABABCABAB"}$**
| Index $i$ | Substring | Proper Prefixes | Suffixes | LPS Value |
|:---|:---|:---|:---|:---|
| 0 | `"A"` | None | None | 0 |
| 1 | `"AB"` | `"A"` | `"B"` | 0 |
| 2 | `"ABA"` | `"A"`, `"AB"` | `"A"`, `"BA"` | 1 (`"A"`) |
| 3 | `"ABAB"` | `"A"`, `"AB"`, `"ABA"` | `"B"`, `"AB"`, `"BAB"` | 2 (`"AB"`) |
| 4 | `"ABABC"` | ... | ... | 0 |
| 5 | `"ABABCA"` | ... | ... | 1 (`"A"`) |
| 6 | `"ABABCAB"` | ... | ... | 2 (`"AB"`) |
| 7 | `"ABABCABA"`| ... | ... | 3 (`"ABA"`) |
| 8 | `"ABABCABAB"`| ... | ... | 4 (`"ABAB"`)|

### Complete KMP Implementation
```cpp
#include <iostream>
#include <vector>
#include <string>

class KMP {
public:
    // Build the Longest Prefix Suffix (LPS) array in O(M)
    static std::vector<int> buildLPS(const std::string& pattern) {
        int m = static_cast<int>(pattern.size());
        std::vector<int> lps(m, 0);
        int len = 0; // Length of the previous longest prefix suffix
        int i = 1;

        while (i < m) {
            if (pattern[i] == pattern[len]) {
                ++len;
                lps[i] = len;
                ++i;
            } else {
                if (len != 0) {
                    // Fall back to previous longest prefix
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    ++i;
                }
            }
        }
        return lps;
    }

    // Search pattern in text in O(N)
    static std::vector<int> search(const std::string& text, const std::string& pattern) {
        std::vector<int> matches;
        int n = static_cast<int>(text.size());
        int m = static_cast<int>(pattern.size());

        if (m == 0 || m > n) return matches;

        std::vector<int> lps = buildLPS(pattern);
        int i = 0; // Pointer for text
        int j = 0; // Pointer for pattern

        while (i < n) {
            if (text[i] == pattern[j]) {
                ++i;
                ++j;
            }

            if (j == m) {
                // Match found at index (i - j)
                matches.push_back(i - j);
                j = lps[j - 1]; // Reset pattern pointer using LPS
            } else if (i < n && text[i] != pattern[j]) {
                if (j != 0) {
                    j = lps[j - 1]; // Shift pattern using LPS without moving text pointer
                } else {
                    ++i;
                }
            }
        }
        return matches;
    }
};
```

---

## 3. Rabin-Karp Algorithm (Rolling Hash)

### Key Insight
Instead of checking character by character, compute a numerical hash of the pattern $P$, and compare it with the rolling hash of every length-$M$ window of $T$. If the hashes match, verify character-by-character to eliminate hash collisions (spurious hits).

### Mathematical Formulation
For string $S$ with base $B = 256$ and a large prime $Q = 10^9 + 7$:
$$\text{Hash}(S[0 \dots M-1]) = \left(\sum_{k=0}^{M-1} S[k] \cdot B^{M - 1 - k}\right) \pmod Q$$

To slide the window from $T[i \dots i+M-1]$ to $T[i+1 \dots i+M]$ in $O(1)$:
$$\text{Hash}_{\text{next}} = \left( B \cdot (\text{Hash}_{\text{prev}} - T[i] \cdot B^{M-1}) + T[i+M] \right) \pmod Q$$

### Complete Rabin-Karp Implementation
```cpp
#include <iostream>
#include <vector>
#include <string>

class RabinKarp {
private:
    static constexpr long long BASE = 256;
    static constexpr long long MOD = 1000000007;

public:
    static std::vector<int> search(const std::string& text, const std::string& pattern) {
        std::vector<int> matches;
        int n = static_cast<int>(text.size());
        int m = static_cast<int>(pattern.size());

        if (m == 0 || m > n) return matches;

        // Precompute BASE^(m-1) % MOD
        long long h = 1;
        for (int i = 0; i < m - 1; ++i) {
            h = (h * BASE) % MOD;
        }

        long long pHash = 0; // Hash value for pattern
        long long tHash = 0; // Hash value for current window in text

        // Calculate initial hashes for pattern and first window
        for (int i = 0; i < m; ++i) {
            pHash = (BASE * pHash + static_cast<unsigned char>(pattern[i])) % MOD;
            tHash = (BASE * tHash + static_cast<unsigned char>(text[i])) % MOD;
        }

        // Slide window over text
        for (int i = 0; i <= n - m; ++i) {
            // If hash matches, perform character-by-character check
            if (pHash == tHash) {
                bool match = true;
                for (int j = 0; j < m; ++j) {
                    if (text[i + j] != pattern[j]) {
                        match = false;
                        break;
                    }
                }
                if (match) {
                    matches.push_back(i);
                }
            }

            // Calculate hash for next window: remove leading char, add trailing char
            if (i < n - m) {
                tHash = (BASE * (tHash - static_cast<unsigned char>(text[i]) * h) + static_cast<unsigned char>(text[i + m])) % MOD;
                if (tHash < 0) {
                    tHash += MOD; // Ensure positive remainder
                }
            }
        }
        return matches;
    }
};
```

---

## 4. Z-Algorithm

### Key Insight
For a string $S$ of length $K$, the **Z-Array** $Z[i]$ represents the length of the longest substring starting at $S[i]$ that is also a prefix of $S$.
By creating a combined string $S = P + \text{"$"'} + T$ (where `$` is a delimiter not present in $P$ or $T$), any index $i$ in the text part where $Z[i] = M$ represents a full match of the pattern.

### Efficient $O(K)$ Z-Array Construction
Maintain a window $[L, R]$ where $S[L \dots R]$ is the prefix-matching substring with the maximum $R$. For each index $i$:
- If $i > R$, compute $Z[i]$ naively and update $[L, R]$.
- If $i \le R$, let $k = i - L$. If $Z[k] < R - i + 1$, then $Z[i] = Z[k]$. Otherwise, extend from $R + 1$ onwards and update $[L, R]$.

### Complete Z-Algorithm Implementation
```cpp
#include <iostream>
#include <vector>
#include <string>

class ZAlgorithm {
public:
    static std::vector<int> computeZ(const std::string& s) {
        int n = static_cast<int>(s.size());
        std::vector<int> z(n, 0);
        int l = 0, r = 0;

        for (int i = 1; i < n; ++i) {
            if (i <= r) {
                z[i] = std::min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
                ++z[i];
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        return z;
    }

    static std::vector<int> search(const std::string& text, const std::string& pattern) {
        std::vector<int> matches;
        int n = static_cast<int>(text.size());
        int m = static_cast<int>(pattern.size());

        if (m == 0 || m > n) return matches;

        std::string concat = pattern + "$" + text;
        std::vector<int> z = computeZ(concat);

        for (int i = m + 1; i < static_cast<int>(concat.size()); ++i) {
            if (z[i] == m) {
                matches.push_back(i - (m + 1));
            }
        }
        return matches;
    }
};
```

---

## 5. Boyer-Moore Algorithm (Bad Character Rule)

### Key Insight
Instead of scanning left-to-right, Boyer-Moore compares the pattern to the text **from right to left** ($j = M - 1$ down to $0$). When a mismatch occurs at $T[i + j] \ne P[j]$, it uses the **Bad Character Heuristic** to skip several alignments in one step.

### Bad Character Heuristic
If character $c = T[i + j]$ occurs in $P$, shift $P$ so that the rightmost occurrence of $c$ in $P$ aligns with $T[i + j]$. If $c$ does not occur in $P$, shift $P$ entirely past $T[i + j]$.

### Complete Boyer-Moore Implementation
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class BoyerMoore {
private:
    static constexpr int ALPHABET_SIZE = 256;

    static std::vector<int> buildBadCharTable(const std::string& pattern) {
        int m = static_cast<int>(pattern.size());
        std::vector<int> badChar(ALPHABET_SIZE, -1);
        for (int i = 0; i < m; ++i) {
            badChar[static_cast<unsigned char>(pattern[i])] = i;
        }
        return badChar;
    }

public:
    static std::vector<int> search(const std::string& text, const std::string& pattern) {
        std::vector<int> matches;
        int n = static_cast<int>(text.size());
        int m = static_cast<int>(pattern.size());

        if (m == 0 || m > n) return matches;

        std::vector<int> badChar = buildBadCharTable(pattern);
        int shift = 0;

        while (shift <= (n - m)) {
            int j = m - 1;

            // Right-to-left comparison
            while (j >= 0 && pattern[j] == text[shift + j]) {
                --j;
            }

            if (j < 0) {
                // Match found
                matches.push_back(shift);
                // Shift pattern past the current match if possible
                shift += (shift + m < n) ? (m - badChar[static_cast<unsigned char>(text[shift + m])]) : 1;
            } else {
                // Shift pattern based on the bad character rule
                shift += std::max(1, j - badChar[static_cast<unsigned char>(text[shift + j])]);
            }
        }
        return matches;
    }
};
```

---

## 💻 Driver & Comprehensive Verification

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <cassert>

void printMatches(const std::string& name, const std::vector<int>& matches) {
    std::cout << name << ": [";
    for (size_t i = 0; i < matches.size(); ++i) {
        std::cout << matches[i] << (i + 1 < matches.size() ? ", " : "");
    }
    std::cout << "]\n";
}

int main() {
    std::string text = "AABAACAADAABAABA";
    std::string pattern = "AABA";

    std::cout << "Text:    \"" << text << "\"\n";
    std::cout << "Pattern: \"" << pattern << "\"\n\n";

    auto mNaive = searchNaive(text, pattern);
    auto mKMP = KMP::search(text, pattern);
    auto mRK = RabinKarp::search(text, pattern);
    auto mZ = ZAlgorithm::search(text, pattern);
    auto mBM = BoyerMoore::search(text, pattern);

    printMatches("Naive      ", mNaive);
    printMatches("KMP        ", mKMP);
    printMatches("Rabin-Karp ", mRK);
    printMatches("Z-Algorithm", mZ);
    printMatches("Boyer-Moore", mBM);

    // Verify all algorithms produce the exact same indices
    assert(mNaive == mKMP);
    assert(mKMP == mRK);
    assert(mRK == mZ);
    assert(mZ == mBM);
    std::cout << "\n✅ All algorithms verified and match expected indices: {0, 9, 12}\n";

    return 0;
}
```

---

## Next Step

- Go to [04_String_Transformation.md](04_String_Transformation.md) to continue with String Transformations.
