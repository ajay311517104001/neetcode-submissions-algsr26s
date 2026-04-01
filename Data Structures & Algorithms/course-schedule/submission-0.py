class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, p in prerequisites:
            graph[course].append(p)
        
        visited = set()

        def dfs(c):
            if c in visited:
                return False
            if graph[c] == []:
                return True
            

            visited.add(c)
            for p in graph[c]:
                if not dfs(p):
                    return False
          
            visited.remove(c)
            graph[c] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True