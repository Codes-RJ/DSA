# Bit Manipulation

## Overview
Bit manipulation is the technique of directly manipulating bits within binary representations of numbers. It's a powerful optimization technique that can lead to highly efficient solutions for many problems, especially in competitive programming and system-level programming.

## Topics Covered

### 1. Basic Bit Operations (`01_Basic_Bit_Operations.md`)
- Bitwise AND, OR, XOR, NOT operations
- Left and right shift operations
- Bit setting, clearing, and toggling
- Bit checking and extraction

### 2. Bit Tricks (`02_Bit_Tricks.md`)
- Power of two operations
- Counting set bits efficiently
- Finding unique elements
- Bit manipulation for mathematical operations

### 3. Bit Masks (`03_Bit_Masks.md`)
- Creating and using bit masks
- Subset generation using bits
- State representation with bits
- Bitmask DP techniques

### 4. Binary Representation (`04_Binary_Representation.md`)
- Understanding binary number system
- Converting between number systems
- Signed and unsigned representations
- Two's complement

### 5. Bit Manipulation Problems (`05_Bit_Manipulation_Problems.md`)
- Common bit manipulation problems
- Optimization techniques
- Real-world applications
- Practice problems

## Key Concepts

### Bitwise Operations
- **AND (&)**: Bitwise conjunction
- **OR (|)**: Bitwise disjunction
- **XOR (^)**: Bitwise exclusive or
- **NOT (~)**: Bitwise negation
- **Left Shift (<<)**: Shift bits left
- **Right Shift (>>)**: Shift bits right

### Common Bit Patterns
- **Power of Two**: Only one bit set
- **Even/Odd**: Last bit determines parity
- **Sign Bit**: Most significant bit for signed numbers
- **Mask**: Used to isolate specific bits

## Basic Operations

### 1. Bit Checking
```cpp
class BitOperations {
public:
    // Check if bit at position k is set (0-indexed)
    static bool isBitSet(int n, int k) {
        return (n & (1 << k)) != 0;
    }
    
    // Check if bit at position k is clear
    static bool isBitClear(int n, int k) {
        return (n & (1 << k)) == 0;
    }
    
    // Get value of bit at position k
    static int getBit(int n, int k) {
        return (n >> k) & 1;
    }
};
```

### 2. Bit Setting and Clearing
```cpp
class BitModification {
public:
    // Set bit at position k
    static int setBit(int n, int k) {
        return n | (1 << k);
    }
    
    // Clear bit at position k
    static int clearBit(int n, int k) {
        return n & ~(1 << k);
    }
    
    // Toggle bit at position k
    static int toggleBit(int n, int k) {
        return n ^ (1 << k);
    }
    
    // Update bit at position k to value v (0 or 1)
    static int updateBit(int n, int k, int v) {
        int mask = 1 << k;
        return (n & ~mask) | ((v << k) & mask);
    }
};
```

### 3. Bit Counting
```cpp
class BitCounting {
public:
    // Count set bits (Brian Kernighan's algorithm)
    static int countSetBits(int n) {
        int count = 0;
        while (n) {
            n &= (n - 1); // Clear the rightmost set bit
            count++;
        }
        return count;
    }
    
    // Count clear bits
    static int countClearBits(int n) {
        int bitLength = sizeof(n) * 8;
        return bitLength - countSetBits(n);
    }
    
    // Count set bits in range [l, r]
    static int countSetBitsInRange(int n, int l, int r) {
        int mask = ((1 << (r - l + 1)) - 1) << l;
        int masked = n & mask;
        return countSetBits(masked);
    }
};
```

## Advanced Bit Techniques

### 1. Power of Two Operations
```cpp
class PowerOfTwo {
public:
    // Check if n is a power of two
    static bool isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
    
    // Get next power of two greater than n
    static int nextPowerOfTwo(int n) {
        if (n <= 1) return 2;
        
        n--;
        n |= n >> 1;
        n |= n >> 2;
        n |= n >> 4;
        n |= n >> 8;
        n |= n >> 16;
        n++;
        
        return n;
    }
    
    // Get previous power of two less than or equal to n
    static int previousPowerOfTwo(int n) {
        if (n <= 1) return 1;
        
        n |= n >> 1;
        n |= n >> 2;
        n |= n >> 4;
        n |= n >> 8;
        n |= n >> 16;
        
        return n - (n >> 1);
    }
};
```

### 2. Bit Reversal and Rotation
```cpp
class BitManipulationAdvanced {
public:
    // Reverse bits of a number
    static unsigned int reverseBits(unsigned int n) {
        unsigned int result = 0;
        int bitCount = sizeof(n) * 8;
        
        for (int i = 0; i < bitCount; i++) {
            result <<= 1;
            result |= (n & 1);
            n >>= 1;
        }
        
        return result;
    }
    
    // Rotate bits left by k positions
    static unsigned int rotateLeft(unsigned int n, int k) {
        int bitCount = sizeof(n) * 8;
        k %= bitCount;
        
        return (n << k) | (n >> (bitCount - k));
    }
    
    // Rotate bits right by k positions
    static unsigned int rotateRight(unsigned int n, int k) {
        int bitCount = sizeof(n) * 8;
        k %= bitCount;
        
        return (n >> k) | (n << (bitCount - k));
    }
    
    // Swap odd and even bits
    static unsigned int swapOddEvenBits(unsigned int n) {
        unsigned int evenBits = n & 0xAAAAAAAA; // Mask for even positions
        unsigned int oddBits = n & 0x55555555;  // Mask for odd positions
        
        evenBits >>= 1;
        oddBits <<= 1;
        
        return evenBits | oddBits;
    }
};
```

## Bit Masks and Applications

### 1. Subset Generation
```cpp
class SubsetGeneration {
public:
    // Generate all subsets using bitmask
    static std::vector<std::vector<int>> generateSubsets(const std::vector<int>& arr) {
        int n = arr.size();
        std::vector<std::vector<int>> subsets;
        
        for (int mask = 0; mask < (1 << n); mask++) {
            std::vector<int> subset;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    subset.push_back(arr[i]);
                }
            }
            subsets.push_back(subset);
        }
        
        return subsets;
    }
    
    // Generate subsets of specific size
    static std::vector<std::vector<int>> generateSubsetsOfSize(
        const std::vector<int>& arr, int k) {
        int n = arr.size();
        std::vector<std::vector<int>> subsets;
        
        for (int mask = 0; mask < (1 << n); mask++) {
            if (__builtin_popcount(mask) == k) {
                std::vector<int> subset;
                for (int i = 0; i < n; i++) {
                    if (mask & (1 << i)) {
                        subset.push_back(arr[i]);
                    }
                }
                subsets.push_back(subset);
            }
        }
        
        return subsets;
    }
};
```

### 2. Bitmask DP
```cpp
class BitmaskDP {
public:
    // Assignment problem using bitmask DP
    static int assignmentProblem(const std::vector<std::vector<int>>& cost) {
        int n = cost.size();
        int dp[1 << 20]; // Assuming n <= 20
        
        for (int mask = 0; mask < (1 << n); mask++) {
            dp[mask] = INT_MAX;
        }
        dp[0] = 0;
        
        for (int mask = 0; mask < (1 << n); mask++) {
            int k = __builtin_popcount(mask); // Number of assigned jobs
            
            for (int i = 0; i < n; i++) {
                if (!(mask & (1 << i))) { // If job i is not assigned
                    int newMask = mask | (1 << i);
                    dp[newMask] = std::min(dp[newMask], dp[mask] + cost[k][i]);
                }
            }
        }
        
        return dp[(1 << n) - 1];
    }
    
    // Traveling Salesman Problem (TSP) using bitmask DP
    static int tsp(const std::vector<std::vector<int>>& dist) {
        int n = dist.size();
        int dp[1 << 15][15]; // Assuming n <= 15
        
        for (int mask = 0; mask < (1 << n); mask++) {
            for (int i = 0; i < n; i++) {
                dp[mask][i] = INT_MAX;
            }
        }
        
        dp[1][0] = 0; // Start from city 0
        
        for (int mask = 1; mask < (1 << n); mask++) {
            for (int u = 0; u < n; u++) {
                if (mask & (1 << u) && dp[mask][u] != INT_MAX) {
                    for (int v = 0; v < n; v++) {
                        if (!(mask & (1 << v))) {
                            int newMask = mask | (1 << v);
                            dp[newMask][v] = std::min(dp[newMask][v], 
                                                      dp[mask][u] + dist[u][v]);
                        }
                    }
                }
            }
        }
        
        int result = INT_MAX;
        for (int i = 1; i < n; i++) {
            result = std::min(result, dp[(1 << n) - 1][i] + dist[i][0]);
        }
        
        return result;
    }
};
```

## Practical Applications

### 1. Finding Unique Elements
```cpp
class UniqueElements {
public:
    // Find element that appears once while others appear twice
    static int findUnique(const std::vector<int>& arr) {
        int result = 0;
        for (int num : arr) {
            result ^= num;
        }
        return result;
    }
    
    // Find two unique elements while others appear twice
    static std::pair<int, int> findTwoUnique(const std::vector<int>& arr) {
        int xorAll = 0;
        for (int num : arr) {
            xorAll ^= num;
        }
        
        // Find rightmost set bit
        int rightmostSet = xorAll & -xorAll;
        
        int num1 = 0, num2 = 0;
        for (int num : arr) {
            if (num & rightmostSet) {
                num1 ^= num;
            } else {
                num2 ^= num;
            }
        }
        
        return {num1, num2};
    }
    
    // Find element that appears once while others appear three times
    static int findUniqueThrice(const std::vector<int>& arr) {
        int ones = 0, twos = 0;
        
        for (int num : arr) {
            ones = (ones ^ num) & ~twos;
            twos = (twos ^ num) & ~ones;
        }
        
        return ones;
    }
};
```

### 2. Mathematical Operations
```cpp
class BitMath {
public:
    // Multiply two numbers using bit operations
    static long long multiply(int a, int b) {
        long long result = 0;
        
        while (b > 0) {
            if (b & 1) {
                result += a;
            }
            a <<= 1;
            b >>= 1;
        }
        
        return result;
    }
    
    // Divide two numbers using bit operations
    static std::pair<int, int> divide(int dividend, int divisor) {
        if (divisor == 0) return {INT_MAX, 0}; // Division by zero
        
        bool negative = (dividend < 0) ^ (divisor < 0);
        long long dvd = abs(dividend);
        long long dvs = abs(divisor);
        
        int quotient = 0;
        for (int i = 31; i >= 0; i--) {
            if ((dvs << i) <= dvd) {
                dvd -= (dvs << i);
                quotient += (1 << i);
            }
        }
        
        if (negative) quotient = -quotient;
        return {quotient, dvd};
    }
    
    // Calculate absolute value without branching
    static int absoluteValue(int n) {
        int mask = n >> (sizeof(int) * 8 - 1);
        return (n ^ mask) - mask;
    }
    
    // Find maximum of two numbers without branching
    static int max(int a, int b) {
        return a ^ ((a ^ b) & -(a < b));
    }
    
    // Find minimum of two numbers without branching
    static int min(int a, int b) {
        return b ^ ((a ^ b) & -(a < b));
    }
};
```

## Optimization Techniques

### 1. Bit Hacks for Performance
```cpp
class BitHacks {
public:
    // Fast absolute value
    static int fastAbs(int n) {
        int mask = n >> 31;
        return (n + mask) ^ mask;
    }
    
    // Fast sign function
    static int sign(int n) {
        return (n > 0) - (n < 0);
    }
    
    // Fast min/max
    static int fastMin(int a, int b) {
        return b + ((a - b) & ((a - b) >> (sizeof(int) * 8 - 1)));
    }
    
    static int fastMax(int a, int b) {
        return a - ((a - b) & ((a - b) >> (sizeof(int) * 8 - 1)));
    }
    
    // Check if numbers have opposite signs
    static bool oppositeSigns(int a, int b) {
        return (a ^ b) < 0;
    }
    
    // Fast modulo for power of 2
    static int fastModPowerOfTwo(int n, int power) {
        return n & (power - 1);
    }
};
```

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Bit Check | O(1) | O(1) |
| Bit Set/Clear | O(1) | O(1) |
| Count Set Bits | O(number of set bits) | O(1) |
| Reverse Bits | O(log n) | O(1) |
| Subset Generation | O(2^n * n) | O(2^n * n) |
| Bitmask DP | O(2^n * n) | O(2^n) |

## Best Practices

1. **Use Unsigned Types**: For predictable bit behavior
2. **Avoid Undefined Behavior**: Be careful with signed shifts
3. **Consider Endianness**: For bit-level operations
4. **Use Built-in Functions**: Like __builtin_popcount for optimization
5. **Document Bit Logic**: Bit operations can be hard to read

## Common Pitfalls

1. **Operator Precedence**: Use parentheses for clarity
2. **Signed vs Unsigned**: Different behavior for right shifts
3. **Integer Overflow**: Be careful with left shifts
4. **Undefined Behavior**: Shifting by >= bit width
5. **Portability**: Bit representation may vary

## Summary

Bit manipulation is a powerful technique for optimizing algorithms and solving problems efficiently. Mastering bit operations enables elegant solutions to many computational problems and is essential for competitive programming and system-level programming.
