"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # Implementation in BFS
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #I need to visit it in the layer wise
        if not node:
            return node
        # we can have the hashmap
        hmap ={}
        enque = collections.deque()
        hmap[node] = Node(node.val)
        enque.append(node)
        while enque:
            curr = enque.popleft()
            for n in curr.neighbors:
                if n not in hmap:
                    cn_node = Node(n.val)
                    hmap[n] = cn_node
                    enque.append(n)
                hmap[curr].neighbors.append(hmap[n])
                
        return hmap[node]

        