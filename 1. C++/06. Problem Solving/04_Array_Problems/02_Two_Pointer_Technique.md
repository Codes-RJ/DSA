# Two-Pointer Technique: Efficiency and Optimization

## Overview
The two-pointer technique is an essential optimization pattern that reduces the number of operations by using two separate indices to traverse a data structure (usually an array or linked list). By coordinating the pointer movements based on local conditions, we can solve problems in $O(N)$ that would otherwise require $O(N^2)$.

---

## 1. Multi-Dimensional Sums (Pairs, Triplets)

### Finding a Pair with Target Sum (2-Pointer)
Already discussed, but essential to note that the array **must be sorted**. If not, sorting it first ($O(N \log N)$) followed by 2-pointers ($O(N)$) is still better than brute force ($O(N^2)$).

### Finding Triplets with Sum Zero (3nd Pointer)
**Strategy**: For each element `i`, use the Two-Pointer technique on the remaining part of the array to find pairs that sum to `-arr[i]`.

```cpp
vector<vector<int>> findTriplets(vector<int>& arr) {
    int n = arr.size();
    sort(arr.begin(), arr.end());
    vector<vector<int>> res;

    for (int i = 0; i < n - 2; i++) {
        // Skip duplicates for the first element
        if (i > 0 && arr[i] == arr[i - 1]) continue;

        int l = i + 1, r = n - 1;
        while (l < r) {
            int sum = arr[i] + arr[l] + arr[r];
            if (sum == 0) {
                res.push_back({arr[i], arr[l], arr[r]});
                // Skip duplicates for second and third elements
                while (l < r && arr[l] == arr[l + 1]) l++;
                while (l < r && arr[r] == arr[r - 1]) r--;
                l++; r--;
            } else if (sum < 0) l++;
            else r--;
        }
    }
    return res;
}
```

---

## 2. Partitioning: Dutch National Flag Algorithm
A specialized version using three pointers (`low`, `mid`, `high`) to sort an array of three distinct values (like 0s, 1s, and 2s) in a single pass.

```cpp
void sortColors(vector<int>& arr) {
    int low = 0, mid = 0, high = arr.size() - 1;
    while (mid <= high) {
        if (arr[mid] == 0) {
            swap(arr[low++], arr[mid++]);
        } else if (arr[mid] == 1) {
            mid++;
        } else {
            swap(arr[mid], arr[high--]); // Don't increment mid yet!
        }
    }
}
```

---

## 3. String Processing with Two Pointers

### Reverse Vowels
Find vowels from both ends and swap them. This skips consonants and only processes necessary characters.
```cpp
string reverseVowels(string s) {
    string vowels = "aeiouAEIOU";
    int l = 0, r = s.length() - 1;
    while (l < r) {
        while (l < r && vowels.find(s[l]) == string::npos) l++;
        while (l < r && vowels.find(s[r]) == string::npos) r--;
        swap(s[l++], s[r--]);
    }
    return s;
}
```

---

## 4. Sorting Squares: $O(N)$ for Sorted Mixed Arrays
Given a sorted array containing negative numbers, create a sorted array of their squares.
- **Problem**: $(-5)^2 = 25$ is larger than $(2)^2 = 4$. Negative numbers can become the largest when squared.
- **Solution**: Use two pointers at both ends to find the largest squared value and fill the result array from back to front.

```cpp
vector<int> sortedSquares(vector<int>& arr) {
    int n = arr.size();
    vector<int> res(n);
    int l = 0, r = n - 1, idx = n - 1;
    while (l <= r) {
        if (abs(arr[l]) > abs(arr[r])) {
            res[idx--] = arr[l] * arr[l++];
        } else {
            res[idx--] = arr[r] * arr[r--];
        }
    }
    return res;
}
```

---

## 5. Summary and Limitations

| Variation | Purpose | Time | Space |
|-----------|---------|------|-------|
| **Opposite Pointer** | Finding pairs, target sums | $O(N)$ | $O(1)$ |
| **Slower Pointer** | Linked list center, cycle detection | $O(N)$ | $O(1)$ |
| **Three Pointer** | Triplet sums, Flag sorting | $O(N^2)$ / $O(N)$ | $O(1)$ |

### Corner Cases
- **No duplicates skipped**: Could lead to infinite loops or incorrect counts.
- **Index Out of Range**: Always verify `l < r` or `curr != nullptr` inside inner loops.
- **Empty Arrays**: Simple `if` check at the start.
- **All same values**: Pointer logic must handle this without unnecessary swaps or increments.
---

## Next Step

- Go to [03_Sliding_Window.md](03_Sliding_Window.md) to continue with Sliding Window.
