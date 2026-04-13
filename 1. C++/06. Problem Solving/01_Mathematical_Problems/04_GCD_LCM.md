# GCD and LCM

## Introduction
Greatest Common Divisor (GCD) and Least Common Multiple (LCM) are fundamental in number theory.

## Greatest Common Divisor (GCD)
The GCD of two or more integers is the largest positive integer that divides each of the integers without a remainder.

### Euclidean Algorithm
The most efficient way to find GCD.
`gcd(a, b) = gcd(b, a % b)` until `b` becomes 0.

#### C++ Implementation (Recursive)
```cpp
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
```

#### C++ Implementation (Iterative)
```cpp
int gcd(int a, int b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}
```

## Least Common Multiple (LCM)
The LCM of two or more integers is the smallest positive integer that is divisible by all of them.

### Relationship Between GCD and LCM
`a * b = gcd(a, b) * lcm(a, b)`
Therefore, `lcm(a, b) = (a * b) / gcd(a, b)`

#### C++ Implementation
```cpp
long long lcm(int a, int b) {
    if (a == 0 || b == 0) return 0;
    // Divide before multiplying to avoid overflow
    return ((long long)a / gcd(a, b)) * b;
}
```

## Extended Euclidean Algorithm
Used to find integer coefficients `x` and `y` such that `ax + by = gcd(a, b)`. These are useful in finding modular multiplicative inverses.

```cpp
int extendedGCD(int a, int b, int &x, int &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    int x1, y1;
    int gcd = extendedGCD(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return gcd;
}
```

## Complexity
- **Time**: O(log(min(a, b))) for Euclidean Algorithm.
- **Space**: O(1) or O(log N) for recursion stack.
---

## Next Step

- Go to [05_Modular_Arithmetic.md](05_Modular_Arithmetic.md) to continue with Modular Arithmetic.
