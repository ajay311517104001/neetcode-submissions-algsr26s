# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Binary tree maximum path sum
    #  get the one fat branch from left subtree + one fat branch from right subtree + root itself -> update to global max
    # do the same for left subtree and the right sub tree
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def getMaxBranch(node):
            if not node:
                return 0

            left = getMaxBranch(node.left)
            right = getMaxBranch(node.right)
            path = max(left,right) + node.val
            return max(path , 0) # clamping the negative value to zero

        maxi = float('-inf')
        def dfs(node):
            nonlocal maxi
            if not node:
                return 

            left = getMaxBranch(node.left)
            right = getMaxBranch(node.right)
            maxi = max(maxi , left + right + node.val)

            dfs(node.left) 
            dfs(node.right)



        dfs(root)
        return maxi
        

        
