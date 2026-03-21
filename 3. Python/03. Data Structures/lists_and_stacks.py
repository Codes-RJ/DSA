def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


numbers = [10, 20, 30, 40, 50]
target = 30

print("Numbers:", numbers)
print("Index of target:", linear_search(numbers, target))

stack = []
stack.append(100)
stack.append(200)
print("Stack after push:", stack)
print("Popped value:", stack.pop())
