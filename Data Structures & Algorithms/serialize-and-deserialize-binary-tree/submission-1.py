# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        res = []
        enque = deque([root])
        while enque:
            node = enque.popleft()
            if not node:
                res.append('N')
            else:
                res.append(str(node.val))
                enque.append(node.left)
                enque.append(node.right)

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(int(vals[0]))
        enque = deque([root])
        val = 1
        while enque:
            node = enque.popleft()
            if vals[val] !="N":
                node.left = TreeNode(int(vals[val]))
                enque.append(node.left)
            val+=1
            if vals[val]!="N":
                node.right = TreeNode(int(vals[val]))
                enque.append(node.right)
            val+=1
        return root

