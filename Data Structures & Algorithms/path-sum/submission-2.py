# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root , total , targetSum):
        # More cleaner an simple solution
            if not root:
                return False
            # check if not root return false
            total+=root.val
            # for the incoming node update the total
            if not root.left and not root.right:
                return total == targetSum
            #  check if the node left and right has none
            #  check if the total == to the targetSum
            return dfs(root.left , total , targetSum) or dfs(root.right, total , targetSum)

        return dfs(root , 0 , targetSum)
        #  only one path is valid so either left or right subtree path is valid



        # def dfs(root , total , targetSum):
        #     if not root:
        #         return False
        #     if root and not root.left and not root.right:
        #         # reached end of the leaf
        #         total+=root.val
        #         if total == targetSum:
        #             return True
        #         return False
            
        #     total+= root.val
            
        #     if dfs(root.left , total , targetSum):
        #         return True
        #     if dfs(root.right , total , targetSum):
        #         return True
        #     return False
        # return dfs(root,0, targetSum)
        
