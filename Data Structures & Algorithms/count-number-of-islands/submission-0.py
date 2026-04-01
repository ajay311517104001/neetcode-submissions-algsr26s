class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Total_island = 0
        ROWS , COLUMNS = len(grid), len(grid[0])
        visited =set()
        # what if the given land is empty?
        if len(grid) == 0:
            return Total_island

        # dfs to find the island
        def dfs(r,c):
            # check if the land is goind pre bound or out of bound and check if the land is not 1
            if (min(r,c) < 0 or r==ROWS or c == COLUMNS or grid[r][c] == '0' or (r,c) in visited):
                return 0

            visited.add((r,c))

            dfs(r+1 , c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

            return 1

        # need to check for each and every cell we have land means i 
        # we skip when it is already visisted and if its 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    Total_island+=dfs(r,c)
        return Total_island


        