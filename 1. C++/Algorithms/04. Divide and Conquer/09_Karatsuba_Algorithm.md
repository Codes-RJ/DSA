# 09_Karatsuba_Algorithm.md

## Karatsuba Algorithm for Fast Multiplication

### Definition

Karatsuba's algorithm is a divide-and-conquer algorithm for multiplying large numbers efficiently. It is faster than the traditional grade-school multiplication method.

### Traditional Multiplication

For two n-digit numbers, grade-school multiplication takes O(n²) time.

Example: 1234 × 5678 requires 16 single-digit multiplications.

### Karatsuba's Insight

For two numbers x and y, split each into two halves:

```
x = a * 10^(n/2) + b
y = c * 10^(n/2) + d

Traditional: x * y = ac*10^n + (ad + bc)*10^(n/2) + bd
This requires 4 multiplications: ac, ad, bc, bd

Karatsuba: x * y = ac*10^n + (ac + bd - (a-b)(c-d))*10^(n/2) + bd
This requires only 3 multiplications:
    p1 = a * c
    p2 = b * d
    p3 = (a - b) * (c - d)  (or (a+b)*(c+d) depending on sign)
Then: ad + bc = p1 + p2 - p3
```

### Algorithm Steps

```
Step 1: Split numbers into two halves
Step 2: Recursively compute three products:
        p1 = a * c
        p2 = b * d
        p3 = (a + b) * (c + d)  [or (a - b)*(c - d) for signed]
Step 3: Compute ad + bc = p3 - p1 - p2
Step 4: Combine: result = p1 * 10^(2m) + (p3 - p1 - p2) * 10^m + p2
```

### Implementation

```cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

string addStrings(string a, string b) {
    string result;
    int carry = 0;
    int i = a.length() - 1;
    int j = b.length() - 1;
    
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += a[i--] - '0';
        if (j >= 0) sum += b[j--] - '0';
        result.push_back(sum % 10 + '0');
        carry = sum / 10;
    }
    
    reverse(result.begin(), result.end());
    return result;
}

string subtractStrings(string a, string b) {
    string result;
    int borrow = 0;
    int i = a.length() - 1;
    int j = b.length() - 1;
    
    while (i >= 0) {
        int diff = (a[i] - '0') - borrow;
        if (j >= 0) diff -= (b[j] - '0');
        
        if (diff < 0) {
            diff += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }
        
        result.push_back(diff + '0');
        i--;
        j--;
    }
    
    // Remove leading zeros
    while (result.length() > 1 && result.back() == '0') {
        result.pop_back();
    }
    
    reverse(result.begin(), result.end());
    return result;
}

string multiplyByPowerOf10(string num, int power) {
    if (num == "0") return num;
    return num + string(power, '0');
}

string karatsuba(string x, string y) {
    // Remove leading zeros
    while (x.length() > 1 && x[0] == '0') x.erase(0, 1);
    while (y.length() > 1 && y[0] == '0') y.erase(0, 1);
    
    // Base cases
    if (x == "0" || y == "0") return "0";
    if (x.length() == 1 && y.length() == 1) {
        int product = (x[0] - '0') * (y[0] - '0');
        return to_string(product);
    }
    
    // Make lengths equal by padding with zeros
    int n = max(x.length(), y.length());
    if (x.length() < n) x = string(n - x.length(), '0') + x;
    if (y.length() < n) y = string(n - y.length(), '0') + y;
    
    // For odd length, make it even by adding one more zero
    if (n % 2 != 0) {
        n++;
        x = "0" + x;
        y = "0" + y;
    }
    
    int m = n / 2;
    
    // Split numbers
    string a = x.substr(0, m);
    string b = x.substr(m);
    string c = y.substr(0, m);
    string d = y.substr(m);
    
    // Recursively compute three products
    string ac = karatsuba(a, c);
    string bd = karatsuba(b, d);
    string ab_cd = karatsuba(addStrings(a, b), addStrings(c, d));
    
    // ad + bc = (a+b)(c+d) - ac - bd
    string ad_bc = subtractStrings(subtractStrings(ab_cd, ac), bd);
    
    // Combine: ac * 10^(2m) + (ad+bc) * 10^m + bd
    string result = addStrings(
        addStrings(multiplyByPowerOf10(ac, 2 * m), 
                   multiplyByPowerOf10(ad_bc, m)), 
        bd);
    
    // Remove leading zeros
    while (result.length() > 1 && result[0] == '0') {
        result.erase(0, 1);
    }
    
    return result;
}

int main() {
    string x = "1234";
    string y = "5678";
    
    string product = karatsuba(x, y);
    
    cout << x << " × " << y << " = " << product << endl;
    
    return 0;
}
```

### Example Walkthrough

```
x = 1234, y = 5678
n = 4, m = 2

a = 12, b = 34
c = 56, d = 78

Compute:
ac = 12 × 56 = 672
bd = 34 × 78 = 2652
(a+b) = 12+34 = 46
(c+d) = 56+78 = 134
(a+b)(c+d) = 46 × 134 = 6164

ad + bc = 6164 - 672 - 2652 = 2840

Result = 672 × 10^4 + 2840 × 10^2 + 2652
       = 6720000 + 284000 + 2652
       = 7006652

Verify: 1234 × 5678 = 7006652 ✓
```

### Time Complexity Analysis

| Algorithm | Time Complexity | Multiplications |
|-----------|----------------|-----------------|
| Grade school | O(n²) | n² |
| Karatsuba | O(n^log₂3) ≈ O(n^1.585) | n^log₂3 |
| Toom-Cook | O(n^1.465) | More complex |
| FFT-based | O(n log n) | Very complex |

### Recurrence Relation

```
T(n) = 3T(n/2) + O(n)

By Master Theorem:
T(n) = O(n^(log₂3)) ≈ O(n^1.585)
```

### Comparison

| n (digits) | Grade School | Karatsuba |
|------------|--------------|-----------|
| 10 | 100 | ~50 |
| 100 | 10,000 | ~2,500 |
| 1000 | 1,000,000 | ~100,000 |
| 10,000 | 100,000,000 | ~4,000,000 |

### Advantages

| Advantage | Description |
|-----------|-------------|
| Faster than grade school | O(n^1.585) vs O(n²) |
| Still simple | Easier than FFT methods |
| Works on any base | Decimal, binary, etc. |
| Recursive structure | Natural divide and conquer |

### Disadvantages

| Disadvantage | Description |
|--------------|-------------|
| Overhead for small n | Base case needed |
| Memory usage | Creates many strings |
| Implementation complexity | Harder than grade school |

### Applications

| Application | Description |
|-------------|-------------|
| Big integer arithmetic | Python's long integers, Java's BigInteger |
| Cryptography | RSA requires large number multiplication |
| Computer algebra systems | Symbolic computation |
| Scientific computing | High precision calculations |

### Practice Problems

1. Multiply two large numbers using Karatsuba
2. Implement Karatsuba for binary numbers
3. Compare performance of Karatsuba vs grade school
4. Implement Karatsuba with base case using grade school
5. Extend Karatsuba to handle negative numbers
