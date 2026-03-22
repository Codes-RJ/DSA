# Java Variables and Keywords

## Overview

Variables in Java are named storage locations that hold data values of specific types. Keywords are reserved words that have special meaning to the Java compiler and cannot be used as identifiers. Java is a statically-typed language, meaning all variables must be declared with a specific type before use.

## Java Keywords

Java has 50 reserved keywords. These are divided into several categories:

### Primitive Type Keywords
```java
// Numeric types
byte        // 8-bit signed integer (-128 to 127)
short       // 16-bit signed integer (-32,768 to 32,767)
int         // 32-bit signed integer (-2^31 to 2^31-1)
long        // 64-bit signed integer (-2^63 to 2^63-1)
float       // 32-bit floating point (IEEE 754)
double      // 64-bit floating point (IEEE 754)

// Other primitive types
char        // 16-bit Unicode character (0 to 65,535)
boolean     // Boolean value (true or false)
```

### Control Flow Keywords
```java
// Selection statements
if          // Conditional statement
else        // Alternative conditional
switch      // Multi-way branch
case        // Switch case label
default     // Default switch case

// Loop statements
for         // For loop
while       // While loop
do          // Do-while loop

// Jump statements
break       // Exit loop or switch
continue    // Skip to next iteration
return      // Return from method
```

### Class and Object Keywords
```java
// Class-related
class       // Class definition
interface   // Interface definition
extends     // Class inheritance
implements  // Interface implementation
import      // Import package
package     // Package declaration

// Access modifiers
public      // Public access
protected   // Protected access
private     // Private access

// Object-related
new         // Create object instance
this        // Reference to current object
super       // Reference to parent class
instanceof  // Type checking
```

### Method and Variable Modifiers
```java
// Method modifiers
static      // Class method/variable
final       // Constant/non-overridable
abstract    // Abstract method/class
synchronized// Thread synchronization
native      // Native method (JNI)
strictfp    // Strict floating-point

// Variable modifiers
transient   // Not serialized
volatile    // Thread-safe variable
```

### Exception Handling Keywords
```java
try         // Try block
catch       // Exception handler
finally     // Finally block
throw       // Throw exception
throws      // Exception declaration
```

### Other Keywords
```java
void        // No return value
enum        // Enumeration type
assert      // Assertion
```

### Reserved Keywords (not currently used)
```java
const       // Reserved for future use
goto        // Reserved for future use
```

## Variable Declaration and Initialization

### Basic Variable Declaration
```java
public class VariableBasics {
    public static void main(String[] args) {
        // Declaration without initialization
        int age;
        double salary;
        char grade;
        boolean isStudent;
        
        // Declaration with initialization
        int score = 100;
        double pi = 3.14159;
        char initial = 'A';
        boolean isValid = true;
        
        // Multiple variable declaration
        int x = 10, y = 20, z = 30;
        String firstName = "John", lastName = "Doe";
        
        System.out.println("Score: " + score);
        System.out.println("PI: " + pi);
        System.out.println("Initial: " + initial);
        System.out.println("Valid: " + isValid);
    }
}
```

### Variable Types in Detail

#### Primitive Types
```java
public class PrimitiveTypes {
    public static void main(String[] args) {
        // Integer types
        byte smallNumber = 127;        // -128 to 127
        short mediumNumber = 32767;    // -32,768 to 32,767
        int regularNumber = 2147483647; // -2^31 to 2^31-1
        long largeNumber = 9223372036854775807L; // Note the 'L' suffix
        
        // Floating-point types
        float singlePrecision = 3.14f;   // Note the 'f' suffix
        double doublePrecision = 3.141592653589793;
        
        // Character type
        char letter = 'A';
        char unicodeChar = '\u03A9';      // Greek letter Omega
        char digitChar = '5';
        
        // Boolean type
        boolean isTrue = true;
        boolean isFalse = false;
        
        // Display values and ranges
        System.out.println("Byte: " + smallNumber + " (max: " + Byte.MAX_VALUE + ")");
        System.out.println("Short: " + mediumNumber + " (max: " + Short.MAX_VALUE + ")");
        System.out.println("Int: " + regularNumber + " (max: " + Integer.MAX_VALUE + ")");
        System.out.println("Long: " + largeNumber + " (max: " + Long.MAX_VALUE + ")");
        System.out.println("Float: " + singlePrecision + " (max: " + Float.MAX_VALUE + ")");
        System.out.println("Double: " + doublePrecision + " (max: " + Double.MAX_VALUE + ")");
        System.out.println("Char: " + letter + " (Unicode: " + (int)letter + ")");
        System.out.println("Unicode: " + unicodeChar);
        System.out.println("Boolean: " + isTrue);
    }
}
```

#### Reference Types
```java
public class ReferenceTypes {
    public static void main(String[] args) {
        // String (reference type)
        String greeting = "Hello, World!";
        String emptyString = "";
        String nullString = null;
        
        // Arrays (reference types)
        int[] numbers = {1, 2, 3, 4, 5};
        String[] names = new String[3];
        names[0] = "Alice";
        names[1] = "Bob";
        names[2] = "Charlie";
        
        // Custom class instances
        Person person = new Person("John", 25);
        
        // Display information
        System.out.println("String: " + greeting);
        System.out.println("Array length: " + numbers.length);
        System.out.println("First name: " + names[0]);
        System.out.println("Person: " + person.getName() + ", " + person.getAge());
        
        // Null check
        if (nullString != null) {
            System.out.println("Null string: " + nullString.length());
        } else {
            System.out.println("String is null");
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

## Variable Scope and Lifetime

### Local Variables
```java
public class LocalVariables {
    public static void main(String[] args) {
        int outerVar = 10;  // Local to main method
        
        if (outerVar > 5) {
            int innerVar = 20;  // Local to if block
            System.out.println("Inner: " + innerVar);
            System.out.println("Outer: " + outerVar);
        }
        
        // Error: innerVar is not accessible here
        // System.out.println(innerVar);  // Compilation error!
        
        System.out.println("Outer: " + outerVar);
        
        // Method with local variables
        demonstrateMethodScope();
    }
    
    static void demonstrateMethodScope() {
        int methodVar = 100;  // Local to this method
        System.out.println("Method variable: " + methodVar);
    }
}
```

### Instance Variables (Fields)
```java
public class InstanceVariables {
    // Instance variables (fields)
    private String name;
    private int age;
    private static int instanceCount = 0;  // Class variable
    
    public InstanceVariables(String name, int age) {
        this.name = name;
        this.age = age;
        instanceCount++;
    }
    
    public void displayInfo() {
        System.out.println("Name: " + this.name);
        System.out.println("Age: " + this.age);
        System.out.println("Total instances: " + instanceCount);
    }
    
    // Static method accessing static variable
    public static int getInstanceCount() {
        return instanceCount;
    }
    
    public static void main(String[] args) {
        InstanceVariables person1 = new InstanceVariables("Alice", 25);
        InstanceVariables person2 = new InstanceVariables("Bob", 30);
        
        person1.displayInfo();
        person2.displayInfo();
        
        System.out.println("Total instances via static method: " + 
                          InstanceVariables.getInstanceCount());
    }
}
```

### Static Variables
```java
public class StaticVariables {
    // Static variables (class variables)
    private static final double PI = 3.141592653589793;
    private static int counter = 0;
    
    // Instance variable
    private int id;
    
    public StaticVariables() {
        counter++;
        id = counter;
    }
    
    public void display() {
        System.out.println("Instance ID: " + this.id);
        System.out.println("Total instances: " + counter);
        System.out.println("PI value: " + PI);
    }
    
    public static void displayStatic() {
        System.out.println("Total instances: " + counter);
        System.out.println("PI value: " + PI);
        // Cannot access instance variables here
        // System.out.println(this.id);  // Error!
    }
    
    public static void main(String[] args) {
        StaticVariables obj1 = new StaticVariables();
        StaticVariables obj2 = new StaticVariables();
        StaticVariables obj3 = new StaticVariables();
        
        obj1.display();
        obj2.display();
        
        StaticVariables.displayStatic();
    }
}
```

## Constants and Final Variables

### Final Variables
```java
public class FinalVariables {
    // Final constants
    private static final int MAX_SIZE = 100;
    private final int instanceId;
    
    public FinalVariables(int id) {
        this.instanceId = id;  // Must be initialized once
        // MAX_SIZE = 200;  // Error: Cannot modify final variable
    }
    
    public void display() {
        System.out.println("Instance ID: " + instanceId);
        System.out.println("Max size: " + MAX_SIZE);
        
        // Local final variable
        final double PI = 3.14159;
        // PI = 3.14;  // Error: Cannot modify final variable
        
        // Final reference (object reference cannot change, but object can)
        final StringBuilder sb = new StringBuilder("Hello");
        sb.append(" World");  // This is allowed
        // sb = new StringBuilder("New");  // Error: Cannot change reference
        
        System.out.println("String: " + sb.toString());
    }
    
    public static void main(String[] args) {
        FinalVariables fv = new FinalVariables(42);
        fv.display();
    }
}
```

### Constants Class Pattern
```java
public class Constants {
    // Public static final constants
    public static final double PI = 3.141592653589793;
    public static final double E = 2.718281828459045;
    public static final int DEFAULT_PORT = 8080;
    public static final String APP_NAME = "MyApplication";
    public static final String VERSION = "1.0.0";
    
    // Private constructor to prevent instantiation
    private Constants() {
        throw new AssertionError("Constants class should not be instantiated");
    }
    
    public static void main(String[] args) {
        System.out.println("Application: " + Constants.APP_NAME);
        System.out.println("Version: " + Constants.VERSION);
        System.out.println("Default port: " + Constants.DEFAULT_PORT);
        System.out.println("PI: " + Constants.PI);
    }
}
```

## Type Conversion and Casting

### Implicit Type Conversion (Widening)
```java
public class ImplicitConversion {
    public static void main(String[] args) {
        // Widening conversions (safe, no data loss)
        byte b = 100;
        short s = b;      // byte to short
        int i = s;        // short to int
        long l = i;       // int to long
        float f = l;       // long to float
        double d = f;      // float to double
        
        System.out.println("Byte: " + b);
        System.out.println("Short: " + s);
        System.out.println("Int: " + i);
        System.out.println("Long: " + l);
        System.out.println("Float: " + f);
        System.out.println("Double: " + d);
        
        // Character to int
        char c = 'A';
        int charValue = c;  // 65
        System.out.println("Character '" + c + "' as int: " + charValue);
        
        // Arithmetic promotion
        int x = 10;
        double y = 3.14;
        double result = x + y;  // x promoted to double
        System.out.println("10 + 3.14 = " + result);
    }
}
```

### Explicit Type Conversion (Narrowing)
```java
public class ExplicitConversion {
    public static void main(String[] args) {
        // Narrowing conversions (potential data loss)
        double d = 3.14159;
        float f = (float) d;      // double to float
        long l = (long) f;        // float to long
        int i = (int) l;          // long to int
        short s = (short) i;      // int to short
        byte b = (byte) s;        // short to byte
        
        System.out.println("Original double: " + d);
        System.out.println("To float: " + f);
        System.out.println("To long: " + l);
        System.out.println("To int: " + i);
        System.out.println("To short: " + s);
        System.out.println("To byte: " + b);
        
        // Data loss examples
        double pi = 3.14159;
        int intPi = (int) pi;  // Truncates decimal part
        System.out.println("Double PI: " + pi);
        System.out.println("Int PI: " + intPi);
        
        // Overflow example
        int largeInt = 300;
        byte smallByte = (byte) largeInt;  // Overflow
        System.out.println("Large int: " + largeInt);
        System.out.println "As byte: " + smallByte);
        
        // Character conversion
        int charCode = 65;
        char character = (char) charCode;
        System.out.println("Char code 65 as char: " + character);
    }
}
```

## Variable Naming Conventions

### Naming Rules and Conventions
```java
public class NamingConventions {
    // Constants: UPPER_SNAKE_CASE
    private static final int MAX_ATTEMPTS = 3;
    private static final String DEFAULT_URL = "https://example.com";
    
    // Class names: PascalCase
    public static class UserService {
        // Instance variables: camelCase (private)
        private String userName;
        private int userId;
        private boolean isActive;
        
        // Static variables: camelCase (private static)
        private static int userCounter = 0;
        
        // Methods: camelCase
        public void setUserName(String userName) {
            this.userName = userName;
        }
        
        public String getUserName() {
            return this.userName;
        }
        
        // Boolean getters: is/has prefix
        public boolean isActive() {
            return this.isActive;
        }
        
        // Local variables: camelCase, descriptive names
        public void processUserData() {
            String firstName = "John";
            String lastName = "Doe";
            int userAge = 25;
            boolean hasPremiumAccess = true;
            
            // Avoid these
            int x;                    // Meaningless name
            int a1, b2, c3;           // Non-descriptive
            String temp;              // Too generic
            int num;                  // Abbreviation, be more specific
            
            // Good practices
            int customerAge = 30;
            String emailAddress = "user@example.com";
            boolean isValidInput = true;
            int maxRetryAttempts = 5;
        }
    }
    
    public static void main(String[] args) {
        UserService service = new UserService();
        service.setUserName("Alice");
        System.out.println("User: " + service.getUserName());
    }
}
```

## Advanced Variable Features

### Var Keyword (Java 10+)
```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class VarKeyword {
    public static void main(String[] args) {
        // Local variable type inference (Java 10+)
        var number = 42;                    // Inferred as int
        var decimal = 3.14;                  // Inferred as double
        var text = "Hello, World!";          // Inferred as String
        var flag = true;                     // Inferred as boolean
        
        System.out.println("Number: " + number + " (type: " + 
                          ((Object)number).getClass().getSimpleName() + ")");
        System.out.println("Decimal: " + decimal + " (type: " + 
                          ((Object)decimal).getClass().getSimpleName() + ")");
        System.out.println("Text: " + text + " (type: " + 
                          ((Object)text).getClass().getSimpleName() + ")");
        System.out.println("Flag: " + flag + " (type: " + 
                          ((Object)flag).getClass().getSimpleName() + ")");
        
        // Collections with var
        var names = new ArrayList<String>();  // Inferred as ArrayList<String>
        names.add("Alice");
        names.add("Bob");
        
        var scores = new HashMap<String, Integer>();  // Inferred as HashMap<String, Integer>
        scores.put("Alice", 95);
        scores.put("Bob", 87);
        
        // Enhanced for loop with var
        for (var name : names) {
            System.out.println("Name: " + name);
        }
        
        for (var entry : scores.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        
        // Limitations of var
        // var x;  // Error: Cannot use 'var' without initializer
        // var y = null;  // Error: Cannot infer type for null
        // var z = new int[3];  // Error: Array initializer requires explicit type
        
        // Good use cases for var
        var inputStream = new java.io.ByteArrayInputStream("test".getBytes());
        var stringBuilder = new StringBuilder();
        var list = List.of(1, 2, 3, 4, 5);
    }
}
```

### Records (Java 14+)
```java
public record Person(String name, int age, String email) {
    // Compact constructor (for validation)
    public Person {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Name cannot be null or empty");
        }
        if (age < 0 || age > 150) {
            throw new IllegalArgumentException("Age must be between 0 and 150");
        }
        if (email == null || !email.contains("@")) {
            throw new IllegalArgumentException("Invalid email format");
        }
    }
    
    // Additional methods
    public boolean isAdult() {
        return age >= 18;
    }
    
    public String getDisplayName() {
        return name + " (" + age + ")";
    }
}

public class RecordExample {
    public static void main(String[] args) {
        // Creating records
        var person1 = new Person("Alice", 25, "alice@example.com");
        var person2 = new Person("Bob", 17, "bob@example.com");
        
        // Accessing components (automatically generated)
        System.out.println("Name: " + person1.name());
        System.out.println("Age: " + person1.age());
        System.out.println("Email: " + person1.email());
        
        // Using custom methods
        System.out.println(person1.getDisplayName() + " is adult: " + person1.isAdult());
        System.out.println(person2.getDisplayName() + " is adult: " + person2.isAdult());
        
        // Records are immutable
        // person1.age = 26;  // Error: Cannot assign to final variable
        
        // Built-in methods
        System.out.println("ToString: " + person1);
        System.out.println("Equals: " + person1.equals(new Person("Alice", 25, "alice@example.com")));
        System.out.println("HashCode: " + person1.hashCode());
        
        // Records in collections
        var people = List.of(person1, person2);
        people.forEach(person -> System.out.println(person.getDisplayName()));
    }
}
```

## Variable Best Practices

### Initialization and Null Safety
```java
import java.util.Optional;

public class VariableBestPractices {
    // Initialize variables at declaration
    private String name = "Unknown";
    private int count = 0;
    private boolean initialized = false;
    
    // Use Optional for nullable reference types
    private Optional<String> optionalName = Optional.empty();
    
    public void demonstrateInitialization() {
        // Always initialize variables
        String message = "Hello";
        int attempts = 0;
        boolean success = false;
        
        // Use meaningful default values
        int score = 0;           // Numeric
        boolean isValid = false; // Boolean
        String result = "";      // String
        List<String> items = new ArrayList<>(); // Collections
        
        // Null checks
        String potentiallyNull = getPotentiallyNullString();
        if (potentiallyNull != null) {
            System.out.println("Length: " + potentiallyNull.length());
        }
        
        // Optional for better null handling
        Optional<String> optionalResult = getOptionalString();
        optionalResult.ifPresent(value -> System.out.println("Value: " + value));
        
        // Or provide default
        String safeResult = optionalResult.orElse("Default value");
        System.out.println("Safe result: " + safeResult);
    }
    
    private String getPotentiallyNullString() {
        return Math.random() > 0.5 ? "Not null" : null;
    }
    
    private Optional<String> getOptionalString() {
        return Math.random() > 0.5 ? Optional.of("Optional value") : Optional.empty();
    }
    
    public static void main(String[] args) {
        VariableBestPractices practices = new VariableBestPractices();
        practices.demonstrateInitialization();
    }
}
```

### Variable Scope Management
```java
public class ScopeManagement {
    private static final int GLOBAL_CONSTANT = 100;
    private int instanceVariable = 50;
    
    public void demonstrateScope() {
        // Local variable with same name as instance variable
        int instanceVariable = 25;  // Shadows the instance variable
        
        System.out.println("Local: " + instanceVariable);
        System.out.println("Instance: " + this.instanceVariable);
        System.out.println("Global: " + GLOBAL_CONSTANT);
        
        // Block scope
        {
            int blockVariable = 10;
            System.out.println("Block: " + blockVariable);
        }
        // blockVariable is not accessible here
        
        // Keep scope minimal
        for (int i = 0; i < 5; i++) {
            int loopLocal = i * 2;
            System.out.println("i: " + i + ", loopLocal: " + loopLocal);
        }
        // i and loopLocal are not accessible here
        
        // Use final for variables that won't change
        final double PI = 3.14159;
        final String GREETING = "Hello";
        
        // Effective final (Java 8+)
        String message = "Effective final";
        Runnable runnable = () -> System.out.println(message);  // message is effectively final
        runnable.run();
    }
    
    public static void main(String[] args) {
        ScopeManagement sm = new ScopeManagement();
        sm.demonstrateScope();
    }
}
```

## Common Variable Pitfalls

### Uninitialized Variables
```java
public class VariablePitfalls {
    public static void main(String[] args) {
        // Error: Local variables must be initialized before use
        int uninitializedInt;
        // System.out.println(uninitializedInt);  // Compilation error!
        
        // Always initialize
        int safeInt = 0;
        System.out.println("Safe int: " + safeInt);
        
        // Instance variables are automatically initialized
        InstanceVariables iv = new InstanceVariables();
        iv.displayUninitialized();
        
        // Array elements are automatically initialized
        int[] numbers = new int[5];
        System.out.println("First element: " + numbers[0]);  // 0
        
        String[] strings = new String[5];
        System.out.println("First string: " + strings[0]);  // null
    }
}

class InstanceVariables {
    private int defaultInt;        // Automatically 0
    private double defaultDouble; // Automatically 0.0
    private boolean defaultBool;   // Automatically false
    private String defaultString; // Automatically null
    
    public void displayUninitialized() {
        System.out.println("Default int: " + defaultInt);
        System.out.println("Default double: " + defaultDouble);
        System.out.println("Default boolean: " + defaultBool);
        System.out.println("Default String: " + defaultString);
    }
}
```

### Variable Shadowing
```java
public class VariableShadowing {
    private static int globalVar = 100;
    private int instanceVar = 50;
    
    public void demonstrateShadowing() {
        int localVar = 25;  // Shadows instanceVar
        
        System.out.println("Local var: " + localVar);
        System.out.println("Instance var: " + this.instanceVar);
        System.out.println("Global var: " + VariableShadowing.globalVar);
        
        // Nested shadowing
        {
            int nestedVar = 10;
            System.out.println("Nested var: " + nestedVar);
            
            {
                int deeplyNestedVar = 5;
                System.out.println("Deeply nested: " + deeplyNestedVar);
            }
        }
        
        // Method parameter shadowing
        processData(42);
    }
    
    public void processData(int instanceVar) {  // Parameter shadows instance variable
        System.out.println("Parameter: " + instanceVar);
        System.out.println("Instance: " + this.instanceVar);
        
        // Use this to access instance variable
        this.instanceVar = instanceVar;
        System.out.println("Updated instance: " + this.instanceVar);
    }
    
    public static void main(String[] args) {
        VariableShadowing vs = new VariableShadowing();
        vs.demonstrateShadowing();
    }
}
```

## Performance Considerations

### Primitive vs Reference Types
```java
public class PerformanceConsiderations {
    public static void main(String[] args) {
        // Primitive types are more memory efficient
        long startTime = System.nanoTime();
        
        // Primitive array
        int[] primitiveArray = new int[1000000];
        for (int i = 0; i < primitiveArray.length; i++) {
            primitiveArray[i] = i;
        }
        
        long primitiveTime = System.nanoTime() - startTime;
        
        // Reference array
        startTime = System.nanoTime();
        Integer[] referenceArray = new Integer[1000000];
        for (int i = 0; i < referenceArray.length; i++) {
            referenceArray[i] = i;  // Autoboxing
        }
        
        long referenceTime = System.nanoTime() - startTime;
        
        System.out.println("Primitive array time: " + primitiveTime + " ns");
        System.out.println("Reference array time: " + referenceTime + " ns");
        System.out.println("Ratio: " + (double)referenceTime / primitiveTime);
        
        // Memory usage demonstration
        demonstrateMemoryUsage();
    }
    
    private static void demonstrateMemoryUsage() {
        Runtime runtime = Runtime.getRuntime();
        
        // Primitive array
        runtime.gc();
        long beforePrimitive = runtime.totalMemory() - runtime.freeMemory();
        int[] primitives = new int[1000000];
        long afterPrimitive = runtime.totalMemory() - runtime.freeMemory();
        long primitiveMemory = afterPrimitive - beforePrimitive;
        
        // Reference array
        runtime.gc();
        long beforeReference = runtime.totalMemory() - runtime.freeMemory();
        Integer[] references = new Integer[1000000];
        for (int i = 0; i < references.length; i++) {
            references[i] = Integer.valueOf(i);
        }
        long afterReference = runtime.totalMemory() - runtime.freeMemory();
        long referenceMemory = afterReference - beforeReference;
        
        System.out.println("Primitive array memory: " + primitiveMemory + " bytes");
        System.out.println("Reference array memory: " + referenceMemory + " bytes");
        System.out.println("Memory ratio: " + (double)referenceMemory / primitiveMemory);
    }
}
```

## Best Practices Summary

1. **Always initialize variables** before use
2. **Use meaningful names** that describe the variable's purpose
3. **Follow naming conventions** consistently (camelCase for variables, UPPER_SNAKE_CASE for constants)
4. **Minimize variable scope** - declare in the smallest possible scope
5. **Prefer final variables** when the value won't change
6. **Use Optional** for nullable reference types (Java 8+)
7. **Consider var** for local variables when the type is obvious (Java 10+)
8. **Avoid variable shadowing** to prevent confusion
9. **Choose appropriate types** based on required range and precision
10. **Use constants** for fixed values instead of magic numbers

## Conclusion

Understanding variables and keywords is fundamental to Java programming. Java's strong typing system, combined with modern language features like var and records, provides both safety and expressiveness. By following best practices and understanding the nuances of different variable types, scopes, and initialization patterns, you can write clean, efficient, and maintainable Java code that effectively leverages the language's type system and memory management features.
