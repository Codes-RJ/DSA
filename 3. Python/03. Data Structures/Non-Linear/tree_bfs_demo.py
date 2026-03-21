from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs(root):
    if root is None:
        return

    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.value, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    print()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

bfs(root)
