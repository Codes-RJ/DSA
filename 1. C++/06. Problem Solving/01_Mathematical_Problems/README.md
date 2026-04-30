# README.md

## Mathematical Problems - Complete Guide

### Overview

Mathematical problems form the foundation of algorithmic thinking. They involve number theory, combinatorics, modular arithmetic, series, and prime numbers. Solving mathematical problems efficiently requires understanding mathematical concepts and their algorithmic implementations. These problems frequently appear in coding interviews and competitive programming.

---

### Topics Covered

| # | Name | Purpose |
| --- | --- | --- |
| 1. | [01_Number_Theory.md](01_Number_Theory.md) | understand Number Theory Basics |
| 2. | [02_Prime_Numbers.md](02_Prime_Numbers.md) | understand Prime Numbers and Sieve Algorithms |
| 3. | [03_Factorial_and_Combinatorics.md](03_Factorial_and_Combinatorics.md) | understand Factorial and Combinatorics |
| 4. | [04_GCD_LCM.md](04_GCD_LCM.md) | understand GCD and LCM (Euclidean Algorithm) |
| 5. | [05_Modular_Arithmetic.md](05_Modular_Arithmetic.md) | understand Modular Arithmetic |
| 6. | [06_Series_and_Summations.md](06_Series_and_Summations.md) | understand Series and Summations |
| 7. | [README.md](README.md) | understand Mathematical Problems Overview |

---

## 1. Number Theory

This topic covers fundamental number theory concepts and algorithms.

**File:** [01_Number_Theory.md](01_Number_Theory.md)

**What you will learn:**
- Divisibility rules
- Prime numbers and composite numbers
- Factors and multiples
- Prime factorization
- Divisors and their properties
- Perfect numbers, abundant numbers, deficient numbers

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Divisor** | Number that divides another number evenly |
| **Prime Number** | Number greater than 1 with exactly two divisors |
| **Composite Number** | Number with more than two divisors |
| **Prime Factorization** | Breaking number into product of primes |

**Syntax:**
```cpp
// Prime factorization
vector<int> primeFactors(int n) {
    vector<int> factors;
    for (int i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            factors.push_back(i);
            n /= i;
        }
    }
    if (n > 1) factors.push_back(n);
    return factors;
}
```

---

## 2. Prime Numbers

This topic covers prime number detection and generation algorithms.

**File:** [02_Prime_Numbers.md](02_Prime_Numbers.md)

**What you will learn:**
- Primality testing (trial division)
- Sieve of Eratosthenes (generate all primes up to n)
- Sieve of Sundaram
- Segmented Sieve (for large ranges)
- Miller-Rabin primality test (probabilistic)

**Key Concepts:**

| Algorithm | Complexity | Use Case |
|-----------|------------|----------|
| **Trial Division** | O(√n) | Single number |
| **Sieve of Eratosthenes** | O(n log log n) | All primes up to n |
| **Segmented Sieve** | O(√R log log R) | Primes in range [L,R] |

**Syntax:**
```cpp
// Sieve of Eratosthenes
vector<bool> sieve(int n) {
    vector<bool> isPrime(n + 1, true);
    isPrime[0] = isPrime[1] = false;
    
    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    return isPrime;
}
```

---

## 3. Factorial and Combinatorics

This topic covers factorial computation and combinatorial counting.

**File:** [03_Factorial_and_Combinatorics.md](03_Factorial_and_Combinatorics.md)

**What you will learn:**
- Factorial computation (iterative, recursive)
- Large factorial modulo
- Permutations (nPr)
- Combinations (nCr)
- Binomial coefficients
- Pascal's triangle

**Key Concepts:**

| Formula | Expression | Description |
|---------|------------|-------------|
| **Factorial** | n! = n × (n-1) × ... × 1 | Product of first n numbers |
| **Permutation** | nPr = n! / (n-r)! | Number of arrangements |
| **Combination** | nCr = n! / (r! × (n-r)!) | Number of selections |

**Syntax:**
```cpp
// Combination using symmetry
long long combination(int n, int r) {
    if (r > n) return 0;
    if (r == 0 || r == n) return 1;
    if (r > n - r) r = n - r;
    
    long long result = 1;
    for (int i = 0; i < r; i++) {
        result = result * (n - i) / (i + 1);
    }
    return result;
}
```

---

## 4. GCD and LCM

This topic covers the Euclidean algorithm for GCD and LCM computation.

**File:** [04_GCD_LCM.md](04_GCD_LCM.md)

**What you will learn:**
- Greatest Common Divisor (GCD)
- Euclidean algorithm (recursive and iterative)
- Extended Euclidean algorithm
- Least Common Multiple (LCM)
- Relationship: LCM(a,b) × GCD(a,b) = a × b
- GCD of multiple numbers

**Key Concepts:**

| Algorithm | Complexity | Description |
|-----------|------------|-------------|
| **Euclidean Algorithm** | O(log n) | GCD(a, b) = GCD(b, a mod b) |
| **Extended Euclidean** | O(log n) | Finds x,y such that ax + by = GCD(a,b) |

**Syntax:**
```cpp
// Euclidean algorithm for GCD
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// LCM using GCD
int lcm(int a, int b) {
    return a / gcd(a, b) * b;  // Divide first to avoid overflow
}
```

---

## 5. Modular Arithmetic

This topic covers arithmetic operations modulo a number.

**File:** [05_Modular_Arithmetic.md](05_Modular_Arithmetic.md)

**What you will learn:**
- Modulo operation properties
- Modular addition, subtraction, multiplication
- Modular exponentiation (fast power)
- Modular inverse (Fermat's theorem, extended GCD)
- Modular arithmetic in competitive programming

**Key Concepts:**

| Operation | Formula |
|-----------|---------|
| **Addition** | (a + b) mod m = (a mod m + b mod m) mod m |
| **Multiplication** | (a × b) mod m = (a mod m × b mod m) mod m |
| **Fast Exponentiation** | a^b mod m in O(log b) |

**Syntax:**
```cpp
// Modular exponentiation
long long modPow(long long a, long long b, long long mod) {
    long long result = 1;
    a = a % mod;
    
    while (b > 0) {
        if (b & 1) {
            result = (result * a) % mod;
        }
        a = (a * a) % mod;
        b >>= 1;
    }
    return result;
}

// Modular inverse using Fermat's theorem (mod must be prime)
long long modInverse(long long a, long long mod) {
    return modPow(a, mod - 2, mod);
}
```

---

## 6. Series and Summations

This topic covers common series and summation formulas.

**File:** [06_Series_and_Summations.md](06_Series_and_Summations.md)

**What you will learn:**
- Arithmetic progression (AP)
- Geometric progression (GP)
- Sum of natural numbers
- Sum of squares and cubes
- Harmonic series
- Fibonacci series

**Key Concepts:**

| Series | Formula | Sum |
|--------|---------|-----|
| **Natural Numbers** | 1 + 2 + ... + n | n(n+1)/2 |
| **Squares** | 1² + 2² + ... + n² | n(n+1)(2n+1)/6 |
| **Cubes** | 1³ + 2³ + ... + n³ | [n(n+1)/2]² |
| **Arithmetic Progression** | a, a+d, a+2d, ... | n/2 × (2a + (n-1)d) |
| **Geometric Progression** | a, ar, ar², ... | a(rⁿ - 1)/(r - 1) |

**Syntax:**
```cpp
// Sum of first n natural numbers
long long sumNatural(int n) {
    return (long long)n * (n + 1) / 2;
}

// Sum of squares
long long sumSquares(int n) {
    return (long long)n * (n + 1) * (2 * n + 1) / 6;
}

// Sum of AP
long long sumAP(long long a, long long d, long long n) {
    return n * (2 * a + (n - 1) * d) / 2;
}
```

---

### Complexity Summary

| Problem Type | Time Complexity | Space Complexity |
|--------------|----------------|------------------|
| Prime Check (Trial) | O(√n) | O(1) |
| Sieve of Eratosthenes | O(n log log n) | O(n) |
| GCD (Euclidean) | O(log n) | O(1) |
| Fast Exponentiation | O(log b) | O(1) |
| Combination (Direct) | O(r) | O(1) |

---

### Common Mathematical Formulas

| Formula | Expression |
|---------|------------|
| **GCD(a,b) × LCM(a,b)** | a × b |
| **Number of divisors** | (e₁+1) × (e₂+1) × ... |
| **Sum of divisors** | (p₁^(e₁+1)-1)/(p₁-1) × ... |
| **nCr modulo prime** | n! × (r!)^-1 × ((n-r)!)^-1 mod p |

---

### Prerequisites

Before starting this section, you should have completed:

- [01. Basics](../../01.%20Basics/README.md) - Basic arithmetic, loops
- [02. Basic Problems](../../02.%20Basic%20Problems/README.md) - Basic problem solving

---

### Sample Mathematical Problem Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Problem: Find the sum of all prime numbers up to n
long long sumOfPrimes(int n) {
    vector<bool> isPrime(n + 1, true);
    isPrime[0] = isPrime[1] = false;
    
    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    
    long long sum = 0;
    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) {
            sum += i;
        }
    }
    return sum;
}

// Problem: Compute GCD of an array of numbers
int gcdArray(vector<int>& arr) {
    int result = arr[0];
    for (int i = 1; i < arr.size(); i++) {
        result = gcd(result, arr[i]);
    }
    return result;
}

int main() {
    cout << "Sum of primes up to 100: " << sumOfPrimes(100) << endl;
    
    vector<int> nums = {24, 36, 48, 60};
    cout << "GCD of array: " << gcdArray(nums) << endl;
    
    return 0;
}
```

---

### Learning Path

```
Level 1: Basic Number Theory
├── Prime Numbers
├── GCD and LCM
└── Prime Factorization

Level 2: Advanced Number Theory
├── Sieve of Eratosthenes
├── Modular Arithmetic
└── Modular Inverse

Level 3: Combinatorics
├── Factorials
├── Permutations
└── Combinations

Level 4: Series and Formulas
├── AP and GP
├── Summation Formulas
└── Binomial Theorem
```

---

### Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Integer overflow in factorial | Use long long or modular arithmetic |
| Forgetting 1 is not prime | Handle n=1 as special case |
| Not using symmetry in nCr | Use min(r, n-r) for efficiency |
| Division before multiplication in LCM | Multiply after division to avoid overflow |
| Negative numbers in modulo | Add mod before modulo operation |

---

### Practice Questions

After completing this section, you should be able to:

1. Check if a number is prime (optimized)
2. Generate all primes up to 1,000,000 using sieve
3. Find prime factors of a number
4. Compute GCD and LCM of two numbers
5. Compute nCr modulo prime
6. Find modular inverse using Fermat's theorem
7. Sum of first n natural numbers (O(1) formula)
8. Compute Fibonacci numbers efficiently
9. Find the number of divisors of a number
10. Compute the sum of divisors of a number

---

### Next Steps

- Go to [01_Number_Theory.md](01_Number_Theory.md) to understand Number Theory Basics.