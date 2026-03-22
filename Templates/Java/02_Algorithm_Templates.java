import java.util.*;
import java.io.*;
import java.math.*;
import java.text.*;
import java.time.*;
import java.util.function.*;
import java.util.stream.*;

/**
 * Algorithm Templates for Competitive Programming and DSA Practice
 * Includes comprehensive implementations of common algorithms
 */
public class AlgorithmTemplates {
    
    // Fast I/O setup
    private static final FastScanner fs = new FastScanner(System.in);
    private static final PrintWriter out = new PrintWriter(System.out);
    
    // Constants
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
    }
    
    // =============================================
    // SORTING ALGORITHMS
    // =============================================
    
    static class SortingAlgorithms {
        
        // Bubble Sort
        public static void bubbleSort(int[] arr) {
            int n = arr.length;
            for (int i = 0; i < n - 1; i++) {
                boolean swapped = false;
                for (int j = 0; j < n - i - 1; j++) {
                    if (arr[j] > arr[j + 1]) {
                        swap(arr, j, j + 1);
                        swapped = true;
                    }
                }
                if (!swapped) break;
            }
        }
        
        // Selection Sort
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
                    swap(arr, i, minIdx);
                }
            }
        }
        
        // Insertion Sort
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
        
        // Merge Sort
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
        
        // Quick Sort
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
                    swap(arr, i, j);
                }
            }
            swap(arr, i + 1, high);
            return i + 1;
        }
        
        // Heap Sort
        public static void heapSort(int[] arr) {
            int n = arr.length;
            
            // Build max heap
            for (int i = n / 2 - 1; i >= 0; i--) {
                heapify(arr, n, i);
            }
            
            // Extract elements from heap
            for (int i = n - 1; i > 0; i--) {
                swap(arr, 0, i);
                heapify(arr, i, 0);
            }
        }
        
        private static void heapify(int[] arr, int n, int i) {
            int largest = i;
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            
            if (left < n && arr[left] > arr[largest]) {
                largest = left;
            }
            
            if (right < n && arr[right] > arr[largest]) {
                largest = right;
            }
            
            if (largest != i) {
                swap(arr, i, largest);
                heapify(arr, n, largest);
            }
        }
        
        // Counting Sort
        public static void countingSort(int[] arr) {
            if (arr.length == 0) return;
            
            int max = Arrays.stream(arr).max().getAsInt();
            int min = Arrays.stream(arr).min().getAsInt();
            int range = max - min + 1;
            
            int[] count = new int[range];
            int[] output = new int[arr.length];
            
            // Store count of each element
            for (int num : arr) {
                count[num - min]++;
            }
            
            // Change count[i] to contain position
            for (int i = 1; i < count.length; i++) {
                count[i] += count[i - 1];
            }
            
            // Build output array
            for (int i = arr.length - 1; i >= 0; i--) {
                output[count[arr[i] - min] - 1] = arr[i];
                count[arr[i] - min]--;
            }
            
            // Copy to original array
            System.arraycopy(output, 0, arr, 0, arr.length);
        }
        
        // Radix Sort
        public static void radixSort(int[] arr) {
            if (arr.length == 0) return;
            
            int max = Arrays.stream(arr).max().getAsInt();
            
            for (int exp = 1; max / exp > 0; exp *= 10) {
                countingSortByDigit(arr, exp);
            }
        }
        
        private static void countingSortByDigit(int[] arr, int exp) {
            int[] output = new int[arr.length];
            int[] count = new int[10];
            
            // Store count of occurrences
            for (int num : arr) {
                int digit = (num / exp) % 10;
                count[digit]++;
            }
            
            // Change count[i] to contain position
            for (int i = 1; i < 10; i++) {
                count[i] += count[i - 1];
            }
            
            // Build output array
            for (int i = arr.length - 1; i >= 0; i--) {
                int digit = (arr[i] / exp) % 10;
                output[count[digit] - 1] = arr[i];
                count[digit]--;
            }
            
            // Copy to original array
            System.arraycopy(output, 0, arr, 0, arr.length);
        }
        
        private static void swap(int[] arr, int i, int j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    
    // =============================================
    // SEARCHING ALGORITHMS
    // =============================================
    
    static class SearchingAlgorithms {
        
        // Linear Search
        public static int linearSearch(int[] arr, int target) {
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] == target) return i;
            }
            return -1;
        }
        
        // Binary Search (iterative)
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
        
        // Binary Search (recursive)
        public static int binarySearchRecursive(int[] arr, int target, int left, int right) {
            if (left > right) return -1;
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) return binarySearchRecursive(arr, target, mid + 1, right);
            else return binarySearchRecursive(arr, target, left, mid - 1);
        }
        
        // Lower Bound
        public static int lowerBound(int[] arr, int target) {
            int left = 0, right = arr.length;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (arr[mid] < target) left = mid + 1;
                else right = mid;
            }
            return left;
        }
        
        // Upper Bound
        public static int upperBound(int[] arr, int target) {
            int left = 0, right = arr.length;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (arr[mid] <= target) left = mid + 1;
                else right = mid;
            }
            return left;
        }
        
        // Jump Search
        public static int jumpSearch(int[] arr, int target) {
            int n = arr.length;
            int step = (int) Math.sqrt(n);
            int prev = 0;
            
            // Find the block where element could be
            while (prev < n && arr[Math.min(step, n) - 1] < target) {
                prev = step;
                step += (int) Math.sqrt(n);
                if (prev >= n) return -1;
            }
            
            // Linear search in identified block
            for (int i = prev; i < Math.min(step, n); i++) {
                if (arr[i] == target) return i;
            }
            
            return -1;
        }
        
        // Interpolation Search
        public static int interpolationSearch(int[] arr, int target) {
            int left = 0, right = arr.length - 1;
            
            while (left <= right && target >= arr[left] && target <= arr[right]) {
                if (left == right) {
                    return arr[left] == target ? left : -1;
                }
                
                // Estimate position
                int pos = left + ((target - arr[left]) * (right - left)) / (arr[right] - arr[left]);
                
                if (arr[pos] == target) return pos;
                else if (arr[pos] < target) left = pos + 1;
                else right = pos - 1;
            }
            
            return -1;
        }
        
        // Exponential Search
        public static int exponentialSearch(int[] arr, int target) {
            if (arr.length == 0) return -1;
            if (arr[0] == target) return 0;
            
            int i = 1;
            while (i < arr.length && arr[i] <= target) {
                i *= 2;
            }
            
            return binarySearch(arr, target, i / 2, Math.min(i, arr.length - 1));
        }
        
        private static int binarySearch(int[] arr, int target, int left, int right) {
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (arr[mid] == target) return mid;
                else if (arr[mid] < target) left = mid + 1;
                else right = mid - 1;
            }
            return -1;
        }
    }
    
    // =============================================
    // ARRAY ALGORITHMS
    // =============================================
    
    static class ArrayAlgorithms {
        
        // Kadane's Algorithm - Maximum Subarray Sum
        public static int maxSubarraySum(int[] nums) {
            int maxSoFar = nums[0];
            int maxEndingHere = nums[0];
            
            for (int i = 1; i < nums.length; i++) {
                maxEndingHere = Math.max(nums[i], maxEndingHere + nums[i]);
                maxSoFar = Math.max(maxSoFar, maxEndingHere);
            }
            
            return maxSoFar;
        }
        
        // Two Sum Problem
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
        
        // Three Sum Problem
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
        
        // Maximum Product Subarray
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
        
        // Find Missing Number
        public static int findMissingNumber(int[] nums) {
            int n = nums.length;
            int expectedSum = n * (n + 1) / 2;
            int actualSum = 0;
            for (int num : nums) {
                actualSum += num;
            }
            return expectedSum - actualSum;
        }
        
        // Find Duplicate Number
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
        
        // Rotate Array
        public static void rotateArray(int[] nums, int k) {
            int n = nums.length;
            k %= n;
            if (k < 0) k += n;
            
            reverse(nums, 0, n - 1);
            reverse(nums, 0, k - 1);
            reverse(nums, k, n - 1);
        }
        
        private static void reverse(int[] nums, int left, int right) {
            while (left < right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
                right--;
            }
        }
        
        // Next Permutation
        public static void nextPermutation(int[] nums) {
            int n = nums.length;
            int i = n - 2;
            
            // Find the first decreasing element
            while (i >= 0 && nums[i] >= nums[i + 1]) {
                i--;
            }
            
            if (i >= 0) {
                int j = n - 1;
                // Find element just larger than nums[i]
                while (j > i && nums[j] <= nums[i]) {
                    j--;
                }
                swap(nums, i, j);
            }
            
            // Reverse the suffix
            reverse(nums, i + 1, n - 1);
        }
        
        private static void swap(int[] nums, int i, int j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
    
    // =============================================
    // STRING ALGORITHMS
    // =============================================
    
    static class StringAlgorithms {
        
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
        
        // Longest Palindromic Substring
        public static String longestPalindrome(String s) {
            if (s == null || s.length() < 1) return "";
            
            int start = 0, end = 0;
            for (int i = 0; i < s.length(); i++) {
                int len1 = expandAroundCenter(s, i, i);
                int len2 = expandAroundCenter(s, i, i + 1);
                int maxLen = Math.max(len1, len2);
                
                if (maxLen > end - start) {
                    start = i - (maxLen - 1) / 2;
                    end = i + maxLen / 2;
                }
            }
            return s.substring(start, end + 1);
        }
        
        private static int expandAroundCenter(String s, int left, int right) {
            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                left--;
                right++;
            }
            return right - left - 1;
        }
        
        // Longest Common Prefix
        public static String longestCommonPrefix(String[] strs) {
            if (strs == null || strs.length == 0) return "";
            
            String prefix = strs[0];
            for (int i = 1; i < strs.length; i++) {
                while (strs[i].indexOf(prefix) != 0) {
                    prefix = prefix.substring(0, prefix.length() - 1);
                    if (prefix.isEmpty()) return "";
                }
            }
            return prefix;
        }
        
        // Valid Parentheses
        public static boolean isValidParentheses(String s) {
            Deque<Character> stack = new ArrayDeque<>();
            for (char c : s.toCharArray()) {
                if (c == '(' || c == '{' || c == '[') {
                    stack.push(c);
                } else {
                    if (stack.isEmpty()) return false;
                    char top = stack.pop();
                    if ((c == ')' && top != '(') ||
                        (c == '}' && top != '{') ||
                        (c == ']' && top != '[')) {
                        return false;
                    }
                }
            }
            return stack.isEmpty();
        }
        
        // Generate Parentheses
        public static List<String> generateParentheses(int n) {
            List<String> result = new ArrayList<>();
            generateParentheses(result, "", 0, 0, n);
            return result;
        }
        
        private static void generateParentheses(List<String> result, String current, 
                                               int open, int close, int max) {
            if (current.length() == max * 2) {
                result.add(current);
                return;
            }
            
            if (open < max) {
                generateParentheses(result, current + "(", open + 1, close, max);
            }
            if (close < open) {
                generateParentheses(result, current + ")", open, close + 1, max);
            }
        }
        
        // Word Break
        public static boolean wordBreak(String s, List<String> wordDict) {
            Set<String> wordSet = new HashSet<>(wordDict);
            boolean[] dp = new boolean[s.length() + 1];
            dp[0] = true;
            
            for (int i = 1; i <= s.length(); i++) {
                for (int j = 0; j < i; j++) {
                    if (dp[j] && wordSet.contains(s.substring(j, i))) {
                        dp[i] = true;
                        break;
                    }
                }
            }
            
            return dp[s.length()];
        }
        
        // Edit Distance
        public static int editDistance(String word1, String word2) {
            int m = word1.length(), n = word2.length();
            int[][] dp = new int[m + 1][n + 1];
            
            for (int i = 0; i <= m; i++) dp[i][0] = i;
            for (int j = 0; j <= n; j++) dp[0][j] = j;
            
            for (int i = 1; i <= m; i++) {
                for (int j = 1; j <= n; j++) {
                    if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                        dp[i][j] = dp[i - 1][j - 1];
                    } else {
                        dp[i][j] = 1 + Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
                    }
                }
            }
            
            return dp[m][n];
        }
        
        // KMP Algorithm
        public static int kmpSearch(String text, String pattern) {
            int[] lps = computeLPS(pattern);
            int i = 0, j = 0;
            
            while (i < text.length()) {
                if (pattern.charAt(j) == text.charAt(i)) {
                    i++;
                    j++;
                }
                
                if (j == pattern.length()) {
                    return i - j;
                } else if (i < text.length() && pattern.charAt(j) != text.charAt(i)) {
                    if (j != 0) {
                        j = lps[j - 1];
                    } else {
                        i++;
                    }
                }
            }
            
            return -1;
        }
        
        private static int[] computeLPS(String pattern) {
            int[] lps = new int[pattern.length()];
            int len = 0, i = 1;
            
            while (i < pattern.length()) {
                if (pattern.charAt(i) == pattern.charAt(len)) {
                    len++;
                    lps[i] = len;
                    i++;
                } else {
                    if (len != 0) {
                        len = lps[len - 1];
                    } else {
                        lps[i] = 0;
                        i++;
                    }
                }
            }
            
            return lps;
        }
    }
    
    // =============================================
    // TREE ALGORITHMS
    // =============================================
    
    // Binary Tree Node
    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        
        TreeNode(int val) {
            this.val = val;
            this.left = null;
            this.right = null;
        }
    }
    
    static class TreeAlgorithms {
        
        // Inorder Traversal
        public static List<Integer> inorderTraversal(TreeNode root) {
            List<Integer> result = new ArrayList<>();
            inorderTraversal(root, result);
            return result;
        }
        
        private static void inorderTraversal(TreeNode node, List<Integer> result) {
            if (node != null) {
                inorderTraversal(node.left, result);
                result.add(node.val);
                inorderTraversal(node.right, result);
            }
        }
        
        // Preorder Traversal
        public static List<Integer> preorderTraversal(TreeNode root) {
            List<Integer> result = new ArrayList<>();
            preorderTraversal(root, result);
            return result;
        }
        
        private static void preorderTraversal(TreeNode node, List<Integer> result) {
            if (node != null) {
                result.add(node.val);
                preorderTraversal(node.left, result);
                preorderTraversal(node.right, result);
            }
        }
        
        // Postorder Traversal
        public static List<Integer> postorderTraversal(TreeNode root) {
            List<Integer> result = new ArrayList<>();
            postorderTraversal(root, result);
            return result;
        }
        
        private static void postorderTraversal(TreeNode node, List<Integer> result) {
            if (node != null) {
                postorderTraversal(node.left, result);
                postorderTraversal(node.right, result);
                result.add(node.val);
            }
        }
        
        // Level Order Traversal
        public static List<List<Integer>> levelOrder(TreeNode root) {
            List<List<Integer>> result = new ArrayList<>();
            if (root == null) return result;
            
            Queue<TreeNode> queue = new LinkedList<>();
            queue.offer(root);
            
            while (!queue.isEmpty()) {
                int levelSize = queue.size();
                List<Integer> currentLevel = new ArrayList<>();
                
                for (int i = 0; i < levelSize; i++) {
                    TreeNode node = queue.poll();
                    currentLevel.add(node.val);
                    
                    if (node.left != null) queue.offer(node.left);
                    if (node.right != null) queue.offer(node.right);
                }
                
                result.add(currentLevel);
            }
            
            return result;
        }
        
        // Maximum Depth of Binary Tree
        public static int maxDepth(TreeNode root) {
            if (root == null) return 0;
            return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
        }
        
        // Validate Binary Search Tree
        public static boolean isValidBST(TreeNode root) {
            return isValidBST(root, null, null);
        }
        
        private static boolean isValidBST(TreeNode node, Integer min, Integer max) {
            if (node == null) return true;
            if ((min != null && node.val <= min) || (max != null && node.val >= max)) {
                return false;
            }
            return isValidBST(node.left, min, node.val) && isValidBST(node.right, node.val, max);
        }
        
        // Lowest Common Ancestor
        public static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
            if (root == null || root == p || root == q) return root;
            
            TreeNode left = lowestCommonAncestor(root.left, p, q);
            TreeNode right = lowestCommonAncestor(root.right, p, q);
            
            if (left != null && right != null) return root;
            return left != null ? left : right;
        }
        
        // Serialize and Deserialize Binary Tree
        public static String serialize(TreeNode root) {
            if (root == null) return "null";
            
            Queue<TreeNode> queue = new LinkedList<>();
            queue.offer(root);
            StringBuilder sb = new StringBuilder();
            
            while (!queue.isEmpty()) {
                TreeNode node = queue.poll();
                if (node == null) {
                    sb.append("null,");
                    continue;
                }
                
                sb.append(node.val).append(",");
                queue.offer(node.left);
                queue.offer(node.right);
            }
            
            return sb.toString();
        }
        
        public static TreeNode deserialize(String data) {
            if (data.equals("null")) return null;
            
            String[] values = data.split(",");
            Queue<TreeNode> queue = new LinkedList<>();
            TreeNode root = new TreeNode(Integer.parseInt(values[0]));
            queue.offer(root);
            
            int i = 1;
            while (!queue.isEmpty() && i < values.length) {
                TreeNode node = queue.poll();
                
                if (!values[i].equals("null")) {
                    node.left = new TreeNode(Integer.parseInt(values[i]));
                    queue.offer(node.left);
                }
                i++;
                
                if (i < values.length && !values[i].equals("null")) {
                    node.right = new TreeNode(Integer.parseInt(values[i]));
                    queue.offer(node.right);
                }
                i++;
            }
            
            return root;
        }
    }
    
    // =============================================
    // GRAPH ALGORITHMS
    // =============================================
    
    // Graph Node
    static class GraphNode {
        int val;
        List<GraphNode> neighbors;
        
        GraphNode(int val) {
            this.val = val;
            this.neighbors = new ArrayList<>();
        }
    }
    
    static class GraphAlgorithms {
        
        // BFS Traversal
        public static List<Integer> bfs(int start, Map<Integer, List<Integer>> graph) {
            List<Integer> result = new ArrayList<>();
            if (!graph.containsKey(start)) return result;
            
            Queue<Integer> queue = new LinkedList<>();
            Set<Integer> visited = new HashSet<>();
            
            queue.offer(start);
            visited.add(start);
            
            while (!queue.isEmpty()) {
                int node = queue.poll();
                result.add(node);
                
                for (int neighbor : graph.get(node)) {
                    if (!visited.contains(neighbor)) {
                        visited.add(neighbor);
                        queue.offer(neighbor);
                    }
                }
            }
            
            return result;
        }
        
        // DFS Traversal
        public static List<Integer> dfs(int start, Map<Integer, List<Integer>> graph) {
            List<Integer> result = new ArrayList<>();
            Set<Integer> visited = new HashSet<>();
            dfs(start, graph, visited, result);
            return result;
        }
        
        private static void dfs(int node, Map<Integer, List<Integer>> graph, 
                               Set<Integer> visited, List<Integer> result) {
            if (!graph.containsKey(node) || visited.contains(node)) return;
            
            visited.add(node);
            result.add(node);
            
            for (int neighbor : graph.get(node)) {
                dfs(neighbor, graph, visited, result);
            }
        }
        
        // Dijkstra's Algorithm
        public static Map<Integer, Integer> dijkstra(int start, Map<Integer, List<int[]>> graph) {
            Map<Integer, Integer> distances = new HashMap<>();
            PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
            
            distances.put(start, 0);
            pq.offer(new int[]{start, 0});
            
            while (!pq.isEmpty()) {
                int[] current = pq.poll();
                int node = current[0];
                int distance = current[1];
                
                if (distance > distances.getOrDefault(node, Integer.MAX_VALUE)) continue;
                
                if (graph.containsKey(node)) {
                    for (int[] edge : graph.get(node)) {
                        int neighbor = edge[0];
                        int weight = edge[1];
                        int newDistance = distance + weight;
                        
                        if (newDistance < distances.getOrDefault(neighbor, Integer.MAX_VALUE)) {
                            distances.put(neighbor, newDistance);
                            pq.offer(new int[]{neighbor, newDistance});
                        }
                    }
                }
            }
            
            return distances;
        }
        
        // Topological Sort
        public static List<Integer> topologicalSort(int numCourses, List<int[]> prerequisites) {
            Map<Integer, List<Integer>> graph = new HashMap<>();
            int[] inDegree = new int[numCourses];
            
            for (int[] prereq : prerequisites) {
                int course = prereq[0];
                int prerequisite = prereq[1];
                
                graph.computeIfAbsent(prerequisite, k -> new ArrayList<>()).add(course);
                inDegree[course]++;
            }
            
            Queue<Integer> queue = new LinkedList<>();
            for (int i = 0; i < numCourses; i++) {
                if (inDegree[i] == 0) {
                    queue.offer(i);
                }
            }
            
            List<Integer> result = new ArrayList<>();
            while (!queue.isEmpty()) {
                int course = queue.poll();
                result.add(course);
                
                if (graph.containsKey(course)) {
                    for (int neighbor : graph.get(course)) {
                        inDegree[neighbor]--;
                        if (inDegree[neighbor] == 0) {
                            queue.offer(neighbor);
                        }
                    }
                }
            }
            
            return result.size() == numCourses ? result : new ArrayList<>();
        }
        
        // Union-Find (Disjoint Set Union)
        static class DSU {
            int[] parent;
            int[] rank;
            
            public DSU(int n) {
                parent = new int[n];
                rank = new int[n];
                for (int i = 0; i < n; i++) {
                    parent[i] = i;
                }
            }
            
            public int find(int x) {
                if (parent[x] != x) {
                    parent[x] = find(parent[x]);
                }
                return parent[x];
            }
            
            public void union(int x, int y) {
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
        }
    }
    
    // =============================================
    // DYNAMIC PROGRAMMING
    // =============================================
    
    static class DynamicProgramming {
        
        // Fibonacci (DP)
        public static long fibonacci(int n) {
            if (n <= 1) return n;
            
            long[] dp = new long[n + 1];
            dp[0] = 0;
            dp[1] = 1;
            
            for (int i = 2; i <= n; i++) {
                dp[i] = dp[i - 1] + dp[i - 2];
            }
            
            return dp[n];
        }
        
        // Coin Change Problem
        public static int coinChange(int[] coins, int amount) {
            int[] dp = new int[amount + 1];
            Arrays.fill(dp, amount + 1);
            dp[0] = 0;
            
            for (int i = 1; i <= amount; i++) {
                for (int coin : coins) {
                    if (coin <= i) {
                        dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                    }
                }
            }
            
            return dp[amount] == amount + 1 ? -1 : dp[amount];
        }
        
        // Longest Increasing Subsequence
        public static int lengthOfLIS(int[] nums) {
            if (nums.length == 0) return 0;
            
            int[] dp = new int[nums.length];
            Arrays.fill(dp, 1);
            
            for (int i = 1; i < nums.length; i++) {
                for (int j = 0; j < i; j++) {
                    if (nums[j] < nums[i]) {
                        dp[i] = Math.max(dp[i], dp[j] + 1);
                    }
                }
            }
            
            return Arrays.stream(dp).max().getAsInt();
        }
        
        // 0/1 Knapsack Problem
        public static int knapsack(int capacity, int[] weights, int[] values) {
            int n = weights.length;
            int[][] dp = new int[n + 1][capacity + 1];
            
            for (int i = 1; i <= n; i++) {
                for (int w = 0; w <= capacity; w++) {
                    if (weights[i - 1] <= w) {
                        dp[i][w] = Math.max(dp[i - 1][w], 
                                          values[i - 1] + dp[i - 1][w - weights[i - 1]]);
                    } else {
                        dp[i][w] = dp[i - 1][w];
                    }
                }
            }
            
            return dp[n][capacity];
        }
        
        // Longest Common Subsequence
        public static int longestCommonSubsequence(String text1, String text2) {
            int m = text1.length(), n = text2.length();
            int[][] dp = new int[m + 1][n + 1];
            
            for (int i = 1; i <= m; i++) {
                for (int j = 1; j <= n; j++) {
                    if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                        dp[i][j] = dp[i - 1][j - 1] + 1;
                    } else {
                        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                    }
                }
            }
            
            return dp[m][n];
        }
        
        // Minimum Edit Distance
        public static int minEditDistance(String word1, String word2) {
            int m = word1.length(), n = word2.length();
            int[][] dp = new int[m + 1][n + 1];
            
            for (int i = 0; i <= m; i++) dp[i][0] = i;
            for (int j = 0; j <= n; j++) dp[0][j] = j;
            
            for (int i = 1; i <= m; i++) {
                for (int j = 1; j <= n; j++) {
                    if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                        dp[i][j] = dp[i - 1][j - 1];
                    } else {
                        dp[i][j] = 1 + Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
                    }
                }
            }
            
            return dp[m][n];
        }
    }
    
    // =============================================
    // BIT MANIPULATION
    // =============================================
    
    static class BitManipulation {
        
        // Count set bits
        public static int countSetBits(int n) {
            int count = 0;
            while (n > 0) {
                count += n & 1;
                n >>= 1;
            }
            return count;
        }
        
        // Check if power of 2
        public static boolean isPowerOfTwo(int n) {
            return n > 0 && (n & (n - 1)) == 0;
        }
        
        // Single Number (XOR)
        public static int singleNumber(int[] nums) {
            int result = 0;
            for (int num : nums) {
                result ^= num;
            }
            return result;
        }
        
        // Reverse bits
        public static int reverseBits(int n) {
            int result = 0;
            for (int i = 0; i < 32; i++) {
                result = (result << 1) | (n & 1);
                n >>= 1;
            }
            return result;
        }
        
        // Hamming distance
        public static int hammingDistance(int x, int y) {
            return countSetBits(x ^ y);
        }
        
        // Get bit at position
        public static boolean getBit(int n, int pos) {
            return (n & (1 << pos)) != 0;
        }
        
        // Set bit at position
        public static int setBit(int n, int pos) {
            return n | (1 << pos);
        }
        
        // Clear bit at position
        public static int clearBit(int n, int pos) {
            return n & ~(1 << pos);
        }
        
        // Toggle bit at position
        public static int toggleBit(int n, int pos) {
            return n ^ (1 << pos);
        }
    }
    
    // =============================================
    // MATHEMATICAL ALGORITHMS
    // =============================================
    
    static class MathematicalAlgorithms {
        
        // GCD (Euclidean Algorithm)
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
        
        // Check if prime
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
        
        // Generate prime factors
        public static List<Long> primeFactors(long n) {
            List<Long> factors = new ArrayList<>();
            
            // Handle 2 separately
            while (n % 2 == 0) {
                factors.add(2L);
                n /= 2;
            }
            
            // Check odd divisors
            for (long i = 3; i * i <= n; i += 2) {
                while (n % i == 0) {
                    factors.add(i);
                    n /= i;
                }
            }
            
            // If remaining n is prime
            if (n > 2) {
                factors.add(n);
            }
            
            return factors;
        }
    }
    
    // =============================================
    // UTILITY METHODS
    // =============================================
    
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
        
        // Generate random array
        public static int[] generateRandomArray(int n, int min, int max) {
            Random rand = new Random();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = rand.nextInt(max - min + 1) + min;
            }
            return arr;
        }
    }
    
    // =============================================
    // MAIN SOLVE FUNCTION
    // =============================================
    
    public static void solve() {
        out.println("=== Algorithm Templates Demonstration ===\n");
        
        // Test sorting algorithms
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        out.println("Original array:");
        Utils.printArray(arr);
        
        // Test different sorting algorithms
        int[] testArr = arr.clone();
        SortingAlgorithms.bubbleSort(testArr);
        out.println("Bubble Sort:");
        Utils.printArray(testArr);
        
        testArr = arr.clone();
        SortingAlgorithms.selectionSort(testArr);
        out.println("Selection Sort:");
        Utils.printArray(testArr);
        
        testArr = arr.clone();
        SortingAlgorithms.insertionSort(testArr);
        out.println("Insertion Sort:");
        Utils.printArray(testArr);
        
        testArr = arr.clone();
        SortingAlgorithms.mergeSort(testArr);
        out.println("Merge Sort:");
        Utils.printArray(testArr);
        
        testArr = arr.clone();
        SortingAlgorithms.quickSort(testArr);
        out.println("Quick Sort:");
        Utils.printArray(testArr);
        
        // Test searching algorithms
        int[] sortedArr = arr.clone();
        Arrays.sort(sortedArr);
        int target = 25;
        out.println("Linear search for " + target + ": " + SearchingAlgorithms.linearSearch(sortedArr, target));
        out.println("Binary search for " + target + ": " + SearchingAlgorithms.binarySearch(sortedArr, target));
        
        // Test array algorithms
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        out.println("Maximum subarray sum: " + ArrayAlgorithms.maxSubarraySum(nums));
        
        int[] twoSumArr = {2, 7, 11, 15};
        int[] twoSumResult = ArrayAlgorithms.twoSum(twoSumArr, 9);
        out.println("Two sum result: " + Arrays.toString(twoSumResult));
        
        // Test string algorithms
        String str = "racecar";
        out.println("Is \"" + str + "\" palindrome: " + StringAlgorithms.isPalindrome(str));
        
        String lps = StringAlgorithms.longestPalindrome("babad");
        out.println("Longest palindrome substring: " + lps);
        
        // Test mathematical algorithms
        out.println("GCD of 48 and 18: " + MathematicalAlgorithms.gcd(48, 18));
        out.println("LCM of 48 and 18: " + MathematicalAlgorithms.lcm(48, 18));
        out.println("Is 17 prime: " + MathematicalAlgorithms.isPrime(17));
        
        // Test DP algorithms
        out.println("Fibonacci(10): " + DynamicProgramming.fibonacci(10));
        
        int[] coins = {1, 2, 5};
        out.println("Coin change for 11: " + DynamicProgramming.coinChange(coins, 11));
        
        // Test bit manipulation
        out.println("Set bits in 13: " + BitManipulation.countSetBits(13));
        out.println("Is 16 power of 2: " + BitManipulation.isPowerOfTwo(16));
        
        // Test tree algorithms
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(3);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(2);
        root.left.right = new TreeNode(4);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(8);
        
        out.println("Inorder traversal: " + TreeAlgorithms.inorderTraversal(root));
        out.println("Preorder traversal: " + TreeAlgorithms.preorderTraversal(root));
        out.println("Postorder traversal: " + TreeAlgorithms.postorderTraversal(root));
        out.println("Max depth: " + TreeAlgorithms.maxDepth(root));
        out.println("Is BST: " + TreeAlgorithms.isValidBST(root));
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
