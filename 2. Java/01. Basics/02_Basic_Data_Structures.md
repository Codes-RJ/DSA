# Java Basic Data Structures

## Overview

Java provides a rich set of built-in data structures through both language features and the Java Collections Framework. Understanding these fundamental data structures is essential for efficient algorithm implementation and problem-solving in Java.

## Built-in Data Structures

### Arrays

#### Single-Dimensional Arrays
```java
public class ArrayBasics {
    public static void main(String[] args) {
        // Array declaration and initialization
        int[] numbers = {1, 2, 3, 4, 5};
        String[] names = {"Alice", "Bob", "Charlie"};
        double[] prices = new double[5];  // Initialized with default values
        
        // Access elements
        System.out.println("First number: " + numbers[0]);
        System.out.println("Array length: " + numbers.length);
        
        // Modify elements
        numbers[0] = 10;
        prices[0] = 99.99;
        
        // Iterate over arrays
        System.out.println("Numbers using for loop:");
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }
        
        System.out.println("Numbers using enhanced for loop:");
        for (int num : numbers) {
            System.out.println(num);
        }
        
        // Array operations
        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        System.out.println("Sum: " + sum);
        
        // Find maximum
        int max = numbers[0];
        for (int num : numbers) {
            if (num > max) {
                max = num;
            }
        }
        System.out.println("Maximum: " + max);
        
        // Array copying
        int[] copy = new int[numbers.length];
        System.arraycopy(numbers, 0, copy, 0, numbers.length);
        
        // Java 8+ array copying
        int[] modernCopy = Arrays.copyOf(numbers, numbers.length);
        
        System.out.println("Original: " + Arrays.toString(numbers));
        System.out.println("Copy: " + Arrays.toString(modernCopy));
    }
}
```

#### Multi-Dimensional Arrays
```java
public class MultiDimensionalArrays {
    public static void main(String[] args) {
        // 2D array (matrix)
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        
        // Access 2D array elements
        System.out.println("Element at [0][1]: " + matrix[0][1]);
        System.out.println("Matrix dimensions: " + matrix.length + "x" + matrix[0].length);
        
        // Iterate over 2D array
        System.out.println("Matrix elements:");
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        
        // Enhanced for loop for 2D array
        System.out.println("Matrix using enhanced for:");
        for (int[] row : matrix) {
            for (int element : row) {
                System.out.print(element + " ");
            }
            System.out.println();
        }
        
        // Jagged array (irregular dimensions)
        int[][] jagged = new int[3][];
        jagged[0] = new int[2];  // 2 elements
        jagged[1] = new int[4];  // 4 elements
        jagged[2] = new int[3];  // 3 elements
        
        // Initialize jagged array
        jagged[0] = new int[]{1, 2};
        jagged[1] = new int[]{3, 4, 5, 6};
        jagged[2] = new int[]{7, 8, 9};
        
        System.out.println("Jagged array:");
        for (int[] row : jagged) {
            System.out.println(Arrays.toString(row));
        }
        
        // 3D array
        int[][][] cube = new int[2][3][4];
        cube[0][0][0] = 1;
        cube[1][2][3] = 24;
        
        System.out.println("3D array size: " + cube.length + "x" + 
                          cube[0].length + "x" + cube[0][0].length);
    }
}
```

### Strings

#### String Basics
```java
public class StringBasics {
    public static void main(String[] args) {
        // String creation
        String str1 = "Hello";
        String str2 = new String("World");
        String str3 = "Hello";  // String literal reuse
        
        // String comparison
        System.out.println("str1 == str3: " + (str1 == str3));  // true (same literal)
        System.out.println("str1 == str2: " + (str1 == str2));  // false (different objects)
        System.out.println("str1.equals(str3): " + str1.equals(str3));  // true
        System.out.println("str1.equals(str2): " + str1.equals(str2));  // false
        
        // String concatenation
        String greeting = str1 + ", " + str2 + "!";
        System.out.println("Greeting: " + greeting);
        
        // String methods
        String text = "Java Programming Language";
        System.out.println("Length: " + text.length());
        System.out.println("Character at 5: " + text.charAt(5));
        System.out.println("Substring: " + text.substring(5, 16));
        System.out.println("Uppercase: " + text.toUpperCase());
        System.out.println("Lowercase: " + text.toLowerCase());
        System.out.println("Contains 'Java': " + text.contains("Java"));
        System.out.println("Starts with 'Java': " + text.startsWith("Java"));
        System.out.println("Ends with 'Language': " + text.endsWith("Language"));
        System.out.println("Index of 'Program': " + text.indexOf("Program"));
        System.out.println("Replace 'Java' with 'Python': " + text.replace("Java", "Python"));
        
        // String trimming
        String spaced = "   Hello World   ";
        System.out.println("Original: '" + spaced + "'");
        System.out.println("Trimmed: '" + spaced.trim() + "'");
        
        // String splitting
        String sentence = "Java,is,awesome";
        String[] words = sentence.split(",");
        System.out.println("Split result: " + Arrays.toString(words));
        
        // String formatting
        String name = "Alice";
        int age = 25;
        double score = 95.5;
        
        String formatted = String.format("Name: %s, Age: %d, Score: %.2f", name, age, score);
        System.out.println(formatted);
        
        // StringBuilder for efficient string manipulation
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 1000; i++) {
            sb.append(i).append(" ");
        }
        String result = sb.toString();
        System.out.println("StringBuilder result length: " + result.length());
    }
}
```

## Java Collections Framework

### List Interface

#### ArrayList
```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class ArrayListExample {
    public static void main(String[] args) {
        // Create ArrayList
        List<String> names = new ArrayList<>();
        
        // Add elements
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");
        names.add("David");
        
        // Add at specific position
        names.add(1, "Eve");  // Insert at index 1
        
        System.out.println("Names: " + names);
        System.out.println("Size: " + names.size());
        
        // Access elements
        System.out.println("Element at index 2: " + names.get(2));
        System.out.println("First element: " + names.get(0));
        System.out.println("Last element: " + names.get(names.size() - 1));
        
        // Check existence
        System.out.println("Contains 'Alice': " + names.contains("Alice"));
        System.out.println("Index of 'Charlie': " + names.indexOf("Charlie"));
        
        // Remove elements
        names.remove("Bob");  // Remove by value
        names.remove(0);      // Remove by index
        
        System.out.println("After removals: " + names);
        
        // Iterate over ArrayList
        System.out.println("Using iterator:");
        Iterator<String> iterator = names.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
        
        System.out.println("Using enhanced for loop:");
        for (String name : names) {
            System.out.println(name);
        }
        
        System.out.println("Using forEach (Java 8+):");
        names.forEach(name -> System.out.println(name));
        
        // Sorting
        Collections.sort(names);
        System.out.println("Sorted: " + names);
        
        // Custom sorting
        List<Person> people = new ArrayList<>();
        people.add(new Person("Alice", 25));
        people.add(new Person("Bob", 30));
        people.add(new Person("Charlie", 20));
        
        // Sort by age
        people.sort(Comparator.comparingInt(Person::getAge));
        System.out.println("People sorted by age: " + people);
        
        // Sort by name
        people.sort(Comparator.comparing(Person::getName));
        System.out.println("People sorted by name: " + people);
        
        // ArrayList with primitive types (using wrapper classes)
        List<Integer> numbers = new ArrayList<>();
        numbers.add(10);
        numbers.add(20);
        numbers.add(30);
        
        // Sum all numbers
        int sum = numbers.stream().mapToInt(Integer::intValue).sum();
        System.out.println("Sum: " + sum);
        
        // Filter and collect
        List<Integer> evenNumbers = numbers.stream()
            .filter(n -> n % 2 == 0)
            .collect(Collectors.toList());
        System.out.println("Even numbers: " + evenNumbers);
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
    
    @Override
    public String toString() {
        return name + "(" + age + ")";
    }
}
```

#### LinkedList
```java
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class LinkedListExample {
    public static void main(String[] args) {
        // LinkedList as List
        List<String> list = new LinkedList<>();
        list.add("First");
        list.add("Second");
        list.add("Third");
        
        // LinkedList specific operations
        LinkedList<String> linkedList = new LinkedList<>(list);
        
        // Add at beginning and end
        linkedList.addFirst("Zero");
        linkedList.addLast("Fourth");
        
        System.out.println("LinkedList: " + linkedList);
        
        // Access first and last elements
        System.out.println("First element: " + linkedList.getFirst());
        System.out.println("Last element: " + linkedList.getLast());
        
        // Remove first and last
        linkedList.removeFirst();
        linkedList.removeLast();
        
        System.out.println("After removing first and last: " + linkedList);
        
        // LinkedList as Queue
        Queue<String> queue = new LinkedList<>();
        queue.offer("Task 1");
        queue.offer("Task 2");
        queue.offer("Task 3");
        
        System.out.println("Queue operations:");
        while (!queue.isEmpty()) {
            System.out.println("Processing: " + queue.poll());
        }
        
        // LinkedList as Stack
        LinkedList<Integer> stack = new LinkedList<>();
        stack.push(10);
        stack.push(20);
        stack.push(30);
        
        System.out.println("Stack operations:");
        while (!stack.isEmpty()) {
            System.out.println("Popping: " + stack.pop());
        }
        
        // Performance comparison
        performanceComparison();
    }
    
    private static void performanceComparison() {
        final int SIZE = 100000;
        
        // ArrayList performance
        List<Integer> arrayList = new ArrayList<>();
        long startTime = System.nanoTime();
        for (int i = 0; i < SIZE; i++) {
            arrayList.add(i);
        }
        long arrayListTime = System.nanoTime() - startTime;
        
        // LinkedList performance
        List<Integer> linkedList = new LinkedList<>();
        startTime = System.nanoTime();
        for (int i = 0; i < SIZE; i++) {
            linkedList.add(i);
        }
        long linkedListTime = System.nanoTime() - startTime;
        
        System.out.println("ArrayList add time: " + arrayListTime + " ns");
        System.out.println("LinkedList add time: " + linkedListTime + " ns");
        System.out.println("Ratio: " + (double)linkedListTime / arrayListTime);
    }
}
```

### Set Interface

#### HashSet
```java
import java.util.HashSet;
import java.util.Set;

public class HashSetExample {
    public static void main(String[] args) {
        // Create HashSet
        Set<String> uniqueNames = new HashSet<>();
        
        // Add elements (duplicates are ignored)
        uniqueNames.add("Alice");
        uniqueNames.add("Bob");
        uniqueNames.add("Alice");  // Duplicate, will be ignored
        uniqueNames.add("Charlie");
        uniqueNames.add("Bob");    // Duplicate, will be ignored
        
        System.out.println("Unique names: " + uniqueNames);
        System.out.println("Size: " + uniqueNames.size());
        
        // Check existence
        System.out.println("Contains 'Alice': " + uniqueNames.contains("Alice"));
        System.out.println("Contains 'David': " + uniqueNames.contains("David"));
        
        // Remove elements
        uniqueNames.remove("Bob");
        System.out.println("After removing 'Bob': " + uniqueNames);
        
        // Iterate over HashSet
        System.out.println("Iterating over HashSet:");
        for (String name : uniqueNames) {
            System.out.println(name);
        }
        
        // HashSet with custom objects
        Set<Person> people = new HashSet<>();
        people.add(new Person("Alice", 25));
        people.add(new Person("Bob", 30));
        people.add(new Person("Alice", 25));  // Duplicate if equals/hashCode implemented
        
        System.out.println("People set: " + people);
        
        // Set operations
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        
        set1.add(1);
        set1.add(2);
        set1.add(3);
        set1.add(4);
        
        set2.add(3);
        set2.add(4);
        set2.add(5);
        set2.add(6);
        
        // Union
        Set<Integer> union = new HashSet<>(set1);
        union.addAll(set2);
        System.out.println("Union: " + union);
        
        // Intersection
        Set<Integer> intersection = new HashSet<>(set1);
        intersection.retainAll(set2);
        System.out.println("Intersection: " + intersection);
        
        // Difference
        Set<Integer> difference = new HashSet<>(set1);
        difference.removeAll(set2);
        System.out.println("Difference (set1 - set2): " + difference);
        
        // Symmetric difference
        Set<Integer> symmetricDiff = new HashSet<>(union);
        symmetricDiff.removeAll(intersection);
        System.out.println("Symmetric difference: " + symmetricDiff);
    }
}
```

#### TreeSet
```java
import java.util.TreeSet;
import java.util.Set;
import java.util.NavigableSet;

public class TreeSetExample {
    public static void main(String[] args) {
        // Create TreeSet (sorted order)
        Set<Integer> numbers = new TreeSet<>();
        numbers.add(5);
        numbers.add(2);
        numbers.add(8);
        numbers.add(1);
        numbers.add(9);
        numbers.add(3);
        
        System.out.println("TreeSet (sorted): " + numbers);
        
        // TreeSet specific operations
        TreeSet<Integer> treeSet = new TreeSet<>(numbers);
        
        System.out.println("First element: " + treeSet.first());
        System.out.println("Last element: " + treeSet.last());
        
        // Navigation methods
        System.out.println("Lower than 5: " + treeSet.lower(5));
        System.out.println("Floor of 5: " + treeSet.floor(5));
        System.out.println("Ceiling of 5: " + treeSet.ceiling(5));
        System.out.println("Higher than 5: " + treeSet.higher(5));
        
        // Subset operations
        System.out.println("HeadSet (less than 5): " + treeSet.headSet(5));
        System.out.println("TailSet (greater than or equal to 5): " + treeSet.tailSet(5));
        System.out.println("SubSet [2, 8]: " + treeSet.subSet(2, 8));
        
        // Poll operations
        System.out.println("Poll first: " + treeSet.pollFirst());
        System.out.println("Poll last: " + treeSet.pollLast());
        System.out.println("After polling: " + treeSet);
        
        // TreeSet with custom comparator
        TreeSet<String> reverseOrder = new TreeSet<>(Collections.reverseOrder());
        reverseOrder.add("Apple");
        reverseOrder.add("Banana");
        reverseOrder.add("Cherry");
        reverseOrder.add("Date");
        
        System.out.println("Reverse order: " + reverseOrder);
        
        // TreeSet with custom objects
        TreeSet<Person> people = new TreeSet<>(Comparator.comparing(Person::getName));
        people.add(new Person("Charlie", 25));
        people.add(new Person("Alice", 30));
        people.add(new Person("Bob", 20));
        
        System.out.println("People sorted by name: " + people);
    }
}
```

### Map Interface

#### HashMap
```java
import java.util.HashMap;
import java.util.Map;

public class HashMapExample {
    public static void main(String[] args) {
        // Create HashMap
        Map<String, Integer> scores = new HashMap<>();
        
        // Put key-value pairs
        scores.put("Alice", 95);
        scores.put("Bob", 87);
        scores.put("Charlie", 92);
        scores.put("David", 78);
        
        System.out.println("Scores: " + scores);
        System.out.println("Size: " + scores.size());
        
        // Access values
        System.out.println("Alice's score: " + scores.get("Alice"));
        System.out.println("Eve's score: " + scores.get("Eve"));  // null
        
        // Get with default value
        System.out.println("Eve's score (with default): " + scores.getOrDefault("Eve", 0));
        
        // Check if key exists
        System.out.println("Contains key 'Alice': " + scores.containsKey("Alice"));
        System.out.println("Contains key 'Eve': " + scores.containsKey("Eve"));
        
        // Check if value exists
        System.out.println("Contains value 95: " + scores.containsValue(95));
        
        // Replace values
        scores.replace("Bob", 88);
        System.out.println("After replacing Bob's score: " + scores);
        
        // Put if absent
        scores.putIfAbsent("Eve", 85);
        System.out.println("After putIfAbsent Eve: " + scores);
        
        // Remove entries
        scores.remove("David");
        System.out.println("After removing David: " + scores);
        
        // Iterate over HashMap
        System.out.println("Iterating over entries:");
        for (Map.Entry<String, Integer> entry : scores.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        
        System.out.println("Iterating over keys:");
        for (String key : scores.keySet()) {
            System.out.println(key + ": " + scores.get(key));
        }
        
        System.out.println("Iterating over values:");
        for (Integer value : scores.values()) {
            System.out.println(value);
        }
        
        // Java 8+ forEach
        System.out.println("Using forEach:");
        scores.forEach((name, score) -> System.out.println(name + " scored " + score));
        
        // Compute operations
        scores.compute("Alice", (name, score) -> score + 5);
        System.out.println("After compute (Alice +5): " + scores);
        
        scores.computeIfAbsent("Frank", name -> 80);
        System.out.println("After computeIfAbsent Frank: " + scores);
        
        scores.computeIfPresent("Bob", (name, score) -> score + 2);
        System.out.println("After computeIfPresent (Bob +2): " + scores);
        
        // Merge operation
        scores.merge("Alice", 5, (oldValue, newValue) -> oldValue + newValue);
        System.out.println("After merge (Alice +5): " + scores);
        
        // HashMap with custom objects as keys
        Map<Person, String> personCities = new HashMap<>();
        personCities.put(new Person("Alice", 25), "New York");
        personCities.put(new Person("Bob", 30), "Los Angeles");
        
        System.out.println("Person cities: " + personCities);
    }
}
```

#### TreeMap
```java
import java.util.TreeMap;
import java.util.Map;

public class TreeMapExample {
    public static void main(String[] args) {
        // Create TreeMap (sorted by keys)
        Map<String, Integer> sortedScores = new TreeMap<>();
        
        sortedScores.put("Charlie", 92);
        sortedScores.put("Alice", 95);
        sortedScores.put("Bob", 87);
        sortedScores.put("David", 78);
        
        System.out.println("TreeMap (sorted by key): " + sortedScores);
        
        // TreeMap specific operations
        TreeMap<String, Integer> treeMap = new TreeMap<>(sortedScores);
        
        System.out.println("First key: " + treeMap.firstKey());
        System.out.println("Last key: " + treeMap.lastKey());
        
        // Navigation methods
        System.out.println("Key before 'Bob': " + treeMap.lowerKey("Bob"));
        System.out.println("Key at or before 'Bob': " + treeMap.floorKey("Bob"));
        System.out.println("Key at or after 'Bob': " + treeMap.ceilingKey("Bob"));
        System.out.println("Key after 'Bob': " + treeMap.higherKey("Bob"));
        
        // SubMap operations
        System.out.println("HeadMap (before 'Bob'): " + treeMap.headMap("Bob"));
        System.out.println("TailMap (from 'Bob'): " + treeMap.tailMap("Bob"));
        System.out.println("SubMap ['Alice', 'Charlie'): " + treeMap.subMap("Alice", "Charlie"));
        
        // Poll operations
        System.out.println("Poll first entry: " + treeMap.pollFirstEntry());
        System.out.println("Poll last entry: " + treeMap.pollLastEntry());
        System.out.println("After polling: " + treeMap);
        
        // TreeMap with custom comparator
        TreeMap<String, Integer> reverseOrder = new TreeMap<>(Collections.reverseOrder());
        reverseOrder.putAll(sortedScores);
        
        System.out.println("Reverse order TreeMap: " + reverseOrder);
        
        // TreeMap with numeric keys
        TreeMap<Integer, String> numberNames = new TreeMap<>();
        numberNames.put(3, "Three");
        numberNames.put(1, "One");
        numberNames.put(4, "Four");
        numberNames.put(2, "Two");
        numberNames.put(5, "Five");
        
        System.out.println("Number names: " + numberNames);
        
        // Range operations
        System.out.println("Numbers 2-4: " + numberNames.subMap(2, true, 4, true));
    }
}
```

### Queue Interface

#### PriorityQueue
```java
import java.util.PriorityQueue;
import java.util.Queue;

public class PriorityQueueExample {
    public static void main(String[] args) {
        // Natural ordering (min-heap)
        Queue<Integer> minHeap = new PriorityQueue<>();
        minHeap.offer(5);
        minHeap.offer(2);
        minHeap.offer(8);
        minHeap.offer(1);
        minHeap.offer(9);
        
        System.out.println("PriorityQueue (min-heap): " + minHeap);
        
        System.out.println("Peek (smallest): " + minHeap.peek());
        System.out.println("Poll (remove smallest): " + minHeap.poll());
        System.out.println("After poll: " + minHeap);
        
        System.out.println("Removing elements in priority order:");
        while (!minHeap.isEmpty()) {
            System.out.println(minHeap.poll());
        }
        
        // Max-heap using custom comparator
        Queue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        maxHeap.offer(5);
        maxHeap.offer(2);
        maxHeap.offer(8);
        maxHeap.offer(1);
        maxHeap.offer(9);
        
        System.out.println("PriorityQueue (max-heap): " + maxHeap);
        System.out.println("Peek (largest): " + maxHeap.peek());
        
        // PriorityQueue with custom objects
        Queue<Task> taskQueue = new PriorityQueue<>(Comparator.comparingInt(Task::getPriority));
        taskQueue.offer(new Task("Low priority", 3));
        taskQueue.offer(new Task("High priority", 1));
        taskQueue.offer(new Task("Medium priority", 2));
        
        System.out.println("Task queue:");
        while (!taskQueue.isEmpty()) {
            System.out.println(taskQueue.poll());
        }
    }
}

class Task implements Comparable<Task> {
    private String description;
    private int priority;
    
    public Task(String description, int priority) {
        this.description = description;
        this.priority = priority;
    }
    
    public int getPriority() { return priority; }
    public String getDescription() { return description; }
    
    @Override
    public int compareTo(Task other) {
        return Integer.compare(this.priority, other.priority);
    }
    
    @Override
    public String toString() {
        return description + " (priority: " + priority + ")";
    }
}
```

## Advanced Data Structures

### Enum Types
```java
public enum Day {
    MONDAY("Monday", 1),
    TUESDAY("Tuesday", 2),
    WEDNESDAY("Wednesday", 3),
    THURSDAY("Thursday", 4),
    FRIDAY("Friday", 5),
    SATURDAY("Saturday", 6),
    SUNDAY("Sunday", 7);
    
    private final String displayName;
    private final int dayNumber;
    
    Day(String displayName, int dayNumber) {
        this.displayName = displayName;
        this.dayNumber = dayNumber;
    }
    
    public String getDisplayName() { return displayName; }
    public int getDayNumber() { return dayNumber; }
    
    public boolean isWeekend() {
        return this == SATURDAY || this == SUNDAY;
    }
    
    public boolean isWeekday() {
        return !isWeekend();
    }
}

public class EnumExample {
    public static void main(String[] args) {
        // Using enum
        Day today = Day.WEDNESDAY;
        
        System.out.println("Today is " + today.getDisplayName());
        System.out.println("Day number: " + today.getDayNumber());
        System.out.println("Is weekend: " + today.isWeekend());
        System.out.println("Is weekday: " + today.isWeekday());
        
        // Iterate over enum values
        System.out.println("All days:");
        for (Day day : Day.values()) {
            System.out.println(day + " (" + day.getDisplayName() + ")");
        }
        
        // Enum in collections
        Set<Day> workingDays = EnumSet.range(Day.MONDAY, Day.FRIDAY);
        System.out.println("Working days: " + workingDays);
        
        Set<Day> weekend = EnumSet.of(Day.SATURDAY, Day.SUNDAY);
        System.out.println("Weekend: " + weekend);
        
        // EnumMap
        EnumMap<Day, String> activities = new EnumMap<>(Day.class);
        activities.put(Day.MONDAY, "Meeting");
        activities.put(Day.TUESDAY, "Development");
        activities.put(Day.WEDNESDAY, "Testing");
        activities.put(Day.THURSDAY, "Documentation");
        activities.put(Day.FRIDAY, "Review");
        
        System.out.println("Weekly activities:");
        for (Map.Entry<Day, String> entry : activities.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
```

### Optional Class (Java 8+)
```java
import java.util.Optional;

public class OptionalExample {
    public static void main(String[] args) {
        // Creating Optional
        Optional<String> optional1 = Optional.of("Hello");
        Optional<String> optional2 = Optional.ofNullable(null);
        Optional<String> optional3 = Optional.empty();
        
        // Check if value is present
        System.out.println("Optional1 has value: " + optional1.isPresent());
        System.out.println("Optional2 has value: " + optional2.isPresent());
        System.out.println("Optional3 has value: " + optional3.isPresent());
        
        // Get value (safe ways)
        optional1.ifPresent(value -> System.out.println("Value: " + value));
        
        // Or provide default
        String value = optional2.orElse("Default value");
        System.out.println("Optional2 with default: " + value);
        
        // Or compute default
        String computedValue = optional3.orElseGet(() -> "Computed default");
        System.out.println("Optional3 with computed default: " + computedValue);
        
        // Or throw exception
        try {
            String value2 = optional3.orElseThrow(() -> new IllegalArgumentException("No value present"));
        } catch (IllegalArgumentException e) {
            System.out.println("Caught exception: " + e.getMessage());
        }
        
        // Transform value
        Optional<Integer> length = optional1.map(String::length);
        System.out.println("Length of 'Hello': " + length.orElse(0));
        
        // Filter value
        Optional<String> filtered = optional1.filter(s -> s.startsWith("H"));
        System.out.println("Filtered: " + filtered.orElse("No match"));
        
        // Chain operations
        String result = Optional.of("  Java  ")
            .map(String::trim)
            .filter(s -> s.length() > 0)
            .map(String::toUpperCase)
            .orElse("EMPTY");
        
        System.out.println("Chained result: " + result);
        
        // Optional in methods
        Optional<String> userName = findUserName(1);
        userName.ifPresent(name -> System.out.println("User found: " + name));
        
        Optional<String> missingUser = findUserName(999);
        System.out.println("Missing user: " + missingUser.orElse("Not found"));
    }
    
    private static Optional<String> findUserName(int userId) {
        // Simulate database lookup
        if (userId == 1) {
            return Optional.of("Alice");
        }
        return Optional.empty();
    }
}
```

## Performance Considerations

### Time Complexity Summary
```java
public class ComplexityAnalysis {
    public static void main(String[] args) {
        System.out.println("=== Time Complexity Summary ===\n");
        
        System.out.println("ArrayList:");
        System.out.println("  Access: O(1)");
        System.out.println("  Add (end): O(1) amortized");
        System.out.println("  Add (middle): O(n)");
        System.out.println("  Remove (end): O(1)");
        System.out.println("  Remove (middle): O(n)");
        System.out.println("  Search: O(n)\n");
        
        System.out.println("LinkedList:");
        System.out.println("  Access: O(n)");
        System.out.println("  Add (end): O(1)");
        System.out.println("  Add (beginning): O(1)");
        System.out.println("  Add (middle): O(n)");
        System.out.println("  Remove (end): O(n)");
        System.out.println("  Remove (beginning): O(1)");
        System.out.println("  Search: O(n)\n");
        
        System.out.println("HashSet:");
        System.out.println("  Add: O(1) average");
        System.out.println("  Remove: O(1) average");
        System.out.println("  Contains: O(1) average");
        System.out.println("  Size: O(1)\n");
        
        System.out.println("TreeSet:");
        System.out.println("  Add: O(log n)");
        System.out.println("  Remove: O(log n)");
        System.out.println("  Contains: O(log n)");
        System.out.println("  First/Last: O(log n)\n");
        
        System.out.println("HashMap:");
        System.out.println("  Put: O(1) average");
        System.out.println("  Get: O(1) average");
        System.out.println("  Remove: O(1) average");
        System.out.println("  ContainsKey: O(1) average\n");
        
        System.out.println("TreeMap:");
        System.out.println("  Put: O(log n)");
        System.out.println("  Get: O(log n)");
        System.out.println("  Remove: O(log n)");
        System.out.println("  ContainsKey: O(log n)");
    }
}
```

### Memory Usage Comparison
```java
import java.util.*;

public class MemoryUsageComparison {
    public static void main(String[] args) {
        final int SIZE = 100000;
        
        // Test ArrayList
        List<Integer> arrayList = new ArrayList<>();
        long before = getUsedMemory();
        for (int i = 0; i < SIZE; i++) {
            arrayList.add(i);
        }
        long after = getUsedMemory();
        System.out.println("ArrayList memory: " + (after - before) + " bytes");
        
        // Test LinkedList
        List<Integer> linkedList = new LinkedList<>();
        before = getUsedMemory();
        for (int i = 0; i < SIZE; i++) {
            linkedList.add(i);
        }
        after = getUsedMemory();
        System.out.println("LinkedList memory: " + (after - before) + " bytes");
        
        // Test HashSet
        Set<Integer> hashSet = new HashSet<>();
        before = getUsedMemory();
        for (int i = 0; i < SIZE; i++) {
            hashSet.add(i);
        }
        after = getUsedMemory();
        System.out.println("HashSet memory: " + (after - before) + " bytes");
        
        // Test TreeSet
        Set<Integer> treeSet = new TreeSet<>();
        before = getUsedMemory();
        for (int i = 0; i < SIZE; i++) {
            treeSet.add(i);
        }
        after = getUsedMemory();
        System.out.println("TreeSet memory: " + (after - before) + " bytes");
    }
    
    private static long getUsedMemory() {
        Runtime runtime = Runtime.getRuntime();
        System.gc();
        return runtime.totalMemory() - runtime.freeMemory();
    }
}
```

## Choosing the Right Data Structure

### Decision Guidelines
```java
public class DataStructureSelection {
    public static void main(String[] args) {
        System.out.println("=== Data Structure Selection Guide ===\n");
        
        System.out.println("Use ArrayList when:");
        System.out.println("- You need random access by index");
        System.out.println("- Elements are stored contiguously");
        System.out.println("- You mostly add/remove from the end");
        System.out.println("- Cache performance is important\n");
        
        System.out.println("Use LinkedList when:");
        System.out.println("- You need frequent insertions/deletions at both ends");
        System.out.println("- Random access is not required");
        System.out.println("- Iterator validity is important\n");
        
        System.out.println("Use HashSet when:");
        System.out.println("- You need unique elements");
        System.out.println("- Order doesn't matter");
        System.out.println("- You need fast O(1) operations\n");
        
        System.out.println("Use TreeSet when:");
        System.out.println("- You need sorted unique elements");
        System.out.println("- You need range queries");
        System.out.println("- Order is important\n");
        
        System.out.println("Use HashMap when:");
        System.out.println("- You need key-value pairs");
        System.out.println("- Order doesn't matter");
        System.out.println("- You need fast O(1) operations\n");
        
        System.out.println("Use TreeMap when:");
        System.out.println("- You need sorted key-value pairs");
        System.out.println("- You need range queries");
        System.out.println("- Order is important\n");
        
        System.out.println("Use PriorityQueue when:");
        System.out.println("- You need elements processed by priority");
        System.out.println("- You need min/max element quickly");
        System.out.println("- Order of processing matters\n");
    }
}
```

## Best Practices

1. **Prefer interfaces over implementations** - code to List, Set, Map interfaces
2. **Choose the right collection** based on your use case and performance requirements
3. **Use generics** for type safety
4. **Initialize collections with appropriate capacity** when size is known
5. **Use enhanced for loops** for cleaner iteration
6. **Consider streams** for functional-style operations (Java 8+)
7. **Use Optional** instead of null for better null safety (Java 8+)
8. **Be aware of thread safety** - use concurrent collections for multi-threading
9. **Override equals() and hashCode()** for custom objects in collections
10. **Use immutable collections** when data shouldn't change (Java 9+)

## Conclusion

Java provides a comprehensive set of data structures through both language features and the Collections Framework. Understanding the characteristics, performance implications, and appropriate use cases for each data structure is essential for writing efficient and maintainable Java code. The Collections Framework offers type-safe, high-performance implementations that can handle most common data structure needs, while modern Java features like streams and Optional provide additional functionality for working with collections.
