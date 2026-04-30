# 01_Number_Theory.md

## Number Theory Basics

### Overview

Number theory is a branch of pure mathematics that deals with the properties and relationships of numbers, particularly integers. In programming, number theory provides fundamental concepts and algorithms for solving problems related to divisibility, prime numbers, factors, and modular arithmetic. Understanding number theory is essential for competitive programming and cryptography.

---

### 1. Divisibility

**Definition:** An integer a is divisible by integer b (b ≠ 0) if there exists an integer k such that a = b × k. We write b | a (b divides a).

**Properties of Divisibility:**

| Property | Expression | Example |
|----------|------------|---------|
| **Reflexive** | a \| a | 5 \| 5 |
| **Transitive** | If a \| b and b \| c, then a \| c | 2 \| 4 and 4 \| 12 ⇒ 2 \| 12 |
| **Linearity** | If a \| b and a \| c, then a \| (b × x + c × y) | 3 \| 6 and 3 \| 9 ⇒ 3 \| (6×2 + 9×3) = 3 \| 39 |

**Divisibility Rules:**

| Divisor | Rule | Example |
|---------|------|---------|
| **2** | Last digit is even | 124 → last digit 4 (even) ✓ |
| **3** | Sum of digits divisible by 3 | 123 → 1+2+3=6 ✓ |
| **4** | Last two digits divisible by 4 | 124 → 24 ÷ 4 = 6 ✓ |
| **5** | Last digit is 0 or 5 | 125 → last digit 5 ✓ |
| **6** | Divisible by 2 and 3 | 126 → even and sum=9 ✓ |
| **8** | Last three digits divisible by 8 | 1240 → 240 ÷ 8 = 30 ✓ |
| **9** | Sum of digits divisible by 9 | 126 → 1+2+6=9 ✓ |
| **10** | Last digit is 0 | 120 → last digit 0 ✓ |

---

### 2. Factors and Multiples

**Factors (Divisors):** Numbers that divide a given number evenly.

**Multiples:** Numbers that are divisible by a given number.

**Example with n = 12:**
- Factors: 1, 2, 3, 4, 6, 12
- Multiples: 12, 24, 36, 48, ...

**Finding All Factors (O(√n)):**

```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> getFactors(int n) {
    vector<int> factors;
    
    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            factors.push_back(i);           // Add divisor
            if (i != n / i) {
                factors.push_back(n / i);   // Add paired divisor
            }
        }
    }
    
    sort(factors.begin(), factors.end());
    return factors;
}

int main() {
    int n = 36;
    vector<int> factors = getFactors(n);
    
    cout << "Factors of " << n << ": ";
    for (int f : factors) {
        cout << f << " ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
Factors of 36: 1 2 3 4 6 9 12 18 36
```

---

### 3. Prime Numbers

**Definition:** A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

**First few primes:** 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, ...

**Properties:**
- 2 is the only even prime
- Every prime number (except 2 and 3) is of form 6k ± 1
- There are infinitely many primes

**Composite Numbers:** Numbers greater than 1 that are not prime (have more than two divisors).

**Primality Test (O(√n)):**

```cpp
#include <iostream>
using namespace std;

bool isPrime(int n) {
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
    cout << "Is 17 prime? " << isPrime(17) << endl;
    cout << "Is 25 prime? " << isPrime(25) << endl;
    cout << "Is 97 prime? " << isPrime(97) << endl;
    
    return 0;
}
```

**Output:**
```
Is 17 prime? true
Is 25 prime? false
Is 97 prime? true
```

---

### 4. Prime Factorization

**Fundamental Theorem of Arithmetic:** Every integer greater than 1 can be uniquely represented as a product of prime numbers (ignoring order).

**Example:** 84 = 2² × 3 × 7

**Prime Factorization Algorithm (O(√n)):**

```cpp
#include <iostream>
#include <vector>
#include <map>
using namespace std;

// Method 1: Return vector of prime factors (with repetitions)
vector<int> primeFactors(int n) {
    vector<int> factors;
    
    // Handle factor 2
    while (n % 2 == 0) {
        factors.push_back(2);
        n /= 2;
    }
    
    // Handle odd factors
    for (int i = 3; i * i <= n; i += 2) {
        while (n % i == 0) {
            factors.push_back(i);
            n /= i;
        }
    }
    
    // If remaining n is prime > 1
    if (n > 1) {
        factors.push_back(n);
    }
    
    return factors;
}

// Method 2: Return frequency map of prime factors
map<int, int> primeFactorsWithCount(int n) {
    map<int, int> factors;
    
    for (int i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            factors[i]++;
            n /= i;
        }
    }
    
    if (n > 1) {
        factors[n]++;
    }
    
    return factors;
}

int main() {
    int n = 84;
    
    vector<int> factors = primeFactors(n);
    cout << n << " = ";
    for (int f : factors) {
        cout << f;
        if (f != factors.back()) cout << " × ";
    }
    cout << endl;
    
    map<int, int> factorsMap = primeFactorsWithCount(84);
    cout << n << " = ";
    for (auto [p, exp] : factorsMap) {
        cout << p;
        if (exp > 1) cout << "^" << exp;
        cout << " × ";
    }
    cout << endl;
    
    return 0;
}
```

**Output:**
```
84 = 2 × 2 × 3 × 7
84 = 2^2 × 3 × 7 ×
```

---

### 5. Number of Divisors

If n = p₁^e₁ × p₂^e₂ × ... × p_k^e_k, then:

**Number of divisors:** d(n) = (e₁ + 1) × (e₂ + 1) × ... × (e_k + 1)

**Sum of divisors:** σ(n) = (p₁^(e₁+1) - 1)/(p₁ - 1) × (p₂^(e₂+1) - 1)/(p₂ - 1) × ...

```cpp
#include <iostream>
#include <map>
using namespace std;

int countDivisors(int n) {
    int count = 1;
    
    for (int i = 2; i * i <= n; i++) {
        int exponent = 0;
        while (n % i == 0) {
            exponent++;
            n /= i;
        }
        if (exponent > 0) {
            count *= (exponent + 1);
        }
    }
    
    if (n > 1) {
        count *= 2;
    }
    
    return count;
}

int sumDivisors(int n) {
    int sum = 1;
    
    for (int i = 2; i * i <= n; i++) {
        int exponent = 0;
        int powerSum = 1;
        int currentPower = 1;
        
        while (n % i == 0) {
            exponent++;
            currentPower *= i;
            powerSum += currentPower;
            n /= i;
        }
        
        if (exponent > 0) {
            sum *= powerSum;
        }
    }
    
    if (n > 1) {
        sum *= (1 + n);
    }
    
    return sum;
}

int main() {
    int n = 36;
    cout << "Number of divisors of " << n << ": " << countDivisors(n) << endl;
    cout << "Sum of divisors of " << n << ": " << sumDivisors(n) << endl;
    
    return 0;
}
```

**Output:**
```
Number of divisors of 36: 9
Sum of divisors of 36: 91
```

**Verification:** 36 = 2² × 3²
- Divisors: 1,2,3,4,6,9,12,18,36 → 9 divisors
- Sum of divisors: 1+2+3+4+6+9+12+18+36 = 91

---

### 6. Perfect, Abundant, Deficient Numbers

| Type | Definition | Example |
|------|------------|---------|
| **Perfect** | Sum of proper divisors = n | 6 (1+2+3=6) |
| **Abundant** | Sum of proper divisors > n | 12 (1+2+3+4+6=16 > 12) |
| **Deficient** | Sum of proper divisors < n | 8 (1+2+4=7 < 8) |

```cpp
#include <iostream>
using namespace std;

string classifyNumber(int n) {
    int sum = 1;  // 1 is always a proper divisor
    
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            sum += i;
            if (i != n / i) {
                sum += n / i;
            }
        }
    }
    
    if (sum == n) return "Perfect";
    if (sum > n) return "Abundant";
    return "Deficient";
}

int main() {
    int numbers[] = {6, 12, 8, 28, 30};
    
    for (int n : numbers) {
        cout << n << " is " << classifyNumber(n) << endl;
    }
    
    return 0;
}
```

**Output:**
```
6 is Perfect
12 is Abundant
8 is Deficient
28 is Perfect
30 is Abundant
```

---

### Summary Table

| Concept | Formula | Complexity |
|---------|---------|------------|
| **Factors** | Find all i where n % i == 0 | O(√n) |
| **Prime Test** | Check divisors up to √n | O(√n) |
| **Prime Factorization** | Divide by primes | O(√n) |
| **Number of Divisors** | Π(eᵢ + 1) | O(√n) |
| **Sum of Divisors** | Π(pᵢ^(eᵢ+1)-1)/(pᵢ-1) | O(√n) |

---

### Key Takeaways

1. **Divisibility** is the foundation of number theory
2. **Prime numbers** are building blocks of all integers
3. **Prime factorization** is unique for every integer
4. **Divisors count** can be computed using exponents in prime factorization
5. **Perfect numbers** are rare (only 51 known as of 2024)
6. **Time complexity** of most number theory algorithms is O(√n)

---

### Practice Questions

1. Find all divisors of 100
2. Check if 997 is prime
3. Find prime factorization of 420
4. Count how many divisors 360 has
5. Find the sum of divisors of 100
6. Determine if 496 is a perfect number
7. Find the smallest abundant number
8. Find the greatest common divisor of two numbers

---

### Next Steps

- Go to [02_Prime_Numbers.md](02_Prime_Numbers.md) to understand Prime Numbers and Sieve Algorithms.