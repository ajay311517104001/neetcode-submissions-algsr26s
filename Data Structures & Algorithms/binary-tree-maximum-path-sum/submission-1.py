# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # insights of the problem
    # 1) a path means each pair of adjacent nodes edges connecting ot htem 
    # 2) a node cannot appear in the sequence more than once
    # 3) The path does not necessarily need to include the root

    #  left and right should have the same height
    #  if so check they are connecting 
    #  get the sum
    #  get the max

    # intution I can start any node and end at anynode from the tree and neeed to return the maximum path sum
    # A path can have 1 split in the parent level but no more split in the child level
    #  to get the maximum from the tree I can try the post order as it start from the base to the root
    # 
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxi = float('-inf')

        def dfs(node):
            nonlocal maxi
            if not node:
                return 0

            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            maxi = max( maxi , left + right + node.val)
            return max(left,right) + node.val

        res = dfs(root)
        return max(res, maxi)
        