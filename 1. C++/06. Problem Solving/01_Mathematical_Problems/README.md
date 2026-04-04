# Mathematical Problems

## Overview
Mathematical problems form the foundation of algorithmic thinking and competitive programming. This section covers essential mathematical concepts and their applications in programming, including number theory, combinatorics, and modular arithmetic.

## Topics Covered

### 1. Number Theory (`01_Number_Theory.md`)
- Divisibility and factors
- Prime numbers and primality testing
- Sieve algorithms
- Number theoretic functions
- Diophantine equations

### 2. Prime Numbers (`02_Prime_Numbers.md`)
- Prime checking algorithms
- Sieve of Eratosthenes
- Segmented sieve
- Prime factorization
- Prime number theorems

### 3. Factorial and Combinatorics (`03_Factorial_and_Combinatorics.md`)
- Factorial computation
- Permutations and combinations
- Binomial coefficients
- Pascal's triangle
- Inclusion-exclusion principle

### 4. GCD and LCM (`04_GCD_LCM.md`)
- Euclidean algorithm
- Extended Euclidean algorithm
- LCM computation
- Diophantine equations
- Modular inverses

### 5. Modular Arithmetic (`05_Modular_Arithmetic.md`)
- Modular operations
- Fermat's little theorem
- Chinese remainder theorem
- Modular exponentiation
- Modular inverses

### 6. Series and Summations (`06_Series_and_Summations.md`)
- Arithmetic series
- Geometric series
- Fibonacci sequence
- Summation formulas
- Recurrence relations

## Key Mathematical Concepts

### Number Theory Fundamentals
- **Divisibility**: a divides b if b = a × k for some integer k
- **Prime Numbers**: Natural numbers greater than 1 with exactly two divisors
- **GCD**: Greatest common divisor of two numbers
- **LCM**: Least common multiple of two numbers

### Combinatorial Mathematics
- **Permutations**: Ordered arrangements of objects
- **Combinations**: Unordered selections of objects
- **Binomial Coefficients**: Number of ways to choose k items from n items
- **Factorial**: Product of all positive integers up to n

### Modular Arithmetic
- **Modulo Operation**: Remainder after division
- **Modular Addition**: (a + b) mod m = ((a mod m) + (b mod m)) mod m
- **Modular Multiplication**: (a × b) mod m = ((a mod m) × (b mod m)) mod m
- **Modular Exponentiation**: Efficient computation of (a^b) mod m

## Common Algorithms

### 1. Sieve of Eratosthenes
```cpp
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

### 2. Euclidean Algorithm
```cpp
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
```

### 3. Modular Exponentiation
```cpp
long long modPow(long long a, long long b, long long mod) {
    long long result = 1;
    a %= mod;
    
    while (b > 0) {
        if (b & 1) {
            result = (result * a) % mod;
        }
        a = (a * a) % mod;
        b >>= 1;
    }
    
    return result;
}
```

## Problem-Solving Strategies

### 1. Pattern Recognition
- Look for mathematical patterns in the problem
- Identify sequences or series
- Recognize common mathematical properties

### 2. Mathematical Modeling
- Convert real-world problems to mathematical equations
- Identify constraints and relationships
- Choose appropriate mathematical tools

### 3. Optimization Techniques
- Use mathematical properties to optimize solutions
- Apply number theory results
- Leverage combinatorial formulas

### 4. Edge Case Analysis
- Consider boundary conditions
- Handle special cases (zero, one, negative numbers)
- Validate mathematical assumptions

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Prime Check (Naive) | O(√n) | O(1) |
| Sieve of Eratosthenes | O(n log log n) | O(n) |
| GCD (Euclidean) | O(log min(a,b)) | O(1) |
| Modular Exponentiation | O(log b) | O(1) |
| Factorial | O(n) | O(1) |

## Applications

### Competitive Programming
- Number theory problems
- Combinatorial counting
- Cryptography challenges
- Mathematical optimization

### Real-World Applications
- Cryptography and security
- Statistical analysis
- Engineering calculations
- Financial modeling

### Computer Science
- Algorithm analysis
- Data structure design
- Complexity theory
- Cryptographic protocols

## Common Pitfalls

1. **Integer Overflow**: Use appropriate data types (long long)
2. **Modular Arithmetic**: Always apply modulo after operations
3. **Precision Issues**: Be careful with floating-point calculations
4. **Edge Cases**: Handle zero, one, and negative values properly
5. **Time Limits**: Optimize for large input sizes

## Best Practices

1. **Use Long Long**: For large numbers to avoid overflow
2. **Precompute Values**: Use sieves and dynamic programming
3. **Modular Arithmetic**: Apply modulo consistently
4. **Test Edge Cases**: Verify with boundary values
5. **Mathematical Proofs**: Understand why algorithms work

## Learning Resources

### Books
- "Elementary Number Theory" by David Burton
- "Concrete Mathematics" by Graham, Knuth, Patashnik
- "Competitive Programming 3" by Steven Halim

### Online Resources
- Khan Academy (Number Theory)
- Brilliant.org (Mathematics)
- GeeksforGeeks (Mathematical Algorithms)
- Codeforces (Math problems)

## Practice Problems

### Beginner Level
- Prime or composite checking
- GCD and LCM calculations
- Basic factorial problems
- Simple series summations

### Intermediate Level
- Sieve implementations
- Modular arithmetic problems
- Combinatorial counting
- Number theoretic functions

### Advanced Level
- Segmented sieve
- Chinese remainder theorem
- Advanced number theory
- Mathematical optimization

## Summary

Mathematical problems are essential for developing analytical thinking and algorithmic skills. Mastering these concepts provides a strong foundation for advanced algorithms and competitive programming success.
