rows = 5

print("Right triangle pattern:")
for i in range(1, rows + 1):
    print("* " * i)

print("\nNumber pattern:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
