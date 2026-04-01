# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #  basically give priority to to the right sub tree for every node traversal

        #  if the root is none 
        #  return the root

        #  if right take right print all right nodes
        # what if the right sub tree does not exist and the left subtree exists
        #  traverse left sub tree and explore all the nodes in the right
        # it should cover all the maximum depeth of the tree


        # implementing regular bfs
        #  have root in enque

        #  declare res
        res = []
        enque = collections.deque()
        enque.append((0,root))
        level = 0
        while len(enque) > 0:
            for _ in range(len(enque)):
                level , node = enque.popleft()
                if node:
                # check if it is the last element in the enque
                    if len(res) > level:
                        res[level] = node.val 
                    else:
                        res.insert(level, node.val)
                    level+=1
                    enque.append((level,node.left ))
                    enque.append((level,node.right))
                #  add it to res
                # else get the children add it to the enque
            
            
        return res


