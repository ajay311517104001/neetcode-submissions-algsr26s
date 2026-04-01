# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Questions:
# 1) can the nodes contains duplicates
# 2) can the root node be empty
#3) can I get only one node
#4) can expect a skewed tree?

# I need to validate the given bst tree and return the bool value
# The curr node should be greater the all the nodes in the left subtree and should be less than the all the node in the right subtree
# for each and every node we need to check the above condition

# T.c -> O(n)2 , since we perform the for each and every node validation for the left and right subtree , in worst case it is n*n -> O(n)^2
# S.c -> O(n)or O(h) , recursion stack the peak auxiliary memory is O(n) at a time.

# Input ->  root node
# output-> boolean value

class Solution:
    leftCheck = staticmethod(lambda nodeVal,val: nodeVal >= val)
    rightCheck = staticmethod(lambda nodeVal,val: nodeVal <= val )
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.isValid(root.left , root.val , self.leftCheck)
        right = self.isValid(root.right, root.val , self.rightCheck)

        if not left or not right:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    
    def isValid(self,node, val , check):
        if not node:
            return True
        
        if check(node.val , val):
            return False
        
        return self.isValid(node.left , val , check) and self.isValid(node.right , val , check)
    
    # def isValidright(self,node, val):
    #     if not node:
    #         return True
        
    #     if node.val <= val:
    #         return False
        
    #     return self.isValidright(node.left, val) and self.isValidright(node.right , val)
        