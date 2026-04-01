# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse the tree in sorterd order add them in an array 
        #  return the value based on the index
        # TC -> O(N)
        # SPACE -> O(H) + O(n) -> O(n), since it is greater


        # How it can be done in iterative approach

        enque = collections.deque()
        counter = 0
        # 
        while True:
            while root:
                enque.append(root)
                root = root.left
            counter+=1
            node = enque.pop()
            if counter == k:
                return node.val
            root = node.right



        # node = None
        # if not root:
        #     return root
        # def dfs(root , counter):
        #     if not root:
        #         return 0
        #     if counter == k:
        #         node = root

        #     counter = dfs(root.left , counter)
        #     counter = dfs(root.right , counter)
        #     counter +=1
            
        #     return counter
        

            
             


        # dfs(root, 0 )
        # return root.val


        # arr =[]
        # if not root:
        #     return root
        # def dfs(root):
        #     if not root:
        #         return 
        #     dfs(root.left)
        #     arr.append(root.val)
        #     dfs(root.right)


        # dfs(root)
        # return arr[k-1]
        
        