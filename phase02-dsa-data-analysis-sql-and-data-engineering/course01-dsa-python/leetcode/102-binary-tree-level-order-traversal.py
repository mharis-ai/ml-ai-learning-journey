# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue = deque([root])
    
        while queue:
            level = []

            for _ in range(len(queue)):
                e = queue.popleft()
                level.append(e.val)
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)

            result.append(level)

        return result