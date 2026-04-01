# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Implementting dfs with counter inside
        def dfs(root, maxVal):
            if not root:
                return 0
            res = 1 if root.val>= maxVal else 0
            maxVal = max(root.val, maxVal)
            res = res + dfs(root.left , maxVal)
            res = res + dfs(root.right , maxVal)

            return res
        return dfs(root, root.val)




    #    Implementing dfs
    # # T.C -> O(n) where n is the number of nodes in the tree
    # # S.C -> O(h) recursion stack , height of the tree
    #     self.counter = 0
    #     def dfs(root , overall):
    #         #  leaf nodes or edge cases
    #         if not root:
    #             return 
    #         # condition
    #         if root.val >= overall:
    #             self.counter+=1
    #             overall = root.val
    #         #  traversal
    #         dfs(root.left , overall)
    #         dfs(root.right , overall)
    #     dfs(root, root.val)
    #     return self.counter


        # The incoming tree should not be override it - the interview is at risk

        # TC -> O(n), where n is the number of nodes present it the tree
        # SC -> O(n), where n is the space required for n nodes to store in enque
        # crete a enque to store the nodes
        # enque = collections.deque([root])
        # # counter to count the valid nodes
        # counter = 1
        # #  rootval = root.val
        # rootVal = root.val
        # #  counter = 1
        # while len(enque) > 0:
        # # outer loop check if enque is not null
        #     #  inner loop runs with the current present enque length
        #     for _ in range(len(enque)):
        #         #  get the root node value
        #         node = enque.popleft()
        #         #  compare the root node and the current node value to its left
        #         if node:
        #         #  if the root is and current node smaller update the root
        #             if node.left and node.left.val >= node.val:
        #                 counter+=1
        #             elif node.left:
        #                 node.left.val = node.val
        #         #  increment the count
        #         # else: update the left with the value of the current node
        #         #  if the root and the current node is smaller than the right
        #             if node.right and node.right.val >= node.val:
        #                 counter+=1
        #             elif node.right:
        #                 node.right.val = node.val
        #         #  update the curr 
        #         #  increment the count
        #         # else:udpate the value with the value of current node
        #             enque.append(node.left)
        #             enque.append(node.right)
        # return counter

        