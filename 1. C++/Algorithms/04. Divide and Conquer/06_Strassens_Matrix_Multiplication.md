# 06_Strassens_Matrix_Multiplication.md

## Strassen's Matrix Multiplication

### Definition

Strassen's algorithm is a divide-and-conquer algorithm for matrix multiplication that multiplies two n×n matrices in O(n^2.81) time, which is better than the naive O(n³) algorithm.

### Standard Matrix Multiplication (Naive)

For two 2×2 matrices:

```
[A B]   [E F]   [AE+BG  AF+BH]
[C D] * [G H] = [CE+DG  CF+DH]
```

This requires 8 multiplications and 4 additions.

### Strassen's Improvement

Strassen discovered that 2×2 matrix multiplication can be done with only 7 multiplications (at the cost of more additions).

```
P1 = A * (F - H)
P2 = (A + B) * H
P3 = (C + D) * E
P4 = D * (G - E)
P5 = (A + D) * (E + H)
P6 = (B - D) * (G + H)
P7 = (A - C) * (E + F)

Then:
AE + BG = P5 + P4 - P2 + P6
AF + BH = P1 + P2
CE + DG = P3 + P4
CF + DH = P5 + P1 - P3 - P7
```

### Algorithm Steps

```
Step 1: Divide each matrix into 4 submatrices of size n/2 × n/2
Step 2: Compute 7 products recursively (P1 through P7)
Step 3: Compute the 4 quadrants of result using the formulas
Step 4: Combine quadrants into result matrix
```

### Implementation

```cpp
#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<long long>> Matrix;

Matrix add(Matrix A, Matrix B) {
    int n = A.size();
    Matrix C(n, vector<long long>(n));
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
    
    return C;
}

Matrix subtract(Matrix A, Matrix B) {
    int n = A.size();
    Matrix C(n, vector<long long>(n));
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i][j] = A[i][j] - B[i][j];
        }
    }
    
    return C;
}

Matrix strassen(Matrix A, Matrix B) {
    int n = A.size();
    
    // Base case: small matrix, use naive multiplication
    if (n <= 2) {
        Matrix C(n, vector<long long>(n, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        return C;
    }
    
    int newSize = n / 2;
    
    // Divide matrices into quadrants
    Matrix A11(newSize, vector<long long>(newSize));
    Matrix A12(newSize, vector<long long>(newSize));
    Matrix A21(newSize, vector<long long>(newSize));
    Matrix A22(newSize, vector<long long>(newSize));
    
    Matrix B11(newSize, vector<long long>(newSize));
    Matrix B12(newSize, vector<long long>(newSize));
    Matrix B21(newSize, vector<long long>(newSize));
    Matrix B22(newSize, vector<long long>(newSize));
    
    for (int i = 0; i < newSize; i++) {
        for (int j = 0; j < newSize; j++) {
            A11[i][j] = A[i][j];
            A12[i][j] = A[i][j + newSize];
            A21[i][j] = A[i + newSize][j];
            A22[i][j] = A[i + newSize][j + newSize];
            
            B11[i][j] = B[i][j];
            B12[i][j] = B[i][j + newSize];
            B21[i][j] = B[i + newSize][j];
            B22[i][j] = B[i + newSize][j + newSize];
        }
    }
    
    // Compute the 7 products
    Matrix P1 = strassen(A11, subtract(B12, B22));
    Matrix P2 = strassen(add(A11, A12), B22);
    Matrix P3 = strassen(add(A21, A22), B11);
    Matrix P4 = strassen(A22, subtract(B21, B11));
    Matrix P5 = strassen(add(A11, A22), add(B11, B22));
    Matrix P6 = strassen(subtract(A12, A22), add(B21, B22));
    Matrix P7 = strassen(subtract(A11, A21), add(B11, B12));
    
    // Compute result quadrants
    Matrix C11 = add(subtract(add(P5, P4), P2), P6);
    Matrix C12 = add(P1, P2);
    Matrix C21 = add(P3, P4);
    Matrix C22 = subtract(subtract(add(P5, P1), P3), P7);
    
    // Combine quadrants
    Matrix C(n, vector<long long>(n));
    for (int i = 0; i < newSize; i++) {
        for (int j = 0; j < newSize; j++) {
            C[i][j] = C11[i][j];
            C[i][j + newSize] = C12[i][j];
            C[i + newSize][j] = C21[i][j];
            C[i + newSize][j + newSize] = C22[i][j];
        }
    }
    
    return C;
}

int main() {
    Matrix A = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };
    
    Matrix B = {
        {1, 0, 0, 0},
        {0, 1, 0, 0},
        {0, 0, 1, 0},
        {0, 0, 0, 1}
    };
    
    Matrix C = strassen(A, B);
    
    cout << "Result Matrix:" << endl;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cout << C[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}
```

### Time Complexity Analysis

```
Recurrence: T(n) = 7T(n/2) + O(n²)

By Master Theorem:
T(n) = O(n^(log₂7)) ≈ O(n^2.807) ≈ O(n^2.81)
```

### Comparison of Matrix Multiplication Algorithms

| Algorithm | Time Complexity | Multiplications |
|-----------|----------------|-----------------|
| Naive | O(n³) | n³ |
| Strassen | O(n^2.81) | ~7n^2.81 |
| Coppersmith-Winograd | O(n^2.376) | Very complex |
| Current best | O(n^2.37286) | Theoretical |

### Space Complexity

O(n²) for storing submatrices

### When to Use Strassen

| Scenario | Recommendation |
|----------|----------------|
| n is power of 2 | Ideal |
| n is small (< 64) | Naive may be faster |
| n is large | Strassen wins |
| Floating point | May have precision issues |

### Advantages

| Advantage | Description |
|-----------|-------------|
| Asymptotically faster | O(n^2.81) vs O(n³) |
| Divide and conquer | Natural recursive structure |
| Cache efficient | When implemented carefully |

### Disadvantages

| Disadvantage | Description |
|--------------|-------------|
| Higher constant factor | More overhead than naive for small matrices |
| Numerical stability | Can accumulate rounding errors |
| Memory usage | Requires extra space for submatrices |
| Only for square matrices | Assumes n is power of 2 |

### Practice Problems

1. Multiply two 2×2 matrices using Strassen's formulas
2. Implement Strassen for n that is power of 2
3. Compare performance of naive vs Strassen for various n
4. Extend Strassen to handle matrices of any size (pad with zeros)
5. Implement Strassen for integer matrices (no precision issues)
---

## Next Step

- Go to [07_Closest_Pair_of_Points.md](07_Closest_Pair_of_Points.md) to continue with Closest Pair of Points.
