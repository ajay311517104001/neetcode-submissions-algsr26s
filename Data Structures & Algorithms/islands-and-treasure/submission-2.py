class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        #  collect all the co ordinates of the treasure chest
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r,c))


        #    multi source bfs
        while queue:
            r,c = queue.popleft()

            for dr , dc in directions:
                nr = r + dr
                nc = c + dc
                if ( min(nr,nc)<0 or nr >= ROW or nc >= COL or grid[nr][nc] != 2147483647):
                    continue
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr,nc))

                


    