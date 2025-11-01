# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        if not root:
            return None

        count = 0
        result = None

        def dfs(node):
            nonlocal count, result
            if not node or result:
                return
            dfs(node.left)
            count += 1
            if count == k:
                result = node.val
                return 
            dfs(node.right)

        dfs(root)
        return result