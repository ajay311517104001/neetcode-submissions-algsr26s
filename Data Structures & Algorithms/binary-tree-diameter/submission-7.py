# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # optimal approach
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = float('-inf')
        def c_diameter(node):
            nonlocal maxi
            if not node:
                return 0

            left = c_diameter(node.left)
            right = c_diameter(node.right)
            maxi = max(maxi , left+right)
            return max(left,right)+1
        c_diameter(root)
        return maxi

