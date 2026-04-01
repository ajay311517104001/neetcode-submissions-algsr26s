# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we commited an intresting mistake instead of swapping node we swapped the values

        # TC -> O(n) where n is the number of nodes in the bst
        # SC -> O(H), where h is the height of the binary search tree m
        # In skewed tree, it will be O(n) 
        #  what is our approach to invert a binary search tree
        # def dfs(root):
        #     if not root:
        #         return 

            
        #     root.left , root.right = root.right , root.left
            
        #     dfs(root.left)
        #     dfs(root.right)

        # dfs(root)
        # return root

        #  we can also use stack approach to invert a binary tree
        if not root:
            return root
        stack = [root]
        # till stack exists
        while stack:
        #  get the root node from stack
            node = stack.pop()
            node.left , node.right = node.right , node.left
        # change invert its left and right poisions
        # check if the root has left 
            if node.left:
                stack.append(node.left)
        #  add that to stack
            if node.right:
                stack.append(node.right)
        # cehck if it has the right node
        # add to stack
        return root