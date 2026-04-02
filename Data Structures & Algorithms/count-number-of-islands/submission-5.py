class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS , COLUMNS = len(grid) , len(grid[0])
        visited = set()
        def bfs(r,c):
            queue = deque([(r,c)])
            visited.add((r,c))
            
            while queue:
                r,c = queue.popleft()
                
                for dr , dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    ndr , ndc = r +dr , c +dc
                    if (ndr,ndc) not in visited and 0 <= ndr < ROWS and 0 <= ndc < COLUMNS and grid[ndr][ndc] == '1':
                        queue.append((ndr,ndc))
                        visited.add((ndr,ndc))
            




            
        count =0
        for r in range(0,ROWS):
            for c in range(0,COLUMNS):
                if grid[r][c] == '1' and (r,c) not in visited:
                        count+=1
                        bfs(r,c)
        return count
        