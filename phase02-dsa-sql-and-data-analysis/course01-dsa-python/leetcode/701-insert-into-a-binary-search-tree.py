# Definition for a binary tree node.
class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
    def insertIntoBST(self, root, val: int):
        if not root:
            return TreeNode(val)
            
        temp = root
        while temp:
            if temp.val > val:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = TreeNode(val)
                    break

            else:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = TreeNode(val)
                    break

        return root