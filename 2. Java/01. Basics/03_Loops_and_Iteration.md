# Java Loops and Iteration

## Overview

Loops are fundamental control structures that allow repeated execution of code blocks. Java provides several types of loops and iteration mechanisms, each suited for different scenarios. Understanding loops and their relationship with data structures is crucial for efficient algorithm implementation.

## Types of Loops

### for Loop

#### Traditional for Loop
```java
public class TraditionalForLoop {
    public static void main(String[] args) {
        // Basic for loop
        for (int i = 0; i < 5; i++) {
            System.out.println("Iteration " + i);
        }
        
        // For loop with multiple variables
        for (int i = 0, j = 10; i < 5 && j > 5; i++, j--) {
            System.out.println("i: " + i + ", j: " + j);
        }
        
        // For loop with arrays
        int[] numbers = {10, 20, 30, 40, 50};
        for (int i = 0; i < numbers.length; i++) {
            System.out.println("numbers[" + i + "] = " + numbers[i]);
        }
        
        // Reverse iteration
        for (int i = numbers.length - 1; i >= 0; i--) {
            System.out.println("Reverse: " + numbers[i]);
        }
        
        // For loop with step
        for (int i = 0; i < 10; i += 2) {
            System.out.println("Even numbers: " + i);
        }
        
        // Nested for loops
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                System.out.print(i * j + " ");
            }
            System.out.println();
        }
        
        // For loop with collections
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
        for (int i = 0; i < names.size(); i++) {
            System.out.println("Name " + i + ": " + names.get(i));
        }
    }
}
```

#### Enhanced for Loop (for-each)
```java
import java.util.*;

public class EnhancedForLoop {
    public static void main(String[] args) {
        // Array iteration
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.println("Array elements:");
        for (int num : numbers) {
            System.out.println(num);
        }
        
        // List iteration
        List<String> fruits = Arrays.asList("Apple", "Banana", "Cherry");
        System.out.println("Fruits:");
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
        
        // Set iteration
        Set<Integer> uniqueNumbers = new HashSet<>(Arrays.asList(1, 2, 3, 2, 1));
        System.out.println("Unique numbers:");
        for (int num : uniqueNumbers) {
            System.out.println(num);
        }
        
        // Map iteration (entry set)
        Map<String, Integer> scores = new HashMap<>();
        scores.put("Alice", 95);
        scores.put("Bob", 87);
        scores.put("Charlie", 92);
        
        System.out.println("Scores:");
        for (Map.Entry<String, Integer> entry : scores.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        
        // 2D array iteration
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        System.out.println("Matrix elements:");
        for (int[] row : matrix) {
            for (int element : row) {
                System.out.print(element + " ");
            }
            System.out.println();
        }
        
        // Custom object iteration
        List<Person> people = Arrays.asList(
            new Person("Alice", 25),
            new Person("Bob", 30),
            new Person("Charlie", 20)
        );
        
        System.out.println("People:");
        for (Person person : people) {
            System.out.println(person.getName() + " (" + person.getAge() + ")");
        }
    }
}

class Person {
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() { return name; }
    public int getAge() { return age; }
}
```

### while Loop

#### Basic while Loop
```java
import java.util.*;

public class WhileLoop {
    public static void main(String[] args) {
        // Simple counter
        int count = 0;
        while (count < 5) {
            System.out.println("Count: " + count);
            count++;
        }
        
        // Reading until condition
        Scanner scanner = new Scanner(System.in);
        List<Integer> inputs = new ArrayList<>();
        
        System.out.println("Enter numbers (enter 0 to stop):");
        int number;
        while (scanner.hasNextInt()) {
            number = scanner.nextInt();
            if (number == 0) break;
            inputs.add(number);
        }
        
        System.out.println("You entered: " + inputs);
        scanner.close();
        
        // Processing queue
        Queue<String> tasks = new LinkedList<>();
        tasks.add("Task 1");
        tasks.add("Task 2");
        tasks.add("Task 3");
        
        System.out.println("Processing tasks:");
        while (!tasks.isEmpty()) {
            System.out.println("Processing: " + tasks.poll());
        }
        
        // File reading simulation
        List<String> lines = Arrays.asList("Line 1", "Line 2", "Line 3", "");
        Iterator<String> iterator = lines.iterator();
        
        System.out.println("Reading lines:");
        while (iterator.hasNext()) {
            String line = iterator.next();
            if (line.isEmpty()) break;
            System.out.println(line);
        }
    }
}
```

#### while Loop with Data Structures
```java
import java.util.*;

public class WhileWithDataStructures {
    public static void main(String[] args) {
        // Stack processing
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        
        System.out.println("Stack elements:");
        while (!stack.isEmpty()) {
            System.out.println(stack.pop());
        }
        
        // Iterator-based processing
        List<String> words = Arrays.asList("Hello", "World", "Java", "Programming");
        Iterator<String> wordIterator = words.iterator();
        
        System.out.println("Words with length > 4:");
        while (wordIterator.hasNext()) {
            String word = wordIterator.next();
            if (word.length() > 4) {
                System.out.println(word);
            }
        }
        
        // ListIterator for bidirectional traversal
        List<Integer> numbers = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        ListIterator<Integer> listIterator = numbers.listIterator(numbers.size());
        
        System.out.println("Reverse traversal:");
        while (listIterator.hasPrevious()) {
            System.out.println(listIterator.previous());
        }
        
        // Processing with condition
        int[] data = {1, 3, 5, 7, 9, 2, 4, 6, 8, 10};
        int index = 0;
        
        System.out.println("Odd numbers:");
        while (index < data.length) {
            if (data[index] % 2 == 0) {
                break;  // Stop at first even number
            }
            System.out.println(data[index]);
            index++;
        }
    }
}
```

### do-while Loop

#### Basic do-while Loop
```java
import java.util.*;

public class DoWhileLoop {
    public static void main(String[] args) {
        // Guaranteed at least one execution
        int count = 0;
        do {
            System.out.println("Count: " + count);
            count++;
        } while (count < 5);
        
        // Menu example
        Scanner scanner = new Scanner(System.in);
        int choice;
        
        do {
            System.out.println("\nMenu:");
            System.out.println("1. Option 1");
            System.out.println("2. Option 2");
            System.out.println("3. Exit");
            System.out.print("Enter choice: ");
            
            if (scanner.hasNextInt()) {
                choice = scanner.nextInt();
                
                switch (choice) {
                    case 1:
                        System.out.println("You chose Option 1");
                        break;
                    case 2:
                        System.out.println("You chose Option 2");
                        break;
                    case 3:
                        System.out.println("Exiting...");
                        break;
                    default:
                        System.out.println("Invalid choice");
                }
            } else {
                System.out.println("Invalid input");
                choice = 0;  // Continue loop
                scanner.next();  // Clear invalid input
            }
        } while (choice != 3);
        
        // Input validation
        int number;
        do {
            System.out.print("Enter a positive number: ");
            while (!scanner.hasNextInt()) {
                System.out.println("That's not a number!");
                System.out.print("Enter a positive number: ");
                scanner.next();
            }
            number = scanner.nextInt();
        } while (number <= 0);
        
        System.out.println("You entered: " + number);
        scanner.close();
        
        // Game loop simulation
        Random random = new Random();
        int target = random.nextInt(100) + 1;
        int guess;
        int attempts = 0;
        
        System.out.println("Guess the number (1-100):");
        do {
            System.out.print("Your guess: ");
            guess = scanner.nextInt();
            attempts++;
            
            if (guess < target) {
                System.out.println("Too low!");
            } else if (guess > target) {
                System.out.println("Too high!");
            } else {
                System.out.println("Correct! You got it in " + attempts + " attempts.");
            }
        } while (guess != target);
    }
}
```

## Loop Control Statements

### break Statement
```java
public class BreakStatement {
    public static void main(String[] args) {
        // Break out of loop
        for (int i = 0; i < 10; i++) {
            if (i == 5) {
                System.out.println("Breaking at i = " + i);
                break;
            }
            System.out.println("i = " + i);
        }
        
        // Break in nested loops with label
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int target = 5;
        boolean found = false;
        
        outerLoop:
        for (int i = 0; i < matrix.length && !found; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == target) {
                    System.out.println("Found " + target + " at [" + i + "][" + j + "]");
                    found = true;
                    break outerLoop;  // Break both loops
                }
            }
        }
        
        // Break in switch within loop
        for (int i = 1; i <= 5; i++) {
            switch (i) {
                case 1:
                    System.out.println("One");
                    break;  // Break switch, not loop
                case 2:
                    System.out.println("Two");
                    break;
                case 3:
                    System.out.println("Three");
                    break;  // This breaks switch, loop continues
                default:
                    System.out.println("Other");
                    break;
            }
            System.out.println("Loop iteration " + i + " completed");
        }
        
        // Break with while loop
        int count = 0;
        while (true) {  // Infinite loop
            System.out.println("Count: " + count);
            count++;
            if (count >= 5) {
                break;  // Exit infinite loop
            }
        }
        
        // Break in data structure processing
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Eve");
        String searchName = "Charlie";
        
        for (String name : names) {
            if (name.equals(searchName)) {
                System.out.println("Found " + searchName);
                break;
            }
            System.out.println("Checking: " + name);
        }
    }
}
```

### continue Statement
```java
public class ContinueStatement {
    public static void main(String[] args) {
        // Skip even numbers
        System.out.println("Odd numbers:");
        for (int i = 0; i < 10; i++) {
            if (i % 2 == 0) {
                continue;  // Skip even numbers
            }
            System.out.println(i);
        }
        
        // Process only positive numbers
        int[] numbers = {1, -2, 3, -4, 5, -6, 7, -8, 9, -10};
        System.out.println("Positive numbers:");
        for (int num : numbers) {
            if (num < 0) {
                continue;  // Skip negative numbers
            }
            System.out.println(num);
        }
        
        // Continue in nested loops
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        System.out.println("Skipping multiples of 3:");
        
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] % 3 == 0) {
                    continue;  // Skip multiples of 3
                }
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        
        // Continue with while loop
        int i = 0;
        System.out.println("Numbers not divisible by 2 or 3:");
        while (i < 20) {
            i++;
            if (i % 2 == 0 || i % 3 == 0) {
                continue;  // Skip multiples of 2 or 3
            }
            System.out.println(i);
        }
        
        // Continue with data structures
        List<String> words = Arrays.asList("apple", "banana", "cherry", "date", "elderberry");
        System.out.println("Words starting with 'c':");
        
        for (String word : words) {
            if (!word.startsWith("c")) {
                continue;  // Skip words not starting with 'c'
            }
            System.out.println(word);
        }
        
        // Continue with labeled loops
        outer:
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (i == 2 && j == 2) {
                    System.out.println("Skipping (2,2)");
                    continue outer;  // Skip to next iteration of outer loop
                }
                System.out.println("(" + i + "," + j + ")");
            }
        }
    }
}
```

## Iterators and Loop Integration

### Iterator-Based Loops
```java
import java.util.*;

public class IteratorLoops {
    public static void main(String[] args) {
        // List with Iterator
        List<String> fruits = new ArrayList<>(Arrays.asList("Apple", "Banana", "Cherry", "Date"));
        
        System.out.println("Using Iterator:");
        Iterator<String> iterator = fruits.iterator();
        while (iterator.hasNext()) {
            String fruit = iterator.next();
            System.out.println(fruit);
        }
        
        // ListIterator for bidirectional access
        List<Integer> numbers = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        ListIterator<Integer> listIterator = numbers.listIterator();
        
        System.out.println("Forward with ListIterator:");
        while (listIterator.hasNext()) {
            System.out.println(listIterator.next());
        }
        
        System.out.println("Backward with ListIterator:");
        while (listIterator.hasPrevious()) {
            System.out.println(listIterator.previous());
        }
        
        // Safe removal while iterating
        List<String> names = new ArrayList<>(Arrays.asList("Alice", "Bob", "Charlie", "David", "Eve"));
        System.out.println("Original names: " + names);
        
        Iterator<String> nameIterator = names.iterator();
        while (nameIterator.hasNext()) {
            String name = nameIterator.next();
            if (name.startsWith("B")) {
                nameIterator.remove();  // Safe removal
            }
        }
        System.out.println("After removing names starting with 'B': " + names);
        
        // Set iteration
        Set<Integer> uniqueNumbers = new HashSet<>(Arrays.asList(3, 1, 4, 1, 5, 9, 2, 6, 5));
        System.out.println("Set elements:");
        Iterator<Integer> setIterator = uniqueNumbers.iterator();
        while (setIterator.hasNext()) {
            System.out.println(setIterator.next());
        }
        
        // Map iteration
        Map<String, Integer> scores = new HashMap<>();
        scores.put("Alice", 95);
        scores.put("Bob", 87);
        scores.put("Charlie", 92);
        
        System.out.println("Map entries:");
        Iterator<Map.Entry<String, Integer>> mapIterator = scores.entrySet().iterator();
        while (mapIterator.hasNext()) {
            Map.Entry<String, Integer> entry = mapIterator.next();
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        
        // Modifying while iterating
        List<Integer> squares = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        System.out.println("Original squares: " + squares);
        
        ListIterator<Integer> modifierIterator = squares.listIterator();
        while (modifierIterator.hasNext()) {
            int value = modifierIterator.next();
            modifierIterator.set(value * value);  // Replace with square
        }
        System.out.println("Squared values: " + squares);
    }
}
```

### forEach Method (Java 8+)
```java
import java.util.*;
import java.util.function.Consumer;

public class ForEachMethod {
    public static void main(String[] args) {
        // List forEach
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");
        System.out.println("Names using forEach:");
        names.forEach(name -> System.out.println(name));
        
        // Method reference
        System.out.println("Names using method reference:");
        names.forEach(System.out::println);
        
        // Map forEach
        Map<String, Integer> scores = new HashMap<>();
        scores.put("Alice", 95);
        scores.put("Bob", 87);
        scores.put("Charlie", 92);
        
        System.out.println("Scores using forEach:");
        scores.forEach((name, score) -> System.out.println(name + ": " + score));
        
        // Set forEach
        Set<Integer> numbers = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5));
        System.out.println("Numbers using forEach:");
        numbers.forEach(num -> System.out.println(num * 2));  // Double each number
        
        // Array forEach (Arrays.stream)
        int[] array = {1, 2, 3, 4, 5};
        System.out.println("Array elements using forEach:");
        Arrays.stream(array).forEach(num -> System.out.println(num));
        
        // Custom Consumer
        Consumer<String> printer = str -> System.out.println("-> " + str.toUpperCase());
        System.out.println("Custom consumer:");
        names.forEach(printer);
        
        // Nested forEach
        List<List<Integer>> matrix = Arrays.asList(
            Arrays.asList(1, 2, 3),
            Arrays.asList(4, 5, 6),
            Arrays.asList(7, 8, 9)
        );
        
        System.out.println("Matrix using nested forEach:");
        matrix.forEach(row -> {
            row.forEach(element -> System.out.print(element + " "));
            System.out.println();
        });
        
        // forEach with filtering
        List<Integer> numbersList = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        System.out.println("Even numbers:");
        numbersList.stream()
            .filter(num -> num % 2 == 0)
            .forEach(num -> System.out.println(num));
        
        // forEach with complex operations
        Map<String, List<Integer>> studentGrades = new HashMap<>();
        studentGrades.put("Alice", Arrays.asList(95, 87, 92));
        studentGrades.put("Bob", Arrays.asList(78, 85, 90));
        studentGrades.put("Charlie", Arrays.asList(88, 92, 95));
        
        System.out.println("Student averages:");
        studentGrades.forEach((student, grades) -> {
            double average = grades.stream()
                .mapToInt(Integer::intValue)
                .average()
                .orElse(0.0);
            System.out.println(student + ": " + String.format("%.2f", average));
        });
    }
}
```

## Loops with Different Data Structures

### Array Loops
```java
public class ArrayLoops {
    public static void main(String[] args) {
        // Single-dimensional array
        int[] numbers = {10, 20, 30, 40, 50};
        
        // Traditional for loop
        System.out.println("Traditional for loop:");
        for (int i = 0; i < numbers.length; i++) {
            System.out.println("numbers[" + i + "] = " + numbers[i]);
        }
        
        // Enhanced for loop
        System.out.println("Enhanced for loop:");
        for (int num : numbers) {
            System.out.println(num);
        }
        
        // While loop
        System.out.println("While loop:");
        int index = 0;
        while (index < numbers.length) {
            System.out.println(numbers[index]);
            index++;
        }
        
        // 2D array
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        
        System.out.println("2D array with nested for loops:");
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        
        System.out.println("2D array with enhanced for loops:");
        for (int[] row : matrix) {
            for (int element : row) {
                System.out.print(element + " ");
            }
            System.out.println();
        }
        
        // Jagged array
        int[][] jagged = {{1, 2}, {3, 4, 5}, {6, 7, 8, 9}};
        
        System.out.println("Jagged array:");
        for (int i = 0; i < jagged.length; i++) {
            for (int j = 0; j < jagged[i].length; j++) {
                System.out.print(jagged[i][j] + " ");
            }
            System.out.println();
        }
        
        // Array operations
        System.out.println("Array operations:");
        int sum = 0;
        int max = numbers[0];
        int min = numbers[0];
        
        for (int num : numbers) {
            sum += num;
            if (num > max) max = num;
            if (num < min) min = num;
        }
        
        System.out.println("Sum: " + sum);
        System.out.println("Average: " + (double) sum / numbers.length);
        System.out.println("Max: " + max);
        System.out.println("Min: " + min);
        
        // String array
        String[] words = {"Hello", "World", "Java", "Programming"};
        System.out.println("String array:");
        for (String word : words) {
            System.out.println(word + " (length: " + word.length() + ")");
        }
    }
}
```

### Collection Loops
```java
import java.util.*;

public class CollectionLoops {
    public static void main(String[] args) {
        // List operations
        List<String> arrayList = new ArrayList<>(Arrays.asList("A", "B", "C", "D", "E"));
        
        System.out.println("ArrayList with index-based loop:");
        for (int i = 0; i < arrayList.size(); i++) {
            System.out.println(i + ": " + arrayList.get(i));
        }
        
        System.out.println("ArrayList with enhanced for loop:");
        for (String item : arrayList) {
            System.out.println(item);
        }
        
        System.out.println("ArrayList with iterator:");
        Iterator<String> iterator = arrayList.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
        
        System.out.println("ArrayList with forEach:");
        arrayList.forEach(System.out::println);
        
        // LinkedList operations
        LinkedList<Integer> linkedList = new LinkedList<>();
        linkedList.add(10);
        linkedList.add(20);
        linkedList.add(30);
        
        System.out.println("LinkedList:");
        for (Integer num : linkedList) {
            System.out.println(num);
        }
        
        // Set operations
        Set<String> hashSet = new HashSet<>(Arrays.asList("Apple", "Banana", "Cherry", "Apple"));
        
        System.out.println("HashSet (unordered):");
        for (String fruit : hashSet) {
            System.out.println(fruit);
        }
        
        Set<String> treeSet = new TreeSet<>(hashSet);
        System.out.println("TreeSet (sorted):");
        for (String fruit : treeSet) {
            System.out.println(fruit);
        }
        
        // Queue operations
        Queue<String> queue = new LinkedList<>();
        queue.offer("First");
        queue.offer("Second");
        queue.offer("Third");
        
        System.out.println("Queue processing:");
        while (!queue.isEmpty()) {
            System.out.println("Processing: " + queue.poll());
        }
        
        // Stack operations
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        
        System.out.println("Stack processing:");
        while (!stack.isEmpty()) {
            System.out.println("Popping: " + stack.pop());
        }
        
        // Map operations
        Map<String, Integer> map = new HashMap<>();
        map.put("One", 1);
        map.put("Two", 2);
        map.put("Three", 3);
        
        System.out.println("Map keys:");
        for (String key : map.keySet()) {
            System.out.println(key);
        }
        
        System.out.println("Map values:");
        for (Integer value : map.values()) {
            System.out.println(value);
        }
        
        System.out.println("Map entries:");
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }
        
        System.out.println("Map with forEach:");
        map.forEach((key, value) -> System.out.println(key + " -> " + value));
    }
}
```

## Advanced Loop Patterns

### Nested Loops with Data Structures
```java
import java.util.*;

public class NestedLoopsWithStructures {
    public static void main(String[] args) {
        // Matrix multiplication simulation
        int[][] matrixA = {{1, 2}, {3, 4}};
        int[][] matrixB = {{5, 6}, {7, 8}};
        int[][] result = new int[2][2];
        
        System.out.println("Matrix multiplication:");
        for (int i = 0; i < matrixA.length; i++) {
            for (int j = 0; j < matrixB[0].length; j++) {
                for (int k = 0; k < matrixB.length; k++) {
                    result[i][j] += matrixA[i][k] * matrixB[k][j];
                }
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
        
        // List of lists processing
        List<List<Integer>> listOfLists = Arrays.asList(
            Arrays.asList(1, 2, 3),
            Arrays.asList(4, 5, 6),
            Arrays.asList(7, 8, 9)
        );
        
        System.out.println("List of lists:");
        for (List<Integer> innerList : listOfLists) {
            for (Integer number : innerList) {
                System.out.print(number + " ");
            }
            System.out.println();
        }
        
        // Cartesian product
        List<String> colors = Arrays.asList("Red", "Green", "Blue");
        List<String> sizes = Arrays.asList("S", "M", "L");
        
        System.out.println("Cartesian product:");
        for (String color : colors) {
            for (String size : sizes) {
                System.out.println(color + " " + size);
            }
        }
        
        // Nested map processing
        Map<String, Map<String, Integer>> nestedMap = new HashMap<>();
        Map<String, Integer> aliceScores = new HashMap<>();
        aliceScores.put("Math", 95);
        aliceScores.put("Science", 87);
        
        Map<String, Integer> bobScores = new HashMap<>();
        bobScores.put("Math", 78);
        bobScores.put("Science", 92);
        
        nestedMap.put("Alice", aliceScores);
        nestedMap.put("Bob", bobScores);
        
        System.out.println("Nested map:");
        for (Map.Entry<String, Map<String, Integer>> studentEntry : nestedMap.entrySet()) {
            System.out.println("Student: " + studentEntry.getKey());
            for (Map.Entry<String, Integer> scoreEntry : studentEntry.getValue().entrySet()) {
                System.out.println("  " + scoreEntry.getKey() + ": " + scoreEntry.getValue());
            }
        }
        
        // Finding pairs in array
        int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int target = 10;
        
        System.out.println("Pairs that sum to " + target + ":");
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                if (numbers[i] + numbers[j] == target) {
                    System.out.println("(" + numbers[i] + ", " + numbers[j] + ")");
                }
            }
        }
    }
}
```

### Stream-based Iteration (Java 8+)
```java
import java.util.*;
import java.util.stream.*;

public class StreamIteration {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        
        // Filter and process
        System.out.println("Even numbers doubled:");
        numbers.stream()
            .filter(n -> n % 2 == 0)
            .map(n -> n * 2)
            .forEach(System.out::println);
        
        // Sum of squares
        int sumOfSquares = numbers.stream()
            .map(n -> n * n)
            .mapToInt(Integer::intValue)
            .sum();
        
        System.out.println("Sum of squares: " + sumOfSquares);
        
        // Collect to new list
        List<Integer> squares = numbers.stream()
            .map(n -> n * n)
            .collect(Collectors.toList());
        
        System.out.println("Squares: " + squares);
        
        // Group by condition
        Map<Boolean, List<Integer>> partitioned = numbers.stream()
            .collect(Collectors.partitioningBy(n -> n % 2 == 0));
        
        System.out.println("Even numbers: " + partitioned.get(true));
        System.out.println("Odd numbers: " + partitioned.get(false));
        
        // String operations
        List<String> words = Arrays.asList("hello", "world", "java", "stream", "api");
        
        System.out.println("Uppercase words:");
        words.stream()
            .map(String::toUpperCase)
            .forEach(System.out::println);
        
        // Filter by length
        List<String> longWords = words.stream()
            .filter(w -> w.length() > 4)
            .collect(Collectors.toList());
        
        System.out.println("Words longer than 4 characters: " + longWords);
        
        // Reduce operation
        Optional<String> concatenated = words.stream()
            .reduce((s1, s2) -> s1 + " " + s2);
        
        concatenated.ifPresent(System.out::println);
        
        // Parallel stream
        System.out.println("Parallel processing:");
        numbers.parallelStream()
            .map(n -> {
                System.out.println("Processing: " + n + " on " + Thread.currentThread().getName());
                return n * n;
            })
            .forEach(System.out::println);
        
        // Custom object processing
        List<Person> people = Arrays.asList(
            new Person("Alice", 25),
            new Person("Bob", 30),
            new Person("Charlie", 20),
            new Person("David", 35)
        );
        
        System.out.println("People older than 25:");
        people.stream()
            .filter(p -> p.getAge() > 25)
            .map(Person::getName)
            .forEach(System.out::println);
        
        // Group by age range
        Map<String, List<Person>> byAgeRange = people.stream()
            .collect(Collectors.groupingBy(p -> {
                if (p.getAge() < 25) return "Young";
                else if (p.getAge() < 35) return "Adult";
                else return "Senior";
            }));
        
        System.out.println("People by age range:");
        byAgeRange.forEach((range, personList) -> {
            System.out.println(range + ": " + personList);
        });
    }
}
```

## Performance Considerations

### Loop Performance Comparison
```java
import java.util.*;

public class LoopPerformance {
    public static void main(String[] args) {
        final int SIZE = 1000000;
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < SIZE; i++) {
            list.add(i);
        }
        
        // Traditional for loop
        long startTime = System.nanoTime();
        long sum1 = 0;
        for (int i = 0; i < list.size(); i++) {
            sum1 += list.get(i);
        }
        long duration1 = System.nanoTime() - startTime;
        
        // Enhanced for loop
        startTime = System.nanoTime();
        long sum2 = 0;
        for (Integer num : list) {
            sum2 += num;
        }
        long duration2 = System.nanoTime() - startTime;
        
        // Iterator
        startTime = System.nanoTime();
        long sum3 = 0;
        Iterator<Integer> iterator = list.iterator();
        while (iterator.hasNext()) {
            sum3 += iterator.next();
        }
        long duration3 = System.nanoTime() - startTime;
        
        // forEach method
        startTime = System.nanoTime();
        long[] sum4 = {0};
        list.forEach(num -> sum4[0] += num);
        long duration4 = System.nanoTime() - startTime;
        
        // Stream
        startTime = System.nanoTime();
        long sum5 = list.stream().mapToLong(Integer::longValue).sum();
        long duration5 = System.nanoTime() - startTime;
        
        System.out.println("Traditional for loop: " + duration1 + " ns");
        System.out.println("Enhanced for loop: " + duration2 + " ns");
        System.out.println("Iterator: " + duration3 + " ns");
        System.out.println("forEach method: " + duration4 + " ns");
        System.out.println("Stream: " + duration5 + " ns");
        
        System.out.println("All sums equal: " + 
            (sum1 == sum2 && sum2 == sum3 && sum3 == sum4[0] && sum4[0] == sum5));
        
        // LinkedList performance comparison
        LinkedList<Integer> linkedList = new LinkedList<>();
        for (int i = 0; i < 10000; i++) {
            linkedList.add(i);
        }
        
        // Index-based access (slow for LinkedList)
        startTime = System.nanoTime();
        long linkedListSum1 = 0;
        for (int i = 0; i < linkedList.size(); i++) {
            linkedListSum1 += linkedList.get(i);
        }
        duration1 = System.nanoTime() - startTime;
        
        // Iterator-based access (fast for LinkedList)
        startTime = System.nanoTime();
        long linkedListSum2 = 0;
        Iterator<Integer> linkedListIterator = linkedList.iterator();
        while (linkedListIterator.hasNext()) {
            linkedListSum2 += linkedListIterator.next();
        }
        duration2 = System.nanoTime() - startTime;
        
        System.out.println("\nLinkedList index-based: " + duration1 + " ns");
        System.out.println("LinkedList iterator-based: " + duration2 + " ns");
        System.out.println("Ratio: " + (double)duration1 / duration2);
    }
}
```

## Modern Java Loop Features

### var in Loops (Java 10+)
```java
import java.util.*;

public class VarInLoops {
    public static void main(String[] args) {
        // var with enhanced for loop
        var numbers = Arrays.asList(1, 2, 3, 4, 5);
        System.out.println("Using var with enhanced for loop:");
        for (var num : numbers) {
            System.out.println(num + " (type: " + ((Object)num).getClass().getSimpleName() + ")");
        }
        
        // var with traditional for loop
        System.out.println("Using var with traditional for loop:");
        for (var i = 0; i < numbers.size(); i++) {
            System.out.println(i + ": " + numbers.get(i) + 
                             " (type: " + ((Object)i).getClass().getSimpleName() + ")");
        }
        
        // var with collections
        var list = new ArrayList<String>();
        list.add("Hello");
        list.add("World");
        
        System.out.println("Using var with ArrayList:");
        for (var item : list) {
            System.out.println(item + " (type: " + ((Object)item).getClass().getSimpleName() + ")");
        }
        
        // var with maps
        var map = new HashMap<String, Integer>();
        map.put("One", 1);
        map.put("Two", 2);
        
        System.out.println("Using var with HashMap:");
        for (var entry : map.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }
        
        // var with streams
        var stream = numbers.stream();
        System.out.println("Stream operations with var:");
        stream.map(num -> num * 2)
              .forEach(System.out::println);
    }
}
```

## Best Practices

1. **Prefer enhanced for loops** for simple iteration over collections
2. **Use traditional for loops** when you need the index
3. **Use iterators** when you need to remove elements while iterating
4. **Use streams** for complex data processing and functional-style operations
5. **Be careful with infinite loops** - always have clear exit conditions
6. **Minimize loop overhead** by moving invariant code outside the loop
7. **Use appropriate loop type** based on the data structure and use case
8. **Consider performance** when choosing between iteration methods
9. **Use meaningful variable names** for loop counters
10. **Avoid modifying collections** while iterating (except through iterators)

## Conclusion

Loops and iteration are fundamental to Java programming, providing various ways to process data structures efficiently. From traditional loops to modern stream-based iteration, Java offers multiple approaches suited for different scenarios. Understanding the relationship between loops and data structures, along with performance considerations and modern language features, enables writing efficient, readable, and maintainable Java code. The choice of iteration method can significantly impact both performance and code clarity, making it essential to choose the right approach for each use case.
