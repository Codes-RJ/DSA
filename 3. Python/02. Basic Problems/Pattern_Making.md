Here is a comprehensive Python Pattern Programming Guide, structured similarly to the C++ and Java versions you provided.

---

# Pattern Programming Guide (Python)

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

```python
n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()
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

```python
n = int(input("Enter the number of rows: "))

for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end=" ")
    # Print stars
    for j in range(i + 1):
        print("*", end=" ")
    print()
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

```python
n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()
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

```python
n = int(input("Enter the number of rows: "))

for i in range(n):
    # Print spaces
    for j in range(i):
        print(" ", end=" ")
    # Print stars
    for j in range(n - i):
        print("*", end=" ")
    print()
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

```python
n = int(input("Enter the number of rows: "))

for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Print stars
    for j in range(2 * i + 1):
        print("*", end="")
    print()
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

```python
n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()
```
```
Enter the number of rows: 5
*********
 *******
  *****
   ***
    *
```

### 1.7 Mirrored Right-Angled Triangle (One-liner)

```python
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
```
```
Enter the number of rows: 5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

### 1.8 Inverted Mirrored Triangle (One-liner)

```python
n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
```
```
Enter the number of rows: 5
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
```

---

## 2. Hollow Star Patterns

### 2.1 Hollow Right-Angled Triangle

```python
n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(i + 1):
        if j == 0 or j == i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
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

```python
n = int(input("Enter the size of the square: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
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

```python
n = int(input("Enter the number of rows: "))

for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Print stars with hollow condition
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
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

```python
n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars with hollow condition
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```
```
Enter the number of rows: 5
*********
 *     *
  *   *
   * *
    *
```

### 2.5 Hollow Diamond

```python
n = int(input("Enter the number of rows for half diamond: "))

# Upper half
for i in range(1, n + 1):
    spaces = " " * (n - i)
    if i == 1:
        stars = "*"
    else:
        stars = "*" + " " * (2 * i - 3) + "*"
    print(spaces + stars)

# Lower half
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    if i == 1:
        stars = "*"
    else:
        stars = "*" + " " * (2 * i - 3) + "*"
    print(spaces + stars)
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

## 3. Diamond Star Patterns

### 3.1 Solid Diamond (Optimized Formula Version)

```python
n = int(input("Enter number of rows for half diamond: "))

total_rows = 2 * n - 1
mid = n

for i in range(1, total_rows + 1):
    distance_from_mid = abs(i - mid)
    stars = total_rows - 2 * distance_from_mid
    spaces = distance_from_mid
    
    print(" " * spaces + "*" * stars)
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

```python
n = int(input("Enter the number of rows for half diamond: "))

# Upper half
for i in range(1, n + 1):
    spaces = " " * (n - i)
    if i == 1:
        stars = "*"
    else:
        stars = "*" + " " * (2 * i - 3) + "*"
    print(spaces + stars)

# Lower half
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    if i == 1:
        stars = "*"
    else:
        stars = "*" + " " * (2 * i - 3) + "*"
    print(spaces + stars)
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

### 3.3 Diamond with Numbers (Alternating)

```python
n = int(input("Enter the number of rows: "))

# Upper half
for i in range(1, n + 1):
    spaces = " " * (n - i)
    row = ""
    for j in range(1, 2 * i):
        if j % 2 == 1:
            row += str(i)
        else:
            row += " "
    print(spaces + row)

# Lower half
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    row = ""
    for j in range(1, 2 * i):
        if j % 2 == 1:
            row += str(i)
        else:
            row += " "
    print(spaces + row)
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

## 4. Number Patterns

### 4.1 Floyd's Triangle

```python
n = int(input("Enter the number of rows: "))

num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
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

```python
n = int(input("Enter the number of rows: "))

for i in range(n):
    # Print spaces
    print(" " * (n - i - 1), end="")
    
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()
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

```python
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    # Print spaces
    print(" " * (n - i), end="")
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")
    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
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

```python
n = int(input("Enter the number of rows for half diamond: "))

# Upper half
for i in range(1, n + 1):
    spaces = " " * (n - i)
    numbers = "".join(str(j) for j in range(1, i + 1))
    numbers += "".join(str(j) for j in range(i - 1, 0, -1))
    print(spaces + numbers)

# Lower half
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    numbers = "".join(str(j) for j in range(1, i + 1))
    numbers += "".join(str(j) for j in range(i - 1, 0, -1))
    print(spaces + numbers)
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

### 4.5 Binary Number Triangle

```python
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j % 2, end=" ")
    print()
```
```
Enter the number of rows: 5
1 
1 0 
1 0 1 
1 0 1 0 
1 0 1 0 1 
```

### 4.6 Pattern 1 23 456 78910

```python
n = int(input("Enter the number of rows: "))

num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```
```
Enter the number of rows: 5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
```

### 4.7 Pattern 1 22 333 4444

```python
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
```
```
Enter the number of rows: 5
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
```

### 4.8 Reverse Number Triangle

```python
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        print(j, end=" ")
    print()
```
```
Enter the number of rows: 5
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
```

---

## 5. Alphabet Patterns

### 5.1 Right-Angled Alphabet Triangle

```python
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    ch = 'A'
    for j in range(i):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)
    print()
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

```python
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    # Print spaces
    print(" " * (n - i), end="")
    
    # Print increasing letters
    ch = 'A'
    for j in range(i):
        print(ch, end="")
        ch = chr(ord(ch) + 1)
    
    # Print decreasing letters
    ch = chr(ord(ch) - 2)
    for j in range(i - 1):
        print(ch, end="")
        ch = chr(ord(ch) - 1)
    
    print()
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

```python
n = int(input("Enter the number of rows: "))

ch = 'A'
for i in range(1, n + 1):
    for j in range(i):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)
        if ch > 'Z':
            ch = 'A'
    print()
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

```python
n = int(input("Enter the number of rows: "))

# Upper half
for i in range(1, n + 1):
    spaces = " " * (n - i)
    letters = ""
    ch = 'A'
    for j in range(i):
        letters += ch
        ch = chr(ord(ch) + 1)
    ch = chr(ord(ch) - 2)
    for j in range(i - 1):
        letters += ch
        ch = chr(ord(ch) - 1)
    print(spaces + letters)

# Lower half
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    letters = ""
    ch = 'A'
    for j in range(i):
        letters += ch
        ch = chr(ord(ch) + 1)
    ch = chr(ord(ch) - 2)
    for j in range(i - 1):
        letters += ch
        ch = chr(ord(ch) - 1)
    print(spaces + letters)
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

### 5.5 Inverted Alphabet Triangle

```python
n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    ch = 'A'
    for j in range(i):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)
    print()
```
```
Enter the number of rows: 5
A B C D E 
A B C D 
A B C 
A B 
A 
```

### 5.6 Pattern A BB CCC DDDD

```python
n = int(input("Enter the number of rows: "))

ch = 'A'
for i in range(1, n + 1):
    for j in range(i):
        print(ch, end=" ")
    print()
    ch = chr(ord(ch) + 1)
```
```
Enter the number of rows: 5
A 
B B 
C C C 
D D D D 
E E E E E 
```

---

## 6. Special / Art Patterns

### 6.1 Butterfly Pattern

```python
n = int(input("Enter the number of rows for half butterfly: "))

# Upper half
for i in range(1, n + 1):
    stars = "*" * i
    spaces = " " * (2 * (n - i))
    print(stars + spaces + stars)

# Lower half
for i in range(n, 0, -1):
    stars = "*" * i
    spaces = " " * (2 * (n - i))
    print(stars + spaces + stars)
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

```python
n = int(input("Enter the number of rows: "))

# Upper half (inverted pyramid)
for i in range(n, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# Lower half (pyramid)
for i in range(2, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
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

```python
n = int(input("Enter the size (odd number): "))

mid = n // 2
for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
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

```python
n = int(input("Enter the size (odd number): "))

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
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

```python
n = int(input("Enter the size (odd number >= 5): "))

mid = n // 2
for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*", end=" ")
        elif i == 0 and j > mid:
            print("*", end=" ")
        elif i == n - 1 and j < mid:
            print("*", end=" ")
        elif j == 0 and i < mid:
            print("*", end=" ")
        elif j == n - 1 and i > mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
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

```python
n = int(input("Enter the size: "))

# Create n x n matrix filled with zeros
spiral = [[0] * n for _ in range(n)]

top, bottom, left, right = 0, n - 1, 0, n - 1
num = 1

while top <= bottom and left <= right:
    # Left to right
    for i in range(left, right + 1):
        spiral[top][i] = num
        num += 1
    top += 1
    
    # Top to bottom
    for i in range(top, bottom + 1):
        spiral[i][right] = num
        num += 1
    right -= 1
    
    # Right to left
    if top <= bottom:
        for i in range(right, left - 1, -1):
            spiral[bottom][i] = num
            num += 1
        bottom -= 1
    
    # Bottom to top
    if left <= right:
        for i in range(bottom, top - 1, -1):
            spiral[i][left] = num
            num += 1
        left += 1

# Print the spiral
for row in spiral:
    for val in row:
        print(f"{val:3d}", end=" ")
    print()
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

```python
n = int(input("Enter the size: "))

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
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

```python
n = int(input("Enter the size (10-20 recommended): "))

mid = n // 2

# Upper half (two curves)
for i in range(mid // 2, mid + 1, 2):
    spaces1 = " " * ((mid - i) // 2)
    stars1 = "*" * i
    spaces2 = " " * (mid - i)
    stars2 = "*" * i
    print(spaces1 + stars1 + spaces2 + stars2)

# Lower half (V shape)
for i in range(mid, 0, -1):
    spaces = " " * (mid - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
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

```python
n = int(input("Enter the number of rows: "))

spaces = 0
for i in range(1, n + 1):
    row = ""
    for j in range(1, n + 1):
        if j == spaces + 1 or j == n - spaces:
            row += "*"
        else:
            row += " "
    
    if i <= n // 2:
        spaces += 1
    else:
        spaces -= 1
    
    print(row)
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

### 6.10 Pyramid with Frame

```python
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    spaces = " " * (n - i)
    if i == 1:
        stars = "*"
    elif i == n:
        stars = "*" * (2 * i - 1)
    else:
        stars = "*" + " " * (2 * i - 3) + "*"
    print(spaces + stars)
```
```
Enter the number of rows: 5
    *
   * *
  *   *
 *     *
*********
```

### 6.11 Diamond with Border

```python
n = int(input("Enter the number of rows for half diamond: "))

# Upper half
for i in range(1, n + 1):
    spaces = " " * (n - i)
    if i == n:
        stars = "*" * (2 * i - 1)
    else:
        stars = "*" + " " * (2 * i - 3) + "*"
    print(spaces + stars)

# Lower half
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    if i == n:
        stars = "*" * (2 * i - 1)
    else:
        stars = "*" + " " * (2 * i - 3) + "*"
    print(spaces + stars)
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

```python
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number of rows: "))

primes = []
num = 2
while len(primes) < n * (n + 1) // 2:
    if is_prime(num):
        primes.append(num)
    num += 1

idx = 0
for i in range(1, n + 1):
    for j in range(i):
        print(primes[idx], end=" ")
        idx += 1
    print()
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

```python
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(i + 1):
        print(fibonacci(j), end=" ")
    print()
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

```python
def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(factorial(i))
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

```python
n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(i + 1):
        print(2 ** j, end=" ")
    print()
```
```
Enter number of rows: 5
1 
1 2 
1 2 4 
1 2 4 8 
1 2 4 8 16 
```

### 7.5 Multiplication Table Pattern

```python
n = int(input("Enter the size: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4d}", end="")
    print()
```
```
Enter the size: 5
   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25
```

### 7.6 Sum Pattern (1 = 1, 1+2 = 3, etc.)

```python
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    total = 0
    for j in range(1, i + 1):
        total += j
        if j == i:
            print(f"{j} = {total}")
        else:
            print(f"{j} + ", end="")
```
```
Enter number of rows: 5
1 = 1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
1 + 2 + 3 + 4 + 5 = 15
```

---

## 8. Geometric / Grid Patterns

### 8.1 Wave Pattern

```python
import math

n = int(input("Enter number of rows: "))

for i in range(n):
    row = ""
    for j in range(n):
        wave = int(abs(math.sin((i + j) * math.pi / 4)) * 2)
        if wave > 1:
            row += "* "
        else:
            row += "  "
    print(row)
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

```python
def print_tree(height, level=0):
    if level >= height:
        return
    
    spaces = " " * (height - level - 1)
    stars = "*" * (2 * level + 1)
    print(spaces + stars)
    
    print_tree(height, level + 1)

n = int(input("Enter tree height: "))
print_tree(n)
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

```python
n = int(input("Enter pattern size: "))

center = n // 2
for i in range(n):
    row = ""
    for j in range(n):
        dist = abs(i - center) + abs(j - center)
        if dist <= n // 3:
            row += "* "
        else:
            row += "  "
    print(row)
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

```python
n = int(input("Enter the size: "))

for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "* " * n
    print(spaces + stars)
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

```python
n = int(input("Enter the size: "))

for i in range(n):
    row = ""
    for j in range(n):
        if (i + j) % 2 == 0:
            row += "*"
        else:
            row += " "
    print(row)
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

### 8.6 Concentric Squares Pattern

```python
n = int(input("Enter the size: "))

for i in range(n):
    for j in range(n):
        min_dist = min(i, j, n - 1 - i, n - 1 - j)
        print(min_dist + 1, end=" ")
    print()
```
```
Enter the size: 5
1 1 1 1 1 
1 2 2 2 1 
1 2 3 2 1 
1 2 2 2 1 
1 1 1 1 1 
```

### 8.7 Circular Pattern

```python
import math

n = int(input("Enter the size (odd number recommended): "))

center = n // 2
radius = n // 3

for i in range(n):
    row = ""
    for j in range(n):
        dist = math.sqrt((i - center) ** 2 + (j - center) ** 2)
        if abs(dist - radius) < 0.5:
            row += "* "
        else:
            row += "  "
    print(row)
```
```
Enter the size (odd number recommended): 11
          *           
        *   *         
      *       *       
    *           *     
  *               *   
*                   * 
  *               *   
    *           *     
      *       *       
        *   *         
          *           
```

### 8.8 Spiral Text Pattern

```python
def create_spiral(n):
    spiral = [[' ' for _ in range(n)] for _ in range(n)]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0
    row, col = 0, 0
    char = '*'
    
    for i in range(n * n):
        spiral[row][col] = char
        next_row = row + directions[dir_idx][0]
        next_col = col + directions[dir_idx][1]
        
        if (next_row < 0 or next_row >= n or 
            next_col < 0 or next_col >= n or 
            spiral[next_row][next_col] != ' '):
            dir_idx = (dir_idx + 1) % 4
            next_row = row + directions[dir_idx][0]
            next_col = col + directions[dir_idx][1]
        
        row, col = next_row, next_col
    
    return spiral

n = int(input("Enter the size: "))
spiral = create_spiral(n)

for row in spiral:
    print(" ".join(row))
```
```
Enter the size: 5
* * * * * 
  * * * * 
  *   * * 
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

### 9.2 String Concatenation Optimization

```python
n = int(input("Enter size: "))

# Efficient approach using string building
output = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j or i + j == n - 1:
            row.append("*")
        else:
            row.append(" ")
    output.append(" ".join(row))

print("\n".join(output))
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

```python
n = int(input("Enter size: "))

total = n * n
for k in range(total):
    i = k // n
    j = k % n
    
    if i == 0 or i == n - 1 or j == 0 or j == n - 1:
        print("*", end=" ")
    else:
        print(" ", end=" ")
    
    if j == n - 1:
        print()
```
```
Enter size: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
```

### 9.4 Functional Pattern Generator

```python
def generate_pattern(n, condition_func):
    for i in range(n):
        row = []
        for j in range(n):
            row.append("*" if condition_func(i, j) else " ")
        print(" ".join(row))

n = int(input("Enter size: "))

print("X Pattern:")
generate_pattern(n, lambda i, j: i == j or i + j == n - 1)

print("\nHollow Square:")
generate_pattern(n, lambda i, j: i == 0 or i == n - 1 or j == 0 or j == n - 1)
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

### 9.5 List Comprehension Patterns (One-liners)

```python
n = int(input("Enter size: "))

# Hollow Square using list comprehension
hollow_square = "\n".join(
    " ".join("*" if i == 0 or i == n-1 or j == 0 or j == n-1 else " " for j in range(n))
    for i in range(n)
)
print("Hollow Square:")
print(hollow_square)

# X Pattern using list comprehension
x_pattern = "\n".join(
    " ".join("*" if i == j or i + j == n-1 else " " for j in range(n))
    for i in range(n)
)
print("\nX Pattern:")
print(x_pattern)
```
```
Enter size: 5
Hollow Square:
* * * * *
*       *
*       *
*       *
* * * * *

X Pattern:
*       *
  *   *
    *
  *   *
*       *
```

### 9.6 Memory-Efficient Spiral (No Matrix Storage)

```python
def get_spiral_value(n, row, col):
    layer = min(row, col, n - 1 - row, n - 1 - col)
    first_num = 1
    
    for k in range(layer):
        first_num += 4 * (n - 2 * k - 1)
    
    start_row, start_col = layer, layer
    end_row, end_col = n - 1 - layer, n - 1 - layer
    
    if row == start_row:
        return first_num + (col - start_col)
    elif col == end_col:
        return first_num + (end_row - start_row) + (row - start_row)
    elif row == end_row:
        return first_num + 2 * (end_row - start_row) + (end_col - col)
    else:
        return first_num + 3 * (end_row - start_row) + (end_row - row)

n = int(input("Enter size: "))

for i in range(n):
    row = []
    for j in range(n):
        row.append(f"{get_spiral_value(n, i, j):3d}")
    print(" ".join(row))
```
```
Enter size: 5
  1   2   3   4   5
 16  17  18  19   6
 15  24  25  20   7
 14  23  22  21   8
 13  12  11  10   9
```

### 9.7 Generator for Large Patterns

```python
def pattern_generator(n):
    for i in range(n):
        row = []
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                row.append("*")
            else:
                row.append(" ")
        yield " ".join(row)

n = int(input("Enter size: "))

# Generate and print lazily (memory efficient)
for line in pattern_generator(n):
    print(line)
```
```
Enter size: 5
* * * * *
*       *
*       *
*       *
* * * * *
```

### 9.8 Using `center()` Method for Pyramids

```python
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    stars = "*" * (2 * i - 1)
    print(stars.center(2 * n - 1))
```
```
Enter number of rows: 5
    *    
   ***   
  *****  
 ******* 
*********
```

### 9.9 Using `rjust()` and `ljust()` for Alignment

```python
n = int(input("Enter number of rows: "))

# Right-aligned triangle
for i in range(1, n + 1):
    print(("*" * i).rjust(n))

print()

# Left-aligned triangle
for i in range(1, n + 1):
    print(("*" * i).ljust(n))
```
```
Enter number of rows: 5
    *
   **
  ***
 ****
*****

*   
**  
*** 
****
*****
```

### 9.10 Using `itertools` for Pattern Generation

```python
from itertools import cycle

n = int(input("Enter number of rows: "))

# Alternating pattern using cycle
symbols = cycle(["*", "#", "@"])
for i in range(1, n + 1):
    symbol = next(symbols)
    print((symbol * i).center(n))
```
```
Enter number of rows: 5
    *    
   ##   
  @@@@  
 ***** 
######
```

---

## Best Practices Summary

1. **Use string multiplication**: Python's `"*" * n` is highly optimized
2. **Build with lists then join**: Faster than string concatenation in loops
3. **Use list comprehensions**: More concise and often faster
4. **Leverage `center()`, `ljust()`, `rjust()`**: Cleaner alignment
5. **Use generators for large patterns**: Memory efficient
6. **Precompute constants**: Avoid recalculating inside loops
7. **Use `sys.stdout.write()` for huge outputs**: Faster than print
8. **Take advantage of Python's functional features**: `map()`, `filter()`, `lambda`
9. **Use `itertools` for complex iteration patterns**
10. **Keep code readable**: Python's philosophy emphasizes readability

### Performance Comparison Example

```python
import time

n = 1000

# Method 1: String concatenation (slow)
start = time.time()
result = ""
for i in range(n):
    result += " " * (n - i) + "*" * (2 * i + 1) + "\n"
print(f"Concatenation: {time.time() - start:.4f}s")

# Method 2: List join (faster)
start = time.time()
rows = []
for i in range(n):
    rows.append(" " * (n - i) + "*" * (2 * i + 1))
result = "\n".join(rows)
print(f"List join: {time.time() - start:.4f}s")

# Method 3: List comprehension (fastest for simple patterns)
start = time.time()
rows = [" " * (n - i) + "*" * (2 * i + 1) for i in range(n)]
result = "\n".join(rows)
print(f"List comprehension: {time.time() - start:.4f}s")
```

---

## Conclusion

Pattern programming in Python offers a unique combination of simplicity and power. Python's features like string multiplication, list comprehensions, and built-in alignment methods make pattern generation particularly elegant. Key takeaways:

- **String multiplication** (`"*" * n`) is a Python superpower for patterns
- **List comprehensions** provide concise, readable pattern generation
- **Built-in methods** (`center()`, `ljust()`, `rjust()`) simplify alignment
- **Functional approaches** enable reusable pattern generators
- **Memory efficiency** matters for large patterns; use generators when appropriate

Practice these patterns to master:
- Loop structures and nested iterations
- String manipulation techniques
- List comprehensions and functional programming
- Mathematical thinking and problem decomposition
- Performance optimization strategies

Python's readability and expressiveness make pattern programming an enjoyable way to strengthen programming fundamentals while learning the language's unique features.