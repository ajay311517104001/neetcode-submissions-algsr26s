# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

        
       
        

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # p and q
        # Basically if p is < root < q return root
        if root and p and q:
            if p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left , p , q)
            elif p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right , p , q)
            else:
                return root
        
        #  if p and q are smaller than root check left subtree
        #  if p and q greater than root check right subtree












