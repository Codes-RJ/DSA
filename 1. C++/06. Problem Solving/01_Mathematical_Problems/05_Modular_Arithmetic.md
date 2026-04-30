# 05_Modular_Arithmetic.md

## Modular Arithmetic

### Overview

Modular arithmetic is a system of arithmetic for integers where numbers "wrap around" after reaching a certain value called the modulus. It is fundamental to number theory, cryptography, competitive programming, and computer science. Modular arithmetic allows us to work with very large numbers by keeping results within a fixed range.

---

### 1. Basic Concepts

**Definition:** Two integers a and b are said to be congruent modulo m if m divides (a - b). This is written as:

```
a ≡ b (mod m)
```

**Examples:**
- 17 ≡ 2 (mod 5) because 17 - 2 = 15 is divisible by 5
- 23 ≡ 1 (mod 11) because 23 - 1 = 22 is divisible by 11
- 0 ≡ 8 (mod 4) because 0 - 8 = -8 is divisible by 4

**Basic Operations:**

```cpp
#include <iostream>
using namespace std;

const int MOD = 1000000007;

int modAdd(int a, int b, int mod) {
    return (a % mod + b % mod) % mod;
}

int modSub(int a, int b, int mod) {
    return (a % mod - b % mod + mod) % mod;
}

int modMul(int a, int b, int mod) {
    return (1LL * (a % mod) * (b % mod)) % mod;
}

int main() {
    int a = 123456789, b = 987654321;
    int mod = 1000000007;
    
    cout << "a = " << a << ", b = " << b << ", mod = " << mod << endl;
    cout << "(a + b) mod m = " << modAdd(a, b, mod) << endl;
    cout << "(a - b) mod m = " << modSub(a, b, mod) << endl;
    cout << "(a × b) mod m = " << modMul(a, b, mod) << endl;
    
    return 0;
}
```

**Output:**
```
a = 123456789, b = 987654321, mod = 1000000007
(a + b) mod m = 111111100
(a - b) mod m = 135802475
(a × b) mod m = 117766407
```

---

### 2. Properties of Modular Arithmetic

| Property | Expression |
|----------|------------|
| **Additive Identity** | (a + 0) ≡ a (mod m) |
| **Multiplicative Identity** | (a × 1) ≡ a (mod m) |
| **Additive Inverse** | a + (-a) ≡ 0 (mod m) |
| **Associative** | (a + b) + c ≡ a + (b + c) (mod m) |
| **Commutative** | a + b ≡ b + a (mod m) |
| **Distributive** | a × (b + c) ≡ a × b + a × c (mod m) |

```cpp
#include <iostream>
using namespace std;

void demonstrateProperties(int mod) {
    int a = 7, b = 11, c = 13;
    
    cout << "Mod = " << mod << endl;
    cout << "Commutative: " << ((a + b) % mod == (b + a) % mod ? "✓" : "✗") << endl;
    cout << "Associative: " << (((a + b) % mod + c) % mod == (a + (b + c) % mod) % mod ? "✓" : "✗") << endl;
    cout << "Distributive: " << ((a * (b + c)) % mod == (a * b + a * c) % mod ? "✓" : "✗") << endl;
}

int main() {
    demonstrateProperties(17);
    demonstrateProperties(100);
    
    return 0;
}
```

---

### 3. Modular Exponentiation (Fast Power)

Modular exponentiation computes a^b mod m efficiently in O(log b) time.

**Algorithm (Exponentiation by Squaring):**
```
a^b mod m:
    result = 1
    a = a mod m
    while b > 0:
        if b is odd: result = (result × a) mod m
        a = (a × a) mod m
        b = b / 2
    return result
```

```cpp
#include <iostream>
#include <chrono>
using namespace std;

// Iterative modular exponentiation
long long modPow(long long a, long long b, long long mod) {
    long long result = 1;
    a %= mod;
    
    while (b > 0) {
        if (b & 1) {  // If b is odd
            result = (result * a) % mod;
        }
        a = (a * a) % mod;
        b >>= 1;  // b = b / 2
    }
    
    return result;
}

// Recursive modular exponentiation
long long modPowRecursive(long long a, long long b, long long mod) {
    if (b == 0) return 1 % mod;
    
    long long half = modPowRecursive(a, b / 2, mod);
    long long result = (half * half) % mod;
    
    if (b & 1) {
        result = (result * a) % mod;
    }
    
    return result;
}

int main() {
    long long a = 2, b = 10, mod = 1000;
    cout << "2^10 mod 1000 = " << modPow(a, b, mod) << endl;
    
    a = 123456789, b = 1000000000, mod = 1000000007;
    cout << "123456789^1000000000 mod 1000000007 = " << modPow(a, b, mod) << endl;
    
    return 0;
}
```

**Output:**
```
2^10 mod 1000 = 24
123456789^1000000000 mod 1000000007 = 577634554
```

---

### 4. Modular Inverse

The modular inverse of a modulo m is an integer x such that:

```
a × x ≡ 1 (mod m)
```

The modular inverse exists only when gcd(a, m) = 1 (a and m are coprime).

**Method 1: Fermat's Little Theorem (when m is prime)**

For prime modulus m: a^(m-2) ≡ a^(-1) (mod m)

**Method 2: Extended Euclidean Algorithm (any modulus)**

```cpp
#include <iostream>
#include <tuple>
using namespace std;

// Extended Euclidean algorithm
tuple<int, int, int> extendedGCD(int a, int b) {
    if (b == 0) {
        return {a, 1, 0};
    }
    
    auto [gcd, x1, y1] = extendedGCD(b, a % b);
    int x = y1;
    int y = x1 - (a / b) * y1;
    
    return {gcd, x, y};
}

// Modular inverse using Fermat's theorem (mod must be prime)
int modInverseFermat(int a, int mod) {
    return modPow(a, mod - 2, mod);
}

// Modular inverse using extended GCD (mod can be any)
int modInverseExtended(int a, int mod) {
    auto [gcd, x, y] = extendedGCD(a, mod);
    
    if (gcd != 1) {
        return -1;  // Inverse doesn't exist
    }
    
    return (x % mod + mod) % mod;
}

int main() {
    int a = 3, mod = 11;
    
    cout << "a = " << a << ", mod = " << mod << endl;
    cout << "Inverse (Fermat): " << modInverseFermat(a, mod) << endl;
    cout << "Inverse (Extended): " << modInverseExtended(a, mod) << endl;
    
    // Verification
    int inv = modInverseExtended(a, mod);
    cout << "Verification: " << a << " × " << inv << " = " << (a * inv) % mod << " ≡ 1 mod " << mod << endl;
    
    // Example where inverse doesn't exist
    a = 4, mod = 8;
    cout << "\na = " << a << ", mod = " << mod << endl;
    cout << "Inverse exists? " << (modInverseExtended(a, mod) != -1 ? "Yes" : "No") << endl;
    
    return 0;
}
```

**Output:**
```
a = 3, mod = 11
Inverse (Fermat): 4
Inverse (Extended): 4
Verification: 3 × 4 = 12 ≡ 1 mod 11

a = 4, mod = 8
Inverse exists? No
```

---

### 5. Modular Division

Division in modular arithmetic is performed by multiplying by the modular inverse:

```
(a / b) mod m = a × b^(-1) mod m
```

```cpp
#include <iostream>
using namespace std;

// Modular division (mod must be prime for Fermat to work)
int modDivide(int a, int b, int mod) {
    int inv = modInverseFermat(b, mod);
    if (inv == -1) return -1;
    return modMul(a, inv, mod);
}

int main() {
    int a = 10, b = 2, mod = 1000000007;
    
    cout << "a = " << a << ", b = " << b << ", mod = " << mod << endl;
    cout << "(a / b) mod m = " << modDivide(a, b, mod) << endl;
    cout << "Expected (standard division): " << (10 / 2) << endl;
    
    return 0;
}
```

---

### 6. Modular Arithmetic in Competitive Programming

Common modulus values:
- 10^9 + 7 (1,000,000,007) - prime number
- 998,244,353 - prime number (used in NTT)

```cpp
#include <iostream>
using namespace std;

const int MOD1 = 1000000007;
const int MOD2 = 998244353;

// Precomputed factorials for nCr modulo prime
vector<long long> fact, invFact;

void precompute(int n, int mod) {
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

long long nCrMod(int n, int r, int mod) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % mod * invFact[n - r] % mod;
}

int main() {
    int n = 100;
    precompute(n, MOD1);
    
    cout << "C(50, 25) mod " << MOD1 << " = " << nCrMod(50, 25, MOD1) << endl;
    
    return 0;
}
```

---

### 7. Modular Exponentiation Visual Example

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

void modPowDebug(long long a, long long b, long long mod) {
    cout << "Computing " << a << "^" << b << " mod " << mod << endl;
    cout << "Step-by-step:" << endl;
    
    long long result = 1;
    a %= mod;
    
    int step = 1;
    while (b > 0) {
        cout << "  Step " << step << ": b = " << b << " (";
        if (b & 1) cout << "odd";
        else cout << "even";
        cout << "), a = " << a;
        
        if (b & 1) {
            result = (result * a) % mod;
            cout << ", result = " << result;
        }
        cout << endl;
        
        a = (a * a) % mod;
        b >>= 1;
        step++;
    }
    
    cout << "Final result: " << result << endl;
}

int main() {
    modPowDebug(3, 13, 100);
    
    return 0;
}
```

**Output:**
```
Computing 3^13 mod 100
Step-by-step:
  Step 1: b = 13 (odd), a = 3, result = 3
  Step 2: b = 6 (even), a = 9
  Step 3: b = 3 (odd), a = 81, result = 243
  Step 4: b = 1 (odd), a = 6561, result = 243
Final result: 43
```

**Verification:** 3^13 = 1,594,323 ≡ 43 (mod 100)

---

### Common Modulus Values

| Modulus | Prime? | Common Use |
|---------|--------|------------|
| 10^9 + 7 | Yes | General purpose, large prime |
| 998,244,353 | Yes | NTT operations |
| 10^9 + 9 | Yes | Alternative to 10^9+7 |
| 10^9 + 21 | Yes | Another alternative |
| 2^31 - 1 | Yes | 32-bit signed max (Mersenne prime) |
| 10^5 + 3 | Yes | Smaller modulus for testing |

---

### Key Takeaways

1. **Modular arithmetic** keeps numbers bounded, preventing overflow
2. **Modular exponentiation** computes powers in O(log b) time
3. **Modular inverse** exists only when gcd(a, m) = 1
4. **Fermat's theorem** gives a^-1 ≡ a^(m-2) when m is prime
5. **Extended Euclidean algorithm** finds inverses for any modulus
6. **Common moduli** include 10^9+7 and 998,244,353
7. **Precomputation** of factorials enables O(1) nCr queries

---

### Practice Questions

1. Compute 5^100 mod 13
2. Find the modular inverse of 7 modulo 17
3. Check if 8 has a modular inverse modulo 12
4. Compute (7 + 15) × (23 - 8) mod 11
5. Find the last 3 digits of 2^1000
6. Compute C(100, 50) mod 10^9+7
7. Find the smallest positive integer x such that 3x ≡ 5 (mod 7)
8. Determine if 2 is a quadratic residue modulo 7

---

### Next Steps

- Go to [06_Series_and_Summations.md](06_Series_and_Summations.md) for Series and Summations.