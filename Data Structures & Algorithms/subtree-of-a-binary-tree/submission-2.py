# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #  Height of the left tree and right tree should be same
        # elements of the tree should be the same
        # same structure should be the same

        #  find the subroot's root in the main tree
        # once you find the root compare its nodes
        stack = [root]
        start_root = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node and node.val == subRoot.val:
                start_root.append(node)
            
            stack.append(node.left)
            stack.append(node.right)
        res = []
        for n in start_root:
            stackp = [n]
            stackq = [subRoot]
            isMatch = True
            while stackp and stackq:
                node1 = stackp.pop()
                node2 = stackq.pop()
                if not node1 and not node2:
                    continue
                if (node1 is None or node2 is None) or node1.val != node2.val:
                    isMatch = False
                    break
                stackp.append(node1.left)
                stackp.append(node1.right)
                stackq.append(node2.left)
                stackq.append(node2.right)
            if isMatch:
                return True
        return False
        
        


