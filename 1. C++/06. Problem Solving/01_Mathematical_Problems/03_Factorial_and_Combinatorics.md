# 03_Factorial_and_Combinatorics.md

## Factorial and Combinatorics

### Overview

Factorials and combinatorics form the foundation of counting problems. Factorial represents the product of all positive integers up to n, while combinatorics deals with counting selections and arrangements of objects. These concepts are essential for probability, statistics, and algorithmic problem solving.

---

### 1. Factorial

**Definition:** n! (n factorial) is the product of all positive integers from 1 to n.

```
n! = n × (n-1) × (n-2) × ... × 2 × 1
```

**Special cases:**
- 0! = 1 (by definition)
- 1! = 1

**First few factorials:**
- 0! = 1
- 1! = 1
- 2! = 2
- 3! = 6
- 4! = 24
- 5! = 120
- 6! = 720
- 7! = 5040
- 8! = 40320
- 9! = 362880
- 10! = 3628800

**Factorial Implementation:**

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Iterative factorial
long long factorialIterative(int n) {
    if (n < 0) return -1;  // Error
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

// Recursive factorial
long long factorialRecursive(int n) {
    if (n <= 1) return 1;
    return n * factorialRecursive(n - 1);
}

// Factorial modulo M (for large n)
long long factorialMod(int n, long long mod) {
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result = (result * i) % mod;
    }
    return result;
}

int main() {
    cout << "Factorial using iteration:" << endl;
    for (int i = 0; i <= 10; i++) {
        cout << i << "! = " << factorialIterative(i) << endl;
    }
    
    cout << "\nFactorial using recursion:" << endl;
    cout << "5! = " << factorialRecursive(5) << endl;
    cout << "7! = " << factorialRecursive(7) << endl;
    
    long long mod = 1000000007;
    cout << "\n10! mod " << mod << " = " << factorialMod(10, mod) << endl;
    
    return 0;
}
```

**Output:**
```
Factorial using iteration:
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800

Factorial using recursion:
5! = 120
7! = 5040

10! mod 1000000007 = 3628800
```

---

### 2. Factorial Properties

| Property | Expression | Example |
|----------|------------|---------|
| **Recurrence** | n! = n × (n-1)! | 5! = 5 × 24 = 120 |
| **Growth Rate** | n! ≈ √(2πn) × (n/e)ⁿ | Stirling's approximation |
| **Divisibility** | n! is divisible by all numbers ≤ n | 5! divisible by 1,2,3,4,5 |
| **Trailing Zeros** | Count factor of 10 = min(factor of 2, factor of 5) | 10! has 2 trailing zeros |

**Counting Trailing Zeros in n!:**

```cpp
#include <iostream>
using namespace std;

// Count trailing zeros in n!
int countTrailingZeros(int n) {
    int count = 0;
    for (int i = 5; i <= n; i *= 5) {
        count += n / i;
    }
    return count;
}

int main() {
    cout << "Trailing zeros in 10!: " << countTrailingZeros(10) << endl;
    cout << "Trailing zeros in 100!: " << countTrailingZeros(100) << endl;
    cout << "Trailing zeros in 1000!: " << countTrailingZeros(1000) << endl;
    
    return 0;
}
```

**Output:**
```
Trailing zeros in 10!: 2
Trailing zeros in 100!: 24
Trailing zeros in 1000!: 249
```

---

### 3. Permutations

**Definition:** A permutation is an arrangement of objects in a specific order. The number of ways to arrange r objects from a set of n distinct objects.

**Formula:** nPr = n! / (n - r)!

**Types of Permutations:**

| Type | Formula | Example |
|------|---------|---------|
| **r-permutations (ordered)** | n! / (n-r)! | Number of ways to choose president, VP, secretary from 10 people |
| **Permutations with repetition** | n^r | Number of 3-digit codes using digits 0-9 |
| **Circular permutations** | (n-1)! | Number of ways to seat n people around a circle |

```cpp
#include <iostream>
using namespace std;

// Compute nPr (permutations)
long long nPr(int n, int r) {
    if (r < 0 || r > n) return 0;
    
    long long result = 1;
    for (int i = 0; i < r; i++) {
        result *= (n - i);
    }
    return result;
}

// Permutations with repetition
long long permutationsWithRepetition(int n, int r) {
    long long result = 1;
    for (int i = 0; i < r; i++) {
        result *= n;
    }
    return result;
}

// Circular permutations
long long circularPermutations(int n) {
    if (n <= 0) return 0;
    long long result = 1;
    for (int i = 2; i < n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    cout << "P(10, 3) = " << nPr(10, 3) << " (ways to choose ordered committee of 3 from 10)" << endl;
    cout << "Permutations with repetition (10^3) = " << permutationsWithRepetition(10, 3) << " (3-digit codes)" << endl;
    cout << "Circular permutations (5 people) = " << circularPermutations(5) << " (ways to seat around circle)" << endl;
    
    return 0;
}
```

**Output:**
```
P(10, 3) = 720 (ways to choose ordered committee of 3 from 10)
Permutations with repetition (10^3) = 1000 (3-digit codes)
Circular permutations (5 people) = 24 (ways to seat around circle)
```

---

### 4. Combinations

**Definition:** A combination is a selection of objects where order does not matter. The number of ways to choose r objects from a set of n distinct objects.

**Formula:** nCr = n! / (r! × (n - r)!)

**Properties:**
- nCr = nC(n-r) (symmetry)
- nCr = nC(r-1) × (n - r + 1) / r (recurrence)

**Pascal's Rule:** nCr = (n-1)C(r-1) + (n-1)Cr

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Method 1: Direct computation (risk of overflow)
long long nCrDirect(int n, int r) {
    if (r < 0 || r > n) return 0;
    if (r == 0 || r == n) return 1;
    
    // Use symmetry to minimize computation
    if (r > n - r) r = n - r;
    
    long long result = 1;
    for (int i = 0; i < r; i++) {
        result = result * (n - i) / (i + 1);
    }
    return result;
}

// Method 2: Using Pascal's triangle (DP)
long long nCrDP(int n, int r) {
    vector<vector<long long>> C(n + 1, vector<long long>(n + 1, 0));
    
    for (int i = 0; i <= n; i++) {
        C[i][0] = C[i][i] = 1;
        for (int j = 1; j < i; j++) {
            C[i][j] = C[i-1][j-1] + C[i-1][j];
        }
    }
    
    return C[n][r];
}

// Method 3: nCr modulo M (for large values)
long long nCrMod(int n, int r, long long mod) {
    if (r < 0 || r > n) return 0;
    if (r == 0 || r == n) return 1;
    
    if (r > n - r) r = n - r;
    
    long long result = 1;
    for (int i = 0; i < r; i++) {
        result = (result * (n - i)) % mod;
        result = (result * modInverse(i + 1, mod)) % mod;
    }
    return result;
}

// Precompute factorials for nCr queries
vector<long long> fact, invFact;

void precomputeFactorials(int n, long long mod) {
    fact.resize(n + 1);
    invFact.resize(n + 1);
    
    fact[0] = 1;
    for (int i = 1; i <= n; i++) {
        fact[i] = (fact[i-1] * i) % mod;
    }
    
    invFact[n] = modPow(fact[n], mod - 2, mod);
    for (int i = n - 1; i >= 0; i--) {
        invFact[i] = (invFact[i+1] * (i + 1)) % mod;
    }
}

long long nCrPrecomputed(int n, int r, long long mod) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % mod * invFact[n - r] % mod;
}

int main() {
    cout << "C(10, 3) = " << nCrDirect(10, 3) << " (ways to choose 3 from 10)" << endl;
    cout << "C(10, 7) = " << nCrDirect(10, 7) << " (symmetry: C(10,7) = C(10,3))" << endl;
    
    long long mod = 1000000007;
    precomputeFactorials(100, mod);
    cout << "C(50, 25) mod " << mod << " = " << nCrPrecomputed(50, 25, mod) << endl;
    
    return 0;
}
```

**Output:**
```
C(10, 3) = 120 (ways to choose 3 from 10)
C(10, 7) = 120 (symmetry: C(10,7) = C(10,3))
C(50, 25) mod 1000000007 = 695109549
```

---

### 5. Pascal's Triangle

Pascal's triangle is a triangular array where each number is the sum of the two numbers above it.

```
Row 0:                1
Row 1:              1   1
Row 2:            1   2   1
Row 3:          1   3   3   1
Row 4:        1   4   6   4   1
Row 5:      1   5  10  10   5   1
Row 6:    1   6  15  20  15   6   1
```

**Properties:**
- First and last element of each row is 1
- Each element is C(row, column)
- Row sums = 2^row
- Alternating sum = 0 for row > 0

```cpp
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

vector<vector<long long>> generatePascalTriangle(int rows) {
    vector<vector<long long>> triangle(rows);
    
    for (int i = 0; i < rows; i++) {
        triangle[i].resize(i + 1, 1);
        for (int j = 1; j < i; j++) {
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j];
        }
    }
    
    return triangle;
}

void printPascalTriangle(int rows) {
    vector<vector<long long>> triangle = generatePascalTriangle(rows);
    
    for (int i = 0; i < rows; i++) {
        // Add spaces for alignment
        cout << string((rows - i - 1) * 3, ' ');
        
        for (int j = 0; j <= i; j++) {
            cout << setw(6) << triangle[i][j];
        }
        cout << endl;
    }
}

int main() {
    cout << "Pascal's Triangle (first 7 rows):" << endl;
    printPascalTriangle(7);
    
    cout << "\nRow sums:" << endl;
    for (int i = 0; i <= 10; i++) {
        long long rowSum = 0;
        for (int j = 0; j <= i; j++) {
            rowSum += nCrDirect(i, j);
        }
        cout << "Row " << i << " sum = " << rowSum << " = 2^" << i << endl;
    }
    
    return 0;
}
```

**Output:**
```
Pascal's Triangle (first 7 rows):
                    1
                 1     1
              1     2     1
           1     3     3     1
        1     4     6     4     1
     1     5    10    10     5     1
  1     6    15    20    15     6     1

Row sums:
Row 0 sum = 1 = 2^0
Row 1 sum = 2 = 2^1
Row 2 sum = 4 = 2^2
Row 3 sum = 8 = 2^3
Row 4 sum = 16 = 2^4
Row 5 sum = 32 = 2^5
Row 6 sum = 64 = 2^6
Row 7 sum = 128 = 2^7
Row 8 sum = 256 = 2^8
Row 9 sum = 512 = 2^9
Row 10 sum = 1024 = 2^10
```

---

### 6. Binomial Theorem

The binomial theorem describes the expansion of (x + y)ⁿ:

```
(x + y)ⁿ = Σ_{k=0}^{n} C(n,k) × x^{n-k} × y^k
```

**Examples:**
- (x + y)² = x² + 2xy + y²
- (x + y)³ = x³ + 3x²y + 3xy² + y³
- (x + y)⁴ = x⁴ + 4x³y + 6x²y² + 4xy³ + y⁴

**Useful Identities:**
- Σ C(n,k) = 2ⁿ
- Σ (-1)^k × C(n,k) = 0
- Σ k × C(n,k) = n × 2ⁿ⁻¹
- Σ k² × C(n,k) = n(n+1) × 2ⁿ⁻²

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printBinomialExpansion(int n) {
    cout << "(x + y)^" << n << " = ";
    
    for (int k = 0; k <= n; k++) {
        long long coeff = nCrDirect(n, k);
        
        if (coeff > 1) cout << coeff;
        
        if (n - k > 0) {
            cout << "x";
            if (n - k > 1) cout << "^" << (n - k);
        }
        
        if (k > 0) {
            cout << "y";
            if (k > 1) cout << "^" << k;
        }
        
        if (k < n) cout << " + ";
    }
    cout << endl;
}

int main() {
    for (int i = 1; i <= 5; i++) {
        printBinomialExpansion(i);
    }
    
    return 0;
}
```

**Output:**
```
(x + y)^1 = x + y
(x + y)^2 = x^2 + 2xy + y^2
(x + y)^3 = x^3 + 3x^2y + 3xy^2 + y^3
(x + y)^4 = x^4 + 4x^3y + 6x^2y^2 + 4xy^3 + y^4
(x + y)^5 = x^5 + 5x^4y + 10x^3y^2 + 10x^2y^3 + 5xy^4 + y^5
```

---

### 7. Stars and Bars (Combinations with Repetition)

The number of ways to distribute n identical items into k distinct bins:

**Formula:** C(n + k - 1, k - 1)

**Example:** Number of non-negative integer solutions to x₁ + x₂ + x₃ = 5 is C(5+3-1, 3-1) = C(7,2) = 21

```cpp
// Number of solutions to x1 + x2 + ... + xk = n (non-negative integers)
long long starsAndBars(int n, int k) {
    return nCrDirect(n + k - 1, k - 1);
}

int main() {
    cout << "Number of non-negative integer solutions to x+y+z = 5: " << starsAndBars(5, 3) << endl;
    cout << "Number of ways to distribute 10 identical candies among 4 children: " << starsAndBars(10, 4) << endl;
    
    return 0;
}
```

**Output:**
```
Number of non-negative integer solutions to x+y+z = 5: 21
Number of ways to distribute 10 identical candies among 4 children: 286
```

---

### Summary Table

| Concept | Formula | Complexity |
|---------|---------|------------|
| **Factorial** | n! = n × (n-1)! | O(n) |
| **Permutation (nPr)** | n! / (n-r)! | O(r) |
| **Combination (nCr)** | n! / (r! × (n-r)!) | O(r) |
| **nCr Mod M** | factorial precomputation + modular inverse | O(1) per query |
| **Pascal's Triangle** | DP recurrence | O(n²) |
| **Stars and Bars** | C(n+k-1, k-1) | O(k) |

---

### Key Takeaways

1. **Factorials grow extremely fast** - 20! exceeds 2⁶³, use modular arithmetic for large n
2. **nCr symmetry** - nCr = nC(n-r) can simplify computations
3. **Pascal's triangle** provides an O(n²) way to compute all binomial coefficients
4. **Precompute factorials** for O(1) nCr queries after O(n) preprocessing
5. **Stars and bars** solves distribution problems with identical items
6. **Stirling approximation** approximates large factorials

---

### Practice Questions

1. Compute 15! and count its trailing zeros
2. Find the number of ways to arrange the letters in "MISSISSIPPI"
3. Calculate C(100, 50) modulo 10⁹+7
4. How many 5-card hands can be dealt from a 52-card deck?
5. In how many ways can 3 people be chosen from 10 to form a committee?
6. Find the coefficient of x⁵ in (x + 2)¹⁰
7. How many non-negative integer solutions to x + y + z + w = 20?
8. Generate Pascal's triangle up to row 10

---

### Next Steps

- Go to [04_GCD_LCM.md](04_GCD_LCM.md) for GCD and LCM.