# Java Conditional Statements

## Overview

Conditional statements allow programs to make decisions and execute different code paths based on specific conditions. Java provides several conditional constructs that enable branching logic, which is fundamental to algorithm implementation and problem-solving.

## if Statement

### Basic if Statement
```java
public class BasicIfStatement {
    public static void main(String[] args) {
        int age = 18;
        
        // Simple if statement
        if (age >= 18) {
            System.out.println("You are eligible to vote");
        }
        
        // if-else statement
        int score = 85;
        if (score >= 90) {
            System.out.println("Grade: A");
        } else {
            System.out.println("Grade: Not A");
        }
        
        // if-else if-else ladder
        if (score >= 90) {
            System.out.println("Grade: A");
        } else if (score >= 80) {
            System.out.println("Grade: B");
        } else if (score >= 70) {
            System.out.println("Grade: C");
        } else if (score >= 60) {
            System.out.println("Grade: D");
        } else {
            System.out.println("Grade: F");
        }
        
        // Nested if statements
        int temperature = 25;
        boolean isRaining = false;
        
        if (temperature > 20) {
            System.out.println("Warm weather");
            if (isRaining) {
                System.out.println("But it's raining");
            } else {
                System.out.println("Perfect weather for a walk");
            }
        } else {
            System.out.println("Cool weather");
        }
        
        // Multiple conditions in single if
        int number = 42;
        if (number > 0 && number % 2 == 0) {
            System.out.println(number + " is positive and even");
        }
        
        if (number < 0 || number > 100) {
            System.out.println(number + " is out of range");
        }
    }
}
```

### Complex Conditions
```java
public class ComplexConditions {
    public static void main(String[] args) {
        int age = 25;
        boolean hasLicense = true;
        boolean hasCar = false;
        String country = "USA";
        
        // Multiple conditions with AND (&&)
        if (age >= 18 && hasLicense && hasCar) {
            System.out.println("You can drive");
        } else {
            System.out.println("You cannot drive");
        }
        
        // Multiple conditions with OR (||)
        if (age >= 18 || (country.equals("USA") && age >= 16)) {
            System.out.println("You can get a license");
        }
        
        // Combining AND and OR (use parentheses for clarity)
        if ((age >= 18 && hasLicense) || (age >= 16 && hasLicense && country.equals("USA"))) {
            System.out.println("Driving eligible");
        } else {
            System.out.println("Not driving eligible");
        }
        
        // NOT operator (!)
        if (!hasCar) {
            System.out.println("You don't have a car");
        }
        
        // Complex boolean logic
        boolean canDrive = (age >= 18 && hasLicense) || 
                         (age >= 16 && hasLicense && country.equals("USA"));
        
        if (canDrive && hasCar) {
            System.out.println("You can drive your car");
        } else if (canDrive && !hasCar) {
            System.out.println("You can drive but need a car");
        } else {
            System.out.println("You cannot drive");
        }
        
        // Short-circuit evaluation
        String text = null;
        if (text != null && text.length() > 0) {  // text.length() won't be called if text is null
            System.out.println("Text has content");
        } else {
            System.out.println("Text is null or empty");
        }
        
        // Bitwise operators vs logical operators
        int a = 5, b = 3;
        if (a > 0 && b > 0) {
            System.out.println("Both positive (logical AND)");
        }
        
        if ((a > 0) & (b > 0)) {  // Both sides are evaluated
            System.out.println("Both positive (bitwise AND)");
        }
    }
}
```

### Ternary Operator
```java
public class TernaryOperator {
    public static void main(String[] args) {
        int age = 20;
        String status;
        
        // Basic ternary operator
        status = (age >= 18) ? "Adult" : "Minor";
        System.out.println("Status: " + status);
        
        // Nested ternary (avoid for readability)
        int score = 75;
        String grade = (score >= 90) ? "A" : 
                      (score >= 80) ? "B" : 
                      (score >= 70) ? "C" : "F";
        System.out.println("Grade: " + grade);
        
        // Ternary in expressions
        int max = (age > score) ? age : score;
        System.out.println("Maximum: " + max);
        
        // Ternary with method calls
        String message = (age >= 18) ? getAdultMessage() : getMinorMessage();
        System.out.println(message);
        
        // Ternary with assignments
        int x = 10, y = 20;
        int result = (x > y) ? x : y;
        System.out.println("Result: " + result);
        
        // Ternary in return statements
        System.out.println("Absolute value of -5: " + absolute(-5));
        System.out.println("Absolute value of 5: " + absolute(5));
        
        // Complex ternary (not recommended - use if-else instead)
        String complexResult = (age >= 18) ? 
            ((hasLicense()) ? "Can drive" : "Cannot drive") : 
            "Too young to drive";
        System.out.println("Complex result: " + complexResult);
    }
    
    private static String getAdultMessage() {
        return "Welcome, adult!";
    }
    
    private static String getMinorMessage() {
        return "Hello, minor!";
    }
    
    private static int absolute(int value) {
        return (value >= 0) ? value : -value;
    }
    
    private static boolean hasLicense() {
        return true;
    }
}
```

## switch Statement

### Basic switch Statement
```java
public class BasicSwitchStatement {
    public static void main(String[] args) {
        int day = 3;
        
        // Switch with int
        switch (day) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("Sunday");
                break;
            default:
                System.out.println("Invalid day");
                break;
        }
        
        // Switch with char
        char grade = 'B';
        switch (grade) {
            case 'A':
                System.out.println("Excellent");
                break;
            case 'B':
                System.out.println("Good");
                break;
            case 'C':
            case 'D':
                System.out.println("Average");
                break;
            case 'F':
                System.out.println("Poor");
                break;
            default:
                System.out.println("Invalid grade");
        }
        
        // Switch with String (Java 7+)
        String color = "red";
        switch (color) {
            case "red":
                System.out.println("Stop");
                break;
            case "yellow":
                System.out.println("Caution");
                break;
            case "green":
                System.out.println("Go");
                break;
            default:
                System.out.println("Invalid signal");
                break;
        }
        
        // Switch with enum
        Day today = Day.WEDNESDAY;
        switch (today) {
            case MONDAY:
            case TUESDAY:
            case WEDNESDAY:
            case THURSDAY:
            case FRIDAY:
                System.out.println("Weekday");
                break;
            case SATURDAY:
            case SUNDAY:
                System.out.println("Weekend");
                break;
        }
    }
    
    enum Day {
        MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
    }
}
```

### Enhanced switch (Java 14+)
```java
public class EnhancedSwitch {
    public static void main(String[] args) {
        // Traditional switch expression
        int day = 3;
        String dayName;
        
        switch (day) {
            case 1:
                dayName = "Monday";
                break;
            case 2:
                dayName = "Tuesday";
                break;
            case 3:
                dayName = "Wednesday";
                break;
            case 4:
                dayName = "Thursday";
                break;
            case 5:
                dayName = "Friday";
                break;
            case 6:
                dayName = "Saturday";
                break;
            case 7:
                dayName = "Sunday";
                break;
            default:
                dayName = "Invalid day";
                break;
        }
        System.out.println("Traditional: " + dayName);
        
        // Switch expression (Java 14+)
        String dayNameExpr = switch (day) {
            case 1 -> "Monday";
            case 2 -> "Tuesday";
            case 3 -> "Wednesday";
            case 4 -> "Thursday";
            case 5 -> "Friday";
            case 6 -> "Saturday";
            case 7 -> "Sunday";
            default -> "Invalid day";
        };
        System.out.println("Expression: " + dayNameExpr);
        
        // Switch with complex logic
        int score = 85;
        String result = switch (score / 10) {
            case 10, 9 -> "A";
            case 8 -> "B";
            case 7 -> "C";
            case 6 -> "D";
            default -> "F";
        };
        System.out.println("Grade: " + result);
        
        // Switch with yield (Java 14+)
        String message = switch (day) {
            case 1, 2, 3, 4, 5 -> {
                yield "Weekday";
            }
            case 6, 7 -> {
                yield "Weekend";
            }
            default -> {
                yield "Invalid day";
            }
        };
        System.out.println("Message: " + message);
        
        // Switch with pattern matching preview (Java 17+ preview)
        Object obj = "Hello";
        String typeInfo = switch (obj) {
            case String s -> "String: " + s;
            case Integer i -> "Integer: " + i;
            case Double d -> "Double: " + d;
            default -> "Unknown type";
        };
        System.out.println("Type info: " + typeInfo);
    }
}
```

## Modern Java Conditional Features

### Pattern Matching in instanceof (Java 16+)
```java
public class PatternMatching {
    public static void main(String[] args) {
        Object obj1 = "Hello World";
        Object obj2 = 42;
        Object obj3 = 3.14;
        
        // Traditional instanceof
        if (obj1 instanceof String) {
            String str = (String) obj1;
            System.out.println("String length: " + str.length());
        }
        
        // Pattern matching with instanceof (Java 16+)
        if (obj1 instanceof String str) {
            System.out.println("String length: " + str.length());
        }
        
        if (obj2 instanceof Integer num) {
            System.out.println("Integer value: " + num);
        }
        
        if (obj3 instanceof Double d) {
            System.out.println("Double value: " + d);
        }
        
        // Pattern matching with additional conditions
        Object obj4 = "Java";
        if (obj4 instanceof String s && s.length() > 3) {
            System.out.println("Long string: " + s);
        }
        
        // Pattern matching in else-if chain
        Object obj5 = 100;
        if (obj5 instanceof String s) {
            System.out.println("Processing string: " + s);
        } else if (obj5 instanceof Integer i) {
            System.out.println("Processing integer: " + i);
        } else if (obj5 instanceof Double d) {
            System.out.println("Processing double: " + d);
        } else {
            System.out.println("Unknown type");
        }
        
        // Demonstrate with custom objects
        Object person = new Person("Alice", 25);
        if (person instanceof Person p) {
            System.out.println("Person: " + p.getName() + ", " + p.getAge());
        }
    }
    
    static class Person {
        private String name;
        private int age;
        
        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
        
        public String getName() { return name; }
        public int getAge() { return age; }
    }
}
```

### Switch Expressions with Pattern Matching (Java 17+ Preview)
```java
public class SwitchPatternMatching {
    public static void main(String[] args) {
        // Switch with type patterns
        Object obj = "Hello";
        
        String result = switch (obj) {
            case String s -> "String: " + s;
            case Integer i -> "Integer: " + i;
            case Double d -> "Double: " + d;
            case null -> "Null value";
            default -> "Unknown type";
        };
        
        System.out.println("Result: " + result);
        
        // Switch with guarded patterns
        Object num = 42;
        String typeInfo = switch (num) {
            case Integer i && i > 0 -> "Positive integer: " + i;
            case Integer i && i < 0 -> "Negative integer: " + i;
            case Integer i -> "Zero: " + i;
            case Double d && d > 0 -> "Positive double: " + d;
            case Double d && d < 0 -> "Negative double: " + d;
            case Double d -> "Zero double: " + d;
            default -> "Not a number";
        };
        
        System.out.println("Type info: " + typeInfo);
        
        // Switch with nested patterns
        Object container = new Container("Hello");
        String containerInfo = switch (container) {
            case Container(String s) -> "Container with string: " + s;
            case Container(Integer i) -> "Container with integer: " + i;
            case Container c -> "Container with: " + c.getContent();
            default -> "Not a container";
        };
        
        System.out.println("Container info: " + containerInfo);
    }
    
    static class Container {
        private Object content;
        
        public Container(Object content) {
            this.content = content;
        }
        
        public Object getContent() { return content; }
    }
}
```

## Conditional Expressions with Data Structures

### Collection Operations
```java
import java.util.*;

public class CollectionConditionals {
    public static void main(String[] args) {
        // List operations
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        
        // Conditional processing
        List<Integer> evens = new ArrayList<>();
        List<Integer> odds = new ArrayList<>();
        
        for (int num : numbers) {
            if (num % 2 == 0) {
                evens.add(num);
            } else {
                odds.add(num);
            }
        }
        
        System.out.println("Even numbers: " + evens);
        System.out.println("Odd numbers: " + odds);
        
        // Conditional filtering with streams
        List<Integer> filtered = numbers.stream()
            .filter(n -> n > 5)
            .collect(Collectors.toList());
        
        System.out.println("Numbers > 5: " + filtered);
        
        // Multiple conditions
        List<Integer> specialNumbers = numbers.stream()
            .filter(n -> n % 2 == 0 && n % 3 == 0)
            .collect(Collectors.toList());
        
        System.out.println("Numbers divisible by 2 and 3: " + specialNumbers);
        
        // Map operations
        Map<String, Integer> scores = new HashMap<>();
        scores.put("Alice", 95);
        scores.put("Bob", 87);
        scores.put("Charlie", 92);
        scores.put("David", 78);
        
        // Conditional processing of map
        Map<String, String> grades = new HashMap<>();
        for (Map.Entry<String, Integer> entry : scores.entrySet()) {
            String name = entry.getKey();
            int score = entry.getValue();
            
            if (score >= 90) {
                grades.put(name, "A");
            } else if (score >= 80) {
                grades.put(name, "B");
            } else if (score >= 70) {
                grades.put(name, "C");
            } else {
                grades.put(name, "F");
            }
        }
        
        System.out.println("Grades: " + grades);
        
        // Set operations
        Set<Integer> uniqueNumbers = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 3, 2, 1));
        Set<Integer> processedNumbers = new HashSet<>();
        
        for (int num : uniqueNumbers) {
            if (num % 2 == 0) {
                processedNumbers.add(num * 2);
            } else {
                processedNumbers.add(num * 3);
            }
        }
        
        System.out.println("Processed numbers: " + processedNumbers);
        
        // Conditional sorting
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Eve");
        boolean ascending = false;
        
        if (ascending) {
            Collections.sort(names);
        } else {
            names.sort(Collections.reverseOrder());
        }
        
        System.out.println("Sorted " + (ascending ? "ascending" : "descending") + ": " + names);
    }
}
```

### Optional-based Conditionals (Java 8+)
```java
import java.util.*;

public class OptionalConditionals {
    public static void main(String[] args) {
        // Optional with conditional processing
        Optional<String> optionalName = Optional.of("Alice");
        Optional<String> emptyOptional = Optional.empty();
        
        // ifPresent
        optionalName.ifPresent(name -> System.out.println("Name: " + name));
        
        // ifPresentOrElse (Java 9+)
        optionalName.ifPresentOrElse(
            name -> System.out.println("Found: " + name),
            () -> System.out.println("Not found")
        );
        
        emptyOptional.ifPresentOrElse(
            name -> System.out.println("Found: " + name),
            () -> System.out.println("Not found")
        );
        
        // filter with Optional
        Optional<String> filtered = optionalName.filter(name -> name.startsWith("A"));
        System.out.println("Filtered: " + filtered.orElse("No match"));
        
        // map with conditional logic
        Optional<Integer> length = optionalName.map(String::length);
        System.out.println("Length: " + length.orElse(0));
        
        // Complex conditional chain
        String result = optionalName
            .filter(name -> name.length() > 3)
            .map(String::toUpperCase)
            .orElse("Default");
        
        System.out.println("Result: " + result);
        
        // Optional in method with conditional return
        Optional<String> userName = findUserName(1);
        String message = userName
            .map(name -> "Welcome, " + name + "!")
            .orElse("Welcome, guest!");
        
        System.out.println(message);
        
        // Optional with nested conditionals
        Optional<User> user = findUser(1);
        String userInfo = user
            .filter(u -> u.isActive())
            .map(User::getName)
            .filter(name -> !name.isEmpty())
            .map(String::toUpperCase)
            .orElse("UNKNOWN USER");
        
        System.out.println("User info: " + userInfo);
    }
    
    private static Optional<String> findUserName(int userId) {
        // Simulate database lookup
        if (userId == 1) {
            return Optional.of("Alice");
        }
        return Optional.empty();
    }
    
    private static Optional<User> findUser(int userId) {
        // Simulate database lookup
        if (userId == 1) {
            return Optional.of(new User("Alice", true));
        }
        return Optional.empty();
    }
    
    static class User {
        private String name;
        private boolean active;
        
        public User(String name, boolean active) {
            this.name = name;
            this.active = active;
        }
        
        public String getName() { return name; }
        public boolean isActive() { return active; }
    }
}
```

## Advanced Conditional Patterns

### Strategy Pattern with Conditionals
```java
import java.util.*;
import java.util.function.*;

public class StrategyPattern {
    public static void main(String[] args) {
        // Function-based strategy
        Map<String, BinaryOperator<Integer>> operations = new HashMap<>();
        operations.put("+", (a, b) -> a + b);
        operations.put("-", (a, b) -> a - b);
        operations.put("*", (a, b) -> a * b);
        operations.put("/", (a, b) -> b != 0 ? a / b : 0);
        
        int a = 10, b = 5;
        String op = "+";
        
        int result = operations.containsKey(op) ? 
            operations.get(op).apply(a, b) : 0;
        
        System.out.println(a + " " + op + " " + b + " = " + result);
        
        // Predicate-based filtering
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        
        Map<String, Predicate<Integer>> filters = new HashMap<>();
        filters.put("even", n -> n % 2 == 0);
        filters.put("odd", n -> n % 2 != 0);
        filters.put("prime", StrategyPattern::isPrime);
        filters.put("greaterThan5", n -> n > 5);
        
        String filterType = "prime";
        List<Integer> filtered = numbers.stream()
            .filter(filters.getOrDefault(filterType, n -> true))
            .collect(Collectors.toList());
        
        System.out.println(filterType + " numbers: " + filtered);
        
        // Consumer-based actions
        Map<String, Consumer<String>> actions = new HashMap<>();
        actions.put("uppercase", String::toUpperCase);
        actions.put("lowercase", String::toLowerCase);
        actions.put("reverse", StrategyPattern::reverse);
        
        String text = "Hello World";
        String actionType = "uppercase";
        
        Consumer<String> action = actions.getOrDefault(actionType, s -> s);
        action.accept(text);  // This doesn't return anything, just processes
        
        // For demonstration, let's show the result
        String processed = switch (actionType) {
            case "uppercase" -> text.toUpperCase();
            case "lowercase" -> text.toLowerCase();
            case "reverse" -> reverse(text);
            default -> text;
        };
        
        System.out.println("Processed text: " + processed);
    }
    
    private static boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }
    
    private static String reverse(String s) {
        return new StringBuilder(s).reverse().toString();
    }
}
```

### State Machine with Conditionals
```java
import java.util.*;

public class StateMachine {
    public enum State {
        IDLE, STARTED, RUNNING, PAUSED, STOPPED
    }
    
    public enum Event {
        START, STOP, PAUSE, RESUME, RUN
    }
    
    private State currentState = State.IDLE;
    
    public void processEvent(Event event) {
        switch (currentState) {
            case IDLE:
                if (event == Event.START) {
                    currentState = State.STARTED;
                    System.out.println("Machine started");
                } else {
                    System.out.println("Invalid event in IDLE state");
                }
                break;
                
            case STARTED:
                if (event == Event.RUN) {
                    currentState = State.RUNNING;
                    System.out.println("Machine running");
                } else if (event == Event.STOP) {
                    currentState = State.STOPPED;
                    System.out.println("Machine stopped");
                } else {
                    System.out.println("Invalid event in STARTED state");
                }
                break;
                
            case RUNNING:
                if (event == Event.PAUSE) {
                    currentState = State.PAUSED;
                    System.out.println("Machine paused");
                } else if (event == Event.STOP) {
                    currentState = State.STOPPED;
                    System.out.println("Machine stopped");
                } else {
                    System.out.println("Invalid event in RUNNING state");
                }
                break;
                
            case PAUSED:
                if (event == Event.RESUME) {
                    currentState = State.RUNNING;
                    System.out.println("Machine resumed");
                } else if (event == Event.STOP) {
                    currentState = State.STOPPED;
                    System.out.println("Machine stopped");
                } else {
                    System.out.println("Invalid event in PAUSED state");
                }
                break;
                
            case STOPPED:
                if (event == Event.START) {
                    currentState = State.STARTED;
                    System.out.println("Machine restarted");
                } else {
                    System.out.println("Invalid event in STOPPED state");
                }
                break;
        }
    }
    
    public State getCurrentState() {
        return currentState;
    }
    
    public static void main(String[] args) {
        StateMachine machine = new StateMachine();
        
        // Test state transitions
        Event[] events = {
            Event.START, Event.RUN, Event.PAUSE, 
            Event.RESUME, Event.STOP, Event.START
        };
        
        for (Event event : events) {
            System.out.println("Current state: " + machine.getCurrentState());
            System.out.println("Processing event: " + event);
            machine.processEvent(event);
            System.out.println();
        }
        
        // Test invalid transitions
        System.out.println("Testing invalid transitions:");
        machine.processEvent(Event.PAUSE);  // Invalid in STOPPED state
    }
}
```

## Performance Considerations

### Branch Prediction
```java
import java.util.*;

public class BranchPrediction {
    public static void main(String[] args) {
        // Sorted data (predictable branches)
        List<Integer> sortedData = new ArrayList<>();
        for (int i = 0; i < 100000; i++) {
            sortedData.add(i);
        }
        
        // Random data (unpredictable branches)
        List<Integer> randomData = new ArrayList<>(sortedData);
        Collections.shuffle(randomData);
        
        // Test with sorted data
        long startTime = System.nanoTime();
        long sum1 = conditionalSum(sortedData);
        long duration1 = System.nanoTime() - startTime;
        
        // Test with random data
        startTime = System.nanoTime();
        long sum2 = conditionalSum(randomData);
        long duration2 = System.nanoTime() - startTime;
        
        // Test branchless version
        startTime = System.nanoTime();
        long sum3 = branchlessSum(randomData);
        long duration3 = System.nanoTime() - startTime;
        
        System.out.println("Conditional sum (sorted): " + duration1 + " ns");
        System.out.println("Conditional sum (random): " + duration2 + " ns");
        System.out.println("Branchless sum (random): " + duration3 + " ns");
        
        System.out.println("Results equal: " + (sum2 == sum3));
        System.out.println("Branch prediction impact: " + (double)duration2 / duration1);
    }
    
    private static long conditionalSum(List<Integer> data) {
        long sum = 0;
        for (int num : data) {
            if (num < 50000) {  // Branch condition
                sum += num;
            }
        }
        return sum;
    }
    
    private static long branchlessSum(List<Integer> data) {
        long sum = 0;
        for (int num : data) {
            sum += (num < 50000) ? num : 0;  // Branchless using ternary
        }
        return sum;
    }
}
```

### Switch vs if-else Performance
```java
public class SwitchVsIfPerformance {
    public static void main(String[] args) {
        final int ITERATIONS = 1000000;
        int[] testValues = new int[ITERATIONS];
        
        // Generate test values
        Random random = new Random();
        for (int i = 0; i < ITERATIONS; i++) {
            testValues[i] = random.nextInt(10);
        }
        
        // Test switch statement
        long startTime = System.nanoTime();
        for (int value : testValues) {
            switchResult(value);
        }
        long switchTime = System.nanoTime() - startTime;
        
        // Test if-else chain
        startTime = System.nanoTime();
        for (int value : testValues) {
            ifElseResult(value);
        }
        long ifElseTime = System.nanoTime() - startTime;
        
        // Test array lookup
        String[] lookupTable = {"Zero", "One", "Two", "Three", "Four", 
                               "Five", "Six", "Seven", "Eight", "Nine"};
        startTime = System.nanoTime();
        for (int value : testValues) {
            if (value >= 0 && value < lookupTable.length) {
                String result = lookupTable[value];
            }
        }
        long lookupTime = System.nanoTime() - startTime;
        
        System.out.println("Switch time: " + switchTime + " ns");
        System.out.println("If-else time: " + ifElseTime + " ns");
        System.out.println("Lookup time: " + lookupTime + " ns");
        System.out.println("Switch vs If-else ratio: " + (double)ifElseTime / switchTime);
        System.out.println("Lookup vs Switch ratio: " + (double)lookupTime / switchTime);
    }
    
    private static String switchResult(int value) {
        switch (value) {
            case 0: return "Zero";
            case 1: return "One";
            case 2: return "Two";
            case 3: return "Three";
            case 4: return "Four";
            case 5: return "Five";
            case 6: return "Six";
            case 7: return "Seven";
            case 8: return "Eight";
            case 9: return "Nine";
            default: return "Unknown";
        }
    }
    
    private static String ifElseResult(int value) {
        if (value == 0) return "Zero";
        else if (value == 1) return "One";
        else if (value == 2) return "Two";
        else if (value == 3) return "Three";
        else if (value == 4) return "Four";
        else if (value == 5) return "Five";
        else if (value == 6) return "Six";
        else if (value == 7) return "Seven";
        else if (value == 8) return "Eight";
        else if (value == 9) return "Nine";
        else return "Unknown";
    }
}
```

## Common Conditional Patterns

### Input Validation
```java
import java.util.*;

public class InputValidation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Age validation
        int age = 0;
        boolean validAge = false;
        
        while (!validAge) {
            System.out.print("Enter your age (0-120): ");
            if (scanner.hasNextInt()) {
                age = scanner.nextInt();
                if (age >= 0 && age <= 120) {
                    validAge = true;
                    
                    // Age-based categorization
                    if (age < 18) {
                        System.out.println("You are a minor");
                    } else if (age < 65) {
                        System.out.println("You are an adult");
                    } else {
                        System.out.println("You are a senior citizen");
                    }
                } else {
                    System.out.println("Age must be between 0 and 120");
                }
            } else {
                System.out.println("Please enter a valid number");
                scanner.next(); // Clear invalid input
            }
        }
        
        // Password validation
        System.out.print("Enter password: ");
        String password = scanner.next();
        
        boolean hasUpper = false, hasLower = false, hasDigit = false, hasSpecial = false;
        boolean lengthValid = password.length() >= 8;
        
        for (char c : password.toCharArray()) {
            if (Character.isUpperCase(c)) hasUpper = true;
            else if (Character.isLowerCase(c)) hasLower = true;
            else if (Character.isDigit(c)) hasDigit = true;
            else if (!Character.isLetterOrDigit(c)) hasSpecial = true;
        }
        
        if (lengthValid && hasUpper && hasLower && hasDigit && hasSpecial) {
            System.out.println("Strong password!");
        } else {
            System.out.println("Weak password. Requirements:");
            if (!lengthValid) System.out.println("- At least 8 characters");
            if (!hasUpper) System.out.println("- At least one uppercase letter");
            if (!hasLower) System.out.println("- At least one lowercase letter");
            if (!hasDigit) System.out.println("- At least one digit");
            if (!hasSpecial) System.out.println("- At least one special character");
        }
        
        // Email validation
        System.out.print("Enter email: ");
        String email = scanner.next();
        
        boolean validEmail = email.contains("@") && 
                           email.contains(".") && 
                           email.indexOf("@") < email.lastIndexOf(".") &&
                           email.indexOf("@") > 0 &&
                           email.lastIndexOf(".") < email.length() - 1;
        
        if (validEmail) {
            System.out.println("Valid email format");
        } else {
            System.out.println("Invalid email format");
        }
        
        scanner.close();
    }
}
```

### Error Handling with Conditionals
```java
import java.io.*;
import java.util.*;

public class ErrorHandling {
    public static void main(String[] args) {
        // File processing with error handling
        String filename = "example.txt";
        
        try {
            File file = new File(filename);
            if (!file.exists()) {
                System.out.println("File does not exist: " + filename);
                return;
            }
            
            if (!file.canRead()) {
                System.out.println("Cannot read file: " + filename);
                return;
            }
            
            BufferedReader reader = new BufferedReader(new FileReader(file));
            String line;
            int lineNumber = 0;
            
            while ((line = reader.readLine()) != null) {
                lineNumber++;
                
                // Validate line content
                if (line.trim().isEmpty()) {
                    System.out.println("Warning: Empty line at line " + lineNumber);
                    continue;
                }
                
                // Check for specific patterns
                if (line.contains("error")) {
                    System.out.println("Found error keyword at line " + lineNumber);
                } else if (line.contains("warning")) {
                    System.out.println("Found warning at line " + lineNumber);
                }
                
                // Process valid line
                if (line.length() > 0) {
                    System.out.println("Processing line " + lineNumber + ": " + 
                                     line.substring(0, Math.min(50, line.length())));
                }
            }
            
            reader.close();
            System.out.println("File processed successfully");
            
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IO error: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Unexpected error: " + e.getMessage());
        }
        
        // Array bounds checking
        int[] array = {1, 2, 3, 4, 5};
        int index = 10;
        
        if (index >= 0 && index < array.length) {
            System.out.println("Element at index " + index + ": " + array[index]);
        } else {
            System.out.println("Index " + index + " is out of bounds");
        }
        
        // Null checking
        String text = null;
        String result = "";
        
        if (text != null && !text.isEmpty()) {
            result = text.toUpperCase();
        } else {
            result = "DEFAULT";
        }
        
        System.out.println("Result: " + result);
        
        // Division by zero prevention
        int numerator = 10;
        int denominator = 0;
        
        if (denominator != 0) {
            System.out.println("Result: " + (numerator / denominator));
        } else {
            System.out.println("Cannot divide by zero");
        }
    }
}
```

## Best Practices

1. **Use clear and simple conditions** that are easy to understand
2. **Prefer if-else** for complex conditions over nested ternary operators
3. **Use switch** when testing multiple values of the same variable
4. **Use enhanced switch expressions** (Java 14+) for cleaner code
5. **Consider pattern matching** (Java 16+) for type checking and casting
6. **Use Optional** instead of null checks for better null safety (Java 8+)
7. **Validate inputs** before processing
8. **Handle edge cases** explicitly
9. **Use meaningful variable names** in conditions
10. **Keep conditionals short** and move complex logic to methods

## Conclusion

Conditional statements are fundamental to programming logic and decision-making in Java. Understanding the various conditional constructs, their performance implications, and modern language features enables writing clear, efficient, and maintainable code. Java continues to enhance conditional programming with features like pattern matching, switch expressions, and improved Optional handling, providing more expressive and type-safe ways to implement branching logic. By following best practices and choosing the right conditional construct for each situation, you can write code that is both readable and performant.
