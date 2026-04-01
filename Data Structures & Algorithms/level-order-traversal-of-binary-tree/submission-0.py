# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Implementing level order with DFS
        res = []
        # for visiting each and every new depth we will be creating the sub array and add the elements to it
        def dfs(root, depth):
            # if res length  == depth 
            if not root:
                return
            if len(res) == depth:
                res.append([])
            #  create a new sub array
            res[depth].append(root.val)
            # for the newly created sub array add the root value
            dfs(root.left , depth+1)
            dfs(root.right , depth + 1)
            # tracers dfs left
            # traverse dfs right

        dfs(root, 0)
        return res















        # # TC -> O(N), where n is the number of nodes in the tree
        # # sc- > O(N) . where N is the number of nodes pushed in enque
        # # result array
        # res = []
        # # if no root : return root
        # #  add the root to the enqueue
        # enque = deque() 
        # enque.append(root)
        # # iterate till if enqueue
        # while len(enque) > 0:
        # # subarray
        #     sub_arr = []
        #     for i in range(0,len(enque)):
        #         # pop the left
        #         node = enque.popleft()
        #         #  add it to the result array
        #         if node:
        #             sub_arr.append(node.val)
        #         # check if left add it to enque
        #             enque.append(node.left)
        #             enque.append(node.right)
        #     if len(sub_arr)>0:
        #         res.append(sub_arr)
        # return res

        # cehck if right add it to enque

        #  add the sub array to the result array