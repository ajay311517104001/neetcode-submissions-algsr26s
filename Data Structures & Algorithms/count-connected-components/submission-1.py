class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # build the graph
        visited = set()
        graph = collections.defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Here is my intituion we maitain a overall visited set
        # we initiate for each and every I try preforming the dfs traverstal
        # and add them to the visited

        def dfs(node):
            # to stop if there are any cycle
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)
            


        # when initiating the traversal I'll check for the node already exists 
        # in the set if yes i'll continue with the next node
        # the total dfs calls are the number of connected components in the graph
        count = 0
        for i in range(n):
            if i not in visited: 
                dfs(i)
                count+=1
        return count

        # Time Complexity:
        # Space complexity
                

        