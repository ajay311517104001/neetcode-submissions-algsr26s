class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # since it is an undirected graph, the opposite nodes are neighbour to each other
        # criteria to tell the graph is a tree, it is not a binary search tree, its graph tree
     

        # constraints for a perfect graph tree
        # there are no duplicate edges between the same node 
        # all the nodes in the tree should be connected (if not it is considered as forest)
        # Acyclic (no cycles i the graph)
        # we can start from any node and we should visit all th nodes present in the graph

        # build a undirected graph in a map
        graph = defaultdict(list)
        visited = set()
        # check for the cycles by traversing and check all the nodes are visited
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)


        def dfs(n, parent):
            if n in visited:
                return False

            visited.add(n)
            for neighbor in graph[n]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor , n):
                    return False
            return True


        return   dfs(0,-1) and len(visited) == n