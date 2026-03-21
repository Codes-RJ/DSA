from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
print_list(head)

stack = []
stack.append(5)
stack.append(15)
print("Stack top:", stack[-1])

queue = deque([1, 2])
print("Queue front:", queue[0])
