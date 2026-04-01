"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # DFS Implementation
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Cloning a graph is kind of cloning a binary tree
        # we definitely need the hashmap to map the cloned nodes 
        # the goal is to deep copy the graph with the dfs or bfs approach

        # first we recursively create the neighbour cloned node if the cloned node exists in the hmap we stop the recursion
        hmap ={}
        def dfs(node):
            # what would be my stop condition
            # if my cloned neighbour is already exists in the hmap means we return the cloned node
            if node in hmap:
                return hmap[node]

            c_node = Node(node.val)
            hmap[node] = c_node

            for n in node.neighbors:
                c_node.neighbors.append(dfs(n))
            return c_node

        return dfs(node) if node else node

         