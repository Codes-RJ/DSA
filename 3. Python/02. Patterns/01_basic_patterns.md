# Pattern Programming Guide

This comprehensive guide covers essential pattern programs in C++. Each section includes a description, the C++ code in proper markdown blocks, and the expected output.

---

### Table of Contents

1. [Right-Angled Triangles](#1-right-angled-triangles)
2. [Equilateral Triangle (Pyramid)](#2-equilateral-triangle-pyramid)
3. [Hollow Patterns](#3-hollow-patterns)
4. [Diamond Patterns](#4-diamond-patterns)
5. [Number Patterns](#5-number-patterns)
6. [Alphabet Patterns](#6-alphabet-patterns)
7. [Advanced Patterns](#7-advanced-patterns)

---

## 1. Right-Angled Triangles

These patterns form a 90-degree triangle. The orientation depends on the position of the hypotenuse.

### 1.1. Hypotenuse on the Right (Bottom-Left Aligned)

**Description:** The most common triangle pattern. Row `i` contains `i+1` stars.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
* 
* * 
* * * 
* * * * 
* * * * * 
```

---

### 1.2. Hypotenuse on the Left (Bottom-Right Aligned)

**Description:** Right-aligned triangle. Print spaces first, then stars.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        // Print spaces
        for (int j = 0; j < n - i - 1; j++) {
            cout << "  ";
        }
        // Print stars
        for (int j = 0; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
```

---

### 1.3. Vertically Inverse (Top-Left Aligned)

**Description:** Starts with maximum stars and decreases.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
* * * * * 
* * * * 
* * * 
* * 
* 
```

---

### 1.4. Vertically Inverse with Hypotenuse on Left (Top-Right Aligned)

**Description:** Inverse of the right-aligned triangle.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        // Print spaces
        for (int j = 0; j < i; j++) {
            cout << "  ";
        }
        // Print stars
        for (int j = 0; j < n - i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
```

---

## 2. Equilateral Triangle (Pyramid)

### 2.1. Solid Pyramid

**Description:** Symmetric triangle with odd number of stars in each row.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        // Print spaces
        for (int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }
        // Print stars
        for (int j = 0; j < 2 * i + 1; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
    *
   ***
  *****
 *******
*********
```

---

### 2.2. Inverted Pyramid

**Description:** Pyramid upside down.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = n; i >= 1; i--) {
        // Print spaces
        for (int j = 0; j < n - i; j++) {
            cout << " ";
        }
        // Print stars
        for (int j = 0; j < 2 * i - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
*********
 *******
  *****
   ***
    *
```

---

## 3. Hollow Patterns

### 3.1. Hollow Right-Angled Triangle

**Description:** Stars only on the boundary.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            // Print star for first column, last column of row, or last row
            if (j == 0 || j == i || i == n - 1) {
                cout << "* ";
            } else {
                cout << "  ";
            }
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
* 
* * 
*   * 
*     * 
* * * * * 
```

---

### 3.2. Hollow Square

**Description:** Border-only square pattern.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the size of the square: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 || i == n - 1 || j == 0 || j == n - 1) {
                cout << "* ";
            } else {
                cout << "  ";
            }
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
```

---

### 3.3. Hollow Pyramid

**Description:** Pyramid with hollow interior.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        // Print spaces
        for (int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }
        // Print stars with hollow condition
        for (int j = 0; j < 2 * i + 1; j++) {
            if (j == 0 || j == 2 * i || i == n - 1) {
                cout << "*";
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
    *
   * *
  *   *
 *     *
*********
```

---

### 3.4. Hollow Inverted Pyramid

**Description:** Inverted pyramid with hollow interior.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = n; i >= 1; i--) {
        // Print spaces
        for (int j = 0; j < n - i; j++) {
            cout << " ";
        }
        // Print stars with hollow condition
        for (int j = 0; j < 2 * i - 1; j++) {
            if (j == 0 || j == 2 * i - 2 || i == n) {
                cout << "*";
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
*********
 *     *
  *   *
   * *
    *
```

---

## 4. Diamond Patterns

### 4.1. Solid Diamond

**Description:** Combination of pyramid and inverted pyramid.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows for half diamond: ";
    cin >> n;

    // Upper half
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }

    // Lower half
    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

---

### 4.2. Hollow Diamond

**Description:** Diamond with only the boundary printed.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows for half diamond: ";
    cin >> n;

    // Upper half
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            if (j == 1 || j == 2 * i - 1) {
                cout << "*";
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }

    // Lower half
    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            if (j == 1 || j == 2 * i - 1) {
                cout << "*";
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
```

---

## 5. Number Patterns

### 5.1. Floyd's Triangle

**Description:** Consecutive numbers in a right-angled triangle.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;
    
    int num = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << num << " ";
            num++;
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 4):**
```
1 
2 3 
4 5 6 
7 8 9 10 
```

---

### 5.2. Pascal's Triangle

**Description:** Binomial coefficients arranged in triangular form.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        int val = 1;
        // Print spaces
        for (int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }
        for (int j = 0; j <= i; j++) {
            cout << val << " ";
            val = val * (i - j) / (j + 1);
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 
```

---

### 5.3. Number Pyramid

**Description:** Numbers arranged in a pyramid pattern.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        // Print spaces
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        // Print increasing numbers
        for (int j = 1; j <= i; j++) {
            cout << j;
        }
        // Print decreasing numbers
        for (int j = i - 1; j >= 1; j--) {
            cout << j;
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
    1
   121
  12321
 1234321
123454321
```

---

### 5.4. Number Diamond

**Description:** Diamond pattern using numbers.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows for half diamond: ";
    cin >> n;

    // Upper half
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= i; j++) {
            cout << j;
        }
        for (int j = i - 1; j >= 1; j--) {
            cout << j;
        }
        cout << endl;
    }

    // Lower half
    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= i; j++) {
            cout << j;
        }
        for (int j = i - 1; j >= 1; j--) {
            cout << j;
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
    1
   121
  12321
 1234321
123454321
 1234321
  12321
   121
    1
```

---

## 6. Alphabet Patterns

### 6.1. Right-Angled Alphabet Triangle

**Description:** Alphabetical characters in a right-angled triangle.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        char ch = 'A';
        for (int j = 1; j <= i; j++) {
            cout << ch << " ";
            ch++;
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
A 
A B 
A B C 
A B C D 
A B C D E 
```

---

### 6.2. Alphabet Pyramid

**Description:** Letters arranged in a pyramid pattern.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        // Print spaces
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        
        char ch = 'A';
        // Print increasing letters
        for (int j = 1; j <= i; j++) {
            cout << ch;
            ch++;
        }
        
        ch -= 2;
        // Print decreasing letters
        for (int j = 1; j <= i - 1; j++) {
            cout << ch;
            ch--;
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
```

---

### 6.3. Continuous Alphabet Triangle

**Description:** Continuous alphabetical sequence.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;
    
    char ch = 'A';
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << ch << " ";
            ch++;
            if (ch > 'Z') ch = 'A';
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
A 
B C 
D E F 
G H I J 
K L M N O 
```

---

## 7. Advanced Patterns

### 7.1. Butterfly Pattern

**Description:** Symmetrical butterfly design using stars.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows for half butterfly: ";
    cin >> n;

    // Upper half
    for (int i = 1; i <= n; i++) {
        // Left stars
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        // Spaces
        for (int j = 1; j <= 2 * (n - i); j++) {
            cout << " ";
        }
        // Right stars
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    }

    // Lower half
    for (int i = n; i >= 1; i--) {
        // Left stars
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        // Spaces
        for (int j = 1; j <= 2 * (n - i); j++) {
            cout << " ";
        }
        // Right stars
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
```

---

### 7.2. Hourglass Pattern

**Description:** Inverted pyramid combined with pyramid.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    // Upper half (inverted pyramid)
    for (int i = n; i >= 1; i--) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }

    // Lower half (pyramid)
    for (int i = 2; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
```

---

### 7.3. Plus Sign Pattern

**Description:** Plus sign shape made of stars.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the size (odd number): ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            // Print star at middle row or middle column
            if (i == (n + 1) / 2 || j == (n + 1) / 2) {
                cout << "* ";
            } else {
                cout << "  ";
            }
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
    *     
    *     
* * * * * 
    *     
    *     
```

---

### 7.4. X Shape Pattern

**Description:** Diagonal cross pattern.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the size (odd number): ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            // Print star at main diagonal or secondary diagonal
            if (i == j || i + j == n + 1) {
                cout << "* ";
            } else {
                cout << "  ";
            }
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
*       * 
  *   *   
    *     
  *   *   
*       * 
```

---

### 7.5. Swastik Pattern

**Description:** Swastik symbol pattern.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the size (odd number >= 5): ";
    cin >> n;
    
    int mid = (n + 1) / 2;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            // Conditions for swastik pattern
            if (i == mid || j == mid) {
                cout << "* ";
            }
            else if (i == 1 && j > mid) {
                cout << "* ";
            }
            else if (i == n && j < mid) {
                cout << "* ";
            }
            else if (j == 1 && i < mid) {
                cout << "* ";
            }
            else if (j == n && i > mid) {
                cout << "* ";
            }
            else {
                cout << "  ";
            }
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 7):**
```
* * * * * * * 
          *   
          *   
* * * * * * * 
*             
*             
* * * * * * * 
```

---

### 7.6. Spiral Pattern

**Description:** Square spiral pattern.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "Enter the size: ";
    cin >> n;
    
    vector<vector<int>> spiral(n, vector<int>(n, 0));
    
    int top = 0, bottom = n - 1, left = 0, right = n - 1;
    int num = 1;
    
    while (top <= bottom && left <= right) {
        // Fill top row
        for (int i = left; i <= right; i++) {
            spiral[top][i] = num++;
        }
        top++;
        
        // Fill right column
        for (int i = top; i <= bottom; i++) {
            spiral[i][right] = num++;
        }
        right--;
        
        // Fill bottom row
        if (top <= bottom) {
            for (int i = right; i >= left; i--) {
                spiral[bottom][i] = num++;
            }
            bottom--;
        }
        
        // Fill left column
        if (left <= right) {
            for (int i = bottom; i >= top; i--) {
                spiral[i][left] = num++;
            }
            left++;
        }
    }
    
    // Print spiral pattern
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%3d ", spiral[i][j]);
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
  1   2   3   4   5 
 16  17  18  19   6 
 15  24  25  20   7 
 14  23  22  21   8 
 13  12  11  10   9 
```

---

### 7.7. Chessboard Pattern

**Description:** Alternating star and space pattern.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the size: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if ((i + j) % 2 == 0) {
                cout << "* ";
            } else {
                cout << "  ";
            }
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
*   *   * 
  *   *   
*   *   * 
  *   *   
*   *   * 
```

---

### 7.8. Heart Pattern

**Description:** Heart shape made of stars.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the size (10-20 recommended): ";
    cin >> n;
    
    int mid = n / 2;

    for (int i = mid / 2; i <= mid; i += 2) {
        // Print spaces
        for (int j = 1; j < mid - i; j += 2) {
            cout << " ";
        }
        // Print first heart curve
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        // Print spaces between
        for (int j = 1; j <= mid - i; j++) {
            cout << " ";
        }
        // Print second heart curve
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    }
    
    // Lower part of heart
    for (int i = mid; i >= 1; i--) {
        for (int j = i; j < mid; j++) {
            cout << " ";
        }
        for (int j = 1; j <= (i * 2) - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 12):**
```
  ***      ***
 *****    *****
*******  *******
*****************
 ***************
  *************
   ***********
    *********
     *******
      *****
       ***
        *
```

---

### 7.9. Diamond with Numbers (Alternate Version)

**Description:** Diamond pattern with alternating numbers.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    // Upper half
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            if (j % 2 == 1) {
                cout << i;
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }

    // Lower half
    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            if (j % 2 == 1) {
                cout << i;
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 5):**
```
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
```

---

### 7.10. Zigzag Pattern

**Description:** Zigzag line pattern.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;
    
    int spaces = 0;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (j == spaces + 1 || j == n - spaces) {
                cout << "*";
            } else {
                cout << " ";
            }
        }
        
        if (i <= n / 2) {
            spaces++;
        } else {
            spaces--;
        }
        cout << endl;
    }
    return 0;
}
```

**Output (n = 9):**
```
*       *
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *
*       *
```

---

## Summary Table

| Pattern Type | Key Logic | Difficulty |
| :--- | :--- | :--- |
| **Right-Angled Triangles** | Nested loops with inner loop condition dependent on outer | ⭐ |
| **Pyramid/Diamond** | Split into halves, spaces for centering | ⭐⭐ |
| **Hollow Patterns** | Conditional printing for boundaries | ⭐⭐ |
| **Number Patterns** | Counter variables or mathematical formulas | ⭐⭐ |
| **Alphabet Patterns** | Character manipulation and ASCII values | ⭐⭐ |
| **Butterfly/Hourglass** | Symmetric patterns with mirroring logic | ⭐⭐⭐ |
| **Spiral** | 2D array traversal with boundary updates | ⭐⭐⭐⭐ |
| **Heart/Swastik** | Complex conditional logic for shapes | ⭐⭐⭐⭐ |

---

## Tips for Pattern Programming

1. **Analyze the pattern:** Count spaces, stars, and look for symmetry
2. **Break it down:** Split complex patterns into smaller parts
3. **Use loops wisely:** Outer loop for rows, inner loops for columns
4. **Find relationships:** Look for mathematical relationships between row numbers and pattern elements
5. **Start simple:** Begin with solid patterns before attempting hollow ones
6. **Debug with print statements:** Print row and column indices to understand the logic

Happy Coding! 🚀