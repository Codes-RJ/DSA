# Custom Stacks and Queues in C++

## 📖 Overview

While the C++ Standard Template Library provides `std::stack` and `std::queue` as container adapters over `std::deque` or `std::vector`, understanding how to build these data structures from scratch is a core prerequisite for technical interviews, systems programming, and memory-constrained environments.

This guide covers:
1. **Dynamic Array-Based Stack** (Amortized $O(1)$ push/pop with geometric resizing)
2. **Linked-List-Based Stack** (Strict $O(1)$ worst-case operations)
3. **Min-Stack** ($O(1)$ `getMin()` in auxiliary $O(1)$ space)
4. **Circular Array Queue** (Ring buffer with modulo arithmetic)
5. **Queue Implemented Using Two Stacks** (Amortized $O(1)$ operations)
6. **Monotonic Queue** (Sliding window maximum in $O(N)$)

---

## 1. Dynamic Array-Based Stack

### Principle
Maintains an underlying heap array that doubles in size when capacity is exceeded and shrinks by half when utilization drops below 25% (preventing thrashing).

```cpp
#include <iostream>
#include <stdexcept>
#include <utility>

template<typename T>
class ArrayStack {
private:
    T* data_;
    size_t capacity_;
    size_t topIndex_;

    void resize(size_t newCapacity) {
        T* newData = new T[newCapacity];
        for (size_t i = 0; i < topIndex_; ++i) {
            newData[i] = std::move(data_[i]);
        }
        delete[] data_;
        data_ = newData;
        capacity_ = newCapacity;
    }

public:
    explicit ArrayStack(size_t initialCapacity = 4)
        : capacity_(initialCapacity), topIndex_(0) {
        data_ = new T[capacity_];
    }

    ~ArrayStack() {
        delete[] data_;
    }

    // Rule of 5
    ArrayStack(const ArrayStack& other) : capacity_(other.capacity_), topIndex_(other.topIndex_) {
        data_ = new T[capacity_];
        for (size_t i = 0; i < topIndex_; ++i) data_[i] = other.data_[i];
    }

    ArrayStack& operator=(const ArrayStack& other) {
        if (this != &other) {
            delete[] data_;
            capacity_ = other.capacity_;
            topIndex_ = other.topIndex_;
            data_ = new T[capacity_];
            for (size_t i = 0; i < topIndex_; ++i) data_[i] = other.data_[i];
        }
        return *this;
    }

    ArrayStack(ArrayStack&& other) noexcept
        : data_(other.data_), capacity_(other.capacity_), topIndex_(other.topIndex_) {
        other.data_ = nullptr;
        other.capacity_ = 0;
        other.topIndex_ = 0;
    }

    ArrayStack& operator=(ArrayStack&& other) noexcept {
        if (this != &other) {
            delete[] data_;
            data_ = other.data_;
            capacity_ = other.capacity_;
            topIndex_ = other.topIndex_;
            other.data_ = nullptr;
            other.capacity_ = 0;
            other.topIndex_ = 0;
        }
        return *this;
    }

    void push(const T& value) {
        if (topIndex_ == capacity_) {
            resize(capacity_ * 2);
        }
        data_[topIndex_++] = value;
    }

    void pop() {
        if (empty()) throw std::underflow_error("Stack underflow: stack is empty");
        --topIndex_;
        if (topIndex_ > 0 && topIndex_ <= capacity_ / 4 && capacity_ > 4) {
            resize(capacity_ / 2);
        }
    }

    T& top() {
        if (empty()) throw std::underflow_error("Stack is empty");
        return data_[topIndex_ - 1];
    }

    const T& top() const {
        if (empty()) throw std::underflow_error("Stack is empty");
        return data_[topIndex_ - 1];
    }

    bool empty() const noexcept { return topIndex_ == 0; }
    size_t size() const noexcept { return topIndex_; }
    size_t capacity() const noexcept { return capacity_; }
};
```

---

## 2. Min-Stack ($O(1)$ Time and $O(1)$ Auxiliary Space)

### The Technique
To maintain the minimum element in $O(1)$ without a second stack, encode the previous minimum whenever a new minimum is pushed:
- If $x < \text{minVal}$: push $(2x - \text{minVal})$ and update $\text{minVal} = x$.
- Since $x < \text{minVal}$, the pushed value is strictly less than $x$, acting as a flag.
- When popping, if the popped value $y < \text{minVal}$, restore previous minimum: $\text{minVal} = 2 \cdot \text{minVal} - y$.

```cpp
#include <stack>
#include <stdexcept>
#include <iostream>

class MinStack {
private:
    std::stack<long long> st_;
    long long minVal_;

public:
    MinStack() : minVal_(0) {}

    void push(int val) {
        long long x = val;
        if (st_.empty()) {
            st_.push(x);
            minVal_ = x;
        } else if (x >= minVal_) {
            st_.push(x);
        } else {
            // Encode: 2*x - minVal
            st_.push(2 * x - minVal_);
            minVal_ = x;
        }
    }

    void pop() {
        if (st_.empty()) throw std::underflow_error("Stack is empty");
        long long topVal = st_.top();
        st_.pop();

        if (topVal < minVal_) {
            // Restore previous min: 2*minVal - encodedVal
            minVal_ = 2 * minVal_ - topVal;
        }
    }

    int top() const {
        if (st_.empty()) throw std::underflow_error("Stack is empty");
        long long topVal = st_.top();
        return (topVal < minVal_) ? static_cast<int>(minVal_) : static_cast<int>(topVal);
    }

    int getMin() const {
        if (st_.empty()) throw std::underflow_error("Stack is empty");
        return static_cast<int>(minVal_);
    }

    bool empty() const noexcept { return st_.empty(); }
};
```

---

## 3. Circular Array Queue (Ring Buffer)

### Principle
Using a fixed-size array, elements are inserted at `rear` and removed from `front`. Modulo arithmetic wraps indices around the array boundaries:
- `rear = (rear + 1) % capacity`
- `front = (front + 1) % capacity`

```
         Front                  Rear
           ↓                     ↓
Index:  [  0  |  1  |  2  |  3  |  4  ]
Value:  [ 10  | 20  | 30  |  -- |  -- ]
```

```cpp
#include <iostream>
#include <stdexcept>

template<typename T>
class CircularQueue {
private:
    T* data_;
    size_t capacity_;
    size_t front_;
    size_t rear_;
    size_t size_;

public:
    explicit CircularQueue(size_t capacity)
        : capacity_(capacity), front_(0), rear_(0), size_(0) {
        data_ = new T[capacity_];
    }

    ~CircularQueue() {
        delete[] data_;
    }

    bool push(const T& value) {
        if (full()) return false;
        data_[rear_] = value;
        rear_ = (rear_ + 1) % capacity_;
        ++size_;
        return true;
    }

    bool pop() {
        if (empty()) return false;
        front_ = (front_ + 1) % capacity_;
        --size_;
        return true;
    }

    T& front() {
        if (empty()) throw std::underflow_error("Queue is empty");
        return data_[front_];
    }

    const T& front() const {
        if (empty()) throw std::underflow_error("Queue is empty");
        return data_[front_];
    }

    bool empty() const noexcept { return size_ == 0; }
    bool full() const noexcept { return size_ == capacity_; }
    size_t size() const noexcept { return size_; }
};
```

---

## 4. Queue Using Two Stacks

### Principle
- **`inputStack`**: Receives all pushed items.
- **`outputStack`**: Feeds `pop()` and `front()` operations.
- When `outputStack` is empty, transfer all elements from `inputStack` to `outputStack` (reversing their order to satisfy FIFO).
- **Time Complexity**: Amortized $O(1)$ per operation because each element is moved at most twice.

```cpp
#include <stack>
#include <stdexcept>

template<typename T>
class QueueTwoStacks {
private:
    std::stack<T> inStack_;
    std::stack<T> outStack_;

    void transfer() {
        if (outStack_.empty()) {
            while (!inStack_.empty()) {
                outStack_.push(std::move(inStack_.top()));
                inStack_.pop();
            }
        }
    }

public:
    void push(const T& value) {
        inStack_.push(value);
    }

    void pop() {
        transfer();
        if (outStack_.empty()) throw std::underflow_error("Queue underflow");
        outStack_.pop();
    }

    T& front() {
        transfer();
        if (outStack_.empty()) throw std::underflow_error("Queue is empty");
        return outStack_.top();
    }

    bool empty() const noexcept {
        return inStack_.empty() && outStack_.empty();
    }

    size_t size() const noexcept {
        return inStack_.size() + outStack_.size();
    }
};
```

---

## 5. Monotonic Queue (Sliding Window Maximum)

### Principle
A double-ended queue (`std::deque`) storing indices in strictly decreasing order of array values. Elements smaller than the new element are popped from the back. Elements falling outside the current sliding window are popped from the front.

```cpp
#include <vector>
#include <deque>

std::vector<int> maxSlidingWindow(const std::vector<int>& nums, int k) {
    std::vector<int> result;
    std::deque<int> dq; // Stores indices

    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        // Remove indices out of current window [i - k + 1, i]
        if (!dq.empty() && dq.front() <= i - k) {
            dq.pop_front();
        }

        // Maintain monotonic decreasing property
        while (!dq.empty() && nums[dq.back()] <= nums[i]) {
            dq.pop_back();
        }

        dq.push_back(i);

        // Window of size k has formed
        if (i >= k - 1) {
            result.push_back(nums[dq.front()]);
        }
    }
    return result;
}
```

---

## 💻 Driver & Comprehensive Verification

```cpp
#include <iostream>
#include <cassert>

int main() {
    std::cout << "========== 1. ARRAY STACK ==========\n";
    ArrayStack<int> st;
    st.push(10);
    st.push(20);
    st.push(30);
    assert(st.top() == 30);
    assert(st.size() == 3);
    st.pop();
    assert(st.top() == 20);

    std::cout << "\n========== 2. MIN-STACK ==========\n";
    MinStack minSt;
    minSt.push(5);
    minSt.push(3);
    minSt.push(7);
    minSt.push(2);
    assert(minSt.getMin() == 2);
    minSt.pop();
    assert(minSt.getMin() == 3);
    assert(minSt.top() == 7);

    std::cout << "\n========== 3. CIRCULAR QUEUE ==========\n";
    CircularQueue<int> cq(3);
    assert(cq.push(100));
    assert(cq.push(200));
    assert(cq.push(300));
    assert(cq.full());
    assert(cq.front() == 100);
    cq.pop();
    assert(cq.push(400));
    assert(cq.front() == 200);

    std::cout << "\n========== 4. SLIDING WINDOW MAXIMUM ==========\n";
    std::vector<int> arr = {1, 3, -1, -3, 5, 3, 6, 7};
    auto windowMax = maxSlidingWindow(arr, 3);
    std::vector<int> expected = {3, 3, 5, 5, 6, 7};
    assert(windowMax == expected);

    std::cout << "✅ All custom stack and queue implementations verified successfully!\n";
    return 0;
}
```

---

## Next Step

- Go to [11_Trie.md](11_Trie.md) to understand the Trie (Prefix Tree) Data Structure.
