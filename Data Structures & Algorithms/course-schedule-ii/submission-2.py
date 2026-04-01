class Solution:
    # Topological sort Implementation
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for c, p in prerequisites:
            graph[c].append(p)


        
        cycle , visited = set(), set()
        res =[]

        def dfs(crs):
            # when my recursion reaches the depeth it pass all the base condition and 
            # added itself to the cycle and it does not have any prereq so for loop skips and directly 
            # means we reached the depth so we mark that as visited and update the completed course in the res
            # and we undo the cycle and return 
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for p in graph[crs]:
                if not dfs(p):
                    return False
            visited.add(crs)
            res.append(crs)
            cycle.remove(crs)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
            
        