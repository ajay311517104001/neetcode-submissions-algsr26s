class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Here is the thing, I need to return the order course completed 
        # do as deep as possible for the prerequisites, once you reach the depth mark the corse as completed and maintain the completed course order
        # It is basically a graph problem can be solved with the Dfs approach


        graph= defaultdict(list)

        for c,p in prerequisites:
            graph[c].append(p)

        res =[]
        visited = set()
        def dfs(course):
            if not graph[course]:
                if course not in res:
                    res.append(course)
                return True
            if course in visited:
                return False
            # mark the course to visited to avoid duplicates

            visited.add(course)
            for p in graph[course]:
                if p not in res:
                    if not dfs(p):
                        return False
            res.append(course)
            visited.remove(course)
            graph[course] = []
            return True


        for c in range(numCourses):
            
            if not dfs(c):
                return []
            
        return res
        