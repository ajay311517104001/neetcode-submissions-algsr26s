class Solution:
    # Implementation in BFS
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS , COLUMNS = len(grid) , len(grid[0])
        directions = [[0,-1],[0,1],[1 ,0],[-1 , 0]]
        def bfs(r,c):
            enque = collections.deque()
            enque.append((r,c))
            grid[r][c] = 0
            count=1
            while enque:
                r,c = enque.popleft()
                for dr , dc in directions:
                    nrd = r+dr
                    ncd = c+dc
                    if (min(nrd,ncd) < 0 or nrd >= ROWS or ncd >= COLUMNS or grid[nrd][ncd] == 0):
                        continue
                    grid[nrd][ncd] = 0
                    enque.append((nrd,ncd))
                    count+=1
            return count

        max_island = 0
        for r  in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 1:
                    max_island = max(max_island, bfs(r,c))
        return max_island

        # Time Complexity: O(r.c), where r and c are the rows and columns 
        # Space Complexity: O(r.c) whre r and c are the rows and columns
