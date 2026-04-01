# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        diameter = left+right
        sub = max(self.diameterOfBinaryTree(root.left) , self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)



    def getHeight(self, node):
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)

        return max(left, right)+1
