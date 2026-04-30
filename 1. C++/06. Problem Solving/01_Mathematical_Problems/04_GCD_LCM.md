# 04_GCD_LCM.md

## GCD and LCM (Euclidean Algorithm)

### Overview

The Greatest Common Divisor (GCD) and Least Common Multiple (LCM) are fundamental concepts in number theory. GCD is the largest number that divides two or more numbers without leaving a remainder. LCM is the smallest positive number that is a multiple of two or more numbers. The Euclidean algorithm provides an efficient way to compute GCD, and LCM can be derived from GCD.

---

### 1. Greatest Common Divisor (GCD)

**Definition:** The GCD of two or more integers is the largest positive integer that divides each of the integers without a remainder.

**Notation:** gcd(a, b) or (a, b)

**Examples:**
- gcd(12, 18) = 6
- gcd(24, 36, 48) = 12
- gcd(17, 19) = 1 (coprime)

**Properties:**
- gcd(a, b) = gcd(b, a)
- gcd(a, 0) = a
- gcd(a, b) = gcd(a, b % a) (Euclidean algorithm)
- gcd(a, b) = gcd(a - b, b) (subtractive algorithm)

**GCD Implementation (Euclidean Algorithm):**

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Recursive Euclidean algorithm
int gcdRecursive(int a, int b) {
    if (b == 0) return a;
    return gcdRecursive(b, a % b);
}

// Iterative Euclidean algorithm
int gcdIterative(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// GCD of an array
int gcdArray(vector<int>& arr) {
    int result = arr[0];
    for (int i = 1; i < arr.size(); i++) {
        result = gcdIterative(result, arr[i]);
        if (result == 1) break;  // Early exit
    }
    return result;
}

int main() {
    cout << "gcd(12, 18) = " << gcdRecursive(12, 18) << endl;
    cout << "gcd(48, 18) = " << gcdIterative(48, 18) << endl;
    cout << "gcd(17, 19) = " << gcdIterative(17, 19) << endl;
    
    vector<int> arr = {24, 36, 48, 60};
    cout << "gcd of [24, 36, 48, 60] = " << gcdArray(arr) << endl;
    
    return 0;
}
```

**Output:**
```
gcd(12, 18) = 6
gcd(48, 18) = 6
gcd(17, 19) = 1
gcd of [24, 36, 48, 60] = 12
```

---

### 2. Euclidean Algorithm - Step by Step

The Euclidean algorithm finds GCD by repeatedly applying the property: GCD(a, b) = GCD(b, a mod b).

**Example: gcd(48, 18)**
```
48 ÷ 18 = 2 remainder 12
gcd(48, 18) = gcd(18, 12)

18 ÷ 12 = 1 remainder 6
gcd(18, 12) = gcd(12, 6)

12 ÷ 6 = 2 remainder 0
gcd(12, 6) = 6

Therefore, gcd(48, 18) = 6
```

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Step-by-step Euclidean algorithm (debug version)
int gcdStepByStep(int a, int b) {
    cout << "Computing gcd(" << a << ", " << b << ")" << endl;
    
    int step = 1;
    while (b != 0) {
        int quotient = a / b;
        int remainder = a % b;
        cout << "  Step " << step << ": " << a << " = " << b << " × " << quotient << " + " << remainder << endl;
        a = b;
        b = remainder;
        step++;
    }
    
    cout << "Result: " << a << endl;
    return a;
}

int main() {
    gcdStepByStep(48, 18);
    cout << endl;
    gcdStepByStep(1071, 462);
    
    return 0;
}
```

**Output:**
```
Computing gcd(48, 18)
  Step 1: 48 = 18 × 2 + 12
  Step 2: 18 = 12 × 1 + 6
  Step 3: 12 = 6 × 2 + 0
Result: 6

Computing gcd(1071, 462)
  Step 1: 1071 = 462 × 2 + 147
  Step 2: 462 = 147 × 3 + 21
  Step 3: 147 = 21 × 7 + 0
Result: 21
```

---

### 3. Extended Euclidean Algorithm

The extended Euclidean algorithm finds integers x and y such that:

**ax + by = gcd(a, b)**

This is used for finding modular inverses and solving linear Diophantine equations.

```cpp
#include <iostream>
#include <tuple>
using namespace std;

// Extended Euclidean algorithm
// Returns (gcd, x, y) such that a*x + b*y = gcd(a, b)
tuple<int, int, int> extendedGCD(int a, int b) {
    if (b == 0) {
        return {a, 1, 0};
    }
    
    auto [gcd, x1, y1] = extendedGCD(b, a % b);
    int x = y1;
    int y = x1 - (a / b) * y1;
    
    return {gcd, x, y};
}

// Iterative extended Euclidean algorithm
tuple<int, int, int> extendedGCDIterative(int a, int b) {
    int x0 = 1, x1 = 0;
    int y0 = 0, y1 = 1;
    
    while (b != 0) {
        int q = a / b;
        int r = a % b;
        
        a = b;
        b = r;
        
        int x2 = x0 - q * x1;
        int y2 = y0 - q * y1;
        
        x0 = x1;
        y0 = y1;
        x1 = x2;
        y1 = y2;
    }
    
    return {a, x0, y0};
}

int main() {
    int a = 48, b = 18;
    
    auto [gcd, x, y] = extendedGCD(a, b);
    cout << "Extended Euclidean algorithm:" << endl;
    cout << "gcd(" << a << ", " << b << ") = " << gcd << endl;
    cout << x << " × " << a << " + " << y << " × " << b << " = " << gcd << endl;
    
    // Verify
    cout << "Verification: " << (a * x + b * y) << endl;
    
    return 0;
}
```

**Output:**
```
Extended Euclidean algorithm:
gcd(48, 18) = 6
(-1) × 48 + (3) × 18 = 6
Verification: 6
```

---

### 4. Least Common Multiple (LCM)

**Definition:** The LCM of two or more integers is the smallest positive integer that is divisible by each of the integers.

**Formula:** lcm(a, b) = |a × b| / gcd(a, b)

**Examples:**
- lcm(4, 6) = 12
- lcm(12, 18) = 36

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// LCM of two numbers
long long lcm(int a, int b) {
    // Use long long to avoid overflow
    return (long long)abs(a) / gcdIterative(a, b) * abs(b);
}

// LCM of an array
long long lcmArray(vector<int>& arr) {
    long long result = arr[0];
    for (int i = 1; i < arr.size(); i++) {
        result = lcm(result, arr[i]);
    }
    return result;
}

int main() {
    cout << "lcm(4, 6) = " << lcm(4, 6) << endl;
    cout << "lcm(12, 18) = " << lcm(12, 18) << endl;
    cout << "lcm(7, 13) = " << lcm(7, 13) << endl;
    
    vector<int> arr = {2, 3, 4, 5};
    cout << "lcm of [2, 3, 4, 5] = " << lcmArray(arr) << endl;
    
    return 0;
}
```

**Output:**
```
lcm(4, 6) = 12
lcm(12, 18) = 36
lcm(7, 13) = 91
lcm of [2, 3, 4, 5] = 60
```

---

### 5. Relationship Between GCD and LCM

For two numbers:
```
gcd(a, b) × lcm(a, b) = a × b
```

This relationship can be used to compute LCM from GCD or vice versa.

```cpp
#include <iostream>
using namespace std;

void demonstrateRelation(int a, int b) {
    int g = gcdIterative(a, b);
    long long l = lcm(a, b);
    long long product = (long long)a * b;
    
    cout << "For a = " << a << ", b = " << b << ":" << endl;
    cout << "  gcd(a, b) = " << g << endl;
    cout << "  lcm(a, b) = " << l << endl;
    cout << "  gcd × lcm = " << g * l << endl;
    cout << "  a × b = " << product << endl;
    cout << "  Verified: " << (g * l == product ? "✓" : "✗") << endl;
    cout << endl;
}

int main() {
    demonstrateRelation(12, 18);
    demonstrateRelation(15, 25);
    demonstrateRelation(8, 9);
    
    return 0;
}
```

**Output:**
```
For a = 12, b = 18:
  gcd(a, b) = 6
  lcm(a, b) = 36
  gcd × lcm = 216
  a × b = 216
  Verified: ✓

For a = 15, b = 25:
  gcd(a, b) = 5
  lcm(a, b) = 75
  gcd × lcm = 375
  a × b = 375
  Verified: ✓

For a = 8, b = 9:
  gcd(a, b) = 1
  lcm(a, b) = 72
  gcd × lcm = 72
  a × b = 72
  Verified: ✓
```

---

### 6. GCD and LCM of More Than Two Numbers

GCD of more than two numbers can be computed iteratively:
```
gcd(a, b, c) = gcd(gcd(a, b), c)
```

Similarly for LCM:
```
lcm(a, b, c) = lcm(lcm(a, b), c)
```

```cpp
#include <iostream>
#include <vector>
using namespace std;

// GCD of n numbers
template<typename T>
T gcdMultiple(vector<T>& arr) {
    T result = arr[0];
    for (size_t i = 1; i < arr.size(); i++) {
        result = gcdIterative(result, arr[i]);
        if (result == 1) break;  // Can't get smaller than 1
    }
    return result;
}

// LCM of n numbers
template<typename T>
long long lcmMultiple(vector<T>& arr) {
    long long result = arr[0];
    for (size_t i = 1; i < arr.size(); i++) {
        result = lcm(result, arr[i]);
    }
    return result;
}

int main() {
    vector<int> numbers = {12, 18, 24, 30};
    
    cout << "Numbers: ";
    for (int n : numbers) cout << n << " ";
    cout << endl;
    
    cout << "GCD = " << gcdMultiple(numbers) << endl;
    cout << "LCM = " << lcmMultiple(numbers) << endl;
    
    // Verify: Each number should divide LCM
    long long l = lcmMultiple(numbers);
    cout << "\nVerification:" << endl;
    for (int n : numbers) {
        cout << l << " ÷ " << n << " = " << (l / n) << " (remainder 0? " << (l % n == 0 ? "✓" : "✗") << ")" << endl;
    }
    
    return 0;
}
```

**Output:**
```
Numbers: 12 18 24 30 
GCD = 6
LCM = 360

Verification:
360 ÷ 12 = 30 (remainder 0? ✓)
360 ÷ 18 = 20 (remainder 0? ✓)
360 ÷ 24 = 15 (remainder 0? ✓)
360 ÷ 30 = 12 (remainder 0? ✓)
```

---

### 7. Applications

#### 1. Reducing Fractions

```cpp
void reduceFraction(int& numerator, int& denominator) {
    int g = gcdIterative(abs(numerator), abs(denominator));
    numerator /= g;
    denominator /= g;
    
    // Ensure denominator is positive
    if (denominator < 0) {
        numerator = -numerator;
        denominator = -denominator;
    }
}

int main() {
    int num = 48, den = 180;
    cout << "Original fraction: " << num << "/" << den << endl;
    
    reduceFraction(num, den);
    cout << "Reduced fraction: " << num << "/" << den << endl;
    
    return 0;
}
```

**Output:**
```
Original fraction: 48/180
Reduced fraction: 4/15
```

#### 2. Finding Common Period (Cycles)

```cpp
// Find when two cycles will align
long long findAlignment(int cycle1, int cycle2) {
    return lcm(cycle1, cycle2);
}

int main() {
    cout << "Planet A orbits every 12 months, Planet B every 18 months" << endl;
    cout << "They will align every " << findAlignment(12, 18) << " months" << endl;
    
    return 0;
}
```

**Output:**
```
Planet A orbits every 12 months, Planet B every 18 months
They will align every 36 months
```

---

### Complexity Summary

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **Euclidean (GCD)** | O(log min(a, b)) | O(1) |
| **Extended Euclidean** | O(log min(a, b)) | O(log n) (recursion) |
| **LCM using GCD** | O(log min(a, b)) | O(1) |
| **GCD of array** | O(n × log M) | O(1) |
| **LCM of array** | O(n × log M) | O(1) |

---

### Key Takeaways

1. **Euclidean algorithm** computes GCD in O(log n) time
2. **Extended Euclidean** finds coefficients for Bezout's identity
3. **LCM = a × b / GCD(a, b)** - use division before multiplication to avoid overflow
4. **GCD and LCM are associative** - can compute for multiple numbers iteratively
5. **GCD(a, b) = 1** means a and b are coprime
6. **Applications** include fraction reduction, period alignment, and modular arithmetic

---

### Practice Questions

1. Find gcd(252, 105) using the Euclidean algorithm
2. Find lcm(24, 36, 48)
3. Find integers x and y such that 56x + 72y = 8
4. Reduce the fraction 144/240 to simplest form
5. Two bells ring at intervals of 12 and 18 minutes. When will they ring together?
6. Find the largest number that divides 245 and 315 exactly
7. Find the smallest number divisible by 4, 5, 6, 8, and 10
8. Prove that consecutive integers are always coprime

---

### Next Steps

- Go to [05_Modular_Arithmetic.md](05_Modular_Arithmetic.md) for Modular Arithmetic.