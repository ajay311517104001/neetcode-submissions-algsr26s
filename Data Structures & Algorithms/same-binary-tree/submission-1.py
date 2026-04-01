# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # If the incoming nodes both None means P == Q
            if not p and not q:
                return True
            #  if one of the nodes are none or if values mismatch
            if (p is None or q is None) or p.val != q.val:
                return False
            return (self.isSameTree(p.left , q.left) and
              self.isSameTree(p.right,q.right))
        



