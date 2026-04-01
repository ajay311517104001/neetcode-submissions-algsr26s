# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # optimal approach
    #  to maintain the positive and negative infinity
    # TC -> O(n), where n is the number of nodes in the tree
    # SC -> O(h), where h is the height of the tree O(log n)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root , left , right):
            if not root:
                return True
            # check if the root val stays in between the left and right
            if not left < root.val or not root.val < right:
                return False

            return (isValid(root.left , left , root.val) and
                    isValid(root.right , root.val , right))
            #  if yes call left 
            # if yes call right

        return isValid(root , float("-inf"),float("inf"))
        



    # Brute force Approach
    # left_check = staticmethod(lambda val , limit: val < limit)
    # right_check = staticmethod(lambda val , limit : val > limit)

    # # TC -> for every node in the tree, perfoming the left and right subtree validation repeatedly which is N.N times so O(N2)
    # # SC -> for everynode the tree use O(h) for every iteration which is O(log n)
    # # worst case if the tree is sqewed tree it O(n)
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     #  for in coming node
    #     if not root:
    #         return True
    #     # check that exist in negative and positive bound
    #     if (not self.isValid(root.left ,root.val , self.left_check ) or
    #         not self.isValid(root.right , root.val , self.right_check)):
    #         return False
    #     # check the left subtree by passing the right bound
    #     #  check the right subtree by passing it with right bound
    #     return self.isValidBST(root.left) and self.isValidBST(root.right)

        # is valid
        # if no root return the root
        # check if the root is in bound
        # if not return false

    def isValid(self, root , limit , check):
        if not root:
            return True
        if not check(root.val , limit):
            return False
        return (self.isValid(root.left ,limit , check) and
                self.isValid(root.right ,  limit , check))







    #     #  need to check if the height of the left subtree and height of the right subtree have difference by 1
    #     if not root:
    #         return True
    #     #  explore all the left subtree and all should less than 5
    #     # explore the right subtree and all should be greater than the root
    #     left = self.isValidLeft(root.left , root.val)
    #     right = self.isValidRight(root.right , root.val)
    #     if left and right:
    #        return (self.isValidBST(root.left) and
    #         self.isValidBST(root.right) )
    #     else:
    #         return False
    
    # def isValidLeft(self, root , median):
    #     if not root:
    #         return True
    #     if root.val >= median:
    #         return False
    #     return (self.isValidRight(root.left , median) and
    #         self.isValidRight(root.right , median))

    # def isValidRight(self, root, median):
    #     if not root:
    #         return True
    #     if root.val <= median:
    #         return False
    #     return (self.isValidRight(root.left , median) and
    #         self.isValidRight(root.right , median))




        # can we try the bfs?
        # enque = collections.deque([( root , root.val)])
        # while len(enque) > 0:
        #     for _ in range(len(enque)):
        #         node , rootVal = enque.pop()
        #         #  rule 1 node on left should be less than the root
        #         #  node on the right side should greater than the root
        #         if node:
        #             if node.left and node.val <= node.left.val :
        #                 return False
        #             if node.right and node.val >= node.right.val:
        #                 return False
        #             enque.append((node.left , rootVal))
        #             enque.append((node.left, rootVal))
                    
        # return True
