# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=, NoDefault0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # i can do pre order which tells the root
        # i can do in order traversal 
        # basically 2 stings
        res = []

        def dfs(node):
            if not node:
                res.append('N,')
                return 
            res.append(str(node.val))
            res.append(',')
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        print("".join(res))
        return "".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # with the 2 incoming strings I can decode it and form an entire tree
        # build a tree wiht inorder and preorder traversal
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i+=1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

