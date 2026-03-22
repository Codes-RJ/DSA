import java.util.*;
import java.io.*;
import java.math.*;
import java.text.*;
import java.time.*;
import java.util.function.*;
import java.util.stream.*;

/**
 * Basic Java Template for Competitive Programming and DSA Practice
 * Includes common utilities, data structures, and algorithms
 */
public class BasicTemplate {
    
    // Fast I/O setup
    private static final FastScanner fs = new FastScanner(System.in);
    private static final PrintWriter out = new PrintWriter(System.out);
    
    // Common constants
    private static final int MOD = 1000000007;
    private static final int INF = Integer.MAX_VALUE;
    private static final long LINF = Long.MAX_VALUE;
    
    // Fast Scanner class
    static class FastScanner {
        private final BufferedReader br;
        private StringTokenizer st;
        
        public FastScanner(InputStream in) {
            br = new BufferedReader(new InputStreamReader(in));
        }
        
        public String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        
        public int nextInt() {
            return Integer.parseInt(next());
        }
        
        public long nextLong() {
            return Long.parseLong(next());
        }
        
        public double nextDouble() {
            return Double.parseDouble(next());
        }
        
        public String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
        
        public int[] readIntArray(int n) {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = nextInt();
            }
            return arr;
        }
        
        public long[] readLongArray(int n) {
            long[] arr = new long[n];
            for (int i = 0; i < n; i++) {
                arr[i] = nextLong();
            }
            return arr;
        }
        
        public String[] readStringArray(int n) {
            String[] arr = new String[n];
            for (int i = 0; i < n; i++) {
                arr[i] = next();
            }
            return arr;
        }
        
        public List<Integer> readIntList(int n) {
            List<Integer> list = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                list.add(nextInt());
            }
            return list;
        }
        
        public List<Long> readLongList(int n) {
            List<Long> list = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                list.add(nextLong());
            }
            return list;
        }
    }
    
    // Utility class for common operations
    static class Utils {
        
        // Print array
        public static void printArray(int[] arr) {
            for (int x : arr) {
                out.print(x + " ");
            }
            out.println();
        }
        
        public static void printArray(long[] arr) {
            for (long x : arr) {
                out.print(x + " ");
            }
            out.println();
        }
        
        public static void printArray(String[] arr) {
            for (String x : arr) {
                out.print(x + " ");
            }
            out.println();
        }
        
        // Print list
        public static void printList(List<?> list) {
            for (Object x : list) {
                out.print(x + " ");
            }
            out.println();
        }
        
        // Print 2D array
        public static void print2DArray(int[][] arr) {
            for (int[] row : arr) {
                for (int x : row) {
                    out.print(x + " ");
                }
                out.println();
            }
        }
        
        public static void print2DArray(long[][] arr) {
            for (long[] row : arr) {
                for (long x : row) {
                    out.print(x + " ");
                }
                out.println();
            }
        }
        
        // Reverse array
        public static void reverse(int[] arr) {
            int left = 0, right = arr.length - 1;
            while (left < right) {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left++;
                right--;
            }
        }
        
        public static void reverse(long[] arr) {
            int left = 0, right = arr.length - 1;
            while (left < right) {
                long temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left++;
                right--;
            }
        }
        
        // Swap elements in array
        public static void swap(int[] arr, int i, int j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        
        public static void swap(long[] arr, int i, int j) {
            long temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        
        // Check if array is sorted
        public static boolean isSorted(int[] arr) {
            for (int i = 1; i < arr.length; i++) {
                if (arr[i] < arr[i - 1]) return false;
            }
            return true;
        }
        
        public static boolean isSorted(long[] arr) {
            for (int i = 1; i < arr.length; i++) {
                if (arr[i] < arr[i - 1]) return false;
            }
            return true;
        }
        
        // Find minimum in array
        public static int findMin(int[] arr) {
            int min = arr[0];
            for (int x : arr) {
                min = Math.min(min, x);
            }
            return min;
        }
        
        public static long findMin(long[] arr) {
            long min = arr[0];
            for (long x : arr) {
                min = Math.min(min, x);
            }
            return min;
        }
        
        // Find maximum in array
        public static int findMax(int[] arr) {
            int max = arr[0];
            for (int x : arr) {
                max = Math.max(max, x);
            }
            return max;
        }
        
        public static long findMax(long[] arr) {
            long max = arr[0];
            for (long x : arr) {
                max = Math.max(max, x);
            }
            return max;
        }
        
        // Generate random array
        public static int[] generateRandomArray(int n, int min, int max) {
            Random rand = new Random();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = rand.nextInt(max - min + 1) + min;
            }
            return arr;
        }
        
        public static long[] generateRandomLongArray(int n, long min, long max) {
            Random rand = new Random();
            long[] arr = new long[n];
            for (int i = 0; i < n; i++) {
                arr[i] = min + (long) (rand.nextDouble() * (max - min));
            }
            return arr;
        }
    }
    
    // Mathematical utilities
    static class MathUtils {
        
        // GCD using Euclidean algorithm
        public static long gcd(long a, long b) {
            return b == 0 ? a : gcd(b, a % b);
        }
        
        // LCM
        public static long lcm(long a, long b) {
            return a / gcd(a, b) * b;
        }
        
        // Fast exponentiation
        public static long power(long a, long b, long mod) {
            long result = 1;
            a %= mod;
            while (b > 0) {
                if ((b & 1) == 1) {
                    result = (result * a) % mod;
                }
                a = (a * a) % mod;
                b >>= 1;
            }
            return result;
        }
        
        // Check if number is prime
        public static boolean isPrime(long n) {
            if (n <= 1) return false;
            if (n <= 3) return true;
            if (n % 2 == 0 || n % 3 == 0) return false;
            
            for (long i = 5; i * i <= n; i += 6) {
                if (n % i == 0 || n % (i + 2) == 0) return false;
            }
            return true;
        }
        
        // Sieve of Eratosthenes
        public static boolean[] sieveOfEratosthenes(int n) {
            boolean[] isPrime = new boolean[n + 1];
            Arrays.fill(isPrime, true);
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
        
        // Factorial
        public static long factorial(int n) {
            if (n < 0) return -1;
            long result = 1;
            for (int i = 2; i <= n; i++) {
                result *= i;
            }
            return result;
        }
        
        // Fibonacci
        public static long fibonacci(int n) {
            if (n <= 1) return n;
            long a = 0, b = 1, c;
            for (int i = 2; i <= n; i++) {
                c = a + b;
                a = b;
                b = c;
            }
            return b;
        }
        
        // Combinations (nCr)
        public static long nCr(int n, int r) {
            if (r > n || r < 0) return 0;
            if (r == 0 || r == n) return 1;
            
            r = Math.min(r, n - r);
            long result = 1;
            
            for (int i = 0; i < r; i++) {
                result = result * (n - i) / (i + 1);
            }
            
            return result;
        }
        
        // Permutations (nPr)
        public static long nPr(int n, int r) {
            if (r > n || r < 0) return 0;
            long result = 1;
            for (int i = 0; i < r; i++) {
                result *= (n - i);
            }
            return result;
        }
    }
    
    // String utilities
    static class StringUtils {
        
        // Check if string is palindrome
        public static boolean isPalindrome(String s) {
            int left = 0, right = s.length() - 1;
            while (left < right) {
                if (s.charAt(left) != s.charAt(right)) return false;
                left++;
                right--;
            }
            return true;
        }
        
        // Reverse string
        public static String reverse(String s) {
            return new StringBuilder(s).reverse().toString();
        }
        
        // Check if two strings are anagrams
        public static boolean areAnagrams(String s1, String s2) {
            if (s1.length() != s2.length()) return false;
            
            int[] count = new int[256];
            for (int i = 0; i < s1.length(); i++) {
                count[s1.charAt(i)]++;
                count[s2.charAt(i)]--;
            }
            
            for (int c : count) {
                if (c != 0) return false;
            }
            return true;
        }
        
        // Convert to lowercase
        public static String toLowerCase(String s) {
            return s.toLowerCase();
        }
        
        // Convert to uppercase
        public static String toUpperCase(String s) {
            return s.toUpperCase();
        }
        
        // Count vowels
        public static int countVowels(String s) {
            int count = 0;
            for (char c : s.toCharArray()) {
                if ("aeiouAEIOU".indexOf(c) != -1) {
                    count++;
                }
            }
            return count;
        }
        
        // Count consonants
        public static int countConsonants(String s) {
            int count = 0;
            for (char c : s.toCharArray()) {
                if (Character.isLetter(c) && "aeiouAEIOU".indexOf(c) == -1) {
                    count++;
                }
            }
            return count;
        }
        
        // Remove duplicates
        public static String removeDuplicates(String s) {
            StringBuilder sb = new StringBuilder();
            Set<Character> seen = new HashSet<>();
            
            for (char c : s.toCharArray()) {
                if (!seen.contains(c)) {
                    seen.add(c);
                    sb.append(c);
                }
            }
            return sb.toString();
        }
        
        // Find all substrings
        public static List<String> getAllSubstrings(String s) {
            List<String> substrings = new ArrayList<>();
            int n = s.length();
            
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j <= n; j++) {
                    substrings.add(s.substring(i, j));
                }
            }
            return substrings;
        }
    }
    
    // Array algorithms
    static class ArrayAlgorithms {
        
        // Kadane's algorithm - Maximum subarray sum
        public static int maxSubarraySum(int[] nums) {
            int maxSoFar = nums[0];
            int maxEndingHere = nums[0];
            
            for (int i = 1; i < nums.length; i++) {
                maxEndingHere = Math.max(nums[i], maxEndingHere + nums[i]);
                maxSoFar = Math.max(maxSoFar, maxEndingHere);
            }
            
            return maxSoFar;
        }
        
        // Two sum problem
        public static int[] twoSum(int[] nums, int target) {
            Map<Integer, Integer> numMap = new HashMap<>();
            for (int i = 0; i < nums.length; i++) {
                int complement = target - nums[i];
                if (numMap.containsKey(complement)) {
                    return new int[]{numMap.get(complement), i};
                }
                numMap.put(nums[i], i);
            }
            return new int[]{-1, -1};
        }
        
        // Three sum problem
        public static List<List<Integer>> threeSum(int[] nums) {
            List<List<Integer>> result = new ArrayList<>();
            Arrays.sort(nums);
            
            for (int i = 0; i < nums.length; i++) {
                if (i > 0 && nums[i] == nums[i - 1]) continue;
                
                int left = i + 1, right = nums.length - 1;
                while (left < right) {
                    int sum = nums[i] + nums[left] + nums[right];
                    if (sum == 0) {
                        result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        left++;
                        right--;
                    } else if (sum < 0) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
            return result;
        }
        
        // Maximum product subarray
        public static int maxProductSubarray(int[] nums) {
            int maxSoFar = nums[0];
            int maxEndingHere = nums[0];
            int minEndingHere = nums[0];
            
            for (int i = 1; i < nums.length; i++) {
                if (nums[i] < 0) {
                    int temp = maxEndingHere;
                    maxEndingHere = minEndingHere;
                    minEndingHere = temp;
                }
                
                maxEndingHere = Math.max(nums[i], maxEndingHere * nums[i]);
                minEndingHere = Math.min(nums[i], minEndingHere * nums[i]);
                maxSoFar = Math.max(maxSoFar, maxEndingHere);
            }
            
            return maxSoFar;
        }
        
        // Find missing number
        public static int findMissingNumber(int[] nums) {
            int n = nums.length;
            int expectedSum = n * (n + 1) / 2;
            int actualSum = 0;
            for (int num : nums) {
                actualSum += num;
            }
            return expectedSum - actualSum;
        }
        
        // Find duplicate number
        public static int findDuplicate(int[] nums) {
            int slow = nums[0], fast = nums[0];
            do {
                slow = nums[slow];
                fast = nums[nums[fast]];
            } while (slow != fast);
            
            fast = nums[0];
            while (slow != fast) {
                slow = nums[slow];
                fast = nums[fast];
            }
            return slow;
        }
        
        // Binary search
        public static int binarySearch(int[] arr, int target) {
            int left = 0, right = arr.length - 1;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (arr[mid] == target) return mid;
                else if (arr[mid] < target) left = mid + 1;
                else right = mid - 1;
            }
            return -1;
        }
        
        // Lower bound
        public static int lowerBound(int[] arr, int target) {
            int left = 0, right = arr.length;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (arr[mid] < target) left = mid + 1;
                else right = mid;
            }
            return left;
        }
        
        // Upper bound
        public static int upperBound(int[] arr, int target) {
            int left = 0, right = arr.length;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (arr[mid] <= target) left = mid + 1;
                else right = mid;
            }
            return left;
        }
    }
    
    // Sorting algorithms
    static class SortingAlgorithms {
        
        // Bubble sort
        public static void bubbleSort(int[] arr) {
            int n = arr.length;
            for (int i = 0; i < n - 1; i++) {
                boolean swapped = false;
                for (int j = 0; j < n - i - 1; j++) {
                    if (arr[j] > arr[j + 1]) {
                        Utils.swap(arr, j, j + 1);
                        swapped = true;
                    }
                }
                if (!swapped) break;
            }
        }
        
        // Selection sort
        public static void selectionSort(int[] arr) {
            int n = arr.length;
            for (int i = 0; i < n - 1; i++) {
                int minIdx = i;
                for (int j = i + 1; j < n; j++) {
                    if (arr[j] < arr[minIdx]) {
                        minIdx = j;
                    }
                }
                if (minIdx != i) {
                    Utils.swap(arr, i, minIdx);
                }
            }
        }
        
        // Insertion sort
        public static void insertionSort(int[] arr) {
            for (int i = 1; i < arr.length; i++) {
                int key = arr[i];
                int j = i - 1;
                while (j >= 0 && arr[j] > key) {
                    arr[j + 1] = arr[j];
                    j--;
                }
                arr[j + 1] = key;
            }
        }
        
        // Merge sort
        public static void mergeSort(int[] arr) {
            mergeSort(arr, 0, arr.length - 1);
        }
        
        private static void mergeSort(int[] arr, int left, int right) {
            if (left < right) {
                int mid = left + (right - left) / 2;
                mergeSort(arr, left, mid);
                mergeSort(arr, mid + 1, right);
                merge(arr, left, mid, right);
            }
        }
        
        private static void merge(int[] arr, int left, int mid, int right) {
            int n1 = mid - left + 1;
            int n2 = right - mid;
            
            int[] L = new int[n1];
            int[] R = new int[n2];
            
            for (int i = 0; i < n1; i++) L[i] = arr[left + i];
            for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];
            
            int i = 0, j = 0, k = left;
            while (i < n1 && j < n2) {
                if (L[i] <= R[j]) {
                    arr[k] = L[i];
                    i++;
                } else {
                    arr[k] = R[j];
                    j++;
                }
                k++;
            }
            
            while (i < n1) {
                arr[k] = L[i];
                i++;
                k++;
            }
            
            while (j < n2) {
                arr[k] = R[j];
                j++;
                k++;
            }
        }
        
        // Quick sort
        public static void quickSort(int[] arr) {
            quickSort(arr, 0, arr.length - 1);
        }
        
        private static void quickSort(int[] arr, int low, int high) {
            if (low < high) {
                int pi = partition(arr, low, high);
                quickSort(arr, low, pi - 1);
                quickSort(arr, pi + 1, high);
            }
        }
        
        private static int partition(int[] arr, int low, int high) {
            int pivot = arr[high];
            int i = low - 1;
            
            for (int j = low; j < high; j++) {
                if (arr[j] < pivot) {
                    i++;
                    Utils.swap(arr, i, j);
                }
            }
            Utils.swap(arr, i + 1, high);
            return i + 1;
        }
    }
    
    // Data structures
    static class DataStructures {
        
        // Stack implementation using array
        static class ArrayStack<T> {
            private List<T> stack;
            private int capacity;
            
            public ArrayStack(int capacity) {
                this.capacity = capacity;
                this.stack = new ArrayList<>(capacity);
            }
            
            public void push(T item) {
                if (stack.size() < capacity) {
                    stack.add(item);
                } else {
                    throw new RuntimeException("Stack is full");
                }
            }
            
            public T pop() {
                if (empty()) {
                    throw new RuntimeException("Stack is empty");
                }
                return stack.remove(stack.size() - 1);
            }
            
            public T peek() {
                if (empty()) {
                    throw new RuntimeException("Stack is empty");
                }
                return stack.get(stack.size() - 1);
            }
            
            public boolean empty() {
                return stack.isEmpty();
            }
            
            public int size() {
                return stack.size();
            }
        }
        
        // Queue implementation using linked list
        static class LinkedListQueue<T> {
            private static class Node<T> {
                T data;
                Node<T> next;
                
                Node(T data) {
                    this.data = data;
                    this.next = null;
                }
            }
            
            private Node<T> front, rear;
            private int size;
            
            public LinkedListQueue() {
                front = rear = null;
                size = 0;
            }
            
            public void enqueue(T item) {
                Node<T> newNode = new Node<>(item);
                if (rear == null) {
                    front = rear = newNode;
                } else {
                    rear.next = newNode;
                    rear = newNode;
                }
                size++;
            }
            
            public T dequeue() {
                if (empty()) {
                    throw new RuntimeException("Queue is empty");
                }
                T data = front.data;
                front = front.next;
                if (front == null) {
                    rear = null;
                }
                size--;
                return data;
            }
            
            public T peek() {
                if (empty()) {
                    throw new RuntimeException("Queue is empty");
                }
                return front.data;
            }
            
            public boolean empty() {
                return front == null;
            }
            
            public int size() {
                return size;
            }
        }
        
        // Min-Heap implementation
        static class MinHeap<T extends Comparable<T>> {
            private List<T> heap;
            
            public MinHeap() {
                heap = new ArrayList<>();
            }
            
            public void add(T item) {
                heap.add(item);
                heapifyUp(heap.size() - 1);
            }
            
            public T remove() {
                if (empty()) {
                    throw new RuntimeException("Heap is empty");
                }
                T item = heap.get(0);
                T lastItem = heap.remove(heap.size() - 1);
                if (!empty()) {
                    heap.set(0, lastItem);
                    heapifyDown(0);
                }
                return item;
            }
            
            public T peek() {
                if (empty()) {
                    throw new RuntimeException("Heap is empty");
                }
                return heap.get(0);
            }
            
            public boolean empty() {
                return heap.isEmpty();
            }
            
            public int size() {
                return heap.size();
            }
            
            private void heapifyUp(int index) {
                while (index > 0) {
                    int parent = (index - 1) / 2;
                    if (heap.get(parent).compareTo(heap.get(index)) <= 0) break;
                    Collections.swap(heap, parent, index);
                    index = parent;
                }
            }
            
            private void heapifyDown(int index) {
                int n = heap.size();
                while (true) {
                    int left = 2 * index + 1;
                    int right = 2 * index + 2;
                    int smallest = index;
                    
                    if (left < n && heap.get(left).compareTo(heap.get(smallest)) < 0) {
                        smallest = left;
                    }
                    if (right < n && heap.get(right).compareTo(heap.get(smallest)) < 0) {
                        smallest = right;
                    }
                    
                    if (smallest == index) break;
                    Collections.swap(heap, index, smallest);
                    index = smallest;
                }
            }
        }
    }
    
    // Main solve function - modify this for each problem
    public static void solve() {
        // Example usage of the template
        
        out.println("=== Java Template Demonstration ===\n");
        
        // Read input example
        out.print("Enter number of elements: ");
        int n = fs.nextInt();
        
        int[] arr = fs.readIntArray(n);
        out.print("Original array: ");
        Utils.printArray(arr);
        
        // Sorting example
        int[] sortedArr = arr.clone();
        Arrays.sort(sortedArr);
        out.print("Sorted array: ");
        Utils.printArray(sortedArr);
        
        // Search example
        out.print("Enter target to search: ");
        int target = fs.nextInt();
        int index = ArrayAlgorithms.binarySearch(sortedArr, target);
        if (index != -1) {
            out.println("Found at index: " + index);
        } else {
            out.println("Not found");
        }
        
        // Math utilities example
        out.println("GCD of 48 and 18: " + MathUtils.gcd(48, 18));
        out.println("LCM of 48 and 18: " + MathUtils.lcm(48, 18));
        out.println("Is 17 prime: " + MathUtils.isPrime(17));
        
        // String utilities example
        String str = "racecar";
        out.println("Is \"" + str + "\" palindrome: " + StringUtils.isPalindrome(str));
        
        // Array algorithms example
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        out.println("Maximum subarray sum: " + ArrayAlgorithms.maxSubarraySum(nums));
        
        // Data structures example
        DataStructures.ArrayStack<Integer> stack = new DataStructures.ArrayStack<>(10);
        stack.push(10);
        stack.push(20);
        stack.push(30);
        out.print("Stack elements: ");
        while (!stack.empty()) {
            out.print(stack.pop() + " ");
        }
        out.println();
        
        DataStructures.LinkedListQueue<Integer> queue = new DataStructures.LinkedListQueue<>();
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        out.print("Queue elements: ");
        while (!queue.empty()) {
            out.print(queue.dequeue() + " ");
        }
        out.println();
        
        // Min-Heap example
        DataStructures.MinHeap<Integer> minHeap = new DataStructures.MinHeap<>();
        minHeap.add(30);
        minHeap.add(10);
        minHeap.add(20);
        minHeap.add(40);
        out.print("Min-heap elements: ");
        while (!minHeap.empty()) {
            out.print(minHeap.remove() + " ");
        }
        out.println();
    }
    
    // Main method
    public static void main(String[] args) {
        try {
            solve();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            out.close();
        }
    }
}
