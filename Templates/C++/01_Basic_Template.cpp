#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <bitset>
#include <numeric>
#include <iomanip>
#include <climits>

using namespace std;

// Fast I/O
void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}

// Common type definitions
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;

// Constants
const int MOD = 1e9 + 7;
const int INF = INT_MAX;
const ll LINF = LLONG_MAX;

// Utility functions
template<typename T>
void printVector(const vector<T>& vec) {
    for (const auto& elem : vec) {
        cout << elem << " ";
    }
    cout << "\n";
}

template<typename T>
void printArray(const T arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << "\n";
}

template<typename T>
void print2DVector(const vector<vector<T>>& mat) {
    for (const auto& row : mat) {
        for (const auto& elem : row) {
            cout << elem << " ";
        }
        cout << "\n";
    }
}

// Input functions
template<typename T>
vector<T> readVector(int n) {
    vector<T> vec(n);
    for (int i = 0; i < n; i++) {
        cin >> vec[i];
    }
    return vec;
}

// Mathematical functions
ll gcd(ll a, ll b) {
    return b == 0 ? a : gcd(b, a % b);
}

ll lcm(ll a, ll b) {
    return a / gcd(a, b) * b;
}

ll power(ll a, ll b, ll mod = MOD) {
    ll result = 1;
    a %= mod;
    while (b > 0) {
        if (b & 1) result = (result * a) % mod;
        a = (a * a) % mod;
        b >>= 1;
    }
    return result;
}

bool isPrime(ll n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (ll i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

// String utilities
string toLowerCase(string s) {
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    return s;
}

string toUpperCase(string s) {
    transform(s.begin(), s.end(), s.begin(), ::toupper);
    return s;
}

bool isPalindrome(const string& s) {
    int left = 0, right = s.length() - 1;
    while (left < right) {
        if (s[left] != s[right]) return false;
        left++;
        right--;
    }
    return true;
}

// Array utilities
template<typename T>
void reverseArray(T arr[], int n) {
    reverse(arr, arr + n);
}

template<typename T>
void rotateArray(T arr[], int n, int k) {
    k %= n;
    if (k < 0) k += n;
    reverse(arr, arr + k);
    reverse(arr + k, arr + n);
    reverse(arr, arr + n);
}

// Binary search
int binarySearch(const vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

// Sorting functions
template<typename T>
void sortVector(vector<T>& vec) {
    sort(vec.begin(), vec.end());
}

template<typename T>
void sortVectorDescending(vector<T>& vec) {
    sort(vec.begin(), vec.end(), greater<T>());
}

// Graph utilities (adjacency list)
class Graph {
    int V;
    vector<vector<int>> adj;

public:
    Graph(int vertices) : V(vertices), adj(vertices) {}

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u); // For undirected graph
    }

    void addDirectedEdge(int u, int v) {
        adj[u].push_back(v);
    }

    void printGraph() {
        for (int v = 0; v < V; v++) {
            cout << "Vertex " << v << ": ";
            for (int neighbor : adj[v]) {
                cout << neighbor << " ";
            }
            cout << "\n";
        }
    }

    vector<vector<int>> getAdjacencyList() {
        return adj;
    }

    int getVertexCount() {
        return V;
    }
};

// Stack operations
template<typename T>
class Stack {
    vector<T> elements;

public:
    void push(T element) {
        elements.push_back(element);
    }

    T pop() {
        if (empty()) {
            throw runtime_error("Stack is empty");
        }
        T element = elements.back();
        elements.pop_back();
        return element;
    }

    T top() {
        if (empty()) {
            throw runtime_error("Stack is empty");
        }
        return elements.back();
    }

    bool empty() {
        return elements.empty();
    }

    int size() {
        return elements.size();
    }
};

// Queue operations
template<typename T>
class Queue {
    deque<T> elements;

public:
    void push(T element) {
        elements.push_back(element);
    }

    T pop() {
        if (empty()) {
            throw runtime_error("Queue is empty");
        }
        T element = elements.front();
        elements.pop_front();
        return element;
    }

    T front() {
        if (empty()) {
            throw runtime_error("Queue is empty");
        }
        return elements.front();
    }

    bool empty() {
        return elements.empty();
    }

    int size() {
        return elements.size();
    }
};

// Priority Queue (Min-Heap)
template<typename T>
class MinHeap {
    vector<T> heap;

    void heapifyUp(int index) {
        while (index > 0) {
            int parent = (index - 1) / 2;
            if (heap[parent] <= heap[index]) break;
            swap(heap[parent], heap[index]);
            index = parent;
        }
    }

    void heapifyDown(int index) {
        int n = heap.size();
        while (true) {
            int left = 2 * index + 1;
            int right = 2 * index + 2;
            int smallest = index;

            if (left < n && heap[left] < heap[smallest]) smallest = left;
            if (right < n && heap[right] < heap[smallest]) smallest = right;

            if (smallest == index) break;
            swap(heap[index], heap[smallest]);
            index = smallest;
        }
    }

public:
    void push(T element) {
        heap.push_back(element);
        heapifyUp(heap.size() - 1);
    }

    T pop() {
        if (empty()) {
            throw runtime_error("Heap is empty");
        }
        T minElement = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        if (!empty()) {
            heapifyDown(0);
        }
        return minElement;
    }

    T top() {
        if (empty()) {
            throw runtime_error("Heap is empty");
        }
        return heap[0];
    }

    bool empty() {
        return heap.empty();
    }

    int size() {
        return heap.size();
    }
};

// Disjoint Set Union (Union-Find)
class DSU {
    vector<int> parent;
    vector<int> rank;

public:
    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionSets(int x, int y) {
        int xRoot = find(x);
        int yRoot = find(y);

        if (xRoot == yRoot) return;

        if (rank[xRoot] < rank[yRoot]) {
            parent[xRoot] = yRoot;
        } else if (rank[xRoot] > rank[yRoot]) {
            parent[yRoot] = xRoot;
        } else {
            parent[yRoot] = xRoot;
            rank[xRoot]++;
        }
    }
};

// Common problem-solving patterns
class ProblemSolver {
public:
    // Find maximum subarray sum (Kadane's Algorithm)
    static int maxSubarraySum(const vector<int>& nums) {
        int maxSoFar = nums[0];
        int maxEndingHere = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            maxEndingHere = max(nums[i], maxEndingHere + nums[i]);
            maxSoFar = max(maxSoFar, maxEndingHere);
        }

        return maxSoFar;
    }

    // Check if array is sorted
    static bool isSorted(const vector<int>& arr) {
        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] < arr[i - 1]) return false;
        }
        return true;
    }

    // Find missing number in array [0, n]
    static int findMissingNumber(const vector<int>& nums) {
        int n = nums.size();
        int expectedSum = n * (n + 1) / 2;
        int actualSum = accumulate(nums.begin(), nums.end(), 0);
        return expectedSum - actualSum;
    }

    // Two sum problem
    static vector<int> twoSum(const vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (numMap.find(complement) != numMap.end()) {
                return {numMap[complement], i};
            }
            numMap[nums[i]] = i;
        }
        return {};
    }

    // Check if string has all unique characters
    static bool hasAllUniqueChars(const string& s) {
        bitset<256> charSet;
        for (char c : s) {
            if (charSet[c]) return false;
            charSet[c] = true;
        }
        return true;
    }

    // Generate all permutations of a string
    static vector<string> generatePermutations(string s) {
        vector<string> result;
        sort(s.begin(), s.end());
        do {
            result.push_back(s);
        } while (next_permutation(s.begin(), s.end()));
        return result;
    }

    // Check if two strings are anagrams
    static bool areAnagrams(const string& s1, const string& s2) {
        if (s1.length() != s2.length()) return false;
        int count[256] = {0};
        
        for (char c : s1) count[c]++;
        for (char c : s2) count[c]--;
        
        for (int i = 0; i < 256; i++) {
            if (count[i] != 0) return false;
        }
        return true;
    }

    // Find factorial
    static ll factorial(int n) {
        if (n < 0) return -1; // Error case
        ll result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    // Find nth Fibonacci number
    static ll fibonacci(int n) {
        if (n <= 1) return n;
        
        ll a = 0, b = 1, c;
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return b;
    }

    // Sieve of Eratosthenes
    static vector<bool> sieveOfEratosthenes(int n) {
        vector<bool> isPrime(n + 1, true);
        isPrime[0] = isPrime[1] = false;
        
        for (int p = 2; p * p <= n; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i <= n; i += p) {
                    isPrime[i] = false;
                }
            }
        }
        return isPrime;
    }
};

// Main solve function - modify this for each problem
void solve() {
    // Fast I/O for competitive programming
    fastIO();

    // Read input based on problem requirements
    int n;
    cin >> n;

    vector<int> arr = readVector<int>(n);

    // Your solution logic here
    // Example: find and print maximum element
    if (!arr.empty()) {
        int maxElement = *max_element(arr.begin(), arr.end());
        cout << "Maximum element: " << maxElement << "\n";
    }

    // Example: sort and print array
    sortVector(arr);
    cout << "Sorted array: ";
    printVector(arr);

    // Example: check if array is palindrome
    bool isPalindromeArray = true;
    for (int i = 0; i < arr.size() / 2; i++) {
        if (arr[i] != arr[arr.size() - 1 - i]) {
            isPalindromeArray = false;
            break;
        }
    }
    cout << "Array is " << (isPalindromeArray ? "palindrome" : "not palindrome") << "\n";

    // Add your custom logic here
}

// Main function
int main() {
    // Uncomment the following line for competitive programming
    // fastIO();

    try {
        solve();
    } catch (const exception& e) {
        cerr << "Error: " << e.what() << "\n";
        return 1;
    }

    return 0;
}

// Example usage of utility functions
void exampleUsage() {
    // Vector operations
    vector<int> nums = {5, 2, 8, 1, 9};
    cout << "Original vector: ";
    printVector(nums);

    sortVector(nums);
    cout << "Sorted vector: ";
    printVector(nums);

    // Mathematical operations
    ll a = 12, b = 18;
    cout << "GCD of " << a << " and " << b << ": " << gcd(a, b) << "\n";
    cout << "LCM of " << a << " and " << b << ": " << lcm(a, b) << "\n";

    // String operations
    string str = "Racecar";
    cout << "Is \"" << str << "\" a palindrome? " << (isPalindrome(str) ? "Yes" : "No") << "\n";

    // Graph operations
    Graph g(4);
    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 3);
    cout << "Graph adjacency list:\n";
    g.printGraph();

    // Stack operations
    Stack<int> stack;
    stack.push(1);
    stack.push(2);
    stack.push(3);
    cout << "Stack top: " << stack.top() << "\n";
    stack.pop();
    cout << "Stack size after pop: " << stack.size() << "\n";

    // Queue operations
    Queue<int> queue;
    queue.push(10);
    queue.push(20);
    queue.push(30);
    cout << "Queue front: " << queue.front() << "\n";
    queue.pop();
    cout << "Queue size after pop: " << queue.size() << "\n";

    // Problem solver examples
    vector<int> testArray = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << "Maximum subarray sum: " << ProblemSolver::maxSubarraySum(testArray) << "\n";

    string s1 = "listen", s2 = "silent";
    cout << "Are \"" << s1 << "\" and \"" << s2 << "\" anagrams? " 
         << (ProblemSolver::areAnagrams(s1, s2) ? "Yes" : "No") << "\n";
}

// Uncomment the following to run example usage
/*
int main() {
    exampleUsage();
    return 0;
}
*/
