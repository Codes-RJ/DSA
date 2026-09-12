# Product of Array Except Self in C++ - Division-Free Prefix and Suffix Accumulators

## 1. Introduction & Theoretical Foundations

The **Product of Array Except Self** problem requires calculating an array `answer` such that `answer[i]` is equal to the product of all elements of the input array `nums` except `nums[i]`.

### Critical Constraints:
1. The algorithm must run in **$O(N)$ linear time**.
2. The algorithm **cannot use the division operation `/`**.
3. The algorithm should use **$O(1)$ auxiliary space** (the output array does not count as extra space).

```
Input:   nums   = [ 1,   2,   3,   4 ]

Prefix:           [ 1,   1,   2,   6 ]  (Product of all elements to the left)
Suffix:           [ 24,  12,  4,   1 ]  (Product of all elements to the right)

Product: answer = [ 24,  12,  8,   6 ]
```

---

## 2. Mathematical Formulation & Space Optimization

For any element at index $i$:
$$\text{answer}[i] = \left( \prod_{j=0}^{i-1} \text{nums}[j] \right) \times \left( \prod_{j=i+1}^{N-1} \text{nums}[j] \right) = \text{Prefix}[i] \times \text{Suffix}[i]$$

### Naive Division Fallacy
While one could multiply all numbers to get $\text{TotalProduct}$ and set $\text{answer}[i] = \text{TotalProduct} / \text{nums}[i]$:
1. **Division by Zero**: If any element is $0$, division by zero causes runtime crashes.
2. **Multiple Zeroes**: If the array has $\ge 2$ zeroes, every element in the output is strictly $0$.
3. **Constraint Violation**: The problem strictly forbids division.

### The Two-Pass In-Place Accumulator ($O(1)$ Extra Space)
We eliminate the $O(N)$ prefix and suffix arrays by reusing the output buffer:

1. **Pass 1 (Left to Right)**:
   Store prefix products directly in `answer`:
   - `answer[0] = 1`
   - `answer[i] = answer[i - 1] * nums[i - 1]`
2. **Pass 2 (Right to Left)**:
   Maintain a single running scalar `suffix = 1`:
   - Multiply `answer[i]` by `suffix`: `answer[i] *= suffix`
   - Update `suffix *= nums[i]`

---

## 3. Production-Grade C++ Implementation

```cpp
#include <iostream>
#include <vector>

class ProductArray {
public:
    // O(N) Time, O(1) Auxiliary Space (excluding output array)
    static std::vector<int> productExceptSelf(const std::vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return {};

        std::vector<int> answer(n, 1);

        // Pass 1: answer[i] contains product of all elements to the left of i
        int prefix = 1;
        for (int i = 0; i < n; ++i) {
            answer[i] = prefix;
            prefix *= nums[i];
        }

        // Pass 2: Multiply by running product of all elements to the right of i
        int suffix = 1;
        for (int i = n - 1; i >= 0; --i) {
            answer[i] *= suffix;
            suffix *= nums[i];
        }

        return answer;
    }
};
```

---

## 4. Complete Runnable Verification Suite

```cpp
#include <iostream>
#include <vector>

void printVec(const std::vector<int>& v) {
    std::cout << "[ ";
    for (size_t i = 0; i < v.size(); ++i) {
        std::cout << v[i] << (i + 1 < v.size() ? ", " : " ");
    }
    std::cout << "]" << std::endl;
}

int main() {
    std::cout << "=====================================================" << std::endl;
    std::cout << "       PRODUCT OF ARRAY EXCEPT SELF SUITE            " << std::endl;
    std::cout << "=====================================================" << std::endl;

    // --- 1. Standard Case ---
    std::cout << "\n[1] STANDARD ARRAY {1, 2, 3, 4}:" << std::endl;
    std::vector<int> nums1 = {1, 2, 3, 4};
    std::cout << "  Input:    ";
    printVec(nums1);
    auto res1 = ProductArray::productExceptSelf(nums1);
    std::cout << "  Output:   ";
    printVec(res1);
    std::cout << "  Expected: [ 24, 12, 8, 6 ]" << std::endl;

    // --- 2. Single Zero in Array ---
    std::cout << "\n[2] SINGLE ZERO IN ARRAY {-1, 1, 0, -3, 3}:" << std::endl;
    std::vector<int> nums2 = {-1, 1, 0, -3, 3};
    std::cout << "  Input:    ";
    printVec(nums2);
    auto res2 = ProductArray::productExceptSelf(nums2);
    std::cout << "  Output:   ";
    printVec(res2);
    std::cout << "  Expected: [ 0, 0, 9, 0, 0 ]" << std::endl;

    // --- 3. Multiple Zeroes in Array ---
    std::cout << "\n[3] MULTIPLE ZEROES {0, 4, 0}:" << std::endl;
    std::vector<int> nums3 = {0, 4, 0};
    std::cout << "  Input:    ";
    printVec(nums3);
    auto res3 = ProductArray::productExceptSelf(nums3);
    std::cout << "  Output:   ";
    printVec(res3);
    std::cout << "  Expected: [ 0, 0, 0 ]" << std::endl;

    std::cout << "\n=====================================================" << std::endl;
    return 0;
}
```

---

## 5. Complexity Analysis Table

| Method | Time Complexity | Auxiliary Space | Handles Zeroes? | Uses Division? |
| :--- | :--- | :--- | :--- | :--- |
| **Total Product / Division** | $O(N)$ | $O(1)$ | Fails on $\ge 1$ Zero | Yes (Forbidden) |
| **Separate Prefix/Suffix Arrays** | $O(N)$ | $O(N)$ extra | Fully robust | No |
| **In-Place Two-Pass Accumulator** | $O(N)$ | $O(1)$ extra | Fully robust | No (Optimal) |

---

## 6. Common Pitfalls & Edge Cases

1. **Integer Overflow with Large Products**: If intermediate products exceed $2^{31} - 1$, use `long long` accumulators to prevent undefined behavior.
2. **Forgetting to Initialize Output with 1**: `answer[0]` must begin with `1` because there are no elements to the left of the first item (identity element of multiplication).
3. **Pass 2 Premature Suffix Multiplication**: Multiplying `suffix *= nums[i]` before multiplying into `answer[i]` mistakenly includes `nums[i]` in its own output product! Always multiply `answer[i] *= suffix` first.

---

## Next Step

- Proceed to [10_Find_Duplicate_Number.md](10_Find_Duplicate_Number.md) to explore Floyd's cycle detection applied directly to array indices in $O(N)$ time and $O(1)$ space.
