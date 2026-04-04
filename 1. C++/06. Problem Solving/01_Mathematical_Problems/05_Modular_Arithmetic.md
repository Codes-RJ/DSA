# Modular Arithmetic

## Introduction
Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" when reaching a certain value, called the **modulus**.

## Basic Properties
1. `(a + b) % m = ((a % m) + (b % m)) % m`
2. `(a - b) % m = ((a % m) - (b % m) + m) % m`
3. `(a * b) % m = ((a % m) * (b % m)) % m`
4. `(a / b) % m = (a * modular_inverse(b)) % m`

## Modular Exponentiation (Binary Exponentiation)
Used to calculate `(a ^ b) % m` in O(log b) time.

```cpp
long long power(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return res;
}
```

## Modular Inverse
The modular multiplicative inverse of `a` modulo `m` is an integer `x` such that `(a * x) % m = 1`.
It exists ONLY if `gcd(a, m) = 1`.

### Calculation via Fermat's Little Theorem
If `m` is prime: `x = a^(m-2) % m`.
```cpp
long long modInverse(long long n, long long m) {
    return power(n, m - 2, m);
}
```

### Calculation via Extended Euclidean Algorithm
Works for any `m` where `gcd(a, m) = 1`.

## Common Modulo
In competitive programming, the most common modulus is **10^9 + 7** because:
1. It is a large prime number.
2. It fits comfortably in an `int`.
3. Its square fits in a `long long` for intermediate calculations.

## Applications
- Cryptography (RSA).
- Hash functions.
- Combinatorics calculations for large numbers.
- Preventing integer overflow.
