# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return float('-inf')

        left = self.getbranch(root.left)
        right = self.getbranch(root.right)
        total_sum = left + right + root.val
        sub = max(self.maxPathSum(root.left), self.maxPathSum(root.right))
        return max(total_sum , sub)


    def getbranch(self, node):
        if not node:
            return 0
        left = self.getbranch(node.left)
        right = self.getbranch(node.right)
        total = max(left,right) + node.val
        return max(total, 0 )



        