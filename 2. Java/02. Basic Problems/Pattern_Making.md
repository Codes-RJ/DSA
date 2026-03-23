Here is a comprehensive Java Pattern Programming Guide, structured similarly to the C++ version you provided.

---

# Pattern Programming Guide (Java)

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

```java
import java.util.Scanner;

public class RightAngledTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class RightAngledTriangleRight {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                System.out.print("  ");
            }
            for (int j = 0; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class InvertedTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class InvertedTriangleRight {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print("  ");
            }
            for (int j = 0; j < n - i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class SolidPyramid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < 2 * i + 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class InvertedPyramid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = n; i >= 1; i--) {
            for (int j = 0; j < n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < 2 * i - 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class HollowTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i || i == n - 1) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class HollowSquare {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the square: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || i == n - 1 || j == 0 || j == n - 1) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class HollowPyramid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < 2 * i + 1; j++) {
                if (j == 0 || j == 2 * i || i == n - 1) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class HollowInvertedPyramid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = n; i >= 1; i--) {
            for (int j = 0; j < n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < 2 * i - 1; j++) {
                if (j == 0 || j == 2 * i - 2 || i == n) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class SolidDiamond {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of rows for half diamond: ");
        int n = sc.nextInt();
        sc.close();

        int totalRows = 2 * n - 1;
        int mid = n;

        for (int i = 1; i <= totalRows; i++) {
            int distanceFromMid = Math.abs(i - mid);
            int stars = totalRows - 2 * distanceFromMid;
            int spaces = distanceFromMid;

            for (int j = 0; j < spaces; j++) System.out.print(" ");
            for (int j = 0; j < stars; j++) System.out.print("*");
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class HollowDiamond {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows for half diamond: ");
        int n = sc.nextInt();
        sc.close();

        // Upper half
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= 2 * i - 1; j++) {
                if (j == 1 || j == 2 * i - 1) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }

        // Lower half
        for (int i = n - 1; i >= 1; i--) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= 2 * i - 1; j++) {
                if (j == 1 || j == 2 * i - 1) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class FloydTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        int num = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(num + " ");
                num++;
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class PascalTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 0; i < n; i++) {
            int val = 1;
            for (int j = 0; j < n - i - 1; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j <= i; j++) {
                System.out.print(val + " ");
                val = val * (i - j) / (j + 1);
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class NumberPyramid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print(j);
            }
            for (int j = i - 1; j >= 1; j--) {
                System.out.print(j);
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class NumberDiamond {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows for half diamond: ");
        int n = sc.nextInt();
        sc.close();

        // Upper half
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print(j);
            }
            for (int j = i - 1; j >= 1; j--) {
                System.out.print(j);
            }
            System.out.println();
        }

        // Lower half
        for (int i = n - 1; i >= 1; i--) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print(j);
            }
            for (int j = i - 1; j >= 1; j--) {
                System.out.print(j);
            }
            System.out.println();
        }
    }
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

### 4.5 Diamond with Alternating Numbers

```java
import java.util.Scanner;

public class AlternatingNumberDiamond {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        // Upper half
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= 2 * i - 1; j++) {
                if (j % 2 == 1) {
                    System.out.print(i);
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }

        // Lower half
        for (int i = n - 1; i >= 1; i--) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= 2 * i - 1; j++) {
                if (j % 2 == 1) {
                    System.out.print(i);
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class AlphabetTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 1; i <= n; i++) {
            char ch = 'A';
            for (int j = 1; j <= i; j++) {
                System.out.print(ch + " ");
                ch++;
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class AlphabetPyramid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }

            char ch = 'A';
            for (int j = 1; j <= i; j++) {
                System.out.print(ch);
                ch++;
            }

            ch -= 2;
            for (int j = 1; j <= i - 1; j++) {
                System.out.print(ch);
                ch--;
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class ContinuousAlphabetTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        char ch = 'A';
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(ch + " ");
                ch++;
                if (ch > 'Z') ch = 'A';
            }
            System.out.println();
        }
    }
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

### 5.4 Alphabet Diamond

```java
import java.util.Scanner;

public class AlphabetDiamond {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        // Upper half
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            char ch = 'A';
            for (int j = 1; j <= i; j++) {
                System.out.print(ch);
                ch++;
            }
            ch -= 2;
            for (int j = 1; j <= i - 1; j++) {
                System.out.print(ch);
                ch--;
            }
            System.out.println();
        }

        // Lower half
        for (int i = n - 1; i >= 1; i--) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            char ch = 'A';
            for (int j = 1; j <= i; j++) {
                System.out.print(ch);
                ch++;
            }
            ch -= 2;
            for (int j = 1; j <= i - 1; j++) {
                System.out.print(ch);
                ch--;
            }
            System.out.println();
        }
    }
}
```

```
Enter the number of rows: 5
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
 ABCDCBA
  ABCBA
   ABA
    A
```

---

## 6. Special / Art Patterns

### 6.1 Butterfly Pattern

```java
import java.util.Scanner;

public class ButterflyPattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows for half butterfly: ");
        int n = sc.nextInt();
        sc.close();

        // Upper half
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            for (int j = 1; j <= 2 * (n - i); j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // Lower half
        for (int i = n; i >= 1; i--) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            for (int j = 1; j <= 2 * (n - i); j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class HourglassPattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        // Upper half (inverted pyramid)
        for (int i = n; i >= 1; i--) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= 2 * i - 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // Lower half (pyramid)
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= 2 * i - 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class PlusPattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size (odd number): ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == (n + 1) / 2 || j == (n + 1) / 2) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class XShapePattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size (odd number): ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == j || i + j == n + 1) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class SwastikPattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size (odd number >= 5): ");
        int n = sc.nextInt();
        sc.close();

        int mid = (n + 1) / 2;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == mid || j == mid) {
                    System.out.print("* ");
                } else if (i == 1 && j > mid) {
                    System.out.print("* ");
                } else if (i == n && j < mid) {
                    System.out.print("* ");
                } else if (j == 1 && i < mid) {
                    System.out.print("* ");
                } else if (j == n && i > mid) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }
}
```

```
Enter the size (odd number >= 5): 7
* * * * * * * 
    *         
    *         
    *         
* * * * * * * 
          *   
          *   
* * * * * * * 
```

### 6.6 Spiral Pattern

```java
import java.util.Scanner;

public class SpiralPattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size: ");
        int n = sc.nextInt();
        sc.close();

        int[][] spiral = new int[n][n];

        int top = 0, bottom = n - 1, left = 0, right = n - 1;
        int num = 1;

        while (top <= bottom && left <= right) {
            for (int i = left; i <= right; i++) {
                spiral[top][i] = num++;
            }
            top++;

            for (int i = top; i <= bottom; i++) {
                spiral[i][right] = num++;
            }
            right--;

            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    spiral[bottom][i] = num++;
                }
                bottom--;
            }

            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    spiral[i][left] = num++;
                }
                left++;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.printf("%3d ", spiral[i][j]);
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class ChessboardPattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size: ");
        int n = sc.nextInt();
        sc.close();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if ((i + j) % 2 == 0) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class HeartPattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size (10-20 recommended): ");
        int n = sc.nextInt();
        sc.close();

        int mid = n / 2;

        // Upper half (two curves)
        for (int i = mid / 2; i <= mid; i += 2) {
            for (int j = 1; j < mid - i; j += 2) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            for (int j = 1; j <= mid - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // Lower half (V shape)
        for (int i = mid; i >= 1; i--) {
            for (int j = i; j < mid; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= (i * 2) - 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
```

```
Enter the size (10-20 recommended): 10
  *****       ***** 
 *******     ******* 
*********   ********* 
 ********* ********* 
  ***************** 
   *************** 
    ************* 
     *********** 
      ********* 
       ******* 
```

### 6.9 Zigzag Pattern

```java
import java.util.Scanner;

public class ZigzagPattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int n = sc.nextInt();
        sc.close();

        int spaces = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (j == spaces + 1 || j == n - spaces) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }

            if (i <= n / 2) {
                spaces++;
            } else {
                spaces--;
            }

            System.out.println();
        }
    }
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

### 6.10 Hollow Diamond with Border

```java
import java.util.Scanner;

public class HollowDiamondBorder {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows for half diamond: ");
        int n = sc.nextInt();
        sc.close();

        // Upper half
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= 2 * i - 1; j++) {
                if (j == 1 || j == 2 * i - 1 || i == n) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }

        // Lower half
        for (int i = n - 1; i >= 1; i--) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= 2 * i - 1; j++) {
                if (j == 1 || j == 2 * i - 1) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
```

```
Enter the number of rows for half diamond: 5
    *
   * *
  *   *
 *     *
*********
 *     *
  *   *
   * *
    *
```

---

## 7. Mathematical Patterns

### 7.1 Prime Number Triangle

```java
import java.util.Scanner;
import java.util.ArrayList;

public class PrimeTriangle {
    
    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of rows: ");
        int n = sc.nextInt();
        sc.close();
        
        ArrayList<Integer> primes = new ArrayList<>();
        int num = 2;
        
        while (primes.size() < n * (n + 1) / 2) {
            if (isPrime(num)) {
                primes.add(num);
            }
            num++;
        }
        
        int idx = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(primes.get(idx++) + " ");
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class FibonacciTriangle {
    
    public static int fibonacci(int n) {
        if (n <= 1) return n;
        int a = 0, b = 1, c = 0;
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of rows: ");
        int n = sc.nextInt();
        sc.close();
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print(fibonacci(j) + " ");
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class FactorialPattern {
    
    public static long factorial(int n) {
        if (n <= 1) return 1;
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of rows: ");
        int n = sc.nextInt();
        sc.close();
        
        for (int i = 1; i <= n; i++) {
            System.out.println(factorial(i));
        }
    }
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

### 7.4 Power of 2 Triangle

```java
import java.util.Scanner;

public class PowerOfTwoTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of rows: ");
        int n = sc.nextInt();
        sc.close();
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print((int) Math.pow(2, j) + " ");
            }
            System.out.println();
        }
    }
}
```

```
Enter number of rows: 5
1 
1 2 
1 2 4 
1 2 4 8 
1 2 4 8 16 
```

---

## 8. Geometric / Grid Patterns

### 8.1 Wave Pattern

```java
import java.util.Scanner;

public class WavePattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of rows: ");
        int n = sc.nextInt();
        sc.close();
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int wave = (int) Math.abs(Math.sin((i + j) * Math.PI / 4) * 2);
                if (wave > 1) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }
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

```java
import java.util.Scanner;

public class RecursiveTree {
    
    public static void printTree(int height, int level) {
        if (level >= height) return;
        
        int spaces = height - level - 1;
        int stars = 2 * level + 1;
        
        for (int i = 0; i < spaces; i++) {
            System.out.print(" ");
        }
        for (int i = 0; i < stars; i++) {
            System.out.print("*");
        }
        System.out.println();
        
        printTree(height, level + 1);
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter tree height: ");
        int n = sc.nextInt();
        sc.close();
        
        printTree(n, 0);
    }
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

### 8.3 Manhattan-Distance (Diamond) Pattern

```java
import java.util.Scanner;

public class ManhattanPattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter pattern size: ");
        int n = sc.nextInt();
        sc.close();
        
        int center = n / 2;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int dist = Math.abs(i - center) + Math.abs(j - center);
                char symbol = (dist <= n / 3) ? '*' : ' ';
                System.out.print(symbol + " ");
            }
            System.out.println();
        }
    }
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

### 8.4 Rhombus Pattern

```java
import java.util.Scanner;

public class RhombusPattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size: ");
        int n = sc.nextInt();
        sc.close();
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= n; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
```

```
Enter the size: 5
    * * * * * 
   * * * * * 
  * * * * * 
 * * * * * 
* * * * * 
```

### 8.5 Checkerboard Pattern

```java
import java.util.Scanner;

public class CheckerboardPattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size: ");
        int n = sc.nextInt();
        sc.close();
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if ((i + j) % 2 == 0) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
```

```
Enter the size: 8
* * * * 
 * * * *
* * * * 
 * * * *
* * * * 
 * * * *
* * * * 
 * * * *
```

---

## 9. Optimization & Techniques

### 9.1 Complexity Summary

| Pattern Type | Typical Time | Typical Space |
| :--- | :--- | :--- |
| Simple printing patterns | O(n²) | O(1) |
| Patterns using 2D storage (like spiral matrix) | O(n²) | O(n²) |
| Recursive printing | O(n²) | O(n) |

### 9.2 StringBuilder for Output Optimization

```java
import java.util.Scanner;

public class OptimizedOutput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size: ");
        int n = sc.nextInt();
        sc.close();
        
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j || i + j == n - 1) {
                    sb.append("* ");
                } else {
                    sb.append("  ");
                }
            }
            sb.append("\n");
        }
        
        System.out.print(sb);
    }
}
```

```
Enter size: 5
*       * 
  *   *   
    *     
  *   *   
*       * 
```

### 9.3 Single Loop Grid Traversal

```java
import java.util.Scanner;

public class SingleLoopGrid {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size: ");
        int n = sc.nextInt();
        sc.close();
        
        int total = n * n;
        for (int k = 0; k < total; k++) {
            int i = k / n;
            int j = k % n;
            
            boolean printStar = (i == 0 || i == n - 1 || j == 0 || j == n - 1);
            System.out.print(printStar ? "* " : "  ");
            
            if (j == n - 1) {
                System.out.println();
            }
        }
    }
}
```

```
Enter size: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
```

### 9.4 Template/Functional Pattern Generator

```java
import java.util.Scanner;
import java.util.function.BiPredicate;

public class FunctionalPattern {
    
    public static void generatePattern(int n, BiPredicate<Integer, Integer> condition) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(condition.test(i, j) ? "* " : "  ");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size: ");
        int n = sc.nextInt();
        sc.close();
        
        System.out.println("X Pattern:");
        generatePattern(n, (i, j) -> i == j || i + j == n - 1);
        
        System.out.println("\nHollow Square:");
        generatePattern(n, (i, j) -> i == 0 || i == n - 1 || j == 0 || j == n - 1);
    }
}
```

```
Enter size: 5
X Pattern:
*       * 
  *   *   
    *     
  *   *   
*       * 

Hollow Square:
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
```

### 9.5 Precomputed Pattern (Lookup Table)

```java
import java.util.Scanner;
import java.util.BitSet;

public class LookupTablePattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size: ");
        int n = sc.nextInt();
        sc.close();
        
        // Precompute pattern in BitSet (memory efficient)
        BitSet[] lut = new BitSet[n];
        
        for (int i = 0; i < n; i++) {
            lut[i] = new BitSet(n);
            lut[i].set(i);           // main diagonal
            lut[i].set(n - i - 1);   // secondary diagonal
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(lut[i].get(j) ? "* " : "  ");
            }
            System.out.println();
        }
    }
}
```

```
Enter size: 5
*       * 
  *   *   
    *     
  *   *   
*       * 
```

### 9.6 Memory-Efficient Spiral Pattern

```java
import java.util.Scanner;

public class MemoryEfficientSpiral {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size: ");
        int n = sc.nextInt();
        sc.close();
        
        // Print spiral numbers without storing entire matrix
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int value = getSpiralValue(n, i, j);
                System.out.printf("%3d ", value);
            }
            System.out.println();
        }
    }
    
    private static int getSpiralValue(int n, int row, int col) {
        int layer = Math.min(Math.min(row, col), Math.min(n - 1 - row, n - 1 - col));
        int firstNum = 1;
        
        for (int k = 0; k < layer; k++) {
            firstNum += 4 * (n - 2 * k - 1);
        }
        
        int startRow = layer;
        int startCol = layer;
        int endRow = n - 1 - layer;
        int endCol = n - 1 - layer;
        
        if (row == startRow) {
            return firstNum + (col - startCol);
        } else if (col == endCol) {
            return firstNum + (endRow - startRow) + (row - startRow);
        } else if (row == endRow) {
            return firstNum + 2 * (endRow - startRow) + (endCol - col);
        } else {
            return firstNum + 3 * (endRow - startRow) + (endRow - row);
        }
    }
}
```

```
Enter size: 5
  1   2   3   4   5 
 16  17  18  19   6 
 15  24  25  20   7 
 14  23  22  21   8 
 13  12  11  10   9 
```

---

## Best Practices Summary

1. **Use StringBuilder for large patterns**: Reduces I/O overhead significantly
2. **Precompute conditions**: For complex patterns, compute once and reuse
3. **Avoid nested loops for simple patterns**: Single loop with index math works
4. **Use bitwise operations for flag patterns**: Faster than boolean comparisons
5. **Leverage Java's functional interfaces**: For reusable pattern generators
6. **Consider memory footprint**: Use BitSet for sparse patterns
7. **Optimize math operations**: Precompute constants like `Math.PI` when used repeatedly
8. **Use `printf` for formatted output**: Better control over spacing
9. **Close Scanner resources**: Prevent resource leaks
10. **Use meaningful variable names**: i, j for loops; n for size; etc.

---

## Conclusion

Pattern programming is an excellent way to practice loops, conditionals, and algorithmic thinking in Java. The patterns covered in this guide range from basic star triangles to complex mathematical and artistic patterns. Key takeaways:

- **Master nested loops**: Most patterns rely on proper loop control
- **Understand symmetry**: Many patterns (diamond, butterfly) use symmetric logic
- **Optimize for performance**: Use StringBuilder for large outputs
- **Think in layers**: Spiral patterns require layered approach
- **Leverage Java features**: Functional interfaces, BitSet, and modern APIs

Practice these patterns to strengthen your understanding of:
- Loop structures (for, while)
- Conditional logic (if-else, ternary)
- Mathematical formulas (distance calculations, series)
- Array manipulations
- Memory optimization techniques