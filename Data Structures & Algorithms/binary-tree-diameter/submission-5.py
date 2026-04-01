# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # How I can optimize it from O(n)^2 to O(n)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # what is my input parameter and what is my output ?
        # Input : root
        # output : to return the max diameter
        diameter = 0
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0

            left= dfs(node.left)
            right= dfs(node.right)
            diameter = max(diameter , left+right)
            return max(left,right)+1
        dfs(root)
        return diameter

 
        

        
        