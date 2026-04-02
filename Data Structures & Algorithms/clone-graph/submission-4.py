"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hmap = {}
        def dfs(node):
            if node in hmap:
                return hmap[node]
            curr = Node(node.val)
            hmap[node] = curr
            for n in node.neighbors:
                hmap[node].neighbors.append(dfs(n))
            return hmap[node]

        return dfs(node)

        # if not node:
        #     return 
        # enque = deque()
        # enque.append(node)
        # map = {}
        # curr_node = Node(node.val)
        # map[node] = curr_node
        # while enque:
        #     n = enque.popleft()
        #     for n_ in n.neighbors:
        #         if n_ not in map:
        #             n_node = Node(n_.val)
        #             map[n_] = n_node
        #             enque.append(n_)
        #         map[n].neighbors.append(map[n_])
                
            

        # return curr_node
