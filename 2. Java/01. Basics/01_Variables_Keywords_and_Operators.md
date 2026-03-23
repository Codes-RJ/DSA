# Java Variables, Keywords, and Operators

## Overview
- Variables in Java are containers that hold data values during program execution. Java is a strongly-typed language, meaning every variable must have a declared type.
- Keywords are reserved words that have a predefined meaning in the Java language and cannot be used as identifiers (like variable or class names).
- Understanding variables and keywords is fundamental to Java programming.

## Java Keywords

Java has 53 reserved keywords (as of Java 17). Here are the most important ones, categorized by their use:

### Primitive Type Keywords
```java
byte            // 8-bit integer
short           // 16-bit integer
int             // 32-bit integer
long            // 64-bit integer
float           // 32-bit floating point
double          // 64-bit floating point
char            // 16-bit Unicode character
boolean         // true or false
```

### Class and Object-Related Keywords
```java
class           // Defines a class
interface       // Defines an interface
enum            // Defines an enumerated type
extends         // Indicates inheritance
implements      // Indicates interface implementation
new             // Creates a new object
instanceof      // Tests if an object is an instance of a class
this            // Refers to the current object
super           // Refers to the parent class
abstract        // Declares an abstract class or method
final           // Prevents inheritance, overriding, or reassignment
static          // Defines a class-level member
```

### Access Modifiers
```java
public          // Accessible from anywhere
private         // Accessible only within its own class
protected       // Accessible within the same package and subclasses
```

### Control Flow Keywords
```java
// Conditional statements
if              // Conditional branch
else            // Alternative branch
switch          // Multi-way branch
case            // Label for switch
default         // Default case for switch

// Loops
for             // For loop
while           // While loop
do              // Do-while loop

// Jump statements
break           // Exit loop or switch
continue        // Skip to next loop iteration
return          // Return from a method
```

### Exception Handling Keywords
```java
try             // Starts a block of code that might throw an exception
catch           // Catches an exception thrown in a try block
finally         // Executes code after try-catch, regardless of exception
throw           // Explicitly throws an exception
throws          // Declares exceptions a method might throw
```

### Package and Import Keywords
```java
package         // Declares the package for a class
import          // Imports classes or packages
```

### Other Important Keywords
```java
void            // Indicates a method returns no value
native          // Indicates a method is implemented in platform-specific code
strictfp        // Restricts floating-point calculations for portability
synchronized    // Controls access to a block of code by multiple threads
transient       // Prevents a field from being serialized
volatile        // Indicates a variable may be changed asynchronously
assert          // Tests assumptions about the program
```

### Reserved Literals (Not keywords, but have special meaning)
```java
true            // Boolean true literal
false           // Boolean false literal
null            // Null object reference
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
        String name;
        
        // Declaration with initialization
        int score = 100;
        double pi = 3.14159;
        char initial = 'A';
        boolean isValid = true;
        String greeting = "Hello, World!";
        
        // Multiple declarations in one line
        int x = 10, y = 20, z = 30;
    }
}
```

### Variable Types in Detail

#### Integer Types
```java
public class IntegerTypes {
    public static void main(String[] args) {
        // Different integer sizes
        byte smallNumber = 100;           // -128 to 127
        short mediumNumber = 1000;        // -32,768 to 32,767
        int regularNumber = 100000;       // -2^31 to 2^31-1
        long largeNumber = 1000000000L;   // Must end with 'L'
        
        // Binary, octal, and hexadecimal literals
        int binary = 0b1010;              // 10 in decimal
        int octal = 012;                  // 10 in decimal
        int hex = 0xA;                    // 10 in decimal
        
        // Using underscores for readability (Java 7+)
        int million = 1_000_000;
        long creditCard = 1234_5678_9012_3456L;
        
        System.out.println("Byte: " + smallNumber);
        System.out.println("Long: " + largeNumber);
        System.out.println("Binary: " + binary);
    }
}
```

#### Floating-Point Types
```java
public class FloatingTypes {
    public static void main(String[] args) {
        // Different precision levels
        float singlePrecision = 3.14159f;     // Must end with 'f' or 'F'
        double doublePrecision = 3.141592653589793;
        
        // Scientific notation
        double scientific = 1.23e-4;          // 0.000123
        
        // Special floating-point values
        float positiveInfinity = Float.POSITIVE_INFINITY;
        float negativeInfinity = Float.NEGATIVE_INFINITY;
        float notANumber = Float.NaN;
        
        System.out.println("Float: " + singlePrecision);
        System.out.println("Double: " + doublePrecision);
        System.out.println("Infinity: " + (1.0 / 0.0));
    }
}
```

#### Character Type
```java
public class CharacterTypes {
    public static void main(String[] args) {
        // Basic character
        char basicChar = 'A';
        
        // Unicode characters (supports any character from the Unicode standard)
        char unicodeOmega = '\u03A9';         // Ω
        char unicodeSmiley = '\u263A';        // ☺
        
        // Escape sequences
        char newline = '\n';
        char tab = '\t';
        char backslash = '\\';
        char singleQuote = '\'';
        
        // char is a numeric type (can be used in arithmetic)
        int charValue = basicChar;             // 'A' is 65 in ASCII/Unicode
        
        System.out.println("Character: " + basicChar);
        System.out.println("Unicode Omega: " + unicodeOmega);
        System.out.println("Char as int: " + charValue);
    }
}
```

#### Boolean Type
```java
public class BooleanTypes {
    public static void main(String[] args) {
        // Boolean values
        boolean isTrue = true;
        boolean isFalse = false;
        
        // Booleans from comparisons
        boolean fromComparison = (5 > 3);       // true
        
        // Boolean expressions
        boolean andResult = isTrue && isFalse;  // false
        boolean orResult = isTrue || isFalse;   // true
        boolean notResult = !isTrue;            // false
        
        System.out.println("True: " + isTrue);
        System.out.println("False: " + isFalse);
        System.out.println("5 > 3: " + fromComparison);
    }
}
```

#### Reference Types (Strings and Arrays)
```java
public class ReferenceTypes {
    public static void main(String[] args) {
        // String (a special reference type)
        String greeting = "Hello, World!";
        String empty = "";
        String multiline = """
                This is a
                multi-line
                string (Java 13+)
                """;
        
        // Arrays
        int[] numbers = {1, 2, 3, 4, 5};           // Array literal
        String[] names = new String[5];            // Array of size 5
        names[0] = "Alice";
        
        int[][] matrix = {                         // 2D array
            {1, 2, 3},
            {4, 5, 6}
        };
        
        System.out.println("Greeting: " + greeting);
        System.out.println("First number: " + numbers[0]);
        System.out.println("Matrix[1][2]: " + matrix[1][2]);
    }
}
```

## Variable Scope and Lifetime

### Local Variables
```java
public class LocalScope {
    public void demonstrateLocalScope() {
        int localVar = 10;                           // Exists only within this method
        
        if (localVar > 5) {
            int nestedVar = 20;                      // Exists only within this if block
            System.out.println("Nested: " + nestedVar);
        }
        
        // Error: nestedVar is not accessible here
        // System.out.println(nestedVar);            // Compilation error!
        
        System.out.println("Local: " + localVar);
    }
    
    public static void main(String[] args) {
        new LocalScope().demonstrateLocalScope();
    }
}
```

### Instance Variables (Fields)
```java
public class InstanceVariables {
    // Instance variables - belong to each object instance
    private String name;           // Default: null
    private int age;               // Default: 0
    private boolean isStudent;     // Default: false
    private double score;          // Default: 0.0
    
    // Constructor
    public InstanceVariables(String name, int age) {
        this.name = name;          // 'this' refers to the current instance
        this.age = age;
        // isStudent and score take default values
    }
    
    public void display() {
        System.out.println("Name: " + name + ", Age: " + age);
        System.out.println("Is student: " + isStudent);
        System.out.println("Score: " + score);
    }
    
    public static void main(String[] args) {
        InstanceVariables obj = new InstanceVariables("Alice", 25);
        obj.display();
    }
}
```

### Class Variables (Static)
```java
public class ClassVariables {
    // Class variable - shared across all instances
    private static int counter = 0;
    private static final double PI = 3.14159;          // Constant
    
    private int instanceId;
    
    public ClassVariables() {
        instanceId = ++counter;                        // Increment shared counter
    }
    
    public void display() {
        System.out.println("Instance " + instanceId + " of " + counter + " total");
    }
    
    public static void main(String[] args) {
        ClassVariables obj1 = new ClassVariables();  // Instance 1
        ClassVariables obj2 = new ClassVariables();  // Instance 2
        ClassVariables obj3 = new ClassVariables();  // Instance 3
        
        obj1.display();
        obj2.display();
        obj3.display();
        
        System.out.println("Total instances: " + counter);
        System.out.println("PI constant: " + PI);
    }
}
```

## Constants

### Using `final` Keyword
```java
public class Constants {
    // Class constant (using static final)
    public static final double PI = 3.141592653589793;
    public static final int MAX_SIZE = 100;
    public static final String APP_NAME = "MyApplication";
    
    // Instance constant
    private final int id;                     // Can be initialized in constructor
    
    public Constants(int id) {
        this.id = id;                         // Final variable initialized here
    }
    
    public void demonstrateLocalFinal() {
        final int localConstant = 42;         // Local constant
        // localConstant = 50;                // Error: cannot reassign final variable
        
        System.out.println("Local constant: " + localConstant);
    }
    
    public static void main(String[] args) {
        System.out.println("PI: " + PI);
        System.out.println("App: " + APP_NAME);
        
        Constants obj = new Constants(100);
        obj.demonstrateLocalFinal();
    }
}
```

### `enum` for Constants
```java
public class EnumConstants {
    // Define an enum (type-safe constant set)
    public enum Day {
        MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
    }
    
    public enum OrderStatus {
        PENDING("Waiting for processing"),
        PROCESSING("Being processed"),
        SHIPPED("Shipped to customer"),
        DELIVERED("Delivered"),
        CANCELLED("Order cancelled");
        
        private final String description;
        
        OrderStatus(String description) {
            this.description = description;
        }
        
        public String getDescription() {
            return description;
        }
    }
    
    public static void main(String[] args) {
        Day today = Day.WEDNESDAY;
        OrderStatus status = OrderStatus.SHIPPED;
        
        System.out.println("Today: " + today);
        System.out.println("Status: " + status + " - " + status.getDescription());
        
        // Switch with enum
        switch (today) {
            case MONDAY:
                System.out.println("Start of work week");
                break;
            case FRIDAY:
                System.out.println("TGIF!");
                break;
            default:
                System.out.println("Regular day");
        }
    }
}
```

## Type Inference

### `var` Keyword (Java 10+)
```java
import java.util.ArrayList;
import java.util.HashMap;

public class TypeInference {
    public static void main(String[] args) {
        // Basic type inference
        var integer = 42;                    // int
        var floating = 3.14;                 // double
        var character = 'A';                 // char
        var booleanVar = true;               // boolean
        var string = "Hello";                // String
        
        // Complex types
        var numbers = new ArrayList<Integer>();       // ArrayList<Integer>
        var scores = new HashMap<String, Integer>();  // HashMap<String, Integer>
        
        // With collections
        var list = java.util.List.of(1, 2, 3);    // List<Integer>
        
        // In loops
        for (var i = 0; i < 10; i++) {            // i is int
            System.out.print(i + " ");
        }
        
        // Cannot be used without initialization
        // var something;                         // Error: cannot infer type
        
        // Cannot be used with null
        // var nullVar = null;                    // Error: cannot infer type
        
        System.out.println("\nInferred integer: " + integer);
        System.out.println("Inferred string: " + string);
    }
}
```

## Variable Naming Conventions

### Best Practices
```java
public class NamingConventions {
    // Classes: PascalCase
    public class StudentManager {
        // Constants: UPPER_SNAKE_CASE
        private static final int MAX_STUDENTS = 50;
        private static final String DEFAULT_NAME = "Unknown";
        
        // Instance variables: camelCase
        private String studentName;
        private int studentAge;
        private boolean isValidStudent;
        
        // Methods: camelCase, usually verb-noun
        public void addStudent(String name) {
            // Local variables: camelCase, descriptive
            String newStudentId = "STU-1001";
            int tempCounter = 0;
            
            // Avoid these
            // int x;                                 // meaningless
            // int a1, b2;                            // non-descriptive
        }
        
        // Boolean getters: 'is' prefix
        public boolean isValidStudent() {
            return isValidStudent;
        }
        
        // Getters and setters: get/set prefix
        public String getStudentName() {
            return studentName;
        }
        
        public void setStudentName(String studentName) {
            this.studentName = studentName;
        }
    }
}
```

## Type Conversions

### Implicit (Widening) Conversions
```java
public class ImplicitConversion {
    public static void main(String[] args) {
        // Widening conversions are automatic and safe
        byte b = 10;
        short s = b;          // byte to short
        int i = s;            // short to int
        long l = i;           // int to long
        float f = l;          // long to float (possible precision loss)
        double d = f;         // float to double
        
        // char to int (widening)
        char c = 'A';
        int charToInt = c;    // 65
        
        System.out.println("Char to int: " + charToInt);
        
        // Binary numeric promotion in expressions
        byte b1 = 10;
        byte b2 = 20;
        int sum = b1 + b2;         // Result is promoted to int
        
        // Mixing types
        double result = 10 + 5.5;  // int promoted to double
    }
}
```

### Explicit (Narrowing) Conversions
```java
public class ExplicitConversion {
    public static void main(String[] args) {
        // Narrowing conversions require explicit casting
        double pi = 3.14159;
        int truncated = (int) pi;                 // 3 (loss of fractional part)
        
        long largeNumber = 1_000_000_000_000L;
        int overflow = (int) largeNumber;         // Overflow!
        
        // Casting between numeric types
        int intValue = 100;
        byte byteValue = (byte) intValue;         // Works if within range
        byte overflowByte = (byte) 200;           // 200 mod 256 = -56 (overflow)
        
        // Casting objects (requires inheritance relationship)
        Object obj = "Hello";
        String str = (String) obj;                // Downcasting
        
        // instanceof check for safe casting
        if (obj instanceof String) {
            String safeStr = (String) obj;
            System.out.println("Safe cast: " + safeStr);
        }
        
        System.out.println("Truncated: " + truncated);
        System.out.println("Byte overflow: " + overflowByte);
    }
}
```

### Wrapper Classes and Auto-boxing
```java
public class WrappersAndAutoBoxing {
    public static void main(String[] args) {
        // Primitive wrapper classes
        Integer intObj = Integer.valueOf(42);
        Double doubleObj = Double.valueOf(3.14);
        Boolean boolObj = Boolean.valueOf(true);
        Character charObj = Character.valueOf('A');
        
        // Auto-boxing (Java 5+): automatic conversion from primitive to wrapper
        Integer autoBoxed = 42;                       // int → Integer
        Double autoBoxedDouble = 3.14;                // double → Double
        
        // Auto-unboxing: wrapper to primitive
        int primitive = autoBoxed;                    // Integer → int
        double primitiveDouble = autoBoxedDouble;     // Double → double
        
        // Useful wrapper methods
        int parsedInt = Integer.parseInt("123");
        double parsedDouble = Double.parseDouble("3.14");
        String binaryString = Integer.toBinaryString(42);
        
        System.out.println("Parsed: " + parsedInt);
        System.out.println("Binary: " + binaryString);
        System.out.println("Max int: " + Integer.MAX_VALUE);
    }
}
```

## Common Variable Pitfalls

### Uninitialized Variables
```java
public class UninitializedVariables {
    // Instance variables get default values
    private int instanceInt;        // Default: 0
    private String instanceString;  // Default: null
    private boolean instanceBool;   // Default: false
    
    public void demonstrate() {
        // Local variables MUST be initialized before use
        int localInt;
        // System.out.println(localInt);                // Compilation error!
        
        // Initialize before use
        localInt = 10;
        System.out.println("Local int: " + localInt);
        
        // Instance variables are auto-initialized
        System.out.println("Instance int: " + instanceInt);
        System.out.println("Instance string: " + instanceString);
    }
    
    public static void main(String[] args) {
        new UninitializedVariables().demonstrate();
    }
}
```

### Variable Shadowing
```java
public class VariableShadowing {
    private int value = 100;  // Instance variable
    
    public void demonstrate(int value) {                   // Parameter shadows instance variable
        // Access parameter (closest scope)
        System.out.println("Parameter: " + value);         // Uses parameter
        
        // Access instance variable using 'this'
        System.out.println("Instance: " + this.value);     // Uses instance variable
        
        {
            int value2 = 300;  // Block-level variable
            // System.out.println(value);                  // Still parameter, block doesn't create new scope
        }
    }
    
    public static void main(String[] args) {
        VariableShadowing vs = new VariableShadowing();
        vs.demonstrate(200);
    }
}
```

---
# Java Operators

## Overview
- Operators are special symbols that perform operations on operands (variables and values).
- Java provides a comprehensive set of operators organized into various categories.

## Arithmetic Operators
```java
public class ArithmeticOperators {
    public static void main(String[] args) {
        int a = 10, b = 3;
        
        // Basic arithmetic
        int sum = a + b;          // Addition: 13
        int difference = a - b;   // Subtraction: 7
        int product = a * b;      // Multiplication: 30
        int quotient = a / b;     // Division: 3 (integer division truncates)
        int remainder = a % b;    // Modulo: 1
        
        // Unary operators
        int x = 5;
        int y = +x;               // Unary plus: 5
        int z = -x;               // Unary minus: -5
        
        // Increment/Decrement
        int counter = 0;
        counter++;                // Post-increment: returns 0, then becomes 1
        ++counter;                // Pre-increment: becomes 2, returns 2
        counter--;                // Post-decrement: returns 2, then becomes 1
        --counter;                // Pre-decrement: becomes 0, returns 0
        
        System.out.println("Sum: " + sum);
        System.out.println("Quotient: " + quotient);
        System.out.println("Remainder: " + remainder);
        System.out.println("Counter: " + counter);
        
        // Floating point division
        double precise = 10.0 / 3.0;                    // 3.3333333333333335
        System.out.println("Precise: " + precise);
    }
}
```

## Relational (Comparison) Operators
```java
public class RelationalOperators {
    public static void main(String[] args) {
        int a = 5, b = 10;
        
        boolean equal = (a == b);           // Equal to: false
        boolean notEqual = (a != b);        // Not equal to: true
        boolean lessThan = (a < b);         // Less than: true
        boolean greaterThan = (a > b);      // Greater than: false
        boolean lessEqual = (a <= b);       // Less than or equal: true
        boolean greaterEqual = (a >= b);    // Greater than or equal: false
        
        System.out.println("5 == 10: " + equal);
        System.out.println("5 != 10: " + notEqual);
        System.out.println("5 < 10: " + lessThan);
        
        // Reference comparison vs value comparison
        String s1 = new String("Hello");
        String s2 = new String("Hello");
        
        boolean referenceEqual = (s1 == s2);        // false (different objects)
        boolean valueEqual = s1.equals(s2);         // true (same content)
        
        System.out.println("Reference equal: " + referenceEqual);
        System.out.println("Value equal: " + valueEqual);
    }
}
```

## Logical Operators
```java
public class LogicalOperators {
    public static void main(String[] args) {
        boolean condition1 = true;
        boolean condition2 = false;
        
        // Basic logical operators
        boolean logicalAnd = condition1 && condition2;   // AND: false
        boolean logicalOr = condition1 || condition2;    // OR: true
        boolean logicalNot = !condition1;                // NOT: false
        boolean logicalXor = condition1 ^ condition2;    // XOR: true
        
        // Short-circuit evaluation
        int x = 5;
        boolean shortCircuit = (x > 0) && (++x > 5);      // ++x only evaluated if first is true
        System.out.println("Short-circuit x: " + x);      // x becomes 6
        
        // Non-short-circuit operators (rarely used)
        boolean nonShort = (x > 0) & (++x > 5);           // Always evaluates both
        System.out.println("Non-short-circuit x: " + x);  // x becomes 7
        
        System.out.println("AND: " + logicalAnd);
        System.out.println("OR: " + logicalOr);
        System.out.println("XOR: " + logicalXor);
        
        // De Morgan's Laws
        boolean deMorgan1 = !(condition1 && condition2);
        boolean deMorgan2 = !condition1 || !condition2;
        System.out.println("De Morgan's Laws: " + (deMorgan1 == deMorgan2));
    }
}
```

## Bitwise Operators
```java
public class BitwiseOperators {
    public static void main(String[] args) {
        int a = 0b1010;                                  // 10 in decimal
        int b = 0b1100;                                  // 12 in decimal
        
        int bitwiseAnd = a & b;                           // AND: 0b1000 (8)
        int bitwiseOr = a | b;                            // OR: 0b1110 (14)
        int bitwiseXor = a ^ b;                           // XOR: 0b0110 (6)
        int bitwiseNot = ~a;                              // NOT: 0b...11110101 (depends on bit width)
                             
        int leftShift = a << 2;                           // Left shift: 0b101000 (40)
        int rightShift = a >> 1;                          // Right shift: 0b0101 (5)
        int unsignedRightShift = a >>> 1;                 // Unsigned right shift: 0b0101 (5)
        
        System.out.println("a & b: " + bitwiseAnd + " (binary: " + 
                          Integer.toBinaryString(bitwiseAnd) + ")");
        System.out.println("a | b: " + bitwiseOr + " (binary: " + 
                          Integer.toBinaryString(bitwiseOr) + ")");
        System.out.println("a << 2: " + leftShift);
        
        // Bitwise operators with assignment
        int flags = 0;
        flags |= 0b0001;  // Set bit 0
        flags |= 0b0010;  // Set bit 1
        flags &= ~0b0001; // Clear bit 0
        
        System.out.println("Flags: " + Integer.toBinaryString(flags));
    }
}
```

## Assignment Operators
```java
public class AssignmentOperators {
    public static void main(String[] args) {
        int x = 10;      // Basic assignment
        
        // Compound assignment operators
        x += 5;          // x = x + 5 → 15
        x -= 3;          // x = x - 3 → 12
        x *= 2;          // x = x * 2 → 24
        x /= 4;          // x = x / 4 → 6
        x %= 2;          // x = x % 2 → 0
        
        // Bitwise compound assignment
        int y = 0b1010;
        y &= 0b1100;     // y = y & 0b1100 → 0b1000 (8)
        y |= 0b0011;     // y = y | 0b0011 → 0b1011 (11)
        y ^= 0b0110;     // y = y ^ 0b0110 → 0b1101 (13)
        y <<= 1;         // y = y << 1 → 0b11010 (26)
        
        System.out.println("x: " + x);
        System.out.println("y: " + y);
        
        // Assignment returns a value (can be chained)
        int a, b, c;
        a = b = c = 100;                     // Assigns 100 to all three variables
        System.out.println("a: " + a + ", b: " + b + ", c: " + c);
    }
}
```

## Ternary (Conditional) Operator
```java
public class TernaryOperator {
    public static void main(String[] args) {
        int a = 5, b = 10;
        
        // Basic ternary: condition ? expression1 : expression2
        int max = (a > b) ? a : b;               // Returns larger value
        System.out.println("Maximum: " + max);
        
        // Nested ternary (use sparingly)
        int value = 75;
        String grade = (value >= 90) ? "A" :
                       (value >= 80) ? "B" :
                       (value >= 70) ? "C" :
                       (value >= 60) ? "D" : "F";
        System.out.println("Grade: " + grade);
        
        // Ternary for null checks
        String input = null;
        String output = (input != null) ? input : "default";
        System.out.println("Output: " + output);
        
        // Ternary with method calls
        boolean isValid = true;
        int result = isValid ? computePositive() : computeNegative();
        System.out.println("Result: " + result);
    }
    
    static int computePositive() { return 100; }
    static int computeNegative() { return -100; }
}
```

## Instanceof Operator
```java
public class InstanceofOperator {
    public static void main(String[] args) {
        // Simple instanceof
        String str = "Hello";
        boolean isString = str instanceof String;     // true
        boolean isObject = str instanceof Object;     // true
        
        // With inheritance
        Animal animal = new Dog();
        boolean isDog = animal instanceof Dog;        // true
        boolean isAnimal = animal instanceof Animal;  // true
        boolean isCat = animal instanceof Cat;        // false
        
        // Pattern matching instanceof (Java 16+)
        if (animal instanceof Dog dog) {
            dog.bark();                                // dog is automatically cast
        }
        
        // null instanceof always returns false
        String nullStr = null;
        boolean isNullInstance = nullStr instanceof String;     // false
        
        System.out.println("Is String: " + isString);
        System.out.println("Is Dog: " + isDog);
    }
}

class Animal {}
class Dog extends Animal {
    void bark() { System.out.println("Woof!"); }
}
class Cat extends Animal {}
```

## Operator Precedence
```java
public class OperatorPrecedence {
    public static void main(String[] args) {
        // Multiplication has higher precedence than addition
        int result1 = 5 + 3 * 2;      // 11, not 16
        
        // Use parentheses to change evaluation order
        int result2 = (5 + 3) * 2;    // 16
        
        // Logical AND has higher precedence than OR
        boolean result3 = true || false && false;            // true (&& evaluated first)
        boolean result4 = (true || false) && false;          // false
        
        // Mixing operators
        int complex = 10 + 5 * 2 - 8 / 2;                    // 10 + 10 - 4 = 16
        int withParentheses = (10 + 5) * (2 - 8) / 2;        // 15 * -6 / 2 = -45
        
        System.out.println("5 + 3 * 2 = " + result1);
        System.out.println("(5 + 3) * 2 = " + result2);
        System.out.println("Complex: " + complex);
        System.out.println("With parentheses: " + withParentheses);
    }
}
```

### Common Precedence Rules (Highest to Lowest)
```
1.  () [] . (method call, array access, member access)
2.  ++ -- + - ! ~ (unary operators)
3.  * / %
4.  + -
5.  << >> >>>
6.  < <= > >= instanceof
7.  == !=
8.  &
9.  ^
10. |
11. &&
12. ||
13. ?: (ternary)
14. = += -= *= etc. (assignment)
```

## Special Operators and Constructs

### `+` Operator for String Concatenation
```java
public class StringConcatenation {
    public static void main(String[] args) {
        // String concatenation
        String greeting = "Hello";
        String name = "World";
        String message = greeting + ", " + name + "!";  // "Hello, World!"
        
        // Mixing strings with other types
        int age = 25;
        String intro = "I am " + age + " years old.";  // "I am 25 years old."
        
        // Operator precedence matters
        String result = "Result: " + 10 + 20;          // "Result: 1020"
        String correct = "Result: " + (10 + 20);       // "Result: 30"
        
        System.out.println(message);
        System.out.println(intro);
        System.out.println(result);
        System.out.println(correct);
        
        // Using StringBuilder for multiple concatenations (more efficient)
        StringBuilder sb = new StringBuilder();
        sb.append("Hello").append(", ").append("World").append("!");
        String efficient = sb.toString();
        System.out.println(efficient);
    }
}
```

### `new` Operator (Object Creation)
```java
public class NewOperator {
    public static void main(String[] args) {
        // Creating objects with new
        StringBuilder sb = new StringBuilder();           // Default constructor
        ArrayList<String> list = new ArrayList<>();       // Diamond operator (Java 7+)
        int[] array = new int[10];                        // Array creation
        String str = new String("Hello");                 // String object
        
        // Anonymous arrays
        int[] literalArray = new int[]{1, 2, 3, 4, 5};
        
        // Multidimensional arrays
        int[][] matrix = new int[3][4];
        
        // Using new with generic types
        java.util.HashMap<String, Integer> map = new java.util.HashMap<>();
        map.put("one", 1);
        
        System.out.println("Array length: " + array.length);
        System.out.println("Map size: " + map.size());
    }
}
```

### `instanceof` Pattern Matching (Java 16+)
```java
public class PatternMatching {
    public static void main(String[] args) {
        Object obj = "Hello, World!";
        
        // Old way
        if (obj instanceof String) {
            String str = (String) obj;
            System.out.println("Old way: " + str.toUpperCase());
        }
        
        // Pattern matching (Java 16+)
        if (obj instanceof String str) {
            System.out.println("Pattern matching: " + str.toUpperCase());
        }
        
        // With conditions
        if (obj instanceof String str && str.length() > 10) {
            System.out.println("Long string: " + str);
        }
        
        // With switch expressions (Java 17+)
        switch (obj) {
            case Integer i -> System.out.println("Integer: " + i);
            case String s -> System.out.println("String: " + s);
            case null -> System.out.println("null");
            default -> System.out.println("Other type");
        }
    }
}
```

## Practical Example: Combining Operators
```java
public class CombinedOperators {
    public static void main(String[] args) {
        // Calculate compound interest with combined operators
        double principal = 1000.0;
        double rate = 0.05;
        int years = 3;
        
        double amount = principal;
        for (int i = 0; i < years; i++) {
            amount *= (1 + rate);               // Compound assignment with multiplication
        }
        
        // Complex expression with multiple operators
        int a = 5, b = 10, c = 15;
        int result = (a + b) * c / 2 - 10;      // (5+10)*15/2-10 = 102.5? No, integer division truncates!
        
        // Find maximum of three numbers using ternary
        int max = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);
        
        // Bit flags example
        int permissions = 0;
        permissions |= 0b001;                   // Read permission
        permissions |= 0b010;                   // Write permission
        boolean canRead = (permissions & 0b001) != 0;
        boolean canWrite = (permissions & 0b010) != 0;
        
        System.out.println("Amount after " + years + " years: $" + amount);
        System.out.println("Result: " + result);
        System.out.println("Maximum: " + max);
        System.out.println("Can read: " + canRead);
        System.out.println("Can write: " + canWrite);
    }
}
```

## Best Practices Summary

1. **Always initialize local variables** before use; they don't get default values.
2. **Use meaningful variable names** that describe their purpose (e.g., `studentAge` not `sa`).
3. **Use `final` for constants** and variables that shouldn't change.
4. **Use `var` judiciously** (Java 10+) when the type is obvious from context.
5. **Follow Java naming conventions**:
   - Classes: `PascalCase`
   - Methods and variables: `camelCase`
   - Constants: `UPPER_SNAKE_CASE`
6. **Prefer primitive types over wrappers** for performance unless nullability is needed.
7. **Use `equals()` for string comparison**, not `==`.
8. **Be aware of integer division** - it truncates toward zero.
9. **Use parentheses for clarity** when operator precedence might be ambiguous.
10. **Prefer prefix increment (`++i`) over postfix (`i++`)** when the old value isn't needed.
11. **Use compound operators** (`+=`, `-=`, etc.) for cleaner code.
12. **Understand short-circuit evaluation** in logical operators (`&&`, `||`).
13. **Use bitwise operators only when working with bits or flags**.
14. **Use `instanceof` with pattern matching** (Java 16+) for cleaner type checking.
15. **Use `StringBuilder` for multiple string concatenations** in loops.

## Conclusion

Understanding variables, keywords, and operators is fundamental to Java programming. Java's strong typing and rich set of operators provide powerful tools for building robust applications. By following naming conventions, understanding type conversions, and using operators correctly, you can write more readable, maintainable, and efficient Java code. Modern Java features like `var`, pattern matching, and enhanced switch expressions continue to evolve the language, making it more expressive and developer-friendly.