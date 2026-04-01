class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Total_island = 0
        if len(grid) == 0:
            return Total_island
        ROWS , COLUMNS = len(grid), len(grid[0])
        # visited =set()
        # Note:
        # Alternate approach would be : Insted of making it in the set and using extra space
        # we can reduce the space by mutating the 1 as O so that even if the for loop encounters 
        # it will not take because it looks for value 1


        # what if the given land is empty?
        

        # dfs to find the island
        def dfs(r,c):
            # check if the land is goind pre bound or out of bound and check if the land is not 1
            directions = [[1,0], [-1,0], [0,-1], [0,1]]
            # if (min(r,c) < 0 or r==ROWS or c == COLUMNS or grid[r][c] == '0' or (r,c) in visited):
            if (min(r,c) < 0 or r==ROWS or c == COLUMNS or grid[r][c] == '0'):
                return 0

            # visited.add((r,c))
            grid[r][c] = '0'

            # dfs(r+1 , c)
            # dfs(r-1,c)
            # dfs(r,c-1)
            # dfs(r,c+1)

            for dr , dc in directions:
                dfs(r+dr , c+dc)

            return 1

        # need to check for each and every cell we have land means i 
        # we skip when it is already visisted and if its 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                # if grid[r][c] == "1" and (r,c) not in visited:
                if grid[r][c] == "1" and (r,c):
                    dfs(r,c)
                    Total_island+=1
        return Total_island


        