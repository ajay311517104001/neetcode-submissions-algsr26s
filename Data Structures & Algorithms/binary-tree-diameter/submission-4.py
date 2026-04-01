# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #revisiting this problem 
    # It takes a while to understand the problem first
    # The diameter of the tree is the longest path between two nodes in the tree
    #  It does't necessaraly pass thru the root node the longest path may exist in both left and right part of the tree
    
    # For every node in the tree, I need to find the diameter at that node and return the max diameter of the tree
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftH = self.findHeight(root.left)
        rightH = self.findHeight(root.right)
        diameter = leftH+rightH # since the diameter is not the count of the node it is the count of the edges should be total  nodes -1 in the longest path

        sub = max(self.diameterOfBinaryTree(root.left) , self.diameterOfBinaryTree(root.right))

        return max(diameter, sub)






    
    def findHeight(self,node):
        if not node:
            return 0

        return max(self.findHeight(node.left) , self.findHeight(node.right))+1 

        