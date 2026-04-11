# 05_Power_Exponentiation.md

## Power Exponentiation (Binary Exponentiation)

### Definition

Binary exponentiation (also called exponentiation by squaring) is a divide-and-conquer algorithm that computes x^n efficiently in O(log n) time instead of O(n) time.

### Mathematical Foundation

```
x^n = (x^(n/2))^2 if n is even
x^n = x * (x^((n-1)/2))^2 if n is odd
x^0 = 1
```

### Visual Example

```
Compute 2^13:

13 is odd: 2^13 = 2 * (2^6)^2
6 is even: 2^6 = (2^3)^2
3 is odd: 2^3 = 2 * (2^1)^2
1 is odd: 2^1 = 2 * (2^0)^2 = 2 * 1^2 = 2

Backtrack:
2^3 = 2 * (2)^2 = 2 * 4 = 8
2^6 = (8)^2 = 64
2^13 = 2 * (64)^2 = 2 * 4096 = 8192
```

### Implementation (Recursive)

```cpp
#include <iostream>
using namespace std;

long long powerRecursive(long long x, long long n) {
    if (n == 0) return 1;
    
    long long half = powerRecursive(x, n / 2);
    
    if (n % 2 == 0) {
        return half * half;
    } else {
        return x * half * half;
    }
}

int main() {
    long long x = 2;
    long long n = 13;
    
    long long result = powerRecursive(x, n);
    cout << x << "^" << n << " = " << result << endl;
    
    return 0;
}
```

### Implementation (Iterative)

```cpp
long long powerIterative(long long x, long long n) {
    long long result = 1;
    
    while (n > 0) {
        if (n % 2 == 1) {
            result = result * x;
        }
        x = x * x;
        n = n / 2;
    }
    
    return result;
}
```

### Iterative Visualization

```
Compute 2^13:

x = 2, n = 13, result = 1

n=13 (odd): result = 1 * 2 = 2, x = 4, n = 6
n=6 (even): result = 2, x = 16, n = 3
n=3 (odd): result = 2 * 16 = 32, x = 256, n = 1
n=1 (odd): result = 32 * 256 = 8192, x = 65536, n = 0

Result: 8192
```

### Modular Exponentiation

Used when result can be very large. Compute (x^n) % MOD.

```cpp
const int MOD = 1e9 + 7;

long long powerMod(long long x, long long n, long long mod) {
    long long result = 1;
    x = x % mod;
    
    while (n > 0) {
        if (n % 2 == 1) {
            result = (result * x) % mod;
        }
        x = (x * x) % mod;
        n = n / 2;
    }
    
    return result;
}
```

### Handling Negative Exponents

```cpp
double powerNegative(double x, long long n) {
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    
    double result = 1.0;
    
    while (n > 0) {
        if (n % 2 == 1) {
            result = result * x;
        }
        x = x * x;
        n = n / 2;
    }
    
    return result;
}
```

### Matrix Exponentiation

Used to compute Fibonacci numbers and other linear recurrences efficiently.

```cpp
struct Matrix {
    long long a, b, c, d;
    
    Matrix(long long a1, long long b1, long long c1, long long d1)
        : a(a1), b(b1), c(c1), d(d1) {}
    
    Matrix multiply(const Matrix& other) const {
        return Matrix(
            a * other.a + b * other.c,
            a * other.b + b * other.d,
            c * other.a + d * other.c,
            c * other.b + d * other.d
        );
    }
};

Matrix matrixPower(Matrix m, long long n) {
    Matrix result(1, 0, 0, 1);  // identity matrix
    
    while (n > 0) {
        if (n % 2 == 1) {
            result = result.multiply(m);
        }
        m = m.multiply(m);
        n = n / 2;
    }
    
    return result;
}

// Fibonacci using matrix exponentiation
long long fibonacci(long long n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    Matrix base(1, 1, 1, 0);
    Matrix result = matrixPower(base, n - 1);
    
    return result.a;
}
```

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| Binary exponentiation | O(log n) |
| Naive exponentiation | O(n) |
| Matrix exponentiation | O(log n) for 2x2 matrix |

### Space Complexity

| Implementation | Space |
|----------------|-------|
| Iterative | O(1) |
| Recursive | O(log n) |

### Applications

| Application | Description |
|-------------|-------------|
| Cryptography | RSA encryption uses modular exponentiation |
| Fibonacci numbers | Compute large Fibonacci numbers |
| Linear recurrences | Solve recurrences in O(log n) |
| Combinatorics | Compute large powers modulo MOD |
| Computer graphics | Transformations and rotations |

### Comparison of Methods

| n | Naive (O(n)) | Binary (O(log n)) |
|---|--------------|-------------------|
| 10 | 10 operations | 4 operations |
| 100 | 100 operations | 7 operations |
| 1000 | 1000 operations | 10 operations |
| 10^9 | 1e9 operations | 30 operations |

### Practice Problems

1. Compute x^n for large n
2. Compute (x^n) % MOD for large n
3. Compute x^(-n) for negative exponents
4. Find nth Fibonacci number using matrix exponentiation
5. Compute sum of geometric series using exponentiation
6. Find modular inverse using Fermat's theorem