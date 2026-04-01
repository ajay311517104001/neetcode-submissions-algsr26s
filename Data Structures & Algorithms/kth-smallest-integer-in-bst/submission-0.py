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
        # SPACE -> O(H) + O(n)
        arr =[]
        if not root:
            return root
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)


        dfs(root)
        return arr[k-1]
        
        