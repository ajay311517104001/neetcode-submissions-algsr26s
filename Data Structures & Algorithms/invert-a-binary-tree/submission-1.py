# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we commited an intresting mistake instead of swapping node we swapped the values

        #  what is our approach to invert a binary search tree
        def dfs(root):
            if not root:
                return 

            
            root.left , root.right = root.right , root.left
            
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root