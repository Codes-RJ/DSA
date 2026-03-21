import java.util.ArrayList;
import java.util.List;

public class ArraysAndArrayListDemo {
    public static int linearSearch(List<Integer> values, int target) {
        for (int i = 0; i < values.size(); i++) {
            if (values.get(i) == target) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        List<Integer> values = new ArrayList<>();
        values.add(10);
        values.add(20);
        values.add(30);
        values.add(40);

        int target = 30;
        System.out.println("Index of " + target + ": " + linearSearch(values, target));
    }
}
