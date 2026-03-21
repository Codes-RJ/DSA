n = 5

print(f"Numbers from 1 to {n}:")
for i in range(1, n + 1):
    print(i, end=" ")
print()

print("Even or odd check:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
