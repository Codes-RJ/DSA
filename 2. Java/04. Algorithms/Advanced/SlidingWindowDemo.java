public class SlidingWindowDemo {
    static int maxWindowSum(int[] values, int k) {
        if (k > values.length) {
            return 0;
        }

        int windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += values[i];
        }

        int best = windowSum;
        for (int i = k; i < values.length; i++) {
            windowSum += values[i] - values[i - k];
            best = Math.max(best, windowSum);
        }
        return best;
    }

    public static void main(String[] args) {
        int[] values = {2, 1, 5, 1, 3, 2};
        System.out.println("Maximum sum of window size 3: " + maxWindowSum(values, 3));
    }
}
