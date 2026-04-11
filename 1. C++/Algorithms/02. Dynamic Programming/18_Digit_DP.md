# 18_Digit_DP.md

## Digit DP

### Definition

Digit DP is a technique used to solve problems involving digits of numbers. It is used to count numbers between a given range that satisfy certain digit-based conditions.

### When to Use Digit DP

Problems that ask:

- Count numbers from L to R with a certain digit property
- Sum of digits, product of digits
- Numbers with no consecutive 1s
- Numbers divisible by something
- Numbers with digit sum = K

### Key Concept

We process numbers digit by digit from most significant digit (MSD) to least significant digit (LSD). The state typically includes:

- `pos`: current digit position we are processing
- `tight`: whether we are bound by the prefix of the limit number
- `started`: whether we have started placing non-leading zeros
- Other constraints (sum, count, etc.)

### Basic Template

```cpp
// Convert number to digits array
vector<int> digits;
while (num > 0) {
    digits.push_back(num % 10);
    num /= 10;
}
reverse(digits.begin(), digits.end());
int n = digits.size();

// DP state: pos, tight, started, additional parameters
vector<vector<vector<vector<int>>>> memo(...);

int dfs(int pos, int tight, int started, ...) {
    if (pos == n) {
        // Base case: all digits processed
        return (started ? 1 : 0);  // or other condition
    }
    
    if (memo[pos][tight][started][...] != -1) {
        return memo[pos][tight][started][...];
    }
    
    int limit = tight ? digits[pos] : 9;
    int ans = 0;
    
    for (int dig = 0; dig <= limit; dig++) {
        int newTight = tight && (dig == limit);
        int newStarted = started || (dig != 0);
        
        // Additional constraints
        // newSum = sum + dig, newCount = count + (dig == something), etc.
        
        ans += dfs(pos + 1, newTight, newStarted, ...);
    }
    
    return memo[pos][tight][started][...] = ans;
}

// Result = dfs(0, 1, 0, ...)
```

### Problem 1: Count Numbers with Digit Sum <= K

**Problem:** Count numbers from 0 to N whose sum of digits is ≤ K.

```cpp
int countNumbersWithDigitSum(int N, int K) {
    string s = to_string(N);
    int n = s.length();
    
    // dp[pos][tight][sum]
    vector<vector<vector<int>>> memo(n+1, 
        vector<vector<int>>(2, 
            vector<int>(K+1, -1)));
    
    function<int(int, bool, int)> dfs = [&](int pos, bool tight, int sum) {
        if (sum > K) return 0;
        if (pos == n) return 1;
        
        if (memo[pos][tight][sum] != -1) {
            return memo[pos][tight][sum];
        }
        
        int limit = tight ? (s[pos] - '0') : 9;
        int ans = 0;
        
        for (int dig = 0; dig <= limit; dig++) {
            bool newTight = tight && (dig == limit);
            ans += dfs(pos + 1, newTight, sum + dig);
        }
        
        return memo[pos][tight][sum] = ans;
    };
    
    return dfs(0, true, 0);
}
```

### Problem 2: Count Numbers with No Consecutive 1s in Binary

**Problem:** Count numbers from 0 to N that have no two consecutive 1s in their binary representation.

```cpp
int countNoConsecutiveOnes(int N) {
    string binary = "";
    int temp = N;
    while (temp > 0) {
        binary = char('0' + (temp % 2)) + binary;
        temp /= 2;
    }
    int n = binary.length();
    
    // dp[pos][tight][prev]
    vector<vector<vector<int>>> memo(n+1, 
        vector<vector<int>>(2, 
            vector<int>(2, -1)));
    
    function<int(int, bool, int)> dfs = [&](int pos, bool tight, int prev) {
        if (pos == n) return 1;
        
        if (memo[pos][tight][prev] != -1) {
            return memo[pos][tight][prev];
        }
        
        int limit = tight ? (binary[pos] - '0') : 1;
        int ans = 0;
        
        for (int dig = 0; dig <= limit; dig++) {
            if (prev == 1 && dig == 1) continue;  // two consecutive 1s
            
            bool newTight = tight && (dig == limit);
            ans += dfs(pos + 1, newTight, dig);
        }
        
        return memo[pos][tight][prev] = ans;
    };
    
    return dfs(0, true, 0);
}
```

### Problem 3: Count Numbers Divisible by K

**Problem:** Count numbers from 0 to N that are divisible by K.

```cpp
int countDivisibleByK(int N, int K) {
    string s = to_string(N);
    int n = s.length();
    
    // dp[pos][tight][rem]
    vector<vector<vector<int>>> memo(n+1, 
        vector<vector<int>>(2, 
            vector<int>(K, -1)));
    
    function<int(int, bool, int)> dfs = [&](int pos, bool tight, int rem) {
        if (pos == n) {
            return (rem == 0) ? 1 : 0;
        }
        
        if (memo[pos][tight][rem] != -1) {
            return memo[pos][tight][rem];
        }
        
        int limit = tight ? (s[pos] - '0') : 9;
        int ans = 0;
        
        for (int dig = 0; dig <= limit; dig++) {
            bool newTight = tight && (dig == limit);
            int newRem = (rem * 10 + dig) % K;
            ans += dfs(pos + 1, newTight, newRem);
        }
        
        return memo[pos][tight][rem] = ans;
    };
    
    return dfs(0, true, 0);
}
```

### Problem 4: Count Numbers with Even Number of Odd Digits

**Problem:** Count numbers from 0 to N that have an even number of odd digits.

```cpp
int countEvenOddDigits(int N) {
    string s = to_string(N);
    int n = s.length();
    
    // dp[pos][tight][started][oddCountParity]
    vector<vector<vector<vector<int>>>> memo(n+1, 
        vector<vector<vector<int>>>(2, 
            vector<vector<int>>(2, 
                vector<int>(2, -1))));
    
    function<int(int, bool, bool, int)> dfs = [&](int pos, bool tight, bool started, int oddParity) {
        if (pos == n) {
            return (started && oddParity == 0) ? 1 : 0;
        }
        
        if (memo[pos][tight][started][oddParity] != -1) {
            return memo[pos][tight][started][oddParity];
        }
        
        int limit = tight ? (s[pos] - '0') : 9;
        int ans = 0;
        
        for (int dig = 0; dig <= limit; dig++) {
            bool newTight = tight && (dig == limit);
            bool newStarted = started || (dig != 0);
            int newParity = oddParity;
            
            if (newStarted && (dig % 2 == 1)) {
                newParity ^= 1;  // flip parity
            }
            
            ans += dfs(pos + 1, newTight, newStarted, newParity);
        }
        
        return memo[pos][tight][started][oddParity] = ans;
    };
    
    return dfs(0, true, false, 0);
}
```

### Problem 5: Count Numbers with Special Digit Constraints

**Problem:** Count numbers where digit at even positions is even and digit at odd positions is odd.

```cpp
int countEvenOddPositionDigits(int N) {
    string s = to_string(N);
    int n = s.length();
    
    // dp[pos][tight][started]
    vector<vector<vector<int>>> memo(n+1, 
        vector<vector<int>>(2, 
            vector<int>(2, -1)));
    
    function<int(int, bool, bool)> dfs = [&](int pos, bool tight, bool started) {
        if (pos == n) {
            return started ? 1 : 0;
        }
        
        if (memo[pos][tight][started] != -1) {
            return memo[pos][tight][started];
        }
        
        int limit = tight ? (s[pos] - '0') : 9;
        int ans = 0;
        
        for (int dig = 0; dig <= limit; dig++) {
            bool newTight = tight && (dig == limit);
            bool newStarted = started || (dig != 0);
            
            if (!newStarted) {
                ans += dfs(pos + 1, newTight, false);
            } else {
                // Even position (0-indexed from left)
                if (pos % 2 == 0) {
                    if (dig % 2 == 0) {
                        ans += dfs(pos + 1, newTight, true);
                    }
                } else {
                    if (dig % 2 == 1) {
                        ans += dfs(pos + 1, newTight, true);
                    }
                }
            }
        }
        
        return memo[pos][tight][started] = ans;
    };
    
    return dfs(0, true, false);
}
```

### Problem 6: Sum of Digits of Numbers from L to R

**Problem:** Find sum of digits of all numbers from L to R.

```cpp
long long sumOfDigits(int N) {
    string s = to_string(N);
    int n = s.length();
    
    // dp[pos][tight][sum] - but sum can be large, so we use another approach
    // Better: count how many times each digit appears
    
    vector<vector<vector<long long>>> memo(n+1, 
        vector<vector<long long>>(2, 
            vector<long long>(2, -1)));
    
    function<long long(int, bool, bool)> countNumbers = [&](int pos, bool tight, bool started) {
        if (pos == n) return 1LL;
        if (memo[pos][tight][started] != -1) return memo[pos][tight][started];
        
        int limit = tight ? (s[pos] - '0') : 9;
        long long ans = 0;
        
        for (int dig = 0; dig <= limit; dig++) {
            bool newTight = tight && (dig == limit);
            bool newStarted = started || (dig != 0);
            ans += countNumbers(pos + 1, newTight, newStarted);
        }
        
        return memo[pos][tight][started] = ans;
    };
    
    function<long long(int, bool, bool, int)> sumOfDigitsAtPos = [&](int pos, bool tight, bool started, int targetPos) {
        if (pos == n) return 0LL;
        
        int limit = tight ? (s[pos] - '0') : 9;
        long long ans = 0;
        
        for (int dig = 0; dig <= limit; dig++) {
            bool newTight = tight && (dig == limit);
            bool newStarted = started || (dig != 0);
            
            if (pos == targetPos && newStarted) {
                ans += dig * countNumbers(pos + 1, newTight, newStarted);
            }
            ans += sumOfDigitsAtPos(pos + 1, newTight, newStarted, targetPos);
        }
        
        return ans;
    };
    
    long long total = 0;
    for (int i = 0; i < n; i++) {
        total += sumOfDigitsAtPos(0, true, false, i);
    }
    
    return total;
}

long long sumOfDigitsRange(int L, int R) {
    return sumOfDigits(R) - sumOfDigits(L - 1);
}
```

### Problem 7: Count Numbers with Digit Product <= K

**Problem:** Count numbers from 0 to N where product of digits ≤ K.

```cpp
int countDigitProduct(int N, int K) {
    string s = to_string(N);
    int n = s.length();
    
    // Use map for product state (can be large)
    map<tuple<int, bool, bool, int>, int> memo;
    
    function<int(int, bool, bool, int)> dfs = [&](int pos, bool tight, bool started, int product) {
        if (product > K) return 0;
        if (pos == n) {
            return started ? 1 : 0;
        }
        
        auto key = make_tuple(pos, tight, started, product);
        if (memo.count(key)) return memo[key];
        
        int limit = tight ? (s[pos] - '0') : 9;
        int ans = 0;
        
        for (int dig = 0; dig <= limit; dig++) {
            bool newTight = tight && (dig == limit);
            bool newStarted = started || (dig != 0);
            int newProduct = newStarted ? (product * (dig == 0 ? 1 : dig)) : product;
            ans += dfs(pos + 1, newTight, newStarted, newProduct);
        }
        
        return memo[key] = ans;
    };
    
    return dfs(0, true, false, 1);
}
```

### State Dimensions Summary

| Problem | State Parameters |
|---------|------------------|
| Digit Sum | pos, tight, sum |
| Divisible by K | pos, tight, remainder |
| No Consecutive 1s | pos, tight, prevDigit |
| Even/Odd Digits | pos, tight, started, parity |
| Digit Product | pos, tight, started, product |
