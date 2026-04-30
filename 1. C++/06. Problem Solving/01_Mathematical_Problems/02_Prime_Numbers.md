# 02_Prime_Numbers.md

## Prime Numbers and Sieve Algorithms

### Overview

Prime numbers are fundamental building blocks in number theory. Efficiently generating and testing primes is crucial for many algorithms in cryptography, number theory, and competitive programming. This topic covers various algorithms for primality testing and prime number generation, ranging from simple trial division to advanced sieves.

---

### 1. Primality Testing

**Definition:** Primality testing determines whether a given number is prime.

#### Method 1: Trial Division (O(√n))

The simplest method checks divisibility by all numbers from 2 to √n.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

bool isPrimeTrial(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    cout << boolalpha;
    cout << "Is 17 prime? " << isPrimeTrial(17) << endl;
    cout << "Is 97 prime? " << isPrimeTrial(97) << endl;
    cout << "Is 1000000007 prime? " << isPrimeTrial(1000000007) << endl;
    
    return 0;
}
```

**Output:**
```
Is 17 prime? true
Is 97 prime? true
Is 1000000007 prime? true
```

**Time Complexity:** O(√n) - Suitable for n ≤ 10^12

---

#### Method 2: Miller-Rabin Probabilistic Test

Miller-Rabin is a probabilistic primality test that is very fast for large numbers. It has a small probability of error, but can be made deterministic for specific ranges.

**Key Concept:** Based on the fact that for a prime p, a^(p-1) ≡ 1 (mod p) (Fermat's Little Theorem) and certain square root properties.

```cpp
#include <iostream>
#include <random>
using namespace std;

long long modMul(long long a, long long b, long long mod) {
    long long result = 0;
    a %= mod;
    while (b > 0) {
        if (b & 1) result = (result + a) % mod;
        a = (a * 2) % mod;
        b >>= 1;
    }
    return result;
}

long long modPow(long long a, long long b, long long mod) {
    long long result = 1;
    a %= mod;
    while (b > 0) {
        if (b & 1) result = modMul(result, a, mod);
        a = modMul(a, a, mod);
        b >>= 1;
    }
    return result;
}

bool millerRabin(long long n, int iterations = 5) {
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0) return false;
    
    // Write n-1 as d * 2^r
    long long d = n - 1;
    int r = 0;
    while (d % 2 == 0) {
        d /= 2;
        r++;
    }
    
    random_device rd;
    mt19937_64 gen(rd());
    uniform_int_distribution<long long> dist(2, n - 2);
    
    for (int i = 0; i < iterations; i++) {
        long long a = dist(gen);
        long long x = modPow(a, d, n);
        
        if (x == 1 || x == n - 1) continue;
        
        bool composite = true;
        for (int j = 0; j < r - 1; j++) {
            x = modMul(x, x, n);
            if (x == n - 1) {
                composite = false;
                break;
            }
        }
        
        if (composite) return false;
    }
    
    return true;
}

int main() {
    cout << boolalpha;
    cout << "Is 1000000007 prime? " << millerRabin(1000000007) << endl;
    cout << "Is 1000000009 prime? " << millerRabin(1000000009) << endl;
    cout << "Is 999999937 prime? " << millerRabin(999999937) << endl;
    
    return 0;
}
```

**Output:**
```
Is 1000000007 prime? true
Is 1000000009 prime? true
Is 999999937 prime? true
```

**Time Complexity:** O(k × log³ n) where k is number of iterations

---

### 2. Sieve of Eratosthenes

The Sieve of Eratosthenes generates all prime numbers up to a given limit efficiently.

**Algorithm:**
```
1. Create a boolean array isPrime[0..n] initialized to true
2. Set isPrime[0] = isPrime[1] = false
3. For i from 2 to √n:
     if isPrime[i] is true:
         mark all multiples of i as false
4. Remaining true indices are primes
```

```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

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

vector<int> getPrimes(int n) {
    vector<bool> isPrime = sieve(n);
    vector<int> primes;
    
    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) {
            primes.push_back(i);
        }
    }
    
    return primes;
}

int main() {
    int n = 100;
    vector<int> primes = getPrimes(n);
    
    cout << "Primes up to " << n << ": ";
    for (int p : primes) {
        cout << p << " ";
    }
    cout << endl;
    cout << "Count: " << primes.size() << endl;
    
    return 0;
}
```

**Output:**
```
Primes up to 100: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
Count: 25
```

**Time Complexity:** O(n log log n)
**Space Complexity:** O(n)

---

### 3. Sieve of Eratosthenes Optimizations

#### Optimization 1: Start from i²

Instead of starting from 2i, start from i² because smaller multiples are already marked by smaller primes.

```cpp
for (int j = i * i; j <= n; j += i) {
    isPrime[j] = false;
}
```

#### Optimization 2: Only Odd Numbers

Skip even numbers by storing only odd indices.

```cpp
vector<bool> sieveOptimized(int n) {
    if (n < 2) return {};
    
    // isPrime[i] represents number (2*i + 1)
    vector<bool> isPrime((n + 1) / 2, true);
    
    // 1 is not prime (represents 1 in odd representation)
    isPrime[0] = false;
    
    for (int i = 1; i * i < n; i++) {
        if (isPrime[i]) {
            int num = 2 * i + 1;
            for (int j = num * num; j <= n; j += 2 * num) {
                isPrime[(j - 1) / 2] = false;
            }
        }
    }
    
    return isPrime;
}
```

---

### 4. Segmented Sieve

The segmented sieve finds primes in a range [L, R] where R can be very large (e.g., up to 10^12) but the range length (R-L+1) is small.

**Key Idea:**
1. Generate all primes up to √R using regular sieve
2. Use these primes to mark composites in the range [L, R]

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <cstring>
using namespace std;

vector<int> simpleSieve(int limit) {
    vector<bool> isPrime(limit + 1, true);
    isPrime[0] = isPrime[1] = false;
    
    for (int i = 2; i * i <= limit; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= limit; j += i) {
                isPrime[j] = false;
            }
        }
    }
    
    vector<int> primes;
    for (int i = 2; i <= limit; i++) {
        if (isPrime[i]) {
            primes.push_back(i);
        }
    }
    
    return primes;
}

vector<int> segmentedSieve(long long L, long long R) {
    vector<int> primes = simpleSieve(sqrt(R));
    
    // isPrimeRange[i] represents number (L + i)
    vector<bool> isPrimeRange(R - L + 1, true);
    
    for (int p : primes) {
        // Find the first multiple of p in [L, R]
        long long start = max((long long)p * p, ((L + p - 1) / p) * p);
        
        for (long long j = start; j <= R; j += p) {
            isPrimeRange[j - L] = false;
        }
    }
    
    vector<int> result;
    for (long long i = L; i <= R; i++) {
        if (isPrimeRange[i - L] && i > 1) {
            result.push_back(i);
        }
    }
    
    return result;
}

int main() {
    long long L = 1000000000000LL;
    long long R = 1000000000100LL;
    
    vector<int> primes = segmentedSieve(L, R);
    
    cout << "Primes in range [" << L << ", " << R << "]:" << endl;
    for (int p : primes) {
        cout << p << " ";
    }
    cout << endl;
    cout << "Count: " << primes.size() << endl;
    
    return 0;
}
```

**Output:**
```
Primes in range [1000000000000, 1000000000100]:
1000000000039 1000000000061 1000000000063 1000000000091 1000000000093 
Count: 5
```

**Time Complexity:** O((R-L+1) × log log R + √R log log √R)

---

### 5. Sieve of Sundaram

The Sieve of Sundaram generates all odd primes up to n.

**Key Insight:** All odd composites can be expressed as (i + j + 2ij) for positive integers i, j.

```cpp
vector<int> sieveSundaram(int n) {
    // Generate odds up to n
    int limit = (n - 1) / 2;
    vector<bool> marked(limit + 1, false);
    
    for (int i = 1; i <= limit; i++) {
        for (int j = i; i + j + 2 * i * j <= limit; j++) {
            marked[i + j + 2 * i * j] = true;
        }
    }
    
    vector<int> primes;
    if (n >= 2) primes.push_back(2);
    
    for (int i = 1; i <= limit; i++) {
        if (!marked[i]) {
            primes.push_back(2 * i + 1);
        }
    }
    
    return primes;
}
```

---

### 6. Prime Number Theorem

The Prime Number Theorem describes the asymptotic distribution of prime numbers.

| n | π(n) (number of primes ≤ n) | Approximation n/ln(n) |
|---|-----------------------------|----------------------|
| 10 | 4 | 4.3 |
| 100 | 25 | 21.7 |
| 1000 | 168 | 144.8 |
| 10,000 | 1,229 | 1,085.7 |
| 100,000 | 9,592 | 8,685.9 |
| 1,000,000 | 78,498 | 72,382.4 |

```cpp
int approximatePrimeCount(int n) {
    return (int)(n / log(n));
}
```

---

### Complexity Summary

| Algorithm | Time Complexity | Space Complexity | Use Case |
|-----------|----------------|------------------|----------|
| **Trial Division** | O(√n) | O(1) | Single number (n ≤ 10^12) |
| **Miller-Rabin** | O(k log³ n) | O(1) | Large numbers (n ≤ 10^18) |
| **Sieve of Eratosthenes** | O(n log log n) | O(n) | All primes ≤ n (n ≤ 10^7) |
| **Segmented Sieve** | O((R-L) + √R log log R) | O(R-L) | Prime range (R up to 10^12) |
| **Sieve of Sundaram** | O(n log n) | O(n) | Alternative to Eratosthenes |

---

### Key Takeaways

1. **Trial division** is simple but slow for large numbers
2. **Miller-Rabin** is probabilistic but fast for very large numbers
3. **Sieve of Eratosthenes** is most efficient for generating all primes up to a limit
4. **Segmented sieve** handles large ranges where regular sieve is memory-intensive
5. **Sieve optimizations** (starting from i², odd-only) improve constant factors
6. **Prime number theorem** gives approximation for prime distribution

---

### Practice Questions

1. Write a function to check if a number is prime for n up to 10^12
2. Generate all primes up to 1,000,000 using Sieve of Eratosthenes
3. Find the 10,000th prime number
4. Count how many primes exist between 10^9 and 10^9 + 1000
5. Find the smallest prime greater than 1,000,000,000
6. Implement a segmented sieve for large ranges
7. Find all prime factors of a number up to 10^12
8. Determine if a 20-digit number is prime using Miller-Rabin

---

### Next Steps

- Go to [03_Factorial_and_Combinatorics.md](03_Factorial_and_Combinatorics.md) for Factorial and Combinatorics.