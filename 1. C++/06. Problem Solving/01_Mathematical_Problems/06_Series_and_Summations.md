# 06_Series_and_Summations.md

## Series and Summations

### Overview

Series and summations are fundamental mathematical concepts used to sum sequences of numbers. Understanding these formulas is crucial for algorithmic analysis, probability calculations, and many programming problems. This topic covers arithmetic and geometric progressions, summation formulas, and techniques for computing series efficiently.

---

### 1. Arithmetic Progression (AP)

**Definition:** An arithmetic progression is a sequence where the difference between consecutive terms is constant.

```
a, a + d, a + 2d, a + 3d, ...
```

Where:
- a = first term
- d = common difference
- n = number of terms

**nth term:** Tₙ = a + (n - 1)d

**Sum of first n terms:** Sₙ = n/2 × (2a + (n - 1)d) = n/2 × (first + last)

```cpp
#include <iostream>
using namespace std;

// nth term of AP
long long nthTermAP(long long a, long long d, long long n) {
    return a + (n - 1) * d;
}

// Sum of AP
long long sumAP(long long a, long long d, long long n) {
    return n * (2 * a + (n - 1) * d) / 2;
}

// Sum using first and last term
long long sumAPFirstLast(long long first, long long last, long long n) {
    return n * (first + last) / 2;
}

int main() {
    long long a = 2, d = 3, n = 5;
    
    cout << "AP: ";
    for (int i = 1; i <= n; i++) {
        cout << nthTermAP(a, d, i);
        if (i < n) cout << ", ";
    }
    cout << endl;
    
    cout << "Sum of first " << n << " terms: " << sumAP(a, d, n) << endl;
    
    // Example: Sum of first 100 natural numbers
    cout << "\nSum of first 100 natural numbers: ";
    cout << sumAP(1, 1, 100) << endl;
    cout << "Formula n(n+1)/2: " << (100 * 101) / 2 << endl;
    
    return 0;
}
```

**Output:**
```
AP: 2, 5, 8, 11, 14
Sum of first 5 terms: 40

Sum of first 100 natural numbers: 5050
Formula n(n+1)/2: 5050
```

---

### 2. Geometric Progression (GP)

**Definition:** A geometric progression is a sequence where each term is multiplied by a constant ratio.

```
a, ar, ar², ar³, ...
```

Where:
- a = first term
- r = common ratio
- n = number of terms

**nth term:** Tₙ = a × rⁿ⁻¹

**Sum of first n terms:**
- If r ≠ 1: Sₙ = a × (rⁿ - 1) / (r - 1)
- If r = 1: Sₙ = a × n

**Sum of infinite GP (|r| < 1):** S = a / (1 - r)

```cpp
#include <iostream>
#include <cmath>
using namespace std;

// nth term of GP (using pow for demonstration)
long long nthTermGP(long long a, long long r, long long n) {
    return a * pow(r, n - 1);
}

// Sum of GP (using integer types when possible)
double sumGP(double a, double r, int n) {
    if (r == 1) return a * n;
    return a * (pow(r, n) - 1) / (r - 1);
}

// Sum of infinite GP
double sumInfiniteGP(double a, double r) {
    if (abs(r) >= 1) return INFINITY;
    return a / (1 - r);
}

int main() {
    double a = 2, r = 3;
    int n = 5;
    
    cout << "GP: ";
    for (int i = 1; i <= n; i++) {
        cout << nthTermGP(a, r, i);
        if (i < n) cout << ", ";
    }
    cout << endl;
    
    cout << "Sum of first " << n << " terms: " << sumGP(a, r, n) << endl;
    
    // Geometric series with r < 1
    a = 1, r = 0.5;
    cout << "\nInfinite GP: a = 1, r = 0.5" << endl;
    cout << "Sum for infinite terms: " << sumInfiniteGP(a, r) << endl;
    
    return 0;
}
```

**Output:**
```
GP: 2, 6, 18, 54, 162
Sum of first 5 terms: 242

Infinite GP: a = 1, r = 0.5
Sum for infinite terms: 2
```

---

### 3. Special Summation Formulas

| Series | Formula | Example |
|--------|---------|---------|
| **Natural Numbers** | Σk = n(n+1)/2 | 1+2+...+100 = 5050 |
| **Squares** | Σk² = n(n+1)(2n+1)/6 | 1²+2²+...+10² = 385 |
| **Cubes** | Σk³ = [n(n+1)/2]² | 1³+2³+...+10³ = 3025 |
| **Odd Numbers** | Σ(2k-1) = n² | 1+3+5+...+(2n-1) = n² |
| **Even Numbers** | Σ2k = n(n+1) | 2+4+6+...+2n = n(n+1) |

```cpp
#include <iostream>
using namespace std;

// Sum of first n natural numbers
long long sumNatural(long long n) {
    return n * (n + 1) / 2;
}

// Sum of squares
long long sumSquares(long long n) {
    return n * (n + 1) * (2 * n + 1) / 6;
}

// Sum of cubes
long long sumCubes(long long n) {
    long long s = n * (n + 1) / 2;
    return s * s;
}

// Sum of odd numbers
long long sumOdds(long long n) {
    return n * n;
}

// Sum of even numbers
long long sumEvens(long long n) {
    return n * (n + 1);
}

int main() {
    int n = 10;
    
    cout << "n = " << n << endl;
    cout << "Sum of natural numbers (1 to " << n << "): " << sumNatural(n) << endl;
    cout << "Sum of squares (1² to " << n << "²): " << sumSquares(n) << endl;
    cout << "Sum of cubes (1³ to " << n << "³): " << sumCubes(n) << endl;
    cout << "Sum of odds (1 to " << 2*n-1 << "): " << sumOdds(n) << endl;
    cout << "Sum of evens (2 to " << 2*n << "): " << sumEvens(n) << endl;
    
    // Verify the identity: (1+2+...+n)² = 1³+2³+...+n³
    cout << "\nVerification of cube identity:" << endl;
    cout << "(1+2+...+n)² = " << (sumNatural(n) * sumNatural(n)) << endl;
    cout << "1³+2³+...+n³ = " << sumCubes(n) << endl;
    
    return 0;
}
```

**Output:**
```
n = 10
Sum of natural numbers (1 to 10): 55
Sum of squares (1² to 10²): 385
Sum of cubes (1³ to 10³): 3025
Sum of odds (1 to 19): 100
Sum of evens (2 to 20): 110

Verification of cube identity:
(1+2+...+n)² = 3025
1³+2³+...+n³ = 3025
```

---

### 4. Harmonic Series

**Definition:** The harmonic series is the sum of reciprocals of natural numbers.

```
Hₙ = 1 + 1/2 + 1/3 + ... + 1/n
```

**Properties:**
- Hₙ ≈ ln(n) + γ (where γ ≈ 0.5772156649 is Euler's constant)
- Hₙ grows very slowly

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double harmonicSum(int n) {
    double sum = 0.0;
    for (int i = 1; i <= n; i++) {
        sum += 1.0 / i;
    }
    return sum;
}

double harmonicApprox(int n) {
    return log(n) + 0.5772156649;  // ln(n) + γ
}

int main() {
    cout << fixed << setprecision(6);
    
    cout << "Harmonic Series H_n:" << endl;
    for (int n : {1, 2, 5, 10, 20, 100, 1000}) {
        double exact = harmonicSum(n);
        double approx = harmonicApprox(n);
        cout << "H_" << n << " = " << exact;
        cout << " (approx: " << approx << ", diff: " << approx - exact << ")" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Harmonic Series H_n:
H_1 = 1.000000 (approx: 0.577216, diff: -0.422784)
H_2 = 1.500000 (approx: 1.270363, diff: -0.229637)
H_5 = 2.283333 (approx: 2.188199, diff: -0.095134)
H_10 = 2.928968 (approx: 2.882439, diff: -0.046529)
H_20 = 3.597740 (approx: 3.571850, diff: -0.025890)
H_100 = 5.187378 (approx: 5.182385, diff: -0.004993)
H_1000 = 7.485471 (approx: 7.484971, diff: -0.000500)
```

---

### 5. Arithmetic-Geometric Series

A series where terms are products of corresponding terms of an AP and GP:

```
a + (a + d)r + (a + 2d)r² + ... + (a + (n-1)d)rⁿ⁻¹
```

**Sum formula:** Sₙ = [a - (a + (n-1)d)rⁿ] / (1 - r) + dr(1 - rⁿ⁻¹) / (1 - r)²

```cpp
#include <iostream>
#include <cmath>
using namespace std;

double arithmeticGeometricSum(double a, double d, double r, int n) {
    if (r == 1) {
        return n * (2 * a + (n - 1) * d) / 2;
    }
    
    double term1 = (a - (a + (n - 1) * d) * pow(r, n)) / (1 - r);
    double term2 = d * r * (1 - pow(r, n - 1)) / pow(1 - r, 2);
    return term1 + term2;
}

int main() {
    double a = 1, d = 2, r = 3;
    int n = 4;
    
    cout << "Arithmetic-Geometric Series:" << endl;
    cout << "a = " << a << ", d = " << d << ", r = " << r << ", n = " << n << endl;
    cout << "Terms: ";
    for (int i = 1; i <= n; i++) {
        double term = (a + (i - 1) * d) * pow(r, i - 1);
        cout << term;
        if (i < n) cout << " + ";
    }
    cout << endl;
    cout << "Sum = " << arithmeticGeometricSum(a, d, r, n) << endl;
    
    return 0;
}
```

**Output:**
```
Arithmetic-Geometric Series:
a = 1, d = 2, r = 3, n = 4
Terms: 1 + 9 + 45 + 189
Sum = 244
```

---

### 6. Summation Techniques

#### Prefix Sum Array

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> buildPrefixSum(vector<int>& arr) {
    vector<int> prefix(arr.size() + 1, 0);
    for (int i = 0; i < arr.size(); i++) {
        prefix[i + 1] = prefix[i] + arr[i];
    }
    return prefix;
}

int rangeSum(vector<int>& prefix, int l, int r) {
    // Sum of arr[l] to arr[r] (inclusive)
    return prefix[r + 1] - prefix[l];
}

int main() {
    vector<int> arr = {3, 1, 4, 1, 5, 9, 2, 6};
    vector<int> prefix = buildPrefixSum(arr);
    
    cout << "Array: ";
    for (int x : arr) cout << x << " ";
    cout << endl;
    
    cout << "Sum of arr[2] to arr[5]: " << rangeSum(prefix, 2, 5) << endl;
    cout << "Expected: 4 + 1 + 5 + 9 = " << (4 + 1 + 5 + 9) << endl;
    
    return 0;
}
```

**Output:**
```
Array: 3 1 4 1 5 9 2 6 
Sum of arr[2] to arr[5]: 19
Expected: 4 + 1 + 5 + 9 = 19
```

---

### 7. Common Series Summations

| Series | Formula | Complexity |
|--------|---------|------------|
| **1 + 1/2 + 1/4 + 1/8 + ...** | 2 | O(1) |
| **1 - 1/2 + 1/3 - 1/4 + ...** | ln 2 | O(n) |
| **1 + 1/2² + 1/3² + ...** | π²/6 | O(n) |
| **1/1×2 + 1/2×3 + 1/3×4 + ...** | 1 | O(1) |

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double leibnizPi(int n) {
    // π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
    double sum = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            sum += 1.0 / (2 * i + 1);
        } else {
            sum -= 1.0 / (2 * i + 1);
        }
    }
    return 4 * sum;
}

double baselProblem(int n) {
    // π²/6 = 1 + 1/2² + 1/3² + ...
    double sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += 1.0 / (i * i);
    }
    return sum;
}

double telescopingSeries(int n) {
    // 1/(1×2) + 1/(2×3) + ... + 1/(n×(n+1)) = 1 - 1/(n+1)
    double sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += 1.0 / (i * (i + 1));
    }
    return sum;
}

int main() {
    cout << fixed << setprecision(10);
    
    cout << "Leibniz formula for π (1000 terms): " << leibnizPi(1000) << endl;
    cout << "Actual π: " << M_PI << endl;
    
    cout << "\nBasel problem ζ(2) (1000 terms): " << baselProblem(1000) << endl;
    cout << "π²/6: " << (M_PI * M_PI / 6) << endl;
    
    cout << "\nTelescoping series (100 terms): " << telescopingSeries(100) << endl;
    cout << "Formula 1 - 1/(n+1): " << (1 - 1.0 / 101) << endl;
    
    return 0;
}
```

---

### Complexity Summary

| Series Type | Computation | Complexity |
|-------------|-------------|------------|
| **Arithmetic Progression** | Closed form | O(1) |
| **Geometric Progression** | Closed form (pow) | O(log n) |
| **Sum of powers** | Closed form | O(1) |
| **Harmonic Series** | Iterative | O(n) |
| **Prefix Sum** | Preprocess + O(1) query | O(n) preprocessing |

---

### Key Takeaways

1. **Arithmetic progression** has constant difference between terms
2. **Geometric progression** has constant ratio between terms
3. **Closed form formulas** compute sums in O(1) time
4. **Harmonic series** grows slowly (logarithmically)
5. **Prefix sums** enable O(1) range sum queries after O(n) preprocessing
6. **Telescoping series** cancel intermediate terms, simplifying computation

---

### Practice Questions

1. Find the sum of all odd numbers from 1 to 199
2. Find the sum of the first 20 terms of AP: 5, 8, 11, 14, ...
3. Find the sum of the infinite GP: 1, 1/2, 1/4, 1/8, ...
4. Compute 1² + 2² + 3² + ... + 20²
5. Find the sum of the first 10 terms of GP: 3, 6, 12, 24, ...
6. Calculate the harmonic sum H₁₀₀ (approximate)
7. Find the sum of 1/(1×2) + 1/(2×3) + ... + 1/(99×100)
8. Prove that the sum of first n natural numbers is n(n+1)/2

---

### Next Steps

- Now proceed to [02_Bit_Manipulation/README.md](../../02_Bit_Manipulation/README.md) for understanding Bit Manipulation.