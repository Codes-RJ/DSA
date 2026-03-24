# iostream - Input/Output Stream Library

The `iostream` library is one of the most fundamental C++ headers, providing input and output functionality through streams.

## 📖 Overview

`iostream` is part of the C++ standard library that handles input and output operations. It provides three main stream objects:
- `cin` - Standard input stream (usually keyboard)
- `cout` - Standard output stream (usually console)
- `cerr` - Standard error stream (unbuffered)
- `clog` - Standard logging stream (buffered)

## 🎯 Key Components

### Stream Objects
```cpp
#include <iostream>

int main() {
    int number;
    string name;
    
    // Input with cin
    cout << "Enter your name: ";
    cin >> name;  // Reads a single word
    
    cout << "Enter your age: ";
    cin >> number;  // Reads an integer
    
    // Output with cout
    cout << "Hello, " << name << "! You are " << number << " years old." << endl;
    
    // Error output
    cerr << "This is an error message" << endl;
    
    // Log output
    clog << "This is a log message" << endl;
    
    return 0;
}
```

### Input Methods

#### Basic Input
```cpp
int x;
double y;
char z;
string s;

cin >> x;    // Read integer
cin >> y;    // Read double
cin >> z;    // Read character
cin >> s;    // Read string (single word)
```

#### Multiple Input
```cpp
int a, b, c;
cin >> a >> b >> c;  // Read three integers
```

#### Line Input
```cpp
string line;
getline(cin, line);  // Read entire line
```

#### Mixed Input (Common Pitfall)
```cpp
int age;
string name;

cout << "Enter age: ";
cin >> age;
cin.ignore();  // Clear newline character

cout << "Enter full name: ";
getline(cin, name);  // Now works correctly
```

### Output Methods

#### Basic Output
```cpp
cout << "Hello World!" << endl;
cout << "Value: " << 42 << endl;
```

#### Formatting Output
```cpp
#include <iomanip>

double pi = 3.14159265;

cout << fixed << setprecision(2) << pi << endl;  // 3.14
cout << scientific << pi << endl;                // 3.14e+00
cout << setw(10) << pi << endl;                  // Width of 10
cout << setfill('*') << setw(10) << pi << endl;  // ***3.14159
```

## 🔧 Common Operations

### Reading Arrays
```cpp
int arr[5];
cout << "Enter 5 numbers: ";
for (int i = 0; i < 5; i++) {
    cin >> arr[i];
}

cout << "Array elements: ";
for (int i = 0; i < 5; i++) {
    cout << arr[i] << " ";
}
cout << endl;
```

### Reading Vectors
```cpp
#include <vector>

vector<int> vec;
int n, value;

cout << "Enter number of elements: ";
cin >> n;

cout << "Enter " << n << " elements: ";
for (int i = 0; i < n; i++) {
    cin >> value;
    vec.push_back(value);
}

cout << "Vector elements: ";
for (int val : vec) {
    cout << val << " ";
}
cout << endl;
```

### String Input Handling
```cpp
string firstName, lastName, fullName;

cout << "Enter first name: ";
cin >> firstName;

cout << "Enter last name: ";
cin >> lastName;

fullName = firstName + " " + lastName;
cout << "Full name: " << fullName << endl;

// For full line input
cin.ignore();  // Clear buffer
string address;
cout << "Enter address: ";
getline(cin, address);
cout << "Address: " << address << endl;
```

## 🎮 Interactive Examples

### Calculator Example
```cpp
#include <iostream>
#include <cmath>

int main() {
    double num1, num2;
    char operation;
    
    cout << "Simple Calculator" << endl;
    cout << "Enter first number: ";
    cin >> num1;
    
    cout << "Enter operation (+, -, *, /): ";
    cin >> operation;
    
    cout << "Enter second number: ";
    cin >> num2;
    
    double result;
    switch (operation) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 != 0) {
                result = num1 / num2;
            } else {
                cerr << "Error: Division by zero!" << endl;
                return 1;
            }
            break;
        default:
            cerr << "Error: Invalid operation!" << endl;
            return 1;
    }
    
    cout << "Result: " << num1 << " " << operation << " " << num2 << " = " << result << endl;
    
    return 0;
}
```

### Menu-Driven Program
```cpp
#include <iostream>
#include <vector>

void displayMenu() {
    cout << "\n=== MENU ===" << endl;
    cout << "1. Add element" << endl;
    cout << "2. Display elements" << endl;
    cout << "3. Find maximum" << endl;
    cout << "4. Exit" << endl;
    cout << "Enter choice: ";
}

int main() {
    vector<int> numbers;
    int choice, value;
    
    while (true) {
        displayMenu();
        cin >> choice;
        
        switch (choice) {
            case 1:
                cout << "Enter number to add: ";
                cin >> value;
                numbers.push_back(value);
                cout << "Added: " << value << endl;
                break;
                
            case 2:
                cout << "Elements: ";
                for (int num : numbers) {
                    cout << num << " ";
                }
                cout << endl;
                break;
                
            case 3:
                if (!numbers.empty()) {
                    int max_val = numbers[0];
                    for (int num : numbers) {
                        if (num > max_val) {
                            max_val = num;
                        }
                    }
                    cout << "Maximum: " << max_val << endl;
                } else {
                    cout << "No elements!" << endl;
                }
                break;
                
            case 4:
                cout << "Goodbye!" << endl;
                return 0;
                
            default:
                cerr << "Invalid choice! Try again." << endl;
        }
    }
    
    return 0;
}
```

## ⚡ Performance Tips

### Fast Input (for Competitive Programming)
```cpp
#include <iostream>

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}

int main() {
    fastIO();
    
    int n;
    cin >> n;
    
    // Now input/output is much faster
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        // Process x
    }
    
    return 0;
}
```

### Output Buffering
```cpp
#include <iostream>

int main() {
    // Unbuffered output (slower but immediate)
    cout << "Immediate output" << endl;
    
    // Buffered output (faster)
    for (int i = 0; i < 1000; i++) {
        cout << i << " ";
    }
    cout << flush;  // Force output buffer to flush
    
    return 0;
}
```

## 🐛 Common Pitfalls & Solutions

### 1. Mixing `cin >>` and `getline`
```cpp
// Problem
int age;
string name;
cin >> age;        // Leaves newline in buffer
getline(cin, name); // Skips input

// Solution
cin >> age;
cin.ignore();      // Clear the newline
getline(cin, name);
```

### 2. Input Validation
```cpp
int number;
cout << "Enter a positive number: ";

while (!(cin >> number) || number <= 0) {
    cin.clear();  // Clear error flags
    cin.ignore(numeric_limits<streamsize>::max(), '\n');  // Clear buffer
    cout << "Invalid input! Enter a positive number: ";
}
```

### 3. String Input with Spaces
```cpp
string word, sentence;
cin >> word;        // Only reads first word
getline(cin, sentence);  // Reads entire line
```

## 🎯 Best Practices

1. **Always check input state** when reading critical data
2. **Use `getline()` for string input with spaces**
3. **Clear input buffer** when switching between input types
4. **Use appropriate stream objects** (`cout` for normal output, `cerr` for errors)
5. **Consider fast I/O** for competitive programming

## 📚 Related Headers

- [`iomanip.md`](iomanip.md) - For output formatting
- [`fstream.md`](fstream.md) - For file input/output
- [`sstream.md`](sstream.md) - For string streams
- [`string.md`](string.md) - For string operations

## 🚀 Next Steps

1. Practice basic input/output operations
2. Learn about input validation
3. Explore file operations with `fstream`
4. Study string streams with `sstream`

---

**Examples in this file**: 5 complete programs  
**Key Functions**: `cin`, `cout`, `cerr`, `clog`, `getline()`  
**Common Use Cases**: User interaction, data input, result display
