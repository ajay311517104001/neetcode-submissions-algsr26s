# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def solve(node):
            if not node:
                return [0,0]
            
            left = solve(node.left)
            right = solve(node.right)

            withroot = node.val + left[1] + right[1]
            withoutroot = max(left[1],left[0]) + max(right[1],right[0])

            return [withroot , withoutroot]
        
        return max(solve(root))
        