# Array Rotation

## Introduction
Array rotation involves shifting the elements of an array to the left or right by `k` positions.

## 1. Left Rotation (by k)
`[1, 2, 3, 4, 5]` left rotated by 2 → `[3, 4, 5, 1, 2]`

### Method 1: Extra Space (O(N) Time, O(N) Space)
Create a new array and copy `arr[i]` to `new_arr[(i - k + n) % n]`.

### Method 2: Reverse Algorithm (O(N) Time, O(1) Space)
1. Reverse first `k` elements: `[2, 1, 3, 4, 5]`
2. Reverse remaining `n-k` elements: `[2, 1, 5, 4, 3]`
3. Reverse entire array: `[3, 4, 5, 1, 2]`

**C++ Code (Reverse Algorithm)**:
```cpp
void rotateLeft(vector<int>& arr, int k) {
    int n = arr.size();
    k %= n;
    reverse(arr.begin(), arr.begin() + k);
    reverse(arr.begin() + k, arr.end());
    reverse(arr.begin(), arr.end());
}
```

## 2. Right Rotation (by k)
`[1, 2, 3, 4, 5]` right rotated by 2 → `[4, 5, 1, 2, 3]`

### Method: Reverse Algorithm
1. Reverse first `n-k` elements.
2. Reverse remaining `k` elements.
3. Reverse entire array.

## Juggling Algorithm (O(N) Time, O(1) Space)
A more mathematical approach using the GCD of `n` and `k`. It shifts elements in cycles.

## Key Considerations
- `k` should be taken modulo `n` (`k = k % n`).
- Handle cases where `n=1` or `k=0`.
- Rotation is a special case of cyclic permutation.

## Complexity Summary
- **Time Complexity**: O(N) for all efficient methods.
- **Space Complexity**: 
  - O(1) for Reversal and Juggling algorithms.
  - O(N) if using an auxiliary array.

## Use Cases
- Sliding Window applications where elements circularity is required.
- Scheduling and round-robin tasks.
- Image processing (shifting pixels).
- Cryptographic permutations.
---

## Next Step

- Go to [05_Subarray_Problems.md](05_Subarray_Problems.md) to continue with Subarray Problems.
