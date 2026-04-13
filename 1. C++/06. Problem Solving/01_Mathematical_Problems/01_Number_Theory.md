# Number Theory Fundamentals

## Introduction
Number theory is the branch of mathematics that studies properties of integers. It forms the foundation for many algorithms in computer science, cryptography, and competitive programming. This section covers fundamental concepts and their practical applications.

## Basic Concepts

### 1. Divisibility
An integer `a` divides integer `b` (written as `a | b`) if there exists an integer `k` such that `b = a × k`.

```cpp
class Divisibility {
public:
    // Check if a divides b
    static bool divides(int a, int b) {
        if (a == 0) return b == 0;
        return b % a == 0;
    }
    
    // Count divisors of a number
    static int countDivisors(int n) {
        if (n <= 0) return 0;
        
        int count = 0;
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                count += (i * i == n) ? 1 : 2;
            }
        }
        return count;
    }
    
    // Get all divisors of a number
    static std::vector<int> getDivisors(int n) {
        std::vector<int> divisors;
        if (n <= 0) return divisors;
        
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                divisors.push_back(i);
                if (i != n / i) {
                    divisors.push_back(n / i);
                }
            }
        }
        
        sort(divisors.begin(), divisors.end());
        return divisors;
    }
};
```

### 2. Prime Numbers
A prime number is a natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself.

```cpp
class PrimeNumbers {
public:
    // Check if a number is prime (naive approach)
    static bool isPrimeNaive(int n) {
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
    
    // Sieve of Eratosthenes
    static std::vector<bool> sieveOfEratosthenes(int n) {
        std::vector<bool> isPrime(n + 1, true);
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
    
    // Get all primes up to n
    static std::vector<int> getPrimes(int n) {
        std::vector<bool> isPrime = sieveOfEratosthenes(n);
        std::vector<int> primes;
        
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                primes.push_back(i);
            }
        }
        
        return primes;
    }
};
```

### 3. Prime Factorization
Every integer greater than 1 can be represented uniquely as a product of prime numbers.

```cpp
class PrimeFactorization {
public:
    // Get prime factorization of a number
    static std::vector<std::pair<int, int>> primeFactorization(int n) {
        std::vector<std::pair<int, int>> factors;
        
        // Handle 2 separately
        if (n % 2 == 0) {
            int count = 0;
            while (n % 2 == 0) {
                n /= 2;
                count++;
            }
            factors.push_back({2, count});
        }
        
        // Handle odd divisors
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) {
                int count = 0;
                while (n % i == 0) {
                    n /= i;
                    count++;
                }
                factors.push_back({i, count});
            }
        }
        
        // If remaining n is a prime
        if (n > 2) {
            factors.push_back({n, 1});
        }
        
        return factors;
    }
    
    // Get number of prime factors (with multiplicity)
    static int countPrimeFactors(int n) {
        auto factors = primeFactorization(n);
        int count = 0;
        for (auto& factor : factors) {
            count += factor.second;
        }
        return count;
    }
    
    // Get number of distinct prime factors
    static int countDistinctPrimeFactors(int n) {
        return primeFactorization(n).size();
    }
};
```

## Greatest Common Divisor (GCD)

### Euclidean Algorithm
The GCD of two numbers is the largest number that divides both of them.

```cpp
class GCD {
public:
    // Euclidean algorithm (iterative)
    static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return abs(a);
    }
    
    // Euclidean algorithm (recursive)
    static int gcdRecursive(int a, int b) {
        if (b == 0) return abs(a);
        return gcdRecursive(b, a % b);
    }
    
    // GCD of multiple numbers
    static int gcdMultiple(const std::vector<int>& numbers) {
        if (numbers.empty()) return 0;
        
        int result = numbers[0];
        for (size_t i = 1; i < numbers.size(); i++) {
            result = gcd(result, numbers[i]);
            if (result == 1) break; // Early termination
        }
        return result;
    }
};
```

### Extended Euclidean Algorithm
Finds integers x and y such that: ax + by = gcd(a, b)

```cpp
class ExtendedGCD {
public:
    // Extended Euclidean algorithm
    static std::tuple<int, int, int> extendedGCD(int a, int b) {
        if (b == 0) {
            return {a, 1, 0};
        }
        
        auto [gcd, x1, y1] = extendedGCD(b, a % b);
        int x = y1;
        int y = x1 - (a / b) * y1;
        
        return {gcd, x, y};
    }
    
    // Find modular inverse of a under modulo m
    static int modInverse(int a, int m) {
        auto [gcd, x, y] = extendedGCD(a, m);
        
        if (gcd != 1) {
            return -1; // Inverse doesn't exist
        }
        
        return (x % m + m) % m;
    }
};
```

## Least Common Multiple (LCM)

```cpp
class LCM {
public:
    // LCM of two numbers
    static int lcm(int a, int b) {
        if (a == 0 || b == 0) return 0;
        return abs(a / GCD::gcd(a, b) * b);
    }
    
    // LCM of multiple numbers
    static long long lcmMultiple(const std::vector<int>& numbers) {
        if (numbers.empty()) return 0;
        
        long long result = numbers[0];
        for (size_t i = 1; i < numbers.size(); i++) {
            result = lcm(result, numbers[i]);
        }
        return result;
    }
};
```

## Number Theoretic Functions

### Euler's Totient Function φ(n)
Counts the number of integers up to n that are relatively prime to n.

```cpp
class EulerTotient {
public:
    // Calculate φ(n) for a single number
    static int phi(int n) {
        if (n == 0) return 0;
        
        int result = n;
        auto factors = PrimeFactorization::primeFactorization(n);
        
        for (auto& factor : factors) {
            int p = factor.first;
            result -= result / p;
        }
        
        return result;
    }
    
    // Calculate φ for all numbers up to n using sieve
    static std::vector<int> phiSieve(int n) {
        std::vector<int> phi(n + 1);
        
        for (int i = 0; i <= n; i++) {
            phi[i] = i;
        }
        
        for (int i = 2; i <= n; i++) {
            if (phi[i] == i) { // i is prime
                for (int j = i; j <= n; j += i) {
                    phi[j] -= phi[j] / i;
                }
            }
        }
        
        return phi;
    }
};
```

### Divisor Functions

```cpp
class DivisorFunctions {
public:
    // Sum of divisors of n
    static int sumOfDivisors(int n) {
        if (n <= 0) return 0;
        
        int sum = 0;
        auto factors = PrimeFactorization::primeFactorization(n);
        
        sum = 1;
        for (auto& factor : factors) {
            int p = factor.first;
            int exp = factor.second;
            
            int term = (pow(p, exp + 1) - 1) / (p - 1);
            sum *= term;
        }
        
        return sum;
    }
    
    // Sum of proper divisors (excluding the number itself)
    static int sumOfProperDivisors(int n) {
        return sumOfDivisors(n) - n;
    }
    
    // Check if number is perfect (sum of proper divisors equals the number)
    static bool isPerfect(int n) {
        return n > 1 && sumOfProperDivisors(n) == n;
    }
};
```

## Diophantine Equations

### Linear Diophantine Equations
Equations of the form ax + by = c where a, b, c are integers.

```cpp
class DiophantineEquations {
public:
    // Solve ax + by = c
    // Returns whether solution exists and one solution
    static std::pair<bool, std::pair<int, int>> solveLinearDiophantine(int a, int b, int c) {
        auto [gcd, x, y] = ExtendedGCD::extendedGCD(a, b);
        
        if (c % gcd != 0) {
            return {false, {0, 0}}; // No solution
        }
        
        int factor = c / gcd;
        int x0 = x * factor;
        int y0 = y * factor;
        
        return {true, {x0, y0}};
    }
    
    // Get all solutions of ax + by = c
    static std::vector<std::pair<int, int>> getAllSolutions(int a, int b, int c, int limit) {
        auto [hasSolution, base] = solveLinearDiophantine(a, b, c);
        if (!hasSolution) return {};
        
        auto [gcd, x, y] = ExtendedGCD::extendedGCD(a, b);
        int factor = c / gcd;
        
        std::vector<std::pair<int, int>> solutions;
        int x0 = x * factor;
        int y0 = y * factor;
        
        // General solution: x = x0 + (b/gcd)*t, y = y0 - (a/gcd)*t
        for (int t = -limit; t <= limit; t++) {
            int x_sol = x0 + (b / gcd) * t;
            int y_sol = y0 - (a / gcd) * t;
            solutions.push_back({x_sol, y_sol});
        }
        
        return solutions;
    }
};
```

## Advanced Number Theory

### Chinese Remainder Theorem
Solves systems of congruences.

```cpp
class ChineseRemainderTheorem {
public:
    // Solve system: x ≡ a1 (mod m1), x ≡ a2 (mod m2), ...
    // Returns solution modulo M where M = lcm(m1, m2, ...)
    static std::pair<long long, long long> solveCRT(
        const std::vector<int>& remainders, 
        const std::vector<int>& moduli) {
        
        if (remainders.size() != moduli.size()) {
            return {-1, -1}; // Invalid input
        }
        
        long long result = remainders[0];
        long long current_mod = moduli[0];
        
        for (size_t i = 1; i < remainders.size(); i++) {
            long long a = remainders[i];
            long long m = moduli[i];
            
            auto [gcd, x, y] = ExtendedGCD::extendedGCD(current_mod, m);
            
            if ((a - result) % gcd != 0) {
                return {-1, -1}; // No solution
            }
            
            long long lcm = current_mod / gcd * m;
            long long temp = ((a - result) / gcd * x % (m / gcd) + m / gcd) % (m / gcd);
            
            result = result + current_mod * temp;
            result %= lcm;
            if (result < 0) result += lcm;
            
            current_mod = lcm;
        }
        
        return {result, current_mod};
    }
};
```

## Practical Applications

### 1. Cryptography
```cpp
class CryptographyApplications {
public:
    // RSA key generation (simplified)
    static std::pair<int, int> generateRSAKeys(int p, int q) {
        if (!PrimeNumbers::isPrimeNaive(p) || !PrimeNumbers::isPrimeNaive(q)) {
            return {-1, -1}; // Not primes
        }
        
        int n = p * q;
        int phi = (p - 1) * (q - 1);
        
        // Choose e such that 1 < e < phi and gcd(e, phi) = 1
        int e = 65537; // Common choice
        if (GCD::gcd(e, phi) != 1) {
            // Find another e
            for (e = 3; e < phi; e += 2) {
                if (GCD::gcd(e, phi) == 1) break;
            }
        }
        
        int d = ExtendedGCD::modInverse(e, phi);
        
        return {e, d}; // {public exponent, private exponent}
    }
};
```

### 2. Problem Solving Examples

```cpp
class NumberTheoryProblems {
public:
    // Find largest prime factor
    static int largestPrimeFactor(int n) {
        auto factors = PrimeFactorization::primeFactorization(n);
        if (factors.empty()) return -1;
        
        return factors.back().first;
    }
    
    // Check if two numbers are coprime
    static bool areCoprime(int a, int b) {
        return GCD::gcd(a, b) == 1;
    }
    
    // Find smallest number with exactly n divisors
    static long long smallestNumberWithNDivisors(int n) {
        // This is a complex problem - simplified version
        std::vector<int> primes = PrimeNumbers::getPrimes(50);
        
        long long result = 1;
        int remaining = n;
        
        for (size_t i = 0; i < primes.size() && remaining > 1; i++) {
            int exponent = 1;
            while (remaining % (exponent + 1) == 0) {
                remaining /= (exponent + 1);
                result *= pow(primes[i], exponent);
                exponent++;
            }
        }
        
        return remaining == 1 ? result : -1;
    }
};
```

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Prime Check | O(√n) | O(1) |
| Sieve of Eratosthenes | O(n log log n) | O(n) |
| Prime Factorization | O(√n) | O(log n) |
| GCD (Euclidean) | O(log min(a,b)) | O(1) |
| Extended GCD | O(log min(a,b)) | O(1) |
| Euler's Totient | O(√n) | O(log n) |
| CRT | O(k log M) | O(1) |

## Best Practices

1. **Use Long Long**: For large numbers to avoid overflow
2. **Precompute**: Use sieves for multiple queries
3. **Handle Edge Cases**: Zero, one, and negative numbers
4. **Modular Arithmetic**: Apply consistently in calculations
5. **Optimization**: Use mathematical properties to reduce complexity

## Summary

Number theory provides essential tools for algorithmic problem-solving. Understanding these concepts enables efficient solutions to many computational problems and forms the foundation for advanced algorithms in cryptography and computer science.
---

## Next Step

- Go to [02_Prime_Numbers.md](02_Prime_Numbers.md) to continue with Prime Numbers.
