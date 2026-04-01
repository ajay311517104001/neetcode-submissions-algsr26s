# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # optimal approach
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float('-inf')
        def dfs(node):
            nonlocal maxi
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right),0)
            maxi = max(maxi,left+right+node.val)
            return max(left, right) + node.val

        dfs(root)
        return maxi
        