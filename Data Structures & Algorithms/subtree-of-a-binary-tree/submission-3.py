# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    
    def compare(self , root , subroot):
        # compare all the nodes values and its structure no more nodes or no less nodes
        if not root and not subroot:
            return True
        if (root is None or subroot is None) or root.val!=subroot.val:
            return False
        return (self.compare(root.left , subroot.left) and
        self.compare(root.right, subroot.right))

    def traverse(self,root,subroot):
        if not root:
            return 
        if root.val == subroot.val:
            # campare the main and the subtree
            if self.compare(root , subroot) == True:
                return True
        # continue recursion
        return (self.traverse(root.left , subroot) or
        self.traverse(root.right , subroot))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Implementation with recursion
        # first need to find the start root it may be more than one root 
        #  need to traverse the tree to determine the right node
        if self.traverse(root, subRoot) == True:
            return True
        else:
            return False
        


        
        





        #  Height of the left tree and right tree should be same
        # elements of the tree should be the same
        # same structure should be the same

        #  find the subroot's root in the main tree
        # once you find the root compare its nodes

        # TC -> O(N), where N is the number of nodes in the main tree
        # SC -> O(N), where N is the nodes which matches the subtree root
        # stack = [root]
        # start_root = []
        # while stack:
        #     node = stack.pop()
        #     if not node:
        #         continue
        #     if node and node.val == subRoot.val:
        #         start_root.append(node)
            
        #     stack.append(node.left)
        #     stack.append(node.right)

        # # TC -> O(N X S) where n is the matched nodes S is nodes in the subtree
        # # space -> O(N) space to store the main tree nodes and the subtree nodes
  
        # for n in start_root:
        #     stackp = [n]
        #     stackq = [subRoot]
        #     isMatch = True
        #     while stackp and stackq:
        #         node1 = stackp.pop()
        #         node2 = stackq.pop()
        #         if not node1 and not node2:
        #             continue
        #         if (node1 is None or node2 is None) or node1.val != node2.val:
        #             isMatch = False
        #             break
        #         stackp.append(node1.left)
        #         stackp.append(node1.right)
        #         stackq.append(node2.left)
        #         stackq.append(node2.right)
        #     if isMatch:
        #         return True
        # return False
        
        


