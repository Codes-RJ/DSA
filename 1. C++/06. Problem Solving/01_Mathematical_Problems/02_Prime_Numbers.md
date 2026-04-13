# Prime Numbers

## Introduction
Prime numbers are natural numbers greater than 1 that have exactly two distinct positive divisors: 1 and themselves. They are fundamental building blocks in number theory and have numerous applications in cryptography, computer science, and mathematics.

## Prime Number Properties

### Basic Properties
- **2** is the only even prime number
- **All primes greater than 2 are odd**
- **Prime numbers are infinite** (proved by Euclid)
- **Fundamental Theorem of Arithmetic**: Every integer > 1 can be uniquely expressed as a product of primes

### Prime Distribution
- **Prime Number Theorem**: π(n) ≈ n/ln(n), where π(n) is the number of primes ≤ n
- **Twin Primes**: Prime pairs (p, p+2) like (3,5), (5,7), (11,13)
- **Mersenne Primes**: Primes of the form 2^p - 1 where p is prime

## Prime Number Algorithms

### 1. Basic Prime Checking
```cpp
class PrimeChecker {
public:
    // Naive prime checking
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
    
    // Optimized prime checking
    static bool isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0) return false;
        if (n % 3 == 0) return false;
        
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
    
    // Miller-Rabin primality test (for large numbers)
    static bool isPrimeMillerRabin(long long n, int k = 5) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0) return false;
        
        // Write n-1 as d * 2^s
        long long d = n - 1;
        int s = 0;
        while (d % 2 == 0) {
            d /= 2;
            s++;
        }
        
        // Test k times
        for (int i = 0; i < k; i++) {
            long long a = 2 + rand() % (n - 3);
            long long x = modPow(a, d, n);
            
            if (x == 1 || x == n - 1) continue;
            
            bool composite = true;
            for (int j = 0; j < s - 1; j++) {
                x = modPow(x, 2, n);
                if (x == n - 1) {
                    composite = false;
                    break;
                }
            }
            
            if (composite) return false;
        }
        
        return true;
    }
    
private:
    static long long modPow(long long base, long long exp, long long mod) {
        long long result = 1;
        base %= mod;
        
        while (exp > 0) {
            if (exp & 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }
        
        return result;
    }
};
```

### 2. Sieve of Eratosthenes
```cpp
class SieveOfEratosthenes {
public:
    // Basic sieve implementation
    static std::vector<bool> sieve(int n) {
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
        std::vector<bool> isPrime = sieve(n);
        std::vector<int> primes;
        
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                primes.push_back(i);
            }
        }
        
        return primes;
    }
    
    // Optimized sieve with only odd numbers
    static std::vector<int> getPrimesOptimized(int n) {
        if (n < 2) return {};
        
        std::vector<int> primes = {2};
        std::vector<bool> isPrime((n + 1) / 2, true);
        
        for (int i = 3; i * i <= n; i += 2) {
            if (isPrime[i / 2]) {
                for (int j = i * i; j <= n; j += 2 * i) {
                    isPrime[j / 2] = false;
                }
            }
        }
        
        for (int i = 3; i <= n; i += 2) {
            if (isPrime[i / 2]) {
                primes.push_back(i);
            }
        }
        
        return primes;
    }
    
    // Sieve with smallest prime factor (SPF)
    static std::vector<int> sieveWithSPF(int n) {
        std::vector<int> spf(n + 1);
        
        for (int i = 0; i <= n; i++) {
            spf[i] = i;
        }
        
        for (int i = 2; i * i <= n; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= n; j += i) {
                    if (spf[j] == j) {
                        spf[j] = i;
                    }
                }
            }
        }
        
        return spf;
    }
};
```

### 3. Segmented Sieve
```cpp
class SegmentedSieve {
public:
    // Find primes in range [L, R]
    static std::vector<int> segmentedSieve(long long L, long long R) {
        // Generate all primes up to sqrt(R)
        long long limit = sqrt(R);
        std::vector<int> basePrimes = SieveOfEratosthenes::getPrimes(limit);
        
        // Create boolean array for [L, R]
        std::vector<bool> isPrime(R - L + 1, true);
        
        // Mark non-primes in [L, R]
        for (int prime : basePrimes) {
            long long firstMultiple = (L / prime) * prime;
            if (firstMultiple < L) firstMultiple += prime;
            
            for (long long j = firstMultiple; j <= R; j += prime) {
                if (j != prime) { // Don't mark the prime itself
                    isPrime[j - L] = false;
                }
            }
        }
        
        // Collect primes in [L, R]
        std::vector<int> primes;
        for (long long i = L; i <= R; i++) {
            if (i >= 2 && isPrime[i - L]) {
                primes.push_back(i);
            }
        }
        
        return primes;
    }
};
```

## Prime Factorization

### 1. Basic Factorization
```cpp
class PrimeFactorization {
public:
    // Factorize using trial division
    static std::vector<std::pair<int, int>> factorize(int n) {
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
    
    // Factorize using SPF (Smallest Prime Factor)
    static std::vector<std::pair<int, int>> factorizeWithSPF(int n, 
                                                            const std::vector<int>& spf) {
        std::vector<std::pair<int, int>> factors;
        
        while (n > 1) {
            int prime = spf[n];
            int count = 0;
            
            while (n % prime == 0) {
                n /= prime;
                count++;
            }
            
            factors.push_back({prime, count});
        }
        
        return factors;
    }
    
    // Get all divisors of n
    static std::vector<int> getDivisors(int n) {
        auto factors = factorize(n);
        std::vector<int> divisors = {1};
        
        for (auto factor : factors) {
            int prime = factor.first;
            int exp = factor.second;
            
            int currentSize = divisors.size();
            std::vector<int> newDivisors;
            
            for (int d : divisors) {
                int current = d;
                for (int i = 0; i < exp; i++) {
                    current *= prime;
                    newDivisors.push_back(current);
                }
            }
            
            divisors.insert(divisors.end(), newDivisors.begin(), newDivisors.end());
        }
        
        std::sort(divisors.begin(), divisors.end());
        return divisors;
    }
    
    // Count number of divisors
    static int countDivisors(int n) {
        auto factors = factorize(n);
        int count = 1;
        
        for (auto factor : factors) {
            count *= (factor.second + 1);
        }
        
        return count;
    }
    
    // Sum of divisors
    static long long sumOfDivisors(int n) {
        auto factors = factorize(n);
        long long sum = 1;
        
        for (auto factor : factors) {
            int prime = factor.first;
            int exp = factor.second;
            
            long long term = (pow(prime, exp + 1) - 1) / (prime - 1);
            sum *= term;
        }
        
        return sum;
    }
};
```

## Special Prime Numbers

### 1. Twin Primes
```cpp
class TwinPrimes {
public:
    // Find twin primes up to n
    static std::vector<std::pair<int, int>> findTwinPrimes(int n) {
        std::vector<bool> isPrime = SieveOfEratosthenes::sieve(n);
        std::vector<std::pair<int, int>> twins;
        
        for (int i = 3; i + 2 <= n; i += 2) {
            if (isPrime[i] && isPrime[i + 2]) {
                twins.push_back({i, i + 2});
            }
        }
        
        return twins;
    }
    
    // Count twin primes up to n
    static int countTwinPrimes(int n) {
        return findTwinPrimes(n).size();
    }
};
```

### 2. Mersenne Primes
```cpp
class MersennePrimes {
public:
    // Check if 2^p - 1 is prime (Mersenne prime)
    static bool isMersennePrime(int p) {
        if (!PrimeChecker::isPrime(p)) return false;
        
        long long mersenne = (1LL << p) - 1;
        return PrimeChecker::isPrimeMillerRabin(mersenne);
    }
    
    // Find Mersenne primes for p up to n
    static std::vector<int> findMersennePrimes(int n) {
        std::vector<int> mersennePrimes;
        
        for (int p = 2; p <= n; p++) {
            if (isMersennePrime(p)) {
                mersennePrimes.push_back(p);
            }
        }
        
        return mersennePrimes;
    }
};
```

### 3. Sophie Germain Primes
```cpp
class SophieGermainPrimes {
public:
    // A prime p is Sophie Germain prime if 2p + 1 is also prime
    static std::vector<int> findSophieGermainPrimes(int n) {
        std::vector<bool> isPrime = SieveOfEratosthenes::sieve(2 * n + 1);
        std::vector<int> sophieGermain;
        
        for (int p = 2; p <= n; p++) {
            if (isPrime[p] && isPrime[2 * p + 1]) {
                sophieGermain.push_back(p);
            }
        }
        
        return sophieGermain;
    }
};
```

## Prime Number Applications

### 1. Euler's Totient Function
```cpp
class EulerTotient {
public:
    // Compute φ(n) for a single number
    static int phi(int n) {
        if (n == 0) return 0;
        
        int result = n;
        auto factors = PrimeFactorization::factorize(n);
        
        for (auto factor : factors) {
            int p = factor.first;
            result -= result / p;
        }
        
        return result;
    }
    
    // Compute φ for all numbers up to n using sieve
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

### 2. Prime Number Theorem Verification
```cpp
class PrimeNumberTheorem {
public:
    // Estimate number of primes ≤ n using n/ln(n)
    static double estimatePrimes(int n) {
        if (n < 2) return 0;
        return n / log(n);
    }
    
    // Actual count of primes ≤ n
    static int actualPrimes(int n) {
        return SieveOfEratosthenes::getPrimes(n).size();
    }
    
    // Calculate relative error
    static double relativeError(int n) {
        double estimated = estimatePrimes(n);
        double actual = actualPrimes(n);
        
        return abs(estimated - actual) / actual;
    }
};
```

## Performance Analysis

### Time Complexity
| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Basic Prime Check | O(√n) | O(1) |
| Miller-Rabin | O(k log³n) | O(1) |
| Sieve of Eratosthenes | O(n log log n) | O(n) |
| Segmented Sieve | O((R-L+1) log log R + √R log log √R) | O(√R) |
| Prime Factorization | O(√n) | O(log n) |

### Optimization Tips
1. **Use sieve for multiple queries**: Precompute primes once
2. **Skip even numbers**: Handle 2 separately, then check only odds
3. **Use Miller-Rabin for large numbers**: More efficient than trial division
4. **Segmented sieve for large ranges**: Memory efficient for large intervals
5. **Cache results**: Store frequently used prime information

## Common Applications

### 1. Cryptography
- **RSA Encryption**: Uses large prime numbers
- **Diffie-Hellman Key Exchange**: Prime modulus
- **Digital Signatures**: Prime-based algorithms

### 2. Hash Functions
- **Universal Hashing**: Prime number moduli
- **Collision Reduction**: Prime table sizes

### 3. Computer Science
- **Random Number Generation**: Prime-based generators
- **Load Balancing**: Prime-based distribution
- **Error Detection**: Prime-based checksums

## Best Practices

### 1. Algorithm Selection
- Use **sieve** for multiple prime queries
- Use **Miller-Rabin** for single large number primality test
- Use **segmented sieve** for large ranges
- Use **SPF** for multiple factorizations

### 2. Implementation Tips
- Handle edge cases (n < 2)
- Use appropriate data types (long long for large numbers)
- Consider memory constraints for large sieves
- Optimize inner loops in sieve implementations

### 3. Testing
- Test with small and large numbers
- Verify against known prime lists
- Check performance with different input sizes
- Validate factorization results

## Summary

Prime numbers are fundamental to number theory and have extensive applications in computer science. Understanding various prime algorithms, their complexities, and optimizations is crucial for solving many computational problems efficiently. Mastering prime number techniques provides a strong foundation for advanced algorithmic problem-solving.
---

## Next Step

- Go to [03_Factorial_and_Combinatorics.md](03_Factorial_and_Combinatorics.md) to continue with Factorial and Combinatorics.
