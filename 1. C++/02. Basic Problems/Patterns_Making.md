# Pattern Programming Guide (C++)

## Table of Contents

1. [Star Patterns](#1-star-patterns)
2. [Hollow Star Patterns](#2-hollow-star-patterns)
3. [Diamond Star Patterns](#3-diamond-star-patterns)
4. [Number Patterns](#4-number-patterns)
5. [Alphabet Patterns](#5-alphabet-patterns)
6. [Special / Art Patterns](#6-special--art-patterns)
7. [Mathematical Patterns](#7-mathematical-patterns)
8. [Geometric / Grid Patterns](#8-geometric--grid-patterns)
9. [Optimization & Techniques](#9-optimization--techniques)

---

## 1. Star Patterns

### 1.1 Right-Angled Triangle (Bottom-Left Aligned)

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
```
Enter the number of rows: 5
* 
* * 
* * * 
* * * * 
* * * * * 
```

### 1.2 Right-Angled Triangle (Bottom-Right Aligned)

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            cout << "  ";
        }
        for (int j = 0; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
```

```
Enter the number of rows: 5
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
```

### 1.3 Inverted Right-Angled Triangle (Top-Left Aligned)

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

```
Enter the number of rows: 5
* * * * * 
* * * * 
* * * 
* * 
* 
```

### 1.4 Inverted Right-Angled Triangle (Top-Right Aligned)

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            cout << "  ";
        }
        for (int j = 0; j < n - i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
```

```
Enter the number of rows: 5
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
```

### 1.5 Solid Pyramid

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }
        for (int j = 0; j < 2 * i + 1; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
```

```
Enter the number of rows: 5
    *
   ***
  *****
 *******
*********
```

### 1.6 Inverted Pyramid

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = n; i >= 1; i--) {
        for (int j = 0; j < n - i; j++) {
            cout << " ";
        }
        for (int j = 0; j < 2 * i - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
```

```
Enter the number of rows: 5
*********
 *******
  *****
   ***
    *
```

---

## 2. Hollow Star Patterns

### 2.1 Hollow Right-Angled Triangle

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
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

```
Enter the number of rows: 5
* 
* * 
*   * 
*     * 
* * * * * 
```

### 2.2 Hollow Square

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

```
Enter the size of the square: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
```

### 2.3 Hollow Pyramid

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            cout << " ";
        }
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

```
Enter the number of rows: 5
    *
   * *
  *   *
 *     *
*********
```

### 2.4 Hollow Inverted Pyramid

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = n; i >= 1; i--) {
        for (int j = 0; j < n - i; j++) {
            cout << " ";
        }
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

```
Enter the number of rows: 5
*********
 *     *
  *   *
   * *
    *
```

---

## 3. Diamond Star Patterns

### 3.1 Solid Diamond (Optimized Formula Version)

```cpp
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    int n;
    cout << "Enter number of rows for half diamond: ";
    cin >> n;

    int totalRows = 2 * n - 1;
    int mid = n;

    for (int i = 1; i <= totalRows; i++) {
        int distanceFromMid = abs(i - mid);
        int stars = totalRows - 2 * distanceFromMid;
        int spaces = distanceFromMid;

        for (int j = 0; j < spaces; j++) cout << " ";
        for (int j = 0; j < stars; j++) cout << "*";
        cout << endl;
    }

    return 0;
}
```

```
Enter number of rows for half diamond: 5
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

### 3.2 Hollow Diamond

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows for half diamond: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            if (j == 1 || j == 2 * i - 1) cout << "*";
            else cout << " ";
        }
        cout << endl;
    }

    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            if (j == 1 || j == 2 * i - 1) cout << "*";
            else cout << " ";
        }
        cout << endl;
    }
    return 0;
}
```

```
Enter the number of rows for half diamond: 5
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

## 4. Number Patterns

### 4.1 Floyd's Triangle

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

```
Enter the number of rows: 5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
```

### 4.2 Pascal's Triangle

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        int val = 1;
        for (int j = 0; j < n - i - 1; j++) cout << " ";
        for (int j = 0; j <= i; j++) {
            cout << val << " ";
            val = val * (i - j) / (j + 1);
        }
        cout << endl;
    }
    return 0;
}
```

```
Enter the number of rows: 5
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 
```

### 4.3 Number Pyramid

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) cout << " ";
        for (int j = 1; j <= i; j++) cout << j;
        for (int j = i - 1; j >= 1; j--) cout << j;
        cout << endl;
    }
    return 0;
}
```

```
Enter the number of rows: 5
    1
   121
  12321
 1234321
123454321
```

### 4.4 Number Diamond

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows for half diamond: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) cout << " ";
        for (int j = 1; j <= i; j++) cout << j;
        for (int j = i - 1; j >= 1; j--) cout << j;
        cout << endl;
    }

    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= n - i; j++) cout << " ";
        for (int j = 1; j <= i; j++) cout << j;
        for (int j = i - 1; j >= 1; j--) cout << j;
        cout << endl;
    }

    return 0;
}
```

```
Enter the number of rows for half diamond: 5
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

### 4.5 Diamond with Numbers (Alternate Version)

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) cout << " ";
        for (int j = 1; j <= 2 * i - 1; j++) {
            if (j % 2 == 1) cout << i;
            else cout << " ";
        }
        cout << endl;
    }

    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= n - i; j++) cout << " ";
        for (int j = 1; j <= 2 * i - 1; j++) {
            if (j % 2 == 1) cout << i;
            else cout << " ";
        }
        cout << endl;
    }

    return 0;
}
```

```
Enter the number of rows: 5
    1
   2 2
  3   3
 4     4
5       5
 4     4
  3   3
   2 2
    1
```

---

## 5. Alphabet Patterns

### 5.1 Right-Angled Alphabet Triangle

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

```
Enter the number of rows: 5
A 
A B 
A B C 
A B C D 
A B C D E 
```

### 5.2 Alphabet Pyramid

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) cout << " ";

        char ch = 'A';
        for (int j = 1; j <= i; j++) {
            cout << ch;
            ch++;
        }

        ch -= 2;
        for (int j = 1; j <= i - 1; j++) {
            cout << ch;
            ch--;
        }
        cout << endl;
    }
    return 0;
}
```

```
Enter the number of rows: 5
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
```

### 5.3 Continuous Alphabet Triangle

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

```
Enter the number of rows: 5
A 
B C 
D E F 
G H I J 
K L M N O 
```

---

## 6. Special / Art Patterns

### 6.1 Butterfly Pattern

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows for half butterfly: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) cout << "*";
        for (int j = 1; j <= 2 * (n - i); j++) cout << " ";
        for (int j = 1; j <= i; j++) cout << "*";
        cout << endl;
    }

    for (int i = n; i >= 1; i--) {
        for (int j = 1; j <= i; j++) cout << "*";
        for (int j = 1; j <= 2 * (n - i); j++) cout << " ";
        for (int j = 1; j <= i; j++) cout << "*";
        cout << endl;
    }
    return 0;
}

```
```
Enter the number of rows for half butterfly: 5
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

### 6.2 Hourglass Pattern

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;

    for (int i = n; i >= 1; i--) {
        for (int j = 1; j <= n - i; j++) cout << " ";
        for (int j = 1; j <= 2 * i - 1; j++) cout << "*";
        cout << endl;
    }

    for (int i = 2; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) cout << " ";
        for (int j = 1; j <= 2 * i - 1; j++) cout << "*";
        cout << endl;
    }
    return 0;
}
```

```
Enter the number of rows: 5
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

### 6.3 Plus Sign Pattern

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the size (odd number): ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == (n + 1) / 2 || j == (n + 1) / 2) cout << "* ";
            else cout << "  ";
        }
        cout << endl;
    }
    return 0;
}
```

```
Enter the size (odd number): 5
    * 
    * 
* * * * * 
    * 
    * 
```

### 6.4 X Shape Pattern

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the size (odd number): ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == j || i + j == n + 1) cout << "* ";
            else cout << "  ";
        }
        cout << endl;
    }
    return 0;
}
```

```
Enter the size (odd number): 5
*       * 
  *   *   
    *     
  *   *   
*       * 
```

### 6.5 Swastik Pattern

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
            if (i == mid || j == mid) cout << "* ";
            else if (i == 1 && j > mid) cout << "* ";
            else if (i == n && j < mid) cout << "* ";
            else if (j == 1 && i < mid) cout << "* ";
            else if (j == n && i > mid) cout << "* ";
            else cout << "  ";
        }
        cout << endl;
    }
    return 0;
}
```

```
Enter the size (odd number >= 5): 5
*   * * * 
*   *     
* * * * * 
    *   * 
* * *   * 
```

### 6.6 Spiral Pattern

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
        for (int i = left; i <= right; i++) spiral[top][i] = num++;
        top++;

        for (int i = top; i <= bottom; i++) spiral[i][right] = num++;
        right--;

        if (top <= bottom) {
            for (int i = right; i >= left; i--) spiral[bottom][i] = num++;
            bottom--;
        }

        if (left <= right) {
            for (int i = bottom; i >= top; i--) spiral[i][left] = num++;
            left++;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%3d ", spiral[i][j]);
        }
        cout << endl;
    }

    return 0;
}
```

```
Enter the size: 5
  1   2   3   4   5 
 16  17  18  19   6 
 15  24  25  20   7 
 14  23  22  21   8 
 13  12  11  10   9 
```

### 6.7 Chessboard Pattern

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the size: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if ((i + j) % 2 == 0) cout << "* ";
            else cout << "  ";
        }
        cout << endl;
    }
    return 0;
}
```

```
Enter the size: 8
*   *   *   *   
  *   *   *   * 
*   *   *   *   
  *   *   *   * 
*   *   *   *   
  *   *   *   * 
*   *   *   *   
  *   *   *   * 
```

### 6.8 Heart Pattern

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the size (10-20 recommended): ";
    cin >> n;

    int mid = n / 2;

    for (int i = mid / 2; i <= mid; i += 2) {
        for (int j = 1; j < mid - i; j += 2) cout << " ";
        for (int j = 1; j <= i; j++) cout << "*";
        for (int j = 1; j <= mid - i; j++) cout << " ";
        for (int j = 1; j <= i; j++) cout << "*";
        cout << endl;
    }

    for (int i = mid; i >= 1; i--) {
        for (int j = i; j < mid; j++) cout << " ";
        for (int j = 1; j <= (i * 2) - 1; j++) cout << "*";
        cout << endl;
    }

    return 0;
}
```

```
Enter the size (10-20 recommended): 20
  *****     *****
 *******   *******
********* *********
*******************
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

### 6.9 Zigzag Pattern

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
            if (j == spaces + 1 || j == n - spaces) cout << "*";
            else cout << " ";
        }

        if (i <= n / 2) spaces++;
        else spaces--;

        cout << endl;
    }
    return 0;
}
```

```
Enter the number of rows: 7
*     *
 *   * 
  * *  
   *   
  * *  
 *   * 
*     *
```

---

## 7. Mathematical Patterns

### 7.1 Prime Number Triangle

```cpp
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;

    for (int i = 3; i <= sqrt(n); i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int n;
    cout << "Enter number of rows: ";
    cin >> n;

    vector<int> primes;
    int num = 2;

    while ((int)primes.size() < n * (n + 1) / 2) {
        if (isPrime(num)) primes.push_back(num);
        num++;
    }

    int idx = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << primes[idx++] << " ";
        }
        cout << endl;
    }

    return 0;
}
```

```
Enter number of rows: 5
2 
3 5 
7 11 13 
17 19 23 29 
31 37 41 43 47 
```

### 7.2 Fibonacci Triangle

```cpp
#include <iostream>
using namespace std;

int fibonacci(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int main() {
    int n;
    cout << "Enter number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cout << fibonacci(j) << " ";
        }
        cout << endl;
    }

    return 0;
}
```

```
Enter number of rows: 5
0 
0 1 
0 1 1 
0 1 1 2 
0 1 1 2 3 
```

### 7.3 Factorial Pattern

```cpp
#include <iostream>
using namespace std;

long long factorial(int n) {
    if (n <= 1) return 1;
    long long result = 1;
    for (int i = 2; i <= n; i++) result *= i;
    return result;
}

int main() {
    int n;
    cout << "Enter number of rows: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        cout << factorial(i) << endl;
    }

    return 0;
}
```

```
Enter number of rows: 5
1
2
6
24
120
```

---

## 8. Geometric / Grid Patterns

### 8.1 Wave Pattern

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cout << "Enter number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int wave = (int)(abs(sin((i + j) * 3.14159 / 4) * 2));
            if (wave > 1) cout << "* ";
            else cout << "  ";
        }
        cout << endl;
    }

    return 0;
}
```

```
Enter number of rows: 8
      *       
    *   *     
  *       *   
*           * 
  *       *   
    *   *     
      *       
    *   *     
```

### 8.2 Recursive Tree Pattern

```cpp
#include <iostream>
using namespace std;

void printTree(int height, int level = 0) {
    if (level >= height) return;

    int spaces = height - level - 1;
    int stars = 2 * level + 1;

    for (int i = 0; i < spaces; i++) cout << " ";
    for (int i = 0; i < stars; i++) cout << "*";
    cout << endl;

    printTree(height, level + 1);
}

int main() {
    int n;
    cout << "Enter tree height: ";
    cin >> n;

    printTree(n);

    return 0;
}
```

```
Enter tree height: 5
    *
   ***
  *****
 *******
*********
```

### 8.3 Manhattan-Distance (Memory-Efficient) Pattern

```cpp
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    int n;
    cout << "Enter pattern size: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int dist = abs(i - n / 2) + abs(j - n / 2);
            char symbol = (dist <= n / 3) ? '*' : ' ';
            cout << symbol << " ";
        }
        cout << endl;
    }

    return 0;
}
```

```
Enter pattern size: 7
      *       
    * * *     
  * * * * *   
* * * * * * * 
  * * * * *   
    * * *     
      *       
```

---

## 9. Optimization & Techniques

### 9.1 Complexity Summary

| Pattern Type | Typical Time | Typical Space |
| :--- | :--- | :--- |
| Simple printing patterns | O(n²) | O(1) |
| Patterns using 2D storage (like spiral matrix) | O(n²) | O(n²) |
| Recursive printing | O(n²) | O(n) |

### 9.2 Buffered Output (I/O Optimization)

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;

    string out;
    out.reserve(n * n * 3);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            out += ((i == j || i + j == n - 1) ? "* " : "  ");
        }
        out += '\n';
    }

    cout << out;
    return 0;
}
```

```
5
*       * 
  *   *   
    *     
  *   *   
*       * 
```

### 9.3 Single Loop Grid Traversal Trick

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int total = n * n;
    for (int k = 0; k < total; k++) {
        int i = k / n;
        int j = k % n;

        bool printStar = (i == 0 || i == n - 1 || j == 0 || j == n - 1);
        cout << (printStar ? "* " : "  ");

        if (j == n - 1) cout << '\n';
    }

    return 0;
}
```

```
5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
```

### 9.4 Template-Based Pattern Generator (Framework)

```cpp
#include <iostream>
using namespace std;

template<typename ConditionFunc>
void generatePattern(int n, ConditionFunc condition) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << (condition(i, j) ? "* " : "  ");
        }
        cout << endl;
    }
}

int main() {
    int n;
    cin >> n;

    generatePattern(n, [n](int i, int j) {
        return i == j || i + j == n - 1;
    });

    return 0;
}
```

```
5
*       * 
  *   *   
    *     
  *   *   
*       * 
```

### 9.5 Lookup-Table Optimization (Technique)

```cpp
#include <bitset>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<bitset<1000>> lut(n);    // assuming max n = 1000

    for (int i = 0; i < n; i++) {
        lut[i].set(i);              // main diagonal
        lut[i].set(n - i - 1);      // secondary diagonal
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << (lut[i][j] ? "* " : "  ");
        }
        cout << endl;
    }
}
```

```
5
*       * 
  *   *   
    *     
  *   *   
*       * 
```
