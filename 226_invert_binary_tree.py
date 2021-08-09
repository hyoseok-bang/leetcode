# Pythonic way
def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root
    return None


# BFS with iteration
import collections 

def invertTree(root):
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        # top-down sawp from the parent root
        if node:
            node.left, node.right = node.right, node.left
            # append new node
            queue.append(node.left)
            queue.append(node.right)
    
    return root