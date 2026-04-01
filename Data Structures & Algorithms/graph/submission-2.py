class Graph:
    
    def __init__(self):
        # initialize the graph
        self.adj_list = defaultdict(set)


    def addEdge(self, src: int, dst: int) -> None:
        # add edges to the graph
        # check if the graph already as the node
        # if not adj_list[src]:
        self.adj_list[src].add(dst)
        if not self.adj_list[dst]:
            self.adj_list[dst] = set()


    def removeEdge(self, src: int, dst: int) -> bool:
        # remove the edge from the graph
        if self.adj_list[src] and dst in self.adj_list:
            self.adj_list[src].remove(dst)
            return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        # check if the path exists
        # either bfs or dfs works
        # impelement dfs

        visited = set()
        visited.add(src)
        def dfs(src,dst):
            if src == dst:
                return True

            for d in self.adj_list[src]:
                if d not in visited:
                    visited.add(d)
                    if dfs(d , dst):
                        return True
            visited.remove(src)
            return False
        return dfs(src , dst)

