# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    longest = 0
    def diameterOfBinaryTree(self, root):
        def dfs(node):
            if not node:
                return -1
            # Update the length to the leaf node
            left = dfs(node.left)
            right = dfs(node.right)
            # Update the length of the longest path
            self.longest = max(self.longest, left + right + 2)
            
            return max(left, right) + 1  # Return the longest length btw left and right
        
        dfs(root)
        return self.longest