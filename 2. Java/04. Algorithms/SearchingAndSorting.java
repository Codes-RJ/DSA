import java.util.Arrays;

public class SearchingAndSorting {
    public static int binarySearch(int[] values, int target) {
        int left = 0;
        int right = values.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (values[mid] == target) {
                return mid;
            } else if (values[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] values = {9, 4, 7, 1, 3};
        Arrays.sort(values);

        System.out.println("Sorted array: " + Arrays.toString(values));
        System.out.println("Index of 7: " + binarySearch(values, 7));
    }
}
