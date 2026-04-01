# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # find the height of left subtree
        # find the height of right subtree
        # the difference should be less than or equal to 1
        # abs(height of left - height of right) <=1

        self.res = True
        def dfs(root):

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            if abs(dfs(root.left) - dfs(root.right))>1:
                self.res = False 
            return max(left, right)+1

        
        dfs(root)
        return self.res

        