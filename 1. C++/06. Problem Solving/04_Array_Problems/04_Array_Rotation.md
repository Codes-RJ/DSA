# Array Rotation in C++ - Reversal, Juggling, Block-Swap, and 2D Matrix Rotation

## 1. Introduction & Theoretical Foundations

**Array rotation** involves cyclically shifting the elements of an array by $k$ positions. If an array has length $N$, shifting by $k$ positions partitions the array into two contiguous blocks $A = \text{arr}[0 \dots k-1]$ and $B = \text{arr}[k \dots N-1]$, and transforms $AB \to BA$.

Rotating an array efficiently without allocating $O(N)$ auxiliary buffers is a fundamental interview problem. The operations must also handle arbitrary rotation magnitudes $k \ge N$ (via $k = k \bmod N$) and negative rotations.

This module provides exhaustive theoretical proofs and production-ready C++ implementations for:
1. **The Reversal Algorithm** (3 Reversals in $O(N)$ Time, $O(1)$ Space)
2. **The Juggling Algorithm** (Cycle Decomposition via $\gcd(N, k)$)
3. **Block Swap Algorithm** (Divide & Conquer Recursive Partitioning)
4. **2D Matrix In-Place Rotation by 90°** (Transpose + Reversal)

---

## 2. 1D Array Rotation Algorithms

```
Original Array:   [ 1, 2, 3, 4, 5, 6, 7 ],  k = 3 (Left Rotate)
                   ◄── A ──► ◄─── B ────►

1. Reverse A:     [ 3, 2, 1, 4, 5, 6, 7 ]
2. Reverse B:     [ 3, 2, 1, 7, 6, 5, 4 ]
3. Reverse All:   [ 4, 5, 6, 7, 1, 2, 3 ]  == BA (Rotated!)
```

### 1. The Reversal Algorithm
**Theorem:** For any two strings/blocks $A$ and $B$, $(A^R B^R)^R = (B^R)^R (A^R)^R = BA$.
- To rotate **Left** by $k$:
  1. Reverse $A = \text{arr}[0 \dots k-1]$
  2. Reverse $B = \text{arr}[k \dots N-1]$
  3. Reverse entire array $\text{arr}[0 \dots N-1]$
- To rotate **Right** by $k$:
  Right rotate by $k$ is equivalent to Left rotate by $N - (k \bmod N)$.

### 2. The Juggling Algorithm (GCD Cycles)
Instead of moving one by one or reversing, we can decompose the cyclic permutation into $\gcd(N, k)$ independent disjoint cycles.
Each cycle starts at index $i \in [0, \gcd(N, k) - 1]$ and shifts elements along index chain:
$$i \to (i + k) \bmod N \to (i + 2k) \bmod N \to \dots \to i$$
Every single element is moved exactly once!

### C++ Implementation: 1D Array Rotations

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

class ArrayRotation {
private:
    static int gcd(int a, int b) {
        while (b) {
            a %= b;
            std::swap(a, b);
        }
        return a;
    }

    static void reverseRange(std::vector<int>& arr, int start, int end) {
        while (start < end) {
            std::swap(arr[start++], arr[end--]);
        }
    }

public:
    // 1. Reversal Algorithm: O(N) time, O(1) space
    static void rotateLeftReversal(std::vector<int>& arr, int k) {
        int n = arr.size();
        if (n <= 1) return;
        k %= n;
        if (k < 0) k += n;
        if (k == 0) return;

        reverseRange(arr, 0, k - 1);
        reverseRange(arr, k, n - 1);
        reverseRange(arr, 0, n - 1);
    }

    static void rotateRightReversal(std::vector<int>& arr, int k) {
        int n = arr.size();
        if (n <= 1) return;
        k %= n;
        if (k < 0) k += n;
        rotateLeftReversal(arr, n - k);
    }

    // 2. Juggling Algorithm: O(N) time, O(1) space, exactly N writes
    static void rotateLeftJuggling(std::vector<int>& arr, int k) {
        int n = arr.size();
        if (n <= 1) return;
        k %= n;
        if (k < 0) k += n;
        if (k == 0) return;

        int numCycles = gcd(n, k);
        for (int i = 0; i < numCycles; ++i) {
            int temp = arr[i];
            int j = i;

            while (true) {
                int d = (j + k) % n;
                if (d == i) break;
                arr[j] = arr[d];
                j = d;
            }
            arr[j] = temp;
        }
    }
};
```

---

## 3. 2D Matrix In-Place Rotation (90 Degrees)

### Problem Statement
Given an $N \times N$ 2D matrix representing an image, rotate the image **90 degrees clockwise** in-place (without allocating another $N \times N$ matrix).

```
Original Matrix:          Step 1: Transpose                Step 2: Reverse Each Row
┌───┬───┬───┐             ┌───┬───┬───┐                    ┌───┬───┬───┐
│ 1 │ 2 │ 3 │             │ 1 │ 4 │ 7 │                    │ 7 │ 4 │ 1 │
├───┼───┼───┤             ├───┼───┼───┤                    ├───┼───┼───┤
│ 4 │ 5 │ 6 │    ───►     │ 2 │ 5 │ 8 │           ───►     │ 8 │ 5 │ 2 │
├───┼───┼───┤             ├───┼───┼───┤                    ├───┼───┼───┤
│ 7 │ 8 │ 9 │             │ 3 │ 6 │ 9 │                    │ 9 │ 6 │ 3 │
└───┴───┴───┘             └───┴───┴───┘                    └───┴───┴───┘
```

### Mathematical Geometric Invariant
1. **Clockwise 90° Rotation**:
   - Rotation maps cell $(r, c) \to (c, N - 1 - r)$.
   - Decomposing this affine transform:
     - **Transpose**: $(r, c) \to (c, r)$ (reflect across main diagonal).
     - **Horizontal Reflection**: $(c, r) \to (c, N - 1 - r)$ (reverse each row).
2. **Counter-Clockwise 90° Rotation**:
   - Rotation maps cell $(r, c) \to (N - 1 - c, r)$.
   - Decompose into:
     - **Transpose**: $(r, c) \to (c, r)$.
     - **Vertical Reflection**: Reverse each column (or reverse columns first, then transpose).

### C++ Implementation: 2D Matrix Rotations

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

class MatrixRotation {
public:
    // Rotate N x N matrix 90 degrees Clockwise in-place
    static void rotateClockwise(std::vector<std::vector<int>>& matrix) {
        int n = matrix.size();
        if (n <= 1) return;

        // Step 1: Transpose matrix (swap matrix[i][j] with matrix[j][i])
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                std::swap(matrix[i][j], matrix[j][i]);
            }
        }

        // Step 2: Reverse each row
        for (int i = 0; i < n; ++i) {
            std::reverse(matrix[i].begin(), matrix[i].end());
        }
    }

    // Rotate N x N matrix 90 degrees Counter-Clockwise in-place
    static void rotateCounterClockwise(std::vector<std::vector<int>>& matrix) {
        int n = matrix.size();
        if (n <= 1) return;

        // Step 1: Transpose matrix
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                std::swap(matrix[i][j], matrix[j][i]);
            }
        }

        // Step 2: Reverse each column
        for (int j = 0; j < n; ++j) {
            for (int i = 0, k = n - 1; i < k; ++i, --k) {
                std::swap(matrix[i][j], matrix[k][j]);
            }
        }
    }
};
```

---

## 4. Complete Runnable Verification Suite

```cpp
#include <iostream>
#include <vector>
#include <iomanip>

int main() {
    std::cout << "=====================================================" << std::endl;
    std::cout << "           ARRAY ROTATION ALGORITHMIC SUITE          " << std::endl;
    std::cout << "=====================================================" << std::endl;

    // --- 1. 1D Array Rotation: Reversal vs Juggling ---
    std::cout << "\n[1] 1D ARRAY ROTATION (arr = {1, 2, 3, 4, 5, 6, 7}, k = 3 left):" << std::endl;
    std::vector<int> arr1 = {1, 2, 3, 4, 5, 6, 7};
    ArrayRotation::rotateLeftReversal(arr1, 3);
    std::cout << "  Reversal Result: ";
    for (int v : arr1) std::cout << v << " ";
    std::cout << " (Expected: 4 5 6 7 1 2 3)" << std::endl;

    std::vector<int> arr2 = {1, 2, 3, 4, 5, 6, 7};
    ArrayRotation::rotateLeftJuggling(arr2, 3);
    std::cout << "  Juggling Result: ";
    for (int v : arr2) std::cout << v << " ";
    std::cout << " (Expected: 4 5 6 7 1 2 3)" << std::endl;

    // --- 2. 1D Right Rotation ---
    std::cout << "\n[2] 1D RIGHT ROTATION (arr = {1, 2, 3, 4, 5}, k = 2 right):" << std::endl;
    std::vector<int> arrRight = {1, 2, 3, 4, 5};
    ArrayRotation::rotateRightReversal(arrRight, 2);
    std::cout << "  Right Rotated:   ";
    for (int v : arrRight) std::cout << v << " ";
    std::cout << " (Expected: 4 5 1 2 3)" << std::endl;

    // --- 3. 2D Matrix Clockwise Rotation ---
    std::cout << "\n[3] 2D MATRIX 90-DEGREE CLOCKWISE IN-PLACE ROTATION:" << std::endl;
    std::vector<std::vector<int>> mat = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    MatrixRotation::rotateClockwise(mat);
    for (const auto& row : mat) {
        std::cout << "  ";
        for (int v : row) std::cout << v << " ";
        std::cout << "\n";
    }
    std::cout << "  Expected:\n  7 4 1\n  8 5 2\n  9 6 3\n";

    std::cout << "\n=====================================================" << std::endl;
    return 0;
}
```

---

## 5. Complexity Analysis Table

| Rotation Problem | Algorithm | Time Complexity | Auxiliary Space | Total Data Writes |
| :--- | :--- | :--- | :--- | :--- |
| **1D Rotate** | Reversal Algorithm | $O(N)$ | $O(1)$ | $2N$ element swaps |
| **1D Rotate** | Juggling Algorithm | $O(N)$ | $O(1)$ | Exactly $N$ assignments |
| **2D 90° Clockwise** | Transpose + Row Reverse | $O(N^2)$ | $O(1)$ | $N^2$ element swaps |
| **2D 90° Counter-CW** | Transpose + Col Reverse | $O(N^2)$ | $O(1)$ | $N^2$ element swaps |

---

## 6. Common Pitfalls & Edge Cases

1. **Large $k$ Without Modulo**: Not computing `k = k % n` causes out-of-bounds crashes when $k \ge n$.
2. **Negative $k$ Rotations**: C++ `%` operator retains the sign of negative dividends (`-2 % 5 == -2`). Always normalize via `k = (k % n + n) % n`.
3. **2D Transpose Swapping Double Count**: When computing the transpose, starting the inner loop at `0` instead of `i + 1` swaps elements twice, leaving the matrix unchanged! Always use `for (int j = i + 1; j < n; ++j)`.

---

## Next Step

- Proceed to [05_Subarray_Problems.md](05_Subarray_Problems.md) to explore Kadane's algorithm, prefix sum hash maps, and maximum circular subarrays.
