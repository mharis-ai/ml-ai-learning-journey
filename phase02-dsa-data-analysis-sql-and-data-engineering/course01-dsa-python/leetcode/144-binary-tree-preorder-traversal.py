# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        result = []
        stack = []
        if not root:
            return result

        stack.append(root)
        while stack:
            e = stack.pop()
            result.append(e.val)
            if e.right:
                stack.append(e.right)
            if e.left:
                stack.append(e.left)
        
        return result