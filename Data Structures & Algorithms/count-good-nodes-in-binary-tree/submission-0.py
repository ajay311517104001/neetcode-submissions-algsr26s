# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # crete a enque to store the nodes
        enque = collections.deque([root])
        # counter to count the valid nodes
        counter = 1
        #  rootval = root.val
        rootVal = root.val
        #  counter = 1
        while len(enque) > 0:
        # outer loop check if enque is not null
            #  inner loop runs with the current present enque length
            for _ in range(len(enque)):
                #  get the root node value
                node = enque.popleft()
                #  compare the root node and the current node value to its left
                if node:
                #  if the root is and current node smaller update the root
                    if node.left and node.left.val >= node.val:
                        counter+=1
                    elif node.left:
                        node.left.val = node.val
                #  increment the count
                # else: update the left with the value of the current node
                #  if the root and the current node is smaller than the right
                    if node.right and node.right.val >= node.val:
                        counter+=1
                    elif node.right:
                        node.right.val = node.val
                #  update the curr 
                #  increment the count
                # else:udpate the value with the value of current node
                    enque.append(node.left)
                    enque.append(node.right)
        return counter

        