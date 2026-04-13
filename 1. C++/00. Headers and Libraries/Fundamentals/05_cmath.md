# cmath - Mathematical Functions Library

The `cmath` header provides essential mathematical functions for C++ programming, including trigonometric, exponential, logarithmic, and power functions.

## 📖 Overview

`cmath` is the C++ version of the C math library (`math.h`). It provides a comprehensive set of mathematical functions that work with floating-point numbers.

## 🎯 Key Categories

1. **Basic Operations** - Absolute value, square root, power
2. **Trigonometric Functions** - sin, cos, tan and their inverses
3. **Exponential and Logarithmic** - exp, log, log10, etc.
4. **Rounding Functions** - floor, ceil, round, etc.
5. **Hyperbolic Functions** - sinh, cosh, tanh
6. **Special Functions** - fabs, fmod, etc.

## 🔧 Essential Functions

### Basic Mathematical Operations
```cpp
#include <iostream>
#include <cmath>

int main() {
    double x = -3.14;
    double y = 2.0;
    
    // Absolute value
    cout << "fabs(" << x << ") = " << fabs(x) << endl;  // 3.14
    
    // Square root
    cout << "sqrt(" << y << ") = " << sqrt(y) << endl;  // 1.414
    
    // Power function
    cout << "pow(" << y << ", 3) = " << pow(y, 3) << endl;  // 8.0
    
    // Hypotenuse
    cout << "hypot(3, 4) = " << hypot(3.0, 4.0) << endl;  // 5.0
    
    return 0;
}
```

### Trigonometric Functions
```cpp
#include <iostream>
#include <cmath>

int main() {
    double angle = M_PI / 4;  // 45 degrees in radians
    
    // Basic trigonometric functions
    cout << "sin(" << angle << ") = " << sin(angle) << endl;    // 0.707
    cout << "cos(" << angle << ") = " << cos(angle) << endl;    // 0.707
    cout << "tan(" << angle << ") = " << tan(angle) << endl;    // 1.0
    
    // Inverse trigonometric functions
    cout << "asin(0.5) = " << asin(0.5) << endl;      // 0.524 rad
    cout << "acos(0.5) = " << acos(0.5) << endl;      // 1.047 rad
    cout << "atan(1.0) = " << atan(1.0) << endl;      // 0.785 rad
    
    // Two-argument arctangent
    cout << "atan2(1, 1) = " << atan2(1.0, 1.0) << endl;  // 0.785 rad
    
    return 0;
}
```

### Exponential and Logarithmic Functions
```cpp
#include <iostream>
#include <cmath>

int main() {
    double x = 2.0;
    
    // Exponential functions
    cout << "exp(" << x << ") = " << exp(x) << endl;        // e^2 = 7.389
    cout << "exp2(" << x << ") = " << exp2(x) << endl;      // 2^2 = 4.0
    
    // Logarithmic functions
    cout << "log(" << x << ") = " << log(x) << endl;        // ln(2) = 0.693
    cout << "log10(" << x << ") = " << log10(x) << endl;    // log10(2) = 0.301
    cout << "log2(" << x << ") = " << log2(x) << endl;      // log2(2) = 1.0
    
    return 0;
}
```

## 🎮 Practical Examples

### Example 1: Geometry Calculator
```cpp
#include <iostream>
#include <cmath>
#include <iomanip>

class Geometry {
public:
    // Calculate distance between two points
    static double distance(double x1, double y1, double x2, double y2) {
        return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    }
    
    // Calculate area of triangle using Heron's formula
    static double triangleArea(double a, double b, double c) {
        double s = (a + b + c) / 2.0;
        return sqrt(s * (s - a) * (s - b) * (s - c));
    }
    
    // Calculate area of circle
    static double circleArea(double radius) {
        return M_PI * radius * radius;
    }
    
    // Calculate circumference of circle
    static double circleCircumference(double radius) {
        return 2 * M_PI * radius;
    }
};

int main() {
    cout << fixed << setprecision(2);
    
    // Distance calculation
    double dist = Geometry::distance(0, 0, 3, 4);
    cout << "Distance between (0,0) and (3,4): " << dist << endl;
    
    // Triangle area
    double area = Geometry::triangleArea(3, 4, 5);
    cout << "Area of triangle (3,4,5): " << area << endl;
    
    // Circle calculations
    double radius = 5.0;
    cout << "Area of circle (r=5): " << Geometry::circleArea(radius) << endl;
    cout << "Circumference of circle (r=5): " << Geometry::circleCircumference(radius) << endl;
    
    return 0;
}
```

### Example 2: Physics Calculator
```cpp
#include <iostream>
#include <cmath>

class Physics {
public:
    // Calculate projectile motion
    static void projectile(double velocity, double angle_deg) {
        double angle_rad = angle_deg * M_PI / 180.0;
        double vx = velocity * cos(angle_rad);
        double vy = velocity * sin(angle_rad);
        
        double time_to_max = vy / 9.81;
        double max_height = (vy * vy) / (2 * 9.81);
        double total_time = 2 * time_to_max;
        double range = vx * total_time;
        
        cout << "Initial velocity: " << velocity << " m/s" << endl;
        cout << "Launch angle: " << angle_deg << "°" << endl;
        cout << "Maximum height: " << max_height << " m" << endl;
        cout << "Range: " << range << " m" << endl;
        cout << "Time of flight: " << total_time << " s" << endl;
    }
    
    // Calculate simple pendulum period
    static double pendulumPeriod(double length) {
        return 2 * M_PI * sqrt(length / 9.81);
    }
    
    // Calculate kinetic energy
    static double kineticEnergy(double mass, double velocity) {
        return 0.5 * mass * velocity * velocity;
    }
};

int main() {
    // Projectile motion
    Physics::projectile(30.0, 45.0);
    cout << endl;
    
    // Pendulum period
    double length = 1.0;  // 1 meter
    cout << "Pendulum period (L=1m): " << Physics::pendulumPeriod(length) << " s" << endl;
    
    // Kinetic energy
    double mass = 1000.0;  // 1000 kg
    double velocity = 20.0;  // 20 m/s
    cout << "Kinetic energy (1000kg at 20m/s): " << Physics::kineticEnergy(mass, velocity) << " J" << endl;
    
    return 0;
}
```

### Example 3: Statistical Functions
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

class Statistics {
public:
    // Calculate mean
    static double mean(const vector<double>& data) {
        double sum = 0.0;
        for (double x : data) {
            sum += x;
        }
        return sum / data.size();
    }
    
    // Calculate standard deviation
    static double standardDeviation(const vector<double>& data) {
        double m = mean(data);
        double sum_sq_diff = 0.0;
        
        for (double x : data) {
            sum_sq_diff += pow(x - m, 2);
        }
        
        return sqrt(sum_sq_diff / data.size());
    }
    
    // Calculate correlation coefficient
    static double correlation(const vector<double>& x, const vector<double>& y) {
        if (x.size() != y.size()) return NAN;
        
        double mx = mean(x);
        double my = mean(y);
        
        double numerator = 0.0;
        double sum_x_sq = 0.0;
        double sum_y_sq = 0.0;
        
        for (size_t i = 0; i < x.size(); i++) {
            double dx = x[i] - mx;
            double dy = y[i] - my;
            numerator += dx * dy;
            sum_x_sq += dx * dx;
            sum_y_sq += dy * dy;
        }
        
        double denominator = sqrt(sum_x_sq * sum_y_sq);
        return numerator / denominator;
    }
};

int main() {
    vector<double> data1 = {1, 2, 3, 4, 5};
    vector<double> data2 = {2, 4, 6, 8, 10};
    
    cout << "Data 1: ";
    for (double x : data1) cout << x << " ";
    cout << endl;
    
    cout << "Data 2: ";
    for (double x : data2) cout << x << " ";
    cout << endl;
    
    cout << "Mean of data 1: " << Statistics::mean(data1) << endl;
    cout << "Std dev of data 1: " << Statistics::standardDeviation(data1) << endl;
    cout << "Correlation: " << Statistics::correlation(data1, data2) << endl;
    
    return 0;
}
```

### Example 4: Number Theory Functions
```cpp
#include <iostream>
#include <cmath>
#include <vector>

class NumberTheory {
public:
    // Check if a number is prime
    static bool isPrime(int n) {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        
        for (int i = 3; i <= sqrt(n); i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
    
    // Calculate greatest common divisor
    static int gcd(int a, int b) {
        a = abs(a);
        b = abs(b);
        
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    
    // Calculate least common multiple
    static int lcm(int a, int b) {
        return abs(a * b) / gcd(a, b);
    }
    
    // Generate prime numbers up to n using Sieve of Eratosthenes
    static vector<int> sieveOfEratosthenes(int n) {
        vector<bool> is_prime(n + 1, true);
        is_prime[0] = is_prime[1] = false;
        
        for (int p = 2; p * p <= n; p++) {
            if (is_prime[p]) {
                for (int i = p * p; i <= n; i += p) {
                    is_prime[i] = false;
                }
            }
        }
        
        vector<int> primes;
        for (int i = 2; i <= n; i++) {
            if (is_prime[i]) {
                primes.push_back(i);
            }
        }
        
        return primes;
    }
};

int main() {
    // Prime checking
    int num = 17;
    cout << num << " is " << (NumberTheory::isPrime(num) ? "prime" : "not prime") << endl;
    
    // GCD and LCM
    int a = 24, b = 36;
    cout << "GCD(" << a << ", " << b << ") = " << NumberTheory::gcd(a, b) << endl;
    cout << "LCM(" << a << ", " << b << ") = " << NumberTheory::lcm(a, b) << endl;
    
    // Generate primes
    vector<int> primes = NumberTheory::sieveOfEratosthenes(50);
    cout << "Primes up to 50: ";
    for (int p : primes) {
        cout << p << " ";
    }
    cout << endl;
    
    return 0;
}
```

## ⚡ Rounding Functions

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>

int main() {
    double x = 3.7;
    double y = -3.7;
    double z = 3.3;
    
    cout << fixed << setprecision(1);
    
    // Basic rounding
    cout << "round(" << x << ") = " << round(x) << endl;    // 4.0
    cout << "round(" << y << ") = " << round(y) << endl;    // -4.0
    cout << "round(" << z << ") = " << round(z) << endl;    // 3.0
    
    // Floor (round down)
    cout << "floor(" << x << ") = " << floor(x) << endl;    // 3.0
    cout << "floor(" << y << ") = " << floor(y) << endl;    // -4.0
    
    // Ceil (round up)
    cout << "ceil(" << x << ") = " << ceil(x) << endl;      // 4.0
    cout << "ceil(" << y << ") = " << ceil(y) << endl;      // -3.0
    
    // Truncate (round toward zero)
    cout << "trunc(" << x << ") = " << trunc(x) << endl;    // 3.0
    cout << "trunc(" << y << ") = " << trunc(y) << endl;    // -3.0
    
    return 0;
}
```

## 🎯 Common Mathematical Patterns

### Pattern 1: Safe Square Root
```cpp
double safeSqrt(double x) {
    if (x < 0) {
        return NAN;  // Not a Number
    }
    return sqrt(x);
}
```

### Pattern 2: Angle Conversion
```cpp
double degreesToRadians(double degrees) {
    return degrees * M_PI / 180.0;
}

double radiansToDegrees(double radians) {
    return radians * 180.0 / M_PI;
}
```

### Pattern 3: Power with Error Handling
```cpp
double safePow(double base, double exponent) {
    if (base < 0 && exponent != floor(exponent)) {
        return NAN;  // Complex result
    }
    return pow(base, exponent);
}
```

## 🐛 Common Pitfalls & Solutions

### 1. Division by Zero
```cpp
// Problem
double result = x / y;  // Crash if y = 0

// Solution
double safeDivide(double x, double y) {
    if (fabs(y) < 1e-10) {  // Check for near-zero
        return INFINITY;
    }
    return x / y;
}
```

### 2. Domain Errors
```cpp
// Problem
double result = sqrt(-1);  // Returns NaN
double result2 = log(0);   // Returns -INF

// Solution
double safeLog(double x) {
    if (x <= 0) {
        return NAN;
    }
    return log(x);
}
```

### 3. Floating Point Comparison
```cpp
// Problem
if (a == b) { /* rarely works with floating point */ }

// Solution
bool approximatelyEqual(double a, double b, double epsilon = 1e-10) {
    return fabs(a - b) < epsilon;
}
```

## 🎨 Advanced Mathematical Functions

### Custom Statistical Functions
```cpp
class AdvancedMath {
public:
    // Calculate factorial
    static double factorial(int n) {
        if (n < 0) return NAN;
        if (n == 0 || n == 1) return 1.0;
        
        double result = 1.0;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
    
    // Calculate combination (nCr)
    static double combination(int n, int r) {
        if (r > n || r < 0) return 0.0;
        return factorial(n) / (factorial(r) * factorial(n - r));
    }
    
    // Calculate permutation (nPr)
    static double permutation(int n, int r) {
        if (r > n || r < 0) return 0.0;
        return factorial(n) / factorial(n - r);
    }
};
```

## 📚 Mathematical Constants

```cpp
#include <cmath>

// Common constants
const double PI = M_PI;           // 3.14159...
const double E = M_E;             // 2.71828...
const double LN2 = M_LN2;         // ln(2) = 0.693...
const double LN10 = M_LN10;       // ln(10) = 2.302...
const double SQRT2 = M_SQRT2;     // sqrt(2) = 1.414...
const double SQRT1_2 = M_SQRT1_2; // 1/sqrt(2) = 0.707...
```

## 🚀 Best Practices

1. **Check domain validity** before calling functions like `sqrt` and `log`
2. **Use appropriate comparison** for floating-point numbers
3. **Handle special values** (INF, NAN) appropriately
4. **Use radians** for trigonometric functions
5. **Consider performance** for complex calculations
6. **Use `fabs` instead of `abs`** for floating-point numbers

## 🎯 When to Use cmath

✅ **Use cmath when:**
- Performing mathematical calculations
- Working with geometry or physics problems
- Need statistical functions
- Implementing algorithms requiring math operations
- Working with graphics or game development

❌ **Avoid when:**
- Simple integer arithmetic is sufficient
- Performance is critical and you can use approximations
- You need arbitrary precision arithmetic
---

## Next Step

- Go to [06_cstdlib.md](06_cstdlib.md) to continue with cstdlib.
