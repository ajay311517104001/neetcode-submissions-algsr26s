# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # # If the incoming nodes both None means P == Q
            # if not p and not q:
            #     return True
            # #  if one of the nodes are none or if values mismatch
            # if (p is None or q is None) or p.val != q.val:
            #     return False
            # return (self.isSameTree(p.left , q.left) and
            #   self.isSameTree(p.right,q.right))

            #   TC -> O(p+q) where p and q are number of nodes for a given subtrees
            # SC -> O(h) where h is the height of the subtree 

            stackp = [p]
            stackq =[q]

            while stackp and stackq:
                node1=stackp.pop()
                node2=stackq.pop()

                if not node1 and not node2:
                    continue
                if (node1 is None or node2 is None) or node1.val != node2.val:
                    return False

                stackp.append(node1.left)
                stackp.append(node1.right)
                stackq.append(node2.left)
                stackq.append(node2.right)


            return True
                

        



