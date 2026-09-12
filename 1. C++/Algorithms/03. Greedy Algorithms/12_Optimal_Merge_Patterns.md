# Optimal Merge Patterns (Greedy Minimum Merge Cost)

## 📖 Overview

The **Optimal Merge Patterns** problem (also known as the **Connecting Wires / Ropes Problem**) is a foundational greedy optimization problem directly equivalent to **Huffman Tree Construction**.

Given $N$ sorted files of sizes $S_1, S_2, \dots, S_N$:
- Merging two files of size $X$ and size $Y$ produces a merged file of size $X + Y$.
- The computational cost of the merge operation is equal to $X + Y$ operations.
- The newly formed file is placed back into the pool of files to be merged.
- **Objective**: Determine the optimal merge sequence that minimizes the **total cumulative cost** to merge all $N$ files into a single file.

---

## 🎯 The Merge Tree & Cost Formulation

Any sequence of 2-way merges can be represented as an **extended binary tree** (the Merge Tree):
- The original $N$ files are the **leaf nodes**.
- Each internal node represents a merge step whose weight is the sum of its children.
- The total cost is the sum of all internal nodes, or equivalently:
  $$\text{Total Cost} = \sum_{i=1}^N S_i \cdot d_i$$
  where $S_i$ is the size of the $i$-th initial file, and $d_i$ is the depth (number of edges from root) of leaf $i$ in the merge tree.

```
Example: Files of sizes [2, 3, 4, 5, 6]

               [20]  <-- Root (Total size)
             /      \
            9       [11]
          /   \     /   \
         4     5   5     6
                  / \
                 2   3

Internal Node Costs:
  Step 1: Merge 2 + 3 = 5    (Cost: 5)
  Step 2: Merge 4 + 5 = 9    (Cost: 9)
  Step 3: Merge 5 + 6 = 11   (Cost: 11)
  Step 4: Merge 9 + 11 = 20  (Cost: 20)
---------------------------------------
Total Cumulative Cost = 5 + 9 + 11 + 20 = 45
```

### The Greedy Choice Property
At each step, **greedily merge the two smallest available files**. 
- Because each merge step increases the depth $d_i$ of the participating files by 1, multiplying larger file sizes by larger depths increases total cost.
- Placing the smallest files at the deepest levels ($d_i$ largest) and the largest files closest to the root ($d_i$ smallest) minimizes the sum $\sum S_i \cdot d_i$.

---

## 💻 Complete C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <cassert>
#include <iomanip>
#include <string>

class OptimalMerge {
public:
    struct MergeStep {
        long long file1;
        long long file2;
        long long mergedSize;
    };

    struct MergeResult {
        long long totalCost;
        std::vector<MergeStep> steps;
    };

    // Computes optimal merge cost using a Min-Heap (O(N log N) time)
    static MergeResult computeOptimalMerge(const std::vector<long long>& fileSizes) {
        if (fileSizes.empty()) {
            return {0, {}};
        }
        if (fileSizes.size() == 1) {
            return {0, {}}; // No merges needed
        }

        // Min-heap to always extract the two smallest elements
        std::priority_queue<long long, std::vector<long long>, std::greater<long long>> minHeap(
            fileSizes.begin(), fileSizes.end()
        );

        long long totalCost = 0;
        std::vector<MergeStep> steps;

        while (minHeap.size() > 1) {
            long long first = minHeap.top();
            minHeap.pop();

            long long second = minHeap.top();
            minHeap.pop();

            long long currentCost = first + second;
            totalCost += currentCost;

            steps.push_back({first, second, currentCost});

            minHeap.push(currentCost);
        }

        return {totalCost, steps};
    }
};

int main() {
    std::cout << "=== Optimal Merge Patterns Test Harness ===\n\n";

    struct TestCase {
        std::vector<long long> files;
        long long expectedCost;
        std::string description;
    };

    std::vector<TestCase> testCases = {
        {
            {2, 3, 4, 5, 6}, 
            45, 
            "Five files [2, 3, 4, 5, 6]"
        },
        {
            {4, 3, 2, 6}, 
            29, 
            "Four files unsorted [4, 3, 2, 6] -> Merges: (2+3=5), (4+5=9), (6+9=15) = 29"
        },
        {
            {10, 20, 30}, 
            90, 
            "Three files: (10+20=30), (30+30=60) => 30 + 60 = 90"
        },
        {
            {5}, 
            0, 
            "Single file: No merges needed"
        },
        {
            {1, 2, 5, 10, 35, 89}, 
            224, 
            "Rapidly increasing file sizes"
        }
    };

    for (const auto& tc : testCases) {
        std::cout << "Testing: " << tc.description << "\n";
        std::cout << "  Initial Files: [ ";
        for (long long s : tc.files) std::cout << s << " ";
        std::cout << "]\n";

        auto result = OptimalMerge::computeOptimalMerge(tc.files);

        std::cout << "  Merge Sequence:\n";
        for (size_t i = 0; i < result.steps.size(); i++) {
            const auto& step = result.steps[i];
            std::cout << "    Step " << (i + 1) << ": Merge " << step.file1 
                      << " + " << step.file2 << " => New File " << step.mergedSize 
                      << " (Step Cost: " << step.mergedSize << ")\n";
        }

        std::cout << "  Total Merge Cost: " << result.totalCost 
                  << " [Expected: " << tc.expectedCost << "] => " 
                  << (result.totalCost == tc.expectedCost ? "PASSED" : "FAILED") << "\n\n";

        assert(result.totalCost == tc.expectedCost);
    }

    std::cout << "=== All Optimal Merge Patterns Tests Completed Successfully! ===\n";
    return 0;
}
```

---

## 📊 Complexity Analysis

| Phase / Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Heap Initialization** | $O(N)$ | Floyd's bottom-up linear heap construction |
| **Merge Iterations** | $N - 1$ steps | Exactly $N - 1$ two-way merges reduce $N$ files to 1 |
| **Extract Min & Insert** | $O(\log N)$ | Two `pop()` and one `push()` per merge step |
| **Total Time Complexity** | $O(N \log N)$ | $(N - 1) \times O(\log N)$ priority queue operations |
| **Auxiliary Space** | $O(N)$ | Min-heap holding at most $N$ elements |

---

## 💡 Practical Insights & Variations

1. **Equivalence to Huffman Coding**:
   - The merge tree generated by this greedy algorithm has the exact same structure as a **Huffman Encoding Tree**, where file sizes represent character frequencies and the total cost represents the total bits needed to encode the file collection.
2. **K-Way Merge Generalization**:
   - If we can merge $K$ files simultaneously instead of 2, the greedy strategy still applies: merge the $K$ smallest files at each step. 
   - *Subtle Gotcha*: Before starting, if $(N - 1) \pmod{K - 1} \neq 0$, we must pad the input with $(K - 1) - ((N - 1) \pmod{K - 1})$ dummy files of size 0 to ensure the final root merge consumes exactly $K$ files.
